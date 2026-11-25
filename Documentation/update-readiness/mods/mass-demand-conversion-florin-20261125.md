# MDC Florin source review and 1.081 target declaration — 2026-11-25

Installed **CK3 1.21.0.3 (Florin)**; previous selected MDC audit **1.20.0.4**, with versioned Vanilla Git comparison pin **1.20.0.3 / 0ec13350cde9e410b37a46d3616966838f4ba994**. The authorized standalone target is **mod1.081**, **supported_version="1.21.*"** in both descriptors. This is a target declaration requested by the user, **not a completed runtime compatibility or multiplayer certification**. Bundle and independent packages remain outside this change.

[Florin source audit](../evidence/mdc-florin-source-audit-20261125.json) and [final verification](../evidence/mdc-florin-verification-20261125.json) record the pinned reference, the comparison of the65 existing watches plus4 additional native acceptance dependencies, file preservation and final static checks. Source verification is complete; Engine and runtime gates remain open. All earlier reports, baselines, user observations and raw exports remain historical evidence.

## Result: no gameplay, event or GUI patch demonstrated

The feature-specific comparison found no required change to the existing standalone decision, five recipient groups, eleven fixed native selections, none/80/100 filters, count/send queries, conversion dispatch, hidden acceptance overrides or fixed-slot GUI. Preserve the existing native query with ai_accept thresholds rather than substituting demand_conversion_likelihood_calculation. The native interaction remains responsible for eligibility, acceptance/refusal, negotiations, conversion, family/secret-faith processing and subsequent consequences. Do not weaken religious protection or expand house membership to a larger group as part of this maintenance update.

The confirmed fixed-slot GUI composition and current filter geometry remain the visual reference. The current native controller/GUI review did not demonstrate broken selection or layout bindings. Native file/context changes alone do not justify restoring any earlier failed flowcontainer, caption-width-only or flexible-space composition. See the [GUI failure ledger](mass-demand-conversion-gui-failures-20261005.md) and [user-confirmed fixed-slot reference](mass-demand-conversion-fixed-rows-20261005.md). Source checks cannot replace rendering after a full restart under Florin.

## Acceptance overrides and message contract

Both complete native event definitions remain unchanged relative to the pinned1.20 source, although their surrounding files may change or move their lines:

| Mod override | Native counterpart in1.21.0.3 | Result |
|---|---|---|
| religious_interaction.2002 | events/religion_events/religious_interaction_events.txt:1271–1336 | Complete event unchanged; no new immediate, option, after or decision branch |
| char_interaction.0181 | events/interaction_events/character_interaction_events.txt:1459–1479 | Complete event unchanged; only surrounding context/line position differs |

All four complete caller objects in common/character_interactions/00_religious_interactions.txt are unchanged: house demand509–779, vassal demand781–1384, Minister of Rites1693–2035 and adventurer local-ruler attempt8674–9209. Current dispatches at614/921/1793/8849 still enter scope:puppet_or_actor. Keep that event receiver and the native actor/recipient/puppet distinctions. Overrides continue to affect manual as well as scripted demands; same-ID mods can still conflict.

An ordered AST comparison of each current mod override against installed Vanilla confirms the deliberate transformation:2002 retains executable native immediate blocks outside the old previews plus the single-option executable reward;0181 retains native immediate. Original conversion previews remain under show_as_tooltip inside the feed message. No new executable conversion, omitted choice, extra reward or required event rewrite was found. notify_puppeteer_of_outcome_effect and demand_conversion_vassal_ruler_interaction_effect are unchanged. Reward references remain minor_influence_gain=30, minor_piety_gain=50 and trivial_fervor_value=0.15 with the native tier/condition multipliers; keep them as native references rather than literals.

The updated native messages reference clarifies display defaults, title syntax and icon naming. The existing explicit display=feed, combine_into_one=yes, icon="religious", title, tooltip and description transfer remain consistent with that contract. Native msg_admin_provincial_army_request_denied still uses desc=event_message_text and supplies the localized desc in send_interface_message; event_message_text still expands $DESCRIPTION$. Keep the1.080 fix: both mod events supply desc=mdc_conversion_accepted_desc, while the shared message type uses event_message_text. **Correct recipient-name rendering after that fix remains untested in the recorded game evidence.**

## Native changes inherited without copying or patching them

Three directly relevant conversion objects changed behavior within the monitored source surfaces:

1. **Confession penalty:** common/scripted_effects/00_religious_interaction_effects.txt:1067–1134, demand_conversion_interaction_effect, now tests pam_confession_penalty_var against flag:conversion and separately checks pam_confession_penalty_target against scope:recipient. It clears both variables when applying the outcome. MDC delegates to this helper, so the new contract is inherited automatically. Do not copy the old helper or add a mod-owned replacement. The family-selection and family-conversion helpers remain unchanged.
2. **Ecclesiastical domicile acceptance bonus:** common/scripted_modifiers/00_religion_scripted_modifiers.txt:26 onward, religion_demand_conversion_default_modifier, now accepts the corresponding domicile parameter from either scope:recipient.liege.domicile or scope:puppet_or_actor.domicile for all three building levels. Native acceptance calculations and MDC's existing ai_accept query inherit this bonus; no separate acceptance calculation or added payment/hook is needed.
3. **Validity/clerical region:** common/scripted_triggers/00_religious_triggers.txt:1203–1287, valid_demand_conversion_conditions_trigger, makes the shrine-domicile access optional and adds the clerical-region capital-faith restriction. A demand is blocked when the recipient holds a clerical-region title whose capital county has a faith different from the effective requester's faith. Preserve delegation to the native predicate; do not bypass this restriction or introduce a speculative parallel mod filter.

Further changes are in delegated lifecycle systems, not in copied mod implementations:

- **Study promises:** study_faith now requires an un-imprisoned teacher. Teacher imprisonment can invalidate the scheme and offers the native continuation route; saved progress and scheme modifiers are retained for continuation. Learning/piety/theologian contributions to the study scheme's success are reduced. These are study-scheme values, not new Demand Conversion percentage thresholds.
- **Learning outcomes and continuation:** study_faith_outcome.1000/.1200/.1400 require playable learners; the.1500 fallback also handles nonplayable learners. The new continuation helper restores scheme modifiers but removes the four previous-teacher-specific modifiers. All three continuation choices use it, followed by saved-modifier cleanup. Leave those native choices and cleanup intact.
- **Children and baptism:** convert_to_rite_with_consequences_effect in11_dlc_pam_scripted_effects.txt:18–106 now restricts all knowledge-based piety/stress/convert-modifier penalty branches to adults. Children still reach ordinary rite assignment and subsequent general flags. The baptism check captures the actual current converter as baptism_convert rather than assuming event root is that character, important for family conversion. No MDC age or scope patch is required.
- **Secret faith:** false_conversion_events.txt changes only false_conversion.2000 among its object definitions, adding fallback vulnerable-relation sources when the normal characters-of-interest list misses them. The initial conversion events.0900/.1000/.1010 are unchanged. Record this as downstream native behavior, not an additional MDC feature or forced secret-faith choice.

## Validation, regressions and remaining limits

All28 existing static MDC tests pass with the updated metadata assertions. The linked final verification records source-watch/reference status, encodings, metadata preservation and precise file changes. The historical version-pinned1.078 checker is not a current compatibility gate and must remain unchanged.

The engine exports available in the knowledge base are still versioned1.20.0.3. Fresh1.21 exports and runtime tests are absent. No claim that unchanged script objects establish unchanged compiled-engine behavior is made. Preserve UTF-8 BOM for script/localization files and original line endings; only the authorized descriptor version fields and associated maintenance/test evidence change.

After a full restart, the Florin regression matrix must cover:

- All five groups and three filters: first opening, filter/group changes, reopen, stable radio columns, count/send equality, full click areas, zero targets, long labels, scaling and scrolling. Preserve the native none/80/100 selection contract.
- Native per-target UI acceptance versus script thresholds, including near80/100 and the changed domicile-bonus source; ordinary single and bulk requests. Verify clerical-region capital-faith eligibility and absent-domicile cases without relaxing native guards.
- Accepted vassal and house requests: correct localized name/portrait, no ERROR: or new corresponding log errors, valid mixed/merged feed descriptions/tooltips. Native courtier and guarded puppeteer notifications must remain distinct. Check requester identity, exactly-once conversion/rewards, relevant Minister/adventurer cases, refusals and negotiations.
- Native study promise followed by teacher imprisonment or teacher replacement: appropriate continuation, preserved progress/general modifiers, removal of previous-teacher modifiers, cleanup and save/reload behavior. Playable/nonplayable learning outcomes must stay native.
- Adult versus child family converters and family members whose event root differs: penalties only where native conditions allow, baptism using the actual converter, no mod-triggered second conversion. Secret-faith changes remain a downstream regression consideration.
- Two players choosing different groups/filters concurrently, correct independent requests/messages, save/reload and no desynchronization.

The earlier user-run single accepted vassal request did not crash but exposed the pre1.080 recipient-name localization error; the name correction still has no recorded successful game result. The separate user's reported crash remains **unresolved**, not fixed by this target-version declaration. No publication, blanket compatibility statement or multiplayer certification is included.

## Final pinned comparison and static verification

The upstream tag base/1.21.0.3 was fetched into the existing reference cache without checkout changes. Its dereferenced commit is e529e0063a4f41786380fa2827c01736d9c14d15. All54 audited source paths match the installed1.21.0.3 bytes; this verifies the local source comparison, not independent Steam-depot authenticity or Engine compatibility. The old checkout0ec13350cde9e410b37a46d3616966838f4ba994 and all historical baselines remain unchanged.

The new [dated watch baseline](../update-watch-mdc-florin-20261125.json) refreshes the65 existing MDC watches and adds four precise native dependencies: cathedral-awe acceptance modifier and the three domicile acceptance values15/30/45. The native OR bonus conditions do not cause the same modifier to be counted twice. Other mods' watch records are retained verbatim. Both standalone descriptors change only version1.080→1.081 and supported_version1.20.*→1.21.*; corresponding two test literals are updated. No gameplay, notification, localization, GUI or bundle bytes change.

All28 static tests pass. The [verification evidence](../evidence/mdc-florin-verification-20261125.json) records the final69-watch result, reference identity, preservation, encodings and links. A stale Engine-export status is expected and remains an open gate: no game launch, current binary export, complete renderer/count/percentage/consequence test or multiplayer acceptance was performed. This section and evidence record source verification only; outstanding game tests are not marked as passed.
