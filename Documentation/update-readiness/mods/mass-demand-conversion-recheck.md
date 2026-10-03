# Mass Demand Conversion: caller and Internet recheck

Date: **2026-10-03**, subsequent to the initial supplement; installed **1.20.0.3 (Crozier)**. No gameplay tests. This refines the [source audit](mass-demand-conversion-audit.md), without closing the full feature audit or certifying compatibility. [Follow-up evidence](../evidence/mass-conversion-recheck-20261003.json) preserves current source hashes and the searched native callsite inventory separately from earlier evidence.

## Results

The earlier Internet search was incomplete. A current official developer explanation and additional native callers answer part of the context questions. General interaction context, supported caller patterns and threshold syntax should no longer be described as wholly unknown. Exact script-command initialization, defaults and hardcoded validation stages remain narrower unresolved questions.

### Official developer explanation

Paradox's **By God Alone Dev Diary #8 - (Truly) Everything Else**, published **2026-09-29**, is accessible through the [official Steam announcement feed](https://store.steampowered.com/news/posts/?appids=1158310&feed=steam_community_announcements), Puppet / Interactions section. It explains that interaction actor always exists; for puppet interactions it refers to the puppeteer. The effective character is accessed with `scope:puppet_or_actor`. Actor-root blocks, including `is_available`, remain actor-based; `scope:is_puppet_action ?= yes` distinguishes puppet actions. It also confirms that native interactions were migrated even when not registered as vanilla puppet actions, and that some special interactions need engine support.

This is a developer-documented **interaction** contract. The passage does not explicitly specify the internal construction sequence for `is_character_interaction_potentially_accepted` or `run_interaction`, option defaults, or their validation stages. It therefore resolves the general meaning of the scopes, while leaving script-entry details to the narrower G01 probes. The old observation that a late fallback alone cannot prove early initialization remains correct.

### Current native callers

All paths below are relative to the installed `game` directory. Line numbers and whole-file hashes are retained in the follow-up evidence. These are source examples and comments, not successful runtime observations.

| Native source | Concrete finding | Evidence limit |
|---|---|---|
| `common/important_actions/00_personal_actions.txt:147` | Ransom candidate query enters `root` and supplies `recipient = prev`, just like MDC's query binding | Confirms an intentional native caller pattern; not conversion-specific validation |
| `common/script_values/tutorial_values.txt:105` | Query runs inside a script value using the current character and an explicit recipient | Script-value query use itself is not unsupported; MDC's displayed counts still need verification |
| `common/scripted_triggers/pam_scripted_triggers.txt:1948–2028` | Sway-to-Rite `can_send` helper enters `$ARCHBISHOP$`, supplies `$TARGET$` and omits optional query parameters. The parallel acceptance helper adds `ai_accept = $ACCEPT$`; its comment explicitly describes this additional threshold | Strong evidence of native intent to distinguish sendability from acceptance percentage; no numeric default or internal stage order is stated |
| `common/customizable_localization/pam_sway_to_rite_custom_loc.txt:1–109` | Actual binding is `ARCHBISHOP = root`, `TARGET = scope:second`; thresholds descend from 90. The source comment distinguishes CanSend-blocked targets from 0% acceptance | Do not universally equate an omitted threshold with certain acceptance or exclusion of every refusal; do not turn comments into an undocumented universal Engine rule |
| `common/important_actions/pam_actions.txt:1272` | The same helper is called before creating an important action, with `ARCHBISHOP = root`, `TARGET = scope:sway_to_rite_target` | This is outside a currently opened interaction; named interaction scopes are not explicitly manufactured at this callsite |
| `common/character_interactions/pam_interactions.txt:2988` | The queried courtier Sway-to-Rite interaction immediately uses `puppet_or_actor` in visibility and validity, before acceptance | Together with its callers, supports intended early effective-actor availability; does not prove MDC runtime initialization |
| `common/scripted_effects/10_dlc_tgp_scripted_effects.txt:451,473,495,517` | Non-AI disciples receive movement-switch requests via `run_interaction`, explicit actor/recipient and `send_threshold = decline`; AI disciples take a different direct branch | Native use agrees with the exported send/execute distinction; no forced acceptance follows from the send threshold |
| `events/dlc/ep3/ep3_interactions_events.txt:3099` | Imprisonment dispatch uses `send_threshold = decline` following an explicit validity query | Caller checks cannot establish which checks dispatch itself repeats |
| `events/dlc/ep3/ep3_roman_restoration_events.txt:102,173` | Native mass conversion loops call `ask_for_conversion_interaction` with `execute_threshold = accept` | This is a different interaction and immediate-execution policy from MDC; it is not a verified replacement route |
| `common/important_actions/00_diarchy_actions.txt:1–78` | Native code separates `is_character_interaction_valid` from potentially-accepted queries with explicit `required_response = maybe` | Both triggers have distinct intended roles; no proof that either subsumes every cooldown/pending/range check |

The local query export declares a character scope. Current native Sway-to-Rite callers bind that scope to the intended requester without explicitly creating actor/puppet scopes first. Combined with the developer explanation, this is positive evidence of intended Engine-managed interaction context. A blanket claim that a mod must synthesize these named scopes is unsupported. Do not implement such a workaround from uncertainty alone.

### Further Internet search

Exact searches covered both commands, `required_response`, `send_threshold`, cooldown and puppet context. The supplied [jesec effects mirror](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Effects_list.md) repeats the threshold declaration; its [trigger mirror](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Triggers_list.md) has an older abbreviated signature. Neither supplies the missing defaults or stage ordering. Mirrors are discovery aids; the installed exports remain the versioned source.

The [Tiger trigger validator source](https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/triggers.rs.html) lists the optional response/acceptance parameters. This is primary evidence for Tiger's validator schema, not CK3 Engine runtime behavior. No newly located guide establishes the omitted response default, script-created option selection or complete cooldown/pending validation contract. Failure to locate such a guide does not prove none exists. The earlier HTTP 401 Wiki results remain historical retrieval failures, not a negative finding about Internet knowledge.

## Historical comparison supplement, 2026-10-03

The [new 1.19.0.6→1.20.0.3 comparison](../../research/vanilla-history-20261003.md) now establishes the historical actor-to-effective-actor migration and records original file hashes and selected definition spans. All 295 current source paths in the existing feature seed match the installed 1.20.0.3 byte-for-byte. This closes the historical-snapshot availability gap; it does not close G01–G04 or certify an exhaustive dynamic dependency comparison. The earlier findings above and runtime matrix remain intact.

## Narrowed remaining questions

- **G01:** Check early effective actor and option flags for these three native conversion routes separately in query and dispatch. General actor/puppet terminology and intended native caller context are now sourced; do not spend tests rediscovering those definitions.
- **G02:** Determine omitted `required_response` behavior and whether query and dispatch enforce cooldown, pending requests, range and each relevant validity stage. Prioritize refusal-capable candidates and the actual query/send mismatch. The native CanSend/percentage split is evidence against asserting an acceptance-only default without proof.
- **G03:** Retain native family-list isolation, delayed study and option-dependent consequence questions. Other interactions' caller examples do not answer them.
- **G04:** Query use in a script value is source-confirmed. Verify MDC's requester/recipient binding, displayed candidates and later delivery in the actual decision; changed state may change the count.
- **G05:** Multiplayer routing and save/reload behavior still require actual runtime evidence.

Use [MC-T07, MC-T08 and MC-T11](mass-demand-conversion-tests.md) as the first focused probes of defaults, hardcoded restrictions and options, alongside a matched single-recipient context probe. These refine the research order; all existing test cases remain **not run**. The complete source audit, subsequent code changes and compatibility release are separate milestones.
