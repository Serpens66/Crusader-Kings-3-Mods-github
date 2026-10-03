# SerpInteractionsDecisions update sheet

Purpose: retain the bundle's existing utility decisions/interactions, their custom prices and consequences. Do not turn compatibility work into a new balance package. All scripts, dependencies, event branches, modifiers and EN/DE text were read; other translations are inventoried. Current native contracts and remaining engine gaps are listed in [sources](../sources.md).

## Feature packages

| ID | Entry points and preserved intent | Source-confirmed finding | Implementation package or gate |
|---|---|---|---|
| SI-ABDICATE | `common/decisions/ABD_decision.txt`: `abdicate_decision`, 20 gold × highest tier, dynasty prestige loss, depose and continue as rightful heir according to EN text | Scalar picture; raw `depose = yes`; modern `depose_effect` supports a landless continuation event and has a DEPOSER parameter | **Blocked succession contract:** trace current title/government/player succession, deposal, Japan abdication and landless continuation. Preserve heir continuation; do not blindly replace raw depose with the modern helper, which can change the intended result. Establish ruler/heir validity and apply costs only on a valid completed action |
| SI-RESOURCES | `convert_resources_decision` → events `.01`–`.08`, income/opinion modifiers, existing 365-day cooldown | Scalar picture; `.07.c` requires/pays 500 gold but unavailable condition compares against 300 at line 800; EN `.01.f` also has a suspicious quote/markup placement | Plan-ready narrow correction: unavailable threshold 500, modern picture block and verified text formatting. **Blocked broader contract:** check current council/portrait contexts, loan accounting, list uniqueness and injury helper before changing execution |
| SI-EDUCATION | `additional_education_interaction` → `.0001`, `.0003`, `.0010`; six disciplines | Recipient modifiers gate study; 367-day study marker, student completion at 365 and actor report at 366. Existing student completion is meant to survive actor death | **Blocked delayed context:** audit and test saved actor/recipient survival, validity, exactly-once reward and marker refresh. Preserve payer/student split and independent student completion, not a new university/education-trait system |
| SI-PARDON | `pardon_hook_interaction`: usable hook, `use_hook`, recipient +20 opinion modifier | Actual operation is use_hook, not an explicit remove-hook effect; modifier is 10 years, delay 1, decaying/stacking, max 75 | **Blocked hook contract:** export/test weak and strong hook consumption. Preserve “pardon hook” purpose; if use_hook only puts a strong hook on cooldown, document the discrepancy and get a behavior decision before substituting a remove operation |
| SI-MONEY | Four `send_mpmoney_*_interaction` IDs: fixed transfers 50/100/250/500 outside diplomatic range | Actor pays recipient in on_accept; 250 variant deliberately allows AI recipient, other amounts require human recipient | Plan the same amount policy and actor-side payment. **Blocked exact payment/state contract:** establish accounting and revalidate funds, target and player control at execution; do not remove the deliberate 250-to-AI exception |
| SI-EXCOMM | Three `temp_*excommunication*` interactions and `temp_excommunication_cost` | All three `excommunicate_character` calls omit required `$EXCOMMUNICATOR$`. Calls to old `trait_is_shunned_or_criminal_in_faith_trigger` have no native helper definition; current helper is Rite-based with RITE parameter | Required adaptations are explicit below. **Blocked religion policy mapping:** preserve custom temporal-authority/cooldown purpose under new faith/rite/head structure before selecting full predicates, redirect and consequence behavior |
| SI-CONVERSION | Bundled conversion decision/counts/translations | Older than standalone: scalar picture, four categories, no tributaries, different protection handling | Follow [Mass Demand Conversion](mass-demand-conversion.md), resolving MC-DISPATCH first; port the verified current category behavior to bundle consistently |
| SI-WARS | Bundled Leave Wars scripts/rules/messages/translations | Fourteen content files byte-identical to standalone | Follow [Leave Wars](leave-wars.md); propagate one verified implementation to both distributions and test them separately |

## Resource conversion baseline

The source menu has prestige→gold, piety→gold, three loan-price families chosen by age/health, forced payments with injury chance, and gold→income investment. Cancel still consumes the decision cooldown because it opens the menu; preserve this documented behavior unless a separate user decision changes it.

| Branch | Existing policy to preserve | Test oracle |
|---|---|---|
| Prestige/piety | Spend 300/500/1000/1500; gain 75/150/325/500 immediate gold plus 5-year monthly income 1.25/2.5/5.4/8.3 | Same numerical policy and modifier IDs; exact engine fame/devotion effects from current exports |
| Borrow | Gain 150/300/500/1000; payment modifier depends on age <50/≥50 and health <3/≥3 | Test age 49/50 and health just below/at 3. Keep each loan amount, duration and monthly value; compare text to actual rounded monthly sums |
| Forced payment | Gold 75/150/250/500, dread 10/20/30/50, tyranny 30/60/105/180, custom income/opinion for 5 years | Adult courtier/councillor/vassal candidates exclude spouse and player heir; test duplicate membership and the existing 10% injury chance per selected candidate |
| Investment | Spend 150/300/500/1000, receive current monthly income modifiers for 5/6/8/14 years | At 499 gold `.07.c` is unavailable; at 500 available absent its modifier; no 300-gold mismatch |

Loan text contains rounded totals/percentages that need checking against actual modifier amounts; do not reinterpret those texts as precise engine repayment formulas. Detailed source amounts remain in original modifier/event files and the source baseline, not replaced by invented amortization logic.

Current landless play can lack council positions used for portraits. This is a concrete audit requirement: preserve the council-centered purpose and establish valid visibility or optional portrait behavior from current native contracts. New influence/merit exchanges are **not relevant** because they would add independent functionality. Persistent candidate lists used for injuries require a current list lifetime/uniqueness check before choosing a clearing/deduplication implementation.

## Additional education baseline

Costs are 5 × recipient skill for diplomacy, martial, stewardship, intrigue and learning; 4 × prowess for prowess. Both gold and prestige are charged. Payer stress +10 and student stress +35; self-study can combine those charges because actor and recipient are the same. Preserve this baseline explicitly rather than inadvertently treating self-study as two characters.

Study temporarily applies -3 to the selected ordinary skill (prowess study uses its existing modifier), plus stress-gain multiplier 0.5. Completion grants +5 to the selected ordinary skill and 10% matching lifestyle XP; prowess completion grants +10 prowess and 10% general lifestyle XP. See `common/modifiers/additional_education_modifiers.txt` for exact per-discipline fields.

The student's own `.0010` completion consumes the study marker; the payer report `.0003` also checks that marker. The two paths are an intentional attempt to prevent lost reward after payer death, **not a proven double-reward bug**. Test student=payer, student≠payer, payer death, student death, changed court, save/reload between days 364–367, repeated menu opens and completion events. Expected result: one completed reward, no payment duplication and no expired marker awarding a stale course. Decide the final state owner only after this lifecycle audit.

New university/activity education, newer trait tracks and new skill modifiers are relevant comparison surfaces, but replacing the custom permanent modifiers with education trait upgrades would change purpose. No such redesign is planned. Current scope persistence and required numeric modifier signatures remain gates.

## Excommunication adaptations

The current native helper definition at `00_religious_interaction_effects.txt:3` and current callers establish three macro arguments: `EXCOMMUNICATOR`, `REQUESTING_CHARACTER`, `TARGET_CHARACTER`. For direct custom excommunication, the intended issuer/requester is the actor and victim is recipient. For requested excommunication, issuer is the authority saved as recipient, requester is actor and victim is secondary recipient. These role mappings must be retained when filling the missing argument after authority redirect is audited.

Current `trait_is_shunned_or_criminal_in_rite_trigger` accepts `RITE`, `TRAIT`, `GENDER_CHARACTER`. Merely renaming the old helper while leaving `FAITH` is wrong. Establish whose current rite governs the original crime/sin predicate and apply that same mapping in **both** interaction eligibility and `temp_excommunication_cost`.

Original direct powers are intentionally restricted to a temporal head with communion, with a two-year cooldown for non-sinful targets and a no-cooldown variant for sinful targets. The requested version redirects through authority and can spend a hook. Current native excommunication instead includes clergy/territorial authority, sacraments, protected targets, empire restrictions, rite/head redirects, issuer tracking, legitimacy, recovery modifiers and notifications. These new mechanisms are **relevant**, but wholesale copying native visibility could eliminate the custom temporal feature. Therefore complete the authority/rite audit before choosing predicates; use current consequence helpers with all role parameters once their contract is established.

The cost formula is `max(50, 200 × piety_level − 50 × sinful_traits + 50 × virtuous_traits − conditional crime discounts)`. Existing discount groups are 200 for qualifying kinslayer_3, 150 for the selected serious group and 50 for the lesser group. Native `min = 50` is a floor, consistent with the author's comment. Preserve arithmetic/order and test low/high piety, every crime group and the floor; do not use an unverified new crime interpretation.

`ai_potential` in these interactions is explicitly deprecated in the current native `.info`. Migrate its actor-only conditions to `is_available` while preserving player eligibility; because `is_available` also affects players, do not transfer an AI-only filter unconditionally. Test AI target evaluation and current response context.

## Test and DLC requirements

Use [common protocol](../test-protocol.md) plus MC/LW sheets. Tests include boundary affordability, player versus AI recipients, multiple governments/tiers, same/missing faith/rite/head, hooks, cooldown/refusal, absent councillors, delayed invalidation and two-player simultaneous actions. Capture exact effects, not just menu visibility.

DLC availability is a **per-feature gate**: trace native helper gates for deposal/adventurer continuation, religious authority/rite mechanics and modern war participation. Test available enabled/disabled combinations that the installed DLC permits. No blanket new DLC dependency is added to the bundle from a native filename.

Preserve namespaces/public IDs and translations. Correct the EN markup issue only after confirming the actual displayed string; do not rewrite untranslated text as English silently. Do not advertise the whole bundle as compatible because one small payment interaction passed.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| SI-ABDICATE | export declarations available | [Card](../contracts/SI-ABDICATE.md) |
| SI-RESOURCES | export declarations available | [Card](../contracts/SI-RESOURCES.md) |
| SI-EDUCATION | export declarations available | [Card](../contracts/SI-EDUCATION.md) |
| SI-PARDON | export declarations available | [Card](../contracts/SI-PARDON.md) |
| SI-MONEY | export declarations available | [Card](../contracts/SI-MONEY.md) |
| SI-EXCOMM | export declarations available | [Card](../contracts/SI-EXCOMM.md) |
| SI-CONVERSION | export declarations available | [Card](../contracts/SI-CONVERSION.md) |
| SI-WARS | export declarations available | [Card](../contracts/SI-WARS.md) |
