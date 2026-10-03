# CK3 mod update readiness

The initial preparation report below records the **as-installed 1.20.0.3 (Crozier)** source tree and unresolved contracts before implementation. At that historical stage no mod, installation file, launcher registration or playset was changed. Subsequently standalone MDC 1.078 was implemented with two active event overrides; see its [notification report](mods/mass-demand-conversion-notifications-20261003.md). For new update requests follow the [mandatory version-independent workflow](../handbook/mod-update-workflow.md). User-run exports are separately recorded in [runtime intake](runtime-intake.md); gameplay/GUI/MP acceptance remains pending.

Research date: **2026-10-03**. All 18,710 previously indexed native text/reference hashes still match. The new workspace baseline covers **853 files**, including binary assets and pre-existing user changes. The first inventory had 851 files; two excluded-root OUTDATED markers appeared during the audit and are preserved. See [workspace observations](evidence/workspace-observations.json) for baseline reconciliation. This establishes reproducibility against the local installation; it does not establish that the installation is an unmodified Steam distribution.

## Start here

| Need | Document |
|---|---|
| Carry out a new mod-update request | [Mandatory workflow and comparison tool](../handbook/mod-update-workflow.md) |
| Select the reviewed comparison baseline | [Baseline index](update-watch-index.json), [initial source registration](update-watch-20261003.json) |
| See every functional work package and its gate | [Feature matrix](feature-matrix.md) |
| Check dependencies and permitted combinations | [Conflict matrix](conflicts.md) |
| Follow the implementation order | [Implementation packages](implementation-order.md) |
| Obtain current engine contracts and fresh logs | [User debug run](debug-run.md) |
| Review the captured engine exports | [Runtime intake](runtime-intake.md) |
| Obtain GUI exports through a normal debug start | [Normal debug starter](diagnostic-start.md) |
| Run later acceptance tests | [Test protocol](test-protocol.md) |
| Locate texture consumers and format/size differences | [Asset consumers](asset-consumers.md) and [texture comparison](texture-comparison.md) |
| Trace evidence and distinguish audit depth | [Evidence and sources](sources.md) |
| Check unchanged sources and documentation quality | [Verification](verification.md) |

## Mod sheets

| Mod | Main result |
|---|---|
| [CustomDefines](mods/custom-defines.md) | 23 active keys exist; prepare removal of 12 Knight Manager files; old GUI type replacements need a current rebase and UI contract check |
| [Gender Colour](mods/gender-colour.md) | Two direct native texture replacements; three additional variants need reference/packaging verification |
| [GFX Mod](mods/gfx-mod.md) | Rank atlas is shorter than current native atlas; shared gender textures conflict with other graphical packages |
| [GFX Mod Serp](mods/gfx-mod-serp.md) | 664 textures need consumer-aware review; six concrete post-effect assignment changes; rank atlas and other dimensions differ |
| [Leave Wars](mods/leave-wars.md) | Standalone and bundle content are byte-identical; current war-state revalidation and command contracts are prerequisites |
| [Mass Demand Conversion](mods/mass-demand-conversion.md) | Current standalone 1.078 declares 1.20.*; [two acceptance overrides](mods/mass-demand-conversion-notifications-20261003.md) now have targeted source/caller watches. [Native tests](mods/mass-demand-conversion-tests.md) and G01–G05 remain open |
| [SerpAlerts](mods/serp-alerts.md) | Eight important-action types and four active hook subscriptions; verify current contexts, overlap and recipient routing |
| [SerpInteractionsDecisions](mods/serp-interactions-decisions.md) | Eight feature families; proven helper mismatch in excommunication; exact 500-gold display bug; succession and delayed education need focused tests |

The independent Knight Manager packages and `test` are excluded from updates at the user's request. Their overlaps are still recorded because enabling them can affect retained packages. No exclusion means deleting their directories.

## Evidence levels

**Source-confirmed** means the stated difference or declarative contract was inspected. **Plan ready** means a narrowly defined change can be specified from that evidence, subject to later validation. **Blocked contract** means no behavioral implementation decision should be made until the named engine or feature-audit gap is resolved. **Runtime pending** means expected results are written but not observed in the game.

The collection read complete developer references and discovered literal source dependencies. That discovery does not complete the semantic audit of every engine primitive, GUI loader or parameter-expanded call. Each sheet identifies exactly where the remaining feature audit must continue. This respects the workspace requirement that unknown Vanilla contracts must not be replaced with assumptions.

## Confirmed priorities

1. Preserve existing purposes and numeric policies. Adapt relevant Vanilla changes without introducing unrelated new capabilities.
2. Test SP and MP using new games. Save/reload of these new test campaigns is required; importing old campaigns is outside the compatibility commitment.
3. Keep standalone/bundle and public/local distributions separate. Do not activate competing variants together.
4. Have the user perform engine-dump and gameplay runs using the supplied protocol. Until then, blocked features remain blocked and no runtime compatibility claim is made.
5. Keep Workshop IDs, public IDs and translations unless an audited migration requires a change. Update supported-version metadata only after the corresponding package passes its tests.

## Scope of the next implementation

Start with the shared evidence and engine gates, then apply the ordered packages. This report is the completed preparation deliverable: every enumerated function has a specified work package or a concrete blocker and a resolution procedure. It is not a claim that all packages are already safe to release.

## Current export and example supplement

The subsequent [standalone MDC 1.077 static migration review](mods/mass-demand-conversion-static-migration.md) records retained Script/GUI interfaces, matching category/query/send bindings, count references and byte-identical old/new fixed-option widget. No necessary functional 1.20 mod patch is demonstrated. Engine option/default/validation behavior, actual GUI/delivery outcomes and delayed/list/multiplayer lifecycle remain open. No compatibility, bundle-port or metadata status is promoted.

The [engine registry](../reference/engine-reference.md), [43 separate contract cards](contracts/README.md) and [function/state guide](../workspace/function-contracts.md) reconcile the available 1.20.0.3 exports. [Completion boundary](../research/completion-report.md) distinguishes export success, structural checks and remaining semantic/runtime gates. The user-test [three-run manual](../examples/test-runs.md) uses separate playsets; do not use the Vanilla diagnostic starter for mod tests. Original update statuses remain unchanged.

## Subsequent repeatable update workflow — 2026-10-03

All eight retained distributions now have current maintenance instructions in their sheets and registered source watches. The new checker compares selected objects, their callers/dependencies, file-level contracts and native replacement assets; it does not refresh baselines or patch mods itself. The task instruction authorizes the agent to complete established corrections after the feature audit. Existing Engine/runtime gates and distribution exclusions remain. Historical 1.077 review statements above are retained as earlier findings, not the current MDC package state. See the [workflow verification](../research/mod-update-workflow-verification-20261003.md).
