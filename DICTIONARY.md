# FARS 2024 Annual Report File dictionary

Source: NHTSA 2024 national Annual Report File, first release 2026-04-01.
407 original source columns are preserved; code_labels has six derived columns. Views are documented in README.

## accident

One record per fatal crash in the 2024 national Annual Report File.

Source file: `FARS2024NationalCSV/accident.csv`
Rows: 36,297

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| state | BIGINT | 0.0% | 1 |  |
| statename | VARCHAR | 0.0% | Alabama |  |
| st_case | BIGINT | 0.0% | 100001 | Within this year: join accident by state/st_case; aggregate child tables before crash-level joins. |
| peds | BIGINT | 0.0% | 0 |  |
| pernotmvit | BIGINT | 0.0% | 0 |  |
| ve_total | BIGINT | 0.0% | 1 |  |
| ve_forms | BIGINT | 0.0% | 1 |  |
| pvh_invl | BIGINT | 0.0% | 0 |  |
| persons | BIGINT | 0.0% | 0 |  |
| permvit | BIGINT | 0.0% | 0 |  |
| county | BIGINT | 0.0% | 1 |  |
| countyname | VARCHAR | 0.0% | ABBEVILLE (1) |  |
| city | BIGINT | 0.0% | 0 |  |
| cityname | VARCHAR | 0.0% | ABBEVILLE |  |
| month | BIGINT | 0.0% | 1 |  |
| monthname | VARCHAR | 0.0% | April |  |
| day | BIGINT | 0.0% | 1 |  |
| dayname | VARCHAR | 0.0% | 1 |  |
| day_week | BIGINT | 0.0% | 1 |  |
| day_weekname | VARCHAR | 0.0% | Friday |  |
| year | BIGINT | 0.0% | 2024 |  |
| hour | BIGINT | 0.0% | 0 |  |
| hourname | VARCHAR | 0.0% | 0:00am-0:59am |  |
| minute | BIGINT | 0.0% | 0 |  |
| minutename | VARCHAR | 0.0% | 0 |  |
| tway_id | VARCHAR | 0.0% |  |  |
| tway_id2 | VARCHAR | 0.0% |  |  |
| route | BIGINT | 0.0% | 0 |  |
| routename | VARCHAR | 0.0% | Bureau of Indian Affairs |  |
| rur_urb | BIGINT | 0.0% | 1 |  |
| rur_urbname | VARCHAR | 0.0% | Not Reported |  |
| func_sys | BIGINT | 0.0% | 1 |  |
| func_sysname | VARCHAR | 0.0% | Interstate |  |
| rd_owner | BIGINT | 0.0% | 1 |  |
| rd_ownername | VARCHAR | 0.0% | Army |  |
| nhs | BIGINT | 0.0% | 0 |  |
| nhsname | VARCHAR | 0.0% | This Section IS NOT on the NHS |  |
| sp_jur | BIGINT | 0.0% | 0 |  |
| sp_jurname | VARCHAR | 0.0% | College/University Campus* |  |
| milept | BIGINT | 0.0% | 0 |  |
| mileptname | VARCHAR | 0.0% | 1 |  |
| latitude | DECIMAL(18,12) | 0.0% | 19.064066670000 |  |
| latitudename | VARCHAR | 0.0% | 19.06406667 |  |
| longitud | DECIMAL(18,12) | 0.0% | -100.014730560000 |  |
| longitudname | VARCHAR | 0.0% | -100.01473056 |  |
| harm_ev | BIGINT | 0.0% | 1 |  |
| harm_evname | VARCHAR | 0.0% | Boulder |  |
| man_coll | BIGINT | 0.0% | 0 |  |
| man_collname | VARCHAR | 0.0% | Angle |  |
| reljct1 | BIGINT | 0.0% | 0 |  |
| reljct1name | VARCHAR | 0.0% | No |  |
| reljct2 | BIGINT | 0.0% | 1 |  |
| reljct2name | VARCHAR | 0.0% | Acceleration/Deceleration Lane |  |
| typ_int | BIGINT | 0.0% | 1 |  |
| typ_intname | VARCHAR | 0.0% | Five Point, or More |  |
| rel_road | BIGINT | 0.0% | 1 |  |
| rel_roadname | VARCHAR | 0.0% | Continuous Left - Turn Lane |  |
| wrk_zone | BIGINT | 0.0% | 0 |  |
| wrk_zonename | VARCHAR | 0.0% | Construction |  |
| lgt_cond | BIGINT | 0.0% | 1 |  |
| lgt_condname | VARCHAR | 0.0% | Dark - Lighted |  |
| weather | BIGINT | 0.0% | 1 |  |
| weathername | VARCHAR | 0.0% | Blowing Sand, Soil, Dirt |  |
| sch_bus | BIGINT | 0.0% | 0 |  |
| sch_busname | VARCHAR | 0.0% | No |  |
| rail | VARCHAR | 0.0% | 0000000 |  |
| railname | VARCHAR | 0.0% | 004481J |  |
| not_hour | BIGINT | 0.0% | 0 |  |
| not_hourname | VARCHAR | 0.0% | 0:00am-0:59am |  |
| not_min | BIGINT | 0.0% | 0 |  |
| not_minname | VARCHAR | 0.0% | 0 |  |
| arr_hour | BIGINT | 0.0% | 0 |  |
| arr_hourname | VARCHAR | 0.0% | 0:00am-0:59am |  |
| arr_min | BIGINT | 0.0% | 0 |  |
| arr_minname | VARCHAR | 0.0% | 0 |  |
| hosp_hr | BIGINT | 0.0% | 0 |  |
| hosp_hrname | VARCHAR | 0.0% | 0:00am-0:59am |  |
| hosp_mn | BIGINT | 0.0% | 0 |  |
| hosp_mnname | VARCHAR | 0.0% | 0 |  |
| fatals | BIGINT | 0.0% | 1 |  |

## vehicle

One record per motor vehicle in transport; parked/working vehicles are in omitted Parkwork.

Source file: `FARS2024NationalCSV/vehicle.csv`
Rows: 56,011

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| state | BIGINT | 0.0% | 1 |  |
| statename | VARCHAR | 0.0% | Alabama |  |
| st_case | BIGINT | 0.0% | 100001 | Within this year: join accident by state/st_case; aggregate child tables before crash-level joins. |
| veh_no | BIGINT | 0.0% | 1 | Join transport occupants by state/st_case/veh_no; 0 denotes nonoccupants and PER_TYP=3 belongs to omitted Parkwork. |
| ve_forms | BIGINT | 0.0% | 1 |  |
| month | BIGINT | 0.0% | 1 |  |
| monthname | VARCHAR | 0.0% | April |  |
| day | BIGINT | 0.0% | 1 |  |
| dayname | VARCHAR | 0.0% | 1 |  |
| hour | BIGINT | 0.0% | 0 |  |
| hourname | VARCHAR | 0.0% | 0:00am-0:59am |  |
| minute | BIGINT | 0.0% | 0 |  |
| minutename | VARCHAR | 0.0% | 0 |  |
| harm_ev | BIGINT | 0.0% | 1 |  |
| harm_evname | VARCHAR | 0.0% | Boulder |  |
| man_coll | BIGINT | 0.0% | 0 |  |
| man_collname | VARCHAR | 0.0% | Angle |  |
| numoccs | BIGINT | 0.0% | 0 |  |
| numoccsname | VARCHAR | 0.0% | 01 |  |
| unittype | BIGINT | 0.0% | 1 |  |
| unittypename | VARCHAR | 0.0% | Motor Vehicle In-Transport (Inside or Outside the Trafficway) |  |
| hit_run | BIGINT | 0.0% | 0 |  |
| hit_runname | VARCHAR | 0.0% | No |  |
| reg_stat | BIGINT | 0.0% | 0 |  |
| reg_statname | VARCHAR | 0.0% | Alabama |  |
| owner | BIGINT | 0.0% | 0 |  |
| ownername | VARCHAR | 0.0% | Driver (in this crash) Not Registered Owner (Other Private Owner Listed) |  |
| vin | VARCHAR | 0.0% | ***********2 |  |
| vinname | VARCHAR | 0.0% | ***********2 |  |
| mod_year | BIGINT | 0.0% | 1929 |  |
| mod_yearname | VARCHAR | 0.0% | 1929 |  |
| vpicmake | BIGINT | 0.0% | 10019 |  |
| vpicmakename | VARCHAR | 0.0% | AM General |  |
| vpicmodel | BIGINT | 0.0% | 10007 |  |
| vpicmodelname | VARCHAR | 0.0% | 1 series |  |
| vpicbodyclass | BIGINT | 0.0% | 1 |  |
| vpicbodyclassname | VARCHAR | 0.0% | Bus |  |
| make | BIGINT | 0.0% | 12 |  |
| makename | VARCHAR | 0.0% | AM General |  |
| model | BIGINT | 0.0% | 1 |  |
| body_typ | BIGINT | 0.0% | 1 |  |
| body_typname | VARCHAR | 0.0% | 2-door sedan,hardtop,coupe |  |
| icfinalbody | BIGINT | 0.0% | 0 |  |
| icfinalbodyname | VARCHAR | 0.0% | Ambulance |  |
| gvwr_from | BIGINT | 0.0% | 11 |  |
| gvwr_fromname | VARCHAR | 0.0% | Class 1: 6,000 lbs. or less (2,722 kg or less) |  |
| gvwr_to | BIGINT | 0.0% | 11 |  |
| gvwr_toname | VARCHAR | 0.0% | Class 1: 6,000 lbs. or less (2,722 kg or less) |  |
| tow_veh | BIGINT | 0.0% | 0 |  |
| tow_vehname | VARCHAR | 0.0% | No Trailers |  |
| trlr1vin | VARCHAR | 0.0% | 000000000000 |  |
| trlr1vinname | VARCHAR | 0.0% | 0146077***** |  |
| trlr2vin | VARCHAR | 0.0% | 000000000000 |  |
| trlr2vinname | VARCHAR | 0.0% | 159J53406250 |  |
| trlr3vin | VARCHAR | 0.0% | 000000000000 |  |
| trlr3vinname | VARCHAR | 0.0% | No Trailing Units |  |
| trlr1gvwr | BIGINT | 0.0% | 0 |  |
| trlr1gvwrname | VARCHAR | 0.0% | Class 1: 6,000 lbs or less (2,722 kg or less) |  |
| trlr2gvwr | BIGINT | 0.0% | 0 |  |
| trlr2gvwrname | VARCHAR | 0.0% | Class 1: 6,000 lbs or less (2,722 kg or less) |  |
| trlr3gvwr | BIGINT | 0.0% | 0 |  |
| trlr3gvwrname | VARCHAR | 0.0% | No Trailer GVWR Required |  |
| j_knife | BIGINT | 0.0% | 0 |  |
| j_knifename | VARCHAR | 0.0% | No |  |
| mcarr_id | VARCHAR | 0.0% | 00000000000 |  |
| mcarr_idname | VARCHAR | 0.0% | 01003413480 |  |
| mcarr_i1 | BIGINT | 0.0% | 0 |  |
| mcarr_i1name | VARCHAR | 0.0% | Alabama |  |
| mcarr_i2 | VARCHAR | 0.0% | 000000000 |  |
| mcarr_i2name | VARCHAR | 0.0% | 000001539 |  |
| v_config | BIGINT | 0.0% | 0 |  |
| v_configname | VARCHAR | 0.0% | Bus (seats for more than 15 occupants, including driver) |  |
| cargo_bt | BIGINT | 0.0% | 0 |  |
| cargo_btname | VARCHAR | 0.0% | Auto Transporter |  |
| haz_inv | BIGINT | 0.0% | 1 |  |
| haz_invname | VARCHAR | 0.0% | No |  |
| haz_plac | BIGINT | 0.0% | 0 |  |
| haz_placname | VARCHAR | 0.0% | No |  |
| haz_id | BIGINT | 0.0% | 0 |  |
| haz_idname | VARCHAR | 0.0% | 1005 |  |
| haz_cno | BIGINT | 0.0% | 0 |  |
| haz_cnoname | VARCHAR | 0.0% | 01 |  |
| haz_rel | BIGINT | 0.0% | 0 |  |
| haz_relname | VARCHAR | 0.0% | No |  |
| bus_use | BIGINT | 0.0% | 0 |  |
| bus_usename | VARCHAR | 0.0% | Bus, Unknown Use |  |
| spec_use | BIGINT | 0.0% | 0 |  |
| spec_usename | VARCHAR | 0.0% | Ambulance |  |
| emer_use | BIGINT | 0.0% | 0 |  |
| emer_usename | VARCHAR | 0.0% | Emergency Operation, Emergency Warning Equipment Not in Use |  |
| trav_sp | BIGINT | 0.0% | 0 |  |
| trav_spname | VARCHAR | 0.0% | 001 MPH |  |
| underoverride | BIGINT | 0.0% | 0 |  |
| underoverridename | VARCHAR | 0.0% | No Underride or Override |  |
| rollover | BIGINT | 0.0% | 0 |  |
| rollovername | VARCHAR | 0.0% | No Rollover |  |
| rolinloc | BIGINT | 0.0% | 0 |  |
| rolinlocname | VARCHAR | 0.0% | In Gore |  |
| impact1 | BIGINT | 0.0% | 0 |  |
| impact1name | VARCHAR | 0.0% | 1 Clock Point |  |
| deformed | BIGINT | 0.0% | 0 |  |
| deformedname | VARCHAR | 0.0% | Damage Reported, Extent Unknown |  |
| towed | BIGINT | 0.0% | 5 |  |
| towedname | VARCHAR | 0.0% | Not Reported |  |
| m_harm | BIGINT | 0.0% | 1 |  |
| m_harmname | VARCHAR | 0.0% | Boulder |  |
| fire_exp | BIGINT | 0.0% | 0 |  |
| fire_expname | VARCHAR | 0.0% | No or Not Reported |  |
| mak_mod | BIGINT | 0.0% | 12002 |  |
| mak_modname | VARCHAR | 0.0% | AM General Hummer |  |
| vin_1 | VARCHAR | 0.0% | * |  |
| vin_2 | VARCHAR | 0.0% |  |  |
| vin_3 | VARCHAR | 0.0% |  |  |
| vin_4 | VARCHAR | 0.0% |  |  |
| vin_5 | VARCHAR | 0.0% |  |  |
| vin_6 | VARCHAR | 0.0% |  |  |
| vin_7 | VARCHAR | 0.0% |  |  |
| vin_8 | VARCHAR | 0.0% |  |  |
| vin_9 | VARCHAR | 0.0% |  |  |
| vin_10 | VARCHAR | 0.0% |  |  |
| vin_11 | VARCHAR | 0.0% |  |  |
| vin_12 | VARCHAR | 0.0% |  |  |
| deaths | BIGINT | 0.0% | 0 |  |
| dr_drink | BIGINT | 0.0% | 0 |  |
| dr_drinkname | VARCHAR | 0.0% | No |  |
| dr_pres | BIGINT | 0.0% | 0 |  |
| dr_presname | VARCHAR | 0.0% | No Driver Present/Not Applicable |  |
| l_state | BIGINT | 0.0% | 0 |  |
| l_statename | VARCHAR | 0.0% | Alabama |  |
| dr_zip | VARCHAR | 0.0% | 0 |  |
| dr_zipname | VARCHAR | 0.0% | 10002 |  |
| l_type | BIGINT | 0.0% | 0 |  |
| l_typename | VARCHAR | 0.0% | Full Driver License |  |
| l_status | BIGINT | 0.0% | 0 |  |
| l_statusname | VARCHAR | 0.0% | Canceled or denied |  |
| cdl_stat | BIGINT | 0.0% | 0 |  |
| cdl_statname | VARCHAR | 0.0% | Cancelled or Denied |  |
| l_endors | BIGINT | 0.0% | 0 |  |
| l_endorsname | VARCHAR | 0.0% | Endorsement(s) Required, Compliance Unknown |  |
| l_compl | BIGINT | 0.0% | 0 |  |
| l_complname | VARCHAR | 0.0% | No Driver Present/Unknown if Driver Present |  |
| l_restri | BIGINT | 0.0% | 0 |  |
| l_restriname | VARCHAR | 0.0% | No Driver Present/Unknown if Driver Present |  |
| dr_hgt | BIGINT | 0.0% | 36 |  |
| dr_hgtname | VARCHAR | 0.0% | 36 |  |
| dr_wgt | BIGINT | 0.0% | 100 |  |
| dr_wgtname | VARCHAR | 0.0% | 100 lbs. |  |
| prev_acc | BIGINT | 0.0% | 0 |  |
| prev_accname | VARCHAR | 0.0% | 1 |  |
| prev_sus1 | BIGINT | 0.0% | 0 |  |
| prev_sus1name | VARCHAR | 0.0% | 1 |  |
| prev_sus2 | BIGINT | 0.0% | 0 |  |
| prev_sus2name | VARCHAR | 0.0% | 1 |  |
| prev_sus3 | BIGINT | 0.0% | 0 |  |
| prev_sus3name | VARCHAR | 0.0% | 1 |  |
| prev_dwi | BIGINT | 0.0% | 0 |  |
| prev_dwiname | VARCHAR | 0.0% | 1 |  |
| prev_spd | BIGINT | 0.0% | 0 |  |
| prev_spdname | VARCHAR | 0.0% | 1 |  |
| prev_oth | BIGINT | 0.0% | 0 |  |
| prev_othname | VARCHAR | 0.0% | 1 |  |
| first_mo | BIGINT | 0.0% | 0 |  |
| first_moname | VARCHAR | 0.0% | April |  |
| first_yr | BIGINT | 0.0% | 0 |  |
| first_yrname | VARCHAR | 0.0% | 2019 |  |
| last_mo | BIGINT | 0.0% | 0 |  |
| last_moname | VARCHAR | 0.0% | April |  |
| last_yr | BIGINT | 0.0% | 0 |  |
| last_yrname | VARCHAR | 0.0% | 2019 |  |
| speedrel | BIGINT | 0.0% | 0 |  |
| speedrelname | VARCHAR | 0.0% | No |  |
| vtrafway | BIGINT | 0.0% | 0 |  |
| vtrafwayname | VARCHAR | 0.0% | Entrance/Exit Ramp |  |
| vnum_lan | BIGINT | 0.0% | 0 |  |
| vnum_lanname | VARCHAR | 0.0% | Five lanes |  |
| vspd_lim | BIGINT | 0.0% | 0 |  |
| vspd_limname | VARCHAR | 0.0% | 10 MPH |  |
| valign | BIGINT | 0.0% | 0 |  |
| valignname | VARCHAR | 0.0% | Curve - Unknown Direction |  |
| vprofile | BIGINT | 0.0% | 0 |  |
| vprofilename | VARCHAR | 0.0% | Downhill |  |
| vpavetyp | BIGINT | 0.0% | 0 |  |
| vpavetypname | VARCHAR | 0.0% | Blacktop, Bituminous, or Asphalt |  |
| vsurcond | BIGINT | 0.0% | 0 |  |
| vsurcondname | VARCHAR | 0.0% | Dry |  |
| vtrafcon | BIGINT | 0.0% | 0 |  |
| vtrafconname | VARCHAR | 0.0% | Flashing Traffic Control Signal |  |
| vtcont_f | BIGINT | 0.0% | 0 |  |
| vtcont_fname | VARCHAR | 0.0% | Device Functioning Properly |  |
| p_crash1 | BIGINT | 0.0% | 0 |  |
| p_crash1name | VARCHAR | 0.0% | Accelerating in Road |  |
| p_crash2 | BIGINT | 0.0% | 1 |  |
| p_crash2name | VARCHAR | 0.0% | Animal -unknown location |  |
| p_crash3 | BIGINT | 0.0% | 0 |  |
| p_crash3name | VARCHAR | 0.0% | Accelerating |  |
| pcrash4 | BIGINT | 0.0% | 0 |  |
| pcrash4name | VARCHAR | 0.0% | No Driver Present / Unknown if Driver Present |  |
| pcrash5 | BIGINT | 0.0% | 0 |  |
| pcrash5name | VARCHAR | 0.0% | Departed roadway |  |
| acc_type | BIGINT | 0.0% | 0 |  |
| acc_typename | VARCHAR | 0.0% | A1-Single Driver-Right Roadside Departure-Drive Off Road |  |

## person

One record per involved person, including nonoccupants and occupants of vehicles not in transport.

Source file: `FARS2024NationalCSV/person.csv`
Rows: 88,326

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| state | BIGINT | 0.0% | 1 |  |
| statename | VARCHAR | 0.0% | Alabama |  |
| st_case | BIGINT | 0.0% | 100001 | Within this year: join accident by state/st_case; aggregate child tables before crash-level joins. |
| veh_no | BIGINT | 0.0% | 0 | Join transport occupants by state/st_case/veh_no; 0 denotes nonoccupants and PER_TYP=3 belongs to omitted Parkwork. |
| per_no | BIGINT | 0.0% | 1 | Person identity requires state/st_case/veh_no/per_no. |
| ve_forms | BIGINT | 0.0% | 1 |  |
| county | BIGINT | 0.0% | 1 |  |
| month | BIGINT | 0.0% | 1 |  |
| monthname | VARCHAR | 0.0% | April |  |
| day | BIGINT | 0.0% | 1 |  |
| dayname | VARCHAR | 0.0% | 1 |  |
| hour | BIGINT | 0.0% | 0 |  |
| hourname | VARCHAR | 0.0% | 0:00am-0:59am |  |
| minute | BIGINT | 0.0% | 0 |  |
| minutename | VARCHAR | 0.0% | 0 |  |
| harm_ev | BIGINT | 0.0% | 1 |  |
| harm_evname | VARCHAR | 0.0% | Boulder |  |
| man_coll | BIGINT | 0.0% | 0 |  |
| man_collname | VARCHAR | 0.0% | Angle |  |
| sch_bus | BIGINT | 0.0% | 0 |  |
| sch_busname | VARCHAR | 0.0% | No |  |
| rur_urb | BIGINT | 0.0% | 1 |  |
| rur_urbname | VARCHAR | 0.0% | Not Reported |  |
| func_sys | BIGINT | 0.0% | 1 |  |
| func_sysname | VARCHAR | 0.0% | Interstate |  |
| mod_year | BIGINT | 10.2% | 1929 |  |
| mod_yearname | VARCHAR | 0.0% |  |  |
| vpicmake | BIGINT | 10.2% | 10019 |  |
| vpicmakename | VARCHAR | 0.0% |  |  |
| vpicmodel | BIGINT | 10.2% | 10007 |  |
| vpicmodelname | VARCHAR | 0.0% |  |  |
| vpicbodyclass | BIGINT | 10.2% | 1 |  |
| vpicbodyclassname | VARCHAR | 0.0% |  |  |
| make | BIGINT | 10.2% | 12 |  |
| makename | VARCHAR | 0.0% |  |  |
| body_typ | BIGINT | 10.2% | 1 |  |
| body_typname | VARCHAR | 0.0% |  |  |
| icfinalbody | BIGINT | 10.2% | 0 |  |
| icfinalbodyname | VARCHAR | 0.0% |  |  |
| gvwr_from | BIGINT | 10.2% | 11 |  |
| gvwr_fromname | VARCHAR | 0.0% |  |  |
| gvwr_to | BIGINT | 10.2% | 11 |  |
| gvwr_toname | VARCHAR | 0.0% |  |  |
| tow_veh | BIGINT | 10.2% | 0 |  |
| tow_vehname | VARCHAR | 0.0% |  |  |
| spec_use | BIGINT | 10.2% | 0 |  |
| spec_usename | VARCHAR | 0.0% |  |  |
| emer_use | BIGINT | 10.2% | 0 |  |
| emer_usename | VARCHAR | 0.0% |  |  |
| rollover | BIGINT | 10.2% | 0 |  |
| rollovername | VARCHAR | 0.0% |  |  |
| impact1 | BIGINT | 10.2% | 0 |  |
| impact1name | VARCHAR | 0.0% |  |  |
| fire_exp | BIGINT | 10.2% | 0 |  |
| fire_expname | VARCHAR | 0.0% |  |  |
| mak_mod | BIGINT | 10.2% | 12002 |  |
| mak_modname | VARCHAR | 0.0% |  |  |
| age | BIGINT | 0.0% | 0 |  |
| agename | VARCHAR | 0.0% | 1 Year |  |
| sex | BIGINT | 0.0% | 1 |  |
| sexname | VARCHAR | 0.0% | Female |  |
| per_typ | BIGINT | 0.0% | 1 |  |
| per_typname | VARCHAR | 0.0% | Bicyclist |  |
| inj_sev | BIGINT | 0.0% | 0 |  |
| inj_sevname | VARCHAR | 0.0% | Died Prior to Crash* |  |
| seat_pos | BIGINT | 0.0% | 0 |  |
| seat_posname | VARCHAR | 0.0% | Appended to a Motor Vehicle for Motion |  |
| rest_use | BIGINT | 0.0% | 1 |  |
| rest_usename | VARCHAR | 0.0% | Booster Seat |  |
| rest_mis | BIGINT | 0.0% | 0 |  |
| rest_misname | VARCHAR | 0.0% | No Indication of Misuse |  |
| helm_use | BIGINT | 0.0% | 16 |  |
| helm_usename | VARCHAR | 0.0% | DOT-Compliant Motorcycle Helmet |  |
| helm_mis | BIGINT | 0.0% | 0 |  |
| helm_misname | VARCHAR | 0.0% | No Indication of Misuse |  |
| air_bag | BIGINT | 0.0% | 1 |  |
| air_bagname | VARCHAR | 0.0% | Deployed- Combination |  |
| ejection | BIGINT | 0.0% | 0 |  |
| ejectionname | VARCHAR | 0.0% | Ejected - Unknown Degree |  |
| ej_path | BIGINT | 0.0% | 0 |  |
| ej_pathname | VARCHAR | 0.0% | Ejection Path Not Applicable |  |
| extricat | BIGINT | 0.0% | 0 |  |
| extricatname | VARCHAR | 0.0% | Extricated |  |
| drinking | BIGINT | 0.0% | 0 |  |
| drinkingname | VARCHAR | 0.0% | No (Alcohol Not Involved) |  |
| alc_status | BIGINT | 0.0% | 0 |  |
| alc_statusname | VARCHAR | 0.0% | Not Reported |  |
| atst_typ | BIGINT | 0.0% | 0 |  |
| atst_typname | VARCHAR | 0.0% | Blood |  |
| alc_res | BIGINT | 0.0% | 0 |  |
| alc_resname | VARCHAR | 0.0% | 0.000 % BAC |  |
| drugs | BIGINT | 0.0% | 0 |  |
| drugsname | VARCHAR | 0.0% | No (drugs not involved) |  |
| dstatus | BIGINT | 0.0% | 0 |  |
| dstatusname | VARCHAR | 0.0% | Not Reported |  |
| hospital | BIGINT | 0.0% | 0 |  |
| hospitalname | VARCHAR | 0.0% | EMS Air |  |
| doa | BIGINT | 0.0% | 0 |  |
| doaname | VARCHAR | 0.0% | Died En Route |  |
| death_mo | BIGINT | 0.0% | 1 |  |
| death_moname | VARCHAR | 0.0% | April |  |
| death_da | BIGINT | 0.0% | 1 |  |
| death_daname | VARCHAR | 0.0% | 1 |  |
| death_yr | BIGINT | 0.0% | 2024 |  |
| death_yrname | VARCHAR | 0.0% | 2024 |  |
| death_tm | BIGINT | 0.0% | 0 |  |
| death_tmname | VARCHAR | 0.0% | 0 |  |
| death_hr | BIGINT | 0.0% | 0 |  |
| death_hrname | VARCHAR | 0.0% | 0:00-0:59 |  |
| death_mn | BIGINT | 0.0% | 0 |  |
| death_mnname | VARCHAR | 0.0% | 0 |  |
| lag_hrs | BIGINT | 0.0% | 0 |  |
| lag_hrsname | VARCHAR | 0.0% | 0 |  |
| lag_mins | BIGINT | 0.0% | 0 |  |
| lag_minsname | VARCHAR | 0.0% | 0 |  |
| str_veh | BIGINT | 0.0% | 0 |  |
| devtype | BIGINT | 0.0% | 0 |  |
| devtypename | VARCHAR | 0.0% | Bicycle |  |
| devmotor | BIGINT | 0.0% | 0 |  |
| devmotorname | VARCHAR | 0.0% | Motorized |  |
| location | BIGINT | 0.0% | 0 |  |
| locationname | VARCHAR | 0.0% | At Intersection - In Marked Crosswalk |  |
| work_inj | BIGINT | 0.0% | 0 |  |
| work_injname | VARCHAR | 0.0% | No |  |
| hispanic | BIGINT | 0.0% | 0 |  |
| hispanicname | VARCHAR | 0.0% | Central or South American |  |

## code_labels

Distinct observed code/label tuples for 30 selected fields; county/city scoped by state. Four city codes have multiple source labels. Use unambiguous_code_labels for unique lookups. MAK_MOD is combined make/model; this is not a full/historical catalog.

Source file: `Derived from accident/vehicle/person paired NAME columns`
Rows: 10,164

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| table_name | VARCHAR | 0.0% | accident |  |
| column_name | VARCHAR | 0.0% | age |  |
| context_column | VARCHAR | 0.0% |  |  |
| context_value | BIGINT | 0.0% | 0 |  |
| code | BIGINT | 0.0% | 0 | code_labels has variants. Join unambiguous_code_labels using table_name/column_name/context_column/context_value/code; ambiguous city codes are excluded. |
| label | VARCHAR | 0.0% | 0.000 % BAC |  |

## Exact definitions and manual pages

### accident

| Column | Original header | Definition | Manual PDF page |
|---|---|---|---|
| state | STATE | This data element identifies the State in which the crash occurred. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 34 |
| statename | STATENAME | Source label for STATE. This data element identifies the State in which the crash occurred. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 34 |
| st_case | ST_CASE | This data element is the unique case number assigned to each crash. It appears on each data file and is used to merge information from the data files together. | 36 |
| peds | PEDS | This data element is the number of Person Forms (Not a Motor Vehicle Occupant) that are applicable to this case (i.e., non-occupants). | 42 |
| pernotmvit | PERNOTMVIT | This data element is a count of the number of non-motorists in the crash. A non-motorist is defined as a pedestrian, a cyclist, an occupant of a motor vehicle not in-transport, a person riding a horse, an occupant of an animal drawn conveyance, person associated with non-motorist conveyance (e.g., baby carriage, skateboard, wheelchair), or an other non-motorist (e.g., person outside a trafficway, person in a house). | 43 |
| ve_total | VE_TOTAL | This data element is the number of contact motor vehicles that the officer reported on the police crash report as a unit involved in the crash. | 44 |
| ve_forms | VE_FORMS | This data element is a count of the number of motor vehicles in-transport involved in the crash. Legally parked vehicles are not included. | 45 |
| pvh_invl | PVH_INVL | This data element is a count of the number of parked and working vehicles involved in the crash. | 46 |
| persons | PERSONS | This data element is a count of the number of Person Level (Motor Vehicle Occupant) Forms that are applicable to this case (i.e., occupants). | 47 |
| permvit | PERMVIT | This data element is a count of the number of motorists in the crash. A motorist is a driver, passenger, or unknown occupant type of a motor vehicle in-transport. | 48 |
| county | COUNTY | This data element records the location of the unstabilized event with regard to the County. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 49 |
| countyname | COUNTYNAME | Source label for COUNTY. This data element records the location of the unstabilized event with regard to the County. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 49 |
| city | CITY | This data element records the location of the unstabilized event with regard to the City. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 50 |
| cityname | CITYNAME | Source label for CITY. This data element records the location of the unstabilized event with regard to the City. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 50 |
| month | MONTH | This data element records the month in which the crash occurred. | 51 |
| monthname | MONTHNAME | Source label for MONTH. This data element records the month in which the crash occurred. | 51 |
| day | DAY | This data element records the day of the month on which the crash occurred. | 52 |
| dayname | DAYNAME | Source label for DAY. This data element records the day of the month on which the crash occurred. | 52 |
| day_week | DAY_WEEK | This data element records the day of the week on which the crash occurred. | 53 |
| day_weekname | DAY_WEEKNAME | Source label for DAY_WEEK. This data element records the day of the week on which the crash occurred. | 53 |
| year | YEAR | This data element records the year in which the crash occurred. | 54 |
| hour | HOUR | This data element records the hour at which the crash occurred. | 55 |
| hourname | HOURNAME | Source label for HOUR. This data element records the hour at which the crash occurred. | 55 |
| minute | MINUTE | This data element records the minutes after the hour at which the crash occurred. | 56 |
| minutename | MINUTENAME | Source label for MINUTE. This data element records the minutes after the hour at which the crash occurred. | 56 |
| tway_id | TWAY_ID | This data element records the trafficway on which the crash occurred. | 57 |
| tway_id2 | TWAY_ID2 | This data element records the trafficway on which the crash occurred. | 57 |
| route | ROUTE | This data element identifies the route signing designation of the trafficway on which the crash occurred. | 58 |
| routename | ROUTENAME | Source label for ROUTE. This data element identifies the route signing designation of the trafficway on which the crash occurred. | 58 |
| rur_urb | RUR_URB | This data element identifies the classification of the segment of the trafficway on which the crash occurred based on FHWA-approved adjusted Census boundaries of small urban and urbanized areas. | 60 |
| rur_urbname | RUR_URBNAME | Source label for RUR_URB. This data element identifies the classification of the segment of the trafficway on which the crash occurred based on FHWA-approved adjusted Census boundaries of small urban and urbanized areas. | 60 |
| func_sys | FUNC_SYS | This data element identifies the functional classification of the segment of the trafficway on which the crash occurred. | 61 |
| func_sysname | FUNC_SYSNAME | Source label for FUNC_SYS. This data element identifies the functional classification of the segment of the trafficway on which the crash occurred. | 61 |
| rd_owner | RD_OWNER | This data element identifies the entity that has legal ownership of the segment of the trafficway on which the crash occurred. The entity that maintains the trafficway may differ from the owner in some locations. | 62 |
| rd_ownername | RD_OWNERNAME | Source label for RD_OWNER. This data element identifies the entity that has legal ownership of the segment of the trafficway on which the crash occurred. The entity that maintains the trafficway may differ from the owner in some locations. | 62 |
| nhs | NHS | This data element identifies whether this crash occurred on a trafficway that is part of the National Highway System. | 64 |
| nhsname | NHSNAME | Source label for NHS. This data element identifies whether this crash occurred on a trafficway that is part of the National Highway System. | 64 |
| sp_jur | SP_JUR | This data element identifies if the location on the trafficway where the crash occurred qualifies as a Special Jurisdiction even though it may be patrolled by State, county or local police (e.g., all State highways running through Indian Reservations are under the jurisdiction of the Indian Reservation). | 65 |
| sp_jurname | SP_JURNAME | Source label for SP_JUR. This data element identifies if the location on the trafficway where the crash occurred qualifies as a Special Jurisdiction even though it may be patrolled by State, county or local police (e.g., all State highways running through Indian Reservations are under the jurisdiction of the Indian Reservation). | 65 |
| milept | MILEPT | This data element records the milepoint nearest to the location where the crash occurred. | 66 |
| mileptname | MILEPTNAME | Source label for MILEPT. This data element records the milepoint nearest to the location where the crash occurred. | 66 |
| latitude | LATITUDE | This element identifies the location of the crash using Global Position coordinates. This is the position of latitude. | 67 |
| latitudename | LATITUDENAME | Source label for LATITUDE. This element identifies the location of the crash using Global Position coordinates. This is the position of latitude. | 67 |
| longitud | LONGITUD | This element identifies the location of the crash using Global Position coordinates. This is the position of longitude. | 68 |
| longitudname | LONGITUDNAME | Source label for LONGITUD. This element identifies the location of the crash using Global Position coordinates. This is the position of longitude. | 68 |
| harm_ev | HARM_EV | This data element describes the first injury- or-damage producing event of the crash. | 69 |
| harm_evname | HARM_EVNAME | Source label for HARM_EV. This data element describes the first injury- or-damage producing event of the crash. | 69 |
| man_coll | MAN_COLL | This data element describes the orientation of two motor vehicles in-transport when they are involved in the “First Harmful Event” of a collision crash. If the “First Harmful Event” is not a collision between two motor vehicles in-transport, it is classified as such. | 74 |
| man_collname | MAN_COLLNAME | Source label for MAN_COLL. This data element describes the orientation of two motor vehicles in-transport when they are involved in the “First Harmful Event” of a collision crash. If the “First Harmful Event” is not a collision between two motor vehicles in-transport, it is classified as such. | 74 |
| reljct1 | RELJCT1 | This data element identifies the crash’s location with respect to presence in an interchange area. The coding of this data element is done in two sub-fields (see also C20B) and is based on the location of the “First Harmful Event” of the crash. | 76 |
| reljct1name | RELJCT1NAME | Source label for RELJCT1. This data element identifies the crash’s location with respect to presence in an interchange area. The coding of this data element is done in two sub-fields (see also C20B) and is based on the location of the “First Harmful Event” of the crash. | 76 |
| reljct2 | RELJCT2 | This data element identifies the crash’s location with respect to presence in or proximity to components typically in junction or interchange areas. The coding of this data element is done in two sub-fields (see also C20A) and is based on the location of the “First Harmful Event” of the crash. | 77 |
| reljct2name | RELJCT2NAME | Source label for RELJCT2. This data element identifies the crash’s location with respect to presence in or proximity to components typically in junction or interchange areas. The coding of this data element is done in two sub-fields (see also C20A) and is based on the location of the “First Harmful Event” of the crash. | 77 |
| typ_int | TYP_INT | This data element identifies and allows separation of various intersection types. | 79 |
| typ_intname | TYP_INTNAME | Source label for TYP_INT. This data element identifies and allows separation of various intersection types. | 79 |
| rel_road | REL_ROAD | This data element identifies the location of the crash as it relates to its position within or outside the trafficway based on the “First Harmful Event.” | 80 |
| rel_roadname | REL_ROADNAME | Source label for REL_ROAD. This data element identifies the location of the crash as it relates to its position within or outside the trafficway based on the “First Harmful Event.” | 80 |
| wrk_zone | WRK_ZONE | This data element identifies a motor vehicle traffic crash in which the first harmful event occurs within the boundaries of a work zone or on an approach to or exit from a work zone, resulting from an activity, behavior, or control related to the movement of the traffic units through the work zone. | 82 |
| wrk_zonename | WRK_ZONENAME | Source label for WRK_ZONE. This data element identifies a motor vehicle traffic crash in which the first harmful event occurs within the boundaries of a work zone or on an approach to or exit from a work zone, resulting from an activity, behavior, or control related to the movement of the traffic units through the work zone. | 82 |
| lgt_cond | LGT_COND | This data element records the type/level of light that existed at the time of the crash as indicated in the case material. | 83 |
| lgt_condname | LGT_CONDNAME | Source label for LGT_COND. This data element records the type/level of light that existed at the time of the crash as indicated in the case material. | 83 |
| weather | WEATHER | This derived data element records the prevailing atmospheric conditions that existed at the time of the crash as indicated in the case material. | 84 |
| weathername | WEATHERNAME | Source label for WEATHER. This derived data element records the prevailing atmospheric conditions that existed at the time of the crash as indicated in the case material. | 84 |
| sch_bus | SCH_BUS | This data element identifies if a school bus, or motor vehicle functioning as a school bus, is related to the crash. | 86 |
| sch_busname | SCH_BUSNAME | Source label for SCH_BUS. This data element identifies if a school bus, or motor vehicle functioning as a school bus, is related to the crash. | 86 |
| rail | RAIL | This data element identifies if the crash occurred in or near a rail grade crossing. | 87 |
| railname | RAILNAME | Source label for RAIL. This data element identifies if the crash occurred in or near a rail grade crossing. | 87 |
| not_hour | NOT_HOUR | This data element records the hour that emergency medical service was notified. | 88 |
| not_hourname | NOT_HOURNAME | Source label for NOT_HOUR. This data element records the hour that emergency medical service was notified. | 88 |
| not_min | NOT_MIN | This data element records the minutes after the hour that emergency medical service was notified. | 89 |
| not_minname | NOT_MINNAME | Source label for NOT_MIN. This data element records the minutes after the hour that emergency medical service was notified. | 89 |
| arr_hour | ARR_HOUR | This data element records the hour that emergency medical service arrived on the crash scene. | 90 |
| arr_hourname | ARR_HOURNAME | Source label for ARR_HOUR. This data element records the hour that emergency medical service arrived on the crash scene. | 90 |
| arr_min | ARR_MIN | This data element records the minutes after the hour that emergency medical service arrived on the crash scene. | 91 |
| arr_minname | ARR_MINNAME | Source label for ARR_MIN. This data element records the minutes after the hour that emergency medical service arrived on the crash scene. | 91 |
| hosp_hr | HOSP_HR | This data element records the hour that emergency medical service arrived at the treatment facility to which it was transporting victims of the crash. | 92 |
| hosp_hrname | HOSP_HRNAME | Source label for HOSP_HR. This data element records the hour that emergency medical service arrived at the treatment facility to which it was transporting victims of the crash. | 92 |
| hosp_mn | HOSP_MN | This data element records the minutes after the hour that emergency medical service arrived at the treatment facility to which it was transporting victims of the crash. | 93 |
| hosp_mnname | HOSP_MNNAME | Source label for HOSP_MN. This data element records the minutes after the hour that emergency medical service arrived at the treatment facility to which it was transporting victims of the crash. | 93 |
| fatals | FATALS | This data element records the number of fatally injured people in the crash. | 94 |

### vehicle

| Column | Original header | Definition | Manual PDF page |
|---|---|---|---|
| state | STATE | This data element identifies the State in which the crash occurred. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 34 |
| statename | STATENAME | Source label for STATE. This data element identifies the State in which the crash occurred. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 34 |
| st_case | ST_CASE | This data element is the unique case number assigned to each crash. It appears on each data file and is used to merge information from the data files together. | 36 |
| veh_no | VEH_NO | This data element is the consecutive number assigned to each vehicle in the case. This data element appears on each vehicle level data file and is used in conjunction with the ST_CASE data element to merge information from vehicle level data files. | 37 |
| ve_forms | VE_FORMS | This data element is a count of the number of motor vehicles in-transport involved in the crash. Legally parked vehicles are not included. | 45 |
| month | MONTH | This data element records the month in which the crash occurred. | 51 |
| monthname | MONTHNAME | Source label for MONTH. This data element records the month in which the crash occurred. | 51 |
| day | DAY | This data element records the day of the month on which the crash occurred. | 52 |
| dayname | DAYNAME | Source label for DAY. This data element records the day of the month on which the crash occurred. | 52 |
| hour | HOUR | This data element records the hour at which the crash occurred. | 55 |
| hourname | HOURNAME | Source label for HOUR. This data element records the hour at which the crash occurred. | 55 |
| minute | MINUTE | This data element records the minutes after the hour at which the crash occurred. | 56 |
| minutename | MINUTENAME | Source label for MINUTE. This data element records the minutes after the hour at which the crash occurred. | 56 |
| harm_ev | HARM_EV | This data element describes the first injury- or-damage producing event of the crash. | 69 |
| harm_evname | HARM_EVNAME | Source label for HARM_EV. This data element describes the first injury- or-damage producing event of the crash. | 69 |
| man_coll | MAN_COLL | This data element describes the orientation of two motor vehicles in-transport when they are involved in the “First Harmful Event” of a collision crash. If the “First Harmful Event” is not a collision between two motor vehicles in-transport, it is classified as such. | 74 |
| man_collname | MAN_COLLNAME | Source label for MAN_COLL. This data element describes the orientation of two motor vehicles in-transport when they are involved in the “First Harmful Event” of a collision crash. If the “First Harmful Event” is not a collision between two motor vehicles in-transport, it is classified as such. | 74 |
| numoccs | NUMOCCS | This data element is a count of the number of occupants in this vehicle. | 115 |
| numoccsname | NUMOCCSNAME | Source label for NUMOCCS. This data element is a count of the number of occupants in this vehicle. | 115 |
| unittype | UNITTYPE | This data element identifies the type of unit that applies to this motor vehicle at the time it became an involved vehicle in the crash and was reported as a unit on the police crash report. | 116 |
| unittypename | UNITTYPENAME | Source label for UNITTYPE. This data element identifies the type of unit that applies to this motor vehicle at the time it became an involved vehicle in the crash and was reported as a unit on the police crash report. | 116 |
| hit_run | HIT_RUN | This data element identifies whether this vehicle was a contact vehicle in the crash that did not stop to render aid (this can include drivers who flee the scene on foot). Hit-and-run is coded when a motor vehicle in-transport or its driver departs from the scene; vehicles not in-transport are excluded. It does not matter whether the hit-and-run vehicle was striking or struck. | 97 |
| hit_runname | HIT_RUNNAME | Source label for HIT_RUN. This data element identifies whether this vehicle was a contact vehicle in the crash that did not stop to render aid (this can include drivers who flee the scene on foot). Hit-and-run is coded when a motor vehicle in-transport or its driver departs from the scene; vehicles not in-transport are excluded. It does not matter whether the hit-and-run vehicle was striking or struck. | 97 |
| reg_stat | REG_STAT | This element identifies the State in which this vehicle was registered. | 119 |
| reg_statname | REG_STATNAME | Source label for REG_STAT. This element identifies the State in which this vehicle was registered. | 119 |
| owner | OWNER | This data element identifies the type of registered owner of the vehicle. | 122 |
| ownername | OWNERNAME | Source label for OWNER. This data element identifies the type of registered owner of the vehicle. | 122 |
| vin | VIN | This data element records the vehicle identification number (VIN) of this vehicle assigned by the vehicle manufacturer. The VIN contains information on the vehicle such as: manufacturer, model year, model, body type, restraint type, etc. | 123 |
| vinname | VINNAME | Source label for VIN. This data element records the vehicle identification number (VIN) of this vehicle assigned by the vehicle manufacturer. The VIN contains information on the vehicle such as: manufacturer, model year, model, body type, restraint type, etc. | 123 |
| mod_year | MOD_YEAR | This data element identifies the manufacturer’s model year of this vehicle. | 124 |
| mod_yearname | MOD_YEARNAME | Source label for MOD_YEAR. This data element identifies the manufacturer’s model year of this vehicle. | 124 |
| vpicmake | VPICMAKE | This element identifies the Make (manufacturer brand name) of this vehicle as per NHTSA vPIC submissions. | 125 |
| vpicmakename | VPICMAKENAME | Source label for VPICMAKE. This element identifies the Make (manufacturer brand name) of this vehicle as per NHTSA vPIC submissions. | 125 |
| vpicmodel | VPICMODEL | This element identifies the Model of this vehicle using NHTSA’s VIN decoder application, vPIC. | 126 |
| vpicmodelname | VPICMODELNAME | Source label for VPICMODEL. This element identifies the Model of this vehicle using NHTSA’s VIN decoder application, vPIC. | 126 |
| vpicbodyclass | VPICBODYCLASS | This element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc., as defined by the manufacturer. | 128 |
| vpicbodyclassname | VPICBODYCLASSNAME | Source label for VPICBODYCLASS. This element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc., as defined by the manufacturer. | 128 |
| make | MAKE | This data element identifies the make (manufacturer) of this vehicle by NCSA historically. | 131 |
| makename | MAKENAME | Source label for MAKE. This data element identifies the make (manufacturer) of this vehicle by NCSA historically. | 131 |
| model | MODEL | This data element identifies the NCSA model of this vehicle within a given NCSA make. | 137 |
| body_typ | BODY_TYP | This data element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc. as defined by NCSA. | 138 |
| body_typname | BODY_TYPNAME | Source label for BODY_TYP. This data element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc. as defined by NCSA. | 138 |
| icfinalbody | ICFINALBODY | This element captures the completed/finished body class for an incomplete vehicle. An incomplete vehicle is completed by a final stage manufacturer. The intent of this data element is to capture the body class for incomplete vehicles when they are finished for road use. | 146 |
| icfinalbodyname | ICFINALBODYNAME | Source label for ICFINALBODY. This element captures the completed/finished body class for an incomplete vehicle. An incomplete vehicle is completed by a final stage manufacturer. The intent of this data element is to capture the body class for incomplete vehicles when they are finished for road use. | 146 |
| gvwr_from | GVWR_FROM | This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| gvwr_fromname | GVWR_FROMNAME | Source label for GVWR_FROM. This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| gvwr_to | GVWR_TO | This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| gvwr_toname | GVWR_TONAME | Source label for GVWR_TO. This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| tow_veh | TOW_VEH | This data element identifies whether this vehicle had any attached trailing units or was towing another motor vehicle. | 149 |
| tow_vehname | TOW_VEHNAME | Source label for TOW_VEH. This data element identifies whether this vehicle had any attached trailing units or was towing another motor vehicle. | 149 |
| trlr1vin | TRLR1VIN | This data element records the vehicle identification number (VIN) of any trailing units of a combination vehicle. | 151 |
| trlr1vinname | TRLR1VINNAME | Source label for TRLR1VIN. This data element records the vehicle identification number (VIN) of any trailing units of a combination vehicle. | 151 |
| trlr2vin | TRLR2VIN | This data element records the vehicle identification number (VIN) of any trailing units of a combination vehicle. | 151 |
| trlr2vinname | TRLR2VINNAME | Source label for TRLR2VIN. This data element records the vehicle identification number (VIN) of any trailing units of a combination vehicle. | 151 |
| trlr3vin | TRLR3VIN | This data element records the vehicle identification number (VIN) of any trailing units of a combination vehicle. | 151 |
| trlr3vinname | TRLR3VINNAME | Source label for TRLR3VIN. This data element records the vehicle identification number (VIN) of any trailing units of a combination vehicle. | 151 |
| trlr1gvwr | TRLR1GVWR | This element identifies the gross vehicle weight rating of any trailing units as identified by the manufacturer in the vehicle’s VIN. | 152 |
| trlr1gvwrname | TRLR1GVWRNAME | Source label for TRLR1GVWR. This element identifies the gross vehicle weight rating of any trailing units as identified by the manufacturer in the vehicle’s VIN. | 152 |
| trlr2gvwr | TRLR2GVWR | This element identifies the gross vehicle weight rating of any trailing units as identified by the manufacturer in the vehicle’s VIN. | 152 |
| trlr2gvwrname | TRLR2GVWRNAME | Source label for TRLR2GVWR. This element identifies the gross vehicle weight rating of any trailing units as identified by the manufacturer in the vehicle’s VIN. | 152 |
| trlr3gvwr | TRLR3GVWR | This element identifies the gross vehicle weight rating of any trailing units as identified by the manufacturer in the vehicle’s VIN. | 152 |
| trlr3gvwrname | TRLR3GVWRNAME | Source label for TRLR3GVWR. This element identifies the gross vehicle weight rating of any trailing units as identified by the manufacturer in the vehicle’s VIN. | 152 |
| j_knife | J_KNIFE | This data element identifies whether this vehicle experienced a jackknife anytime during the unstabilized situation. | 153 |
| j_knifename | J_KNIFENAME | Source label for J_KNIFE. This data element identifies whether this vehicle experienced a jackknife anytime during the unstabilized situation. | 153 |
| mcarr_id | MCARR_ID | This data element records the issuing authority and motor carrier identification number (if applicable) to this vehicle. | 154 |
| mcarr_idname | MCARR_IDNAME | Source label for MCARR_ID. This data element records the issuing authority and motor carrier identification number (if applicable) to this vehicle. | 154 |
| mcarr_i1 | MCARR_I1 | This data element records the issuing authority if applicable to this vehicle. | 155 |
| mcarr_i1name | MCARR_I1NAME | Source label for MCARR_I1. This data element records the issuing authority if applicable to this vehicle. | 155 |
| mcarr_i2 | MCARR_I2 | This data element records the motor carrier identification number if applicable to this vehicle. | 156 |
| mcarr_i2name | MCARR_I2NAME | Source label for MCARR_I2. This data element records the motor carrier identification number if applicable to this vehicle. | 156 |
| v_config | V_CONFIG | This data element describes the general configuration of this vehicle if applicable. | 157 |
| v_configname | V_CONFIGNAME | Source label for V_CONFIG. This data element describes the general configuration of this vehicle if applicable. | 157 |
| cargo_bt | CARGO_BT | This data element describes the primary cargo carrying capability of this vehicle if applicable. | 159 |
| cargo_btname | CARGO_BTNAME | Source label for CARGO_BT. This data element describes the primary cargo carrying capability of this vehicle if applicable. | 159 |
| haz_inv | HAZ_INV | This data element identifies whether this vehicle was carrying hazardous materials. | 161 |
| haz_invname | HAZ_INVNAME | Source label for HAZ_INV. This data element identifies whether this vehicle was carrying hazardous materials. | 161 |
| haz_plac | HAZ_PLAC | This data element identifies the presence of hazardous materials for this vehicle and whether this vehicle displayed a hazardous materials placard. | 162 |
| haz_placname | HAZ_PLACNAME | Source label for HAZ_PLAC. This data element identifies the presence of hazardous materials for this vehicle and whether this vehicle displayed a hazardous materials placard. | 162 |
| haz_id | HAZ_ID | This data element identifies the four-digit hazardous materials identification number for this vehicle. | 163 |
| haz_idname | HAZ_IDNAME | Source label for HAZ_ID. This data element identifies the four-digit hazardous materials identification number for this vehicle. | 163 |
| haz_cno | HAZ_CNO | This data element identifies the single-digit hazardous materials class number for this vehicle. | 164 |
| haz_cnoname | HAZ_CNONAME | Source label for HAZ_CNO. This data element identifies the single-digit hazardous materials class number for this vehicle. | 164 |
| haz_rel | HAZ_REL | This data element identifies whether any hazardous cargo was released from the cargo tank or compartment of this vehicle. | 165 |
| haz_relname | HAZ_RELNAME | Source label for HAZ_REL. This data element identifies whether any hazardous cargo was released from the cargo tank or compartment of this vehicle. | 165 |
| bus_use | BUS_USE | This data element describes the common type of bus service this vehicle was being used as at the time of the crash or the primary use for the bus if not in service at the time of the crash. | 166 |
| bus_usename | BUS_USENAME | Source label for BUS_USE. This data element describes the common type of bus service this vehicle was being used as at the time of the crash or the primary use for the bus if not in service at the time of the crash. | 166 |
| spec_use | SPEC_USE | This data element identifies any special use associated with this vehicle at the time of the crash. | 167 |
| spec_usename | SPEC_USENAME | Source label for SPEC_USE. This data element identifies any special use associated with this vehicle at the time of the crash. | 167 |
| emer_use | EMER_USE | This data element identifies whether this vehicle was engaged in emergency use. Emergency Motor Vehicle Use indicates operation of any motor vehicle that is legally authorized by a government authority to respond to emergencies while actually engaged in such response. These vehicles can respond with or without the use of emergency warning equipment. | 169 |
| emer_usename | EMER_USENAME | Source label for EMER_USE. This data element identifies whether this vehicle was engaged in emergency use. Emergency Motor Vehicle Use indicates operation of any motor vehicle that is legally authorized by a government authority to respond to emergencies while actually engaged in such response. These vehicles can respond with or without the use of emergency warning equipment. | 169 |
| trav_sp | TRAV_SP | This data element records the speed the vehicle was traveling prior to the occurrence of the crash as reported by the investigating officer. | 170 |
| trav_spname | TRAV_SPNAME | Source label for TRAV_SP. This data element records the speed the vehicle was traveling prior to the occurrence of the crash as reported by the investigating officer. | 170 |
| underoverride | UNDEROVERRIDE | This element indicates whether this vehicle experienced an underride or override with another vehicle during the crash. | 171 |
| underoverridename | UNDEROVERRIDENAME | Source label for UNDEROVERRIDE. This element indicates whether this vehicle experienced an underride or override with another vehicle during the crash. | 171 |
| rollover | ROLLOVER | This data element identifies this vehicle’s involvement in a rollover or overturn during the crash. Rollover is defined as any vehicle rotation of 90° or more about any true longitudinal or lateral axis. Rollover can occur at any time during the crash. | 172 |
| rollovername | ROLLOVERNAME | Source label for ROLLOVER. This data element identifies this vehicle’s involvement in a rollover or overturn during the crash. Rollover is defined as any vehicle rotation of 90° or more about any true longitudinal or lateral axis. Rollover can occur at any time during the crash. | 172 |
| rolinloc | ROLINLOC | This data element identifies the location of the trip point or start of this vehicle’s roll. | 173 |
| rolinlocname | ROLINLOCNAME | Source label for ROLINLOC. This data element identifies the location of the trip point or start of this vehicle’s roll. | 173 |
| impact1 | IMPACT1 | This data element identifies the area on this vehicle that produced the first instance of injury to non-motorists or occupants of this vehicle, or that resulted in the first instance of damage to other property or to this vehicle. | 174 |
| impact1name | IMPACT1NAME | Source label for IMPACT1. This data element identifies the area on this vehicle that produced the first instance of injury to non-motorists or occupants of this vehicle, or that resulted in the first instance of damage to other property or to this vehicle. | 174 |
| deformed | DEFORMED | This data element records the amount of damage sustained by this vehicle as indicated in the case material based on an operational damage scale. | 176 |
| deformedname | DEFORMEDNAME | Source label for DEFORMED. This data element records the amount of damage sustained by this vehicle as indicated in the case material based on an operational damage scale. | 176 |
| towed | TOWED | This data element identifies whether the vehicle was towed from the scene of the crash. | 177 |
| towedname | TOWEDNAME | Source label for TOWED. This data element identifies whether the vehicle was towed from the scene of the crash. | 177 |
| m_harm | M_HARM | This data element describes the event that resulted in the most severe injury or, if no injury, the greatest property damage involving this vehicle. | 178 |
| m_harmname | M_HARMNAME | Source label for M_HARM. This data element describes the event that resulted in the most severe injury or, if no injury, the greatest property damage involving this vehicle. | 178 |
| fire_exp | FIRE_EXP | This data element identifies whether a fire in any way related to the crash occurred in this vehicle. | 183 |
| fire_expname | FIRE_EXPNAME | Source label for FIRE_EXP. This data element identifies whether a fire in any way related to the crash occurred in this vehicle. | 183 |
| mak_mod | MAK_MOD | This derived data element represents the five-digit combination of two data elements, the two- digit “NCSA Make” code (MAKE) followed by the three-digit “NCSA Model” code (MODEL). | 187 |
| mak_modname | MAK_MODNAME | Source label for MAK_MOD. This derived data element represents the five-digit combination of two data elements, the two- digit “NCSA Make” code (MAKE) followed by the three-digit “NCSA Model” code (MODEL). | 187 |
| vin_1 | VIN_1 | This data element represents the first character in the VIN string for this vehicle. | 188 |
| vin_2 | VIN_2 | This data element represents the second character in the VIN string for this vehicle. | 189 |
| vin_3 | VIN_3 | This data element represents the third character in the VIN string for this vehicle. | 190 |
| vin_4 | VIN_4 | This data element represents the fourth character in the VIN string for this vehicle. | 191 |
| vin_5 | VIN_5 | This data element represents the fifth character in the VIN string for this vehicle. | 192 |
| vin_6 | VIN_6 | This data element represents the sixth character in the VIN string for this vehicle. | 193 |
| vin_7 | VIN_7 | This data element represents the seventh character in the VIN string for this vehicle. | 194 |
| vin_8 | VIN_8 | This data element represents the eighth character in the VIN string for this vehicle. | 195 |
| vin_9 | VIN_9 | This data element represents the ninth character in the VIN string for this vehicle. | 196 |
| vin_10 | VIN_10 | This data element represents the tenth character in the VIN string for this vehicle. | 197 |
| vin_11 | VIN_11 | This data element represents the eleventh character in the VIN string for this vehicle. | 198 |
| vin_12 | VIN_12 | This data element represents the twelfth character in the VIN string for this vehicle. | 199 |
| deaths | DEATHS | This data element records the number of fatalities that occurred in this vehicle. | 200 |
| dr_drink | DR_DRINK | This data element records whether the driver was drinking. | 201 |
| dr_drinkname | DR_DRINKNAME | Source label for DR_DRINK. This data element records whether the driver was drinking. | 201 |
| dr_pres | DR_PRES | This data element identifies whether a driver was present in this vehicle at the onset of the unstabilized situation. | 202 |
| dr_presname | DR_PRESNAME | Source label for DR_PRES. This data element identifies whether a driver was present in this vehicle at the onset of the unstabilized situation. | 202 |
| l_state | L_STATE | This element identifies the State of issue for the license held by this driver. | 203 |
| l_statename | L_STATENAME | Source label for L_STATE. This element identifies the State of issue for the license held by this driver. | 203 |
| dr_zip | DR_ZIP | This data element records the ZIP Code of the driver’s address as listed in the case material. | 206 |
| dr_zipname | DR_ZIPNAME | Source label for DR_ZIP. This data element records the ZIP Code of the driver’s address as listed in the case material. | 206 |
| l_type | L_TYPE | This data element identifies the type of license held by this driver at the time of the crash. | 207 |
| l_typename | L_TYPENAME | Source label for L_TYPE. This data element identifies the type of license held by this driver at the time of the crash. | 207 |
| l_status | L_STATUS | This data element identifies the status of the driver’s license at the time of the crash. | 208 |
| l_statusname | L_STATUSNAME | Source label for L_STATUS. This data element identifies the status of the driver’s license at the time of the crash. | 208 |
| cdl_stat | CDL_STAT | This data element indicates the status of the driver’s commercial driver’s license (CDL) if applicable. | 210 |
| cdl_statname | CDL_STATNAME | Source label for CDL_STAT. This data element indicates the status of the driver’s commercial driver’s license (CDL) if applicable. | 210 |
| l_endors | L_ENDORS | This data element identifies whether the vehicle driven at the time of the crash required endorsements on a commercial driver’s license (CDL) and whether this driver was complying with the CDL endorsements. | 211 |
| l_endorsname | L_ENDORSNAME | Source label for L_ENDORS. This data element identifies whether the vehicle driven at the time of the crash required endorsements on a commercial driver’s license (CDL) and whether this driver was complying with the CDL endorsements. | 211 |
| l_compl | L_COMPL | This data element identifies the type of license possessed or not possessed by this driver for the class of vehicle being driven at the time of the crash. | 212 |
| l_complname | L_COMPLNAME | Source label for L_COMPL. This data element identifies the type of license possessed or not possessed by this driver for the class of vehicle being driven at the time of the crash. | 212 |
| l_restri | L_RESTRI | This data element indicates whether this driver was compliant with restrictions on their license. | 213 |
| l_restriname | L_RESTRINAME | Source label for L_RESTRI. This data element indicates whether this driver was compliant with restrictions on their license. | 213 |
| dr_hgt | DR_HGT | This data element identifies this driver’s height (in inches). | 214 |
| dr_hgtname | DR_HGTNAME | Source label for DR_HGT. This data element identifies this driver’s height (in inches). | 214 |
| dr_wgt | DR_WGT | This data element identifies this driver’s weight (in pounds). | 215 |
| dr_wgtname | DR_WGTNAME | Source label for DR_WGT. This data element identifies this driver’s weight (in pounds). | 215 |
| prev_acc | PREV_ACC | This data element records any previous crashes for this driver that occurred within 5 years of the crash date. | 216 |
| prev_accname | PREV_ACCNAME | Source label for PREV_ACC. This data element records any previous crashes for this driver that occurred within 5 years of the crash date. | 216 |
| prev_sus1 | PREV_SUS1 | This data element records any underage pre-conviction administrative license suspension, revocation, or withdrawal in the 5 years prior to the crash date including those for zero-tolerance alcohol violations while driving or refusing to submit to chemical testing. This element is only for administrative actions associated with alcohol. These are NOT BAC convictions. | 217 |
| prev_sus1name | PREV_SUS1NAME | Source label for PREV_SUS1. This data element records any underage pre-conviction administrative license suspension, revocation, or withdrawal in the 5 years prior to the crash date including those for zero-tolerance alcohol violations while driving or refusing to submit to chemical testing. This element is only for administrative actions associated with alcohol. These are NOT BAC convictions. | 217 |
| prev_sus2 | PREV_SUS2 | This data element records the count of previous pre-conviction administratively imposed suspensions, revocations, or withdrawals within the 5 years prior to the crash date for driving with a BAC above a specified limit or refusing to submit to chemical testing. This element is only for administrative actions associated with alcohol. These are NOT BAC convictions. | 218 |
| prev_sus2name | PREV_SUS2NAME | Source label for PREV_SUS2. This data element records the count of previous pre-conviction administratively imposed suspensions, revocations, or withdrawals within the 5 years prior to the crash date for driving with a BAC above a specified limit or refusing to submit to chemical testing. This element is only for administrative actions associated with alcohol. These are NOT BAC convictions. | 218 |
| prev_sus3 | PREV_SUS3 | This data element records any previous license suspensions, revocations, or withdrawals for this driver other than Administrative action for BAC violations within 5 years from the crash date. This element would include administrative actions associated with drugged driving. | 219 |
| prev_sus3name | PREV_SUS3NAME | Source label for PREV_SUS3. This data element records any previous license suspensions, revocations, or withdrawals for this driver other than Administrative action for BAC violations within 5 years from the crash date. This element would include administrative actions associated with drugged driving. | 219 |
| prev_dwi | PREV_DWI | This data element records any previous DWI convictions for this driver that occurred within 5 years of the crash date. | 220 |
| prev_dwiname | PREV_DWINAME | Source label for PREV_DWI. This data element records any previous DWI convictions for this driver that occurred within 5 years of the crash date. | 220 |
| prev_spd | PREV_SPD | This data element records any previous speeding convictions for this driver that occurred within 5 years of the crash date. | 221 |
| prev_spdname | PREV_SPDNAME | Source label for PREV_SPD. This data element records any previous speeding convictions for this driver that occurred within 5 years of the crash date. | 221 |
| prev_oth | PREV_OTH | This data element records any other previous moving violations or convictions for this driver that occurred within 5 years of the crash date. | 222 |
| prev_othname | PREV_OTHNAME | Source label for PREV_OTH. This data element records any other previous moving violations or convictions for this driver that occurred within 5 years of the crash date. | 222 |
| first_mo | FIRST_MO | This data element records the month of the first crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 223 |
| first_moname | FIRST_MONAME | Source label for FIRST_MO. This data element records the month of the first crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 223 |
| first_yr | FIRST_YR | This data element records the year of the first crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 224 |
| first_yrname | FIRST_YRNAME | Source label for FIRST_YR. This data element records the year of the first crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 224 |
| last_mo | LAST_MO | This data element records the month of the last crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 225 |
| last_moname | LAST_MONAME | Source label for LAST_MO. This data element records the month of the last crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 225 |
| last_yr | LAST_YR | This data element records the year of the last crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 226 |
| last_yrname | LAST_YRNAME | Source label for LAST_YR. This data element records the year of the last crash, suspension, or conviction for this driver that occurred within 5 years of the crash date. | 226 |
| speedrel | SPEEDREL | This data element identifies if the driver was speeding, and it was related to the crash as identified by law enforcement. | 227 |
| speedrelname | SPEEDRELNAME | Source label for SPEEDREL. This data element identifies if the driver was speeding, and it was related to the crash as identified by law enforcement. | 227 |
| vtrafway | VTRAFWAY | This data element identifies the attribute that best describes the trafficway flow just prior to this vehicle’s critical precrash event. | 228 |
| vtrafwayname | VTRAFWAYNAME | Source label for VTRAFWAY. This data element identifies the attribute that best describes the trafficway flow just prior to this vehicle’s critical precrash event. | 228 |
| vnum_lan | VNUM_LAN | This data element identifies the attribute that best describes the number of travel lanes just prior to this vehicle’s critical precrash event. | 229 |
| vnum_lanname | VNUM_LANNAME | Source label for VNUM_LAN. This data element identifies the attribute that best describes the number of travel lanes just prior to this vehicle’s critical precrash event. | 229 |
| vspd_lim | VSPD_LIM | This data element identifies the attribute that best represents the speed limit just prior to this vehicle’s critical precrash event. | 230 |
| vspd_limname | VSPD_LIMNAME | Source label for VSPD_LIM. This data element identifies the attribute that best represents the speed limit just prior to this vehicle’s critical precrash event. | 230 |
| valign | VALIGN | This data element identifies the attribute that best represents the roadway alignment prior to this vehicle’s critical precrash event. | 231 |
| valignname | VALIGNNAME | Source label for VALIGN. This data element identifies the attribute that best represents the roadway alignment prior to this vehicle’s critical precrash event. | 231 |
| vprofile | VPROFILE | This data element identifies the attribute that best represents the roadway grade prior to this vehicle’s critical precrash event. | 232 |
| vprofilename | VPROFILENAME | Source label for VPROFILE. This data element identifies the attribute that best represents the roadway grade prior to this vehicle’s critical precrash event. | 232 |
| vpavetyp | VPAVETYP | This data element identifies the attribute that best represents the roadway surface type prior to this vehicle’s critical precrash event. | 233 |
| vpavetypname | VPAVETYPNAME | Source label for VPAVETYP. This data element identifies the attribute that best represents the roadway surface type prior to this vehicle’s critical precrash event. | 233 |
| vsurcond | VSURCOND | This data element identifies the attribute that best represents the roadway surface condition prior to this vehicle’s critical precrash event. | 234 |
| vsurcondname | VSURCONDNAME | Source label for VSURCOND. This data element identifies the attribute that best represents the roadway surface condition prior to this vehicle’s critical precrash event. | 234 |
| vtrafcon | VTRAFCON | This data element identifies the attribute that best describes the traffic controls in the vehicle’s environment just prior to this vehicle’s critical precrash event. | 235 |
| vtrafconname | VTRAFCONNAME | Source label for VTRAFCON. This data element identifies the attribute that best describes the traffic controls in the vehicle’s environment just prior to this vehicle’s critical precrash event. | 235 |
| vtcont_f | VTCONT_F | This data element identifies the functionality of the traffic control device recorded for this vehicle in the data element “Traffic Control Device.” | 237 |
| vtcont_fname | VTCONT_FNAME | Source label for VTCONT_F. This data element identifies the functionality of the traffic control device recorded for this vehicle in the data element “Traffic Control Device.” | 237 |
| p_crash1 | P_CRASH1 | This data element identifies the attribute that best describes this vehicle’s activity prior to the driver’s realization of an impending critical event or just prior to impact if the driver took no action or had no time to attempt any evasive maneuvers. | 238 |
| p_crash1name | P_CRASH1NAME | Source label for P_CRASH1. This data element identifies the attribute that best describes this vehicle’s activity prior to the driver’s realization of an impending critical event or just prior to impact if the driver took no action or had no time to attempt any evasive maneuvers. | 238 |
| p_crash2 | P_CRASH2 | This data element identifies the attribute that best describes the critical event that made this crash imminent (i.e., something occurred that made the collision possible). | 240 |
| p_crash2name | P_CRASH2NAME | Source label for P_CRASH2. This data element identifies the attribute that best describes the critical event that made this crash imminent (i.e., something occurred that made the collision possible). | 240 |
| p_crash3 | P_CRASH3 | This data element identifies the attribute that best describes the movements/actions taken by this driver, within a critical crash envelope, in response to the “Critical Precrash Event.” | 244 |
| p_crash3name | P_CRASH3NAME | Source label for P_CRASH3. This data element identifies the attribute that best describes the movements/actions taken by this driver, within a critical crash envelope, in response to the “Critical Precrash Event.” | 244 |
| pcrash4 | PCRASH4 | This data element identifies the attribute that best describes the stability of this vehicle after the “Critical Precrash Event,” but before the impact. | 245 |
| pcrash4name | PCRASH4NAME | Source label for PCRASH4. This data element identifies the attribute that best describes the stability of this vehicle after the “Critical Precrash Event,” but before the impact. | 245 |
| pcrash5 | PCRASH5 | This data element identifies the attribute that best describes the location of this vehicle after the “Critical Precrash Event,” but before the impact. | 246 |
| pcrash5name | PCRASH5NAME | Source label for PCRASH5. This data element identifies the attribute that best describes the location of this vehicle after the “Critical Precrash Event,” but before the impact. | 246 |
| acc_type | ACC_TYPE | This data element identifies the attribute that best describes the type of crash this vehicle was involved in based on the “First Harmful Event” and the precrash circumstances. | 247 |
| acc_typename | ACC_TYPENAME | Source label for ACC_TYPE. This data element identifies the attribute that best describes the type of crash this vehicle was involved in based on the “First Harmful Event” and the precrash circumstances. | 247 |

### person

| Column | Original header | Definition | Manual PDF page |
|---|---|---|---|
| state | STATE | This data element identifies the State in which the crash occurred. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 34 |
| statename | STATENAME | Source label for STATE. This data element identifies the State in which the crash occurred. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 34 |
| st_case | ST_CASE | This data element is the unique case number assigned to each crash. It appears on each data file and is used to merge information from the data files together. | 36 |
| veh_no | VEH_NO | This data element is the consecutive number assigned to each vehicle in the case. This data element appears on each vehicle level data file and is used in conjunction with the ST_CASE data element to merge information from vehicle level data files. | 37 |
| per_no | PER_NO | This data element is the consecutive number assigned to each person in the case (i.e., each occupant, pedestrian, or non-motorists involved in the crash). This data element appears on each person level data file and is used in conjunction with the ST_CASE data element (and sometimes the VEH_NO data element) to merge information from person level data files. | 38 |
| ve_forms | VE_FORMS | This data element is a count of the number of motor vehicles in-transport involved in the crash. Legally parked vehicles are not included. | 45 |
| county | COUNTY | This data element records the location of the unstabilized event with regard to the County. The codes are from the General Services Administration’s (GSA) publication of worldwide Geographic Location Codes (GLC). | 49 |
| month | MONTH | This data element records the month in which the crash occurred. | 51 |
| monthname | MONTHNAME | Source label for MONTH. This data element records the month in which the crash occurred. | 51 |
| day | DAY | This data element records the day of the month on which the crash occurred. | 52 |
| dayname | DAYNAME | Source label for DAY. This data element records the day of the month on which the crash occurred. | 52 |
| hour | HOUR | This data element records the hour at which the crash occurred. | 55 |
| hourname | HOURNAME | Source label for HOUR. This data element records the hour at which the crash occurred. | 55 |
| minute | MINUTE | This data element records the minutes after the hour at which the crash occurred. | 56 |
| minutename | MINUTENAME | Source label for MINUTE. This data element records the minutes after the hour at which the crash occurred. | 56 |
| harm_ev | HARM_EV | This data element describes the first injury- or-damage producing event of the crash. | 69 |
| harm_evname | HARM_EVNAME | Source label for HARM_EV. This data element describes the first injury- or-damage producing event of the crash. | 69 |
| man_coll | MAN_COLL | This data element describes the orientation of two motor vehicles in-transport when they are involved in the “First Harmful Event” of a collision crash. If the “First Harmful Event” is not a collision between two motor vehicles in-transport, it is classified as such. | 74 |
| man_collname | MAN_COLLNAME | Source label for MAN_COLL. This data element describes the orientation of two motor vehicles in-transport when they are involved in the “First Harmful Event” of a collision crash. If the “First Harmful Event” is not a collision between two motor vehicles in-transport, it is classified as such. | 74 |
| sch_bus | SCH_BUS | This data element identifies if a school bus, or motor vehicle functioning as a school bus, is related to the crash. | 86 |
| sch_busname | SCH_BUSNAME | Source label for SCH_BUS. This data element identifies if a school bus, or motor vehicle functioning as a school bus, is related to the crash. | 86 |
| rur_urb | RUR_URB | This data element identifies the classification of the segment of the trafficway on which the crash occurred based on FHWA-approved adjusted Census boundaries of small urban and urbanized areas. | 60 |
| rur_urbname | RUR_URBNAME | Source label for RUR_URB. This data element identifies the classification of the segment of the trafficway on which the crash occurred based on FHWA-approved adjusted Census boundaries of small urban and urbanized areas. | 60 |
| func_sys | FUNC_SYS | This data element identifies the functional classification of the segment of the trafficway on which the crash occurred. | 61 |
| func_sysname | FUNC_SYSNAME | Source label for FUNC_SYS. This data element identifies the functional classification of the segment of the trafficway on which the crash occurred. | 61 |
| mod_year | MOD_YEAR | This data element identifies the manufacturer’s model year of this vehicle. | 124 |
| mod_yearname | MOD_YEARNAME | Source label for MOD_YEAR. This data element identifies the manufacturer’s model year of this vehicle. | 124 |
| vpicmake | VPICMAKE | This element identifies the Make (manufacturer brand name) of this vehicle as per NHTSA vPIC submissions. | 125 |
| vpicmakename | VPICMAKENAME | Source label for VPICMAKE. This element identifies the Make (manufacturer brand name) of this vehicle as per NHTSA vPIC submissions. | 125 |
| vpicmodel | VPICMODEL | This element identifies the Model of this vehicle using NHTSA’s VIN decoder application, vPIC. | 126 |
| vpicmodelname | VPICMODELNAME | Source label for VPICMODEL. This element identifies the Model of this vehicle using NHTSA’s VIN decoder application, vPIC. | 126 |
| vpicbodyclass | VPICBODYCLASS | This element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc., as defined by the manufacturer. | 128 |
| vpicbodyclassname | VPICBODYCLASSNAME | Source label for VPICBODYCLASS. This element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc., as defined by the manufacturer. | 128 |
| make | MAKE | This data element identifies the make (manufacturer) of this vehicle by NCSA historically. | 131 |
| makename | MAKENAME | Source label for MAKE. This data element identifies the make (manufacturer) of this vehicle by NCSA historically. | 131 |
| body_typ | BODY_TYP | This data element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc. as defined by NCSA. | 138 |
| body_typname | BODY_TYPNAME | Source label for BODY_TYP. This data element identifies a classification of this vehicle based on its general body configuration, size, shape, doors, etc. as defined by NCSA. | 138 |
| icfinalbody | ICFINALBODY | This element captures the completed/finished body class for an incomplete vehicle. An incomplete vehicle is completed by a final stage manufacturer. The intent of this data element is to capture the body class for incomplete vehicles when they are finished for road use. | 146 |
| icfinalbodyname | ICFINALBODYNAME | Source label for ICFINALBODY. This element captures the completed/finished body class for an incomplete vehicle. An incomplete vehicle is completed by a final stage manufacturer. The intent of this data element is to capture the body class for incomplete vehicles when they are finished for road use. | 146 |
| gvwr_from | GVWR_FROM | This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| gvwr_fromname | GVWR_FROMNAME | Source label for GVWR_FROM. This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| gvwr_to | GVWR_TO | This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| gvwr_toname | GVWR_TONAME | Source label for GVWR_TO. This element identifies the range of gross vehicle weight rating of the power unit as identified by the manufacturer through the vehicle’s VIN submission. GVWR_FROM defines the lowest value and GVWR_TO defines the highest value for the range of the GVWR specified by the manufacturer as the recommended loaded weight for a vehicle. | 148 |
| tow_veh | TOW_VEH | This data element identifies whether this vehicle had any attached trailing units or was towing another motor vehicle. | 149 |
| tow_vehname | TOW_VEHNAME | Source label for TOW_VEH. This data element identifies whether this vehicle had any attached trailing units or was towing another motor vehicle. | 149 |
| spec_use | SPEC_USE | This data element identifies any special use associated with this vehicle at the time of the crash. | 167 |
| spec_usename | SPEC_USENAME | Source label for SPEC_USE. This data element identifies any special use associated with this vehicle at the time of the crash. | 167 |
| emer_use | EMER_USE | This data element identifies whether this vehicle was engaged in emergency use. Emergency Motor Vehicle Use indicates operation of any motor vehicle that is legally authorized by a government authority to respond to emergencies while actually engaged in such response. These vehicles can respond with or without the use of emergency warning equipment. | 169 |
| emer_usename | EMER_USENAME | Source label for EMER_USE. This data element identifies whether this vehicle was engaged in emergency use. Emergency Motor Vehicle Use indicates operation of any motor vehicle that is legally authorized by a government authority to respond to emergencies while actually engaged in such response. These vehicles can respond with or without the use of emergency warning equipment. | 169 |
| rollover | ROLLOVER | This data element identifies this vehicle’s involvement in a rollover or overturn during the crash. Rollover is defined as any vehicle rotation of 90° or more about any true longitudinal or lateral axis. Rollover can occur at any time during the crash. | 172 |
| rollovername | ROLLOVERNAME | Source label for ROLLOVER. This data element identifies this vehicle’s involvement in a rollover or overturn during the crash. Rollover is defined as any vehicle rotation of 90° or more about any true longitudinal or lateral axis. Rollover can occur at any time during the crash. | 172 |
| impact1 | IMPACT1 | This data element identifies the area on this vehicle that produced the first instance of injury to non-motorists or occupants of this vehicle, or that resulted in the first instance of damage to other property or to this vehicle. | 174 |
| impact1name | IMPACT1NAME | Source label for IMPACT1. This data element identifies the area on this vehicle that produced the first instance of injury to non-motorists or occupants of this vehicle, or that resulted in the first instance of damage to other property or to this vehicle. | 174 |
| fire_exp | FIRE_EXP | This data element identifies whether a fire in any way related to the crash occurred in this vehicle. | 183 |
| fire_expname | FIRE_EXPNAME | Source label for FIRE_EXP. This data element identifies whether a fire in any way related to the crash occurred in this vehicle. | 183 |
| mak_mod | MAK_MOD | This derived data element represents the five-digit combination of two data elements, the two- digit “NCSA Make” code (MAKE) followed by the three-digit “NCSA Model” code (MODEL). | 187 |
| mak_modname | MAK_MODNAME | Source label for MAK_MOD. This derived data element represents the five-digit combination of two data elements, the two- digit “NCSA Make” code (MAKE) followed by the three-digit “NCSA Model” code (MODEL). | 187 |
| age | AGE | This data element identifies the person’s age in years on the date of the crash. | 301 |
| agename | AGENAME | Source label for AGE. This data element identifies the person’s age in years on the date of the crash. | 301 |
| sex | SEX | This data element identifies the sex of this person involved in the crash. | 302 |
| sexname | SEXNAME | Source label for SEX. This data element identifies the sex of this person involved in the crash. | 302 |
| per_typ | PER_TYP | This data element describes the role of this person or non-motorist at the time they became involved in the crash. | 303 |
| per_typname | PER_TYPNAME | Source label for PER_TYP. This data element describes the role of this person or non-motorist at the time they became involved in the crash. | 303 |
| inj_sev | INJ_SEV | This data element describes the severity of the injury to this person in the crash using the KABCO scale. | 305 |
| inj_sevname | INJ_SEVNAME | Source label for INJ_SEV. This data element describes the severity of the injury to this person in the crash using the KABCO scale. | 305 |
| seat_pos | SEAT_POS | This data element identifies the location of this person in or on the vehicle. | 306 |
| seat_posname | SEAT_POSNAME | Source label for SEAT_POS. This data element identifies the location of this person in or on the vehicle. | 306 |
| rest_use | REST_USE | This data element records the restraint equipment in use by this occupant at the time of the crash. | 308 |
| rest_usename | REST_USENAME | Source label for REST_USE. This data element records the restraint equipment in use by this occupant at the time of the crash. | 308 |
| rest_mis | REST_MIS | This data element identifies any misuse of the available restraint system used by this person. | 310 |
| rest_misname | REST_MISNAME | Source label for REST_MIS. This data element identifies any misuse of the available restraint system used by this person. | 310 |
| helm_use | HELM_USE | This data element records the helmet use by this occupant at the time of the crash. | 311 |
| helm_usename | HELM_USENAME | Source label for HELM_USE. This data element records the helmet use by this occupant at the time of the crash. | 311 |
| helm_mis | HELM_MIS | This data element identifies any misuse of the helmet used by this person. | 312 |
| helm_misname | HELM_MISNAME | Source label for HELM_MIS. This data element identifies any misuse of the helmet used by this person. | 312 |
| air_bag | AIR_BAG | This data element records air bag availability and deployment for this person as reported in the case material. | 313 |
| air_bagname | AIR_BAGNAME | Source label for AIR_BAG. This data element records air bag availability and deployment for this person as reported in the case material. | 313 |
| ejection | EJECTION | This data element describes the ejection status and degree of ejection for this person, excluding motorcycle occupants. | 315 |
| ejectionname | EJECTIONNAME | Source label for EJECTION. This data element describes the ejection status and degree of ejection for this person, excluding motorcycle occupants. | 315 |
| ej_path | EJ_PATH | This data element identifies the path by which this person was ejected from the vehicle. | 316 |
| ej_pathname | EJ_PATHNAME | Source label for EJ_PATH. This data element identifies the path by which this person was ejected from the vehicle. | 316 |
| extricat | EXTRICAT | This data element identifies if equipment was used to remove this person from the vehicle. | 317 |
| extricatname | EXTRICATNAME | Source label for EXTRICAT. This data element identifies if equipment was used to remove this person from the vehicle. | 317 |
| drinking | DRINKING | This data element records whether alcohol was involved for this person and reflects the judgment of law enforcement. | 318 |
| drinkingname | DRINKINGNAME | Source label for DRINKING. This data element records whether alcohol was involved for this person and reflects the judgment of law enforcement. | 318 |
| alc_status | ALC_STATUS | This data element identifies whether an alcohol test was given to this person. | 319 |
| alc_statusname | ALC_STATUSNAME | Source label for ALC_STATUS. This data element identifies whether an alcohol test was given to this person. | 319 |
| atst_typ | ATST_TYP | This data element identifies the type of alcohol test that was given to this person. | 320 |
| atst_typname | ATST_TYPNAME | Source label for ATST_TYP. This data element identifies the type of alcohol test that was given to this person. | 320 |
| alc_res | ALC_RES | This data element identifies the alcohol test result for this person. | 322 |
| alc_resname | ALC_RESNAME | Source label for ALC_RES. This data element identifies the alcohol test result for this person. | 322 |
| drugs | DRUGS | This data element records whether drugs were involved for this person and reflects the judgment of law enforcement. | 324 |
| drugsname | DRUGSNAME | Source label for DRUGS. This data element records whether drugs were involved for this person and reflects the judgment of law enforcement. | 324 |
| dstatus | DSTATUS | This data element identifies whether a drug test was given to this person. | 325 |
| dstatusname | DSTATUSNAME | Source label for DSTATUS. This data element identifies whether a drug test was given to this person. | 325 |
| hospital | HOSPITAL | This data element identifies the mode of transportation to a hospital or medical facility provided for this person. | 326 |
| hospitalname | HOSPITALNAME | Source label for HOSPITAL. This data element identifies the mode of transportation to a hospital or medical facility provided for this person. | 326 |
| doa | DOA | This data element identifies if this person died at the scene of the crash or en route to a hospital/medical facility. | 327 |
| doaname | DOANAME | Source label for DOA. This data element identifies if this person died at the scene of the crash or en route to a hospital/medical facility. | 327 |
| death_mo | DEATH_MO | This data element records the month of this person’s death. | 328 |
| death_moname | DEATH_MONAME | Source label for DEATH_MO. This data element records the month of this person’s death. | 328 |
| death_da | DEATH_DA | This data element records the day of the month of this person’s death. | 329 |
| death_daname | DEATH_DANAME | Source label for DEATH_DA. This data element records the day of the month of this person’s death. | 329 |
| death_yr | DEATH_YR | This data element records the year of this person’s death. | 330 |
| death_yrname | DEATH_YRNAME | Source label for DEATH_YR. This data element records the year of this person’s death. | 330 |
| death_tm | DEATH_TM | This data element records the hour and minute of this person’s death utilizing the 24-hour clock format. | 331 |
| death_tmname | DEATH_TMNAME | Source label for DEATH_TM. This data element records the hour and minute of this person’s death utilizing the 24-hour clock format. | 331 |
| death_hr | DEATH_HR | This data element records the hour of this person’s death utilizing the 24-hour clock format. | 332 |
| death_hrname | DEATH_HRNAME | Source label for DEATH_HR. This data element records the hour of this person’s death utilizing the 24-hour clock format. | 332 |
| death_mn | DEATH_MN | This data element records the minutes after the hour of this person’s death. | 333 |
| death_mnname | DEATH_MNNAME | Source label for DEATH_MN. This data element records the minutes after the hour of this person’s death. | 333 |
| lag_hrs | LAG_HRS | This data element records the hours between the time of the crash and this person’s time of death. | 334 |
| lag_hrsname | LAG_HRSNAME | Source label for LAG_HRS. This data element records the hours between the time of the crash and this person’s time of death. | 334 |
| lag_mins | LAG_MINS | This data element records the minutes, in addition to hours (“Lag Hours”), between the time of the crash and this person’s time of death. | 335 |
| lag_minsname | LAG_MINSNAME | Source label for LAG_MINS. This data element records the minutes, in addition to hours (“Lag Hours”), between the time of the crash and this person’s time of death. | 335 |
| str_veh | STR_VEH | This data element identifies the “Vehicle Number” (VEH_NO) of the motor vehicle in-transport that made contact with this non-motorist. | 336 |
| devtype | DEVTYPE | This element describes the type of transport device operated by the non-motorist. | 337 |
| devtypename | DEVTYPENAME | Source label for DEVTYPE. This element describes the type of transport device operated by the non-motorist. | 337 |
| devmotor | DEVMOTOR | This element describes the motorization of the device operated by the non-motorist. | 338 |
| devmotorname | DEVMOTORNAME | Source label for DEVMOTOR. This element describes the motorization of the device operated by the non-motorist. | 338 |
| location | LOCATION | This data element identifies the attribute that best describes the location of this non-motorist with respect to the roadway at the time of the crash. | 339 |
| locationname | LOCATIONNAME | Source label for LOCATION. This data element identifies the attribute that best describes the location of this non-motorist with respect to the roadway at the time of the crash. | 339 |
| work_inj | WORK_INJ | This data element records whether the death certificate indicated this person was "at work" at the time of the crash. | 342 |
| work_injname | WORK_INJNAME | Source label for WORK_INJ. This data element records whether the death certificate indicated this person was "at work" at the time of the crash. | 342 |
| hispanic | HISPANIC | This data element records the Hispanic origin of this person from the death certificate. | 343 |
| hispanicname | HISPANICNAME | Source label for HISPANIC. This data element records the Hispanic origin of this person from the death certificate. | 343 |

