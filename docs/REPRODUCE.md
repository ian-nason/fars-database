# Build, validation and update details

[Overview](../README.md) · [Dictionary](../DICTIONARY.md) · [Publication verification](../PUBLICATION.md)

These detailed notes preserve the audited release documentation. Statements about local-only checks and later publication gates describe that earlier build stage; [PUBLICATION.md](../PUBLICATION.md) records the completed public-host verification. Catalog integration is still pending.


`source-lock.json` pins the 32,672,161-byte original ZIP (SHA-256 `5112727a8c0dc91ffee27ca05bddb073934f2d192ce4fae997da767dccdbe04f`), every member, release notes and official manual. Download size does not estimate RAM or output size. A changed archive fails closed; do not silently update checksums. The manual is DOT HS 813 794, SHA-256 `210bc33d0572147bf695a39d5261e75158d88b269221e18e460b23d0504cc574`.

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
