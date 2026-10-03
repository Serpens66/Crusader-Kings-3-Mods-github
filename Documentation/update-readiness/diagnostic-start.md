# Normal debug start and manual GUI export

Updated on 2026-10-03 for **1.20.0.3 (Crozier)**. The revised normal-start workflow has **not been run in CK3**. It replaces the automatic console-action workflow after the first attempt crashed. See [observed first-run outcome](diagnostic-first-run.md).

## Your next run

1. Keep Steam running. Close CK3 and the Paradox launcher.
2. Double-click [Start-Vanilla-Diagnostics.cmd](Start-Vanilla-Diagnostics.cmd) in Explorer. Keep the terminal open until completion; do not reopen the launcher during the run.
3. At the main menu, open the debug console and enter `dump_data_types` once. Wait for the export to finish.
4. Exit the game normally. The helper then captures evidence and restores your original mod selection.

Starting with Steam's ordinary Play button does not activate the helper. This starter opens CK3 once, with `-gdpr-compliant -debug_mode -suppress_error_log`. It sends no console command, operates no mouse or keyboard, loads no save, and does not close the game automatically. It does not repeat `script_docs` or launch the old history stage. An authentication or other interactive dialog remains your action.

## What is automatic

Read-only preflight checks the installed version, hashes of audited sources and executable, running CK3/known launcher processes, the existing mod-selection schema and unfinished recovery records. A changed source stops the run before changing the mod selection. `--preflight` performs these checks without launching CK3 or modifying userdata.

The helper creates a unique folder under `Documentation/update-readiness/runtime-evidence`, backs up all existing logs and exact `dlc_load.json` bytes, then temporarily empties `enabled_mods`. Other fields, including `disabled_dlcs`, are retained. No playsets, launcher databases, settings, presets or saves are edited. Existing script exports and earlier evidence folders are retained.

After game exit, new/changed logs are copied into `main-menu-data-types`. Fresh nonempty files directly under the `data_types` output tree are required; unchanged old exports do not satisfy the check. Each copy has its original path, modification time, byte size and SHA-256 in `run.json`. Child process output is recorded separately if the game supplies any.

New/changed crash evidence is compared against the pre-launch snapshot. Only each report's `exception.txt`, `meta.yml` and `logs/*.log` files are eligible for copying into the run's `crashes` directory. Saves, settings and memory dumps are neither read for this capture nor copied. A crash report marks the run incomplete even if the exit code is zero and exports exist; a nonzero exit or missing fresh export also marks it incomplete. A crash report that is not yet written when collection occurs may be absent; the game exit code and collection errors are still retained.

All source copies have a `.raw` suffix and retain exact bytes, avoiding silent BOM or line-ending conversions. Documentation validators skip this evidence tree; manifests protect its raw hashes. AGOT rule references in fresh logs are recorded as existing-profile warnings with no asserted relationship to a crash. No cleanup of the user profile is attempted.

The original mod selection is restored byte-for-byte on completion and handled failures. If another program edits the selection during the run, that edit is preserved, the manifest remains incomplete and the original backup is available for review. Windows byte-range locking prevents concurrent helper runs. The persistent `diagnostic-start.lock` is only a lock carrier; Windows releases the active lock if the helper crashes.

## Interrupted run or missing export

Keep the terminal open until completion. The helper waits without imposing a timeout or killing CK3. It periodically reminds you to export and exit normally. Ctrl+C is ignored while the child runs, to prevent restoring enabled mods under a live game. Closing the terminal forcibly or restarting Windows can interrupt restoration.

For recovery, close CK3 and the launcher first. From workspace PowerShell, use the actual run-folder path printed by the terminal:

    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' -B '.\Documentation\update-readiness\tools\diagnostic_start.py' --restore '<absolute run folder>'

Recovery verifies the backup hash and restores only over the helper's temporary configuration or an already restored original. External edits require review; do not overwrite them blindly. Do not start another diagnostic run after an interrupted run until restoration is resolved. Missing exports are reported as missing rather than replaced by historical files.

## What this run establishes

This is a GUI export and **main-menu baseline with the existing user profile**, not a clean-profile certification, history-completion test or mod compatibility claim. Campaign ticks, feature-window checks, save/load and multiplayer remain pending under the [test protocol](test-protocol.md). Logs must still be reviewed for actual version/checksum, loaded mods/DLC, datatype content and baseline diagnostics. Empty `code_revisions.log` is not version proof. Successful capture is called `captured-review-pending`.

After completion, tell the agent that the diagnosis finished. Evidence is already in the shared workspace; no upload is needed. The agent can verify fresh outputs and reconcile them with the retained script references and feature audits.

## Sources and verification

The complete current native `_commandline_options.info` documents debug mode at lines 46-47 and error-window suppression at 57-58. Launcher metadata supplies the executable and `-gdpr-compliant`/debug arguments. The previous actual crash report demonstrates that the executable ran version 1.20.0.3; this is historical run evidence, not proof that the revised workflow succeeds. Paths, hashes and contracts are recorded in [diagnostic source audit](evidence/diagnostic-start-audit.json).

The primary [Tiger developer procedure](https://github.com/amtep/tiger/wiki/Updating-to-new-game-versions), accessed 2026-10-03, specifies `dump_data_types` and the `logs/data_types` output tree. Command execution and full export contents must still be observed in the revised run.

Offline tests exercise exact normal-start arguments, old/empty/missing exports, raw-byte capture, capture races, crash allowlisting, new versus old reports, warning classification, successful mocked completion, launch failure, crash with and without nonzero exit, exact restoration and preservation of external edits. All process launches in integration tests are mocked; no game or real userdata writes occur.

Preparation results: **13 offline tests passed** and read-only preflight passed for **1.20.0.3 (Crozier)** with two selected mods. Documentation links/encoding checks passed. Source-preservation checks match all mod and audited game files; the older workspace baseline reports a changed `AGENTS.md`, already present when this revision began. That file was not edited, and the old baseline was not rewritten. No revised game start or real userdata mutation was performed during preparation.
