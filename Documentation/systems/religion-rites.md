# Religion, rites and clerical systems in Crozier

Baseline: **1.20.0.3**, checked **2026-10-03**. These are current schema/declaration findings, not a completed implementation audit. [Coverage and remaining questions](../research/crozier-source-coverage.md) and [source hashes/locations](../research/general-120-evidence.json) accompany this chapter. Use [lookup](../tools/lookup.py) for exact exported commands.

## Separate databases and ownership

The installation separates `religion_family_types`, `religion_types`, `faith_types`, `rite_types`, `tenet_types`, `doctrine_types`, `doctrine_group_types`, `doctrine_category_types`, `holy_site_types`, `rite_names` and `rite_icons` under `common/religion`. Each has a current `.info` reference. New child definitions can reference existing parent keys; do not infer that adding one child requires overriding the parent's entire file. Collision handling still needs the appropriate loader contract.

`faith_types/_faith_types.info:1–78` defines `faith_details` with required `religion`, presentation, religious head, head-of-rite override and theocracy government. A scripted `main_rite` owns effective core tenets; keep Rite-specific doctrines there. Faith doctrines fill otherwise unfilled groups, while Rite doctrine choices take precedence in their groups. If no scripted main Rite exists, faith tenets/doctrines seed a dynamic main Rite. DLC-dependent `tenet_selection_pair` has an optional fallback tenet. Faith localization can inherit absent keys from the religion.

`rite_types/_rite_types.info:34–82` separates conversion permission (`convert`, default yes) from creation (`create`, default yes). A type without a parent faith is available for script creation rather than automatically instantiated from history. Accessing an uncreated `rite:key` can error: validate existence before using it. The exported `create_rite_from_type` runs in character scope and targets a Rite type; it creates the Rite in that character's Faith. A Rite type is a database definition, while a Rite is a runtime scope; do not interchange them.

The complete effect export additionally supplies `type`, optional `save_scope_as` and `convert` (founder conversion defaults to **no**, unlike the Rite type's conversion permission). The scoped character becomes founder. Native historical-character effects create `daoxue` under explicit date/global-marker guards before assigning the character's Rite. This is an actual caller, not proof that all dynamic creation workflows are already tested.

## History and changes of parent Faith

`history/faiths/_faith_history.info` documents date-driven creation, main Rite, religious head, knowledge/permission/prohibition, popularity and Rite setup. Rite membership is chronologically additive; moving a Rite to another Faith removes its prior membership. A `tenet_setup` replaces the whole core-tenet set, whereas doctrine setup overwrites only the specified groups. DLC alternatives are checked in definition order and need an appropriate fallback.

The reference explicitly describes a first pass assigning main Rites and parent Faiths, followed by created/enabled flags, tenet statuses, Rite setup and popularity. Known/permitted/prohibited status lists run in that order; duplicate entries can warn even when later entries replace earlier state. History is bookmark initialization, not an instruction to schedule gameplay events on those dates. Faith `origin` supports historical religious-head mismatches; it is not a general permission to ignore erroneous history.

The current export says `set_parent_faith` is a Rite-scoped effect targeting a Faith and also updates the Faith of following characters and counties. This is a potentially broad state change, not a harmless edit to a parent pointer. Audit its consumers, doctrine removal, heads and callbacks for a real feature.

## Doctrine groups, selection and precedence

`doctrine_types/_doctrine_types.info` requires `doctrine_group_type`; groups reference a category. Ordering uses `index` and should be unique. `doctrine_group_types/_doctrine_group_types.info:25–36` documents `doctrine_lock = none|rite|faith|religion` (default none), the corresponding branch/move removal rules and the exception when the destination already practices the same locked doctrine. Group `main_rite` only supplies UI warnings; its actual gameplay behavior is left to script.

`change_doctrine` replaces the existing doctrine of the same group. Numeric/special doctrine parameters use `special_parameters`; arbitrary boolean parameters are separate. Do not treat each special value as additive: the reference supplies per-field highest-value, merge, boolean and override rules. `piety_cost` evaluates in Rite scope, while several presentation/selection blocks remain Faith-scoped. Their actor reference can be absent.

Doctrine and tenet selection must examine the UI's `selected_doctrines` / `selected_tenets` lists when checking simultaneous choices. Current live Faith contents may differ from the proposed selection. `tenet_types/_tenet_types.info` separately documents `can_pick_as_personal_tenet` in character scope, `personal_tenet_modifier` and `personal_tenet_parameters`, queried with `has_personal_tenet_flag`. Its DLC field limits code-driven lists and does not automatically make `is_shown` fail.

Knowledge, popularity, personal choice and core/permitted/prohibited status are separate concepts. Retrieve their individual exported operations and triggers rather than reducing all of them to `has_tenet`. Personal-tenet hooks are described in the [migration and hooks chapter](crozier-migration.md).

## Holy sites, relic benefits and spiritual fulfillment

`holy_site_types/_holy_site_types.info:1–79` supports location-specific and general types. Regular and Eminent sites have different benefit ownership: global Faith modifiers require Eminent status; holder/county benefits can apply to both. Repeated scaled modifier blocks evaluate `scale` in holy-site scope. `holy_site_total_artifact_rarity` uses qualifying relic rarity; the eligibility predicate differs between the documented Faith and county cases. Parameter presence tests do not distinguish a parameter written as yes from one written as no.

The export supplies Faith-scoped `create_holy_site`; dynamic site creation must use its actual input structure and audit placement, Faith membership and benefit consumers. The type definition alone does not establish runtime creation or every DLC-access rule.

Its current declaration rejects a type already present in the Faith and a barony already hosting another holy site. A location supplied by the type can be overridden; a locationless type needs `county` or `barony`. `eminent` defaults to no; an optional `actor` attributes the on-action. These documented constraints are distinct from menu eligibility and script-level capacity policy.

`common/spiritual_fulfillment/_spiritual_fulfillment_type.info` maps religions to fulfillment types: mappings must not overlap, and one empty religion list supplies a fallback. Levels require unique thresholds within the defined bounds. Positive levels activate at or above their threshold, negative levels at or below it; zero is documented as always active. Levels provide modifiers, icons and flags for `has_fulfillment_parameter`. `stress_and_fulfillment_impact` is an exposed effect, but its exact argument forms and trait relevance must be taken from the current export/callers.

## Clerical regions, heads and leases

The export places `create_clerical_region` in province scope; retrieve its fields, including the title and domicile setup, rather than substituting an ordinary government-based domicile operation. The resulting clerical title/region is distinct from the secular de jure hierarchy. Create/merge/split APIs are declarations; membership, succession, capital and invalidation need a feature audit.

The creation declaration limits initial membership to free counties in the capital's de jure kingdom that are reachable by land adjacency. It supplies `domicile_type`, naming fields and `save_scope_as` for the new title. Adjective defaults to the name when absent; other optional naming fields retain their declared optionality. Do not promise a whole-kingdom region when adjacency or existing membership excludes counties.

`religious_head_or_challenger` is an exported target. An ordinary head, challenger and head of Rite are distinct roles; test absent roles and the specific interaction route. `head_of_rite` / `head_of_rites` and the `rite_conversion` special interaction are native interaction facilities, not a guarantee of any arbitrary conversion workflow.

The [lease schema](crozier-migration.md) describes both vassal-based and clerical-region-based benefit hierarchies. Taxes, levies, religious superiors, secular lieges and holders must not be treated as one ownership chain.

## Acceptance boundary

No religion feature or example was game-tested here. For implementation, complete the selected feature's Vanilla audit, then cover every supported bookmark/DLC combination, uncreated/moved Rites, doctrine locks, selection state, absent heads, site placement/benefits, parent-change callbacks and save/reload. The [native conversion research](../update-readiness/mods/mass-demand-conversion-recheck.md) illustrates why a positive query or a late scope fallback cannot certify all command stages.
