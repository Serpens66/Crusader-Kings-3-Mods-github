# Native conversion acceptance matrix

Prepared: **2026-10-03**, for installed **1.20.0.3 (Crozier)**. All cases: **not run**. This is a test specification, not an executable probe or result. Read the [audit and remaining gates](mass-demand-conversion-audit.md) and [common test protocol](../test-protocol.md). The general own-interaction fixtures do not replace these native tests.

## Controlled comparison and recording

Use new test campaigns with only the standalone mod, and a separate playset for the bundle. Keep both alternatives disabled in the other's run. Do not use the Vanilla diagnostic starter for a mod test. Record build/commit/checksum, mod hashes, DLC, language, player/character IDs, category and snapshot save. Capture fresh diagnostics and distinguish pre-existing errors.

For each comparison reload the **same pre-action save** to establish equivalent actor/recipient state. One branch sends the native interaction manually, another records the mod's current query and script dispatch. Instrumentation must first be source-audited; no probe implementation or generated scope initialization is supplied here. Log actual option flags, effective actor, pending interaction, recipient cooldown and resource balances. Different random answers across restored branches are not by themselves a mismatch; compare allowed chains/invariants and record random outcome.

Record four separate quantities: displayed candidates at T0; query-positive dispatch attempts at T1; actual deliveries/pending replies at T1; actual converted characters after outcomes. At unchanged state, count and candidate set should match; at changed state, record the removed/added candidates and re-evaluation. Family conversions are outcomes, not additional mod requests. Never infer deliveries solely from loop iterations or a clean log.

For resource changes record both characters' gold/treasury/influence/piety, unity, legitimacy, fulfillment, hooks, faith/rite/secret faith, opinions, modifiers, capital faith and notifications where applicable. Keep pending study and response state through save/reload. Store evidence under Documentation only; do not overwrite raw exports or original result sheets.

## Cases

| ID | Setup / action | Expected observation and gate |
|---|---|---|
| MC-T01 | Direct-vassal category, eligible AI ruler | Compare manual/native and mod query/delivery identity; only this category processed; G01/G02/G04 |
| MC-T02 | Indirect vassal, then protected indirect vassal | Proper indirect membership; stronger mod protection exclusion preserved even where native direct-contract gate differs; G02/G04 |
| MC-T03 | AI ruler tributary; non-ruler/player controls if constructible | Native route's AI/ruler gates observed; no assumption that tributary status alone suffices; G01/G02 |
| MC-T04 | Courtier, then ruler/prisoner/former courtier | Only correct courtier route; shared puppet scope initialized despite actor-oriented entry point; G01/G02 |
| MC-T05 | House-head requester; ruler/non-ruler members, house vassal and bloc-only outsider | Only enumerated house and native-valid route; no automatic bloc expansion or alternate vassal routing; G02/G04 |
| MC-T06 | Missing house, self, same faith, same faith with different rite | No invalid scopes or new category policy; record the native faith-based visibility result; G02/G04 |
| MC-T07 | Manual refusal-capable AI recipient | Query default response/cutoff measured separately; send threshold is not forced acceptance or proof query includes refusals; G02 |
| MC-T08 | Fresh target, 15-year cooldown, existing pending request and rapid repeat | Actual cooldown/pending enforcement for query AND dispatch; no duplicate requests; G02 |
| MC-T09 | Strong recipient hook over actor, devoted/order member, religious head, war, protected direct vassal, promise and diarch | Each shared invalidity condition individually compared with manual native request; G01/G02 |
| MC-T10 | Landless camp without/with shrine; nomadic-philosophy/zealous combinations; domicile/steppe restriction | Literal native guards observed; no invented DLC prerequisite; record unavailable setup as not tested; G02 |
| MC-T11 | Hook/influence/concession available but not manually selected; resource boundary and later balance change | Record script-created option flags, no guessed default selection; conditional native costs/payments attributed to correct stage; G01/G02/G03 |
| MC-T12 | Accepted courtier/house/vassal requests | Correct native conversion route, opinions, unity/state-faith/tenet rewards and messages; no executing duplicate from tooltip-only calls; G03 |
| MC-T13 | Full refusal and house refusal | Native crime/opinion/state-faith outcomes and cadet-branch availability; no direct mod conversion; G03 |
| MC-T14 | Gold, favor and study responses, each accepted/refused; hook alternative where available | Native 2011/2012/2015 paths remain usable; exact transfers/hook direction recorded; weights are not advertised fixed probabilities; G03 |
| MC-T15 | Conversion with spouses/family; secret-faith choice; rite knowledge below/exactly 0.6 and 0.8 | Outcome character set and native rite/piety/stress/modifiers distinguished from request count; G03 |
| MC-T16 | Study success, partial failure, no further learning; save/reload pending step | Two-day native completion routing and subsequent choices/notifications survive correctly; G03 |
| MC-T17 | Study after requester death, changed direct liege, initial indirect vassal or tributary | Record native `is_vassal_of` completion guard and obligation cleanup; do not demand an unsupported universal completion guarantee; G03 |
| MC-T18 | Change faith/relationship/resources while decision is open | T0 display may differ from T1 candidates; no invalid send/charge and execution re-evaluates; G02/G04 |
| MC-T19 | Large court/realm with multiple related candidates and rapid repeats | No cross-request family-list/saved-scope contamination; exact recipients and timing; G03/G04 |
| MC-T20 | All five categories, EN/DE and remaining translation key coverage | Radio selection and count scope correct; no other category executed; eight languages have tributary keys structurally, actual rendering untested; G04 |
| MC-T21 | Two real players act separately and simultaneously; save/reload pending reply/study | Correct per-player identities, costs, notifications and outcomes, no OOS; G05 |
| MC-T22 | Standalone/bundle separate playsets | Record five-versus-four current categories; equal behavior required only for corresponding verified routes. No bundle update implied; G04/G05 |

For probabilistic branches use a naturally occurring recorded outcome or separately audited diagnostic forcing with equivalent preconditions; directly firing an event does not prove dispatch reached that event. A successful menu/export/startup is not a campaign test. Unavailable DLC/government/MP scenarios stay **not tested**, with the coverage limit recorded.

## Blank result record

| Case | Status | Snapshot / actor / recipient | Query / attempt / delivery / conversion counts | Options / costs / messages / diagnostics | Gate closed and remaining limit |
|---|---|---|---|---|---|
| MC-T01–MC-T22 (one row per executed case) | not run | pending | pending | pending | none |

Attach before/after evidence, exact reproduction and clean-baseline comparison to each row. Close only the demonstrated gate/case; a passing own-interaction lab does not close native conversion. Keep failed/unavailable cases visible. Only after required semantic contracts and applicable runtime cases are resolved may a separate mod update and compatibility declaration be considered.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.
