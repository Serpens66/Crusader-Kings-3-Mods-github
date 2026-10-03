# Leave Wars update sheet

Purpose: a player supporting another leader's war can select a shared war, withdraw and incur configured costs, alliance/opinion consequences and messages. It does not grant withdrawal as primary leader. Standalone and bundle ship fourteen byte-identical content files; update them consistently but test separate distributions.

Evidence: original interaction, complete `events/leave_war_mod_events.txt`, cost values, six game-rule settings, opinions, messages, effect text and translations; current WAR, INT, VALUE and ON sources in [source register](../sources.md). No effect signature or runtime behavior is inferred from the old comments claiming hardcoded limits or tooltip bugs.

## Work packages

| ID | Contract and affected content | Action or gate |
|---|---|---|
| LW-SELECT | `leave_war_interaction_mod`: recipient is allied war leader; on-send saves up to ten war scopes and opens `leave_war_mod.0001` on actor | **Blocked command/chain contract:** establish current war predicates and scope preservation from exports and native dispatch. Retain the existing ten-slot picker; validate candidate membership, same side and non-primary actor at opening and selection. An ended or changed war must produce no costs/effects |
| LW-EXIT | All ten event branches mutate actor, selected war, leader and other participants, then clear eleven saved scopes | **Blocked primitive/lifecycle contract:** obtain `remove_participant`, `clear_saved_scope`, alliance break, prestige/experience and short-term payment signatures. Audit modern native removal callers and war hooks before factoring repeated branches into a shared helper |
| LW-RULES | `leave_war_mod_costs` and four cost values, two opinions, four message types and custom remove-participant effect text | Preserve existing six settings and costs; verify display/actual deltas and current native notifications. Keep custom messages only where they fulfill existing intent without duplicating new native messages |

## Existing numeric policy

Let `tier` be the current engine value of the actor's `highest_held_title_tier`. Baseline costs are `50 × tier` prestige and `25 × tier` gold; half/double settings scale both and the opinion penalties. The event also subtracts prestige experience explicitly. Whether that duplicates any implicit engine change is unresolved until the current command contract and live deltas are checked.

| Setting | Payment/prestige/experience | Leader opinion | Same-side other participant opinion | Alliance break |
|---|---|---|---|---|
| nothing | None | None | None | Still attempted if allied |
| only_opinion | None | -80 | -30 | Still attempted if allied |
| only_prestigehonorgold | Base | None | None | Still attempted if allied |
| default | Base | -80 | -30 | Still attempted if allied |
| half | Half base | -40 | -15 | Still attempted if allied |
| double | Double base | -160 | -60 | Still attempted if allied |

Payment goes to the selected recipient/leader, which also receives prestige when that cost branch is enabled. Opinion values are explicit overrides of attached opinion modifiers. War removal and custom participant/actor notifications occur in every setting. “Nothing” does not currently mean alliance preservation; do not change that established behavior silently.

## Relevant new mechanics

| Mechanic | Classification | Implication |
|---|---|---|
| Adventurer/contract war participation and modern side-switch/removal callers | Relevant | Current `06_ep3_laamp_interactions.txt` removes participants in explicit war scope; decide validity for the mod's existing secondary-participant purpose after full native audit |
| Different top title tiers | Relevant | Price scales use engine tier value; add the highest available tier to tests rather than assuming empire is the maximum |
| New join/leave notifications | Unresolved | Old workaround messages may now duplicate native delivery; compare baseline and mod runs |
| More than ten candidate wars | Existing limit, not new feature | Keep cap; test 11 candidates, document that only ten are offered and ensure no unselected war changes. No new selector/paging system is commissioned |
| Religion/rite conversion, activities and artifact systems | Not relevant to withdrawal logic | Do not add behavior to these systems |

## Exact test scenarios

1. Test actor supporting leader on attacker and defender sides, one shared war each. Expected: selected war loses actor, other wars remain; actor never ends or leads the war through this action.
2. Test all six rule settings at below/exact/above funds, recording gold, prestige, prestige experience, leader receipts, opinions and alliance state. Expected deltas are the table, subject to any documented engine accounting correction.
3. Open selector, then end the war/change leader/remove actor before selecting. Expected updated implementation: no charged no-op, no stale scope effects, no erroneous message.
4. Test zero, one, ten and eleven shared wars, cancel, repeated sends and save/reload with an open event. Ensure the saved-scope cleanup applies to every branch and no previous selection leaks into the next request.
5. Two players withdraw independently; host/client agree on participants and balances. Test hotjoin/save/reload and native/custom message deduplication.

## Completion gates

The actual implementation must not assume that any arbitrary participant can be removed, that an engine predicate name remained valid, or that effects preserve saved scopes across events. Resolve these through the exports and a feature audit of the modern native caller chain, then run [the test protocol](../test-protocol.md). Retain standalone IDs and propagate verified code/translations to the identical bundle copy. No metadata compatibility bump before both distributions pass.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| LW-SELECT | mixed; missing names are not proof of unsupported API | [Card](../contracts/LW-SELECT.md) |
| LW-EXIT | export declarations available | [Card](../contracts/LW-EXIT.md) |
| LW-RULES | export declarations available | [Card](../contracts/LW-RULES.md) |

## Maintenance after future game updates — 2026-10-03

Follow the [mandatory update workflow](../../handbook/mod-update-workflow.md). A request to check this mod includes established targeted corrections after the full affected-feature audit. Run `Documentation/tools/check_mod_updates.py --mod "Leave Wars"`; it is read-only and uses the [reviewed baseline index](../update-watch-index.json). The initial registration has **9 watches** against 1.20.0.3. Unchanged watches do not close the Engine/runtime gates above.

**Watched surfaces:** Native alliance/adventurer war interactions, war hooks/messages and interaction/event/value/message schemas; current Engine war-removal/payment/saved-scope declarations.

**Preserved intent and audit priorities:** Preserve the ten-slot picker, six settings and exact payment/opinion/alliance policy. Check changed participation/caller scopes, ended wars, actor/leader roles, delayed target validity and duplicate native notifications. Engine prestige/experience semantics still require evidence.

**Required regression acceptance:** All settings, 10/11 war candidates, ended/reassigned wars, secondary versus primary roles, exact gold/prestige/experience deltas, save/reload and two players. Bundle is a separate distribution; modify it only when explicitly included in the task.

Known watch lists are curated source registrations, not a complete semantic/transitive graph. Add newly discovered relevant dependencies after their source audit. Keep future reports and baselines dated; preserve older evidence, user edits and distribution identity. No source hash or successful parser run establishes gameplay/GUI/MP compatibility. Release metadata remains gated by the prescribed actual tests unless the user explicitly authorizes a separate target declaration.
