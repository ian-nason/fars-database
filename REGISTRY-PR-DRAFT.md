Add the pinned FARS 2024 national Annual Report File: all accident, vehicle and person source fields, observed code labels and crash/person views with documented missing-value handling. Crash-level aggregation prevents vehicle/person join inflation; conflicting source labels remain explicit.

Local validation includes all-cell source comparisons, 44 regression fixtures, schema/keys/relationships/missingness/metadata checks, per-crash and national reconciliation, six examples, installed Python/R localhost readers, Codex implementation review and independent Claude review. Public-host checksum/range/client checks must be completed and recorded before opening this PR.

This branch adds only fars. New public destination approval and publication remain pending; no merge is requested.
