# Command and construct quick reference

This is a curated discovery index, **not a complete engine API**. The context column describes the intended use taught here, not an exhaustive list of supported engine scopes. Syntax samples are source-informed; commands outside the mini-mod have not been engine-tested. Parameter variants, target types, DLC gates, budget/lifetime behavior and numeric units must be checked for the actual feature.

Local evidence locations below are relative to the game root in [local-index.json](local-index.json). A line match establishes occurrence, not the enclosing scope or the complete contract. Use [lookup](index-guide.md) to inspect surrounding text and definitions.

| Symbol | Role | Intended context | Form | Local occurrence |
|---|---|---|---|---|
| `is_alive` | trigger | character | `is_alive = yes` | `common/achievements/ep3_achievements.txt:26`; `common/achievements/standard_achievements.txt:189` |
| `is_adult` | trigger | character | `is_adult = yes` | `common/activities/activity_types/camp_party.txt:5`; `common/activities/activity_types/chariot_race.txt:673` |
| `is_ai` | trigger | character | `is_ai = no` | `common/achievements/fp2_achievements.txt:63`; `common/achievements/fp2_achievements.txt:77` |
| `gold` | numeric read | character | `gold >= 5` | `common/activities/activity_types/camp_party.txt:49`; `common/activities/activity_types/camp_party.txt:69` |
| `age` | numeric read | character | `age >= 16` | `common/accolade_names/00_accolade_names.txt:1283`; `common/accolade_names/00_accolade_names.txt:1714` |
| `exists` | trigger | context/reference | `exists = liege` | `common/accolade_names/00_accolade_names.txt:20`; `common/accolade_names/00_accolade_names.txt:45` |
| `always` | trigger | context-independent predicate | `always = yes` | `common/accolade_names/00_accolade_names.txt:4864`; `common/achievements/ep1_achievements.txt:141` |
| `has_trait` | trigger | character | `has_trait = brave` | `common/accolade_names/00_accolade_names.txt:28`; `common/accolade_names/00_accolade_names.txt:29` |
| `has_variable` | trigger | variable owner | `has_variable = doc_score` | `common/achievements/ep1_achievements.txt:9`; `common/achievements/ep1_achievements.txt:106` |
| `has_character_flag` | trigger | character | `has_character_flag = doc_flag` | `common/achievements/ce3_achievements.txt:38`; `common/achievements/ce3_achievements.txt:43` |
| `is_in_list` | trigger | candidate/list context | `is_in_list = doc_targets` | `common/activities/activity_types/camp_party.txt:619`; `common/activities/activity_types/coronation.txt:1949` |
| `add_gold` | effect | character | `add_gold = 2` | `common/activities/activity_types/gruesome_festival.txt:131`; `common/activities/activity_types/hike.txt:179` |
| `pay_short_term_gold` | effect | payer character; target character | `pay_short_term_gold = { target = scope:recipient gold = 5 }` | `common/activities/pulse_actions/tour_actions.txt:944`; `common/activities/pulse_actions/tour_actions.txt:953` |
| `add_prestige` | effect | character | `add_prestige = 10` | `common/activities/activity_types/festival.txt:212`; `common/activities/activity_types/festival.txt:231` |
| `add_piety` | effect | character | `add_piety = 10` | `common/activities/activity_types/funeral.txt:1781`; `common/activities/activity_types/hike.txt:109` |
| `add_stress` | effect | character | `add_stress = 10` | `common/activities/pulse_actions/camp_party_actions.txt:50`; `common/activities/pulse_actions/camp_party_actions.txt:59` |
| `add_trait` | effect | character | `add_trait = brave` | `common/activities/activity_types/wedding.txt:1337`; `common/activities/pulse_actions/camp_party_actions.txt:1060` |
| `remove_trait` | effect | character | `remove_trait = brave` | `common/activities/pulse_actions/pilgrimage_actions.txt:1130`; `common/activities/pulse_actions/pilgrimage_actions.txt:1147` |
| `set_variable` | effect | variable owner | `set_variable = { name = doc_score value = 1 }` | `common/activities/activity_types/chariot_race.txt:506`; `common/activities/activity_types/chariot_race.txt:515` |
| `change_variable` | effect | numeric variable owner | `change_variable = { name = doc_score add = 1 }` | `common/activities/activity_types/chariot_race.txt:396`; `common/activities/activity_types/coronation.txt:2377` |
| `remove_variable` | effect | variable owner | `remove_variable = doc_score` | `common/activities/activity_types/coronation.txt:434`; `common/activities/activity_types/coronation.txt:435` |
| `set_global_variable` | effect | game state | `set_global_variable = { name = doc_marker value = yes }` | `common/activities/activity_types/debate.txt:902`; `common/activities/activity_types/feast.txt:5151` |
| `save_scope_as` | effect | current object | `save_scope_as = doc_target` | `common/activities/activity_types/camp_party.txt:113`; `common/activities/activity_types/chariot_race.txt:417` |
| `save_temporary_scope_as` | selection/temporary helper | current object | `save_temporary_scope_as = doc_target` | `common/achievements/ep2_achievements.txt:234`; `common/achievements/standard_achievements.txt:411` |
| `save_scope_value_as` | effect | chain context | `save_scope_value_as = { name = doc_value value = 1 }` | `common/activities/activity_types/hunt.txt:5643`; `common/activities/pulse_actions/roaming_actions.txt:67` |
| `add_character_flag` | effect | character | `add_character_flag = doc_flag` | `common/activities/activity_types/chariot_race.txt:777`; `common/activities/activity_types/feast.txt:4962` |
| `remove_character_flag` | effect | character | `remove_character_flag = doc_flag` | `common/activities/activity_types/chariot_race.txt:738`; `common/activities/activity_types/coronation.txt:433` |
| `add_to_list` | effect | current candidate | `add_to_list = doc_targets` | `common/activities/activity_types/camp_party.txt:719`; `common/activities/activity_types/camp_party.txt:752` |
| `add_to_temporary_list` | effect | current candidate | `add_to_temporary_list = doc_targets` | `common/activities/activity_types/pilgrimage.txt:64`; `common/activities/activity_types/pilgrimage.txt:117` |
| `add_to_variable_list` | effect | list owner; target object | `add_to_variable_list = { name = doc_targets target = scope:target }` | `common/activities/activity_types/coronation.txt:1971`; `common/activities/activity_types/coronation.txt:1990` |
| `clear_variable_list` | effect | list owner | `clear_variable_list = doc_targets` | `common/activities/activity_types/funeral.txt:1669`; `common/casus_belli_types/07_ep3_wars.txt:6218` |
| `trigger_event` | effect | receiver appropriate to event/hook | `trigger_event = { id = doc_demo.0001 days = 1 }` | `common/activities/activity_locales/tournament_locales.txt:5`; `common/activities/activity_locales/tournament_locales.txt:114` |
| `debug_log` | effect | current chain | `debug_log = "doc_demo executed"` | `common/casus_belli_types/00_religious_war.txt:3318`; `common/casus_belli_types/00_religious_war.txt:3363` |
| `debug_log_scopes` | effect | current chain | `debug_log_scopes = yes` | `common/casus_belli_types/07_ep3_wars.txt:389`; `common/character_interactions/00_prison_interactions.txt:4820` |
| `custom_tooltip` | effect description | current display context | `custom_tooltip = doc_tooltip` | `common/activities/activity_types/camp_party.txt:148`; `common/activities/activity_types/camp_party.txt:220` |
| `hidden_effect` | effect presentation wrapper | inherits current scope | `hidden_effect = { add_gold = 1 }` | `common/activities/activity_types/coronation.txt:3000`; `common/activities/activity_types/gruesome_festival.txt:129` |
| `add_character_modifier` | effect | character | `add_character_modifier = { modifier = doc_modifier years = 1 }` | `common/activities/activity_types/coronation.txt:2809`; `common/activities/activity_types/coronation.txt:2832` |
| `remove_character_modifier` | effect | character | `remove_character_modifier = doc_modifier` | `common/activities/activity_types/feast.txt:173`; `common/activities/activity_types/feast.txt:186` |
| `add_opinion` | effect | opinion holder; target character | `add_opinion = { target = scope:actor modifier = doc_opinion }` | `common/activities/activity_types/festival.txt:256`; `common/activities/activity_types/pilgrimage.txt:2802` |
| `if` | effect control | inherits current scope | `if = { limit = { is_alive = yes } add_gold = 1 }` | `common/accolade_types/04_ep2_common_attributes.txt:35`; `common/accolade_types/04_ep2_common_attributes.txt:46` |
| `trigger_if` | trigger control | inherits current scope | `trigger_if = { limit = { exists = liege } liege = { is_alive = yes } }` | `common/achievements/ce3_achievements.txt:113`; `common/achievements/ep1_achievements.txt:119` |
| `random` | effect control | inherits current scope | `random = { chance = 25 add_gold = 1 }` | `common/activities/activity_types/coronation.txt:2816`; `common/activities/activity_types/coronation.txt:2868` |
| `random_list` | effect control | inherits current scope | `random_list = { 1 = { add_gold = 1 } 3 = { add_gold = 2 } }` | `common/activities/activity_types/feast.txt:4513`; `common/activities/activity_types/hike.txt:413` |
| `any_child` | trigger iterator | character to character candidates | `any_child = { is_alive = yes }` | `common/achievements/ep1_achievements.txt:307`; `common/achievements/standard_achievements.txt:187` |
| `every_child` | effect/formula iterator | character to character candidates | `every_child = { limit = { is_alive = yes } add_gold = 1 }` | `common/activities/guest_invite_rules/activity_invite_rules.txt:615`; `common/activities/guest_invite_rules/activity_invite_rules.txt:625` |
| `random_child` | effect iterator | character to character candidate | `random_child = { limit = { is_alive = yes } save_scope_as = doc_child }` | `common/on_action/travel_on_actions.txt:1681`; `common/scripted_effects/09_dlc_mpo_scripted_effects.txt:2284` |
| `ordered_child` | effect/formula iterator | character to character candidates | `ordered_child = { order_by = age max = 1 save_scope_as = doc_child }` | `common/script_values/09_mpo_values.txt:2554`; `common/script_values/09_mpo_values.txt:2578` |
| `every_in_list` | effect iterator | list context to member type | `every_in_list = { list = doc_targets add_gold = 1 }` | `common/activities/activity_types/coronation.txt:1936`; `common/activities/activity_types/coronation.txt:1945` |
| `is_character_interaction_potentially_accepted` | trigger | actor character; recipient character | `is_character_interaction_potentially_accepted = { recipient = scope:recipient interaction = gift_interaction }` | `common/character_interactions/00_religious_interactions.txt:8577`; `common/character_interactions/00_vassal_interactions.txt:2471` |
| `has_dlc_feature` | trigger | feature context | `has_dlc_feature = royal_court` | `common/activities/activity_types/chariot_race.txt:6`; `common/activities/activity_types/feast.txt:2971` |
| `add_trait_xp` | effect | character | `add_trait_xp = { trait = tourney_participant track = bow value = 1 }` | `common/activities/activity_types/hike.txt:191`; `common/activities/activity_types/wedding.txt:1331` |

## Interpretation notes

- `is_alive`: Life-state predicate.
- `is_adult`: Adult eligibility.
- `is_ai`: Player/AI distinction.
- `gold`: Read balance; not an assignment.
- `age`: Age read; use is_adult for adult policy.
- `exists`: Check target existence.
- `always`: Constant truth value.
- `has_trait`: Trait membership.
- `has_variable`: Guard optional object state.
- `has_character_flag`: Character preference marker.
- `is_in_list`: List membership; verify lifetime.
- `add_gold`: Create/change gold; audit budget treatment.
- `pay_short_term_gold`: Native-style transfer form.
- `add_prestige`: Prestige change.
- `add_piety`: Piety change.
- `add_stress`: Stress change.
- `add_trait`: Trait addition.
- `remove_trait`: Trait removal.
- `set_variable`: Store object-owned state.
- `change_variable`: Adjust existing numeric state.
- `remove_variable`: Cleanup object state.
- `set_global_variable`: Shared state, not per-player preference.
- `save_scope_as`: Name an object for the chain.
- `save_temporary_scope_as`: Short-lived saved target; audit evaluation boundary.
- `save_scope_value_as`: Save chain value; inspect exact signature.
- `add_character_flag`: Set character marker.
- `remove_character_flag`: Remove character marker.
- `add_to_list`: Build chain list.
- `add_to_temporary_list`: Build shorter-lived list; audit boundary.
- `add_to_variable_list`: Object-owned target list.
- `clear_variable_list`: Clear persistent collection.
- `trigger_event`: Explicit event delivery.
- `debug_log`: Debug observation.
- `debug_log_scopes`: Inspect scope stack; verify available form.
- `custom_tooltip`: Text key does not itself perform the described effect.
- `hidden_effect`: Effects execute with suppressed ordinary tooltip text.
- `add_character_modifier`: Attach defined modifier; audit repeat behavior.
- `remove_character_modifier`: Remove attachment.
- `add_opinion`: Directional opinion.
- `if`: Guard state-changing branch.
- `trigger_if`: Guard conditional predicate; choose absence fallback.
- `random`: Probability gate.
- `random_list`: Relative weighted branch choice.
- `any_child`: Candidate conditions directly inside.
- `every_child`: Mutate selected candidates; formula body differs.
- `random_child`: May have no candidate.
- `ordered_child`: Inspect current ordering behavior.
- `every_in_list`: Body requires appropriate list member type.
- `is_character_interaction_potentially_accepted`: Native interaction query, not execution.
- `has_dlc_feature`: Feature gate; validate exact DLC key.
- `add_trait_xp`: Track API needs trait/track dependency and DLC audit.

## Non-command numeric/schema vocabulary

`value`, `add`, `multiply`, `divide`, `min`, `max`, `base`, `modifier`, `factor`, `scope`, `cost`, `is_shown` and `effect` are reader-specific fields/constructs. Their presence in a script does not make them interchangeable engine effects. See [language](../handbook/script-language.md) and [values](../handbook/state-and-values.md).

## Complete signatures and scope links

Generate `script_docs` in an explicitly requested debug session after every relevant patch. The Wiki identifies output under the user `logs` directory, commonly including effects, triggers, event scopes, event targets and modifier/on-action references. Use the files actually produced by the current build; filenames and completeness can change. Record version, run date and the exported file hashes.

Generate `dump_data_types` for UI/data-binding functions and return types. Current source callers remain useful when a function is not documented in an older online table. No current local generated dumps were found during this research, so this collection does not manufacture a complete 1.20 engine signature registry.

External discovery references: [Effects list](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Effects_list.md), [Triggers list](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Triggers_list.md), [Scopes list](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Scopes_list.md), [Data Types](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Data_types.md), [OldEnt versioned dumps](https://github.com/OldEnt/crusader-kings-3-triggers-modifiers-effects-event-scopes-targets-on-actions-code-revisions-list). The effect/trigger Wiki pages explicitly label their tables outdated.

## Debug workflow vocabulary

`-debug_mode` exposes developer access; `-develop` is documented for reloading. Wiki-described tools include console `effect`/`trigger`, `event`, `explorer`, `run`, `release_mode`, `log_viewer`, GUI inspection and command help. Verify availability and context in the current build. A direct console test can bypass the ordinary feature entry point, so also test normal gameplay dispatch.
