# Feature coverage and implementation gates

Every row has an authored sheet containing original intent, local evidence, planned file/ID surfaces, variants, relevant mechanics and test scenarios. All engine/runtime checks remain **not run**. A discovery closure is not substituted for a completed semantic feature audit.

| Feature | Sheet | Status | New mechanics | Exact remaining check |
|---|---|---|---|---|
| CD-COMBAT | [Sheet](mods/custom-defines.md) | plan ready | Relevant: current combat coefficient | Main-phase casualty comparison; engine numerical run pending |
| CD-DYNASTY | [Sheet](mods/custom-defines.md) | plan ready | Relevant: current highest tiers and dynasty contributions | Native keys verified; gameplay contribution/cap test pending |
| CD-MAP | [Sheet](mods/custom-defines.md) | plan ready | Relevant: current map/event UI | Exact keys verified; zoom and option rendering pending |
| CD-RULES | [Sheet](mods/custom-defines.md) | blocked contract | Relevant: current rules/preset UI | UI export, nested loader precedence, current-type rebase |
| CD-LOBBY | [Sheet](mods/custom-defines.md) | blocked contract | Relevant: current character types | Designer overloads and engine post-start permission |
| CD-TOOLTIPS | [Sheet](mods/custom-defines.md) | blocked contract | Relevant: current health UI | Datatype signatures, consumer and rendered values |
| CD-KNIGHTS | [Sheet](mods/custom-defines.md) | plan ready | Relevant: excluded duplicate knight feature | 12-file removal; incoming references and native UI regression |
| GC-ICONS | [Sheet](mods/gender-colour.md) | blocked render | Relevant: current gender/status consumers | Frame selection and render acceptance |
| GC-EXTRAS | [Sheet](mods/gender-colour.md) | blocked consumer | Unresolved: variant consumption | Actual static/dynamic references before packaging changes |
| GC-PACKAGE | [Sheet](mods/gender-colour.md) | plan ready | Not relevant: new gameplay mechanics | Preview present; preserve identity; metadata after tests |
| GS-ICONS | [Sheet](mods/gfx-mod-serp.md) | blocked consumer | Relevant: current icon/trait consumers | 291 absent same paths; 41 size mismatches; current mapping |
| GS-RANK | [Sheet](mods/gfx-mod-serp.md) | blocked contract | Relevant: current title-tier frames | GX-RANK mapping; separate local art validation |
| GS-ILLUSTRATIONS | [Sheet](mods/gfx-mod-serp.md) | blocked render | Relevant: current regiment/character UI | Consumer/aspect/frame rendering |
| GS-CONTAINERS | [Sheet](mods/gfx-mod-serp.md) | blocked render | Unresolved: current PNG-under-dds loading | Current engine acceptance; no silent conversion |
| GS-POST | [Sheet](mods/gfx-mod-serp.md) | plan ready | Relevant: current map volumes/zoom | Six exact assignments; BOM upon editing; render transition test |
| GS-PACKAGE | [Sheet](mods/gfx-mod-serp.md) | plan ready | Not relevant: new gameplay additions | Local registration and credits; do not publish over public variant |
| GX-RANK | [Sheet](mods/gfx-mod.md) | blocked contract | Relevant: current title-tier frames | Current frame mapping and atlas rendering |
| GX-ARTIFACT | [Sheet](mods/gfx-mod.md) | blocked render | Relevant: existing artifact UI states | Current consumers and common/unique/empty rendering |
| GX-GENDER | [Sheet](mods/gfx-mod.md) | blocked render | Relevant: current status frame consumers | Separate graphical distribution and frame test |
| GX-EXTRAS | [Sheet](mods/gfx-mod.md) | blocked consumer | Unresolved: alternate asset consumption | Static/dynamic references; no automatic deletion |
| GX-PACKAGE | [Sheet](mods/gfx-mod.md) | plan ready | Not relevant: gameplay additions | Preserve public/local identity and original credits |
| LW-SELECT | [Sheet](mods/leave-wars.md) | standalone implemented; runtime pending | Relevant: current secondary participation | War predicates, saved context and selection-time revalidation |
| LW-EXIT | [Sheet](mods/leave-wars.md) | standalone implemented; runtime pending | Relevant: modern native war removal | Removal/cleanup/alliance/payment/experience contracts |
| LW-RULES | [Sheet](mods/leave-wars.md) | standalone implemented; runtime pending | Relevant: new title tiers and notifications | Rule arithmetic verified; accounting/duplicates need current engine tests |
| MC-CANDIDATES | [Sheet](mods/mass-demand-conversion.md) | blocked contract | Relevant: tributaries, domicile, diarch, faith/rite | G01/G02/G04: Engine query defaults/validation and dynamic GUI/count/delivery behavior; standalone textual mappings statically checked |
| MC-DISPATCH | [Sheet](mods/mass-demand-conversion.md) | blocked contract | Relevant: current conversion consequences | G01/G02/G03/G05: Engine dispatch/options/validation, actual outcomes and delayed/list/MP lifecycle; no mandatory standalone functional patch demonstrated |
| MC-VARIANTS | [Sheet](mods/mass-demand-conversion.md) | plan ready after MC gates | Relevant: current schema and standalone categories | Standalone GUI/count surfaces statically checked; bundle port and separate-playset/runtime tests still pending |
| SA-JOIN | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current war/diarch constraints | Target-specific query and native scope:target contract |
| SA-STOP | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current vassal-war authority | Current selectable war and correct leader query context |
| SA-EDUCATION | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current child/court eligibility | Editing permission and current education view binding |
| SA-CONVERSION | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current faith/rite/authority | MC query gate; preserve three existing alert categories |
| SA-WAR-START | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current CB context and native messages | Callback sets, list uniqueness and per-side duplicate tests |
| SA-WAR-JOIN | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current joiner/war context | Current participant exclusions and receiver-list contracts |
| SA-DEATH | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: pre-death state and optional killer | Getter/icon timing and current native notification comparison |
| SA-COURT | [Sheet](mods/serp-alerts.md) | blocked contract | Relevant: current court/landless/employer state | Old employer validity, current message delivery duplicates |
| SI-ABDICATE | [Sheet](mods/serp-interactions-decisions.md) | blocked contract | Relevant: governments, landless play, current succession | Preserve heir continuation; full player/title handoff contract |
| SI-RESOURCES | [Sheet](mods/serp-interactions-decisions.md) | narrow fixes ready; execution blocked | Relevant: council availability and accounting; no new currencies | 500 threshold/picture confirmed; loans/injury/list behavior unresolved |
| SI-EDUCATION | [Sheet](mods/serp-interactions-decisions.md) | blocked contract | Relevant: current delayed scopes and skill/modifier system | Student reward exactly once, death/expiry/save lifecycle |
| SI-PARDON | [Sheet](mods/serp-interactions-decisions.md) | blocked contract | Unresolved: weak/strong consumption | Use versus remove-hook semantics and original pardon purpose |
| SI-MONEY | [Sheet](mods/serp-interactions-decisions.md) | blocked contract | Relevant: current budgets and player control | Exact actor-side debit/credit and target revalidation |
| SI-EXCOMM | [Sheet](mods/serp-interactions-decisions.md) | required fixes identified; policy blocked | Relevant: rites, authority, legitimacy, current recovery | Required EXCOMMUNICATOR, removed helper, intended temporal policy |
| SI-CONVERSION | [Sheet](mods/serp-interactions-decisions.md) | blocked by MC | Relevant: current conversion schema/consequences | Same shared MC work package; test bundle separately |
| SI-WARS | [Sheet](mods/serp-interactions-decisions.md) | blocked by LW | Relevant: modern war contracts | Same shared LW work package; test bundle separately |

## Coverage boundary

The 43 work packages group supporting events, rules, values, modifiers, translations and assets with their entry-point behavior. All their lexical definitions are enumerated in [entry points](entry-points.md); all files and textures are in the evidence manifests. Sub-options are specified in the sheets rather than falsely counted as independent mods.

Dormant innovation tweaks, conversion-notification replacements, guest-arrival subscription and delayed death dispatch are explicitly inactive. Independent Knight Manager roots and test are excluded; the embedded CustomDefines component is covered by CD-KNIGHTS. No inactive code is reactivated by a compatibility update.

A gate is resolved only by the specific source/export/test observation stated here and in the sheet. A missing contract cannot be closed by incrementing supported_version or treating a historical log as current.

## Export reconciliation and state contracts

The [43 cards](contracts/README.md) and [function guide](../workspace/function-contracts.md) add declaration evidence and owner/lifetime gates. Current exports are integrated; old rows requesting signatures are historical combined gates, not evidence that exports are still missing. Remaining caller, permission and runtime questions are retained explicitly in each card. Feature tests remain not run.

## Mass conversion source supplement — 2026-10-03

The [focused audit](mods/mass-demand-conversion-audit.md) and [native tests](mods/mass-demand-conversion-tests.md) refine MC gates without changing compatibility status. Export signatures are present; engine initialization, query defaults, lifecycle and runtime evidence remain unresolved. General own-interaction fixture runs do not certify native conversion.

## Subsequent standalone static migration review — 2026-10-03

[New MDC review](mods/mass-demand-conversion-static-migration.md) confirms retained interfaces, category bindings, count references and unchanged fixed-option widget. No necessary functional patch is demonstrated for standalone 1.077. Existing Engine/runtime gates and all runtime statuses remain open; the four-category bundle is not certified. Machine rows retain the preceding resolution wording separately.
