"""Bounded, pinned FARS 2024 ARF three-table ingestion with crash-safe views."""
from __future__ import annotations
import argparse,csv,datetime,decimal,hashlib,io,json,pathlib,re,shutil,urllib.request,zipfile
import duckdb
HERE=pathlib.Path(__file__).resolve().parent
SCHEMA=json.loads((HERE/'schema.json').read_text());LOCK=json.loads((HERE/'source-lock.json').read_text())
DATA_TABLES=list(SCHEMA)
LICENSE='Public information; redistribution permitted by NHTSA website Ownership policy'
MANUAL='https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813794'
def require(ok,message):
 if not ok:raise ValueError(message)
def sha(path):
 with pathlib.Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def save(path,value):path.write_text(json.dumps(value,indent=2,default=str)+'\n',encoding='utf-8')
def q(s):return '"'+s.replace('"','""')+'"'
def lit(s):return "'"+str(s).replace("'","''")+"'"
def connection(path,readonly=False):return duckdb.connect(str(path),read_only=readonly,config={'memory_limit':'256MiB','threads':'1','max_temp_directory_size':'256MiB','preserve_insertion_order':'true'})
def typed(value,column):
 if column['type']=='VARCHAR':return value
 if value=='':
  require(column.get('source_blank_count',0)>0,'Unexpected numeric blank '+column['name']);return None
 if column['type']=='BIGINT':
  require(bool(re.fullmatch(r'-?[0-9]+',value)),'Invalid integer '+column['name']);return int(value)
 require(bool(re.fullmatch(r'-?[0-9]+(?:\.[0-9]{1,12})?',value)),'Invalid or overprecision decimal '+column['name']);return decimal.Decimal(value)
def verify_archive(path):
 require(path.stat().st_size==LOCK['archive']['bytes'] and sha(path)==LOCK['archive']['sha256'],'Archive size/SHA mismatch')
 with zipfile.ZipFile(path) as z:
  infos=z.infolist();require(len({x.filename for x in infos})==len(infos),'Duplicate ZIP members')
  require(sum(x.file_size for x in infos)<=512*1024**2,'Inflated ZIP exceeds cap')
  require([(x.filename,x.file_size) for x in infos]==[(m['name'],m['bytes']) for m in LOCK['archive']['members']],'ZIP inventory mismatch')
def download(path):
 require(path.resolve().is_relative_to(HERE.resolve()),'Download must stay within guarded repository')
 if path.exists():verify_archive(path);return
 path.parent.mkdir(parents=True,exist_ok=True)
 partial=path.with_name(path.name+'.partial');require(not partial.exists(),'Retained partial download; inspect before retry')
 with urllib.request.urlopen(LOCK['archive']['url'],timeout=45) as src,partial.open('xb') as out:
  total=0
  while b:=src.read(1024*1024):
   total+=len(b);require(total<=LOCK['archive']['bytes'],'Oversize download');out.write(b)
 verify_archive(partial);partial.rename(path)
def extract(archive,table):
 spec=SCHEMA[table];target=HERE/'data'/(table+'-source.csv')
 target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():require(sha(target)==spec['source_sha256'],'Cached source hash mismatch');return target
 partial=target.with_name(target.name+'.partial');require(not partial.exists(),'Retained partial extraction; inspect before retry')
 with zipfile.ZipFile(archive) as z,z.open(spec['source_file']) as src,partial.open('xb') as out:shutil.copyfileobj(src,out,1024*1024)
 require(sha(partial)==spec['source_sha256'],'Extracted source hash mismatch');partial.rename(target);return target
def crash_sql():
 return '''WITH v AS (SELECT state,st_case,count(*) AS vehicle_records,sum(deaths) AS in_transport_vehicle_fatalities FROM vehicle GROUP BY state,st_case),
 p AS (SELECT state,st_case,count(*) AS person_records,count(*) FILTER(WHERE inj_sev=4) AS person_fatalities,
 count(*) FILTER(WHERE per_typ IN (1,2,9)) AS in_transport_people,
 count(*) FILTER(WHERE per_typ=3) AS parked_working_vehicle_people,
 count(*) FILTER(WHERE veh_no=0) AS nonoccupant_people,
 count(*) FILTER(WHERE inj_sev=4 AND veh_no=0) AS nonoccupant_fatalities,
 count(*) FILTER(WHERE inj_sev=4 AND per_typ=3) AS parked_working_vehicle_fatalities
 FROM person GROUP BY state,st_case)
 SELECT a.*,v.vehicle_records,v.in_transport_vehicle_fatalities,p.person_records,p.person_fatalities,
 p.in_transport_people,p.parked_working_vehicle_people,p.nonoccupant_people,p.nonoccupant_fatalities,p.parked_working_vehicle_fatalities,
 CASE WHEN a.latitude IN (77.7777,88.8888,99.9999) THEN NULL ELSE a.latitude END AS latitude_degrees,
 CASE WHEN a.longitud IN (777.7777,888.8888,999.9999) THEN NULL ELSE a.longitud END AS longitude_degrees
 FROM accident a LEFT JOIN v USING(state,st_case) LEFT JOIN p USING(state,st_case)'''
def people_sql():
 return '''SELECT *,CASE WHEN age BETWEEN 0 AND 120 THEN age ELSE NULL END AS age_years,
 CASE WHEN alc_res BETWEEN 0 AND 939 THEN CAST(alc_res*CAST(0.001 AS DECIMAL(4,3)) AS DECIMAL(6,3)) ELSE NULL END AS measured_bac_g_dl,
 alc_res=940 AS bac_top_coded_at_094_or_more,
 CASE WHEN inj_sev=4 THEN true WHEN inj_sev IN(0,1,2,3,6) THEN false ELSE NULL END AS fatal_injury_recorded
 FROM person'''
def unambiguous_labels_sql():
 return '''SELECT table_name,column_name,context_column,context_value,code,min(label) AS label
 FROM code_labels GROUP BY table_name,column_name,context_column,context_value,code HAVING count(*)=1'''
def labels(con):
 # Explicit finite fields, from actual paired source labels; no exploratory 2000-value truncation.
 selected={'accident':['state','county','city','month','day_week','rur_urb','func_sys','lgt_cond','weather','man_coll','harm_ev','rel_road'],
 'vehicle':['make','mak_mod','body_typ','hit_run','dr_pres','dr_drink','speedrel','rollover'],
 'person':['per_typ','inj_sev','sex','age','alc_status','atst_typ','alc_res','drinking','drugs','dstatus']}
 con.execute('CREATE TABLE code_labels(table_name VARCHAR,column_name VARCHAR,context_column VARCHAR,context_value BIGINT,code BIGINT,label VARCHAR)')
 for table,fields in selected.items():
  for field in fields:
   context='state' if field in ('county','city') else None
   con.execute(f'INSERT INTO code_labels SELECT DISTINCT {lit(table)},{lit(field)},{lit(context or "")},{q(context) if context else "0"},{q(field)},{q(field+"name")} FROM {q(table)}')
 return selected
def checks(con,check_counts=True):
 result={}
 def zero(name,sql):
  n=con.execute(sql).fetchone()[0];result[name]=n;require(n==0,name+': '+str(n)+' violations')
 for table,spec in SCHEMA.items():
  if check_counts:require(con.execute(f'SELECT count(*) FROM {table}').fetchone()[0]==spec['rows'],'Row count '+table)
  keys=','.join(spec['key']);zero(table+' duplicate key',f'SELECT count(*) FROM (SELECT {keys},count(*) n FROM {table} GROUP BY ALL HAVING n<>1)')
  zero(table+' missing key',f'SELECT count(*) FROM {table} WHERE '+' OR '.join(q(c)+' IS NULL' for c in spec['key']))
 for t in ['person','vehicle']:zero(t+' crash reference',f'SELECT count(*) FROM {t} x LEFT JOIN accident a USING(state,st_case) WHERE a.st_case IS NULL')
 zero('in-transport occupant vehicle reference','SELECT count(*) FROM person p LEFT JOIN vehicle v USING(state,st_case,veh_no) WHERE p.per_typ IN(1,2,9) AND v.veh_no IS NULL')
 zero('person vehicle number semantics','SELECT count(*) FROM person WHERE (per_typ IN(1,2,3,9) AND veh_no<=0) OR (per_typ NOT IN(1,2,3,9) AND veh_no<>0)')
 zero('parked vehicle collision with transport key','SELECT count(*) FROM person p JOIN vehicle v USING(state,st_case,veh_no) WHERE p.per_typ=3')
 zero('crash identity and vintage','SELECT count(*) FROM accident WHERE year<>2024 OR state<>st_case//10000 OR fatals<1 OR ve_forms<1')
 zero('person type codes','SELECT count(*) FROM person WHERE per_typ NOT IN(1,2,3,4,5,6,7,8,9,10,19)')
 zero('injury codes','SELECT count(*) FROM person WHERE inj_sev NOT IN(0,1,2,3,4,5,6,9)')
 zero('age codes','SELECT count(*) FROM person WHERE NOT(age BETWEEN 0 AND 120 OR age IN(998,999))')
 zero('alcohol result codes','SELECT count(*) FROM person WHERE NOT(alc_res BETWEEN 0 AND 940 OR alc_res IN(995,996,997,998,999))')
 zero('latitude codes','SELECT count(*) FROM accident WHERE NOT(latitude BETWEEN -90 AND 90 OR latitude=99.9999)')
 zero('longitude codes','SELECT count(*) FROM accident WHERE NOT(longitud BETWEEN -180 AND 180 OR longitud IN(777.7777,888.8888,999.9999))')
 zero('duplicate code-label tuple','SELECT count(*) FROM (SELECT table_name,column_name,context_column,context_value,code,label,count(*) n FROM code_labels GROUP BY ALL HAVING n<>1)')
 zero('safe crash fatality/count reconciliation','SELECT count(*) FROM crashes WHERE person_fatalities<>fatals OR vehicle_records<>ve_forms OR person_records<>persons+peds OR in_transport_people<>permvit OR parked_working_vehicle_people+nonoccupant_people<>pernotmvit OR in_transport_vehicle_fatalities+parked_working_vehicle_fatalities+nonoccupant_fatalities<>fatals')
 require(con.execute('SELECT count(*) FROM crashes').fetchone()[0]==con.execute('SELECT count(*) FROM accident').fetchone()[0],'Crash-view join inflation')
 return result
def compare_source(con,archive):
 proof={}
 with zipfile.ZipFile(archive) as z:
  for table,spec in SCHEMA.items():
   n=0;h=hashlib.sha256();nulls=[0]*len(spec['columns']);samples=[]
   with z.open(spec['source_file']) as src:
    reader=csv.reader(io.TextIOWrapper(src,encoding='utf-8-sig',newline=''),strict=True)
    require(next(reader)==[c['source_header'] for c in spec['columns']],'CSV header mismatch')
    cursor=con.execute(f'SELECT * FROM {table} ORDER BY rowid')
    for batch in iter(lambda:cursor.fetchmany(512),[]):
     for actual in batch:
      row=next(reader,None);require(row is not None and len(row)==len(spec['columns']),'CSV width/count mismatch')
      expected=tuple(typed(v,c) for v,c in zip(row,spec['columns']));require(actual==expected,f'Source cell mismatch {table} record {n+1}')
      n+=1;h.update(json.dumps(actual,ensure_ascii=False,default=str,separators=(',',':')).encode()+b'\n');nulls=[a+int(v is None) for a,v in zip(nulls,actual)]
      if n in (1,spec['rows']//2,spec['rows']):samples.append({'source_record':n,'source':row,'typed':actual})
    require(next(reader,None) is None and n==spec['rows'],'CSV final row count mismatch')
   proof[table]={'rows':n,'all_cells_equal':True,'typed_rows_sha256':h.hexdigest(),'null_counts':dict(zip([c['name'] for c in spec['columns']],nulls)),'samples':samples}
 return proof
def build(archive,out):
 from datapond_build import ensure_metadata,build_columns_table,export_dictionary
 if out.exists():raise FileExistsError('Use a new output directory; prior evidence is retained')
 require(out.resolve().is_relative_to(HERE.resolve()),'Output must stay within guarded repository');verify_archive(archive)
 require(shutil.disk_usage(HERE).free>=10*1024**3,'Free disk below 10 GiB');out.mkdir(parents=True)
 con=connection(out/'fars.duckdb')
 try:
  for table,spec in SCHEMA.items():
   path=extract(archive,table);cols=','.join(lit(c['source_header'])+":'VARCHAR'" for c in spec['columns']);kept='['+','.join(lit(c['source_header']) for c in spec['columns'])+']'
   cast=','.join((q(c['source_header']) if c['type']=='VARCHAR' else 'CAST(NULLIF('+q(c['source_header'])+",'') AS "+c['type']+')')+' AS '+q(c['name']) for c in spec['columns'])
   con.execute(f'CREATE TABLE {table} AS SELECT {cast} FROM read_csv({lit(path)},columns={{{cols}}},header=true,nullstr=\'\',force_not_null={kept},strict_mode=true,ignore_errors=false,parallel=false)')
   print(table,con.execute(f'SELECT count(*) FROM {table}').fetchone()[0],flush=True)
  label_fields=labels(con);con.execute('CREATE VIEW crashes AS '+crash_sql());con.execute('CREATE VIEW people AS '+people_sql());con.execute('CREATE VIEW unambiguous_code_labels AS '+unambiguous_labels_sql())
  validation=checks(con);proof=compare_source(con,archive)
  tables=[*SCHEMA,'code_labels'];descs={t:s['description'] for t,s in SCHEMA.items()};descs['code_labels']='Distinct observed code/label tuples for 30 selected fields; county/city scoped by state. Four city codes have multiple source labels. Use unambiguous_code_labels for unique lookups. MAK_MOD is combined make/model; this is not a full/historical catalog.'
  ensure_metadata(con,descriptions=descs,tables=tables,source_url=LOCK['archive']['url'],license=LICENSE,replace=True)
  for c in ['source_file','source_sha256','source_release']:con.execute('ALTER TABLE _metadata ADD COLUMN '+c+' VARCHAR')
  for table in tables:con.execute('UPDATE _metadata SET source_file=?,source_sha256=?,source_release=? WHERE table_name=?',[SCHEMA[table]['source_file'] if table in SCHEMA else 'Derived from accident/vehicle/person paired NAME columns',SCHEMA[table]['source_sha256'] if table in SCHEMA else LOCK['archive']['sha256'],LOCK['release'],table])
  build_columns_table(con,tables=tables,join_hints={'st_case':'Within this year: join accident by state/st_case; aggregate child tables before crash-level joins.','veh_no':'Join transport occupants by state/st_case/veh_no; 0 denotes nonoccupants and PER_TYP=3 belongs to omitted Parkwork.','per_no':'Person identity requires state/st_case/veh_no/per_no.','code':'code_labels has variants. Join unambiguous_code_labels using table_name/column_name/context_column/context_value/code; ambiguous city codes are excluded.'})
  for c in ['description','source_header','manual_url']:con.execute('ALTER TABLE _columns ADD COLUMN '+c+' VARCHAR')
  for table,spec in SCHEMA.items():
   for c in spec['columns']:con.execute('UPDATE _columns SET description=?,source_header=?,manual_url=? WHERE table_name=? AND column_name=?',[c['description'],c['source_header'],MANUAL+'#page='+str(c['manual_pdf_page']),table,c['name']])
  ld={'table_name':'Raw source table name.','column_name':'Raw numeric code column.','context_column':'Additional context: state, or empty string when global.','context_value':'Numeric context value; 0 means no context.','code':'Original integer source code, including unknown/inapplicable categories.','label':'Exact paired source NAME value.'}
  for c,d in ld.items():con.execute('UPDATE _columns SET description=?,source_header=?,manual_url=? WHERE table_name=\'code_labels\' AND column_name=?',[d,'Derived',MANUAL,c])
  export_dictionary(con,out/'DICTIONARY.md',title='FARS 2024 Annual Report File dictionary',tables=tables,intro=['Source: NHTSA 2024 national Annual Report File, first release 2026-04-01.','407 original source columns are preserved; code_labels has six derived columns. Views are documented in README.'])
  with (out/'DICTIONARY.md').open('a',encoding='utf-8') as f:
   f.write('\n## Exact definitions and manual pages\n\n')
   for table,spec in SCHEMA.items():
    f.write('### '+table+'\n\n| Column | Original header | Definition | Manual PDF page |\n|---|---|---|---|\n')
    for c in spec['columns']:f.write('| '+c['name']+' | '+c['source_header']+' | '+c['description'].replace('|','\\|')+' | '+str(c['manual_pdf_page'])+' |\n')
    f.write('\n')
  con.execute('CHECKPOINT')
 finally:con.close()
 with connection(out/'fars.duckdb',True) as con:
  require(checks(con)==validation,'Persisted validation changed');persisted=compare_source(con,archive);require(proof==persisted,'Persisted source comparison changed')
  counts={t:con.execute('SELECT count(*) FROM '+t).fetchone()[0] for t in [*SCHEMA,'code_labels']}
 report={'status':'validated_local_not_published','release':LOCK['release'],'built_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duckdb':duckdb.__version__,'database_sha256':sha(out/'fars.duckdb'),'database_bytes':(out/'fars.duckdb').stat().st_size,'rows':sum(counts.values()),'data_tables':4,'dictionary_columns':413,'table_counts':counts,'label_fields':label_fields,'validation':validation,'source_comparison':persisted,'all_cells_reverified_after_read_only_reopen':True,'build_input_sha256':{n:sha(HERE/n) for n in ['fars.py','schema.json','source-lock.json','pyproject.toml']}}
 save(out/'build-report.json',report);print(json.dumps({k:v for k,v in report.items() if k not in ('source_comparison','validation')},indent=2),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--archive',type=pathlib.Path,default=HERE/'data/FARS2024NationalCSV.zip');p.add_argument('--download',action='store_true');a=p.parse_args()
 if a.download:download(a.archive)
 build(a.archive,a.output)
