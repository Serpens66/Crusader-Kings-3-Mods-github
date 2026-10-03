# Documentation readiness against the existing mods

Review date: **2026-10-03**. Target evidence: local **1.20.0.3 (Crozier)** sources plus the two user-executed export runs. **Verdict: the collection is a strong foundation for understanding, design and source-informed prototypes, but does not yet fully explain all engine-dependent behavior or establish that similar new mods work.**

## What was checked

All eleven existing mod/content roots were included in the review, including the excluded Knight Manager variants and `test`. The review read **149 text/code files** in those roots, revisited the purpose and update sheets, inspected command retrieval and examples, verified hashes of all **11 captured engine-export files**, and consulted complete relevant native developer references. Asset inventories and earlier consumer findings were considered; no new rendering or gameplay test occurred. File reads and lexical indexing are not claimed as a completed semantic audit of every function. [Machine evidence](documentation-readiness.json) records roots, hashes, status counts and boundaries.

The existing update matrix groups retained functions into **43 packages**, with eight recorded as `plan ready` and 35 carrying conditions or blockers. Those are the preparation sheets' unreconciled statuses, not a new assessment that 35 features necessarily remain blocked after the exports. The current exports make several signature questions answerable locally; the corresponding comparisons have not yet been authored.

## Adequacy by task

| Task | Current adequacy | What remains |
|---|---|---|
| Understand syntax, file layout and common patterns | Good foundation | Engine-specific details still require exact contracts; the teaching fixtures are untested |
| Understand each retained mod's purpose and major flows | Largely covered | Not every branch, helper expansion and state transition has a complete behavioral explanation |
| Write a small new decision or immediate interaction | Enough to design and draft with a native feature audit | Scope/cost/static checks and actual execution still required before calling it functional |
| Write a complex mod similar to the bundles/alerts | Incomplete as a self-contained reference | Exact query/dispatch, lifetime, callback, synchronization and side-effect contracts |
| Rebuild or extend current GUI/graphics packages | Incomplete | Current binding arguments, actual window integration, loader/frame mapping and render results |
| Claim full SP/MP compatibility | Insufficient evidence | New-game, save/load, invalidation, simultaneous use and combination tests |

## Concrete gaps

### 1. Current exports are present but not integrated

[Runtime intake](../update-readiness/runtime-intake.md) verifies six script-reference exports and five datatype exports. However, [GUI guidance](../systems/localization-and-gui.md) still says no current local dump was found; [coverage](coverage.md) still lists a missing scope/target dump; the main README's broad no-engine-execution statement predates the diagnostics. Statements that examples and mod-feature tests were not executed remain valid and must be kept distinct from successful export runs.

[Command reference](../reference/commands.md) remains a discovery table with observed uses rather than an indexed current contract catalogue. `Documentation/tools/lookup.py` searches the native/mod definition index and observed symbols, not the newly generated engine exports. It therefore does not yet expose export descriptions, supported scopes/targets, parameters, return types and provenance together.

A minimum completion step is a versioned export index linked from command lookup and the handbook, followed by explicit reconciliation of each affected feature-sheet gate. Preserve original raw dumps and distinguish what an export states from what only callers or runtime tests can establish. Some GUI entries show `Arg0`/`Arg1` without detailed argument types; importing those entries cannot invent missing types, optionality or permissions.

Concrete observation: CustomDefines `gui/11_multiplayer_types.gui:38` invokes `TryStartRulerDesigning` with one argument. The current datatype export lists `TryStartRulerDesigning( Arg0, Arg1 )`; current native `gui/multiplayer_types.gui` callers at 1926, 1975 and 2024 pass a character plus a character-type selector. This is an unresolved call-contract comparison, not proof that an omitted argument is rejected. Post-start permission and multiplayer behavior remain separate questions. The native file was read in full for this comparison; no implementation change is proposed from guessed defaults.

### 2. Feature behavior is not fully reduced to explicit contracts

| Mod family | Existing useful material | Missing for complete understanding/reuse |
|---|---|---|
| CustomDefines | All 23 keys, current differences, GUI targets, removal surface | Exact nested GUI loading, designer permissions, current tooltip bindings and rendered numerical behavior |
| Mass Demand Conversion | Categories, standalone/bundle differences, count/dispatch intent | End-to-end actor/recipient/redirect setup, query versus dispatch agreement, response/cooldown/side effects and duplicate targets |
| Leave Wars | Ten-slot selector, original numeric policies, file dependencies | Saved-war flow across events, selection-time invalidation, cleanup, exact payment/experience consequences and messages |
| SerpAlerts | Eight actions, four active subscriptions and intended recipient sets | Complete callback/state map, optional targets, receiver uniqueness, overlap with native messages and UI-only versus synchronized execution |
| SerpInteractionsDecisions | Resource menus, costs, study timelines, hook/money/religion purposes | Per-branch state transitions, exactly-once education, death/expiry/save behavior, current religious authority and exact transactions |
| Gender Colour / both GFX packages | All 677 texture footprints and consumer candidates | Proven frame/consumer mapping, unresolved alternate assets, container acceptance, export recipe and actual render results |
| Knight Manager variants / test | Orientation, owner-state pattern and overlap risks | Per-preference explanations, helper/caller graph, current knight contract and portable UI packaging; Continued has no actual `.gui` file in its root |

The Knight Manager roots remain excluded from updates. Including their documentation limitations here does not authorize updating them or imply that excluding updates makes their understanding complete.

A complete reusable feature note should specify its input/optional scopes, actor and state owner, initializer/caller, expanded helper parameters, guards, costs, effects, outputs, delayed transitions, cleanup, localization and rendering context. It should link current native definitions/callers/dependencies and state which engine gaps remain. Literal dependency closure is a navigation aid rather than this complete behavioral model.

### 3. Practical examples are not proven working templates

[Examples](../examples/README.md) include decisions, a short event chain, an immediate transfer, a birthday subscriber and shared helpers. They have structural/source checks but no recorded CK3 execution. The GUI sample is explicitly an insertion fragment, not a standalone complete current-window integration.

There is no runtime-verified teaching template matching all of the difficult workspace patterns: bulk native requests with preview/count parity, delayed reward with invalidation and exactly-once state, per-player optional-target notifications, or a current GUI click with correct scoped execution and multiplayer routing. These should be developed after their exact native audits and tested before being promoted to working recipes. Existing old mod code should not be treated as the substitute for such a recipe.

### 4. Runtime gaps cannot be eliminated by adding prose

The successful diagnostic establishes export production and normal main-menu exit. It does not execute a mod feature. The first automatic-run crash remains unexplained; retained AGOT/profile diagnostics also prevent describing the baseline as an error-free clean profile.

Saved scopes, expired/dead targets, repeated actions, numerical deltas, rendering, new save/load and two-player routing still need the [acceptance protocol](../update-readiness/test-protocol.md). Static validation is supplementary; compatible Tiger availability/support is not established here. No tool installation or game launch was performed by this review.

## Recommended completion order

1. **Integrate and reconcile the evidence already available:** versioned engine/API and datatype index, lookup links, obsolete availability statements, per-feature signature comparisons. No additional user game run is needed merely to read existing exports.
2. **Document the exact reusable feature contracts:** conversion/query routing, war selector lifecycle, delayed education, notifications, transactions and current GUI context. Follow current full native definitions, callers, helper expansion and dependencies; leave unproven behavior explicit.
3. **Create and verify representative working recipes:** prioritize immediate transaction, bulk query/dispatch, delayed state, callback notification and current GUI integration. Carry each example through actual display/execution and relevant invalidation/save/MP cases.
4. **Close graphics and package-specific gaps:** only the consumer/frame/container/render questions required by the chosen similar mod; preserve variant/publication boundaries. A map/audio tutorial is not a priority for the current mod family.

Completion means every function in the chosen family has a sourced behavioral contract or a specific remaining engine/test blocker, and every recipe advertised as working has actual acceptance results. It does not mean documenting all CK3 systems or claiming that documentation can guarantee any future feature without its own audit and tests.

## Resolution supplement after export integration

The earlier assessment is retained as history. Engine indexing, lookup integration, separate 43-feature declaration cards, owner/state narratives, Knight learning material and isolated payment/callback/GUI-frame probes have now been added. See [completion report](completion-report.md). Source-informed packages and concrete remaining blockers replace broad claims of missing work; they do not establish functioning gameplay templates. Full transitive semantic audits remain bounded by the gates in each card; no lexical closure is promoted into a complete audit.
