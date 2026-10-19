# Changelog


## 2026-10-18 — Documentation refresh

- Added Python/R quick starts, table descriptions and column counts, view guidance, navigation, and clearer researcher caveats.
- Database bytes, schema, source locks and validated query results are unchanged. Catalog integration was pending at that checkpoint and was completed later on October 18.

## 2026-10-18 — Initial release

- FARS 2024 ARF (first release): 190,798 rows across 4 tables (413 columns) and 3 views; 36,297 crashes, 39,254 fatalities. Artifact 26,488,832 bytes, SHA-256 `2bc31f9e…fc7442`, commit `adb6da02`.
- Every typed cell verified against an independent read of the pinned source ZIP; per-crash count and fatality reconciliation; public immutable URL, HTTP range requests and the installed Python and R clients tested after upload.
- Registry entry opened as a draft pull request, then merged after integration review on October 18.
