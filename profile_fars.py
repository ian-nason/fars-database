"""Stream the three MVP CSVs with bounded samples; discover types and observed label domains."""
import collections,csv,datetime,decimal,hashlib,io,json,pathlib,re,zipfile
ROOT=pathlib.Path(__file__).resolve().parent
lock=json.loads((ROOT/'source-lock.json').read_text());archive=ROOT/'data/FARS2024NationalCSV.zip'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert sha(archive)==lock['archive']['sha256']
headers=set(n for m in lock['archive']['members'] for n in m.get('header',[]))
text=(ROOT/'docs/analytical-user-manual.txt').read_text().replace('S\nAS Name','SAS Name').replace('At\ntribute Codes','Attribute Codes');start=text.index('=== PDF PAGE 34 ===');stop=text.index('=== PDF PAGE 358 ===');definitions={}
for match in re.finditer(r'\nDefinition:?\s+(.+?)(?=\nDefinition|\Z)',text[start:stop],re.S):
 block=match.group(1);meaning=re.split(r'\n(?:Additional Information|SAS Name)',block)[0]
 sas=re.search(r'\nSAS Name\s+(.+?)(?:\nAttribute Codes|\n[0-9]{4}(?:-| ))',block,re.S)
 if not sas:continue
 page=int(list(re.finditer(r'=== PDF PAGE (\d+) ===',text[:start+match.start()]))[-1].group(1))
 for name in re.findall(r'\b[A-Z][A-Z0-9_]*\b',sas.group(1)):
  if name in headers and name not in definitions:definitions[name]={'description':' '.join(meaning.split()),'manual_pdf_page':page}
chars={'TWAY_ID','TWAY_ID2','RAIL','VIN','TRLR1VIN','TRLR2VIN','TRLR3VIN','MCARR_ID','MCARR_I2','DR_ZIP'}|{'VIN_'+str(i) for i in range(1,13)}
schema={};profile={}
with zipfile.ZipFile(archive) as z:
 for table in ['accident','vehicle','person']:
  rec=next(m for m in lock['archive']['members'] if m['name'].lower().endswith('/'+table+'.csv'))
  columns=[];missing=[]
  for name in rec['header']:
   base=name[:-4] if name.endswith('NAME') else name
   if base not in definitions:missing.append(name)
   d=definitions.get(base,{})
   columns.append({'name':name.lower(),'source_header':name,'type':'VARCHAR' if name.endswith('NAME') or name in chars else 'DECIMAL(18,12)' if name in ('LATITUDE','LONGITUD') else 'BIGINT','description':('Source label for '+base+'. ' if name.endswith('NAME') else '')+d.get('description','UNRESOLVED'),'manual_pdf_page':d.get('manual_pdf_page')})
  stats={n:{'blank':0,'dot_missing':0,'max_length':0,'samples':[],'min':None,'max':None} for n in rec['header']};pairs={n[:-4]:set() for n in rec['header'] if n.endswith('NAME') and n[:-4] in rec['header']};omitted={};n=0
  counts={k:collections.Counter() for k in ['STATE','PER_TYP','INJ_SEV','ALC_STATUS','ALC_RES'] if k in rec['header']};totals={k:0 for k in ['FATALS','DEATHS','VE_FORMS','PEDS','PERSONS','PERMVIT','PERNOTMVIT'] if k in rec['header']}
  with z.open(rec['name']) as src:
   reader=csv.DictReader(io.TextIOWrapper(src,encoding='utf-8-sig',newline=''),strict=True)
   for row in reader:
    if None in row or any(v is None for v in row.values()):raise ValueError('Row width mismatch')
    n+=1
    for k in counts:counts[k][row[k]]+=1
    for k in totals:totals[k]+=int(row[k])
    for c in columns:
     name=c['source_header'];value=row[name];s=stats[name];s['blank']+=value=='';s['dot_missing']+=value=='.';s['max_length']=max(s['max_length'],len(value))
     if value not in s['samples'] and len(s['samples'])<5:s['samples'].append(value)
     if c['type']!='VARCHAR' and value not in ('','.'):
      if c['type']=='BIGINT' and not re.fullmatch(r'-?[0-9]+',value):raise ValueError(name+' invalid integer '+value)
      if c['type'].startswith('DECIMAL') and not re.fullmatch(r'-?[0-9]+(?:\.[0-9]{1,12})?',value):raise ValueError(name+' invalid decimal '+value)
      v=decimal.Decimal(value);s['min']=v if s['min'] is None else min(s['min'],v);s['max']=v if s['max'] is None else max(s['max'],v)
    for name,values in pairs.items():
     if name in omitted:continue
     context=row['STATE'] if name in ('COUNTY','CITY') else row.get('MAKE','') if name=='MODEL' else ''
     values.add((context,row[name],row[name+'NAME']))
     if len(values)>2000:omitted[name]='More than 2000 observed context/code/label tuples; labels remain in raw table';values.clear()
  schema[table]={'source_file':rec['name'],'source_sha256':rec['sha256'],'rows':n,'columns':columns,'key':['state','st_case']+(['veh_no'] if table in ('vehicle','person') else [])+(['per_no'] if table=='person' else []),'description':{'accident':'One record per fatal crash in the 2024 national Annual Report File.','vehicle':'One record per motor vehicle in transport; parked/working vehicles are in omitted Parkwork.','person':'One record per involved person, including nonoccupants and occupants of vehicles not in transport.'}[table]}
  profile[table]={'rows':n,'columns':stats,'missing_manual_definitions':missing,'observed_labels':{k:sorted(v) for k,v in pairs.items() if k not in omitted},'label_fields_over_cap':omitted,'source_counts':counts,'source_totals':totals}
  print(table,n,'columns',len(columns),'unmapped',missing,'omitted_labels',list(omitted),flush=True)
(ROOT/'schema.json').write_text(json.dumps(schema,indent=2,default=str)+'\n');(ROOT/'evidence/source-profile.json').write_text(json.dumps(profile,indent=2,default=str)+'\n')
(ROOT/'docs/field-definitions.json').write_text(json.dumps(definitions,indent=2)+'\n')
print('Profile complete',datetime.datetime.now(datetime.timezone.utc).isoformat(),flush=True)
