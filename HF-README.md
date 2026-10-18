---
license: other
license_name: nhtsa-public-information
license_link: https://www.nhtsa.gov/about-nhtsa/privacy-policy
pretty_name: FARS 2024 National Annual Report File
tags:
  - fars
  - nhtsa
  - traffic-safety
  - fatal-crashes
  - transportation
  - duckdb
size_categories:
  - 100K<n<1M
---

# FARS 2024 National Annual Report File

A pinned DuckDB edition of NHTSA's [Fatality Analysis Reporting System](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars), 2024 national Annual Report File: **190,798 rows across 4 tables (413 columns)**, three convenience views, metadata and a dictionary tied to manual pages. The three source tables hold **36,297 fatal crashes, 56,011 vehicles in transport and 88,326 people**; the accident and person tables reconcile to **39,254 fatalities**.

This is the **first 2024 ARF, released April 1, 2026**, not the later final file. Coverage is the 50 states and the District of Columbia; Puerto Rico is a separate archive and is not included.

Built with [fars-database](https://github.com/ian-nason/fars-database). Published to Hugging Face on 2026-10-18. The datapond registry entry is a draft pull request, so `datapond.connect('fars')` does not resolve this database until it is merged; the direct URL below works now.

[Quick start](#quick-start) · [Tables](#tables) · [Views](#pre-built-views) · [Examples](#example-queries) · [Caveats](#researcher-caveats) · [Source](#data-source-and-version) · [License](#license-and-attribution) · [Changelog](#changelog)

## Quick Start

### DuckDB CLI

```sql
SET memory_limit = '128MiB';
SET threads = 1;
SET max_temp_directory_size = '0B';
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/fars-database/resolve/adb6da02a314c39d8b6caf776529bf4a373075da/fars.duckdb' AS fars (READ_ONLY);

-- Fatal crashes and fatalities by state; the crashes view never multiplies rows
SELECT state, statename, count(*) AS fatal_crashes,
       sum(fatals) AS fatalities, sum(nonoccupant_fatalities) AS nonoccupant_fatalities
FROM fars.crashes
GROUP BY state, statename
ORDER BY fatalities DESC, state LIMIT 15;
```

The database is 26 MB. DuckDB fetches byte ranges as needed; transfer volume depends on the query. The examples use this immutable artifact URL:

```
https://huggingface.co/datasets/Nason/fars-database/resolve/adb6da02a314c39d8b6caf776529bf4a373075da/fars.duckdb
```

### Python (duckdb)

```python
import duckdb
con = duckdb.connect(config={"memory_limit": "128MiB", "threads": "1", "max_temp_directory_size": "0B"})
con.sql("INSTALL httpfs; LOAD httpfs;")
con.sql("ATTACH 'https://huggingface.co/datasets/Nason/fars-database/resolve/adb6da02a314c39d8b6caf776529bf4a373075da/fars.duckdb' AS fars (READ_ONLY)")
con.sql("SELECT * FROM fars._metadata").show()
con.sql("SELECT count(*) AS fatal_crashes, sum(fatals) AS fatalities FROM fars.crashes").show()
con.close()
```

### R (DBI + duckdb)

```r
library(DBI)
con <- dbConnect(duckdb::duckdb(config = list(memory_limit = "128MiB", threads = "1", max_temp_directory_size = "0B")))
dbExecute(con, "INSTALL httpfs")
dbExecute(con, "LOAD httpfs")
dbExecute(con, "ATTACH 'https://huggingface.co/datasets/Nason/fars-database/resolve/adb6da02a314c39d8b6caf776529bf4a373075da/fars.duckdb' AS fars (READ_ONLY)")
dbGetQuery(con, "SELECT month, monthname, count(*) AS fatal_crashes, sum(fatals) AS fatalities
                 FROM fars.crashes GROUP BY month, monthname ORDER BY month")
dbDisconnect(con, shutdown = TRUE)
```

In the tested R DuckDB 1.5.5 configuration, BIGINT and DECIMAL results are exposed as doubles. Counts here are exact; coordinates and `measured_bac_g_dl` may be approximate in R although the stored DECIMAL values are exact.

### datapond package (after catalog integration)

The public default catalog does not yet include `fars`. After its registry entry is merged, these examples use the package's normal discovery and connection API:

```python
import datapond
print(datapond.list())
datapond.describe('fars', table='person')
con = datapond.connect('fars')
con.sql('SELECT count(*) AS fatal_crashes, sum(fatals) AS fatalities FROM crashes').show()
con.close()
```

```r
library(datapond)
dp_list()
con <- dp_connect('fars')
dp_describe(con, table = 'person')
DBI::dbGetQuery(con, "SELECT count(*) AS fatal_crashes, sum(fatals) AS fatalities FROM crashes")
dp_disconnect(con)
```

For repeated scans, after catalog integration, download once and connect locally:

```python
import datapond
datapond.download('fars')
con = datapond.connect('fars', local=True)
con.sql('SELECT count(*) AS fatal_crashes, sum(fatals) AS fatalities FROM crashes').show()
con.close()
```

```r
library(datapond)
dp_download('fars')
con <- dp_connect('fars', local = TRUE)
DBI::dbGetQuery(con, "SELECT count(*) AS fatal_crashes, sum(fatals) AS fatalities FROM crashes")
dp_disconnect(con)
```

Verify the recorded artifact SHA-256 after downloading. In tested Python 0.1.1, the optional Hugging Face download path follows the default branch rather than the pinned URL; see [consumer verification](https://github.com/ian-nason/fars-database/blob/main/docs/CONSUMERS.md) for the tested configuration.

Package checks use an isolated candidate registry; default-catalog discovery remains pending. See [consumer verification](https://github.com/ian-nason/fars-database/blob/main/docs/CONSUMERS.md) for exact client versions, paths, resource limits and download behavior. The direct URL examples above work independently of the catalog. The SQL examples below use the `fars` catalog alias from the direct-URL quick start.


## Tables

| Table | Description | Rows | Columns |
|---|---|---:|---:|
| `person` | One record per involved person, including nonoccupants and occupants of vehicles not in transport | 88,326 | 126 |
| `vehicle` | One record per motor vehicle in transport; parked/working vehicles are in the omitted Parkwork file | 56,011 | 201 |
| `accident` | One record per fatal crash in the 2024 national Annual Report File | 36,297 | 80 |
| `code_labels` | Distinct observed code/label tuples for 30 selected fields; county/city scoped by state; four city codes have multiple source labels | 10,164 | 6 |

Keys: `accident (state, st_case)`; `vehicle (state, st_case, veh_no)`; `person (state, st_case, veh_no, per_no)`; all within this year. Every original column and paired `NAME` label is kept with lowercase names; codes are not recoded. Character fields such as `dr_zip`, VIN characters and `tway_id` stay strings; integer codes are BIGINT; coordinates are DECIMAL(18,12). `_metadata` and `_columns` carry provenance, definitions and manual page links.

## Pre-built Views

| View | What it does |
|---|---|
| `crashes` | All `accident` columns plus per-crash counts aggregated before joining: `vehicle_records`, `in_transport_vehicle_fatalities`, `person_records`, `person_fatalities`, `in_transport_people`, `parked_working_vehicle_people`, `nonoccupant_people`, `nonoccupant_fatalities`, `parked_working_vehicle_fatalities`, and `latitude_degrees`/`longitude_degrees` with the unavailable codes (77.7777, 88.8888, 99.9999; 777.7777, 888.8888, 999.9999) set to NULL. Still 36,297 rows |
| `people` | All `person` columns plus `age_years` (0 to 120; 998/999 NULL), `measured_bac_g_dl` (`alc_res` 0 to 939 times 0.001), `bac_top_coded_at_094_or_more` (true for `alc_res`=940) and `fatal_injury_recorded` (true for 4; false for 0, 1, 2, 3, 6; NULL for 5 or 9) |
| `unambiguous_code_labels` | `code_labels` restricted to keys with exactly one source label; join on all five key columns |

Views are not counted in the row and table totals above.

## Example Queries

Fatal injuries by recorded person role and age group; unknown age stays its own group:

```sql
SELECT per_typ, per_typname,
       CASE WHEN age_years IS NULL THEN 'Unknown/not reported'
            WHEN age_years < 18 THEN '0-17'
            WHEN age_years < 65 THEN '18-64' ELSE '65+' END AS age_group,
       count(*) AS fatalities
FROM fars.people
WHERE inj_sev = 4
GROUP BY ALL ORDER BY per_typ, age_group;
```

Alcohol test-result coverage among recorded drivers (test results, not imputed impairment):

```sql
SELECT alc_status, alc_statusname, count(*) AS drivers,
       count(measured_bac_g_dl) AS exact_numeric_test_results,
       count(*) FILTER (WHERE bac_top_coded_at_094_or_more) AS top_coded_test_results
FROM fars.people
WHERE per_typ = 1
GROUP BY alc_status, alc_statusname ORDER BY alc_status;
```

Coordinate availability for mapping (170 crashes lack usable coordinates):

```sql
SELECT count(*) AS fatal_crashes,
       count(*) FILTER (WHERE latitude_degrees IS NOT NULL AND longitude_degrees IS NOT NULL) AS coordinates_available,
       count(*) FILTER (WHERE latitude_degrees IS NULL OR longitude_degrees IS NULL) AS coordinates_missing
FROM fars.crashes;
```

The full set is in [examples.sql](https://github.com/ian-nason/fars-database/blob/main/examples.sql); saved results are bound to the artifact hash.

## Researcher Caveats

1. **Fatal crashes only, no denominator.** FARS records crashes on public trafficways with a death within 30 days. Counts are not risk rates; there is no population, vehicle-miles or trip denominator here. Uninjured occupants may be incompletely recorded.
2. **Join people carefully.** An inner `person` to `vehicle` join drops the 9,020 nonoccupants (`veh_no=0`) and the 426 occupants of parked or working vehicles (`per_typ=3`), whose vehicles live in the omitted Parkwork file. Transport occupants (`per_typ` 1, 2, 9) always match a `vehicle` row. Joining `vehicle` and `person` directly by crash multiplies rows; use `crashes`.
3. **Missing codes are field-specific.** Unknown and not-applicable values stay as source codes (998/999 age, 995 to 999 `alc_res`, coordinate codes above). Do not blanket-convert 9, 99, 999 or 0 to NULL. Only the 9,020 nonoccupant rows have numeric vehicle attributes as NULL; blank text stays empty.
4. **BAC 940 is a top code.** `alc_res`=940 means 0.94 g/dL or greater, not 0.940; the `people` view keeps it separate. `alc_res` 995 to 999 are nonmeasurement categories and never zero. Police-reported `drinking` and measured tests are different variables, and missing tests are not random.
5. **Imputed alcohol estimates are not here.** The three multiple-imputation files (`MIACC`, `MIDRVACC`, `MIPER`) are not loaded; this release cannot reproduce NHTSA's imputed impairment estimates. Per the [alcohol README](https://static.nhtsa.gov/nhtsa/downloads/FARS/README-BAC.pdf), such analyses compute an estimate in each of ten imputations and combine them.
6. **Labels can conflict.** Four city codes carry more than one official label (state 4 code 428; 13/2190; 36/4170; 42/3950). `unambiguous_code_labels` omits them; never join `code_labels` on code alone. `mak_mod` is the combined make/model code; raw `model` is only meaningful with `make`.
7. **Vintage and identity.** `st_case` identifies a crash within one year only; include year when pooling releases. The first ARF may be replaced by a final file with added or revised cases.
8. **Scope of this MVP.** Only `accident`, `vehicle` and `person` are loaded. Parkwork, multiple-response factors, drug/race, vPIC decode and auxiliary files are omitted; their archived identities are pinned in the source lock.

## Data Source and Version

National Highway Traffic Safety Administration, National Center for Statistics and Analysis, Fatality Analysis Reporting System, 2024 national Annual Report File, first release April 1, 2026, acquired October 18, 2026. Pinned source ZIP: 32,672,161 bytes, SHA-256 `5112727a8c0dc91ffee27ca05bddb073934f2d192ce4fae997da767dccdbe04f`. Definitions reference the [Analytical User's Manual](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813794) (DOT HS 813 794, SHA-256 `210bc33d…04cc574`). No automatic refresh is promised.

Artifact: `fars.duckdb`, 26,488,832 bytes, SHA-256 `2bc31f9e9fdd973ddf728cc4e1e0811a7bacf9450dd80c7671c36fa6a1fc7442`, dataset commit `adb6da02a314c39d8b6caf776529bf4a373075da`.

## License and Attribution

Redistribution rests on NHTSA's own [Ownership policy](https://www.nhtsa.gov/about-nhtsa/privacy-policy), which states that information on its website is public information and may be distributed or copied. This is the primary-source permission; no third-party Creative Commons compilation license is borrowed, and no NHTSA endorsement or trademark right is implied. Changes: CSV-to-DuckDB typing, lowercase names, numeric blank-to-NULL on nonoccupant rows, observed label dictionary, metadata and views; original codes and labels are retained. Cite the release vintage, acquisition date and artifact checksum.

## GitHub, Dictionary and Website

[Detailed researcher guide](https://github.com/ian-nason/fars-database/blob/main/docs/RESEARCHER-GUIDE.md) · [Build and update instructions](https://github.com/ian-nason/fars-database/blob/main/docs/REPRODUCE.md) · [Verified publication](https://github.com/ian-nason/fars-database/blob/main/PUBLICATION.md)

- Source, build scripts, tests and evidence: [github.com/ian-nason/fars-database](https://github.com/ian-nason/fars-database)
- Column dictionary (all 413 columns with original headers, definitions and manual PDF pages): [DICTIONARY.md](https://github.com/ian-nason/fars-database/blob/main/DICTIONARY.md)
- Catalog: [datapond registry](https://github.com/datapond-db/registry); the entry for `fars` is a draft pull request and the database will appear on the [datapond website](https://datapond-db.github.io/website/) once it is merged.

## Changelog

### 2026-10-18 — Documentation refresh

- Added Python/R quick starts, table descriptions and column counts, view guidance, navigation, and clearer researcher caveats.
- Database bytes, schema, source locks and validated query results are unchanged. Catalog integration remains pending.

### 2026-10-18 — Initial release

- FARS 2024 ARF (first release): 190,798 rows across 4 tables (413 columns) and 3 views; 36,297 crashes, 39,254 fatalities. Artifact 26,488,832 bytes, SHA-256 `2bc31f9e…fc7442`, commit `adb6da02`.
- Every typed cell verified against an independent read of the pinned source ZIP; per-crash count and fatality reconciliation; public immutable URL, HTTP range requests and the installed Python and R clients tested after upload.
- Registry entry opened as a draft pull request; catalog integration pending.
