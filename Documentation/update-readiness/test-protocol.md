# Acceptance tests for later mod updates

This protocol has been prepared but **not executed**. SP and MP with new games are required. Save/reload refers to those new test campaigns; compatibility with pre-update campaigns is not a promised outcome.

## Record every run

Use one row per run with: run ID/date, executed version/checksum, source/package hashes, enabled DLC, language/UI scale, playset and mod order, bookmark/ruler/government, host/client role, test cases, actual deltas, fresh log folder and pass/fail/blocker. Preserve screenshots when UI rendering or routing matters. A menu opening is insufficient evidence for successful execution.

Use statuses **not run**, **passed**, **failed**, **blocked**. A skipped test is not passed. For a numerical outcome record before/after gold, prestige, prestige experience, piety, stress, modifiers, opinions and recipients as applicable. For probabilistic outcomes record the candidate set and diagnostics; a single random injury result cannot establish a 10% probability.

## Static gates before gameplay

1. Establish current source hashes and finish each relevant native feature audit, including initializer/caller context and parameter expansion. Resolve all `Blocked contract` entries before choosing behavior.
2. Verify `.txt`/`.yml` UTF-8 BOM, source encodings, script structure, declared IDs, event namespaces, literal/helper parameters, assets and localization. Do not blanket re-encode unrelated files.
3. Compare each full override against current native content. Verify GUI nested type precedence and preserve unrelated native functionality. Check both copies of shared standalone/bundle logic for intended equality.
4. Optionally run an already available compatible [Tiger](https://github.com/amtep/tiger) against the exact game/mod configuration. Record validator version and assess warnings individually; upstream documents update lag and false positives. No installation is included in this preparation.

The documentation checker does not perform a complete Jomini grammar/type audit or render the GUI. Run it to check documentation/evidence preservation, not to certify mod behavior.

## Playsets

Start with the empty Vanilla baseline from [debug run](debug-run.md). Then test each updated package alone. Excluded Knight Manager roots/test remain disabled. Do not combine bundle with standalone Leave Wars or standalone conversion; do not combine both GFX variants.

After individual success, test these dependency-aware combinations:

| Run | Packages | Purpose |
|---|---|---|
| Standalone utilities | CustomDefines after knight removal + SerpAlerts + Leave Wars + Mass Demand Conversion | Shared event UI, conversion queries and notifications |
| Bundle utilities | CustomDefines after knight removal + SerpAlerts + SerpInteractionsDecisions | Shared alerts/transactions and all bundle features |
| Public graphics | Each passing gameplay playset + GFX-Mod | Current icon/rank/artifact presentation |
| Local graphics | Each passing gameplay playset + GFX-Mod Serp | Larger replacement footprint and map transitions |
| Gender-only graphics | Each passing gameplay playset + Gender Colour | Status icon rendering without competing GFX coloring |

These are proposed certification combinations, not claims they currently work. Any additional personal mod list requires its own conflict inspection. A package failure blocks dependent combination certification.

## Common scenario matrix

| Scenario | Expected invariant |
|---|---|
| Below/exact/above affordability | Preview matches enabled state and charged amount; no hidden debt policy change |
| Self/other/player/AI targets | Exact original policy preserved; no actor/recipient swaps |
| Missing faith/rite/house/council/war target | No invalid scope access or unwanted charge |
| Conditions change while menu/event is open | Execution revalidates; stale targets cause no charged no-op |
| Repeat and overlapping actions | No duplicate charges/rewards, stale scopes or unintended persistent lists |
| Delayed event, actor/recipient death, court/government change | Owner/target policy follows audited contract; no reward to wrong character |
| New-game save/reload before/after execution | State and pending work survive or expire according to documented policy |
| Current governments and highest available title tier | No obsolete cap or accidental exclusion of a valid existing purpose |
| DLC enabled/disabled where available | Native availability/consequences respected; unavailable feature stays unavailable |
| EN/DE and fallback language | No missing localization, broken markup or misleading costs |
| Fresh start and reload | Cold-start loader behavior tested; hot reload alone does not count |

Each sheet adds precise source-derived amounts and feature scenarios. No generic “test passed” entry replaces them.

## Multiplayer

Use two real players and consistent executable, DLC/session configuration and required gameplay mods. Record host/client checksum and connection results; do not assume a graphical package is checksum-neutral from old comments.

Exercise separate and simultaneous actor actions, exact sender/recipient transfers, target invalidation, delayed education, war withdrawal and notification delivery. Save/reload the new MP campaign and test hotjoin if supported by the session. Record OOS/desync, hotjoin and relevant multiplayer logs. The agent cannot certify a two-player scenario without actual participants/results.

## Release gates

For each package, all required static/feature tests must pass or an explicitly accepted compatibility limit must be stated. Update supported-version metadata only after that package's result, preserving Workshop/public identities. Keep the fuller local GFX distribution local. Publishing or uploading is not part of this task.

For a failed case, preserve the failing logs and exact source hashes, identify the causal mod/Vanilla entry point, repeat the feature audit if new evidence changes its contract, then rerun the failing case plus affected regressions. Do not repeatedly broaden tests after success without a new reason.
