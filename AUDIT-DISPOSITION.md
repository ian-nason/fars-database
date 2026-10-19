# Independent review 01 disposition

> Historical October 18, 2026 checkpoint: the text below is retained as the record of that stage, including its then-pending gates and earlier candidate hashes. It is not current availability or a new approval. Publication and catalog integration are now complete; see the [current README](README.md), [publication receipt](PUBLICATION.md) and [consumer guidance](docs/CONSUMERS.md).

Claude session 6945c837-efac-4ee7-8206-17354fdf79f8 completed initial review on 2026-10-18. All five findings were accepted and corrected before publication. Initial reviewed files are retained in evidence/pre-review01-snapshot, and the original review/prompt/output/session remain inspectable. No waiver or invented approval is claimed.

| Finding | Correction and evidence |
|---|---|
| Medium: NULL comparisons hid absent child groups | Every reconciliation comparison now uses IS DISTINCT FROM. Explicit NOT EXISTS checks reject accidents with no vehicle or person rows. Three new fixtures remove all vehicle rows, remove all people, or set the vehicle fatality aggregate to NULL; all reject. |
| Low: Python 3.10 unsupported | pyproject requires Python >=3.11, consistent with hashlib.file_digest. Tested runtime remains 3.12. |
| Low: numeric NULL/nonoccupant rows only inferred | Read-only validation checks exact row-level equivalence between veh_no=0 and NULL for all 16 numeric fields with source blanks. Two fixtures test correct alignment and equal NULL counts on the wrong people. |
| Low: manual date not evidenced in supplied excerpt | README cites the manual number and checksum without the unsupported date. The ARF release date remains supported by official release notes. |
| Low: missing spaces in public text | Corrected the listed HF card/LICENSE spacing. Hash strings were substituted only by exact value, never broad formatting regexes. |

The corrected artifact is 26,488,832 bytes, SHA-256 `2bc31f9e9fdd973ddf728cc4e1e0811a7bacf9450dd80c7671c36fa6a1fc7442`. All 44 fixtures passed under tests06, with input hashes recorded before execution. The corrected build under release-build02 took 37.10 seconds and peaked at 407.7 MiB sampled process-group RSS. Audit03 and consumer03 passed with the corrected artifact. Every original typed source fingerprint, NULL count, sample and dictionary byte matches the preceding release; previous invariant results remain zero and the new checks pass. No data transformation changed.

The proposed public links remain drafts pending the existing bundled destination approval. No repository creation, source push, artifact upload or registry PR has occurred. After approval and upload, public immutable checksum/range/Python/R checks remain required.
