# CustomDefines update sheet

Purpose: preserve the author's combat/dynasty balance changes, map visibility, compact rules UI, lobby designer access and numerical character tooltips. Remove its embedded Knight Manager component as requested. Evidence: [baseline](../evidence/workspace-baseline.json), [active keys](../define-comparison.md), [native contracts](../sources.md), and complete original files under `CustomDefines`.

## Work packages

| ID | Existing behavior and sources | Current contract | Planned action or gate |
|---|---|---|---|
| CD-COMBAT | `common/defines/serp_defines.txt:5–7`: casualty conversion 0.5 | Native NCombat key exists, 0.3; source comment says soft casualties become hard during main phase | Preserve 0.5 and the narrow override; test a controlled main-phase battle. No pursuit coefficient change or unrelated combat rebalance |
| CD-DYNASTY | Same file:19–21: cap 4, dynasty-vassal multipliers 0.25/0.1 | Native NDynasty keys exist; current values 2/0/0 | Preserve all three custom values; exercise landed and spouse contributions plus cap, including highest current title tier. Do not reactivate commented innovation-speed changes |
| CD-MAP | `defines/graphic/serp_graphic_defines.txt` and `defines/jomini/serp_jomini_defines.txt` | All 19 graphical keys match exact native namespaces; current ranges differ | Retain the documented custom ranges, event threshold 8, large-name step 12 and fog fade step 16. Test zoom endpoints and disabled event options; do not “correct” the native spelling `COMBAT_PREDICITON` |
| CD-RULES | `gui/11_game_rules.gui`: compact controls and Fog of War console button | Current native `gui/game_rules.gui` is 691 lines versus 206; different wrapper/nesting and newer controls | **Blocked GUI contract:** obtain UI dump and establish nested type/override precedence. Rebase the intended spacing/preset controls and fog button onto current relevant types, preserving native functionality. Never replace the new window with the old 206-line structure |
| CD-LOBBY | `gui/11_multiplayer_types.gui`: removes designer enabled guard so it can be requested after start | Current `JominiLobbyViewPreparation` at native line 1898 includes different character-type calls: noble family, adventurer, default | **Blocked GUI/engine contract:** determine whether the engine accepts post-start designing and whether all intended character types are valid. Preserve current flows and type arguments; button availability alone does not prove this capability |
| CD-TOOLTIPS | English/German `localization/*/gui/moretooltip_l_*.yml` | Overrides existing health descriptions and adds health/fertility/stress getters; needs current UI datatype/consumer check | Preserve EN/DE numerical information, existing native text/semantics where required and localization key identities. Verify exact getter types and rendering before implementation. Existing undefined-language fallback is not a new translation commitment |
| CD-KNIGHTS | Predicate, scripted GUI, full knights window, start hook, suppression event and seven localization files | All retained-package literal incoming references were searched; none outside CustomDefines found. Native window and predicate dependencies were read | Prepare removal of the 12 files below as a single package. No residual loaded marker should be advertised by CustomDefines. Validate that no retained feature still references the removed helpers/types/keys |

“19 graphical keys” includes NGui threshold, 16 NMapIcon ranges, NMapName and NFogOfWar. The exact values and source lines are enumerated in the comparison table. Engine combat/renown calculations are not reconstructed from guessed formulas.

## Exact GUI replacement targets

`11_game_rules.gui` declares `GameRuleTypes.hbox_ironman_achievements_info`; the same current native type begins at `gui/game_rules.gui:355`. This is a nested type replacement, not a same-path replacement of the whole 691-line file. Native preset controls now also have their own `vbox_game_rule_preset_options` type at line 438. Audit callers and restore the custom compact/fog behavior in that current structure without duplicating preset controls.

`11_multiplayer_types.gui` replaces `JominiMultiplayerLobby.JominiLobbyViewPreparation`; the native counterpart begins at `gui/multiplayer_types.gui:1898` and is consumed later in that file. Preserve all modern character-type branches and surrounding lobby types. The legacy filename-prefix precedence comment is still unverified for this build.

## Knight removal list

Source: [machine removal list](../evidence/knight-removal-candidates.json). Delete these files only in the later implementation, not during preparation:

1. `common/on_action/knight_manager_on_actions.txt`
2. `common/scripted_guis/knight_manager_gui.txt`
3. `common/scripted_triggers/knighthood_trigger.txt`
4. `events/knight_manager_events.txt`
5. `gui/window_knights.gui`
6. `localization/english/knight_manager_mod_l_english.yml`
7. `localization/french/knight_manager_mod_l_french.yml`
8. `localization/german/knight_manager_mod_l_german.yml`
9. `localization/korean/knight_manager_mod_l_korean.yml`
10. `localization/russian/knight_manager_mod_l_russian.yml`
11. `localization/simp_chinese/knight_manager_mod_l_simp_chinese.yml`
12. `localization/spanish/knight_manager_mod_l_spanish.yml`

This removes the subscriber `on_KnightManager_start`, the `KnightManager_is_loaded` global marker, related toggles/flags and `can_be_knight_trigger` replacement by removing their defining files. Keep all define files, `11_game_rules.gui`, `11_multiplayer_types.gui`, EN/DE `moretooltip` files, descriptor and unrelated assets. Do not remove native hooks or install replacement Knight Manager logic. Old-save migration is outside scope.

## New mechanics relevance

| Mechanic | Classification | Reason |
|---|---|---|
| Current native knight management | Relevant to removal | User explicitly excludes this feature from maintenance; no duplicate custom predicate/window should remain in CustomDefines |
| More title tiers, landed/landless and different lobby character types | Relevant | Dynasty formulas and current lobby UI expose these surfaces; preserve current native branches when rebasing |
| New game-rule/preset UI | Relevant | Old replacement has a materially smaller/different structure |
| Religion, conversion, artifacts and activity systems | Not relevant to the retained balance overrides | No new features added to those systems; UI combinations still need regression testing |
| Engine post-start ruler design and console fog capability | Unresolved | Old enabling behavior is a client UI request; current engine permission and MP behavior require dumps/tests |

## Acceptance tests

- Fresh start with CustomDefines only: no KnightManager marker, callback or custom window; native knight controls function. Repeat in two-player MP.
- Verify all 23 active keys load with no unknown namespace/key messages; unchanged custom values remain. Disabled innovation changes stay disabled.
- Test rules open/close, scrolling, preset save/load/delete and current native controls in EN/DE and at two UI scales. Fog changes must match intended client presentation; record any engine rejection.
- Host/client lobby: normal character, noble family and adventurer where available, preparation versus started game, designer cancel/confirm, ready/start and hotjoin. No broken lobby controls or MP desync.
- Tooltips show appropriate values for self and another character without missing datatype/loc errors. Check 8-option availability threshold with resource/war selector fixtures.

## Gates and dependencies

Read [debug run](../debug-run.md) for UI datatype export and [test protocol](../test-protocol.md). CD-RULES, CD-LOBBY and CD-TOOLTIPS remain blocked until their exact UI/engine contracts are established. Define retention and the removal list are plan ready, with runtime validation pending. A post-start designer restriction must be reported as a concrete engine limitation; do not substitute a gameplay effect that rewrites characters.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| CD-COMBAT | source/asset contract, not an engine-command signature | [Card](../contracts/CD-COMBAT.md) |
| CD-DYNASTY | source/asset contract, not an engine-command signature | [Card](../contracts/CD-DYNASTY.md) |
| CD-MAP | source/asset contract, not an engine-command signature | [Card](../contracts/CD-MAP.md) |
| CD-RULES | export declarations available | [Card](../contracts/CD-RULES.md) |
| CD-LOBBY | export declarations available | [Card](../contracts/CD-LOBBY.md) |
| CD-TOOLTIPS | export declarations available | [Card](../contracts/CD-TOOLTIPS.md) |
| CD-KNIGHTS | export declarations available | [Card](../contracts/CD-KNIGHTS.md) |
