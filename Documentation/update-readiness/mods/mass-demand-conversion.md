# Mass Demand Conversion update sheet

Purpose: shorten repeated manual conversion requests by selecting a category of people and sending native interactions. Preserve native eligibility, refusal, consent and consequence chains. This is not forced direct conversion. Evidence: full standalone/bundle decision and count files, translations, current CONV/CONVE/RITE/INT/DEC sources and native GUI controller in [source register](../sources.md).

## Distribution differences

The standalone decision already uses the modern picture/reference block, `decision_group_type = admin`, a tributary category and five count values. The bundle has older scalar picture syntax and four categories without tributaries. Both share public decision and count IDs. These are different generations of one feature, not independently composable mods.

Both `accept_conversion_notification.txt` files contain only comments. They are inactive historical experiments. Preserve that inactivity; compatibility work does not authorize replacing conversion letters with custom messages.

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

- Each category separately: displayed count equals the eligible send set at execution time; changed state is rechecked. Selection behaves as a radio choice and no other category is processed.
- Same faith, protected direct vassal, protected indirect vassal, tributary, courtier, house ruler, house member who is also vassal, prisoner, missing house and active cooldown. No invalid or duplicate request.
- AI accepts, refuses or requests a concession/study-faith step. Native outcomes, prices and later events remain available; `send_threshold` must not be interpreted as forced acceptance.
- Current faith/rite, domicile, diarch, government and DLC cases where available. Verify generated scope errors and correct actor/recipient identity for query and actual send.
- Rapid repeats, resource changes, large court/realm and MP two actors. No cross-player recipient mixing or disproportionate UI evaluation delay.
- Standalone and bundle in separate playsets, with matching intended category behavior and translations. No active conversion notification override.

## Blocker resolution

Obtain current command signatures and run a minimal actor/recipient comparison between the UI's manual interaction and the script query/dispatch. Capture scope diagnostics, cooldown, validity, consent and side effects. Finish the native initialization/caller audit before choosing a shared helper implementation. Until then MC-DISPATCH blocks behavioral changes; modern picture syntax and inactive-event classification are independently source-confirmed.
