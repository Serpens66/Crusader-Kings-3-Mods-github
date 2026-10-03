# User debug run for current engine evidence

The user completed the normal debug/main-menu GUI export; see [runtime intake](runtime-intake.md). The [normal debug starter](diagnostic-start.md) and [Start-Vanilla-Diagnostics.cmd](Start-Vanilla-Diagnostics.cmd) remain available only if another Vanilla export is needed; do not use them for mod fixture tests. The former automatic console-action attempt crashed after producing the script references; see [first-run outcome](diagnostic-first-run.md). The steps below remain the broader interactive protocol; campaign/UI checks are not claimed by the revised main-menu run.

The user performs these steps. The agent has not launched CK3, installed a tool, registered a mod or changed launch options. This run establishes the current executed build and engine contracts needed by the blocked packages. It is separate from updating mods.

## Prepare the baseline

1. Record the current launch settings, selected playset and enabled DLC so they can be restored. Choose a new empty test playset with **all mods disabled**, including Workshop/local duplicates and excluded Knight Manager variants. Do not uninstall or delete existing mods.
2. With the game closed, preserve the existing user logs in a timestamped copy. Existing logs here are from 2025. Do not clear old saves or reset the user data directory. Record the copy location and the new run start time.
3. Record the launcher installation version, active DLC list, launch options and test date. Use the actual local executable/launcher installation in the report, not the newest online version number.
4. Launch a controlled singleplayer session with `-debug_mode` using your normal launcher configuration. This is an intentional diagnostic run; restore previous options afterwards. At the main menu record the displayed version and checksum. Start a disposable new game and note bookmark, ruler, government and DLC configuration.

The historical official background is [Paradox Making Mods](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-37-making-mods.1410656/). Current availability and semantics of developer commands must be confirmed in the executed build; the previous Wiki/reference catalogue is not proof that every command is present here.

## Export contracts

In the debug console, check command help/autocomplete for `script_docs` and `dump_data_types`, then invoke each available command. Record the actual accepted command, completion/error message and output location. If a command is absent or produces no output, report that exact result instead of substituting a historical table.

Look for newly written files under:

`C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III\logs`

Use timestamps and the console's output messages to identify files produced by this run. Do not assume filenames: common exports include effects, triggers, scopes/targets and GUI datatypes, but actual names and coverage can differ. Copy only the fresh diagnostic exports and relevant logs into `Documentation/update-readiness/runtime-evidence/<date-and-run>/` when results are supplied. Preserve their original bytes; if a new documentation `.txt`/`.yml` copy lacks BOM, store raw bytes with a `.raw` extension and create a separately marked UTF-8 BOM transcription, never silently recode the source evidence.

For every file, the later intake records path, modification time, SHA-256, executed version/checksum and the command that produced it. Console screenshots/version records can be included if convenient; no personal save is needed just to establish command signatures.

## Required questions for the exports

| Feature | Contracts to retrieve |
|---|---|
| Conversion and alerts | `is_character_interaction_potentially_accepted`, `is_character_interaction_valid`, `run_interaction`, `open_interaction_window`; available saved targets, puppet/actor initialization, consent/validity/cooldown semantics |
| Leave Wars | War predicates, primary/secondary membership, `remove_participant`, `clear_saved_scope`, war iterators and alliance break behavior |
| Payment/resources | `pay_short_term_gold`, `remove_short_term_gold`, gold/prestige/experience/piety operations and numeric modifier semantics |
| Hook pardon | `use_hook`, removal alternatives if documented, weak/strong hook behavior and usable/cooldown conditions |
| Education/notifications | Saved-scope/event delay behavior, lists and ownership/uniqueness, temporary state, optional message/icon targets and pre-death getters |
| GUI | `TryStartRulerDesigning` overloads/types, LobbyView permissions, rule/preset and console functions, `open_view_data`, health/fertility/stress getters, rank-tier frame selection |
| Abdication/religion | Depose/player continuation/title/government contracts; faith/rite/head targets and relevant doctrine/tenet predicates |

Exports might not document lifetime, query initialization or all GUI precedence behavior. Those gaps require small, explicitly scoped feature tests after source review. A matching signature does not by itself establish side-effect or ordering behavior.

## Capture clean logs

Pause after the new game loads, open the ordinary rules/portrait/interaction windows to exercise baseline UI, then exit normally. Preserve fresh `code_revisions.log`, `error.log`, `database_conflicts.log`, `gui_warnings.log`, `debug.log`, `game.log` and other newly relevant files actually produced. Record missing files as missing; do not fill the gap with an old log.

No mod feature test is being claimed by this baseline. Existing Vanilla errors are the reference for later comparison, not automatically mod defects. If the executed build differs from 1.20.0.3 or the source checksums change, stop applying old proposals to the new build and refresh the affected audit.

## Return and intake

Provide the version/checksum, enabled DLC, exact console outcomes, fresh exports/logs and their run folder. The agent can then reconcile signatures with the native caller audit, close named gates in the feature sheets and produce the first implementation package.

Restore the original playset and launch options after diagnostics. Later gameplay tests use separate disposable new campaigns and controlled test playsets, as described in [test protocol](test-protocol.md).
