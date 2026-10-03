# More Legacies: complete source map

Source: [6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod). Authored table of observed code, not tested modifier semantics. See [contracts](../../systems/dynasty-legacies.md).

## Track visibility

Every restricted track also has an OR branch retaining visibility when its first perk is owned. Four track blocks have no `is_shown`. Restricted conditions inspect the dynast, not automatically the GUI viewer.

| Track | Definition line | Additional visibility inputs |
|---|---:|---|
| `bld_chivalry_legacy_track` | 1 | `ethos_bellicose`, `ethos_courtly`, `tradition_hereditary_hierarchy`, `tradition_only_the_strong`, `tradition_chivalry`, `tradition_chanson_de_geste` |
| `bld_devotion_legacy_track` | 22 | No explicit visibility block |
| `bld_dominance_legacy_track` | 26 | `ethos_bellicose`, `ethos_stoic`, `tradition_ruling_caste`, `tradition_castle_keepers`, `tradition_staunch_traditionalists`, `tradition_talent_acquisition`, `tradition_swords_for_hire`, `tradition_only_the_strong`, `tradition_eye_for_an_eye`, `tradition_martial_admiration`, `tradition_warrior_culture`, `tradition_fp1_performative_honour`, `tradition_fp1_the_right_to_prove`, `tradition_fp1_trials_by_combat`, `tradition_by_the_sword` |
| `bld_industry_legacy_track` | 56 | No explicit visibility block |
| `bld_influence_legacy_track` | 60 | No explicit visibility block |
| `bld_mercantile_legacy_track` | 64 | `ethos_bureaucratic`, `ethos_egalitarian`, `tradition_astute_diplomats`, `tradition_family_entrepreneurship`, `tradition_maritime_mercantilism`, `tradition_artisans`, `tradition_xenophilic` |
| `bld_seafaring_legacy_track` | 86 | `tradition_maritime_mercantilism`, `tradition_fp1_coastal_warriors`, `tradition_fishermen`, `tradition_practiced_pirates`, `tradition_seafaring`, `tradition_polders` |
| `bld_temptation_legacy_track` | 107 | No explicit visibility block |
| `bld_tradition_legacy_track` | 111 | `ethos_egalitarian`, `tradition_culture_blending`, `tradition_fp2_malleable_subjects`, `tradition_malleable_invaders`, `tradition_xenophilic`, `tradition_language_scholars`, `tradition_religion_blending`, `tradition_african_tolerance`, `tradition_steppe_tolerance` |
| `bld_witchcraft_legacy_track` | 135 | `witch`, `secret_witch` |

## All 50 perk payloads

Numbers below are source values. A negative build speed or phase duration modifier is not a negative success chance. Named values must be evaluated from their definition. No perk in these two mod files adds a custom `effect`, saved state, event or on action.

| ID / English name | Line | Character modifier assignments |
|---|---:|---|
| `bld_chivalry_legacy_1` / Romantic | 3 | `attraction_opinion = 10`; `courting_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value` |
| `bld_chivalry_legacy_2` / Valiant | 22 | `monthly_prestige_gain_mult = 0.1`; `knight_effectiveness_mult = 0.15` |
| `bld_chivalry_legacy_3` / Poetic | 31 | `courtier_and_guest_opinion = 10`; `court_grandeur_baseline_add = 5`; `monthly_court_grandeur_change_mult = 0.5`; `learn_language_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value` |
| `bld_chivalry_legacy_4` / Gallant | 42 | `knight_limit = 1`; `monthly_prestige_gain_per_knight_add = 0.2`; `monthly_piety_gain_per_knight_add = 0.2` |
| `bld_chivalry_legacy_5` / Heroic | 52 | `diplomacy_per_prestige_level = 1`; `prowess_per_prestige_level = 1` |
| `bld_devotion_legacy_1` / Righteous | 63 | `monthly_piety_gain_per_happy_powerful_vassal_mult = 0.05`; `tolerance_advantage_mod = 5` |
| `bld_devotion_legacy_2` / Venerate | 82 | `domain_tax_same_faith_mult = 0.15` |
| `bld_devotion_legacy_3` / Sanctify | 90 | `church_holding_build_speed = -0.1`; `church_holding_build_gold_cost = -0.1`; `church_holding_holding_build_speed = -0.1`; `church_holding_holding_build_gold_cost = -0.1` |
| `bld_devotion_legacy_4` / Unwavering | 101 | `holy_order_hire_cost_mult = -0.2`; `monthly_piety_gain_per_knight_mult = 0.01` |
| `bld_devotion_legacy_5` / Ardent | 110 | `learning_per_piety_level = 1`; `levy_reinforcement_rate_same_faith = 0.1` |
| `bld_dominance_legacy_1` / Ruthless | 121 | `dread_gain_mult = 0.2`; `pursue_efficiency = 0.1`; `enemy_hard_casualty_modifier = 0.1` |
| `bld_dominance_legacy_2` / Oppressive | 141 | `dread_baseline_add = 10`; `monthly_war_income_mult = 0.1` |
| `bld_dominance_legacy_3` / Dark Rumors | 150 | `dread_decay_mult = -0.2`; `monthly_prestige_gain_per_dread_add = 0.05` |
| `bld_dominance_legacy_4` / Intimidating | 159 | `men_at_arms_maintenance = -0.1`; `intimidated_vassal_levy_contribution_mult = 0.1`; `cowed_vassal_levy_contribution_mult = 0.2` |
| `bld_dominance_legacy_5` / Brutal | 169 | `martial_per_prestige_level = 1`; `prowess_per_stress_level = 1` |
| `bld_industry_legacy_1` / Earnest Efforts | 180 | `short_reign_duration_mult = -0.25`; `enemy_hostile_scheme_phase_duration_add = 30` |
| `bld_industry_legacy_2` / Ever-Improving | 199 | `build_speed = -0.1`; `development_growth_factor = 0.2` |
| `bld_industry_legacy_3` / Always Learning | 208 | `councillor_opinion = 10`; `cultural_head_fascination_mult = 0.15` |
| `bld_industry_legacy_4` / Meticulous | 217 | `domain_limit = 1`; `county_opinion_add = 5` |
| `bld_industry_legacy_5` / Perseverance | 226 | `learning_per_stress_level = 1`; `stewardship_per_stress_level = 1`; `monthly_income_per_stress_level_mult = 0.05` |
| `bld_influence_legacy_1` / Power Dynamics | 238 | `vassal_limit = 10`; `direct_vassal_opinion = 5`; `courtier_and_guest_opinion = 5`; `fellow_vassal_opinion = 10`; `liege_opinion = 10` |
| `bld_influence_legacy_2` / Astute | 260 | `monthly_county_control_growth_add = 0.1`; `vassal_tax_contribution_mult = 0.1` |
| `bld_influence_legacy_3` / Cunning | 269 | `befriend_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value`; `sway_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value`; `murder_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value` |
| `bld_influence_legacy_4` / Popular Persona | 279 | `county_opinion_add = 5`; `monthly_tyranny = -0.05` |
| `bld_influence_legacy_5` / Trustworthy | 288 | `intrigue_per_prestige_level = 1` |
| `bld_mercantile_legacy_1` / International Trade | 298 | `diplomatic_range_mult = 0.15`; `independent_ruler_opinion = 10`; `court_grandeur_baseline_add = 5` |
| `bld_mercantile_legacy_2` / Artisans | 318 | `domain_tax_mult = 0.15`; `build_speed = -0.05`; `build_gold_cost = -0.05` |
| `bld_mercantile_legacy_3` / Guarded Roads | 328 | `knight_limit = 1`; `men_at_arms_maintenance = -0.2`; `mercenary_hire_cost_mult = -0.2` |
| `bld_mercantile_legacy_4` / Investors | 338 | `happy_powerful_vassal_tax_contribution_mult = 0.2` |
| `bld_mercantile_legacy_5` / Established Routes | 346 | `diplomatic_range_mult = 0.15`; `long_reign_bonus_mult = 0.25`; `stewardship_per_prestige_level = 1` |
| `bld_seafaring_legacy_1` / Sea Legs | 358 | `prowess = 1`; `no_water_crossing_penalty = yes`; `embarkation_cost_mult = -0.25` |
| `bld_seafaring_legacy_2` / Well-Traveled | 378 | `diplomatic_range_mult = 0.3`; `different_culture_opinion = 10` |
| `bld_seafaring_legacy_3` / Sea Breezes | 387 | `stress_gain_mult = -0.1`; `stress_loss_mult = 0.1`; `naval_movement_speed_mult = 0.2` |
| `bld_seafaring_legacy_4` / Maritime Law | 397 | `monthly_war_income_mult = 0.1`; `coastal_advantage = 5` |
| `bld_seafaring_legacy_5` / Bountiful Seas | 406 | `army_maintenance_mult = -0.2`; `supply_duration = 0.2`; `supply_capacity_mult = 0.2` |
| `bld_temptation_legacy_1` / Fruitful Labors | 418 | `fertility = 0.1`; `years_of_fertility = 5` |
| `bld_temptation_legacy_2` / Comforts of Home | 437 | `court_grandeur_baseline_add = 5`; `spouse_opinion = 10`; `stress_loss_mult = 0.1` |
| `bld_temptation_legacy_3` / Prolific Flirt | 447 | `seduce_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value`; `courting_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value`; `elope_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value` |
| `bld_temptation_legacy_4` / Refined Tastes | 457 | `positive_inactive_inheritance_chance = 0.1`; `negative_inactive_inheritance_chance = -0.1`; `genetic_trait_strengthen_chance = 0.1` |
| `bld_temptation_legacy_5` / Sweet Corruption | 467 | `intrigue_per_stress_level = 1`; `max_seduce_schemes_add = 1` |
| `bld_tradition_legacy_1` / Enduring | 478 | `long_reign_bonus_mult = 0.25`; `title_creation_cost_mult = -0.1`; `domain_tax_same_faith_mult_even_if_baron = 0.1` |
| `bld_tradition_legacy_2` / Unified Front | 498 | `dread_baseline_add = 5`; `dynasty_opinion = 5`; `dynasty_house_opinion = 5`; `close_relative_opinion = 10` |
| `bld_tradition_legacy_3` / Customary | 509 | `monthly_piety_gain_mult = 0.15`; `monthly_prestige_gain_mult = 0.15` |
| `bld_tradition_legacy_4` / Like-Minded | 518 | `same_culture_opinion = 5`; `same_faith_opinion = 5`; `same_culture_holy_order_hire_cost_mult = -0.2`; `same_culture_mercenary_hire_cost_mult = -0.2` |
| `bld_tradition_legacy_5` / Established | 529 | `diplomacy_per_piety_level = 1`; `enemy_personal_scheme_phase_duration_add = 30` |
| `bld_witchcraft_legacy_1` / Profane Rites | 540 | `fertility = 0.1`; `life_expectancy = 5` |
| `bld_witchcraft_legacy_2` / Initiation | 559 | `max_convert_to_witchcraft_schemes_add = 3`; `convert_to_witchcraft_scheme_phase_duration_add = monumental_scheme_phase_duration_bonus_value` |
| `bld_witchcraft_legacy_3` / Sorcerous Studies | 568 | `cultural_head_fascination_mult = 0.15`; `learn_language_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value` |
| `bld_witchcraft_legacy_4` / Otherworldly Aura | 577 | `monthly_piety_gain_per_dread_add = 0.1`; `dread_baseline_add = 5` |
| `bld_witchcraft_legacy_5` / Dark Mysticism | 586 | `intrigue_per_piety_level = 1` |

## Localization and assets

| Language file | Missing track/perk name keys |
|---|---|
| [mod/localization/english/dynasty_legacies/more_legacies_l_english.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/english/dynasty_legacies/more_legacies_l_english.yml) | 0 |
| [mod/localization/french/dynasty_legacies/more_legacies_l_french.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/french/dynasty_legacies/more_legacies_l_french.yml) | 0 |
| [mod/localization/german/dynasty_legacies/more_legacies_l_german.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/german/dynasty_legacies/more_legacies_l_german.yml) | 0 |
| [mod/localization/japanese/dynasty_legacies/more_legacies_l_japanese.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/japanese/dynasty_legacies/more_legacies_l_japanese.yml) | 0 |
| [mod/localization/korean/dynasty_legacies/more_legacies_l_korean.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/korean/dynasty_legacies/more_legacies_l_korean.yml) | 0 |
| [mod/localization/polish/dynasty_legacies/more_legacies_l_polish.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/polish/dynasty_legacies/more_legacies_l_polish.yml) | 0 |
| [mod/localization/russian/dynasty_legacies/more_legacies_l_russian.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/russian/dynasty_legacies/more_legacies_l_russian.yml) | 0 |
| [mod/localization/simp_chinese/dynasty_legacies/more_legacies_l_simp_chinese.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/simp_chinese/dynasty_legacies/more_legacies_l_simp_chinese.yml) | 0 |
| [mod/localization/spanish/dynasty_legacies/more_legacies_l_spanish.yml](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/localization/spanish/dynasty_legacies/more_legacies_l_spanish.yml) | 0 |

All ten IDs have one icon and one illustration path in the repository tree. The inventory records the twenty DDS Git object IDs; pixels/formats/frames were not imported or rendered. `GetIcon` and `GetTrackIcon` are different GUI consumers. Their engine-side path resolution must not be guessed from filenames alone.

## AI and initialization caveats

The ten first perks set `ai_chance.value = 11` and multiply by zero when `can_start_new_legacy_track_trigger = no`; the other forty omit an AI block. The installed perk `.info` documents a default weight of 1000. These are relative selection weights, not percentages. The helper enumerates native tracks explicitly, including the new PAM track, but none of the `bld_` tracks. Therefore its name does not prove that it prevents several custom tracks from being opened together. Trace/customize the policy and test AI separately.

The supplied README describes `tolerance_advantage_mod = 5` as tolerance opinion, while the source uses an advantage modifier. Treat the code/engine entry as the starting point for a tooltip/benefit test, not the prose description. No balance or 1.20 compatibility claim is adopted.
