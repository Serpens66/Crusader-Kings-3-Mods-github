# Developing and validating a new mod

Evidence: workspace `AGENTS.md` and descriptors, [Mod structure, Modding, compatibility, troubleshooting and Tiger sources](../research/sources.md), plus [current native loader findings](../research/vanilla-audit.md).

## Start with a concrete behavior

Describe the trigger, eligible objects, visible result, state changes, AI policy, costs and failure behavior. A feature request such as a mass action needs an exact candidate set and a decision about whether it invokes the native interaction or bypasses it. Find the closest current Vanilla feature before choosing that approach.

Complete the audit before proposing script behavior. Read the relevant `.info` files, entire definitions, their callers and transitive helpers. Record guaranteed and optional scopes, ownership of stored data, timing, DLC gates, effects shown in previews and actual execution. Generated command signatures and supported scopes are required when usage examples do not settle a contract. If a contract is still unknown, identify the gap rather than filling it with a guess.

## Files and descriptors

A content root mirrors the paths below the game's `game` directory: `common/decisions`, `events`, `localization/english`, `gui`, etc. The launcher uses an external `.mod` descriptor pointing to that content root. The content root also contains `descriptor.mod` for metadata/packaging. A repository containing several mods is not itself one content root.

Keep mod `version` distinct from `supported_version`. A supported-version wildcard is a declared compatibility range, not proof that the code works on every matching patch. An external descriptor's machine-specific `path` is not part of a portable Workshop content package. Do not reuse another mod's `remote_file_id` when creating a new mod.

The teaching descriptor in [examples](../examples/README.md) contains no publication ID. It is not registered in the user's installed-mod directory. For actual development, use the launcher-created descriptor or an audited manual setup, then verify the launcher points at the files being edited.

## Encoding and identifiers

This workspace requires UTF-8 **with BOM** for every `.txt` and `.yml` and CRLF for text files. Preserve the encoding of existing files unless the user permits changing it. Documentation Markdown is UTF-8 with CRLF. Verify actual bytes rather than relying on an editor's default.

Use a unique mod prefix for events, helper keys, variables, lists, flags, rules, modifiers, GUI actions and localization. Keep event namespaces consistent. Repeated entries inside a definition may be intentional; duplicate public definitions need a loader-specific explanation.

## Override choices

| Change | What to establish |
|---|---|
| New independent object | Correct database path, unique identifier and required references |
| Same relative path as Vanilla | Whole-file overlap; review all upstream changes and other mod collisions |
| Same object in a different file | Database-specific merge/override rule; filename priority is not universal |
| Add a callback to an on action | Append a uniquely named child on action instead of replacing the native effect |
| Override an event | Native event reference documents `id_override_priority`; hot reload has different priority handling |
| Override history character data | Native reference documents partial override plus additive dated content; do not assume complete replacement |
| Replace localization | Audit the `replace` loader convention and verify displayed result |
| `replace_path` | Removes an entire Vanilla path from the content set; use only if this broad removal is intended |

The older Wiki says individual event/history overrides are impossible. The local 1.20 references document newer mechanisms. Their documented caveats are part of the contract. Do not use either a global alphabetical-load rule or an old prohibition for every subsystem.

For compatibility patches, list exact modified paths and identifiers. Non-overlapping files can still conflict through shared object names, variables, callbacks or a removed dependency in a total conversion. Load order resolves some conflicts but does not combine incompatible gameplay logic automatically.

## Validation levels

1. **Structural:** verify files, encoding, namespaces, matching references, balanced syntax and localization keys. The included documentation checker is deliberately limited.
2. **Source audit:** trace the exact contracts and expanded helper parameters against the installed version. Note the feature-specific audit boundary.
3. **External validator:** if a compatible Tiger release is available, run it against the mod descriptor and the correct installation/dependency configuration. Review warnings rather than hiding unfamiliar errors. This task does not install Tiger.
4. **Runtime:** use a clean playset baseline, then enable the mod; record version, DLC, start date and test save. Compare new errors in `error.log`, `database_conflicts.log`, `gui_warnings.log` and relevant debug output.
5. **Behavior:** test success, ineligibility, absent target, cancellation/decline, repeated execution, state changes during delays and save/reload. Add AI and multiplayer checks when relevant.

Wiki-documented developer tools include `-debug_mode`, `-develop`, `script_docs`, `dump_data_types`, console `effect`/`trigger`, the explorer and file runner. Available commands and reloading behavior must be checked in the actual build. Some database/GUI changes need a restart. A successful hot reload does not prove cold-start behavior, particularly when override priorities are involved.

For Tiger, consult its [upstream usage](https://github.com/amtep/tiger). A typical invocation is `ck3-tiger path/to/descriptor.mod`; use `--game` when automatic detection chooses the wrong installation. Its README explicitly acknowledges false positives and update lag. Validation is evidence, not a replacement for an engine test.

## Packaging and publication

After gameplay validation, confirm the package includes all referenced text, localization and assets and excludes debugging leftovers. Check paths on a case-sensitive system when distributing cross-platform. Describe dependencies, required DLC, compatibility footprint and actual tested game versions.

Workshop metadata and launcher UI can change. Check the current publishing workflow at release time; do not automatically publish a documentation example or assign an existing Workshop ID. Preserve the local/Workshop distinction while testing so the launcher loads the intended copy.

## Handling a game update

Follow the [mandatory mod-update workflow](mod-update-workflow.md). Recheck launcher version and the selected mod's last reviewed source baseline, run the read-only per-mod comparison, inspect complete changed definitions/callers/helpers and current API dumps, then carry out established targeted corrections. Preserve historical indexes and baselines instead of overwriting them during reference refresh. Review behavior, not just parsing; distinguish source registration, feature audit, static checks and actual game tests. Existing descriptors can advertise old versions without proving a code defect. Current MDC 1.078 has two active acceptance event overrides, both requiring complete upstream-event review after a patch.

## General Crozier source supplement — 2026-10-03

Use the [Crozier migration contracts](../systems/crozier-migration.md), [diagnostic/reload boundaries](../systems/crozier-gui-tools.md), and [coverage ledger](../research/crozier-source-coverage.md) for current schema changes. Event and character-history priority fields are distinct. No new diagnostic launch or tool installation was performed.
