# Knight Manager variants: learning-only contracts

All three packages and their text/GUI/descriptors/shortcut bytes were reread and hashed. Current `can_be_knight_trigger`, `can_be_warrior_trigger` and their discovered native `.txt` callers were read in full. [Evidence](knight-manager-evidence.json) preserves exact paths, current parameters, definition ranges, caller lines and state uses. This audit explains local preference wiring; it does not certify complete modern knight eligibility or authorize updating any variant.

## Ownership and execution

The custom `KM_can_be_knight_trigger` evaluates a **candidate character**. `$ARMY_OWNER$` is a required caller substitution pointing to the army owner's character. Relationship predicates compare candidate to owner, but preference flags are read on `$ARMY_OWNER$`. Calling the toggle GUI with a selected knight instead of the player/army owner changes the wrong preference owner. The older actual window constructs `GetPlayer.MakeScope` for group preferences and `Character.MakeScope` for the candidate's manual allowance. These are distinct roots; never copy one for both.

Both variants' custom predicate allows an AI army owner, an acclaimed candidate, or a manually allowed candidate before testing its exclusion set. That bypass applies to the **custom filter only**; it does not prove that all native warrior eligibility can be bypassed. The enclosing copied `can_be_knight_trigger` applies its other conditions as well. Both copies include candidate `is_ai = yes`; this is different from the custom owner's AI check.

Older/manual allowances use candidate character flag `knight_manager_manually_allowed`; Continued uses candidate variable `kmc_manually_allowed`. Group preferences are character flags on owner, not global player settings. Code toggle presence/removal establishes local storage choice; reset on player succession, persistence, invalidation and MP safety require explicit tests and are not guaranteed by a comment saying “MP”. The older startup child sets `KnightManager_is_loaded` globally as an integration marker, not per-player preferences. Its hidden orphan event only references that marker to suppress a validator warning.

## Older filter policy

Older/test preferences cover dynasty kin, vassals, children/grandchildren, spouse plus spouses of descendants, public/secret lover or soulmate, player heir, prowess <6 and 6–12, councillors/court-position holders. Bodyguard/garuda positions are excluded from the latter combined exclusion. The source includes optional dynasty matching and special existence guards in spouse iteration; comments describing null workarounds are historical observations, not engine-contract proof. Group flags toggle in shared ScriptedGui definitions; the real window is a complete native-path replacement.

## Continued filter policy

Continued separates dynasty, house, spouse, descendant, descendant's spouse, heir, lovers/soulmates, councillors, court-position holders, unlanded, highborn/lowborn, above-baron landed and baron-or-lower filters. Its prowess bands are <5, 5–8, 9–12, 13–16 and >16, plus `wounded`. Court-position filter excludes bodyguard/garuda. Manual allowance uses a candidate variable. Exact state names and all occurrences are below.

There is **no actual `.gui` window in the Continued workspace package**. Its `.info.lnk` shortcut is not engine-loaded content. ScriptedGui definitions therefore do not prove that toggles are exposed here. Localization is also absent in this package. Treat incomplete packaging as a concrete learning/consumer gap, rather than claiming a full functional standalone mod. Both variants define native `can_be_knight_trigger` and shared `KM_*` IDs, so they are alternatives and must not be co-enabled.

## Current Vanilla boundaries

Current native definitions have parameterized warrior/knight contracts and are not interchangeable with old full copied predicates. The evidence records exact current keys and callers; [lookup](../tools/lookup.py) retrieves their definitions. The old copies differ in hostage/clergy/cultural/court-position coverage. A modern update would require a complete helper-parameter and eligibility branch comparison plus GUI rebase; it is explicitly out of scope. The current docs retain this blocker rather than manufacturing a “best practice” native replacement from historical code.

For CustomDefines, embedded knight toggles/state/helper dependencies remain a removal-only preparation task. Use the [removal candidate list](../update-readiness/evidence/knight-removal-candidates.json) and CD-KNIGHTS card to preserve unrelated GUI changes; removing an entire shared GUI file would discard other behavior. Existing standalone/test packages stay untouched.

## Learning acceptance cases

Inspect candidate versus owner, acclaimed/manual override versus base eligibility, no-dynasty/spouse contexts, bodyguard/garuda exceptions, exact prowess boundaries, UI checkbox state versus predicate, player succession/save-load and two owners with opposite flags. These are proposed learning tests, **not required updates or completed tests**. The Continue package's absent widget/translation is a prerequisite blocker for its UI cases.

## Knight Manager (MP)

| State/helper token | Exact first occurrence |
|---|---|
| `KnightManager_is_loaded` | [Knight Manager (MP)/common/on_action/knight_manager_on_actions.txt:11](../../Knight%20Manager%20%28MP%29/common/on_action/knight_manager_on_actions.txt) |
| `knight_manager_awful_fighter_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:134](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_bad_fighter_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:156](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_children_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:26](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_councillors_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:90](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_family_spouses_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:48](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_first_row` | [Knight Manager (MP)/gui/window_knights.gui:309](../../Knight%20Manager%20%28MP%29/gui/window_knights.gui) |
| `knight_manager_kin_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:5](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_lover_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:69](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_manually_allowed` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:201](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_mod_error_suppression` | [Knight Manager (MP)/events/knight_manager_events.txt:4](../../Knight%20Manager%20%28MP%29/events/knight_manager_events.txt) |
| `knight_manager_mod_vassals_label` | [Knight Manager (MP)/gui/window_knights.gui:479](../../Knight%20Manager%20%28MP%29/gui/window_knights.gui) |
| `knight_manager_mod_vassals_tooltip` | [Knight Manager (MP)/gui/window_knights.gui:470](../../Knight%20Manager%20%28MP%29/gui/window_knights.gui) |
| `knight_manager_player_heir_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:178](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_second_row` | [Knight Manager (MP)/gui/window_knights.gui:367](../../Knight%20Manager%20%28MP%29/gui/window_knights.gui) |
| `knight_manager_settings` | [Knight Manager (MP)/gui/window_knights.gui:300](../../Knight%20Manager%20%28MP%29/gui/window_knights.gui) |
| `knight_manager_third_row` | [Knight Manager (MP)/gui/window_knights.gui:426](../../Knight%20Manager%20%28MP%29/gui/window_knights.gui) |
| `knight_manager_toggle_awful_fighters_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:130](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_bad_fighters_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:152](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_children_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:22](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_councillors_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:86](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_family_spouses_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:44](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_kin_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:1](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_lover_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:65](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_manually_allowed` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:197](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_player_heir_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:174](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_vassals_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:108](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_vassals_cannot_be_knight` | [Knight Manager (MP)/common/scripted_guis/knight_manager_gui.txt:112](../../Knight%20Manager%20%28MP%29/common/scripted_guis/knight_manager_gui.txt) |

All occurrences and source hashes are retained in [evidence](knight-manager-evidence.json). Token presence does not establish an active caller or correct native contract.

## Knight Manager Continued (MP)

| State/helper token | Exact first occurrence |
|---|---|
| `kmc_average_fighter_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:360](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_barons_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:294](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_child_spouses_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:96](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_children_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:73](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_councillors_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:162](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_court_position_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:184](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_dynasty_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:5](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_excellent_fighter_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:404](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_good_fighter_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:382](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_highborn_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:228](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_house_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:28](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_landed_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:272](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_lover_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:140](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_lowborn_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:250](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_manually_allowed` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:452](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_player_heir_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:118](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_poor_fighter_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:338](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_spouses_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:51](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_terrible_fighter_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:316](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_average_fighters_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:356](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_barons_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:290](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_child_spouses_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:92](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_children_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:69](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_councillors_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:158](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_court_position_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:180](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_dynasty_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:1](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_excellent_fighters_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:400](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_good_fighters_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:378](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_highborn_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:224](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_house_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:24](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_landed_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:268](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_lover_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:136](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_lowborn_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:246](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_manually_allowed` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:448](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_player_heir_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:114](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_poor_fighters_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:334](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_spouses_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:47](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_terrible_fighters_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:312](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_unlanded_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:202](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_toggle_wounded_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:422](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_unlanded_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:206](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |
| `kmc_wounded_cannot_be_knight` | [Knight Manager Continued (MP)/common/scripted_guis/kmc_gui.txt:426](../../Knight%20Manager%20Continued%20%28MP%29/common/scripted_guis/kmc_gui.txt) |

All occurrences and source hashes are retained in [evidence](knight-manager-evidence.json). Token presence does not establish an active caller or correct native contract.

## test

| State/helper token | Exact first occurrence |
|---|---|
| `KnightManager_is_loaded` | [test/common/on_action/knight_manager_on_actions.txt:11](../../test/common/on_action/knight_manager_on_actions.txt) |
| `knight_manager_awful_fighter_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:134](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_bad_fighter_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:156](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_children_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:26](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_councillors_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:90](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_family_spouses_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:48](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_first_row` | [test/gui/window_knights.gui:309](../../test/gui/window_knights.gui) |
| `knight_manager_kin_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:5](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_lover_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:69](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_manually_allowed` | [test/common/scripted_guis/knight_manager_gui.txt:201](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_mod_error_suppression` | [test/events/knight_manager_events.txt:4](../../test/events/knight_manager_events.txt) |
| `knight_manager_mod_vassals_label` | [test/gui/window_knights.gui:479](../../test/gui/window_knights.gui) |
| `knight_manager_mod_vassals_tooltip` | [test/gui/window_knights.gui:470](../../test/gui/window_knights.gui) |
| `knight_manager_player_heir_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:178](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_second_row` | [test/gui/window_knights.gui:367](../../test/gui/window_knights.gui) |
| `knight_manager_settings` | [test/gui/window_knights.gui:300](../../test/gui/window_knights.gui) |
| `knight_manager_third_row` | [test/gui/window_knights.gui:426](../../test/gui/window_knights.gui) |
| `knight_manager_toggle_awful_fighters_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:130](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_bad_fighters_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:152](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_children_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:22](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_councillors_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:86](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_family_spouses_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:44](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_kin_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:1](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_lover_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:65](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_manually_allowed` | [test/common/scripted_guis/knight_manager_gui.txt:197](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_player_heir_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:174](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_toggle_vassals_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:108](../../test/common/scripted_guis/knight_manager_gui.txt) |
| `knight_manager_vassals_cannot_be_knight` | [test/common/scripted_guis/knight_manager_gui.txt:112](../../test/common/scripted_guis/knight_manager_gui.txt) |

All occurrences and source hashes are retained in [evidence](knight-manager-evidence.json). Token presence does not establish an active caller or correct native contract.
