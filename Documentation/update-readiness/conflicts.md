# Mod combinations and distribution conflicts

Evidence: [all collision records](evidence/conflicts.json), [descriptors and hashes](evidence/workspace-baseline.json), [entry points](entry-points.md), and the native loader contracts listed in [sources](sources.md). Recommendations below are a test/playset policy for this update, not a claim that arbitrary load order repairs conflicting definitions.

## Combination matrix

| Combination | Policy | Evidence and consequence |
|---|---|---|
| GFX-Mod + GFX-Mod Serp | Alternative distributions; do not enable together | Same name and Workshop ID `2637472200`, shared assets; local variant intentionally retains additional changes |
| Gender Colour + either GFX package | Require explicit asset ownership; not a certified combination | Both replace `sexuality_icons_female.dds` and `sexuality_icons_male.dds`; compare bytes before deciding which rendering is intended |
| Leave Wars + SerpInteractionsDecisions | Do not enable together in this update | Fourteen matching content files are byte-identical, including interaction/event/rule/message IDs and translations; duplicate distribution of one feature |
| Mass Demand Conversion + SerpInteractionsDecisions | Do not enable together in this update | Same decision/value/localization IDs but divergent generations; standalone adds tributaries and modern picture syntax |
| Independent Knight Manager variants + CustomDefines before removal | Unsupported overlap | Shared knight predicate/UI/callback identifiers and complete `window_knights.gui` replacement |
| Independent Knight Manager variants after CustomDefines removal | Excluded from update/certification | They remain on disk but should be disabled in the test playsets; no current Vanilla equivalence claim was audited here |
| SerpAlerts + standalone conversion/Leave Wars | Candidate combination for later testing | No direct public-ID collision in the checked scripts; related conversion/war messages may still overlap at runtime |
| SerpAlerts + bundle | Candidate combination for later testing | Native interaction queries and custom notifications share subject areas; test duplicate messages and performance |
| CustomDefines after knight removal + retained gameplay mods | Candidate combination | Event-option visibility threshold and GUI changes affect presentation; not just balance keys |
| Either graphical distribution + retained gameplay mods | Candidate combination | Render/icon visibility needs checking, especially missing-interaction icons referenced by the bundle |

Do not activate both a standalone feature and its bundle to test which one wins. Test each distribution independently; consistency is achieved by propagating verified changes to both copies, not by relying on precedence.

## Publication identities and packaging

| Package | Workshop identity | Current advertised version | Packaging note |
|---|---|---|---|
| CustomDefines | 2636812977 | 1.7.* | Also contains UI, localization and knight content |
| Gender Colour | 2602590291 | 1.5.* | Descriptor names `thumbnail.png`; verify actual inclusion before publication |
| GFX-Mod / GFX-Mod Serp | 2637472200 | 1.7.* | Preserve public/local distinction; local Serp external descriptor absent in this workspace |
| Leave Wars | 2643946956 | 1.6.* | Same feature is also shipped inside bundle |
| Mass Demand Conversion | 2753176859 | 1.20.* | Current standalone 1.078; metadata is not runtime certification; older bundle remains separate |
| SerpAlerts | 2637852159 | 1.5.* | Old descriptor is not evidence of an engine failure |
| SerpInteractionsDecisions | 2638425673 | 1.5.* | Contains eight families with different risk levels |

The original preparation left descriptors untouched; the subsequently authorized MDC notification update changed its standalone metadata only. Preserve identities; do not accidentally publish the fuller local GFX package over the public package. Existing graphical credits remain with their respective packages. No third-party asset redistribution rights are newly asserted.

## Loader surfaces to audit during implementation

Same-path files, same object IDs under different files, nested GUI types and localization keys are different loader surfaces. Native event priority rules do not settle GUI type precedence. `11_game_rules.gui` and `11_multiplayer_types.gui` differ from current native filenames but still declare overlapping types; the author's old “loads first” comment is not a current proof.

Current standalone MDC 1.078 defines active priority-1 overrides for `religious_interaction.2002` and `char_interaction.0181`; see the [complete mapping and consequences](mods/mass-demand-conversion-notifications-20261003.md). Other mods defining either ID at the same priority conflict; a higher-priority definition replaces MDC's whole event. Native future changes are not merged into these replacements. The older bundled notification experiment remains commented out. The original statement that both experiments were inactive described the historical preparation stage.

All raw collision candidates, including excluded variants and graphics, remain available in the JSON records. A matching lexical key such as `types`, `window` or a define namespace must not be counted as a proven duplicate gameplay object without reviewing the nested declarations.
