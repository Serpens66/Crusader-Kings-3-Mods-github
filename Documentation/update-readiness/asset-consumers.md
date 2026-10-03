# Static texture consumer discovery

Search date: 2026-10-03. Every retained graphical texture was considered; native GUI, common definitions and graphics declarations were read. [Raw matches and scanned hashes](evidence/asset-consumers.json) separate exact paths from weaker symbolic matches.

| Package | Textures | Exact path match | Any discovered match |
|---|---:|---:|---:|
| Gender Colour | 5 | 2 | 2 |
| GFX-Mod | 8 | 5 | 5 |
| GFX-Mod Serp | 664 | 77 | 455 |

## Assets without a native same path

These are not automatically obsolete: listed candidates may be dynamically selected. Unmatched candidates require actual renderer/context evidence before deletion or remapping.

| Texture | First discovered candidate | Match level |
|---|---|---|
| `Gender Colour/gfx/interface/icons/character_status/sexuality_icons_female_alt.dds` | `No static/symbolic match found` | unresolved |
| `Gender Colour/gfx/interface/icons/character_status/sexuality_icons_male_grey.dds` | `No static/symbolic match found` | unresolved |
| `Gender Colour/gfx/interface/icons/character_status/sexuality_icons_male_wrongicon.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod/gfx/interface/icons/character_status/sexuality_icons_female_mies.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod/gfx/interface/icons/character_status/sexuality_icons_male_grey.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod/gfx/interface/icons/character_status/sexuality_icons_male_wrongicon.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/add_artifact_interaction.dds` | `common/character_interactions/00_debug_interactions.txt:1349` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/add_claim_on_artifact_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/add_house_claim_on_artifact_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/add_random_artifact_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/adroit_elevate_child_of_priestess_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/adroit_visit_priestess_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ai_only_liege_modify_vassal_contract_interaction.dds` | `common/character_interactions/00_modifiy_vassal_contract.txt:573` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ai_only_liege_modify_vassal_contract_interaction2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ai_only_vassal_modify_vassal_contract_interaction.dds` | `common/character_interactions/00_modifiy_vassal_contract.txt:734` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ai_only_vassal_modify_vassal_contract_interaction2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/arrange_marriage_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:12` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ask_for_conversion_courtier_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:158` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ask_for_conversion_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:2` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ask_for_pardon_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:2412` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/basic_duel_interaction_1.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/basic_duel_interaction_2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/basic_duel_interaction_3.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/become_blademaster_1.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/become_blademaster_2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/become_blademaster_3.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/befriend_interaction.dds` | `common/character_interactions/00_scheme_interactions.txt:612` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/blackmail_interaction.dds` | `common/character_interactions/00_blackmail_interactions.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/BoA_ransom_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/break_betrothal_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:1990` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/break_up_with_lover_interaction.dds` | `common/character_interactions/00_lover_interactions.txt:2` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/breaking_sword_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/bring_your_children_to_your_court_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/buy_artifact_claim.dds` | `common/character_interactions/00_artifact_interactions.txt:3645` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/buy_claim_interaction.dds` | `common/character_interactions/00_perk_interactions.txt:896` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/call_ally_interaction.dds` | `common/character_interactions/00_alliance.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/call_dynasty_member_to_war_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:1344` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/call_house_member_to_war_interaction.dds` | `common/character_interactions/00_house_head_interactions.txt:3` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_buy_slave_directly_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_buy_slave_on_market_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_demand_free_illegal_slaves_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_enslave_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_force_start_prostitution_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_force_stop_prostitution_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_free_slave_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_mass_enslave_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_rape_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_seize_slave_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_sell_slave_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/carn_sex_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cdol_alter_sexuality_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cdol_drain_life_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cdol_fascinate_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cdol_mesmerize_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cdol_torment_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/challenge_for_artifact_interaction.dds` | `common/character_interactions/00_artifact_interactions.txt:2042` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/challenge_to_single_combat_interaction.dds` | `common/character_interactions/00_perk_interactions.txt:1232` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/challenge_to_trial_by_combat_interaction.dds` | `common/character_interactions/01_fp1_interactions.txt:104` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/change_immortality_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cheat_mark_for_edit_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/cheat_remove_for_edit_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/chronicle_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/chronicle_interaction2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/claim_throne_interaction.dds` | `common/character_interactions/00_perk_interactions.txt:5` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/convert_to_religion_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:2036` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/convert_to_witchcraft_interaction.dds` | `common/character_interactions/00_witch_interactions.txt:2` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/court_interaction.dds` | `common/character_interactions/00_scheme_interactions.txt:1725` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/create_betrothal_interaction.dds` | `common/character_interactions/00_test_interactions.txt:1006` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/create_claimant_faction_against_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:1367` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_demand_sex_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_discipline_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_fire_court_slaver_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_force_start_pit_fighter_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_force_stop_pit_fighter_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_hire_court_slaver_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_slave_branding_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_slave_murder_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dag_cdo_slave_training_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/debug_start_great_holy_war_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/demand_artifact_interaction.dds` | `common/character_interactions/00_artifact_interactions.txt:1244` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/demand_conversion_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:508` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/demand_conversion_player_ruler_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:1385` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/demand_conversion_vassal_ruler_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:780` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/demand_payment_interaction.dds` | `common/character_interactions/00_perk_interactions.txt:707` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/denounce_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:914` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/designate_gruesome_festivals_sacrifice_interaction.dds` | `common/character_interactions/01_fp1_interactions.txt:7` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/designate_heir_interaction.dds` | `common/character_interactions/00_heir.txt:7` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/destroy_artifact_interaction.dds` | `common/character_interactions/00_artifact_interactions.txt:4385` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/diplomaticvisit_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/disinherit_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:3` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dismiss_concubine_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:3662` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/divorce_character_dynast_request_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:5452` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/divorce_character_dynast_request_rel_head_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:5687` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/divorce_character_house_head_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:3954` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/divorce_character_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:3763` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/divorce_character_rel_head_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:4385` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dl_disown_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dl_fadopt_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dl_heir_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dl_inclusion_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dl_madopt_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dna_transfer_interaction_counts_only.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dna_transfer_interaction_domestic.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dna_transfer_interaction_dukes_only.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dna_transfer_interaction_kings_and_emperors_only.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dragatus_prisoner_marriage_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dress_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dropclaimmod_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dub_knight_duke_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dub_knight_god_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dub_knight_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/duel_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dynast_claim_title_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:1674` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dynast_end_dynasty_wars_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:1805` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/dynast_legitimize_bastard_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:1866` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/educate_child_interaction.dds` | `common/character_interactions/00_education_interactions.txt:5` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/elite_education_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/elope_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:6723` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/end_war_attacker_defeat_interaction.dds` | `common/character_interactions/00_war.txt:1737` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/end_war_attacker_victory_interaction.dds` | `common/character_interactions/00_war.txt:268` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/end_war_attacker_white_peace_interaction.dds` | `common/character_interactions/00_war.txt:816` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/excommunicate_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:3163` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/execute_prisoner_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:6713` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/expose_secret_interaction.dds` | `common/character_interactions/00_character_interactions.txt:1675` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/find_concubine.dds` | `common/character_interactions/00_marriage_interactions.txt:2833` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/fire_court_physician_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/force_join_faction_interaction.dds` | `common/character_interactions/00_faction_interactions.txt:3` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/force_onto_council.dds` | `common/character_interactions/00_vassal_interactions.txt:1750` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/forgive_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:1207` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/full_body_hair_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/fund_inspiration_interaction.dds` | `common/character_interactions/02_ep1_interactions.txt:7` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/get_claim_interaction.dds` | `common/character_interactions/00_test_interactions.txt:660` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/gift_artifact_interaction.dds` | `common/character_interactions/00_artifact_interactions.txt:2` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/gift_artifacts_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/gift_interaction.dds` | `common/character_interactions/00_gift.txt:2` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/give_away_random_artifact_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/grant_immortality_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/grant_independence_interaction.dds` | `common/character_interactions/00_character_interactions.txt:1331` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/grant_NPM_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/grant_vassal_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:3` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/great_conquerors_set_gc.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/hakaretetme_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/hire_court_physician_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/hof_ask_for_claim_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:7154` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/hof_ask_for_gold_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:6791` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/hof_redirect_great_holy_war_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:8023` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/host_honored_guest_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:6535` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/immortality_disease_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/imprisionabso_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/imprison_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/indebt_guest_interaction.dds` | `common/character_interactions/02_ep1_interactions.txt:272` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/inspiration 2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/invite_agent_to_scheme_interaction.dds` | `common/character_interactions/00_invite_agent_to_scheme.txt:2` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/invite_to_council_position_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:1602` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/invite_to_court_interaction.dds` | `common/character_interactions/00_courtier_and_guest_interactions.txt:593` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/join_independence_faction_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:1293` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/join_war_interaction.dds` | `common/character_interactions/00_alliance.txt:2055` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/kick_from_court_interaction.dds` | `common/character_interactions/00_courtier_and_guest_interactions.txt:374` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/learn_language_interaction.dds` | `common/character_interactions/00_scheme_interactions.txt:2595` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/legitimize_bastard_interaction - Copy.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/liege_modify_vassal_contract_interaction.dds` | `common/character_interactions/00_modifiy_vassal_contract.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/liege_modify_vassal_contract_interaction2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/lift_excommunication_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:3423` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/literalist_debate_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:8437` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/make_child_learn_language_interaction.dds` | `common/character_interactions/00_education_interactions.txt:3736` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/make_concubine_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:2770` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/makeabso_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/marry_off_interaction.dds` | `common/character_interactions/00_marriage_interactions.txt:1262` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/military_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/money_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/move_to_dungeon_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:1683` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/move_to_house_arrest_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:1808` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/negotiate_alliance_interaction.dds` | `common/character_interactions/00_alliance.txt:1020` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/no_body_hair_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/nonagression_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/nude_inspect_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/nude_inspect_other_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/offer_concubine.dds` | `common/character_interactions/00_marriage_interactions.txt:2969` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/offer_guardianship_interaction.dds` | `common/character_interactions/00_education_interactions.txt:2200` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/offer_peace_interaction.dds` | `common/character_interactions/00_war.txt:2172` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/offer_vassalization_interaction.dds` | `common/character_interactions/00_character_interactions.txt:3` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/offer_ward_interaction.dds` | `common/character_interactions/00_education_interactions.txt:837` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/pardon_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:2667` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/pay_ransom_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:2562` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/physician_study_1.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/physician_study_2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/physician_study_3.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/propaganda_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/PT_negotiate_transfer.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/PT_pay_transfer_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/pull_out_interaction_1.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/pull_out_interaction_2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/pull_out_interaction_3.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/pull_out_interaction_4.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/quick_change_immortality_genetic_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/quick_change_immortality_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/quick_change_immortality_sterile_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/quick_grant_immortality_genetic_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/quick_grant_immortality_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/quick_grant_immortality_sterile_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ransom_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:1886` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ransom_me_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:3654` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/rcm_override_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/recruit_guest_interaction.dds` | `common/character_interactions/00_courtier_and_guest_interactions.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/release_from_prison_interaction.dds` | `common/character_interactions/00_prison_interactions.txt:4282` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/remove_designated_gruesome_festivals_sacrifice_interaction.dds` | `common/character_interactions/01_fp1_interactions.txt:64` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/remove_guardian_interaction.dds` | `common/character_interactions/00_education_interactions.txt:3425` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/remove_immortality_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/remove_NPM_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/rename_character.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/replace_target_unfit_priestess_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/request_conversion_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/request_excommunication_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:3642` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/restore_inheritance_interaction.dds` | `common/character_interactions/00_dynast_interactions.txt:776` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/restore_knighthood_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/retract_vassal_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:439` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/revoke_leased_title_interaction.dds` | `common/character_interactions/00_lease_interactions.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/revoke_title_interaction.dds` | `common/character_interactions/00_revoke_title_interaction.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/RICE_send_qinghaicong_horses.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/seduce_interaction.dds` | `common/character_interactions/00_scheme_interactions.txt:1063` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/seek_indulgences_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:2400` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/send_gift.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/send_to_holy_order_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:4286` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/set_primary_spouse_interaction.dds` | `common/character_interactions/00_character_interactions.txt:1162` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/spar_with_knight_interaction.dds` | `common/character_interactions/00_tradition_interactions.txt:1` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/start_abduct.dds` | `common/character_interactions/00_scheme_interactions.txt:251` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/start_independence_faction_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:1230` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/start_murder_interaction.dds` | `common/character_interactions/00_scheme_interactions.txt:3` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/start_stealing_back_artifact.dds` | `common/character_interactions/00_artifact_interactions.txt:2813` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/steal_all_artifacts.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/stealvassal_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/stop_attacker_vassal_war_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:2148` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/stop_defender_vassal_war_interaction.dds` | `common/character_interactions/00_vassal_interactions.txt:2288` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/stop_volunteering_as_whore_priestess_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_chastity_rules_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_clothing_rules_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_regain_submissive_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_remove_submissive_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_show_pose_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_train_obedience_accelerated_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sub_train_obedience_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sumptuary_law_debate_interaction.dds` | `common/character_interactions/00_court_amenities_interactions.txt:4` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sun_trial_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:8354` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/sway_interaction.dds` | `common/character_interactions/00_scheme_interactions.txt:2228` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/take_vows_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:5183` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/temporal_condemnation_interaction.dds` | `common/character_interactions/00_religious_interactions.txt:6345` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/trade_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/training_interaction_1.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_brutally_mauled.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_bubonic_plague.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_consumption.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_early_great_pox.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_gout_ridden.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_great_pox.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_ill.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_infirm.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_lovers_pox.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_pneumonic.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_severely_injured.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_sickly.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_smallpox.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_typhus.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_weak.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/ucp_interaction_cure_wounded.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/undress_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/uprisevassal_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_comfort_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_declare_friend_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_declare_rival_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_make_peace_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_renounce_claims_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_threaten_heretic_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/utd_tumble_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/vassal_modify_vassal_contract_interaction.dds` | `common/character_interactions/00_modifiy_vassal_contract.txt:314` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/vassal_modify_vassal_contract_interaction2.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/VIET_gift_baklava.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/VIET_gift_spices.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/view_war_interaction.dds` | `common/character_interactions/00_war.txt:2149` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/volunteer_other_as_whore_priestess_interaction.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/zzzzzz_lascalov_move_courtier.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_status/sexuality_icons_female_mies.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_status/sexuality_icons_male_grey.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/character_status/sexuality_icons_male_wrongicon.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/icon_skills_martial.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/traits/eunuch.dds` | `common/decisions/dlc_decisions/tgp/tgp_tribute_mission_decisions.txt:101` | basename |
| `GFX-Mod Serp/gfx/interface/icons/traits/henbane_addict.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/traits/opium_addled.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/traits/scholar.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/traits/sin_big.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/icons/traits/virtue_big.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/illustrations/men_at_arms_big/knights.dds` | `gfx/court_scene/character_roles/00_default_roles.txt:561` | matching_object_ids |
| `GFX-Mod Serp/gfx/interface/illustrations/men_at_arms_big/leives.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/illustrations/men_at_arms_small/leives.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_standard__.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_yellow.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/interface/window_character/character_view_prowess_bg.dds` | `No static/symbolic match found` | unresolved |
| `GFX-Mod Serp/gfx/map/terrain/flatmap.dds` | `gfx/map/flat_map_styles/flat_map_styles.txt:2` | basename |
