# Texture comparison

Dimensions are header values (width × height). A missing native same-path file does not establish that an asset is unused: scripted or dynamic references may still load it. A header mismatch is not a rendered failure.

| Package | Textures | Without native same path | Size differs | Non DDS containers under dds extension |
|---|---:|---:|---:|---:|
| Gender Colour | 5 | 3 | 0 | 0 |
| GFX-Mod | 8 | 3 | 1 | 0 |
| GFX-Mod Serp | 664 | 291 | 41 | 3 |

## Size differences

| File | Mod width × height | Native width × height |
|---|---|---|
| `GFX-Mod/gfx/portraits/portrait_rank.dds` | 1176 × 194 | 1374 × 194 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/_missing_interaction.dds` | 106 × 106 | 105 × 105 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/artifact.dds` | 106 × 106 | 60 × 60 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/declare_war_interaction.dds` | 106 × 106 | 105 × 105 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/designate_shieldmaiden_interaction.dds` | 106 × 106 | 70 × 70 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/fabricate_hook_interaction.dds` | 106 × 106 | 60 × 60 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/grant_titles_interaction.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_combat.dds` | 106 × 106 | 73 × 72 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_culture.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_dynasty.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_gold.dds` | 106 × 106 | 60 × 60 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_hostile.dds` | 106 × 106 | 60 × 60 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_marriage.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/icon_personal.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/inspiration.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/prison.dds` | 106 × 106 | 70 × 70 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/send_poem_interaction.dds` | 106 × 106 | 60 × 60 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/send_to_varangian_guard_interaction.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/torture_interaction.dds` | 106 × 106 | 60 × 60 |
| `GFX-Mod Serp/gfx/interface/icons/character_interactions/vassal_claim_liege_title_interaction.dds` | 106 × 106 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/administrative_court_1.dds` | 120 × 120 | 119 × 117 |
| `GFX-Mod Serp/gfx/interface/icons/traits/administrative_court_2.dds` | 120 × 120 | 119 × 117 |
| `GFX-Mod Serp/gfx/interface/icons/traits/diplomatic_court_1.dds` | 120 × 120 | 119 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/diplomatic_court_2.dds` | 120 × 120 | 119 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/ill.dds` | 60 × 60 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/intrigue_court_1.dds` | 120 × 120 | 119 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/intrigue_court_2.dds` | 120 × 120 | 119 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/scholarly_court_1.dds` | 120 × 120 | 119 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/scholarly_court_2.dds` | 120 × 120 | 119 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/sin.dds` | 24 × 24 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/virtue.dds` | 24 × 24 | 120 × 120 |
| `GFX-Mod Serp/gfx/interface/icons/traits/warlike_court_1.dds` | 120 × 120 | 118 × 118 |
| `GFX-Mod Serp/gfx/interface/icons/traits/warlike_court_2.dds` | 120 × 120 | 119 × 118 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_blue.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_frozen.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_gray.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_green.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_purple.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_red.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_scheme.dds` | 256 × 64 | 180 × 45 |
| `GFX-Mod Serp/gfx/interface/progressbars/progress_standard.dds` | 256 × 64 | 254 × 64 |
| `GFX-Mod Serp/gfx/portraits/portrait_rank.dds` | 1176 × 194 | 1374 × 194 |

## Other container types

| File | Container |
|---|---|
| `GFX-Mod Serp/gfx/interface/icons/icon_prowess.dds` | PNG |
| `GFX-Mod Serp/gfx/interface/icons/icon_skills.dds` | PNG |
| `GFX-Mod Serp/gfx/interface/icons/icon_skills_martial.dds` | PNG |
