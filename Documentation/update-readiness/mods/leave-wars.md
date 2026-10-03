# Leave Wars update sheet

Purpose: a player supporting another leader's war can select a shared war, withdraw and incur configured costs, alliance/opinion consequences and messages. It does not grant withdrawal as primary leader. Standalone and bundle originally shipped fourteen byte-identical content files. The authorized 2026-10-03 update changes only standalone; bundle is intentionally retained at its earlier state. Synchronize only under a separate authorized bundle request.

Evidence: original interaction, complete `events/leave_war_mod_events.txt`, cost values, six game-rule settings, opinions, messages, effect text and translations; current WAR, INT, VALUE and ON sources in [source register](../sources.md). No effect signature or runtime behavior is inferred from the old comments claiming hardcoded limits or tooltip bugs.

## Work packages

| ID | Contract and affected content | Action or gate |
|---|---|---|
| LW-SELECT | `leave_war_interaction_mod`: recipient is allied war leader; on-send saves up to ten war scopes and opens `leave_war_mod.0001` on actor | **Standalone implemented; runtime pending:** current war predicates and direct-chain declaration audited; live propagation/invalidation still require LW-T cases. Retain the existing ten-slot picker; validate candidate membership, same side and non-primary actor at opening and selection. An ended or changed war must produce no costs/effects |
| LW-EXIT | All ten event branches mutate actor, selected war, leader and other participants, then clear eleven saved scopes | **Standalone implemented; runtime pending:** current primitive declarations, native departure callers and alliance/war context audited. Existing ten legacy branches remain separate; test accounting, cleanup and native callbacks |
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

The actual implementation must not assume that any arbitrary participant can be removed, that an engine predicate name remained valid, or that effects preserve saved scopes across events. Resolve these through the exports and a feature audit of the modern native caller chain, then run [the test protocol](../test-protocol.md). Retain standalone IDs. Bundle propagation is outside the authorized standalone update and its unchanged code is not newly certified. No standalone metadata compatibility bump before its required tests pass.

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

## Implemented standalone update — 2026-10-03

Current [implementation/audit report](leave-wars-update-20261003.md), [runtime acceptance protocol](leave-wars-tests.md), [source evidence](../evidence/leave-wars-source-audit-20261003.json) and [static result](../evidence/leave-wars-verification-20261003.json) supersede the original source-blocked intake for this standalone revision. War-role/side/live-funds guards and all exit/cancel/new-send cleanup are implemented. Matching paid assistance is abandoned without payout; selected-war Frankokratia membership is cleaned. Optional pure personality stress and the native ten-year assistance failure flag are independently toggled and default on, including under Free.

All original prices, opinions, manual notifications/tooltip workaround and ten branches remain. The three custom message filters are updated. Gameplay/GUI/MP, old-save new-rule resolution and notification deduplication remain **not run**. Descriptors remain at 1.121 / 1.6.*. The new comparison baseline updates only standalone Leave Wars; historical baseline, raw exports and bundle remain unchanged.
