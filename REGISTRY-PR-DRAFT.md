> Historical October 18, 2026 checkpoint: the text below is retained as the record of that stage, including its then-pending gates and earlier candidate hashes. It is not current availability or a new approval. Publication and catalog integration are now complete; see the [current README](README.md), [publication receipt](PUBLICATION.md) and [consumer guidance](docs/CONSUMERS.md).

Add the pinned FARS 2024 national Annual Report File: all accident, vehicle and person source fields, observed code labels and crash/person views with documented missing-value handling. Crash-level aggregation prevents vehicle/person join inflation; conflicting source labels remain explicit.

Local validation includes all-cell source comparisons, 44 regression fixtures, schema/keys/relationships/missingness/metadata checks, per-crash and national reconciliation, six examples, installed Python/R localhost readers, Codex implementation review and independent Claude review. Public-host checksum/range/client checks must be completed and recorded before opening this PR.

This branch adds only fars. New public destination approval and publication remain pending; no merge is requested.
