# Silk & Silver: announced modding and migration reference

**Preview only, read 2026-11-03.** Local installation: **1.20.1.2 Crozier**. This chapter describes the forthcoming update, not APIs certified for that installation. The 1.20.1 announcement identifies the accompanying update as **1.21**. Exact release contracts, defaults, optional parameters, DLC permissions and runtime behavior require the released files and fresh engine exports.

Primary source: [Silk & Silver Diary #9 — 3D Art, Music, Modding](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302251844), source `NEWS-1847920302251844`, published 2026-11-03. [Diary #8](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114048834) supplies market/route design context. Earlier vision diaries are inventoried in the [article ledger](../research/game-news-20261103/article-coverage.md). Every paragraph below inherits the **announced** status unless explicitly called unresolved.

Do not run global replacements against current mods using this table. The older [building, history and culture guide](subsystem-guide.md) and the [legacy modifier map](../research/jesec/more-legacies-map.md) still describe their dated baseline. The migration requires semantic changes as well as renamed identifiers.

## Data storage, scoped arguments and GUI

The UGCx section announces **Variable Maps**: key/value associations stored on a scope or globally. This is a new data-structure direction beyond the variables and lists documented in the [state handbook](../handbook/state-and-values.md). No CK3 command syntax, local-map lifetime, key/value type set, iteration order, duplicate-key behavior, serialization or multiplayer guarantee is established in the CK3 text. The linked [EU5 Tinto Talk](https://forum.paradoxplaza.com/forum/threads/tinto-talks-extra-modding-in-1-1-rossbach.1899358/) is useful conceptual background, **not CK3 API documentation**. In particular, do not paste its map-access scope-link grammar or local/global variants into CK3 examples before checking the CK3 release.

The announcement expands the accepted argument types of existing operations:

| Operation | Announced addition | Release audit to perform |
|---|---|---|
| `create_nomad_title`, `create_adventurer_title`, `give_noble_family_title`, `create_domicile_title` | Government-type scope input | Exact field/overload, ownership and domicile initialization |
| Character `aptitude` comparison | Court-position-type scope | RHS syntax, root, missing position and comparison operators |
| `start_war`, `ai_start_best_war`, `has_cb_on` | Scoped casus belli | CB type versus instance, attacker/defender and target bindings |
| `spawn_army`, `create_maa_regiment` | New men-at-arms-type scope | Type prefix, required size/owner/location and DLC availability |
| `modifier_value`, `GetModiferValue` | Read a character's summed modifier value in script/GUI | Exported spelling, arguments, numeric type and applicable modifier family |

`GetModiferValue` is the spelling printed by the diary. **Do not silently correct it to `GetModifierValue`**, or assert that either spelling is an installed function. Fresh data-type exports and a real native GUI caller must settle that discrepancy.

Other announced additions include `not_parameter` on culture/rite-qualified modifiers; government-specific interaction scheduling through `ai_frequency_by_tier_government_override`; and geographical-region `province_modifier`/`county_modifier` fields. Keep each reader separate: trigger conditions, scheduling, province modifiers and character modifiers are not interchangeable contexts.

## Trade databases and generated modifiers

The diary describes an additive data model for trade. These are proposed implementation surfaces to revisit on release:

| Surface | Announced role and connected requirements |
|---|---|
| `common/trade/trade_good_types` | Good definition, base price, basic-good flag and optional origin map position |
| `common/trade/county_potential_trade_goods` | County production eligibility for a good; production still needs an actual producer |
| Categories | A category can group goods, declare a building need and supply expertise-level/milestone bonuses; do not guess an omitted directory |
| `common/trade/trade_market_toll_levels` | Route-owner/market-owner toll rates and AI desire; diary says database position determines tier, so additive order has semantic impact |
| Producer/consumer buildings | Production modifiers plus `trade_good_need`; amount, repeat fulfillment and rite restrictions connect production to benefit |
| Market placement | Duchy market capital references a barony; history, ownership and route topology must agree |

Generated families include good/category production add/mult/flat and buy/sell price add/mult. The diary separately requires **four static price modifiers per new good**: `<good>_buy_price_add_modifier`, `<good>_buy_price_mult_modifier`, `<good>_sell_price_add_modifier`, `<good>_sell_price_mult_modifier`. Do not confuse generated modifier types with these script-defined modifier objects.

The complete new-good workflow links the good, county potential, category, producer, consumer, static price modifiers, localization and both `<good>.dds`/`<good>_small.dds` under `gfx/interface/icons/trade/trade_goods/`. This is a dependency checklist, not a released working template. The sample numbers in the diary are balancing examples.

Runtime scopes are announced for `trade_market`, `trade_route`, `trade_monopoly`, and database scopes for `trade_good_type`/`trade_good_category`. Markets/routes/monopolies may hold variables; the diary mentions timed modifiers for markets and routes. It does not thereby promise every state operation on every new scope.

### Announced callbacks

These source-reported contexts are retained to make the eventual audit concrete. They are **not runtime-verified scope contracts**:

| On action | Diary root | Diary named scopes |
|---|---|---|
| `on_trade_route_created` | Route owner | `trade_route`, `trader` |
| `on_trade_route_edited` | Route owner | `trade_route`, `trader`, `primary_good_changed` |
| `on_trade_route_destroyed` | Route | `destroyer` |
| `on_trader_assigned` | Trader | None listed |
| `on_trade_good_category_level_up` / `_down` | Title | `trade_good_category_type` |
| `on_trade_monopoly_invalidated` | Monopoly | None listed |
| `on_market_changed_toll_level` | Market | `new_toll_level`, `old_toll_level` |
| `on_toll_exception_changed` / `_ended` | Market | `new_toll_level`, `old_toll_level`, `character` |

Missing optionality, callback ordering and scope validity after destruction remain **unresolved**. Do not retain a destroyed route or notify an assumed recipient just because its name appears in this table.

## Holdings, districts and building instances

The announced model is **holding → districts → buildings**, replacing the old flat holding/building model. A holding names a primary district and available districts. A district names its primary building chain and additional building choices. District type, slot allocation, construction gates, enabling conditions, graphical background and level restrictions are separate fields.

Announced district types include regular, holding, duchy-capital, special, great, resource, trade-post and entrepôt uses. Regular slot counts have defines and a district-slot modifier; premium slots have separate history/effect workflows. The article inconsistently presents some exact enum formatting; inspect the released `.info` rather than treating prose punctuation as valid script.

District and individual building instances become scopes. Province links, district/type/province/title links and building/type/district links are separate transitions. Iterator families include `built_regular_district`, `built_buildings` and `district_building`. In particular, the diary moves building effects such as `add_building` from province to district scope. Renaming a command without changing the caller's root would be an incomplete port.

Province history is described as a `districts` block containing district entries with type, level and optional buildings. Special/great/duchy-capital building initialization must be reviewed alongside that new structure; do not copy the entire foreign example as a complete starting mod.

## Roads, map assets and compatibility

Road definitions are announced under `common/roads/road_types`: ordered province IDs, tier and endpoints at market capitals. Sea roads use a spline asset ID and sea-zone paths. Road modifier definitions under `common/roads/road_modifiers` connect road, province, trade-route, travel and army-character modifier contexts. The diary describes default road modifiers, road-specific overrides and a highest-tier-road rule for province application; release validation must establish overlaps, water-road behavior and update timing.

New road scope/list operations include `road_province`, `road_on_route`, `road_in_province`, `road_tier`, `set_road_tier` and timed road modifiers. The army movement types `province_movement_speed` and `county_movement_speed` are distinct from ordinary travel-speed modifiers and are described as usable without a road.

Road visuals use spline styles, terrain matching, shaders/textures and caravan entity definitions. The article names `gfx/map/spline_network/spline_styles`, `trade_route_entities` and `spline_network.splnet`. Style IDs, matching texture formats and `connections = none` require a released example; caravan `possible` is described as evaluating the route owner, not the drawn model.

The diary distinguishes **authored road connectivity** from **generated/editable spline shapes**. Repeated wording that shapes are generated is not evidence that gameplay roads are generated automatically. It describes `SplineNetwork.AppendAssets`, `SplineNetwork.ClearAssets` with confirmation, and map-editor spline editing. These commands were **not run**. They write a network in the user directory that can override game/mod networks if left there. A total conversion needs its own province-ID-aware network, and the single binary `.splnet` cannot be text-merged between two map packages. Resolve released command syntax, destination and restoration procedure before using any generator.

## Migration map: announced replacements

| Historical term or surface | Announced successor / required semantic review |
|---|---|
| `development_level`, `development_rate`, progress and `change_development_*` | Corresponding prosperity terms; generated terrain/region modifiers, government flag, map mode and localization must also be traced |
| `county_opinion`, `county_holder_opinion` | `popular_opinion`, `base_popular_opinion`; modifier families also change |
| Monthly county-control growth/decline | Replaced by control moving toward a baseline: inspect `county_control_baseline`, `control_baseline_add`, `monthly_control_change` |
| `tax_mult` | `all_tax_mult` versus category-specific `generic_tax_mult`; choose meaning, not a mechanical substring replacement |
| Province `monthly_income` modifier/trigger | Category tax modifier versus total-monthly-tax trigger; same old name has different contexts |
| Flat holding buildings / `primary_building` | District membership / `primary_district`; building scope, slots, history and UI all change |
| `building_<key>` / description | `<key>` / `<key>_desc` localization; check collisions and GUI consumers |
| Special/great building commands and slots | District counterparts; rebuild rules and callbacks also migrate |
| `house_power` | `house_power_score` |
| `house_based_confederation` | `confederation_base` with character/house/title bases |
| `administrative_title_maa_setup` | `title_maa_setup`, described as having no default |
| `approves_of_succession_law_change` | `approves_of_law_change` |
| Scripted `is_governor` / `governor_efficiency` overrides | Described as engine-backed; review replacement `governor_efficiency_*` modifiers instead of assuming helper overrides still control the result |

The eleven announced tax categories are generic, agricultural, mining, religious, urban, artisan, maritime, tribal, civic, woodland and commerce. Category naming does not establish which historical income modifier should move to which category in a particular mod.

Other announced facilities: character-history betrothal fields; opposite situation participant groups/opinion and `is_in_opposite_participant_group`; automatic house-aspiration levels; four dynamic decision pickers for buildings, markets, routes and goods categories. These extend [current selection guidance](puppets-and-selection.md); controller/root/selected-target contracts still need the released implementations.

## Art, animation, music and sound: useful observations and limits

The first half of #9 documents a reference → concept → model workflow, readable silhouettes by rank/region, prop/animal variants, portrait poses versus map caravan animation, cultural sprawl patterns and resource/market landmarks. These are useful production principles, **not mesh export specifications, asset keys or permission to redistribute source artwork**. The Paris discussion describes a production constraint on swapping city models; it does not prove an absolute engine impossibility for mods.

The audio team describes cultural event ambiences, settlement-size-dependent province audio across ten levels, caravan hoof/vocal layers, GUI sound feedback and musical stingers for milestones. The music composition/instrumentation discussion is artistic context. No FMOD project/bank version, codec specification, sample rate, packing settings or CK3 event path follows from it. Retain the [audio pipeline limits](news-modding-2025-2026.md) instead of converting this production narrative into a working audio tutorial.

## Release acceptance procedure

When released files become available: establish the installed version, read complete matching `.info`/definitions/callers/helpers and assets, obtain fresh script/UI exports, then resolve every announced identifier/rename by context. Record optional targets, lifecycle, owner/deletion state and DLC gates before writing examples. Test newly created content, invalid/removed targets, repeat execution, save/load and two-player routing; GUI/asset and performance tests are separate. Old export success and this research do not satisfy those tests. No existing workspace mod is updated by this chapter.
