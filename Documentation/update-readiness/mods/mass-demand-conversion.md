# Mass Demand Conversion update sheet

## Acceptance descriptions corrected in1.080 — 2026-10-07

[Current two-notification fix](mass-demand-conversion-message-context-20261007.md): user-tested vassal acceptance did not crash but exposed recipient-name localization failure. Both overrides now supply desc in their event message call; the common type uses event_message_text. Native effects/previews and eight translations retained;28 static tests. Corrected rendering and house/mixed acceptance tests remain open; foreign crash unresolved. Engine exports1.20.0.3 are stale for installed1.20.0.4.


## Short effect preview — 2026-10-05

[Current eight-language text shortening](mass-demand-conversion-short-effect-20261005.md): only the effect-preview sentence changes;35 keys, confirmed GUI layout, gameplay and version1.079 remain unchanged. New dateline preserves all63 watches/history and refreshes eight localization hashes. One-to-two-line wrapping remains untested.


## User-confirmed MDC layout — 2026-10-05

The user confirms that the [fixed-slot recipient layout](mass-demand-conversion-fixed-rows-20261005.md) now looks correct in game. Use that code and its documented geometry as the current visual reference; preserve the failure ledger. This is visual acceptance of the reported presentation, not a complete transition/scaling/scrolling, percentage, delivery or multiplayer certification. Earlier pending-rendering statements describe pre-confirmation states.


## Fixed recipient slots — 2026-10-05

[Current fixed-slot layout](mass-demand-conversion-fixed-rows-20261005.md): latest user screenshot disproves the caption-only correction, including first-open/filter-switch differences. Five permanent slots and explicit radio/text coordinates replace automatic recipient measurement; confirmed filter/viewport and all functional bindings remain. 26 static checks;63 native watches. New rendering remains untested; read the failure ledger before reuse. Earlier dated sections describe historical states.


## Common recipient columns — 2026-10-05

[Current caption-only correction](mass-demand-conversion-radio-columns-20261005.md): user confirms preceding viewport size correction centers the list and shows all five groups. Eleven native recipient captions now have identical285×30 fixed left-aligned fields; filter/scrollbox structure and bindings retained. 24 static tests pass; new column rendering remains untested. Failure ledger records the partial user confirmation.


## Scrollbox nominal-size correction and failed-layout ledger — 2026-10-05

[Current isolated correction](mass-demand-conversion-scroll-size-20261005.md) and [mandatory screenshot-backed failure ledger](mass-demand-conversion-gui-failures-20261005.md). Latest screenshot confirms filter placement but recipient viewport displacement. Native inherited100×100 size is now explicitly overridden514×210; no list/filter behavior change. 23 static tests pass; rendering remains untested. Read the ledger before further GUI changes.


## Git recipient-list restoration — 2026-10-05

[Current restoration and pending game matrix](mass-demand-conversion-git-targets-20261005.md): user reported first-open row overlap and continuing filter inset. Entire native-radio scrollbox subtree restored from Git a81d7f3; custom recipient template removed. Filter heading/columns now use explicit top-left parent/own anchors and x0/122/249/351 positions. 22 static checks pass; first-open/filter-change rendering remains untested. Version 1.079 and gameplay/texts/history retained.


## Explicit flexible-space alignment — 2026-10-05

[Current correction and pending game matrix](mass-demand-conversion-flex-alignment-20261005.md): latest screenshot disproves prior recipient centering and shows filter inset. Explicit 514×32 filter viewport/trailing expander and full-size recipient hbox/equal expanders replace anchor-only alignment. 22 static tests pass; actual rendering remains untested. Gameplay/texts/1.079 metadata, bundle and historical evidence are retained.


## Narrow filter row and centered recipient contents — 2026-10-05

[Current patch and pending runtime matrix](mass-demand-conversion-centered-options-20261005.md): 451-wide left-origin filters inside the existing 514-wide section; only recipient rows use a local native-derived button with centered radio/text content and full-width click regions. Screenshot confirms preceding list fits but is left-aligned and filters still overflow. All gameplay/texts/1.079 metadata and historical records remain; new rendering and MP are untested.


## Current widget alignment — 2026-10-05

[Alignment audit and runtime check](mass-demand-conversion-alignment-20261005.md): latest user screenshot confirms five groups, none mark and indirect count21, but shows right-edge overflow. Current GUI follows native centered flowcontainers, zero-origin overlays and expanding 450-wide rows within a conservative 467-wide scroll content budget. Twenty static tests and 54 native watches; corrected alignment still requires game verification. Gameplay/texts/version1.079 are unchanged. Earlier dated sections retain their original states.


## Current compact widget correction — 2026-10-05

[Compact widget audit, source changes and runtime matrix](mass-demand-conversion-compact-widget-20261005.md): the user demonstrated missing groups and overflow in the previous GUI. Current source now uses a bounded horizontal filter row, native scrollbox, creation-time reset and none fallback, plus explicit effect-preview text. All 35 keys in eight languages and 19 static tests checked; 53 native watches registered. Corrected GUI rendering, unfiltered zero-count parity and MP remain untested. Mod version stays 1.079; earlier sections describe dated states.


## Current standalone localization/version — 2026-10-05

[Version 1.079 localization review](mass-demand-conversion-localization-20261005.md): all eight languages/34 keys checked, Korean fallback text replaced, terminology and grammar corrected. Both standalone version fields incremented; supported-version and runtime/MP status unchanged. Earlier dated findings below remain historical.


## Current standalone chance filter — 2026-10-05

The authorized [chance-filter implementation and source audit](mass-demand-conversion-chance-filter-20261005.md) adds none / at least 80% / 100% to the same five visible groups. Eleven fixed native entries carry selection to gameplay; local GUI state controls display only and resets on opening/closing. Direct/indirect vassals and tributaries use native `ai_accept` thresholds; courtiers and house remain unfiltered. Zeros count zero requests and do not hide the decision. Preserve native negotiations, existing protection policy and normal request dispatch; 100% describes immediate calculated acceptance, not completed conversion.

The new dated baseline retains all 40 previous watches and adds nine file/interface watches (49 total), covering GUI templates/lifecycle/datamodel and percentage-query callers. Preserve fixed entry order and all eleven entries when maintaining the widget. Run `Documentation/tools/test_mdc_chance_filter.py` after edits; its structural checks do not replace the linked runtime matrix. GUI initialization/index ordering, percentage parity/rounding at 80/100 and concurrent two-player routing remain release blockers. Notification overrides, standalone metadata, bundle and historical baselines are preserved. Earlier sections below describe their dated states.


Purpose: shorten repeated manual conversion requests by selecting a category of people and sending native interactions. Preserve native eligibility, refusal, consent and consequence chains. This is not forced direct conversion. Evidence: full standalone/bundle decision and count files, translations, current CONV/CONVE/RITE/INT/DEC sources and native GUI controller in [source register](../sources.md).

## Distribution differences

The standalone decision already uses the modern picture/reference block, `decision_group_type = admin`, a tributary category and five count values. The bundle has older scalar picture syntax and four categories without tributaries. Both share public decision and count IDs. These are different generations of one feature, not independently composable mods.

At the original review both `accept_conversion_notification.txt` files contained only comments, and replacing letters was outside that review’s scope. The subsequently authorized standalone 1.078 notification update is documented below; the older bundled experiment remains inactive.

## Work packages

| ID | Existing flow and source | Current Vanilla contract | Action or gate |
|---|---|---|---|
| MC-CANDIDATES | Decision visibility, widget, effect and script-value counts for direct/indirect vassals, tributaries, courtiers and house | Native vassal interaction includes `target_is_liege_or_above` or tributary, AI ruler restriction and newer validity checks; house interaction now has bloc-related conditions | Audit each original category against the corresponding native interaction, preserving category purpose. Share exactly the same eligibility and actor context across visibility, displayed counts and send loop |
| MC-DISPATCH | `is_character_interaction_potentially_accepted`, `run_interaction`, `send_threshold = decline` | Native consequences include modern conversion, clan/state-faith/tenet and response chains. Several current triggers expect `scope:puppet_or_actor` | **Blocked engine context:** determine what these commands initialize and whether the query checks full validity/cooldown/acceptance. Never synthesize a puppet scope or bypass interaction stages from guesswork; native authority/consent must remain intact |
| MC-VARIANTS | Standalone modern schema versus old bundle; all translations/counts | Current decision-option widget uses `OnSelect` and radio state at `gui/decision_view_widgets/...controller.gui:28–38` | After MC-DISPATCH is resolved, port the verified standalone categories/schema/count behavior into the bundle while preserving shared public IDs and distribution identity. Validate one chosen category per execution |

## Relevant native changes

The current `valid_demand_conversion_conditions_trigger` adds landless domicile requirements, nomadic conditions, promises not to convert, diarch restrictions and direct-contract religious protection. The current vassal interaction also handles tributaries and domicile/steppe restrictions. Current house conversion can recognize house confederation/bloc relationships, but this mod presently enumerates the actor's house only. **Do not automatically add a new bloc-wide category**; preserve the existing enumeration and let native predicates handle members already within it.

The original extra `religiously_protected` filter applies to all vassal candidates, while the native shared trigger explicitly ties protection to a direct liege. That is a confirmed predicate difference, not proof the mod should remove its stronger filter. Preserve the author's protection policy unless a separately explained correction is required; tests must record direct and indirect cases distinctly.

Rite/faith changes and new religious consequences are relevant because dispatch invokes the current native interaction. Puppet/diarch behavior is an unresolved context requirement, not authorization to add puppet controls. Unrelated activities/artifacts are not relevant. Current DLC gates must be retained through native dispatch; do not hardcode the presence of a DLC from a filename.

## Tests with expected outcomes

- Each category separately: at unchanged state, displayed count matches the query-positive execution candidate set. If state changes between display and execution, record both snapshots and recheck candidates. Record actual deliveries and conversions separately; family outcomes are not extra mod requests. Selection behaves as a radio choice and no other category is processed.
- Same faith, protected direct vassal, protected indirect vassal, tributary, courtier, house ruler, house member who is also vassal, prisoner, missing house and active cooldown. No invalid or duplicate request.
- AI accepts, refuses or requests a concession/study-faith step. Native outcomes, prices and later events remain available; `send_threshold` must not be interpreted as forced acceptance.
- Current faith/rite, domicile, diarch, government and DLC cases where available. Verify generated scope errors and correct actor/recipient identity for query and actual send.
- Rapid repeats, resource changes, large court/realm and MP two actors. No cross-player recipient mixing or disproportionate UI evaluation delay.
- Standalone and bundle in separate playsets, with matching intended category behavior and translations. No active conversion notification override.

## Blocker resolution

Current command signatures have been obtained; their full forms and documented limits are in the [dated audit supplement](mass-demand-conversion-audit.md). Compare native manual interaction with script query/dispatch using the [native test matrix](mass-demand-conversion-tests.md). The missing puppet_or_actor fallback is source-confirmed in later conversion effects; earlier query/dispatch initialization, option flags and full cooldown/pending validation remain unknown. Finish remaining caller/engine contracts before choosing a shared helper. MC-DISPATCH still blocks behavioral changes; no compatibility status was promoted.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| MC-CANDIDATES | export declarations available | [Card](../contracts/MC-CANDIDATES.md) |
| MC-DISPATCH | export declarations available | [Card](../contracts/MC-DISPATCH.md) |
| MC-VARIANTS | export declarations available | [Card](../contracts/MC-VARIANTS.md) |

## Dated source-audit supplement (2026-10-03)

[Audit and source hashes](mass-demand-conversion-audit.md) · [22 native acceptance cases](mass-demand-conversion-tests.md) · [Machine evidence](../evidence/mass-conversion-audit-20261003.json). This supplement records category-specific eligibility, conditional costs, response/family/secret-faith/study chains and actual macro bindings. It distinguishes five remaining gates G01–G05. The study completion relationship guard requires special indirect-vassal/tributary coverage. All gameplay/GUI/MP tests remain **not run**; the Vanilla feature audit is not declared complete.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.

## Subsequent static migration review (2026-10-03)

The [standalone 1.077 migration review](mass-demand-conversion-static-migration.md) records 14 retained Script interfaces, three exported GUI bindings, matching category/query/send IDs and textual bindings, eight languages with correct count references, unchanged widget bytes and the unchanged 15-year native cooldown. The current 295 native seed hashes still match. No necessary functional mod patch is demonstrated; this does not prove runtime compatibility. G04 textual mapping is checked, while its actual GUI/count/delivery behavior remains open. G01/G02/G03/G05 keep the narrower Engine/runtime gates. The complete feature audit remains unclosed where contracts are unknown.

The existing protection policy and cooldown are regression topics, not demonstrated new 1.20 defects. Effective actor, rite consequences, the new concession and study promise are real native changes to probe. The bundle port is not included in this standalone conclusion. No metadata or mod-code change was made.

## Notification update 1.078 — 2026-10-03

The explicitly requested standalone update is now implemented for declared target 1.20.*. [Notification source audit, effect mapping and validation](mass-demand-conversion-notifications-20261003.md) distinguish this added behavior from the historical finding that no mandatory functional migration patch was demonstrated. Only religious_interaction.2002 and char_interaction.0181 become hidden priority-1 overrides using the shared merging feed type; native conversion remains tooltip-only here, and native Minister/adventurer rewards and puppet notifiers are preserved. Current callers of these IDs are globally affected, including manual requests. Gameplay/GUI/MP remain **not run**, including MC-N01–MC-N11. Earlier query/dispatch gates are unchanged; metadata 1.078/1.20.* does not close them. Historical statements above about inactive overrides and unchanged metadata describe the preceding review, not the current package. The older bundle remains unchanged.

## Maintenance after future game updates — 2026-10-03

Follow the [mandatory update workflow](../../handbook/mod-update-workflow.md). A request to check this mod includes established targeted corrections after the full affected-feature audit. Run `Documentation/tools/check_mod_updates.py --mod "Mass Demand Conversion"`; it is read-only and uses the [reviewed baseline index](../update-watch-index.json). The initial registration has **40 watches** against 1.20.0.3. Unchanged watches do not close the Engine/runtime gates above.

**Watched surfaces:** Two full acceptance definitions and every direct scalar/block-form script caller; explicit conversion/notifier helpers, reward values, native conversion/study lifecycle, schemas and eight message templates.

**Preserved intent and audit priorities:** Prioritize the full native IDs religious_interaction.2002 and char_interaction.0181. Their replacements do not merge upstream fields. New immediate/option/after effects and new real decisions must be examined; preserve root/actor/recipient/puppet roles, notifier guards and exactly-once Minister/adventurer rewards. Conversion calls stay tooltip-only. The shared feed type reports acceptance, not completed family conversion or study.

**Required regression acceptance:** Run MC-N01–MC-N11 and applicable MC-T cases after a full restart. Record acceptance, completed conversion and reward counts independently. Test merging detail retention, manual/Minister/local-ruler callers, puppet delivery, refusal/gold/favor/study choices, save/reload and two players; conflicts at the same event IDs remain.

Known watch lists are curated source registrations, not a complete semantic/transitive graph. Add newly discovered relevant dependencies after their source audit. Keep future reports and baselines dated; preserve older evidence, user edits and distribution identity. No source hash or successful parser run establishes gameplay/GUI/MP compatibility. Release metadata remains gated by the prescribed actual tests unless the user explicitly authorizes a separate target declaration.
