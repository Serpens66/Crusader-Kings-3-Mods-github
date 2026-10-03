# Crozier data migration and lifecycle contracts

Baseline: **1.20.0.3**, checked **2026-10-03**. [Coverage](../research/crozier-source-coverage.md), [full-file hashes and field/export locations](../research/general-120-evidence.json). This chapter is a migration/reference guide, not permission to rewrite existing mods or skip their full feature audits.

## Ownership and schema migrations

Religion/faith/rite ownership, doctrine locks and tenet state are detailed in [Religion and rites](religion-rites.md). For an older definition, inspect the current database and consumers together. The installed fields include `faith_character_modifier`, `involved_faith_character_modifier`, `interloper_faith_character_modifier`, `tenet_selection_pair` and `tenet_background_icon`. Old field names and texture directories must not be replaced blindly across unrelated schemas. The release announces removal of `character_faith_modifier` on holding buildings; do not confuse that removal with supported same-named fields in another database.

`common/laws/_laws.info:3–12` requires each law to name `law_group_type` and describes unique ordering indexes. `common/law_groups/_law_groups.info` separately owns default law, cumulative behavior, visibility/change eligibility and a government-flag fast path. Thus a new law does not require inserting a nested definition into an existing group. `change_authority_effect` is a native scripted helper, not an engine primitive; trace its actual parameters and callers for an authority change.

`common/governments/_governments.info:311–343` documents `mechanic_type` and the rule that one government per mechanic type should be its default. Arbitrary flags are distinct from mechanics (`:711–718`). Use `government_has_mechanic` / `government_has_flag` for character queries and the exported `government_type_has_flag` for the government-type scope. Having one flag does not automatically enable every administrative feature. `redirects_wars_to_overlord` only redirects when the overlord can intervene. `royal_court` includes `landed`, alongside its other modes and subject restrictions.

The lease reference restricts ordinary leases to eligible non-capital baronies and higher-tier holders. Vassal and clerical-region hierarchies are distinct; missing or mismatched intermediaries can be skipped. Revenue/levy share calculations, lessee remainder and over-allocation handling belong to this schema, not normal vassal tax rules. The current holy-order-specific effect is `lease_out_to_holy_order`; dynamic Holy Orders have their own `common/holy_orders/_holy_orders.info`. Neither declaration establishes arbitrary clerical lease execution.

In `tax_split`, the three claims are a flat split of the original amount; the lessee receives the remainder. Negative claims become zero. An aggregate above one logs a content error and truncates in the documented order `lease_liege`, `top_lease_liege_direct`, then `ruler`. Optional `<share>_max` supplies a final ceiling; an inline numeric `min`/`max` is instead a sequential operation and cannot supply the same ceiling tooltip. Named operand `desc` entries control which terms are shown. The tooltip threshold/hook fields must match the actual calculation; they do not implement payment eligibility by themselves.

## Succession, history and project stages

`common/succession_election/_succession_election.info` assigns unique keys to candidate sets. Set ordering and candidate policy affect which candidates survive; MTTH and script-value score fields are separate alternatives. Appointment candidate/holder/title contexts differ from elector contexts.

The release's phrase `allow_same_candidate_tier` does not match the installed appointment reference's literal **`allowed_candidate_tier = lower|lower_or_equal|any`** (`:32–41`). Use the installed spelling. `use_investment_cap` is documented separately; no undocumented default is inferred. `keep_top_tier_titles_together` defaults to no. Fallback inheritance and trait `inheritance_blocker` need the selected title/trait contract; an announcement is insufficient to supply missing syntax.

The correct character-history override key is **`history_override_priority`**, from `history/_characters.info:24–31`. Higher priority overrides base attributes and birth date; other entries combine additively. Same-ID definitions need different priorities. Events instead use `id_override_priority`; their cold-start priority and hot-reload behavior differ. These two keys are not interchangeable.

Character `effect` requires the character to be alive at the selected start date; `effect_even_if_dead` also supports post-death dated effects according to the current history reference. `obscured` disables normal character access, with `<character_id>_obscured_desc` for the alternative tooltip. A historical definition is not a future scheduled event.

Great Project `founder_heir` is **stage-specific**: during `is_shown` planning it is the founder, while funded-project callbacks describe a current living heir that may be absent. Owner, founder, contributor and heir cannot be treated as synonyms. The reference also distinguishes cancellation from invalidation followed by removal. `expose_scheme_to` is a scheme-scoped effect targeting one character; it does not inherently mean public exposure to everyone.

## Hook contexts and declaration discrepancies

Some current on-action exports say Expected Scope `none`, while native hook headers explicitly describe a root. Preserve both observations; do not interpret the export label alone as proof of rootless runtime execution.

| Hook | Native documented root / targets | Source |
|---|---|---|
| `on_trait_gained`, `on_trait_lost` | Character gaining/losing trait; `scope:trait` | `common/on_action/traits_on_actions.txt:3–6,64–67` |
| `on_character_created` | Newly created character; `scope:creation_reason` flag | `character_created_on_actions.txt:1–18` |
| `on_player_character_change` | New player character; `scope:previous_player_character` | `player_change_on_actions.txt:1–6` |
| `on_county_rite_change` | County title; `scope:old_rite`; explicitly excludes changes to a different Faith | `county_on_actions.txt:1–4` |
| `on_county_faith_change` | County title; `scope:old_faith` | same file `:11–14` |
| `on_death` | Character just about to die; `death_reason`, conditional `killer` and `artifact` | `death.txt:1–7` |
| `on_personal_tenet_gain` | Selecting character; `scope:tenet` | `religion_on_actions.txt:1739–1742` |
| `on_liberation_siege_completion` | Liberator; barony/county/previous controller/war and liberated-barony list | `army_on_actions.txt:622–629` |

Creation reasons include script creation, ruler designer (including generated family), pool/guests/court population, mercenaries, succession, grants, holy wars, migration and save-file fixes. Births use the separate childbirth hooks. Trait callbacks can recursively add traits: native code uses a temporary cooldown to prevent a loop. This is a relevant native design example, not proof that the same marker is correct for every recursion problem.

`on_rite_change`, `on_rite_created` and personal-tenet loss are also exported and have native implementations. Review their individual saved targets; no shared blanket scope contract is assumed. [Lookup](../tools/lookup.py) retrieves their headers and declarations. Add uniquely named child on-actions according to the existing [subscription guidance](events-decisions-on-actions.md); preserve the native subscribers.

## Further contracts to retrieve

| Area | Current entry point and distinction |
|---|---|
| Activities | `tenet_doctrine_based_activity` and slot filters in `_activity_type.info:222–240`; personal filter does not support doctrines. `header_background` uses player-character root, whereas the normal background has activity context |
| Situation GUI | `common/situation/situations/_situations.info` supplies ending/ordinary decision lists, participant-group `gui_tags` and phase textures |
| Council eligibility | `valid_for_council_task` / `valid_for_council_position` test the selected council-position requirement; this differs from checking employment alone |
| Genealogy | Current exported grandchild/great-grandchild and real-parent lists, parent-clearing effects and birth-date triggers; use each exact iterator/target declaration |
| Interaction targets | Review `realm_titles` versus `realm_counties` and `other_faith_heads`; broader target sets can change a mod's behavior |
| Flavorization | Current `_flavourization.info` owns Rite/title-kind/lessee conditions; decoration does not change the underlying holder |
| Balance | Standalone currency gain/loss modifiers apply to lump sums; they are distinct from monthly/yearly income. Retrieve current legitimacy-level effect arguments |
| Other migration points | Locked activity invite rules, dynasty base-name checks, lowborn bookmarks, clerical-marriage parameters and secular inheritance blockers need their specific definitions/consumers |

The actual invite-rule schema is `common/activities/guest_invite_rules/_invite_rules.info`, where `locked` defaults to no and prevents toggling the rule off when enabled. Guest construction has host-character root and an optional special-option flag. The current dynasty trigger is **`dynasty_has_base_name`**; the announcement's `dynast_has_base_name` is another spelling discrepancy, not a supported alias. Trait `inheritance_blocker` and `claim_inheritance_blocker` separately enumerate `none/dynasty/secular/all` in `_traits.info`. These should not be implemented as an unconditional inheritance ban.

## Build-specific and runtime boundaries

The official 1.20.0.3 hotfix lists regression corrections involving appointments, nomad reform, DLC doctrine gating, religious heads, treasury and travel. These are useful regression categories, not new inferred APIs or evidence that a mod's corresponding behavior passes.

No migration, lifecycle, reload or multiplayer test ran here. For each actual mod update, compare original intent with the selected current contract, complete its Vanilla audit and test boundary values, absent targets, multiple requests, callbacks, inheritance, bookmark/DLC variants and save/reload. Historical preservation reports remain unchanged.

## Legacy overrides and added native branches

The [legacy comparison](dynasty-legacies.md) adds concrete 1.19.0.6→1.20.0.3 consequences: PAM track/perks, surrounding-character Iberian struggle branches, administrative-mechanic checks, `faith_character_modifier`, rite-cost and herald-trait changes. Historical Less Restrictive full files must preserve these current native branches in any future port. This source finding does not update an existing mod or close its runtime acceptance gates.
