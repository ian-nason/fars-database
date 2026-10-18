---
license: other
license_name: nhtsa-public-information
license_link: https://www.nhtsa.gov/about-nhtsa/privacy-policy
pretty_name: FARS 2024 National Annual Report File
tags: [fars, traffic-safety, fatal-crashes, duckdb]
size_categories: [100K<n<1M]
---

# FARS 2024 national Annual Report File

Official NHTSA FARS **2024 ARF**, first released April 1,2026, acquired October 18,2026. This is not the later final file. The national source covers50 states and DC; Puerto Rico is separate. Four data tables contain **190,798 rows and 413 columns**: accident 36,297; vehicle 56,011; person 88,326; code_labels 10,164. Three views are excluded from these totals. Artifact size:26,488,832 bytes. SHA-256:`3f7f79d071b7179d7bb68f7c6d17e8cd53c7e4b59941bc85ae6242517fe78bbc`.

With DuckDB and an available httpfs extension:

```sql
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/fars-database/resolve/main/fars.duckdb' AS fars (READ_ONLY);
SELECT state,statename,count(*) AS fatal_crashes,sum(fatals) AS fatalities
FROM fars.crashes GROUP BY state,statename ORDER BY fatalities DESC,state;
```

Pin the dataset commit rather than main for reproducibility. Registry discovery requires the separate registry entry or a local override. The safe crash view aggregates children first; direct vehicle/person joins by crash multiply records. Keys are state/st_case, plus veh_no for vehicles and veh_no/per_no for people, within this year. Nonoccupants have veh_no=0;426 people of per_typ=3 belong to omitted Parkwork and must not be discarded by an inner vehicle join.

## Interpretation

Only fatal traffic crashes are represented, with a death within 30 days. There is no population or travel-exposure denominator here, so counts are not risk rates. Recorded people are not all travelers, and uninjured occupants may be incompletely recorded. No causal or longitudinal-person interpretation is supported.

Raw source fields preserve codes and paired labels; numeric blanks on nonoccupant vehicle attributes become NULL, while blank text stays empty. `crashes` adds reconciled child counts and coordinates with unavailable codes set to NULL. `people` adds age_years(998/999→NULL), measured_bac_g_dl(0–939×0.001), a separate top-code indicator for 940, and recorded-fatal-injury status. Alcohol995–999 means nonmeasurement categories, never zero; police drinking flags and measured tests are distinct. The three alcohol multiple-imputation files are not loaded. This release does not reproduce imputed impairment estimates; analyses across ten imputations must combine estimates rather than average a person's imputed BAC.

`code_labels` retains observed tuples for 30 selected fields, including four city code/context keys with conflicting official names. `unambiguous_code_labels` excludes ambiguous keys for unique lookups. Use all table/column/context/code fields, never code alone. Raw paired labels for other fields remain in their tables. This is not a complete historical code catalog.

Only accident,vehicle,person and the derived dictionary are loaded from the pinned archive. Parkwork, multiple-response factors, detailed drug/race/vPIC files, auxiliary files and alcohol MI tables are omitted. See [source documentation](https://github.com/ian-nason/fars-database) for precise scope, source conflicts, missing codes, update instructions and queries; [DICTIONARY.md](DICTIONARY.md) documents every data column and manual PDF page.

## Provenance, validation and permission

The original 32,672,161-byte ZIP SHA-256 is`5112727a8c0dc91ffee27ca05bddb073934f2d192ce4fae997da767dccdbe04f`. [sources-2024.json](sources-2024.json) records an immutable historical pre-publication evidence snapshot. Every raw typed cell was checked against original CSV/Decimal reads before checkpoint and after read-only reopening; full selected code/label tuples were independently rebuilt. Schemas, metadata, missingness, keys, relationships, all analytic NULL mappings, per-crash count/fatality reconciliation, six examples and 39 fixtures pass. Rebuilds match logical fingerprints and dictionary bytes, not necessarily physical database bytes.

Installed Python/R readers passed localhost HTTP range checks. This evidence does not establish public-host verification; consult the source audit records for later hosting checks and the exact independent review scope. Supplied-evidence review is distinct from independent execution.

Source credit: **National Highway Traffic Safety Administration, National Center for Statistics and Analysis, Fatality Analysis Reporting System,2024 national Annual Report File**, April 1,2026 release. The official [Ownership policy](https://www.nhtsa.gov/about-nhtsa/privacy-policy) permits copying/distribution of website information. No third-party compilation license is borrowed or NHTSA endorsement/trademark permission implied. Cite the release, acquisition date and derivative checksum. This derivative types CSV fields, lowercases names, handles numeric blanks, adds observed labels/metadata and safe views, and preserves source values/codes.
