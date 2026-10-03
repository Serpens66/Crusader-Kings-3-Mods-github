# Three bundled user test runs

Status: **not run**. These are private probes; none is certified functional. No tool starts CK3, changes your playset, or operates input. The old Vanilla diagnostic starter disables mods and must **not** be used for these fixture runs.

## One-time registration and safe selection

1. Close CK3 and its launcher; leave Steam available. Record/screenshot your original selected playset. Preserve any existing identically named external descriptor rather than overwriting it.
2. In Explorer open `Documentation/examples/registration`. Copy only `doclab_demo.mod`, `doclab_gameplay.mod`, `doclab_gui.mod` into `C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III\mod`. Their content paths already point to this workspace. Moving the workspace requires updating those descriptor paths first. No original mod files are copied or edited.
3. In the Paradox launcher create a separate test playset. Run A enables **Documentation demonstration** and **Documentation Contract Lab** only. Run B adds **Documentation GUI Frame Lab** after its gameplay dependency. Keep all existing mods disabled in these playsets. Do not combine original standalone/bundled variants for this test.
4. Enable debug mode through your normal launch configuration. Do not use `-run_console_action` or automatic quit. Start a **new**, uncompressed test campaign with a living adult landed ruler and adult courtiers. Record build/version, checksum, enabled DLC, language, UI scale, date and host/client role. Use English or German; German teaching text deliberately falls back to English.
5. If needed open the debug console with the key under Esc (usually `^`/`°` on German keyboards or backtick on English keyboards; layouts can differ). Only use console adjustments in a disposable single-player test to establish balances/death/timing. Confirm the command's current help before invoking it. MP tests should use normal entry points.
6. Before and after each run use the [read-only log collector](../tools/capture_fixture_logs.py) described below, or preserve timestamped logs manually under Documentation. At the end select your original playset and restore your original launch options. The prepared examples do not alter `dlc_load.json` themselves. Keep the test descriptors for repeat tests or remove only your three added copies later.

The launcher may display source/schema problems immediately; record them before proceeding. A failed load is a test result, not a reason to suppress the error. Known AGOT/profile and pre-existing localization warnings must remain visible and be compared to baseline, not blamed on these examples without evidence.

## Run A — gameplay fixtures

Pause while inspecting balances so income does not obscure exact deltas. Use the original teaching transfer for direct single-target transaction, then the Contract Lab batch for query/dispatch. Record actor/recipient character IDs.

| Case | Action | Required observation |
|---|---|---|
| A01 | Direct five-gold transfer at balances 4, 5, 6 to a living distinct in-range target | At 4 unavailable; at 5 and 6 exactly actor −5, recipient +5, once; no gift opinion added by fixture |
| A02 | Self, dead/child recipient and UI state changed before execution | Self/dead excluded; Contract Lab excludes children, original demo has no child exclusion and uses diplomatic range; execution guards must prevent charge after invalidation |
| A03 | Batch with zero, one, several eligible adult courtiers | Display count N and cost 5N; unchanged candidate set yields exactly N transfers and total payer −5N |
| A04 | Exact total balance and one below; rapid repeat after loss of funds | No partial unaffordable execution; counts/price refresh; execution agrees with guard |
| A05 | Manual notification, spouse present/absent | Exactly one feed entry to actor player per invocation; absent portrait yields no missing-scope error; spouse receives no extra message |
| A06 | Natural birthday for human and AI | One human callback entry, zero AI fixture messages; original birthday effects remain |
| A07 | `doc_demo_decision`, then second request before next day | Pending excludes repeat; exactly +2 once after delivery, marker consumed |
| A08 | Save/reload while pending; payer/target death or missing saved requester | No extra reward; invalid branch no reward; report whether cleanup/expiry works |
| A09 | Force completion with missing requester / after completion / after marker expiry | No reward without valid matching state; record stale-event behavior separately |
| A10 | Old completion delayed into a later request | **Blocked instrumentation/design case:** boolean marker has no generation identity. A console event without original saved context is not a valid reproduction; retaining a stale chain requires an audited injection. Do not certify cross-generation exactly once |

The old event chain is a scope-propagation/marker probe, not the final robust exactly-once recipe. Its 30-day expiry is a fallback; it does not guarantee explicit cleanup on every death or dispatch failure. Real education's 365/366/367 timing needs its own mod test after implementation and cannot be certified by this short probe.

## Run B — GUI and graphics

Use the same gameplay packages plus GUI Frame Lab in a new disposable save. First verify that the panel actually appears. If absent, stop the GUI cases and preserve logs; registration or parsing is a concrete blocker.

| Case | Action | Required observation |
|---|---|---|
| B01 | Inspect panel and native windows | Own panel, readable labels and all native windows; no accidental replacement |
| B02 | Click valid button once and twice | Exactly +2 per click to player root, matching shown/valid scope; no other character changes |
| B03 | Inspect rank rows, columns 1–7 | Record each frame for native/public/local, including blanks, cropping and out-of-range behavior; no inferred tier meaning |
| B04 | Inspect PNG-under-dds icons | Record whether all three render, dimensions/ratio and any engine container error |
| B05 | Alternate UI scale; save/load and player succession | Layout usable, root switches to actual current player, repeated clicks remain correct |

Record screenshots yourself if useful. This agent will not take control of the mouse/keyboard. Production consumer/mask validation remains separate from this raw-frame panel.

## Run C — two human players

Both machines need the same CK3 build, DLC setup where relevant, identical fixture files and identical selected package list. Register each machine's external descriptors with its own workspace paths. Use a fresh MP campaign and normal in-game interactions; do not mix in old mods or debug-only state changes. Debug MP availability itself is an environment gate: record a launch restriction rather than guessing a bypass.

| Case | Action | Required observation |
|---|---|---|
| C01 | Each player sends 5 gold, then both send independently | Correct payer/payee and exact deltas on both machines, no duplicate/crossed transfer |
| C02 | Each player triggers its notification | Only intended player's feed receives one per invocation, optional spouse stays portrait only |
| C03 | Each player clicks own GUI button | Own current ruler receives +2, partner receives none; both clients agree |
| C04 | Concurrent batch, invalidation and repeat | No stale/cross-player candidates or duplicated charges; report any desync |
| C05 | Save/load pending delayed probe and completed actions | One reward per valid request, no repeated transfer on load; unresolved generation case stays blocked |

## Evidence capture and result recording

From workspace PowerShell use the existing portable interpreter:

    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' -B Documentation/tools/capture_fixture_logs.py --label run-A --phase begin

After normal game exit run the same command with `--phase end`. Repeat labels run-B/run-C; each player may use `run-C-host`/`run-C-client`. It only reads logs, selected-mod metadata and crash-report metadata/logs, writing copies under Documentation. No saves or dump binaries are copied. Begin/end snapshots retain hashes and classify changed files; a byte-identical old file is not a new export. The collector cannot establish which character action succeeded, so complete [results](test-results.md) with balances, IDs and visible outcomes.

Allowed statuses: `not run`, `passed with evidence`, `failed`, `blocked/environment`, `inconclusive`. For every passed row record run directory, timestamps, actor/target IDs and exact observed before/after values. Paste relevant new errors and describe deviations. Exports/main-menu exit success are not substitutes for these results. Return the completed table to this chat; corrections and only affected retests follow.
