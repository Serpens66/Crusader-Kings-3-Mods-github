# SerpAlerts update sheet

Purpose: expose useful actions and notify players about wars, deaths and departing courtiers. Evidence: all action/hook/message/event/localization files, native important-action and on-action contracts, actual interaction counterparts and their helper closure in [sources](../sources.md).

## Important actions

All eight types are in `common/important_actions/serp_alerts_actions.txt`. Native IA allows only interface effects during discovery/click; these contexts must not create ordinary persistent gameplay state.

| ID | Types and original intent | Current contract and implementation gate |
|---|---|---|
| SA-JOIN | `serp_action_can_join_war`: scans allies, lieges, vassals, house, dynasty and same-faith rulers, then opens join-war interaction | Native `join_war_interaction` and `can_join_war_liege_vassal_check_trigger` carry current war constraints; the helper also requires `scope:target`. **Blocked query contract:** validate interaction query's selected-war context and full validity; do not reuse the helper without its actual target |
| SA-STOP | `serp_action_can_stop_attacker_vassal_war`, `serp_action_can_stop_defender_vassal_war` | Audit current `00_vassal_interactions.txt` counterparts and current actor/recipient war leadership. Keep two existing action purposes, recheck before opening, and ensure every displayed target has a selectable war |
| SA-EDUCATION | `serp_action_set_education_child`: children and courtiers/guests aged at least the personality threshold, not adult and with no focus | Current eligibility and `open_view_data` window/getter signatures need export and current education/GUI caller audit. **Blocked engine/UI contract:** a qualifying child is not proof the player can edit its education |
| SA-CONVERSION | `serp_action_demand_conversion_vassal`, courtier and house counterparts | Same native conversion query/context gate as MC-DISPATCH. Preserve existing candidate sets and manual interaction opening; do not turn an alert click into forced conversion or automatically add tributary/bloc alerts |

The join action deliberately has priority 1000; conversion alerts have priority 15 and aggregate by type. Keep existing priorities unless performance/current UI behavior proves a specific defect. A “query says possible” result is not automatically a complete current target validation.

## Notification hooks

The mod appends unique child hooks, preserving native direct effects. Native ON explicitly says child/effect/event chain relationships do not imply arbitrary local-state inheritance.

| ID | Entry point | Original recipients and native contract | Planned work |
|---|---|---|---|
| SA-WAR-START | `on_war_started` → `serp_additional_on_war_started` | Separate attacker/defender receiver groups, family/spouse/heir/title heir/pinning/councillors plus special ally/liege sets; native has CB declaration scopes | Trace each set and exclusion on current callback context. Preserve intentional side-specific messages; verify no accidental duplicate from multiple relationships or new native notifications |
| SA-WAR-JOIN | `on_join_war_as_secondary` → custom child | Root joiner, scope:war supplied by native; relatives/spouses/heirs/title heirs/pinners/councillors, excluding existing participants | Revalidate war and joiner, map recipients to current participants, preserve notification purpose. Use engine list contract/export for duplicate semantics |
| SA-DEATH | `on_death` → custom child | Native root is about to die; `scope:death_reason`, optional `scope:killer` supplied. Mod also adds liege and uses `dead_character.killer` before final death | **Blocked pre-death getter/render question:** use the supplied optional killer contract when preparing correction, after verifying optional icon handling. Preserve the author's preference for pre-death relationship wording; do not switch all messages to the orphan delayed event |
| SA-COURT | `on_leave_court` → custom child | Root departing character; `scope:old_employer` provided; does not fire for departure caused by death | Check old-employer validity before player filter and display, preserve existing message type `character_has_left`, compare current native departure notification to prevent spam |

The optional guest-arrival subscription is commented out. Do not enable it. `events/serp_alerts_events.txt` defines hidden `serp_alerts.0001`, but the only mod dispatch to it is commented out; it is an inactive fallback path for this feature, not the active death notification mechanism. Preserve inactivity or remove only after a separately verified complete reference search.

## New mechanics classification

Current diarch, government, tributary and religious rules are relevant through queried native interactions; preserve the existing alert scope rather than creating new categories. New native messages are relevant to duplicate checks. Court/landless relationships are relevant to old-employer validity and child education editing. Engine list uniqueness, pre-death relationship/getter timing and current interface-only command legality remain unresolved export/runtime contracts. Artifact/activity feature additions are not requested.

## Test cases

- Join/stop alerts: compare every listed target to a manual interaction with a specific war; test internal/external/religious wars, same-side/opposite-side participation, already-called allies and ended wars. No false actionable row that cannot open/select a valid interaction.
- Education: own child at another court, ward, unrelated courtier, guest, focus already set, below threshold and adult. Clicking opens the right child's current education view; only permitted targets are actionable.
- Conversion: use MC scenarios; click opens the same manual native interaction, with proper actor/recipient and no changed consent.
- Notifications: create one character in several receiver relationships, and a player related to both belligerents. Record per-cause/per-side messages and native duplicates. Do not assume list insertion uniqueness.
- Death: natural death without killer, known killer, victim who is player/liege/relative/councillor/pinned. No missing right-icon target or broken relationship text.
- Departure: normal transfer, employer death, independent/landless cases and a character leaving then immediately joining a court. No message routed to the wrong employer.
- Large realm notification/action refresh and two-player MP: record evaluation delays, recipients and desync logs. Native child hooks must continue running.

Behavioral changes remain gated by the exact query, list and UI contracts. The additive subscription structure and provided native callback scopes are source-confirmed. After gates close, factor only repeated interface-safe predicates; do not introduce ordinary list-mutating effects into important-action discovery.
