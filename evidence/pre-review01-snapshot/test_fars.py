import copy,decimal,hashlib,io,pathlib,tempfile,unittest,zipfile
from unittest.mock import patch
import duckdb,fars
class Parsing(unittest.TestCase):
 def c(self,t,n):return next(c for c in fars.SCHEMA[t]['columns'] if c['name']==n)
 def test_coordinate_precision(self):self.assertEqual(fars.typed('33.47131111',self.c('accident','latitude')),decimal.Decimal('33.47131111'))
 def test_overprecision_rejected(self):
  with self.assertRaisesRegex(ValueError,'overprecision'):fars.typed('33.1234567890123',self.c('accident','latitude'))
 def test_nan_rejected(self):
  with self.assertRaisesRegex(ValueError,'Invalid'):fars.typed('NaN',self.c('accident','latitude'))
 def test_fractional_integer_rejected(self):
  with self.assertRaisesRegex(ValueError,'Invalid integer'):fars.typed('1.5',self.c('person','age'))
 def test_source_character_blanks_preserved(self):self.assertEqual(fars.typed('',self.c('accident','tway_id2')),'')
 def test_numeric_nonoccupant_blank_is_null(self):self.assertIsNone(fars.typed('',self.c('person','mod_year')))
 def test_unexpected_numeric_blank_rejected(self):
  with self.assertRaisesRegex(ValueError,'Unexpected numeric blank'):fars.typed('',self.c('person','age'))
 def test_missing_sentinel_is_preserved(self):self.assertEqual(fars.typed('999',self.c('person','age')),999)
 def test_zip_leading_zeros_preserved(self):self.assertEqual(fars.typed('00123',self.c('vehicle','dr_zip')),'00123')
 def test_dot_not_silently_null(self):
  with self.assertRaisesRegex(ValueError,'Invalid'):fars.typed('.',self.c('person','age'))
 def test_existing_output_refused(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(FileExistsError):fars.build(pathlib.Path('unused'),pathlib.Path(d))
 def test_output_escape_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaisesRegex(ValueError,'guarded repository'):fars.build(pathlib.Path('unused'),pathlib.Path(d)/'new')
 def test_bad_archive_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'bad.zip';p.write_bytes(b'bad')
   with self.assertRaisesRegex(ValueError,'Archive size/SHA'):fars.verify_archive(p)
 def test_mutated_source_cell_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'a.zip'
   with zipfile.ZipFile(p,'w') as z:z.writestr('a.csv','VALUE\n1\n')
   spec={'accident':{'rows':1,'source_file':'a.csv','columns':[{'name':'value','source_header':'VALUE','type':'BIGINT'}]}}
   with duckdb.connect(config={'memory_limit':'32MiB','threads':'1'}) as con,patch.object(fars,'SCHEMA',spec):
    con.execute('CREATE TABLE accident(value BIGINT)');con.execute('INSERT INTO accident VALUES (2)')
    with self.assertRaisesRegex(ValueError,'Source cell mismatch'):fars.compare_source(con,p)
 def test_fresh_checkout_download_creates_data_directory(self):
  with tempfile.TemporaryDirectory() as d:
   root=pathlib.Path(d);buffer=io.BytesIO()
   with zipfile.ZipFile(buffer,'w') as z:z.writestr('x.csv','1')
   raw=buffer.getvalue();record={'archive':{'url':'https://example.invalid/source.zip','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'members':[{'name':'x.csv','bytes':1}]}}
   with patch.object(fars,'HERE',root),patch.object(fars,'LOCK',record),patch.object(fars.urllib.request,'urlopen',return_value=io.BytesIO(raw)):
    fars.download(root/'data/new.zip');self.assertEqual((root/'data/new.zip').read_bytes(),raw)
 def test_partial_extraction_refused(self):
  with tempfile.TemporaryDirectory() as d,patch.object(fars,'HERE',pathlib.Path(d)):
   (pathlib.Path(d)/'data').mkdir();(pathlib.Path(d)/'data/accident-source.csv.partial').write_bytes(b'partial')
   with self.assertRaisesRegex(ValueError,'Retained partial'):fars.extract(pathlib.Path('unused'),'accident')
 def test_corrupt_cached_extraction_refused(self):
  with tempfile.TemporaryDirectory() as d,patch.object(fars,'HERE',pathlib.Path(d)):
   (pathlib.Path(d)/'data').mkdir();(pathlib.Path(d)/'data/accident-source.csv').write_bytes(b'bad')
   with self.assertRaisesRegex(ValueError,'Cached source hash'):fars.extract(pathlib.Path('unused'),'accident')
class Semantics(unittest.TestCase):
 def setUp(self):
  self.c=duckdb.connect(config={'memory_limit':'64MiB','threads':'1'})
  for t,s in fars.SCHEMA.items():
   self.c.execute('CREATE TABLE '+t+'('+','.join(x['name']+' '+x['type'] for x in s['columns'])+')')
   values={x['name']:'' if x['type']=='VARCHAR' else 0 for x in s['columns']};values.update(state=1,st_case=10001)
   if t=='accident':values.update(year=2024,fatals=1,ve_forms=1,persons=1,peds=0,permvit=1,pernotmvit=0,latitude=decimal.Decimal('33.47131111'),longitud=decimal.Decimal('-86.2'))
   if t=='vehicle':values.update(veh_no=1,deaths=1)
   if t=='person':values.update(veh_no=1,per_no=1,per_typ=1,inj_sev=4,age=30,alc_res=100)
   self.c.execute('INSERT INTO '+t+' VALUES ('+','.join('?' for _ in values)+')',list(values.values()))
  fars.labels(self.c);self.c.execute('CREATE VIEW crashes AS '+fars.crash_sql());self.c.execute('CREATE VIEW people AS '+fars.people_sql());self.c.execute('CREATE VIEW unambiguous_code_labels AS '+fars.unambiguous_labels_sql())
 def tearDown(self):self.c.close()
 def checks(self):return fars.checks(self.c,False)
 def test_valid_fixture(self):self.checks()
 def test_duplicate_crash_rejected(self):
  self.c.execute('INSERT INTO accident SELECT * FROM accident')
  with self.assertRaisesRegex(ValueError,'duplicate key'):self.checks()
 def test_orphan_person_rejected(self):
  self.c.execute('UPDATE person SET st_case=10002')
  with self.assertRaisesRegex(ValueError,'crash reference'):self.checks()
 def test_missing_transport_vehicle_rejected(self):
  self.c.execute('UPDATE person SET veh_no=2')
  with self.assertRaisesRegex(ValueError,'occupant vehicle reference'):self.checks()
 def test_nonoccupant_retained_without_vehicle(self):
  self.c.execute('UPDATE person SET veh_no=0,per_typ=5');self.c.execute('UPDATE vehicle SET deaths=0');self.c.execute('UPDATE accident SET persons=0,peds=1,permvit=0,pernotmvit=1')
  self.checks();self.assertEqual(self.c.execute('SELECT person_fatalities,nonoccupant_fatalities FROM crashes').fetchone(),(1,1))
 def test_parked_occupant_retained_without_transport_vehicle(self):
  self.c.execute('UPDATE person SET veh_no=2,per_typ=3');self.c.execute('UPDATE vehicle SET deaths=0');self.c.execute('UPDATE accident SET permvit=0,pernotmvit=1')
  self.checks();self.assertEqual(self.c.execute('SELECT parked_working_vehicle_fatalities FROM crashes').fetchone(),(1,))
 def test_nonoccupant_with_vehicle_number_rejected(self):
  self.c.execute('UPDATE person SET per_typ=5')
  with self.assertRaisesRegex(ValueError,'vehicle number semantics'):self.checks()
 def test_parked_transport_collision_rejected(self):
  self.c.execute('UPDATE person SET per_typ=3')
  with self.assertRaisesRegex(ValueError,'parked vehicle collision'):self.checks()
 def test_crash_view_prevents_many_to_many_inflation(self):
  self.c.execute('INSERT INTO vehicle SELECT * REPLACE(2 AS veh_no,0 AS deaths) FROM vehicle');self.c.execute('INSERT INTO person SELECT * REPLACE(2 AS per_no,0 AS inj_sev) FROM person');self.c.execute('UPDATE accident SET ve_forms=2,persons=2,permvit=2')
  self.checks();self.assertEqual(self.c.execute('SELECT count(*),sum(fatals) FROM crashes').fetchone(),(1,1));self.assertEqual(self.c.execute('SELECT sum(a.fatals) FROM accident a JOIN vehicle USING(state,st_case) JOIN person USING(state,st_case)').fetchone(),(4,))
 def test_wrong_year_rejected(self):
  self.c.execute('UPDATE accident SET year=2023')
  with self.assertRaisesRegex(ValueError,'vintage'):self.checks()
 def test_bad_alcohol_code_rejected(self):
  self.c.execute('UPDATE person SET alc_res=950')
  with self.assertRaisesRegex(ValueError,'alcohol result codes'):self.checks()
 def test_unknown_bac_not_zero(self):
  self.c.execute('UPDATE person SET alc_res=999');self.assertIsNone(self.c.execute('SELECT measured_bac_g_dl FROM people').fetchone()[0])
 def test_topcoded_bac_not_exact(self):
  self.c.execute('UPDATE person SET alc_res=940');self.assertEqual(self.c.execute('SELECT measured_bac_g_dl,bac_top_coded_at_094_or_more FROM people').fetchone(),(None,True))
 def test_measured_bac_scale(self):self.assertEqual(self.c.execute('SELECT measured_bac_g_dl FROM people').fetchone()[0],decimal.Decimal('0.100'))
 def test_unknown_age_not_years(self):
  self.c.execute('UPDATE person SET age=998');self.assertIsNone(self.c.execute('SELECT age_years FROM people').fetchone()[0])
 def test_unknown_coordinate_not_map_point(self):
  self.c.execute('UPDATE accident SET latitude=77.7777,longitud=999.9999');self.assertEqual(self.c.execute('SELECT latitude_degrees,longitude_degrees FROM crashes').fetchone(),(None,None))
 def test_fatality_reconciliation_fails(self):
  self.c.execute('UPDATE accident SET fatals=2')
  with self.assertRaisesRegex(ValueError,'reconciliation'):self.checks()
 def test_duplicate_label_tuple_rejected(self):
  self.c.execute("INSERT INTO code_labels SELECT * FROM code_labels WHERE column_name='state'")
  with self.assertRaisesRegex(ValueError,'code-label tuple'):self.checks()
 def test_ambiguous_labels_preserved_and_excluded_from_unique_lookup(self):
  self.c.execute("INSERT INTO code_labels VALUES('accident','state','',0,1,'Conflicting')")
  self.checks();self.assertEqual(self.c.execute("SELECT count(*) FROM code_labels WHERE column_name='state'").fetchone()[0],2)
  self.assertEqual(self.c.execute("SELECT count(*) FROM unambiguous_code_labels WHERE column_name='state'").fetchone()[0],0)
if __name__=='__main__':unittest.main(verbosity=2)
