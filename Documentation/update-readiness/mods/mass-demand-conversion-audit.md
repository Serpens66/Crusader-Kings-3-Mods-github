# Mass Demand Conversion: source audit supplement

Date: **2026-10-03**. Installed build: **1.20.0.3 (Crozier)**. This supplements the [original update sheet](mass-demand-conversion.md); it does not replace historical evidence or certify compatibility. **Partial feature source audit; engine-context gates remain; gameplay/GUI/MP not run.**

The [dated evidence](../evidence/mass-conversion-audit-20261003.json) records whole-file SHA-256, exact object boundaries, literal dependency candidates, retained export spans and preservation hashes. [Collector/checker](../../tools/collect_mass_conversion_audit.py) reads the installation and writes only that supplement. Its lexical graph is not a parameter-expanded semantic call graph. A file read/hash does not prove all its branches were semantically audited.

## Sources and provenance

Native paths below are relative to the installed `game` directory. Resolve against `game_root` in the evidence. `objects` contains exact first/last lines; `native_sources` contains whole-file hashes. Numbers below locate the reviewed entry points, not a claim that every dependency is settled.

| Source | Entry points / reviewed contract |
|---|---|
| `common/character_interactions/00_religious_interactions.txt` | Courtier 158; house 508; AI vassal/tributary ruler 780. Read complete definitions, including options, costs and responses |
| `common/character_interactions/_character_interactions.info` | Pending-interaction blocking 111–116; validity fields 242–270; options/default-off 332–367; stages 377–399 |
| `common/scripted_triggers/00_religious_triggers.txt` | Crime 967; shared conversion eligibility 1198 |
| `common/script_values/pam_values.txt` | Conditional influence value 9473 |
| `common/scripted_effects/pam_effects.txt` | Acts of Apostles 1257; gold concession 1334; Mendicant Preachers 1354 |
| `common/scripted_effects/00_religious_interaction_effects.txt` | Family selection 1158; conversion dispatch 1220; family conversion 1287; state-faith refusal piety 1799 |
| `common/scripted_effects/00_interaction_effects.txt` | Puppeteer notification 8; vassal conversion wrapper 4793 |
| `common/scripted_effects/11_dlc_pam_scripted_effects.txt` | Rite conversion consequences 18 |
| `common/scripted_effects/00_unity_effects.txt` | Acceptance 125; refusal 165 |
| `common/scripted_effects/07_dlc_ep3_scripted_effects.txt` | State-faith acceptance piety 10358; refusal piety 10373 |
| `common/scripted_effects/tgp_mandala_scripted_effects.txt` | Mandala converter reward 1652 |
| `events/religion_events/religious_interaction_events.txt` | Acceptance 2002:1271; full refusal 2003:1340; gold 2011:1541; favor 2012:1695; study 2015:1836; notification 2016 follows |
| `events/interaction_events/character_interaction_events.txt` | House acceptance 0181:1444; refusal 0182:1467 |
| `events/religion_events/false_conversion_events.txt` | 0900:731 routes to 1000/1010, including secret-faith choice |
| `common/schemes/scheme_types/study_faith_scheme.txt` | `study_faith`, owner/target scopes, phase success/failure and invalidation |
| `common/on_action/schemes/study_faith_on_actions.txt` | Success:1; failure:34; pending conversion completion scheduled with `days = 2` |
| `common/on_action/dlc/pam/pam_on_actions.txt` | Additional `study_faith_success` subscription:71; keep separate definitions in discovery, do not assume overwrite |
| `events/scheme_events/study_faith_scheme/study_faith_outcome_events.txt` | 0100:7; 0101:36; 0110:118; 0111:146; reports 0102:229 and 0103:241 |
| `common/puppets/actions/puppet_actions.txt` | House action:129; vassal action:134; these register native interactions, not this mod decision |
| `common/puppets/actions/_puppet_actions.info` | Puppet decision ROOT and `scope:puppeteer`:31–34; does not document ordinary script-query initialization |
| `gui/decision_view_widgets/decision_view_widget_decision_option_list_controller.gui` | `OnSelect`, enabled entries and selected radio frame:28–38 |

Both mod decision/count generations, all standalone language files and inactive notification files are separately hashed. The standalone has five categories; the bundle has four. The eight standalone translations each contain a tributary label and tooltip. Existing UTF-8 BOM is retained. The original extra protection filter and public IDs are policy, not an inferred engine defect.

The previous five central Vanilla hashes and launcher metadata matched the recorded baseline. This supplement also captures paths absent from the original per-mod closure, notably puppet action registration and the influence value; absence in that closure was a discovery gap, not evidence that those files changed. Existing global indexes are not rebased.

Internet exploration on this date found no version-specific developer explanation settling query/dispatch initialization. Direct requests to [official Effects](https://ck3.paradoxwikis.com/Effects), [Triggers](https://ck3.paradoxwikis.com/Triggers) and [Interactions](https://ck3.paradoxwikis.com/Interactions_modding) returned HTTP 401. Search results from the previously referenced wiki mirror repeat historical declarations; they are not used to establish a new engine contract. Search failure does not prove that no further explanation exists.

## Complete exported command declarations

Retained local exports are primary evidence for this installed build. [Effects export](../runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw):2654–2667 describes `run_interaction`:

    interaction = interaction_key
    redirect = [yes|no]
    actor = character_actor
    recipient = character_actor
    secondary_actor = character_secondary_actor
    secondary_recipient = character_secondary_recipient
    execute_threshold = accept/maybe/decline
    send_threshold = accept/maybe/decline

Actor and recipient must be defined. Secondary actor/recipient are optional. Redirect defaults to yes and only works if secondary actor and secondary recipient are not set up or are invalid. At least one threshold is required. `execute_threshold` immediately executes if the AI response reaches the threshold; `send_threshold` sends if it reaches the threshold. Supported scopes are exported as `none`; that label does not establish arbitrary calling contexts or scope propagation. The raw export misspells the secondary-character metavariables; the normalized spelling above changes no argument key.

[Triggers export](../runtime-evidence/20261003T005950.086458Z/script-docs/triggers.log.raw):5167–5179 describes the availability/potential-acceptance query:

    is_character_interaction_potentially_accepted = {
        recipient = character
        interaction = interaction_name
        secondary_actor = character
        secondary_recipient = character
        target_title = title
        required_response = yes/maybe
        ai_accept = min acceptance value
    }

The export explicitly labels the last five fields optional; supported scope is `character`. It does **not** specify the default `required_response`, default acceptance cutoff, initialization of puppet scopes, selected send options, full validity/cooldown/pending checks, or evaluation order. The mod omits all five optional fields. Do not equate omission with `decline`, and do not infer that every manually sendable refusal is counted.

The same export at 5190–5196 describes `is_character_interaction_valid` as valid, shown and usable, supported scope `character`:

    is_character_interaction_valid = {
        recipient = character
        interaction = interaction_name
    }

The current mod does not call this trigger. Its existence does not justify adding it or replacing the existing query without resolving the feature's context and acceptance policy.

## Category routes and context

Let A be the decision ROOT/requester and C the current candidate. In each query the mod enters `root`, so `prev` at that exact query is C. Dispatch supplies `actor = root`, `recipient = this`, `send_threshold = decline`, with no execute threshold. This is textual caller binding, not proof of engine-created named scopes.

| Selected category | Enumeration / extra mod policy | Native route and pairwise visibility |
|---|---|---|
| Direct vassals | `every_vassal`; excludes `religiously_protected` contracts | Vassal ruler interaction: C is AI and ruler; A is liege-or-above or overlord; different faith |
| Indirect vassals | `every_vassal_or_below`; C has liege, liege != A; same stronger protection exclusion | Same native vassal route; no automatic relaxation of indirect protection |
| Tributaries | `every_tributary`; no extra contract filter | Same native vassal route; C must still be AI ruler |
| Courtiers | `every_courtier` | Courtier route: C courtier of A, non-ruler, not imprisoned, different faith |
| House | A's `house`, `every_house_member`; missing house guarded | House route: effective actor is house head; C is a ruler; same house or permitted house bloc; excludes C who is ruler and vassal under effective actor |

The house iterator does not enumerate a confederation. Native bloc eligibility does not enlarge the mod's enumeration. House members who are also courtiers or vassals are not automatically queried with another category's interaction. Vassal player rulers are excluded by the selected native vassal route; the separate `demand_conversion_player_ruler_interaction` is not dispatched by this mod. Preserve these facts when defining tests; do not silently add new routes.

Native shared eligibility rejects recipient hooks over effective actor, devoted/order-member recipients, imprisonment by effective actor, war with effective actor, religious heads, direct-liege protected contracts, recorded non-conversion promises and the effective actor's diarch. Landless-adventurer court conversion requires the appropriate shrine/camp parameter. The nomadic gate is the literal NAND of `nomadic_philosophy` and `zealous`; do not replace its meaning with a looser prose summary. The vassal route adds the domicile/steppe incompatibility and puppet influence-affordability branch.

All three native routes declare a **15-year recipient cooldown**. The general interaction reference defaults pending-interaction bypass to no. Whether the script query/dispatch actually applies these hardcoded restrictions, and at which stage, remains G02 below.

Counts describe candidates passing the current mod query, not guaranteed acceptance, number of converted relatives, or verified successful deliveries. At unchanged state, count and loop should select the same query-positive candidate set. At changed state, execution must use the new state; a historical display is not required to equal a later count. The existing loops query again before dispatch. The option controller and `if/else_if` chain describe single-category selection, but actual UI behavior remains untested.

## Response and consequence chains

### Courtier and house

Courtier `on_accept` -> `demand_conversion_interaction_effect` -> family selection -> `false_conversion.0900` -> 1000/1010 -> `convert_family_to_faith_effect`. It also performs native notifications, conditional hook consumption, clan unity, state-faith piety, struggle rewards and personal/core tenet effects. Refusal performs native opinion/toast and unity/state-faith effects.

House acceptance follows the same conversion helper and emits `char_interaction.0181`; refusal invokes the cadet-branch decision, native opinions, `char_interaction.0182`, unity and state-faith effects. Hook and influence choices stay native. The cadet branch path requires native decision availability/execution behavior; an observed call alone is not a guaranteed successful branch creation.

### Vassal and tributary

`on_send` calls `pam_tax_nonbelievers_conversion_concession_effect`. `on_accept` emits `religious_interaction.2002`, calls `demand_conversion_vassal_ruler_interaction_effect`, then unity/state-faith/struggle/tenet effects. The wrapper calls the common conversion helper, records conditional `convert_capital`, conditionally consumes a hook and adds the demand opinion. Event 2002's conversion helper invocation is under `show_as_tooltip`; it is not a second executing conversion.

`on_decline` chooses a conditional-acceptance group (base weight 80, disabled for heresiarchs) or full refusal (base weight 20, further modifiers apply). Inside conditional acceptance, gold/favor/study base weights are 10/50/40 with their own guards and modifiers. These are **weights, not fixed probabilities**.

| Event path | Executing result / actual binding |
|---|---|
| 2011 gold demand | Requester accepts -> `pay_treasury_or_gold` to `scope:recipient`, amount `demand_conversion_bribe_size`, then common conversion. Refuse and hook alternatives remain available |
| 2012 favor demand | Requester accepts -> recipient receives `favor_hook` over event ROOT if absent, then common conversion. Refuse and hook alternatives remain available |
| 2015 study demand | Requester permits study -> recipient starts `study_faith` targeting `scope:puppet_or_actor`, stores `pending_conversion_to_liege` = effective actor for 10 years, schedules 2016 after one day |
| 2003 full refusal | Native opinions, possible crime/hook paths and state-faith refusal piety; no direct faith assignment by the mod |

The study scheme saves `owner` and `target`, invokes success/failure on actions with owner scope, and those schedule 0100 after two days when appropriate. 0100 restores `actor` from the pending variable and saves self as `recipient`; only a living actor and a current `is_vassal_of` relationship advance to 0101, otherwise the obligation is removed. 0110 applies similar relationship checks for partial study failure; 0111 offers conversion, further study or broken promise. 0101/0111 use common conversion and report through 0102/0103. The `is_vassal_of` requirement is especially relevant for initial indirect-vassal and tributary requests: **test and document native outcomes rather than patching Vanilla or promising identical completion across categories**.

### Fallback, costs and macro binding

`demand_conversion_interaction_effect`, family selection and family conversion each contain a missing-scope fallback: `scope:actor = { save_scope_as = puppet_or_actor }`. This is inside effects reached after acceptance, not the earlier shared eligibility/AI acceptance blocks. It cannot certify G01. Even the courtier entry point's shared trigger and default AI modifier use `puppet_or_actor`, although much of the interaction uses `actor` explicitly.

| Actual caller / helper | Binding or conditional behavior |
|---|---|
| Celestial acceptance modifier | Courtier: `ACTOR = scope:actor`; house/vassal: `ACTOR = scope:puppet_or_actor`; all: `RECIPIENT = scope:recipient` |
| Crime helper | `CHARACTER = scope:recipient`; caller is effective actor, or actor in courtier-specific code |
| Family conversion | `FALSE_CONVERSION = no` for actual conversion choice, `yes` for secret-faith choice; `FORCED = yes` in both native demand paths. Native helper label does not mean the mod bypassed the original interaction consent |
| Rite conversion | `RITE = scope:conversion_rite` when present, otherwise `scope:puppet_or_actor.rite`; executed on each selected converter |
| Clan unity helper | `CHARACTER = scope:puppet_or_actor`, `TARGET = scope:recipient`, `REVERSE_NON_HOUSE_TARGET = no`; acceptance uses minor gain or medium loss, refusal medium loss or minor gain according to house majority faith (>= 0.6) |
| Puppeteer outcome notifier | Guards actor/effective actor existence, puppet flag and actor != recipient; `TYPE`/`TITLE` supplied by the exact notification event, not substituted with new messages |
| Influence value | Base 0, adds effective actor's `medium_influence_value` only when `scope:influence_send_option = yes`; puppet cost block zeroes ordinary charge and acceptance has a separate effective-actor deduction |
| Tax-nonbeliever concession | Only when its own option flag is yes, effective actor pays recipient `medium_gold_value` on send. Separate from later 2011's requested bribe |

The mod supplies no interaction option flags. `.info` documents options default off when `starts_enabled` is absent; hook/influence options have no such initializer. The tax concession has a native initializer involving AI actor and affordability. **These UI/default declarations do not settle how `run_interaction` constructs options**, so no free-cost or auto-hook guarantee is made. Test explicit resource balances and flags.

Native conversion may collect recipient, eligible spouses, and eligible family at a ruler's court. The false-conversion event may preserve old faith secretly. Rite knowledge <0.6, <0.8, and >=0.8 selects different piety/stress/modifier branches in `convert_to_rite_with_consequences_effect`; the <0.6 branch additionally checks absence of `convert_at_war`. New rite assignment, five-year flags/modifiers, baptism conditions, mandala reward, clan unity, state-faith piety and tenet benefits belong to native chains. Their primitive callbacks, scope lifetimes and cross-request list isolation are not proven by lexical discovery. The state-faith helper really adds **piety**, despite old comments referring to influence.

## Remaining gates and what can close them

| Gate | Exact unknown | Required evidence |
|---|---|---|
| G01 initialization | Effective actor, puppet flag and option/context creation separately for query and dispatch; fallback timing | Version-specific developer/engine contract if obtainable plus matched manual/script native conversion probes. Never synthesize scopes from guesses |
| G02 eligibility/response | Omitted query response default; shown/valid/failure-only/can-send, cooldown, pending block, range and options included at each stage | Explicit declaration or controlled probes of each condition. Refusal cases must compare query result separately from send threshold |
| G03 consequences/lifecycle | Native callback propagation, family-list isolation across mass requests, capital flag, delayed study completion and invalidation | Finish semantic expansion of relevant discovered helpers, callback contracts and matched native runtime outcomes; save/reload cases |
| G04 UI/count | Script-value requester context, category selection, state changes and delivery accounting | UI/count/send probes at unchanged and changed snapshots, each category independently |
| G05 multiplayer | Actor/recipient routing, pending replies and delayed results with two simultaneous actors | Actual two-player run and save/reload; logs and state deltas |

The declared core routes, explicit macro bindings above, effect fallback and cost guards are source-confirmed. The literal closure is reproducible but includes shared-helper branches beyond conversion; unreviewed dynamic/engine dependencies remain discoverable research, not completed audit. No full Vanilla-audit closure, implementation approval, or supported-version promotion follows. General A/B/C fixture success cannot close G01–G03 for native conversion. See the [native test matrix](mass-demand-conversion-tests.md).

## Validation boundary

The [supplemental verification report](../evidence/mass-conversion-verification-20261003.json) records document links/encoding/status consistency and preservation separately from historical reports. Run the collector with `--check` to compare recorded source/export/mod and non-Documentation hashes, object boundaries and exported spans without launching the game. Link/encoding checks establish document consistency only. Historical baseline differences such as the previously recorded AGENTS.md change remain historical findings; do not erase them. Gameplay, GUI, external Tiger validation and multiplayer remain **not run**.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.
