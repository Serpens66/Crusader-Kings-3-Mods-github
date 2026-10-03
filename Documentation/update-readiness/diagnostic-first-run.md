# First automatic diagnostic run: failed exit with retained exports

Reviewed on 2026-10-03. Source: [original run manifest](runtime-evidence/20261003T005950.086458Z/run.json). This manifest and its raw evidence remain unchanged.

The first `script_docs` start ran from 00:59:50 UTC until 01:01:25 UTC and returned exit code **1**. The game wrote a crash report at 03:01:23/24 local time (UTC+02), within that stage. Its `exception.txt` identifies **1.20.0.3** and **C0000005 / EXCEPTION_ACCESS_VIOLATION**. Its stack trace supplies no CK3 function names, so the specific failing operation is unknown. Neither an auto-exit defect nor a user-profile defect is established.

All six required script-reference files were produced before the failure: effects, triggers, scopes, targets, modifiers and on-actions. All saved stage-file hashes were checked against the original manifest and matched. File tails contain ordinary reference entries; this is not a proof that every engine entry was emitted. The original fresh `code_revisions.log` is empty and therefore cannot establish version or checksum. The crash report establishes the executed version; checksum review remains pending.

The helper correctly marked the run incomplete and did not start `dump_data_types` or the history stage. It restored the original mod selection; the current selection's SHA-256 matched the manifest's original hash during intake. The next normal-start workflow does not regenerate the six script exports.

Fresh error logs contain AGOT rule references. These are recorded as retained-user-profile warnings rather than evidence of active AGOT mods or a demonstrated crash cause. No profile, rule preset, setting or save cleanup was performed. The debug log identifies the loaded preorder DLC; full environment and mod absence still need evidence review.

Crash sources inspected read-only:

- `C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III\crashes\ck3_20261003_030123\exception.txt`
- `C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III\crashes\ck3_20261003_030123\meta.yml`
- Saved stage `debug.log.raw` and `error.log.raw` under the original run folder.

The revised helper will capture new/changed crash text, metadata and log files automatically. Personal saves and memory dumps are excluded. See [normal debug starter](diagnostic-start.md) and [source audit](evidence/diagnostic-start-audit.json) for the retained export paths and hashes.
