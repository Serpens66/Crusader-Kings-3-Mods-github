# Workspace mod inventory

Inventory includes variants and the `test` folder; names and descriptors do not prove runtime compatibility.

Native path collisions are definite whole-file overlap candidates; matching depth-zero keys are lexical object-overlap candidates.
Object merge rules must be checked for the relevant loader. A collision is not automatically a defect.

See [case studies](../workspace/case-studies.md) for interpretation and [local-index.json](local-index.json) for hashes.

## CustomDefines

Text/reference files indexed: 20. External descriptor: `CustomDefines.mod` (present).

- `version = "1.146"`
- `name = "CustomDefines"`
- `supported_version = "1.7.*"`
- `remote_file_id = "2636812977"`

Other files: 0. Extensions: 

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/defines/graphic/serp_graphic_defines.txt` | no | `NGui`, `NMapIcon`, `NMapName` |
| `common/defines/jomini/serp_jomini_defines.txt` | no | `NFogOfWar` |
| `common/defines/serp_defines.txt` | no | `NCombat`, `NDynasty` |
| `common/on_action/knight_manager_on_actions.txt` | no | `on_game_start` |
| `common/scripted_guis/knight_manager_gui.txt` | no |  |
| `common/scripted_triggers/knighthood_trigger.txt` | no | `can_be_knight_trigger` |
| `descriptor.mod` | no |  |
| `events/knight_manager_events.txt` | no |  |
| `gui/11_game_rules.gui` | no |  |
| `gui/11_multiplayer_types.gui` | no |  |
| `gui/window_knights.gui` | yes |  |
| `localization/english/gui/moretooltip_l_english.yml` | no |  |
| `localization/english/knight_manager_mod_l_english.yml` | no |  |
| `localization/french/knight_manager_mod_l_french.yml` | no |  |
| `localization/german/gui/moretooltip_l_german.yml` | no |  |
| `localization/german/knight_manager_mod_l_german.yml` | no |  |
| `localization/korean/knight_manager_mod_l_korean.yml` | no |  |
| `localization/russian/knight_manager_mod_l_russian.yml` | no |  |
| `localization/simp_chinese/knight_manager_mod_l_simp_chinese.yml` | no |  |
| `localization/spanish/knight_manager_mod_l_spanish.yml` | no |  |
## Gender Colour

Text/reference files indexed: 1. External descriptor: `Gender Colour.mod` (present).

- `version = "1.11"`
- `name = "Gender Colour"`
- `supported_version = "1.5.*"`
- `remote_file_id = "2602590291"`

Other files: 6. Extensions: `.dds`: 5, `.png`: 1

Asset same-path overlaps: `gfx/interface/icons/character_status/sexuality_icons_female.dds`, `gfx/interface/icons/character_status/sexuality_icons_male.dds`

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `descriptor.mod` | no |  |
## GFX-Mod

Text/reference files indexed: 2. External descriptor: `GFX-Mod.mod` (present).

- `version = "1.143"`
- `name = "GFX-Mod"`
- `supported_version = "1.7.*"`
- `remote_file_id = "2637472200"`

Other files: 9. Extensions: `.dds`: 8, `.png`: 1

Asset same-path overlaps: `gfx/interface/icons/artifact/artifact_bg.dds`, `gfx/interface/icons/artifact/artifact_unique.dds`, `gfx/interface/icons/character_status/sexuality_icons_female.dds`, `gfx/interface/icons/character_status/sexuality_icons_male.dds`, `gfx/portraits/portrait_rank.dds`

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `credits.txt` | yes |  |
| `descriptor.mod` | no |  |
## GFX-Mod Serp

Text/reference files indexed: 4. External descriptor: `GFX-Mod Serp.mod` (absent).

- `version = "1.143"`
- `name = "GFX-Mod"`
- `supported_version = "1.7.*"`
- `remote_file_id = "2637472200"`

Other files: 667. Extensions: `.dds`: 664, `.jpg`: 2, `.png`: 1

Asset same-path overlaps: `gfx/interface/icons/artifact/artifact_bg.dds`, `gfx/interface/icons/artifact/artifact_unique.dds`, `gfx/interface/icons/character_interactions/_missing_interaction.dds`, `gfx/interface/icons/character_interactions/artifact.dds`, `gfx/interface/icons/character_interactions/declare_war_interaction.dds`, `gfx/interface/icons/character_interactions/designate_shieldmaiden_interaction.dds`, `gfx/interface/icons/character_interactions/fabricate_hook_interaction.dds`, `gfx/interface/icons/character_interactions/grant_titles_interaction.dds`, `gfx/interface/icons/character_interactions/icon_combat.dds`, `gfx/interface/icons/character_interactions/icon_culture.dds`, `gfx/interface/icons/character_interactions/icon_dynasty.dds`, `gfx/interface/icons/character_interactions/icon_gold.dds`, `gfx/interface/icons/character_interactions/icon_hostile.dds`, `gfx/interface/icons/character_interactions/icon_marriage.dds`, `gfx/interface/icons/character_interactions/icon_personal.dds`, `gfx/interface/icons/character_interactions/inspiration.dds`, `gfx/interface/icons/character_interactions/prison.dds`, `gfx/interface/icons/character_interactions/send_poem_interaction.dds`, `gfx/interface/icons/character_interactions/send_to_varangian_guard_interaction.dds`, `gfx/interface/icons/character_interactions/torture_interaction.dds`, `gfx/interface/icons/character_interactions/vassal_claim_liege_title_interaction.dds`, `gfx/interface/icons/character_status/sexuality_icons_female.dds`, `gfx/interface/icons/character_status/sexuality_icons_male.dds`, `gfx/interface/icons/icon_prowess.dds`, `gfx/interface/icons/icon_skills.dds`, `gfx/interface/icons/traits/_frame_commander.dds`, `gfx/interface/icons/traits/_frame_education.dds`, `gfx/interface/icons/traits/_frame_fame_bad.dds`, `gfx/interface/icons/traits/_frame_fame_good.dds`, `gfx/interface/icons/traits/_frame_fame_neutral.dds`, `gfx/interface/icons/traits/_frame_health.dds`, `gfx/interface/icons/traits/_frame_physical_bad.dds`, `gfx/interface/icons/traits/_frame_physical_good.dds`, `gfx/interface/icons/traits/_frame_physical_neutral.dds`, `gfx/interface/icons/traits/_frame_pregnant.dds`, `gfx/interface/icons/traits/_stars_1.dds`, `gfx/interface/icons/traits/_stars_2.dds`, `gfx/interface/icons/traits/_stars_3.dds`, `gfx/interface/icons/traits/_stars_4.dds`, `gfx/interface/icons/traits/administrative_court_1.dds`, `gfx/interface/icons/traits/administrative_court_2.dds`, `gfx/interface/icons/traits/administrator.dds`, `gfx/interface/icons/traits/adulterer.dds`, `gfx/interface/icons/traits/adventurer.dds`, `gfx/interface/icons/traits/aggressive_attacker.dds`, `gfx/interface/icons/traits/albino.dds`, `gfx/interface/icons/traits/ambitious.dds`, `gfx/interface/icons/traits/arbitrary.dds`, `gfx/interface/icons/traits/architect.dds`, `gfx/interface/icons/traits/arrogant.dds`, `gfx/interface/icons/traits/athletic.dds`, `gfx/interface/icons/traits/august.dds`, `gfx/interface/icons/traits/augustus.dds`, `gfx/interface/icons/traits/avaricious.dds`, `gfx/interface/icons/traits/bastard.dds`, `gfx/interface/icons/traits/bastard_founder.dds`, `gfx/interface/icons/traits/beauty_bad_1.dds`, `gfx/interface/icons/traits/beauty_bad_2.dds`, `gfx/interface/icons/traits/beauty_bad_3.dds`, `gfx/interface/icons/traits/beauty_good_1.dds`, `gfx/interface/icons/traits/beauty_good_2.dds`, `gfx/interface/icons/traits/beauty_good_3.dds`, `gfx/interface/icons/traits/berserker.dds`, `gfx/interface/icons/traits/blademaster.dds`, `gfx/interface/icons/traits/blademaster_1.dds`, `gfx/interface/icons/traits/blademaster_2.dds`, `gfx/interface/icons/traits/blademaster_3.dds`, `gfx/interface/icons/traits/bleeder.dds`, `gfx/interface/icons/traits/blind.dds`, `gfx/interface/icons/traits/blood_of_prophet.dds`, `gfx/interface/icons/traits/blood_of_the_prophet_parent.dds`, `gfx/interface/icons/traits/born_in_the_purple.dds`, `gfx/interface/icons/traits/bossy.dds`, `gfx/interface/icons/traits/brave.dds`, `gfx/interface/icons/traits/bubonic_plague.dds`, `gfx/interface/icons/traits/callous.dds`, `gfx/interface/icons/traits/calm.dds`, `gfx/interface/icons/traits/cancer.dds`, `gfx/interface/icons/traits/cannibal.dds`, `gfx/interface/icons/traits/cautious_leader.dds`, `gfx/interface/icons/traits/celibate.dds`, `gfx/interface/icons/traits/chakravarti.dds`, `gfx/interface/icons/traits/charming.dds`, `gfx/interface/icons/traits/chaste.dds`, `gfx/interface/icons/traits/cheese.dds`, `gfx/interface/icons/traits/child_of_concubine.dds`, `gfx/interface/icons/traits/clubfooted.dds`, `gfx/interface/icons/traits/comfort_eater.dds`, `gfx/interface/icons/traits/compassionate.dds`, `gfx/interface/icons/traits/confider.dds`, `gfx/interface/icons/traits/congenital.dds`, `gfx/interface/icons/traits/consecrated_blood.dds`, `gfx/interface/icons/traits/consumption.dds`, `gfx/interface/icons/traits/content.dds`, `gfx/interface/icons/traits/contrite.dds`, `gfx/interface/icons/traits/craven.dds`, `gfx/interface/icons/traits/crusader.dds`, `gfx/interface/icons/traits/crusader_king.dds`, `gfx/interface/icons/traits/curious.dds`, `gfx/interface/icons/traits/cynical.dds`, `gfx/interface/icons/traits/deceitful.dds`, `gfx/interface/icons/traits/denounced.dds`, `gfx/interface/icons/traits/depressed_1.dds`, `gfx/interface/icons/traits/depressed_genetic.dds`, `gfx/interface/icons/traits/desert_warrior.dds`, `gfx/interface/icons/traits/deviant.dds`, `gfx/interface/icons/traits/devoted.dds`, `gfx/interface/icons/traits/diligent.dds`, `gfx/interface/icons/traits/diplomat.dds`, `gfx/interface/icons/traits/diplomatic_court_1.dds`, `gfx/interface/icons/traits/diplomatic_court_2.dds`, `gfx/interface/icons/traits/disfigured.dds`, `gfx/interface/icons/traits/disinherited.dds`, `gfx/interface/icons/traits/disputed_heritage.dds`, `gfx/interface/icons/traits/divine_blood.dds`, `gfx/interface/icons/traits/drunkard.dds`, `gfx/interface/icons/traits/dull.dds`, `gfx/interface/icons/traits/dwarf.dds`, `gfx/interface/icons/traits/early_great_pox.dds`, `gfx/interface/icons/traits/education_diplomacy.dds`, `gfx/interface/icons/traits/education_diplomacy_1.dds`, `gfx/interface/icons/traits/education_diplomacy_2.dds`, `gfx/interface/icons/traits/education_diplomacy_3.dds`, `gfx/interface/icons/traits/education_diplomacy_4.dds`, `gfx/interface/icons/traits/education_intrigue_1.dds`, `gfx/interface/icons/traits/education_intrigue_2.dds`, `gfx/interface/icons/traits/education_intrigue_3.dds`, `gfx/interface/icons/traits/education_intrigue_4.dds`, `gfx/interface/icons/traits/education_learning_1.dds`, `gfx/interface/icons/traits/education_learning_2.dds`, `gfx/interface/icons/traits/education_learning_3.dds`, `gfx/interface/icons/traits/education_learning_4.dds`, `gfx/interface/icons/traits/education_martial_1.dds`, `gfx/interface/icons/traits/education_martial_2.dds`, `gfx/interface/icons/traits/education_martial_3.dds`, `gfx/interface/icons/traits/education_martial_4.dds`, `gfx/interface/icons/traits/education_martial_prowess_1.dds`, `gfx/interface/icons/traits/education_martial_prowess_2.dds`, `gfx/interface/icons/traits/education_martial_prowess_3.dds`, `gfx/interface/icons/traits/education_martial_prowess_4.dds`, `gfx/interface/icons/traits/education_stewardship_1.dds`, `gfx/interface/icons/traits/education_stewardship_2.dds`, `gfx/interface/icons/traits/education_stewardship_3.dds`, `gfx/interface/icons/traits/education_stewardship_4.dds`, `gfx/interface/icons/traits/excommunicated.dds`, `gfx/interface/icons/traits/faith_warrior.dds`, `gfx/interface/icons/traits/family_first.dds`, `gfx/interface/icons/traits/fecund.dds`, `gfx/interface/icons/traits/fickle.dds`, `gfx/interface/icons/traits/flagellant.dds`, `gfx/interface/icons/traits/flexible_leader.dds`, `gfx/interface/icons/traits/forder.dds`, `gfx/interface/icons/traits/forest_fighter.dds`, `gfx/interface/icons/traits/forgiving.dds`, `gfx/interface/icons/traits/fornicator.dds`, `gfx/interface/icons/traits/gallant.dds`, `gfx/interface/icons/traits/generous.dds`, `gfx/interface/icons/traits/giant.dds`, `gfx/interface/icons/traits/gluttonous.dds`, `gfx/interface/icons/traits/gout_ridden.dds`, `gfx/interface/icons/traits/great_pox.dds`, `gfx/interface/icons/traits/greatest_of_khans.dds`, `gfx/interface/icons/traits/greedy.dds`, `gfx/interface/icons/traits/gregarious.dds`, `gfx/interface/icons/traits/hajjaj.dds`, `gfx/interface/icons/traits/hashishiyah.dds`, `gfx/interface/icons/traits/herbalist_1.dds`, `gfx/interface/icons/traits/herbalist_2.dds`, `gfx/interface/icons/traits/herbalist_3.dds`, `gfx/interface/icons/traits/heresiarch.dds`, `gfx/interface/icons/traits/holy_warrior.dds`, `gfx/interface/icons/traits/honest.dds`, `gfx/interface/icons/traits/humble.dds`, `gfx/interface/icons/traits/hunchbacked.dds`, `gfx/interface/icons/traits/hunter.dds`, `gfx/interface/icons/traits/hunter_1.dds`, `gfx/interface/icons/traits/hunter_2.dds`, `gfx/interface/icons/traits/hunter_3.dds`, `gfx/interface/icons/traits/ill.dds`, `gfx/interface/icons/traits/impatient.dds`, `gfx/interface/icons/traits/impotent.dds`, `gfx/interface/icons/traits/improvident.dds`, `gfx/interface/icons/traits/inappetetic.dds`, `gfx/interface/icons/traits/inbred.dds`, `gfx/interface/icons/traits/incapable.dds`, `gfx/interface/icons/traits/incestuous.dds`, `gfx/interface/icons/traits/infertile.dds`, `gfx/interface/icons/traits/infirm.dds`, `gfx/interface/icons/traits/intellect_bad_1.dds`, `gfx/interface/icons/traits/intellect_bad_2.dds`, `gfx/interface/icons/traits/intellect_bad_3.dds`, `gfx/interface/icons/traits/intellect_good_1.dds`, `gfx/interface/icons/traits/intellect_good_2.dds`, `gfx/interface/icons/traits/intellect_good_3.dds`, `gfx/interface/icons/traits/intrigue_court_1.dds`, `gfx/interface/icons/traits/intrigue_court_2.dds`, `gfx/interface/icons/traits/irritable.dds`, `gfx/interface/icons/traits/journaller.dds`, `gfx/interface/icons/traits/jungle_stalker.dds`, `gfx/interface/icons/traits/just.dds`, `gfx/interface/icons/traits/kinslayer_1.dds`, `gfx/interface/icons/traits/kinslayer_2.dds`, `gfx/interface/icons/traits/kinslayer_3.dds`, `gfx/interface/icons/traits/lazy.dds`, `gfx/interface/icons/traits/legitimized_bastard.dds`, `gfx/interface/icons/traits/leper.dds`, `gfx/interface/icons/traits/lifestyle_herbalist.dds`, `gfx/interface/icons/traits/lisping.dds`, `gfx/interface/icons/traits/logistician.dds`, `gfx/interface/icons/traits/lovers_pox.dds`, `gfx/interface/icons/traits/lunatic_1.dds`, `gfx/interface/icons/traits/lunatic_genetic.dds`, `gfx/interface/icons/traits/lustful.dds`, `gfx/interface/icons/traits/maimed.dds`, `gfx/interface/icons/traits/military_engineer.dds`, `gfx/interface/icons/traits/mirza.dds`, `gfx/interface/icons/traits/mujahid.dds`, `gfx/interface/icons/traits/murderer.dds`, `gfx/interface/icons/traits/mystic.dds`, `gfx/interface/icons/traits/mystic_1.dds`, `gfx/interface/icons/traits/mystic_2.dds`, `gfx/interface/icons/traits/mystic_3.dds`, `gfx/interface/icons/traits/one_eyed.dds`, `gfx/interface/icons/traits/one_legged.dds`, `gfx/interface/icons/traits/open_terrain_expert.dds`, `gfx/interface/icons/traits/order_member.dds`, `gfx/interface/icons/traits/organizer.dds`, `gfx/interface/icons/traits/overseer.dds`, `gfx/interface/icons/traits/paragon.dds`, `gfx/interface/icons/traits/paranoid.dds`, `gfx/interface/icons/traits/patient.dds`, `gfx/interface/icons/traits/peasant_leader.dds`, `gfx/interface/icons/traits/pensive.dds`, `gfx/interface/icons/traits/physician.dds`, `gfx/interface/icons/traits/physician_1.dds`, `gfx/interface/icons/traits/physician_2.dds`, `gfx/interface/icons/traits/physician_3.dds`, `gfx/interface/icons/traits/physique_bad_1.dds`, `gfx/interface/icons/traits/physique_bad_2.dds`, `gfx/interface/icons/traits/physique_bad_3.dds`, `gfx/interface/icons/traits/physique_good_1.dds`, `gfx/interface/icons/traits/physique_good_2.dds`, `gfx/interface/icons/traits/physique_good_3.dds`, `gfx/interface/icons/traits/pilgrim.dds`, `gfx/interface/icons/traits/pilgrim_1.dds`, `gfx/interface/icons/traits/pilgrim_2.dds`, `gfx/interface/icons/traits/pilgrim_3.dds`, `gfx/interface/icons/traits/pneumonic.dds`, `gfx/interface/icons/traits/poet.dds`, `gfx/interface/icons/traits/possessed_1.dds`, `gfx/interface/icons/traits/possessed_genetic.dds`, `gfx/interface/icons/traits/pregnant.dds`, `gfx/interface/icons/traits/profligate.dds`, `gfx/interface/icons/traits/pure_blooded.dds`, `gfx/interface/icons/traits/rakish.dds`, `gfx/interface/icons/traits/reaver.dds`, `gfx/interface/icons/traits/reckless.dds`, `gfx/interface/icons/traits/reclusive.dds`, `gfx/interface/icons/traits/reincarnation.dds`, `gfx/interface/icons/traits/reveler.dds`, `gfx/interface/icons/traits/reveler_1.dds`, `gfx/interface/icons/traits/reveler_2.dds`, `gfx/interface/icons/traits/reveler_3.dds`, `gfx/interface/icons/traits/rough_terrain_expert.dds`, `gfx/interface/icons/traits/rowdy.dds`, `gfx/interface/icons/traits/sadistic.dds`, `gfx/interface/icons/traits/saint.dds`, `gfx/interface/icons/traits/saoshyant.dds`, `gfx/interface/icons/traits/saoshyant_descendant.dds`, `gfx/interface/icons/traits/savior.dds`, `gfx/interface/icons/traits/sayyid.dds`, `gfx/interface/icons/traits/scaly.dds`, `gfx/interface/icons/traits/scarred.dds`, `gfx/interface/icons/traits/schemer.dds`, `gfx/interface/icons/traits/scholarly_court_1.dds`, `gfx/interface/icons/traits/scholarly_court_2.dds`, `gfx/interface/icons/traits/sea_raider.dds`, `gfx/interface/icons/traits/seducer.dds`, `gfx/interface/icons/traits/shieldmaiden.dds`, `gfx/interface/icons/traits/shrewd.dds`, `gfx/interface/icons/traits/shy.dds`, `gfx/interface/icons/traits/sickly.dds`, `gfx/interface/icons/traits/sin.dds`, `gfx/interface/icons/traits/sly.dds`, `gfx/interface/icons/traits/smallpox.dds`, `gfx/interface/icons/traits/sodomite.dds`, `gfx/interface/icons/traits/spindly.dds`, `gfx/interface/icons/traits/strategist.dds`, `gfx/interface/icons/traits/strong.dds`, `gfx/interface/icons/traits/stubborn.dds`, `gfx/interface/icons/traits/stuttering.dds`, `gfx/interface/icons/traits/talkative.dds`, `gfx/interface/icons/traits/temperate.dds`, `gfx/interface/icons/traits/theologian.dds`, `gfx/interface/icons/traits/torturer.dds`, `gfx/interface/icons/traits/trusting.dds`, `gfx/interface/icons/traits/twin.dds`, `gfx/interface/icons/traits/typhus.dds`, `gfx/interface/icons/traits/unyielding_defender.dds`, `gfx/interface/icons/traits/varangian.dds`, `gfx/interface/icons/traits/vengeful.dds`, `gfx/interface/icons/traits/viking.dds`, `gfx/interface/icons/traits/virtue.dds`, `gfx/interface/icons/traits/warlike_court_1.dds`, `gfx/interface/icons/traits/warlike_court_2.dds`, `gfx/interface/icons/traits/weak.dds`, `gfx/interface/icons/traits/wheezing.dds`, `gfx/interface/icons/traits/whole_of_body.dds`, `gfx/interface/icons/traits/wild_oat.dds`, `gfx/interface/icons/traits/winter_soldier.dds`, `gfx/interface/icons/traits/witch.dds`, `gfx/interface/icons/traits/wounded_1.dds`, `gfx/interface/icons/traits/wounded_2.dds`, `gfx/interface/icons/traits/wounded_3.dds`, `gfx/interface/icons/traits/wrathful.dds`, `gfx/interface/icons/traits/zealous.dds`, `gfx/interface/illustrations/men_at_arms_big/archers.dds`, `gfx/interface/illustrations/men_at_arms_big/bombard.dds`, `gfx/interface/illustrations/men_at_arms_big/bondi.dds`, `gfx/interface/illustrations/men_at_arms_big/bowmen.dds`, `gfx/interface/illustrations/men_at_arms_big/camel_riders.dds`, `gfx/interface/illustrations/men_at_arms_big/crossbowmen.dds`, `gfx/interface/illustrations/men_at_arms_big/danish_huskarls.dds`, `gfx/interface/illustrations/men_at_arms_big/heavy_cavalry.dds`, `gfx/interface/illustrations/men_at_arms_big/heavy_infantry.dds`, `gfx/interface/illustrations/men_at_arms_big/horse_archers.dds`, `gfx/interface/illustrations/men_at_arms_big/house_guard.dds`, `gfx/interface/illustrations/men_at_arms_big/jomsviking_pirates.dds`, `gfx/interface/illustrations/men_at_arms_big/levies.dds`, `gfx/interface/illustrations/men_at_arms_big/light_cavalry.dds`, `gfx/interface/illustrations/men_at_arms_big/mangonel.dds`, `gfx/interface/illustrations/men_at_arms_big/onager.dds`, `gfx/interface/illustrations/men_at_arms_big/pikemen.dds`, `gfx/interface/illustrations/men_at_arms_big/skirmishers.dds`, `gfx/interface/illustrations/men_at_arms_big/trebuchet.dds`, `gfx/interface/illustrations/men_at_arms_big/varangian_veterans.dds`, `gfx/interface/illustrations/men_at_arms_big/vigmen.dds`, `gfx/interface/illustrations/men_at_arms_big/war_elephants.dds`, `gfx/interface/illustrations/men_at_arms_small/archers.dds`, `gfx/interface/illustrations/men_at_arms_small/bombard.dds`, `gfx/interface/illustrations/men_at_arms_small/bondi.dds`, `gfx/interface/illustrations/men_at_arms_small/bowmen.dds`, `gfx/interface/illustrations/men_at_arms_small/camel_riders.dds`, `gfx/interface/illustrations/men_at_arms_small/crossbowmen.dds`, `gfx/interface/illustrations/men_at_arms_small/danish_huskarls.dds`, `gfx/interface/illustrations/men_at_arms_small/heavy_cavalry.dds`, `gfx/interface/illustrations/men_at_arms_small/heavy_infantry.dds`, `gfx/interface/illustrations/men_at_arms_small/horse_archers.dds`, `gfx/interface/illustrations/men_at_arms_small/house_guard.dds`, `gfx/interface/illustrations/men_at_arms_small/jomsviking_pirates.dds`, `gfx/interface/illustrations/men_at_arms_small/knights.dds`, `gfx/interface/illustrations/men_at_arms_small/levies.dds`, `gfx/interface/illustrations/men_at_arms_small/light_cavalry.dds`, `gfx/interface/illustrations/men_at_arms_small/mangonel.dds`, `gfx/interface/illustrations/men_at_arms_small/onager.dds`, `gfx/interface/illustrations/men_at_arms_small/pikemen.dds`, `gfx/interface/illustrations/men_at_arms_small/skirmishers.dds`, `gfx/interface/illustrations/men_at_arms_small/trebuchet.dds`, `gfx/interface/illustrations/men_at_arms_small/varangian_veterans.dds`, `gfx/interface/illustrations/men_at_arms_small/vigmen.dds`, `gfx/interface/illustrations/men_at_arms_small/war_elephants.dds`, `gfx/interface/progressbars/progress_blue.dds`, `gfx/interface/progressbars/progress_frozen.dds`, `gfx/interface/progressbars/progress_gray.dds`, `gfx/interface/progressbars/progress_green.dds`, `gfx/interface/progressbars/progress_purple.dds`, `gfx/interface/progressbars/progress_red.dds`, `gfx/interface/progressbars/progress_scheme.dds`, `gfx/interface/progressbars/progress_standard.dds`, `gfx/interface/skinned/illustrations/men_at_arms/knights.dds`, `gfx/interface/window_character/character_view_skills_bg.dds`, `gfx/interface/window_character/characterlist_skills_bg.dds`, `gfx/portraits/portrait_rank.dds`

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `credits.txt` | yes |  |
| `descriptor.mod` | no |  |
| `gfx/map/post_effects/posteffect_volumes.txt` | yes |  |
| `info.txt` | no |  |
## Knight Manager (MP)

Text/reference files indexed: 14. External descriptor: `Knight Manager (MP).mod` (present).

- `version = "1.149"`
- `name = "Knight Manager (MP)"`
- `supported_version = "1.9.*"`
- `remote_file_id = "2645646874"`

Other files: 1. Extensions: `.png`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/on_action/knight_manager_on_actions.txt` | no | `on_game_start` |
| `common/scripted_guis/knight_manager_gui.txt` | no |  |
| `common/scripted_triggers/knighthood_trigger.txt` | no | `can_be_knight_trigger` |
| `descriptor.mod` | no |  |
| `events/knight_manager_events.txt` | no |  |
| `gui/window_knights.gui` | yes |  |
| `localization/english/knight_manager_mod_l_english.yml` | no |  |
| `localization/french/knight_manager_mod_l_french.yml` | no |  |
| `localization/german/knight_manager_mod_l_german.yml` | no |  |
| `localization/korean/knight_manager_mod_l_korean.yml` | no |  |
| `localization/polish/knight_manager_mod_l_polish.yml` | no |  |
| `localization/russian/knight_manager_mod_l_russian.yml` | no |  |
| `localization/simp_chinese/knight_manager_mod_l_simp_chinese.yml` | no |  |
| `localization/spanish/knight_manager_mod_l_spanish.yml` | no |  |
## Knight Manager Continued (MP)

Text/reference files indexed: 3. External descriptor: `Knight Manager Continued (MP).mod` (present).

- `version = "1.012"`
- `name = "Knight Manager Continued (MP)"`
- `supported_version = "1.12.*"`
- `remote_file_id = "3084278890"`

Other files: 2. Extensions: `.lnk`: 1, `.png`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/scripted_guis/kmc_gui.txt` | no |  |
| `common/scripted_triggers/kmc_trigger.txt` | no | `can_be_knight_trigger` |
| `descriptor.mod` | no |  |
## Leave Wars

Text/reference files indexed: 15. External descriptor: `Leave Wars.mod` (present).

- `version = "1.121"`
- `name = "Leave Wars"`
- `supported_version = "1.6.*"`
- `remote_file_id = "2643946956"`

Other files: 1. Extensions: `.png`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/character_interactions/leave_war_mod_interaction.txt` | no |  |
| `common/effect_localization/leave_war_mod_effect_loc.txt` | no |  |
| `common/game_rules/leave_war_mod_rules.txt` | no |  |
| `common/messages/leave_war_mod_messages.txt` | no |  |
| `common/opinion_modifiers/leave_war_mod_opinions.txt` | no |  |
| `common/script_values/leave_war_mod_cost_values.txt` | no |  |
| `descriptor.mod` | no |  |
| `events/leave_war_mod_events.txt` | no |  |
| `localization/english/leave_war_mod_l_english.yml` | no |  |
| `localization/french/leave_war_mod_l_french.yml` | no |  |
| `localization/german/leave_war_mod_l_german.yml` | no |  |
| `localization/korean/leave_war_mod_l_korean.yml` | no |  |
| `localization/russian/leave_war_mod_l_russian.yml` | no |  |
| `localization/simp_chinese/leave_war_mod_l_simp_chinese.yml` | no |  |
| `localization/spanish/leave_war_mod_l_spanish.yml` | no |  |
## Mass Demand Conversion

Text/reference files indexed: 12. External descriptor: `Mass Demand Conversion.mod` (present).

- `version = "1.077"`
- `name = "Mass Demand Conversion"`
- `supported_version = "1.19.*"`
- `remote_file_id = "2753176859"`

Other files: 1. Extensions: `.png`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/decisions/mod_mass_convert_subjects.txt` | no |  |
| `common/script_values/mod_mass_convert_subjects_values.txt` | no |  |
| `descriptor.mod` | no |  |
| `events/religion_events/accept_conversion_notification.txt` | no |  |
| `localization/english/mod_mass_convert_subjects_l_english.yml` | no |  |
| `localization/french/mod_mass_convert_subjects_l_french.yml` | no |  |
| `localization/german/mod_mass_convert_subjects_l_german.yml` | no |  |
| `localization/korean/mod_mass_convert_subjects_l_korean.yml` | no |  |
| `localization/polish/mod_mass_convert_subjects_l_polish.yml` | no |  |
| `localization/russian/mod_mass_convert_subjects_l_russian.yml` | no |  |
| `localization/simp_chinese/mod_mass_convert_subjects_l_simp_chinese.yml` | no |  |
| `localization/spanish/mod_mass_convert_subjects_l_spanish.yml` | no |  |
## SerpAlerts

Text/reference files indexed: 12. External descriptor: `SerpAlerts.mod` (present).

- `version = "1.18"`
- `name = "SerpAlerts"`
- `supported_version = "1.5.*"`
- `remote_file_id = "2637852159"`

Other files: 1. Extensions: `.dds`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/important_actions/serp_alerts_actions.txt` | no |  |
| `common/messages/serp_alerts_mod_messages.txt` | no |  |
| `common/on_action/serp_on_actions_alerts_mod.txt` | no | `on_death`, `on_join_war_as_secondary`, `on_leave_court`, `on_war_started` |
| `descriptor.mod` | no |  |
| `events/serp_alerts_events.txt` | no |  |
| `localization/english/serp_alerts_messages_mod_l_english.yml` | no |  |
| `localization/french/serp_alerts_messages_mod_l_french.yml` | no |  |
| `localization/german/serp_alerts_messages_mod_l_german.yml` | no |  |
| `localization/korean/serp_alerts_messages_mod_l_korean.yml` | no |  |
| `localization/russian/serp_alerts_messages_mod_l_russian.yml` | no |  |
| `localization/simp_chinese/serp_alerts_messages_mod_l_simp_chinese.yml` | no |  |
| `localization/spanish/serp_alerts_messages_mod_l_spanish.yml` | no |  |
## SerpInteractionsDecisions

**Historical inventory below:** 24 listed files were removed on 2026-10-03. The current package retains 27 text/reference files and its thumbnail. See [separation record](../update-readiness/mods/serp-interactions-decisions.md#bundle-separation--2026-10-03).

Text/reference files indexed: 51. External descriptor: `SerpInteractionsDecisions.mod` (present).

- `version = "1.26"`
- `name = "SerpInteractionsDecisions"`
- `supported_version = "1.5.*"`
- `remote_file_id = "2638425673"`

Other files: 1. Extensions: `.png`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/character_interactions/additional_education_interactions.txt` | no |  |
| `common/character_interactions/leave_war_mod_interaction.txt` | no |  |
| `common/character_interactions/pardon_hooks_interactions.txt` | no |  |
| `common/character_interactions/send_mpmoney_interactions.txt` | no |  |
| `common/character_interactions/temp_excommunication_interactions.txt` | no |  |
| `common/decisions/ABD_decision.txt` | no |  |
| `common/decisions/convert_resources_decision.txt` | no |  |
| `common/decisions/mod_mass_convert_subjects.txt` | no |  |
| `common/effect_localization/leave_war_mod_effect_loc.txt` | no |  |
| `common/game_rules/leave_war_mod_rules.txt` | no |  |
| `common/messages/leave_war_mod_messages.txt` | no |  |
| `common/modifiers/additional_education_modifiers.txt` | no |  |
| `common/modifiers/convert_resources_modifiers.txt` | no |  |
| `common/opinion_modifiers/additional_education_opinions.txt` | no |  |
| `common/opinion_modifiers/leave_war_mod_opinions.txt` | no |  |
| `common/opinion_modifiers/pardon_hooks_opinions.txt` | no |  |
| `common/script_values/additional_education_cost_values.txt` | no |  |
| `common/script_values/leave_war_mod_cost_values.txt` | no |  |
| `common/script_values/mod_mass_convert_subjects_values.txt` | no |  |
| `common/script_values/temp_excommunication_interactions_cost_values.txt` | no |  |
| `descriptor.mod` | no |  |
| `events/additional_education_events.txt` | no |  |
| `events/convert_resources_events.txt` | no |  |
| `events/leave_war_mod_events.txt` | no |  |
| `events/religion_events/accept_conversion_notification.txt` | no |  |
| `localization/english/ABD_l_english.yml` | no |  |
| `localization/english/additional_education_l_english.yml` | no |  |
| `localization/english/convert_resources_l_english.yml` | no |  |
| `localization/english/leave_war_mod_l_english.yml` | no |  |
| `localization/english/mod_mass_convert_subjects_l_english.yml` | no |  |
| `localization/english/pardonhooks_l_english.yml` | no |  |
| `localization/english/send_mpmoney_l_english.yml` | no |  |
| `localization/english/temp_excom_interactions_l_english.yml` | no |  |
| `localization/french/leave_war_mod_l_french.yml` | no |  |
| `localization/french/mod_mass_convert_subjects_l_french.yml` | no |  |
| `localization/german/ABD_l_german.yml` | no |  |
| `localization/german/additional_education_l_german.yml` | no |  |
| `localization/german/convert_resources_l_german.yml` | no |  |
| `localization/german/leave_war_mod_l_german.yml` | no |  |
| `localization/german/mod_mass_convert_subjects_l_german.yml` | no |  |
| `localization/german/pardonhooks_l_german.yml` | no |  |
| `localization/german/send_mpmoney_l_german.yml` | no |  |
| `localization/german/temp_excom_interactions_l_german.yml` | no |  |
| `localization/korean/leave_war_mod_l_korean.yml` | no |  |
| `localization/korean/mod_mass_convert_subjects_l_korean.yml` | no |  |
| `localization/russian/leave_war_mod_l_russian.yml` | no |  |
| `localization/russian/mod_mass_convert_subjects_l_russian.yml` | no |  |
| `localization/simp_chinese/leave_war_mod_l_simp_chinese.yml` | no |  |
| `localization/simp_chinese/mod_mass_convert_subjects_l_simp_chinese.yml` | no |  |
| `localization/spanish/leave_war_mod_l_spanish.yml` | no |  |
| `localization/spanish/mod_mass_convert_subjects_l_spanish.yml` | no |  |
## test

Text/reference files indexed: 13. External descriptor: `test.mod` (present).

- `version = "2"`
- `name = "test"`
- `supported_version = "1.5.*"`

Other files: 1. Extensions: `.png`: 1

| File | Native same path | Matching native top-level keys |
|---|---|---|
| `common/on_action/knight_manager_on_actions.txt` | no | `on_game_start` |
| `common/scripted_guis/knight_manager_gui.txt` | no |  |
| `common/scripted_triggers/knighthood_trigger.txt` | no | `can_be_knight_trigger` |
| `descriptor.mod` | no |  |
| `events/knight_manager_events.txt` | no |  |
| `gui/window_knights.gui` | yes |  |
| `localization/english/knight_manager_mod_l_english.yml` | no |  |
| `localization/french/knight_manager_mod_l_french.yml` | no |  |
| `localization/german/knight_manager_mod_l_german.yml` | no |  |
| `localization/korean/knight_manager_mod_l_korean.yml` | no |  |
| `localization/russian/knight_manager_mod_l_russian.yml` | no |  |
| `localization/simp_chinese/knight_manager_mod_l_simp_chinese.yml` | no |  |
| `localization/spanish/knight_manager_mod_l_spanish.yml` | no |  |
