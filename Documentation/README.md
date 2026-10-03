# CK3 modding knowledge base

This is a working reference for building new Crusader Kings III mods in this workspace. Start here in a new session. The main language is English; script identifiers remain unchanged.

**Research date:** 2026-10-03. **Installed launcher version:** 1.20.0.3 (Crozier). This is an installation-specific baseline, not a claim about the newest public release. Old user logs identify 1.16.3 and are not current API evidence.

## Reading and retrieval map

| Need | Read |
|---|---|
| Develop a new mod safely | [Development workflow](handbook/development-workflow.md) |
| Check and adapt a mod after a game update | [Mandatory update workflow and read-only source comparison](handbook/mod-update-workflow.md) |
| Understand the language | [Syntax and execution contexts](handbook/script-language.md) |
| Work with scopes | [Scopes and contracts](handbook/scopes.md) |
| Conditions, loops and reusable helpers | [Control flow and macros](handbook/control-flow.md) |
| Store data and calculate numbers | [State and script values](handbook/state-and-values.md) |
| Events, decisions and hooks | [Events, decisions and on actions](systems/events-decisions-on-actions.md) |
| Character interactions | [Interactions](systems/interactions.md) |
| Player-facing text and buttons | [Localization and GUI](systems/localization-and-gui.md) |
| Traits, modifiers and balance | [Traits, modifiers and defines](systems/traits-modifiers-defines.md) |
| Other game systems | [Subsystem guide](systems/subsystem-guide.md) |
| Religion and clerical systems in 1.20 | [Religion and rites](systems/religion-rites.md) |
| Puppets and dynamic decision lists | [Puppets and selection](systems/puppets-and-selection.md) |
| Current schema and hook migrations | [Crozier migration](systems/crozier-migration.md) |
| New GUI, asset and diagnostic facilities | [Crozier GUI/tools](systems/crozier-gui-tools.md) |
| Coverage of current source findings | [Crozier source ledger](research/crozier-source-coverage.md) |
| Start from concrete files | [Examples and test scenarios](examples/README.md) |
| Learn from existing work | [Workspace case studies](workspace/case-studies.md) and [inventory](reference/workspace-inventory.md) |
| Current engine declarations | [Versioned engine reference](reference/engine-reference.md) |
| Detailed function/state contracts | [Function guide](workspace/function-contracts.md), [43 cards](update-readiness/contracts/README.md), [Knight variants](workspace/knight-manager-contracts.md) |
| Complete fixture acceptance runs | [Three-run manual](examples/test-runs.md), [completion status](research/completion-report.md) |
| Find a function or an object | [Command quick reference](reference/commands.md), [local lookup](reference/index-guide.md) |
| Compare historical Vanilla versions | [Full local Git reference and commands](reference/vanilla-history.md), [initial 1.19→1.20 findings](research/vanilla-history-20261003.md) |
| Prepare existing mods for the installed version | [Update readiness and per-mod packages](update-readiness/README.md) |
| Investigate Mass Demand Conversion | [Current 1.078 notification overrides](update-readiness/mods/mass-demand-conversion-notifications-20261003.md), [focused source audit](update-readiness/mods/mass-demand-conversion-audit.md), [static migration findings](update-readiness/mods/mass-demand-conversion-static-migration.md), [native acceptance matrix](update-readiness/mods/mass-demand-conversion-tests.md) |
| Assess readiness against the existing mods | [Documentation readiness audit](research/documentation-readiness.md) |
| Check confidence and gaps | [Audit findings](research/vanilla-audit.md), [coverage](research/coverage.md), [sources](research/sources.md) |

## Rules for future agents

1. Read the workspace `AGENTS.md` again. It is authoritative and can change independently of this collection.
2. Establish the user's requested behavior before choosing implementation details. Find the corresponding native entry point and complete the feature-specific Vanilla audit before proposing behavior or writing code.
3. Use this handbook to find evidence; never treat an observed symbol as a complete engine contract. Trace the relevant definition, caller, helper dependencies, scopes, targets and localization.
4. Verify installation version and source hashes when relying on local references after an update. Current generated dumps outrank historical tables for engine API signatures.
5. Prefer a new uniquely named file/object when the loader supports it. Audit the actual override mechanism before overriding existing content.
6. Use a unique prefix for new public identifiers, variables, flags and localization. Follow this workspace's UTF-8 BOM rule for `.txt`/`.yml` and CRLF rule for text files.
7. State exactly what was validated: structural check, source audit, external validator, or gameplay test. Only a gameplay test supports a claim that the feature works in the engine.
8. For a mod-update request follow the [mandatory update workflow](handbook/mod-update-workflow.md), run the selected mod's source watches, complete the affected feature audit and perform necessary targeted corrections. Preserve unknown contracts, historical baselines and pending runtime tests; do not stop at another plan when the correction is established.

## What is available offline

The authored handbook, annotated examples, topic matrix, workspace inventory, 183 developer-reference paths, native definition index and observed command uses can be searched without internet access. The installation itself remains the source for complete Vanilla scripts; it is not copied into the repository. Internet sources are linked and summarized rather than archived wholesale.

The example mod is **not installed or activated**. Its descriptor is a teaching fixture. The original GUI example remains an insertion fragment; the new GUI/frame lab includes additive registration and a complete source-informed binding, awaiting runtime tests.

## Validation report

See the [static verification report](research/verification.md) for checked links, encodings, example structures and source preservation. User-run engine exports have been captured and verified. Fixture gameplay, Tiger validation and GUI rendering remain unperformed.

## Maintaining this reference

See [index tools](reference/index-guide.md). Regenerate indexes after a patch, compare the relevant hashes and review affected teaching statements. Update source dates and coverage explicitly; a new index alone does not revalidate the handbook. No recurring upkeep or automatic game launch is configured.

## Additional jesec research — 2026-10-03

Read [Dynasty legacy contracts](systems/dynasty-legacies.md) for current track/perk scopes, all additional content, relaxed eligibility and the historical/current GUI distinction. The [repository report](research/jesec-repositories.md), [57-page Wiki ledger](research/jesec-wiki-coverage.md) and [additional Wiki guidance](reference/wiki-extensions.md) integrate with the existing Vanilla-history lock and Crozier chapters. Source pins and new static reports are kept separately; existing gameplay/GUI/MP blockers remain.

## Leave Wars standalone update — 2026-10-03

[Current implementation and source audit](update-readiness/mods/leave-wars-update-20261003.md), [structural regression evidence](update-readiness/evidence/leave-wars-verification-20261003.json) and [pending runtime acceptance](update-readiness/mods/leave-wars-tests.md). Only standalone was updated; bundle and compatibility metadata remain unchanged. The [baseline index](update-readiness/update-watch-index.json) now selects the standalone-audited source record while preserving all historical and other-mod baselines.
