# Searching and refreshing the local reference

## Files

| Reference | Contents | Limit |
|---|---|---|
| [local-index.json](local-index.json) | Installation/workspace paths, version, file hashes, BOM flags, line counts, top-level assignments | Lexical assignments are not a typed game database |
| [observed-symbols.json](observed-symbols.json) | Symbols used as assignment/comparison keys, up to four native locations each | Mixes schema fields, script helpers and engine operations; not a legal-command registry |
| [native-info-index.md](native-info-index.md) | All 183 installed developer `.info` files | Developer documents may be incomplete or contain obsolete schematics |
| [workspace-inventory.md](workspace-inventory.md) | All mod text files, descriptor fields, other asset counts and same-path overlaps | Matching keys are conflict candidates; merge semantics need audit |
| [audit-evidence.json](audit-evidence.json) | Complete-file read hashes and literal helper-reference discovery | No macro expansion, engine validation or proof of all runtime references |
| [commands.md](commands.md) | Curated command/construct starting points | Intended example contexts, not exhaustive supported scopes |

The indexes intentionally preserve ordered/repeated assignment information as records instead of converting script definitions to a single-value dictionary. Hashes refer to original source bytes; CRLF/BOM changes also change a hash.

## Look up a symbol

Portable Python available in this environment:

```powershell
& 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/lookup.py add_gold --context 4
& 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/lookup.py can_be_knight_trigger
```

The tool shows native definition matches, workspace definition matches and observed uses. It reads live source context only when `--context` is supplied. A stale index can point at the wrong line after an update; compare hashes before treating it as evidence. A missing match does not establish that a command is unsupported.

For direct searches, prefer `rg`, restrict to the relevant tree and trace both definitions and callers. Quoted strings and parameter-expanded names need manual review. A GUI template name or field can look like an engine operation to a lexical scanner.

## Regenerate after an update

```powershell
& 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/build_local_reference.py --game 'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game'
& 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/audit_local_sources.py
& 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/verify_documentation.py
```

These scripts use Python's standard library, read the supplied source tree and write only under `Documentation`. No dependency installation is required. `build_local_reference.py` accepts an optional workspace path but always keeps output in this collection. `audit_local_sources.py` uses the roots from the generated index.

The audit discovery selects developer references, explicit seed files and representative meaningful definitions, then follows literal helper references through whole files. Because it can overinclude symbols, call-graph edges are navigation evidence rather than a formal semantic graph. Parameter-generated calls, inherited behavior, database references and engine callbacks still need feature-specific inspection.

Regeneration updates evidence only. It does not revise prose, update a declared research date, run the game, render a GUI or certify new versions. Recheck coverage and version-conflict notes before presenting the handbook as current.
