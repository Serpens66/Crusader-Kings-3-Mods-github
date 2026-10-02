# Vanilla audit findings and evidence boundaries

Research date: 2026-10-03. Installation: `E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III`. Sources are the as-installed files; Steam integrity was not verified and compiled source code is unavailable. “Native/Vanilla” here identifies the installation source tree, not a certification of byte identity with a clean Steam download.

## Version and method

`launcher/launcher-settings.json` currently declares `version = 1.20.0.3 (Crozier)` and `rawVersion = 1.20.0.3`. The executable's exposed ProductVersion was empty, so it does not independently corroborate that value. User `logs/code_revisions.log` instead records a 1.16.3 branch with 2025 timestamps; this older run is separated from the installation baseline.

[local-index.json](../reference/local-index.json) records source paths, byte hashes, line counts and lexical top-level definitions for 18,710 native text/reference files and 157 workspace text/reference files. It also records 47 strict UTF-8 decoding warnings without changing those files. Entries decoded with replacement characters are unsuitable for exact textual claims until inspected in their original encoding.

[audit-evidence.json](../reference/audit-evidence.json) records complete-file reads of developer references and selected definition/caller sources, plus the literal helper dependency closure: 694 files and 14,797 edges in this run. It contains hashes and dependency paths, not copies of the full game. This lexical discovery can overinclude names and miss parameter-generated references. **It is not itself a completed semantic audit of every reachable feature.**

The reviewed contracts below establish the teaching statements actually used. They do not authorize skipping a complete feature audit for a future mod. Missing engine signatures and all runtime-dependent statements remain explicit gaps.

## Reviewed entry-point contracts

| Contract | Native source | Findings used in the handbook |
|---|---|---|
| Decision schema | `common/decisions/_decisions.info:19`, `:204`, `:252`, `:265` | Block picture/reference; visibility/validity distinction; cost versus minimum cost; character-scoped effect |
| Decision AI | Same file `:143`–`:168` | Explicit AI-check setup; goal/interval alternatives; do not infer policy from a single weight |
| Event schema | `events/_events.info:7`, `:12`, `:33`, `:190` | Namespace, default event type/scope, hidden events, trigger/immediate/after/options |
| Event overrides | Same file `:75`–`:84` | Priority mechanism, duplicate-priority errors and hot-reload caveat |
| Interaction availability | `common/character_interactions/_character_interactions.info:562`–`:573`; actual `00_gift.txt:41` | Actor root in `is_available`; deprecated `ai_potential` guidance |
| Interaction pair/outcomes | Same `.info` `:242`–`:262`, `:377`–`:399`; actual `00_gift.txt` | Provided actor/recipient; explicitly scoped mutation and multiple send/response stages |
| Payment form | `common/character_interactions/00_gift.txt:171` | `pay_short_term_gold` with target and gold fields; full engine budget semantics require current command docs/runtime check |
| Child-hook extension | `common/on_action/_on_actions.info:131`–`:149` | Add uniquely named child callbacks; avoid conflicting direct effect/trigger blocks |
| On-action chains | Same file `:122` | Effect chain is separate from listed event chains; setup is not passed automatically |
| Birthday root | `common/on_action/birthday.txt:1`–`:10` | Root is birthday character, after age increased; dispatches child hooks |
| Numeric formulas | `common/script_values/_script_values.info` | Operations in source order, clamps, scope/context requirements, inlining, ranges and lists |
| Macro substitution | `common/scripted_effects/00_accolades_scripted_effects.txt:3072`; `common/scripted_triggers/00_activity_triggers.txt:101` | Parameter placeholders in values/keys/chains; inspect callers and expanded arguments |
| GUI declaration | `common/scripted_guis/00_character.txt:1`; `pam_scripted_guis.txt:2`; `ce1_funeral_scripted_guis.txt:1` | Typed GUI root, condition/action separation |
| GUI dispatch | `gui/interaction_menu_window.gui:372`; `gui/activity_window_widgets/funeral_deceased_selection_button.gui` | Context builder and script action must agree; birth event `birth.9004` traced from native GUI action |
| Timed state | `common/scripted_effects/00_bastard_effects.txt:485`; `common/character_interactions/00_artifact_interactions.txt:204` | Timed `set_variable` syntax observed; generic lifetime/refresh rules not assumed |
| Static modifiers | `common/modifiers/00_activity_feast_modifiers.txt` and attachment callers in evidence closure | Property definitions are separate from effects that attach modifiers |
| Trait tracks/text | `common/traits/_traits.info:19`, `:196`–`:240` | Missing-root fallback, XP tracks and localization; old tier lists are insufficient |
| History | `history/_history.info`; `history/_characters.info:25`–`:30`, `:63`–`:75` | Dated initial-state reader; partial/additive character override and alive/dead effect distinction |
| Travel POI | `common/travel/point_of_interest_types/_travel_point_of_interest_types.info` | Different travelling-character/province callback contracts; local-state restriction |

Ranges above are descriptive evidence locations. Use the original source plus hashes for exact inspection; the scanner does not infer field legality from these line numbers.

## Reviewed larger subsystem boundaries

Culture: general cultural-trait, culture, pillar, tradition and innovation references were inventoried/read; a concrete culture and helper uses were inspected. Religion: religion/faith/rite and doctrine/tenet/holy-site references were read with actual type definitions. History/title references were read together with representative definitions. Building, CB, activity, travel and artifact contracts were inspected with actual samples and literal dependency discovery. Map configuration was read alongside geographical/province references; graphical pipelines were inventoried.

These establish directory/schema orientation and the narrow findings described in the subsystem guide. They do **not** establish a complete new map, activity, religion, scheme, artifact or conquest implementation. Those features need their own full audit of the exact selected capability and consumers.

## Conflicts resolved or left open

| Old/general claim | Local evidence and chosen treatment |
|---|---|
| Individual events cannot be overridden | Current event `.info` provides `id_override_priority`; use its documented caveats |
| History characters always require full-file replacement | Current character-history `.info` provides partial priority override plus additive other entries |
| Faiths should be nested in `common/religion/religions` | Current installation has separate type databases, faith-details blocks and rites; use those actual schemas |
| A root always identifies the player | Current callbacks have character, other-type or no roots; record each contract |
| Interactions never have a root | Overbroad; current `is_available` explicitly has actor root, while other blocks need provided scopes |
| `any_child` can accumulate a script-value number | Developer schematic and dedicated guide differ; use supported `every_`/`ordered_` examples and leave anomalous form unverified |
| Any multi-child `NOT` is conventional negated AND | Wiki summaries differ; handbook uses single-child `NOT` or explicit grouping and requires a current engine check for ambiguous forms |
| Every object database follows the same alphabetical replacement rules | No global contract established; audit the particular loader |
| A graphic mod's historical checksum result remains true | No current general guarantee; verify the actual assets and build |

The developer's activity diary confirms the distinction for optional `?=`: missing left-hand scope comparisons/triggers fail, while effect scope changes skip execution. It does not guarantee the existence of right-hand references or validation of arbitrary list-reader combinations.

## Remaining evidence gaps

No current `effects.log`, `triggers.log`, `event_scopes.log`, `event_targets.log` or complete UI data-type dump was found in the searched game/user trees. OldEnt and Wiki tables are useful discovery sources but do not certify the 1.20.0.3 API. Obtain fresh `script_docs` and `dump_data_types` outputs in an explicitly requested debug session before using an unresolved engine signature.

No engine execution, GUI rendering, external Tiger validation, performance profile, save/reload or multiplayer test has been performed. The examples document those acceptance checks instead of claiming success. This distinction is the required limit of the completed documentation task.
