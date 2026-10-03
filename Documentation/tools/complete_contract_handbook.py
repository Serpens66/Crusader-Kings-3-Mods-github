"""Author the export intake supplement and bounded teaching-fixture contracts.

Only writes within Documentation. Native file reads below are evidence, not tests.
"""
import hashlib
import json
import re
from pathlib import Path

D = Path(__file__).resolve().parents[1]
W = D.parent
G = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')

def write(rel, text):
    p = D / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes((text.strip()+'\n').replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))

def append(rel, text):
    p = D / rel
    old = p.read_text(encoding='utf-8')
    heading = text.strip().splitlines()[0]
    if heading in old: old = old.split(heading)[0].rstrip()+'\n'
    write(rel, old+'\n'+text)

def main():
    engine = json.loads((D/'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'))
    counts = {}
    for e in engine['entries']: counts[e['category']] = counts.get(e['category'],0)+1
    rows = '\n'.join(f'| {k} | {v:,} |' for k,v in counts.items())
    write('reference/engine-reference.md', '''
# Installed engine reference: 1.20.0.3

Intake date: 2026-10-03. Engine commit: `4fe04c7143e6288cf1da609145c22d0ddc3c8878`.
This reference describes the installed Crozier build, not the newest release worldwide.

The [machine-readable index](engine-1.20.0.3.json) contains all eleven retained exports. Entries preserve category, literal name, documented syntax/description, scope/target text, repeated documented fields, available parameter examples and return type, exact raw source, line range and SHA-256. Blank or absent metadata remains absent; parameter examples are not a formal list of required arguments.

| Category | Entries |
|---|---:|
'''+rows+'''

`datatype` includes registered and unregistered functions, promotes and type members. These counts are declarations, not distinct callable names. Same names in different categories/owners and repeated definitions remain separate. `saved_target` records the code-saved target appendix separately from ordinary event-target descriptions.

## Provenance and coverage

The [runtime intake](../update-readiness/evidence/runtime-intake.json) records originals, copies, timestamps and checksums. The first user-run export session produced six script exports but subsequently crashed with an access violation; it is not a successful full diagnostic run. The second normal debug session ended with exit code zero, produced five fresh data-type exports and no fresh crash report, and restored the original mod-selection bytes. Its version and code revision agree with the first exports. Existing script exports were retained, not falsely classified as newly generated in the second run.

The second run establishes an export/main-menu baseline only. It does not establish clean campaign behavior, multiplayer compatibility or a clean user profile. Existing AGOT preset references, the missing `no_stark_wolf.dds` reference and localization diagnostics are retained profile warnings; no causal connection to the earlier crash has been established.

All six script and five data-type export checksums are checked on rebuild. The parser records line spans for declarations, headers, separators, blank lines and uninterpretable sections. Current exports have zero unparsed sections under this parser; synthetic unknown-section tests verify that future unknown text is retained rather than silently discarded. See [parser](../tools/build_engine_reference.py) and [tests](../tools/test_engine_reference.py). Parsing does not certify that engine documentation itself is complete.

The effects export contains bytes incompatible with strict UTF-8. Its index uses a reversible Windows-1252 candidate decoding; raw bytes are preserved. This is not proof of the game's declared output encoding. Other exports are UTF-8 compatible. Do not normalize the original `.raw` files to satisfy mod-file BOM rules.

## Retrieval

Run `python Documentation/tools/lookup.py run_interaction --context 5`, `lookup.py has_variable --context 3`, `lookup.py ScriptedGui.Execute --context 4` or `lookup.py GetPlayer --context 2`. Use the installed portable Python if `python` is unavailable. Engine results print category, version, source and line before existing native/mod definitions and observed uses. Exact spelling matters. A missing indexed result does not prove that a function is forbidden.

The original [local index](index-guide.md) still provides definitions and callers. Use both: an effect declaration states a primitive contract, while the relevant `.info`, definition, caller and helper expansion establish feature context. The index does not infer permissions from names, turn `none` into a universal scope, invent optional arguments, or infer multiplayer synchronization from a `void` return type.

## Signatures that refine the workspace review

| Symbol | Exported information | Remaining feature question |
|---|---|---|
| `run_interaction` | Explicit actor/recipient, redirect and threshold syntax are described in the effect export | Native actor/puppet initialization, acceptance/consent and all downstream conversion consequences |
| `is_character_interaction_valid` | Character trigger with recipient/interaction query syntax | Whether a particular feature supplies every target/context needed by that native interaction |
| `use_hook` | Export describes weak-hook removal and strong-hook cooldown | Whether the original pardon purpose requires deleting a strong hook instead; live notification/cooldown behavior |
| `remove_participant` | War-scope removal with character target | Allowed participants, native hook side effects and selected-war invalidation |
| `save_scope_as`, `clear_saved_scope` | Saved reference primitives and documented chain context | Propagation, invalidation and cleanup for each actual delayed chain |
| `open_view_data` | Optional player routing; omission can open for executing players | Correct per-player education UI routing in multiplayer |
| `TryStartRulerDesigning` | Current global function lists two arguments; native callers supply a character-type string | Whether old one-argument calls have a supported default and post-start permission |
| `ScriptedGui.IsShown`, `IsValid`, `Execute` | Single TopScope argument; registered return types retained | Correct widget root, synchronized click behavior and visible native UI |

Every row is a declaration finding. Retrieve its full raw text before implementation; the [43 contract cards](../update-readiness/contracts/README.md) retain remaining behavioral gates. No compatibility status is promoted automatically.
''')
    write('workspace/function-contracts.md', '''
# Workspace function contracts and state ownership

Read the [43 individual contract cards](../update-readiness/contracts/README.md), the [per-mod sheets](../update-readiness/README.md), [conflict matrix](../update-readiness/conflicts.md) and [source register](../update-readiness/sources.md) together. The cards link engine declarations to their exact raw lines and retain the original feature gate. The evidence file records complete rereads of 149 workspace text files and 1,214 native files; this lexical closure is a retrieval surface, not proof that every transitive macro has a resolved semantic contract.

## How to complete a contract

Start at the real decision, interaction, callback or widget, not a helper in isolation. Record its root and named scopes, enumerate each guard and native call, expand every `$PARAMETER$` using the actual caller, then follow each effect and queued event. Read the complete matching `.info`, definitions, callers, localization and assets. Separate the current mod's behavior, its comments/textual intent, and the installed native contract. If an owner, branch, permission or parameter binding remains unresolved, retain that specific gate and its proposed test. A successful export cannot close a lifetime or consent question.

## Conversion requests

Decision root is the requester. The standalone supplies five category/count paths, including tributaries; the bundled copy supplies four. In candidate iteration `this` becomes candidate; entering requester/root changes `prev` at that exact caller to candidate. A shared predicate must retain that contract for both a Script Value count and a send loop. Neither matching counts nor `send_threshold = decline` proves forced acceptance: current native interaction consequences and later responses still need tracing.

Preserve house enumeration rather than silently expanding to a house bloc; preserve the original stronger indirect-vassal protection policy until intent is decided. Native rite, domicile, steppe, promise, diarch and protection gates are relevant. Query/dispatch initialization of `scope:puppet_or_actor` remains unresolved. The new [contract lab](../examples/contract-lab/README.md) deliberately tests dispatch of an isolated own interaction; success there cannot certify native conversion. Sources: [MC sheet](../update-readiness/mods/mass-demand-conversion.md) and MC-CANDIDATES/MC-DISPATCH cards.

## War withdrawal

The interaction actor is a secondary participant; recipient is leader. The current script stores up to ten war references and opens a selector. Each branch must revalidate current war existence, same side, actor membership and non-primary status before any price or removal. Saved war references are event-chain state, not a durable character preference.

```mermaid
stateDiagram-v2
    [*] --> Enumerated: interaction stores at most ten wars
    Enumerated --> Picker: actor event
    Picker --> Cancelled: cancel
    Picker --> Recheck: choose one saved war
    Recheck --> Invalid: ended / changed leader / actor absent
    Recheck --> Paid: valid updated contract only
    Paid --> Withdrawn: war-scope remove_participant
    Withdrawn --> Cleanup: opinions / alliance / notifications
    Invalid --> Cleanup: required no-charge path
    Cancelled --> Cleanup: audit all saved references
    Cleanup --> [*]
```

This diagram distinguishes the intended safe update from currently unproven revalidation/cleanup paths. Base policy is 25 × tier gold and 50 × tier prestige, with six rule variants; “nothing” still attempts alliance breaking in existing code. `add_prestige` plus explicit experience subtraction needs live delta comparison before refactoring. Native removal callbacks and custom messages can overlap. Sources and exact table: [LW sheet](../update-readiness/mods/leave-wars.md).

## Additional education and delayed state

The payer is interaction actor; the student is recipient, and self-study intentionally combines those roles. The selected ordinary discipline costs five times recipient skill in both gold and prestige; prowess uses four times prowess. Initial stress is payer +10, student +35. Six discipline branches apply temporary study modifiers. The student owns the study marker; a saved actor/recipient reference is not a guarantee that its object remains alive or player-controlled.

```mermaid
stateDiagram-v2
    [*] --> Menu: actor opens education
    Menu --> Cancelled: existing menu cancellation policy
    Menu --> Studying: accept / charge / recipient marker
    Studying --> StudentCompletion: day 365 student event
    Studying --> PayerReport: day 366 payer event
    StudentCompletion --> Rewarded: valid study marker / consume
    PayerReport --> Rewarded: only if marker still permits fallback
    Studying --> Expired: day 367 marker expiry
    Rewarded --> [*]
    Expired --> [*]
    Cancelled --> [*]
```

The two completion paths attempt to retain reward after payer death. They are not a proven duplicate-reward bug. Verify exactly once across self-study, separate students, payer/student death, changed court, reload at days 364–367 and stale events from an earlier course. Permanent reward, expiring marker and chain-local references have different owners/lifetimes. A generation token would be a design change requiring a fully audited chain contract, not a guessed cure. Source: [SI education section](../update-readiness/mods/serp-interactions-decisions.md).

## Payments, hooks and religion

Money transfers execute in actor scope with recipient as target. Preserve 50/100/250/500 values, including the deliberate 250-gold AI-recipient exception. Display-time affordability is insufficient for a mutable target; audit execution guards and short-term budget accounting. The teaching fixture tests a fixed five-gold transfer but does not certify these original interactions.

The pardon calls `use_hook`, so the export's weak removal/strong cooldown distinction resolves the primitive description only. Choosing permanent deletion for strong hooks requires an explicit intent decision before updating the mod. Keep that question in the [decision register](../update-readiness/behavior-decisions.md).

Excommunication helper substitution must bind all of `EXCOMMUNICATOR`, `REQUESTING_CHARACTER`, `TARGET_CHARACTER`; direct powers and requested powers assign different roles. The replacement crime helper accepts `RITE`, `TRAIT`, `GENDER_CHARACTER`, not the old `FAITH` argument. Audit the actor/authority/victim redirect and whose rite governs each crime in both eligibility and price. Do not choose a rite merely from a helper name. Current clergy, territorial authority, protection, legitimacy and response consequences are relevant to the existing temporal-authority feature. Sources: SI-EXCOMM and the SI sheet's exact formula/role table.

## Notification callbacks and GUI

Each callback supplies its own root/guaranteed/optional targets. War start, secondary joining, death and court departure cannot share a guessed context. Recipient collections must document owner, membership overlap, deduplication policy and lifetime. Missing killer/employer/spouse must be guarded before portrait or text resolution. A message sent inside one character scope should be compared to per-player delivery, with native notifications counted separately. Sources: [SerpAlerts sheet](../update-readiness/mods/serp-alerts.md), on-action/message `.info` and exported callback declarations.

GUI observation and execution are distinct. All three ScriptedGui calls must use the same constructed root; a player action uses player root, a selected-character action uses the selected object. `open_view_data` without a player is a routing question in multiplayer. Current two-argument ruler-designer calls do not establish that old calls lack an overload, or that the engine permits post-start editing. Full replacement GUI paths must retain the entire current native content, not merely the old changed button. Sources: CD-RULES/CD-LOBBY/CD-TOOLTIPS and SA-EDUCATION cards.

## Graphics and variants

An asset basename or existing mod comment is not proof of a live consumer. Trace current widget/asset path, atlas dimensions, `framesize`, frame expression and container header. Native portrait rank is 1374×194 with 196×194 frames, while the old rank texture is 1176×194; a raw seven-frame comparison is prepared without inventing tier labels. PNG bytes under `.dds` remain an engine-acceptance test, not permission to silently convert original art. [Private GUI/frame fixture](../examples/gui-frame-lab/README.md) and [asset manifest](../examples/fixture-assets.json) preserve source hashes.

Standalone/bundle conversion and withdrawal share IDs and are alternatives. Public/local graphics packages share paths and represent alternate selections. Knight variants/test also share native trigger/window identities; they are learning material only, excluded from updating. See [Knight contracts](knight-manager-contracts.md). DLC gates follow each actual native/helper branch; a filename does not establish a blanket dependency.
''')
    write('update-readiness/behavior-decisions.md', '''
# Behavior decisions before the affected update

These questions do not block unrelated documentation or fixtures. No existing mod is changed here.

| Feature | Unresolved intent or contract | Required resolution |
|---|---|---|
| SI-PARDON | Does pardon permanently remove strong hooks, or retain existing `use_hook` cooldown semantics? | User behavior choice before substituting a removal effect; weak/strong live tests |
| MC-CANDIDATES | Stronger indirect-vassal religious-protection exclusion than native direct-contract gate | Preserve currently implemented policy by default; ask before relaxing it |
| SI-EXCOMM | Temporal-only custom powers versus modern authority/rite paths | Complete issuer/requester/victim role audit, then ask only where intended policy cannot be recovered |
| SI-ABDICATE | Continue as rightful heir versus modern landless/deposal route | Trace government/succession and player continuation; do not blindly select native helper |
| Delayed examples/SI-EDUCATION | Stale events crossing a new request/course and scope propagation | Current dump plus actual delayed/save-load test; generation-aware example remains blocked pending audited design |
| CD-LOBBY | Old one-argument call defaults and post-start permission | Current native two-argument callers plus focused UI test; no guessed permission bypass |
| Graphics | Exact rank/frame meaning and PNG-under-dds acceptance | Render fixture and current native tier consumers; preserve alternate files |

All other per-feature gates remain in the [43-card matrix](contracts/README.md). A specific remaining test is not evidence of completed compatibility.
''')
    # Complete native type files and branch references for the isolated fixtures.
    audit_paths = [
      'gui/shared/backgrounds.gui','gui/shared/buttons.gui','gui/preload/labels.gui',
      'gui/hud.gui','gui/shared/portraits.gui','gui/scripted_widgets/_scripted_widgets.info',
      'common/scripted_guis/ce1_funeral_scripted_guis.txt',
      'gui/activity_window_widgets/funeral_deceased_selection_button.gui',
      'common/character_interactions/_character_interactions.info','common/character_interactions/00_gift.txt',
      'common/on_action/_on_actions.info','common/on_action/birthday.txt','common/on_action/yearly_on_actions.txt',
      'common/on_action/barter_on_actions.txt','common/messages/_messages.info',
      'common/decisions/_decisions.info','common/scripted_triggers/00_war_and_peace_triggers.txt']
    audit=[]
    for rel in audit_paths:
        p=G/rel
        if not p.exists(): raise FileNotFoundError(p)
        raw=p.read_bytes(); text=raw.decode('utf-8-sig',errors='replace')
        audit.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),
          'full_file_read':True,'lines':len(text.splitlines()),'decode_warning':'\ufffd' in text,
          'boundary':'Native recipe/type evidence; no engine function test or complete transitive semantic closure claimed'})
    write('examples/native-recipe-audit.json',json.dumps(audit,indent=2))
    write('examples/contract-lab/README.md', '''
# Documentation Contract Lab — source-informed, runtime pending

This separately named package adds a five-gold character interaction, courtier count/dispatch decision, player birthday message/manual callback decision and a character-root Scripted GUI action. It uses only its own `doclab_` IDs, plus an additive native `on_birthday` child hook. It is not installed or activated. Source contract intake: [audit manifest](../native-recipe-audit.json), [engine reference](../../reference/engine-reference.md). Test using the [bundled manual](../test-runs.md).

| Files | Entry and scope contract |
|---|---|
| `common/character_interactions/doclab_interactions.txt` | Human actor, distinct living adult recipient; auto-accept, five-gold affordability; on_accept enters actor and rechecks funds/life before payment |
| `common/scripted_triggers/doclab_triggers.txt` | `doclab_batch_candidate`: candidate `this`, requester `root`; requester's native validity query receives candidate through `prev` at this exact root hop |
| `common/script_values/doclab_values.txt` | Fixed amount 5; eligible courtier count; total cost count × amount |
| `common/scripted_effects/doclab_effects.txt` | Rechecks total balance, iterates the shared predicate and runs own interaction with explicit actor/recipient and accept threshold; notification guards optional spouse |
| `common/decisions/doclab_decisions.txt` | Count/total UI and dispatch share values; separate manual callback decision is a repeatable recipient test |
| `common/on_action/doclab_on_actions.txt` | Adds child to native birthday hook; human/live root only; automatic and manual invocation each constitute one separate invocation |
| `common/messages/doclab_messages.txt` | Unique neutral feed-message type; actor portrait, optional spouse portrait |
| `common/scripted_guis/doclab_guis.txt` | Same living human character root for visibility, validity and execution; adds exactly 2 gold per valid click |
| `localization/english`, `localization/german` | English strings; German file is an explicitly English fallback for this private test |

The immediate transfer is not native gift balancing: no gift opinion, native price or struggle effects. Count agrees with the shared predicate when state is unchanged, not with an immutable snapshot under arbitrary concurrent changes. There is no persistent batch list or claim of native conversion equivalence. On-action `.info` states that effect/event chains do not automatically share local scope saves; this fixture creates its own root-bound notification and never relies on a saved scope from a parent effect.

The notification sends in the current human scope. The spouse is optional portrait content, not an additional recipient. No spouse branch omits the right icon entirely. Expected one feed message per invocation for the owning player, zero for AI. Birthday and manual calls deliberately both exist; do not misclassify two separate invocations as duplicate delivery from one callback.

Engine signatures support these API forms; current `00_gift.txt` and native yearly interaction dispatch establish payer and explicit actor/recipient patterns. Native funeral GUI supplies a complete ScriptedGui caller pattern; widget registration `.info` supplies additive window registration. Permissions, synchronization, candidate-query initialization and actual acceptance/rendering remain tests. None of these files is advertised as a working production template yet.
''')
    write('examples/gui-frame-lab/README.md', '''
# Documentation GUI Frame Lab — private diagnostic fixture

Requires the separately named **Documentation Contract Lab**. The [registration descriptor](../registration/doclab_gui.mod) points at this content root; no vanilla GUI path is replaced. `gui/scripted_widgets/doclab_registration.txt` registers `gui/doclab_panel.gui = doclab_panel` using the current `_scripted_widgets.info` contract. The panel is visible when `GetPlayer.IsValid`; runtime placement/loading remains untested.

The button constructs the identical `GuiScope.SetRoot(GetPlayer.MakeScope).End` for `IsShown`, `IsValid` and `Execute`, targeting `doclab_panel_action` in the gameplay lab. A valid click adds two gold to the local player's character. Native funeral ScriptedGui/button caller, full button/background/text type definitions, HUD usage and exports were read and hashed in the [recipe audit](../native-recipe-audit.json). These sources establish a binding recipe, not proof of a rendered or synchronized window.

Three rows compare native portrait-rank atlas, public legacy atlas and local legacy atlas. Columns are literal frames 1–7 with `framesize = { 196 194 }`; they are not asserted title-tier labels. Native atlas width is 1374; old width is 1176. Record cropped/blank/out-of-range behavior rather than assuming an old six-frame texture supports the current consumer. This synthetic panel tests raw frames; actual portrait masks/tier mapping still require checking the live native consumer.

Three further icons probe the existing `icon_prowess`, `icon_skills` and `icon_skills_martial` files whose headers are PNG despite `.dds` suffixes. Their bytes are unmodified. [Asset manifest](../fixture-assets.json) contains six original paths, content hashes, container observations and private-use limits. These copies are local diagnosis material, not a publishable art bundle. No map or audio functionality is added.

Tests: load panel, labels at normal and alternate UI scale, exactly +2 gold per click, no wrong-player grant, all raw frames, all PNG-container icons, native windows still present, save/load and host/client execution. A successful panel does not validate unrelated existing GUI overrides or every asset in GFX-Mod Serp. See [manual](../test-runs.md).
''')
    write('examples/test-runs.md', '''
# Three bundled user test runs

Status: **not run**. These are private probes; none is certified functional. No tool starts CK3, changes your playset, or operates input. The old Vanilla diagnostic starter disables mods and must **not** be used for these fixture runs.

## One-time registration and safe selection

1. Close CK3 and its launcher; leave Steam available. Record/screenshot your original selected playset. Preserve any existing identically named external descriptor rather than overwriting it.
2. In Explorer open `Documentation/examples/registration`. Copy only `doclab_demo.mod`, `doclab_gameplay.mod`, `doclab_gui.mod` into `C:\\Users\\Serpens66\\Documents\\Paradox Interactive\\Crusader Kings III\\mod`. Their content paths already point to this workspace. Moving the workspace requires updating those descriptor paths first. No original mod files are copied or edited.
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

    & 'D:\\CDesktopLink\\Portable\\Python\\WinPy64\\python\\python.exe' -B Documentation/tools/capture_fixture_logs.py --label run-A --phase begin

After normal game exit run the same command with `--phase end`. Repeat labels run-B/run-C; each player may use `run-C-host`/`run-C-client`. It only reads logs, selected-mod metadata and crash-report metadata/logs, writing copies under Documentation. No saves or dump binaries are copied. Begin/end snapshots retain hashes and classify changed files; a byte-identical old file is not a new export. The collector cannot establish which character action succeeded, so complete [results](test-results.md) with balances, IDs and visible outcomes.

Allowed statuses: `not run`, `passed with evidence`, `failed`, `blocked/environment`, `inconclusive`. For every passed row record run directory, timestamps, actor/target IDs and exact observed before/after values. Paste relevant new errors and describe deviations. Exports/main-menu exit success are not substitutes for these results. Return the completed table to this chat; corrections and only affected retests follow.
''')
    cases=[f'A{i:02d}' for i in range(1,11)]+[f'B{i:02d}' for i in range(1,6)]+[f'C{i:02d}' for i in range(1,6)]
    # Rebuilding documentation must never erase user-provided acceptance evidence.
    if not (D/'examples/test-results.md').exists():
        write('examples/test-results.md', '# Fixture acceptance results\n\nNo fixture gameplay or multiplayer test has been executed. Preserve this distinction from the completed export sessions.\n\nBuild / checksum / DLC / language / UI scale / save / player IDs: **pending**.\n\n| Case | Status | Observed result and exact deltas | Evidence / remaining issue |\n|---|---|---|---|\n'+'\n'.join(f'| {x} | not run | — | — |' for x in cases))
    if not (D/'examples/test-results.json').exists():
        write('examples/test-results.json',json.dumps({'version':'1.20.0.3','status':'runtime pending','cases':[{'id':x,'status':'not run','evidence':None} for x in cases]},indent=2))
    # Link every original feature to its separate signature reconciliation.
    matrix=json.loads((D/'update-readiness/feature-matrix.json').read_text(encoding='utf-8'))
    groups={}
    for f in matrix['features']:groups.setdefault(f['sheet'],[]).append(f)
    for sheet, fs in groups.items():
        append('update-readiness/'+sheet, '## Current-export reconciliation (2026-10-03)\n\nDeclarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.\n\n| Feature | Signature intake | Separate contract |\n|---|---|---|\n'+'\n'.join(f"| {f['id']} | {f['signature_status']} | [Card](../{f['contract_card']}) |" for f in fs))
    append('update-readiness/feature-matrix.md','## Export reconciliation and state contracts\n\nThe [43 cards](contracts/README.md) and [function guide](../workspace/function-contracts.md) add declaration evidence and owner/lifetime gates. Current exports are integrated; old rows requesting signatures are historical combined gates, not evidence that exports are still missing. Remaining caller, permission and runtime questions are retained explicitly in each card. Feature tests remain not run.')
    append('examples/README.md','## Current export-backed contract labs\n\nThe [Contract Lab](contract-lab/README.md) and [GUI/frame lab](gui-frame-lab/README.md) are complete separately named source-informed packages with external descriptor templates, English/German fallback text and own IDs. They are not installed, enabled or runtime certified. Use the [three-run manual](test-runs.md) and [results table](test-results.md). The old GUI fragment remains an insertion lesson; the new GUI fixture provides additive registration.\n\n**Delayed-chain limit:** the original boolean marker has no generation identity. A stale completion coinciding with a new request is not ruled out by its guards. Its short chain remains a teaching probe, not a certified robust exactly-once recipe. A generation-aware replacement is blocked pending a fully audited scope/lifetime contract and actual tests. Original mini-mod IDs and raw evidence are retained.\n\nCurrent six script and five UI exports are now [indexed](../reference/engine-reference.md); no re-export is needed for this build unless sources change.')
    append('research/coverage.md','## 2026-10-03 export and fixture supplement\n\n| Topic | Research/source evidence | Static checks | Runtime / exact remaining gap |\n|---|---|---|---|\n| Effects/triggers/scopes/targets/modifiers/on actions | Eleven exports, version/commit and hashes; all line spans accounted | Parser duplicate/unknown/encoding tests | Primitive documentation is not feature permission or complete behavior |\n| GUI functions | Registered/unregistered type declarations retained separately | Known ScriptedGui/TopScope signatures | Widget rendering and MP synchronization pending |\n| 43 existing functions | Separate cards, full source rereads and original per-mod sheets | Signatures reconciled without promoting compatibility | Macro/context/side-effect gates retained per card |\n| Knight variants/test | Trigger/state/widget learning audit | Variant/state source manifest | Historical overrides and continued missing GUI; no updates commissioned |\n| Immediate payment/bulk | Source-informed isolated Contract Lab | IDs, structure, localization and engine reference intake | Exact deltas/query initialization require A/C |\n| Delayed chain | Original two-event probe, state diagram | Namespace/guards/marker references | Cross-generation exactly-once recipe blocked; A07–A10/C05 |\n| Callback/optional targets | Own message and guarded spouse branch | Hook/message files | Recipient/dedup behavior A05–A06/C02 |\n| GUI/frame/container | Additive package and six hashed unmodified assets | Type/registration/asset evidence | B01–B05/C03 required |\n\nSee [completion report](completion-report.md). No runtime fixture result is manufactured.')
    for rel in ['handbook/scopes.md','handbook/state-and-values.md','handbook/control-flow.md','systems/interactions.md','systems/localization-and-gui.md','systems/events-decisions-on-actions.md','reference/index-guide.md','reference/commands.md']:
        append(rel,'## Installed 1.20.0.3 export supplement\n\nThe [current engine reference](../reference/engine-reference.md) now indexes six script and five data-type exports with exact raw line ranges and checksums. Historical statements above about absent generated dumps describe the initial research stage. Use [lookup](../tools/lookup.py) for both engine declarations and existing local definitions/callers. Missing optionality, argument types, scope lifetime, permissions and multiplayer routing remain unknown where the export does not specify them.\n\nSee [workspace function contracts](../workspace/function-contracts.md) for owner/caller/state distinctions and [isolated tests](../examples/test-runs.md) for runtime acceptance. The user completed export sessions, but no example gameplay/GUI/MP tests have been performed.')
    append('research/sources.md','## Current export/recipe sources (2026-10-03)\n\nInstalled baseline 1.20.0.3 and engine commit are supported by the [runtime intake](../update-readiness/evidence/runtime-intake.json), including both original export sessions and their different crash/exit results. All eleven raw sources are listed with path, timestamp, SHA and decoding candidate in [engine index](../reference/engine-1.20.0.3.json). Recipe source paths, full-read line counts and hashes are in [native recipe audit](../examples/native-recipe-audit.json); exact asset originals/hashes in [fixture manifest](../examples/fixture-assets.json).\n\nRechecked [Tiger primary repository](https://github.com/amtep/tiger) and [Wiki archive primary repository](https://github.com/jesec/ck3-modding-wiki) on 2026-10-03. Tiger describes validation scope and possible false positives/update lag; no installed Tiger executable was found and target-build support is not established here. No installation or validation run was performed. Historical wiki/OldEnt references remain discovery aids; current installed exports and native callers take priority for this baseline. These pages are summarized, not mirrored.')
    append('research/documentation-readiness.md','## Resolution supplement after export integration\n\nThe earlier assessment is retained as history. Engine indexing, lookup integration, separate 43-feature declaration cards, owner/state narratives, Knight learning material and isolated payment/callback/GUI-frame probes have now been added. See [completion report](completion-report.md). Source-informed packages and concrete remaining blockers replace broad claims of missing work; they do not establish functioning gameplay templates. Full transitive semantic audits remain bounded by the gates in each card; no lexical closure is promoted into a complete audit.')
    p=D/'README.md';t=p.read_text(encoding='utf-8')
    t=t.replace('Engine execution, Tiger validation and GUI rendering have not been performed.', 'User-run engine exports have been captured and verified. Fixture gameplay, Tiger validation and GUI rendering remain unperformed.')
    t=t.replace('The GUI example is an explicitly marked insertion fragment requiring a real window context.', 'The original GUI example remains an insertion fragment; the new GUI/frame lab includes additive registration and a complete source-informed binding, awaiting runtime tests.')
    t=t.replace('| Find a function or an object |','| Current engine declarations | [Versioned engine reference](reference/engine-reference.md) |\n| Detailed function/state contracts | [Function guide](workspace/function-contracts.md), [43 cards](update-readiness/contracts/README.md), [Knight variants](workspace/knight-manager-contracts.md) |\n| Complete fixture acceptance runs | [Three-run manual](examples/test-runs.md), [completion status](research/completion-report.md) |\n| Find a function or an object |')
    write('README.md',t)
    replacements = {
      'systems/localization-and-gui.md': {
        'The online Data Types table is an orientation; no current local dump was found. Therefore unobserved function signatures need a fresh dump or exact current Vanilla caller.':
        'The online Data Types table is an orientation. The eleven current exports are now indexed in [the installed engine reference](../reference/engine-reference.md). An absent indexed signature still requires an exact current Vanilla caller or focused engine investigation; it is not permission to invent a function.'},
      'reference/commands.md': {
        'No current local generated dumps were found during this research, so this collection does not manufacture a complete 1.20 engine signature registry.':
        'The six script and five data-type exports are now retained and indexed in [the 1.20.0.3 registry](engine-reference.md). The registry conserves the supplied declarations; it does not claim that the engine exports document every permission or behavior.'},
      'update-readiness/README.md': {
        'No game or external validator was run.':
        'The user-run export sessions are now recorded separately in [runtime intake](runtime-intake.md); no fixture gameplay tests or external validator run have been performed.'},
      'update-readiness/debug-run.md': {
        'Use the [normal debug starter](diagnostic-start.md) and [Start-Vanilla-Diagnostics.cmd](Start-Vanilla-Diagnostics.cmd) for the next GUI export: enter `dump_data_types` once at the main menu and exit normally.':
        'The user completed the normal debug/main-menu GUI export; see [runtime intake](runtime-intake.md). The [normal debug starter](diagnostic-start.md) and [Start-Vanilla-Diagnostics.cmd](Start-Vanilla-Diagnostics.cmd) remain available only if another Vanilla export is needed; do not use them for mod fixture tests.'}
    }
    for rel, mapping in replacements.items():
        t=(D/rel).read_text(encoding='utf-8')
        for before,after in mapping.items():t=t.replace(before,after)
        write(rel,t)

if __name__ == '__main__': main()
