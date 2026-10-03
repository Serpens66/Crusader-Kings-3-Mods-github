# Contract supplement validation

Date: 2026-10-03. Installed baseline: 1.20.0.3.

| Executed check | Result | Boundary |
|---|---|---|
| `tools/test_engine_reference.py` | 6 tests passed | Duplicate categories/type owners, unknown-section conservation, reversible decoding, eleven raw hashes/spans, lookup/context |
| `tools/test_contract_labs.py` | 6 tests passed | Own IDs/BOM/localization resolution, cross-package GUI/assets, recipe source hashes, collector freshness/crash exclusions and traversal rejection |
| `tools/verify_documentation.py` | Passed: 733 local links, 176 text files, 25 fixture structures, 157 mod text hashes, 694 original audit hashes, 6 binary fixture hashes | Structural/source checks; no full grammar, engine execution or rendering |
| `tools/finalize_contract_report.py` | Preservation passed with recorded pre-existing instruction drift | 853 original files, 11 raw exports and 1,214 current native contract-source hashes; only previously observed `AGENTS.md` differs |
| `update-readiness/tools/verify_readiness.py` | Strict historical baseline failed only on `AGENTS.md` | Also checked 5,830 consumer-source hashes, 373 native texture hashes and all 43 feature/file assignments; original baseline retained |

Collector tests use synthetic files under Documentation, never real userdata. No live collector run or fixture game test was performed. The six engine tests and six lab/collector tests are separate from the earlier diagnostic-starter tests and the user's actual reference-export sessions.

The general verification report is machine-generated in [verification](verification.md). [Preservation details](contract-preservation.json) retain both original and current hashes for the known instruction-file drift. [Completion boundary](completion-report.md) lists unresolved semantic/behavior gates; [acceptance results](../examples/test-results.md) remain unexecuted.
