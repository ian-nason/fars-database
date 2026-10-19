# Verified public release

> Historical checkpoint, recorded before catalog integration. The dataset is now in the public catalog: [registry PR #7](https://github.com/datapond-db/registry/pull/7) merged on October 18, 2026. The dated checks and version labels below are preserved; see [current consumer guidance](docs/CONSUMERS.md).

Published October 18, 2026. [Dataset](https://huggingface.co/datasets/Nason/fars-database) and [immutable dataset commit](https://huggingface.co/datasets/Nason/fars-database/commit/adb6da02a314c39d8b6caf776529bf4a373075da). The corresponding registry submission is a draft PR; global datapond discovery is not claimed until that PR is merged.

Artifact: `fars.duckdb`, 26,488,832 bytes, SHA-256 `2bc31f9e9fdd973ddf728cc4e1e0811a7bacf9450dd80c7671c36fa6a1fc7442`. All four uploaded files were streamed anonymously from the immutable public commit and matched their frozen sizes/checksums. A 4096-byte range request returned HTTP 206 with the exact Content-Range and original bytes. See publication/public-byte-verification.json.

```sql
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/fars-database/resolve/adb6da02a314c39d8b6caf776529bf4a373075da/fars.duckdb' AS fars (READ_ONLY);
SELECT table_name,row_count,column_count FROM fars._metadata ORDER BY table_name;
```

Installed datapond Python (0.1.1, DuckDB 1.5.4) and R datapond 0.1.0/0.1.1 (DuckDB 1.5.5) passed actual public-HTTPS metadata, row-count and meaningful semantic queries. Python also executed all 6 audited example queries. Before registry merge, tests use a local registry override whose attach_url is the immutable public URL above. Existing httpfs was loaded; no software was installed. Test constructors were bounded to 128 MiB, one thread and no spill, under the 768 MiB group guard. Exact installed package identities and outputs are retained in publication/.

The audited local source snapshot is `b7f7f469de408842f06e60c0f8ace17928fc3d67`; the public source export starts at `e15eaa8611c28a1360e3f61a39ca41bb86c697a0`. PUBLICATION-EXPORT.json maps byte-identical audited source files and any private exclusions. A fresh public history prevents accidental publication of private historical material. This commit adds hosting evidence and a publication-status notice to README; it changes no ingestion code, audited database, dictionaries or source data. Original audit/source manifests and historical pre-publication status text remain intact as evidence.

Independent Claude reviews covered supplied code/documentation/evidence, not independent execution or hash recomputation. Public-host checks were subsequently executed by Codex. All audit findings were resolved before upload. No registry PR merge or CRAN submission is included.
