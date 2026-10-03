# Installed engine reference: 1.20.0.3

Intake date: 2026-10-03. Engine commit: `4fe04c7143e6288cf1da609145c22d0ddc3c8878`.
This reference describes the installed Crozier build, not the newest release worldwide.

The [machine-readable index](engine-1.20.0.3.json) contains all eleven retained exports. Entries preserve category, literal name, documented syntax/description, scope/target text, repeated documented fields, available parameter examples and return type, exact raw source, line range and SHA-256. Blank or absent metadata remains absent; parameter examples are not a formal list of required arguments.

| Category | Entries |
|---|---:|
| effect | 2,127 |
| scope | 74 |
| target | 327 |
| saved_target | 382 |
| modifier | 761 |
| on_action | 930 |
| trigger | 1,935 |
| datatype | 24,593 |

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
