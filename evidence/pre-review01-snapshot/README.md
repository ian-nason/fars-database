# FARS 2024 national Annual Report File

A pinned DuckDB edition of NHTSA's [Fatality Analysis Reporting System](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars). This is the **2024 Annual Report File (ARF), first released April 1, 2026**, acquired October 18, 2026. It is not the later final file. The national archive covers the 50 states and District of Columbia; Puerto Rico is a separate official archive and is not included.

The three original tables contain **36,297 fatal crashes, 56,011 vehicles in transport and 88,326 people**. The observed-label dictionary adds 10,164 rows, for **190,798 rows across four data tables and 413 documented columns**. Three views are excluded from those totals. The source crash and person files both report **39,254 fatalities** in this snapshot.

## Tables, keys and safe joins

| Table | Rows | Key and scope |
|---|---:|---|
| accident | 36,297 | `(state,st_case)` within this year; 80 original columns |
| vehicle | 56,011 | `(state,st_case,veh_no)`; 201 original columns; vehicles in transport |
| person | 88,326 | `(state,st_case,veh_no,per_no)`; 126 original columns; motorists and nonoccupants |
| code_labels | 10,164 | `(table_name,column_name,context_column,context_value,code,label)`; six derived columns |

All original columns and paired `NAME` labels are retained, with lowercase column names. Codes are not recoded or trimmed. Source character fields such as `dr_zip`, VIN characters and trafficway identifiers remain strings, including leading zeros and blank strings. Source integer codes/counts use BIGINT; latitude/longitude use DECIMAL(18,12), preserving source precision beyond the manual's seven-decimal illustration. Raw unknown and inapplicable codes remain numeric codes.

`st_case` identifies a crash within one year, not a person or stable cross-year location. Include year when pooling future releases. An inner person-to-vehicle join would drop nonoccupants (`veh_no=0`) and people in parked/working vehicles (`per_typ=3`). There are **9,020 nonoccupants and 426 parked/working-vehicle occupants** in this source. The latter link to the omitted Parkwork file, not `vehicle`. Transport occupants (`per_typ` 1, 2 or 9) must match a vehicle record; their relationships are checked.

Joining vehicles and people directly by crash creates a many-to-many product. Use `crashes` for crash-level questions: each child table is aggregated by `(state,st_case)` before joining. Its row count remains 36,297. Per-crash checks reconcile vehicle records with `ve_forms`, recorded people with `persons+peds`, transport people with `permvit`, other people with `pernotmvit`, and fatalities with both the person file and vehicle/nonoccupant/parked-occupant components. Repeated crash counts in child tables are not additive.

## Views and missing values

`crashes` includes all accident columns plus these derived fields:

| Field | Meaning |
|---|---|
| vehicle_records | Count of in-transport vehicle records for the crash |
| in_transport_vehicle_fatalities | Sum of vehicle `deaths` |
| person_records / person_fatalities | Recorded people / records with `inj_sev=4` |
| in_transport_people | Person types 1, 2 or 9 |
| parked_working_vehicle_people | Person type 3 |
| nonoccupant_people | `veh_no=0` |
| nonoccupant_fatalities | `veh_no=0` and `inj_sev=4` |
| parked_working_vehicle_fatalities | Person type 3 and `inj_sev=4` |
| latitude_degrees / longitude_degrees | Coordinates with the documented unavailable codes mapped to NULL |

Latitude codes 77.7777, 88.8888 and 99.9999, and longitude codes 777.7777, 888.8888 and 999.9999, are not map locations. The view changes only those codes; original values and labels remain in `accident`.

`people` retains every person column and adds:

| Field | Meaning |
|---|---|
| age_years | Ages 0–120; codes 998/999 become NULL. Code 0 means less than one year. |
| measured_bac_g_dl | `alc_res` 0–939 multiplied by exact decimal 0.001; other codes become NULL |
| bac_top_coded_at_094_or_more | True for `alc_res=940`, meaning 0.94 g/dL or greater, not an exact 0.940 measurement |
| fatal_injury_recorded | True for injury code 4; false for 0,1,2,3,6; NULL for unknown severity 5 or 9. Code 6 means died before the crash. |

`alc_res` 995–999 distinguishes not reported, no test, unknown result, positive without a numeric result and unknown testing status. These are never treated as zero BAC. Police-reported drinking and test measurements are different variables. Missing alcohol results are not random, so measured results do not estimate population impairment prevalence.

Blank numeric vehicle attributes on the 9,020 nonoccupant person records become SQL NULL; blank text/labels remain empty strings. The schema pins the observed blank count for every source field, and validation checks exact NULL counts and percentages. Other unknown/inapplicable codes vary by field: do not globally turn 9, 99, 999 or zero into NULL. Dates/times remain source codes; unknown values are not coerced into calendar timestamps.

## Dictionaries and ambiguous labels

`DICTIONARY.md` documents all 413 data columns with types, sample values, NULL percentages, join hints, original headers, definitions and exact PDF pages in the [official analytical manual](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813794). `_metadata` records table provenance; `_columns` embeds field definitions and source links.

`code_labels` contains every distinct observed source code/label tuple for 30 explicitly selected fields, listed in `build-report.json`. County/city codes require state context; other selected fields are global, with `context_column=''` and `context_value=0`. `mak_mod` is the combined make/model code. The separate raw `model` field must be interpreted with `make`. This dictionary is not every possible or historical FARS code; original labels for other fields remain in their source tables. The exploratory profiler's 2,000-tuple limit is **not used** when building this dictionary.

Four city codes have conflicting official labels, preserved exactly:

| State | City code | Source labels |
|---:|---:|---|
| 4 | 428 | SEDONA; Sedona |
| 13 | 2190 | STONECREST; FORSYTH |
| 36 | 4170 | MIDDLE VILLAGE; NEW YORK CITY; NEW YORK |
| 42 | 3950 | JEFFERSON; JEFFERSON HILLS |

`unambiguous_code_labels` contains only code/context keys with one source label. Join it using all five key columns; ambiguous keys return no label. Do not join `code_labels` on code alone or choose an arbitrary spelling. The crash/person views retain their own source labels and do not join either dictionary.

## Useful queries

```python
import duckdb
con = duckdb.connect('releases/2024-release-final/fars.duckdb', read_only=True)
con.sql('SELECT count(*) AS fatal_crashes, sum(fatals) AS fatalities FROM crashes').show()
```

```sql
SELECT state,statename,count(*) AS fatal_crashes,
       sum(fatals) AS fatalities,sum(nonoccupant_fatalities) AS nonoccupant_fatalities
FROM crashes
GROUP BY state,statename
ORDER BY fatalities DESC,state;
```

`examples.sql` also gives monthly counts, fatalities by recorded person role/age group, driver alcohol-test coverage and coordinate availability. These are descriptive counts within the fatal-crash universe, not population or travel-exposure rates. The complete queries execute in validation and their saved outputs bind to the artifact SHA-256.

## Coverage and limitations

FARS includes crashes involving a motor vehicle on a trafficway customarily open to the public, with a death within 30 days (720 hours). It excludes nonfatal crashes and has no population, vehicle-miles-traveled or total-trip denominator here. Comparing counts is not comparing risk. People recorded in fatal crashes are not a sample of all travelers. The manual warns that uninjured occupants, including bus occupants, may be incompletely recorded; person totals mean recorded forms, not a complete exposure denominator.

This MVP includes only accident, vehicle and person from the pinned national archive. Parkwork, multiple-response factors, detailed drug/race files, vPIC decode files, auxiliary files, and the three multiple-imputation alcohol files (`MIACC`, `MIDRVACC`, `MIPER`) are not loaded. Their exact archived identities remain in the source lock. Do not claim full FARS coverage or that this derivative reproduces NHTSA's imputed alcohol estimates. The official [alcohol README](https://static.nhtsa.gov/nhtsa/downloads/FARS/README-BAC.pdf) directs analysts to calculate an estimate in each of the ten imputations and then combine estimates, not average a person's imputed BAC values. Variance/pooling methods require the linked technical documentation.

Annual file revisions, definitions, coding and geography can change. The first ARF may be replaced by a final file with additional or revised cases. This release is a historical snapshot, not a promise of the latest counts. No record linkage to identify individuals, causal inference, longitudinal-person interpretation or direct O*NET/QCEW/ATUS crosswalk is provided.

## Reproduce and validate

`source-lock.json` pins the 32,672,161-byte original ZIP (SHA-256 `5112727a8c0dc91ffee27ca05bddb073934f2d192ce4fae997da767dccdbe04f`), every member, release notes and official manual. Download size does not estimate RAM or output size. A changed archive fails closed; do not silently update checksums. The manual is DOT HS 813 794, April 2026, SHA-256 `210bc33d0572147bf695a39d5261e75158d88b269221e18e460b23d0504cc574`.

The existing build environment uses Python 3.12 and DuckDB 1.5.5. `pyproject.toml` pins the datapond-build source revision; `helper-lock.json` and `runtime.json` verify the actual imported helper bytes. The installed helper reports version 0.1.1 but its used metadata functions match the pinned revision. No package installation or clean-environment installation test is claimed.

```sh
python -m unittest -v test_fars test_guard
python run_guarded.py evidence/new-build python fars.py --download --output releases/new-candidate
python run_guarded.py evidence/new-audit python audit_release.py releases/new-candidate/fars.duckdb
```

The builder requires output inside this isolated repository, rejects existing output directories, and hashes extracted caches before reuse. Download/extraction partials are retained and never accepted as completed files. After interruption, inspect and quarantine the named partial before retrying. Existing evidence and candidates are retained. For future rebuilds, use a fresh isolated checkout or first inventory retained file usage; do not raise resource caps.

DuckDB uses one thread, 256 MiB memory and at most 256 MiB spill. The Linux supervisor measures the entire worker process group and stops above 768 MiB RSS, 2 GiB of repository files (including `.git` and old attempts), below 1.5 GiB available RAM or 10 GiB free disk, or after 15 minutes. One ingestion worker runs at a time. Per-run resource receipts record sampled peaks; short peaks between samples may not be observed.

Every typed raw cell is compared to an independent streaming Python CSV/Decimal read of the ZIP before checkpoint and after read-only reopening. Full dictionary tuples are independently regenerated from the original CSVs. Additional checks cover keys, references, copied crash fields, exact NULL counts and metadata, every analytic NULL mapping, ambiguity handling, per-crash count/fatality reconciliation and national source totals. The 39,254 total is a locked source-derived regression value, not an independently downloaded bulletin benchmark. SQL callers must specify ordering; preserved physical row order is used only for verification.

Negative fixtures cover duplicate keys, orphan/invalid occupant links, nonoccupant and parked-occupant retention, many-to-many inflation, incorrect vintage, conflicting label lookups, missing/unknown codes, top-coded BAC, decimal precision, source-cell mutation, archive corruption, unsafe output paths and supervisor failure/races. Final results and resource measurements are in `AUDIT-RESULT.md` and the evidence folder.

The consumer probe uses existing Python/DuckDB 1.5.4 and R datapond 0.1.0/0.1.1 with R DuckDB 1.5.5 over localhost HTTP ranges. It loads only preinstalled httpfs, bounds clients, uses fresh R caches and records installed R package hashes. R exposes tested BIGINT/DECIMAL values as doubles: integer counts here are exactly representable, decimal fractions may be approximate in the client; stored DECIMAL values remain exact. Local success does not prove public availability. Actual immutable public-host checksum/range/Python/R tests are a separate post-upload gate.

To update, select year and exact ARF/final release, inspect changed definitions/codes and license terms, pin the archive/manual, regenerate the explicit schema, build in a fresh isolated checkout, rerun all source/semantic/fixture/client checks, obtain Codex implementation and independent Claude review, and resolve findings. Publish only to authorized destinations, verify the immutable public artifact and clients, then open a separate registry PR. No automatic refresh cadence is promised.

## Attribution and permitted redistribution

Source: **National Highway Traffic Safety Administration, National Center for Statistics and Analysis, Fatality Analysis Reporting System, 2024 national Annual Report File**, first release April 1, 2026, acquired October 18, 2026. Cite this release vintage and derivative artifact checksum. The official [NHTSA Ownership policy](https://www.nhtsa.gov/about-nhtsa/privacy-policy) permits copying/distribution of information on its website. This derivative uses that primary-source public-information permission; it does not borrow a third-party compilation license or grant NHTSA trademark rights. See `LICENSE.md`.

Changes: CSV-to-DuckDB typing, lowercase names, explicit numeric blank-to-NULL conversion, observed dictionaries, metadata and safe convenience views. Original codes/labels are retained. No NHTSA endorsement is implied. Public destination approval remains pending; no public repository or registry availability is claimed by this local checkpoint.
