# MC-DISPATCH contract card

## Explicit preview only — 2026-10-05

[Compact-widget patch](../mods/mass-demand-conversion-compact-widget-20261005.md) adds an unconditional custom_tooltip before the five retained send branches. It describes normal requests and subsequent native outcomes; it neither performs nor guarantees conversion. All query/send blocks are unchanged. Runtime count/delivery parity and MP remain open.


## Standalone filter extension — 2026-10-05

[Current implementation/audit and pending tests](../mods/mass-demand-conversion-chance-filter-20261005.md): selected native entry flags choose the unchanged query or native `ai_accept = 80/100`. GUI display state never enters gameplay. Original interaction IDs, actor/recipient bindings and `send_threshold = decline` remain; no forced acceptance, hooks or payment options are introduced. Native defaults are left as in existing/native callers; earlier unresolved initialization/validation contracts are not declared closed. Threshold/UI parity and concurrent MP routing remain untested.


Family: **Mass Demand Conversion**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/mass-demand-conversion.md) · [Behavior guide](../../workspace/function-contracts.md) · [2026-10-03 audit supplement](../mods/mass-demand-conversion-audit.md) · [Native test matrix](../mods/mass-demand-conversion-tests.md)

## Inputs, ownership and order

Decision root is requester; iterator this is candidate; entering root makes candidate available through prev at that caller.
Preview/count and dispatch must use the same category policy. Native query and dispatch initialization need separate tracing.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `run_interaction` | effect | none | [line 2654](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `is_character_interaction_potentially_accepted` | trigger | character | [line 5167](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/triggers.log.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Native actor initialization, consent, cooldown and consequence audit

Source-confirmed: complete exported threshold/redirect syntax, native conditional influence/concession costs and response chains. The common conversion effect has a missing puppet_or_actor fallback to actor, but it occurs after the earlier eligibility/AI query. Engine option initialization, cooldown/pending enforcement, family-list isolation, delayed study and multiplayer remain G01/G02/G03/G05.

Current remaining gate: G01/G02/G03/G05: Engine dispatch/options initialization and validation, actual native consequences and delayed/list/MP lifecycle. Reviewed source routes and standalone actor/recipient/send-threshold bindings are recorded separately; full feature audit unclosed; gameplay/GUI/MP not run.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Mass Demand Conversion` has 12 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](../mods/mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.

## Subsequent static migration review (2026-10-03)

[Reviewed source routes](../mods/mass-demand-conversion-static-migration.md) distinguish effective-actor migration, options/costs, negotiation, family/secret faith, rite consequences and delayed study. The standalone invokes native definitions and does not copy the old conversion implementation. Its five dispatches consistently supply requester/candidate and `send_threshold = decline`, without an execute threshold. No mandatory functional mod patch is demonstrated; the later fallback does not establish earlier Engine initialization. Unchanged cooldown and existing list/context questions are regression coverage, not proven 1.20 defects. Runtime behavior and full audit status remain open.

## Notification update 1.078 — 2026-10-03

[New notification audit and evidence](../mods/mass-demand-conversion-notifications-20261003.md): standalone metadata is now 1.078/1.20.* and its two native acceptance IDs are hidden priority-1 overrides using mdc_conversion_accepted_message. The completed source audit is limited to those notifications, their callers, previews, rewards and puppet notifier. The earlier full query/dispatch/lifecycle/GUI/MP gates remain open and gameplay remains **not run**. Candidate enumeration, all five categories, query/send bindings, option logic and count values are byte-preserved. The four-category bundle and its inactive experiment are untouched; no port is implied. Both native IDs affect all their callers, including manual requests; same-ID mod overrides can conflict. See MC-N01–MC-N11 in the updated test matrix. Historical static-migration and inactivity statements above describe the earlier 1.077 review.
