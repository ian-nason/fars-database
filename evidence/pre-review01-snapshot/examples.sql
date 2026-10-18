-- One record per fatal crash. These are counts in the fatal-crash universe, not risk rates.
SELECT count(*) AS fatal_crashes,sum(fatals) AS fatalities,sum(vehicle_records) AS vehicles_in_transport,sum(person_records) AS people_recorded
FROM crashes;

-- State comparison with explicit fatal-crashes-only scope; Puerto Rico is not in this file.
SELECT state,statename,count(*) AS fatal_crashes,sum(fatals) AS fatalities,sum(nonoccupant_fatalities) AS nonoccupant_fatalities
FROM crashes GROUP BY state,statename ORDER BY fatalities DESC,state LIMIT 15;

-- Monthly fatal-crash counts. The view prevents vehicle/person join multiplication.
SELECT month,monthname,count(*) AS fatal_crashes,sum(fatals) AS fatalities
FROM crashes GROUP BY month,monthname ORDER BY month;

-- Fatal injuries by recorded person role and age range; unknown age remains a separate group.
SELECT per_typ,per_typname,
 CASE WHEN age_years IS NULL THEN 'Unknown/not reported' WHEN age_years<18 THEN '0-17' WHEN age_years<65 THEN '18-64' ELSE '65+' END AS age_group,
 count(*) AS fatalities
FROM people WHERE inj_sev=4 GROUP BY ALL ORDER BY per_typ,age_group;

-- Alcohol TEST-result coverage among recorded drivers, not an imputed impairment prevalence.
SELECT alc_status,alc_statusname,count(*) AS drivers,
 count(measured_bac_g_dl) AS exact_numeric_test_results,
 count(*) FILTER(WHERE bac_top_coded_at_094_or_more) AS top_coded_test_results
FROM people WHERE per_typ=1 GROUP BY alc_status,alc_statusname ORDER BY alc_status;

-- Geographic usability; missing coordinate codes are NULL in the view, never map locations.
SELECT count(*) AS fatal_crashes,
 count(*) FILTER(WHERE latitude_degrees IS NOT NULL AND longitude_degrees IS NOT NULL) AS coordinates_available,
 count(*) FILTER(WHERE latitude_degrees IS NULL OR longitude_degrees IS NULL) AS coordinates_missing
FROM crashes;
