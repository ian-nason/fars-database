"""Read-only release checks independently enumerate schema, missingness, labels and view semantics."""
import csv,importlib.metadata,inspect,io,json,pathlib,platform,re,sys,zipfile
import datapond_build
import fars
def nonoccupant_blank_checks(con,columns=None):
 columns=columns if columns is not None else fars.SCHEMA['person']['columns'];result={}
 for c in columns:
  if c['type']!='VARCHAR' and c['source_blank_count']:
   name='numeric blanks confined exactly to nonoccupants: '+c['name']
   count=con.execute('SELECT count(*) FROM person WHERE ('+fars.q(c['name'])+' IS NULL) IS DISTINCT FROM (veh_no=0)').fetchone()[0]
   result[name]=count;fars.require(count==0,name+': '+str(count))
 return result
def validate(con,report):
 checks={}
 def zero(name,sql):
  n=con.execute(sql).fetchone()[0];checks[name]=n;fars.require(n==0,name+': '+str(n))
 for t,s in fars.SCHEMA.items():
  fars.require(con.execute('DESCRIBE '+t).fetchall() and [(x[0],x[1]) for x in con.execute('DESCRIBE '+t).fetchall()]==[(c['name'],c['type']) for c in s['columns']],'Schema '+t)
  fars.require(con.execute('SELECT row_count,column_count,source_file,source_sha256,source_release,license,source_url FROM _metadata WHERE table_name=?',[t]).fetchone()==(s['rows'],len(s['columns']),s['source_file'],s['source_sha256'],fars.LOCK['release'],fars.LICENSE,fars.LOCK['archive']['url']),'Metadata '+t)
  for c in s['columns']:
   nulls=c['source_blank_count'] if c['type']!='VARCHAR' else 0
   got=con.execute('SELECT data_type,source_file,null_pct,description,source_header,manual_url FROM _columns WHERE table_name=? AND column_name=?',[t,c['name']]).fetchone()
   fars.require(got==(c['type'],s['source_file'],round(100*nulls/s['rows'],1),c['description'],c['source_header'],fars.MANUAL+'#page='+str(c['manual_pdf_page'])),'Dictionary '+t+'.'+c['name'])
   fars.require(con.execute(f'SELECT count(*) FILTER(WHERE {fars.q(c["name"])} IS NULL) FROM {t}').fetchone()[0]==nulls,'NULL count '+t+'.'+c['name'])
 for t in ['vehicle','person']:
  common=(set(c['name'] for c in fars.SCHEMA[t]['columns'])&set(c['name'] for c in fars.SCHEMA['accident']['columns']))-{'state','st_case'}
  zero('consistent copied crash fields in '+t,'SELECT count(*) FROM '+t+' x JOIN accident a USING(state,st_case) WHERE '+' OR '.join('x.'+fars.q(c)+' IS DISTINCT FROM a.'+fars.q(c) for c in sorted(common)))
 checks.update(nonoccupant_blank_checks(con))
 zero('all age NULL mappings','SELECT count(*) FROM people WHERE age_years IS DISTINCT FROM CASE WHEN age IN(998,999) THEN NULL ELSE age END')
 zero('all BAC mappings','SELECT count(*) FROM people WHERE measured_bac_g_dl IS DISTINCT FROM CASE WHEN alc_res BETWEEN 0 AND 939 THEN CAST(alc_res*CAST(0.001 AS DECIMAL(4,3)) AS DECIMAL(6,3)) ELSE NULL END OR bac_top_coded_at_094_or_more IS DISTINCT FROM (alc_res=940)')
 zero('all coordinate NULL mappings','SELECT count(*) FROM crashes WHERE latitude_degrees IS DISTINCT FROM CASE WHEN latitude IN(77.7777,88.8888,99.9999) THEN NULL ELSE latitude END OR longitude_degrees IS DISTINCT FROM CASE WHEN longitud IN(777.7777,888.8888,999.9999) THEN NULL ELSE longitud END')
 fars.require(con.execute('SELECT count(*) FROM people').fetchone()[0]==88326,'Person view count')
 # These are source-derived regression locks, not an independent publication benchmark.
 fars.require(con.execute('SELECT count(*),sum(fatals),sum(vehicle_records),sum(person_records),sum(parked_working_vehicle_people),sum(nonoccupant_people) FROM crashes').fetchone()==(36297,39254,56011,88326,426,9020),'National source totals')
 fars.require(con.execute('SELECT count(DISTINCT state),count(*) FILTER(WHERE state=43) FROM accident').fetchone()==(51,0),'National geography scope')
 selected={'accident':['STATE','COUNTY','CITY','MONTH','DAY_WEEK','RUR_URB','FUNC_SYS','LGT_COND','WEATHER','MAN_COLL','HARM_EV','REL_ROAD'],'vehicle':['MAKE','MAK_MOD','BODY_TYP','HIT_RUN','DR_PRES','DR_DRINK','SPEEDREL','ROLLOVER'],'person':['PER_TYP','INJ_SEV','SEX','AGE','ALC_STATUS','ATST_TYP','ALC_RES','DRINKING','DRUGS','DSTATUS']}
 expected=set()
 with zipfile.ZipFile(fars.HERE/'data/FARS2024NationalCSV.zip') as z:
  for t,fields in selected.items():
   with z.open(fars.SCHEMA[t]['source_file']) as src:
    for row in csv.DictReader(io.TextIOWrapper(src,encoding='utf-8-sig',newline=''),strict=True):
     for field in fields:
      context='state' if field in ('COUNTY','CITY') else '';expected.add((t,field.lower(),context,int(row['STATE']) if context else 0,int(row[field]),row[field+'NAME']))
 actual=set(con.execute('SELECT * FROM code_labels').fetchall());fars.require(actual==expected,'Full observed labels differ from original CSVs')
 fars.require(con.execute('SELECT count(*) FROM code_labels').fetchone()[0]==len(actual),'Duplicate dictionary tuples')
 conflicts=con.execute('SELECT table_name,column_name,context_column,context_value,code,list(label ORDER BY label) FROM code_labels GROUP BY ALL HAVING count(*)>1 ORDER BY context_value,code').fetchall()
 fars.require([(x[0],x[1],x[3],x[4]) for x in conflicts]==[('accident','city',4,428),('accident','city',13,2190),('accident','city',36,4170),('accident','city',42,3950)],'Source city ambiguity distribution changed')
 zero('ambiguous codes excluded from unique view','SELECT count(*) FROM unambiguous_code_labels u JOIN (SELECT table_name,column_name,context_column,context_value,code FROM code_labels GROUP BY ALL HAVING count(*)>1) a USING(table_name,column_name,context_column,context_value,code)')
 zero('unique lookup key','SELECT count(*) FROM (SELECT table_name,column_name,context_column,context_value,code,count(*) n FROM unambiguous_code_labels GROUP BY ALL HAVING n<>1)')
 fars.require(con.execute('SELECT count(*),sum(row_count),sum(column_count) FROM _metadata').fetchone()==(4,report['rows'],413),'Metadata totals')
 fars.require(con.execute('SELECT count(*) FROM _columns').fetchone()[0]==413,'Dictionary total')
 fars.require([(x[0],x[1]) for x in con.execute('DESCRIBE code_labels').fetchall()]==[('table_name','VARCHAR'),('column_name','VARCHAR'),('context_column','VARCHAR'),('context_value','BIGINT'),('code','BIGINT'),('label','VARCHAR')],'Derived dictionary schema')
 fars.require(con.execute("SELECT row_count,column_count,source_sha256,license FROM _metadata WHERE table_name='code_labels'").fetchone()==(10164,6,fars.LOCK['archive']['sha256'],fars.LICENSE),'Derived dictionary metadata')
 zero('derived field documentation and NULL statistics',"SELECT count(*) FROM _columns WHERE table_name='code_labels' AND (description IS NULL OR source_header<>'Derived' OR null_pct IS DISTINCT FROM 0.0)")
 diagnostics={'national_totals':con.execute('SELECT count(*),sum(fatals),sum(vehicle_records),sum(person_records) FROM crashes').fetchone(),'city_label_conflicts':conflicts,'numeric_missing_person_fields':con.execute("SELECT column_name,null_pct FROM _columns WHERE table_name='person' AND null_pct>0 ORDER BY column_name").fetchall(),'alcohol_test_categories':con.execute('SELECT alc_status,alc_statusname,count(*) FROM people GROUP BY ALL ORDER BY alc_status').fetchall(),'source_labels_compared':len(expected),'coordinate_missing':con.execute('SELECT count(*) FILTER(WHERE latitude_degrees IS NULL OR longitude_degrees IS NULL) FROM crashes').fetchone()[0]}
 return checks,diagnostics
def main():
 db=pathlib.Path(sys.argv[1]);report=json.loads((db.parent/'build-report.json').read_text());fars.require(fars.sha(db)==report['database_sha256'],'Artifact hash')
 with fars.connection(db,True) as con:
  checks,diagnostics=validate(con,report);examples=[]
  for sql in re.sub(r'--[^\n]*','',(fars.HERE/'examples.sql').read_text()).split(';'):
   if not sql.strip():continue
   cursor=con.execute(sql);rows=cursor.fetchall();fars.require(bool(rows),'Empty example');examples.append({'sql':sql.strip(),'columns':[x[0] for x in cursor.description],'rows':rows})
 modules={};pin=json.loads((fars.HERE/'helper-lock.json').read_text())
 for name in ['ensure_metadata','build_columns_table','export_dictionary']:
  path=pathlib.Path(inspect.getsourcefile(getattr(datapond_build,name)));modules[name]={'path':str(path),'sha256':fars.sha(path)};fars.require(modules[name]['sha256']==pin['metadata_py_sha256'],'Helper source pin')
 runtime={'python':platform.python_version(),'interpreter':sys.executable,'duckdb':fars.duckdb.__version__,'datapond_build_version':importlib.metadata.version('datapond-build'),'helper_source_pin':pin,'used_helpers':modules,'installed_packages':sorted([{'name':d.metadata['Name'],'version':d.version} for d in importlib.metadata.distributions()],key=lambda x:x['name'].lower())}
 fars.save(fars.HERE/'runtime.json',runtime);proof={'status':'passed','artifact_sha256':fars.sha(db),'checks':checks,'schema_metadata_dictionary_verified':True,'diagnostics':diagnostics}
 fars.save(fars.HERE/'evidence/release-audit.json',proof);fars.save(fars.HERE/'evidence/examples.json',{'artifact_sha256':fars.sha(db),'queries':examples});print(json.dumps(proof,indent=2,default=str))
if __name__=='__main__':main()
