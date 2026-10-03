# Historical Vanilla source reference

Integrated on 2026-10-03. The full [jesec/ck3-mod-base repository](https://github.com/jesec/ck3-mod-base) is available locally at `.reference-cache/ck3-mod-base`, relative to the workspace root. This is a normal working clone with complete fetched history, not a shallow clone, submodule or mod installation. Its initial detached checkout is the pinned 1.20.0.3 commit.

The external repository includes a mod template and automation. This integration uses only its source history and metadata; none of those scripts are executed. Original checkout bytes are retained with local `core.autocrlf=false`. Its notices remain in the clone: game content and MIT-licensed repository tooling have separate licenses. See the upstream [game-content notice](https://github.com/jesec/ck3-mod-base/blob/master/base/LICENSE-GAME-CONTENT) and [tooling license](https://github.com/jesec/ck3-mod-base/blob/master/base/LICENSE). No Vanilla source archive is added to this workspace's tracked files.

## Authority and reproducibility

The [version lock](vanilla-history-lock.json) records the URL, exact patch tags and dereferenced commits. The initial pair is **1.19.0.6 → 1.20.0.3**. 1.19.0.6 is the chosen last-patch baseline; the user's assertion that MDC worked under 1.19 does not establish an exact patch or a historical test result. Floating `base/1.19` and `base/1.19.0` aliases resolve to another commit and are not interchangeable with this lock.

The [first evidence report](../research/vanilla-history-20261003.json) records game-tree IDs, upstream version metadata and its original SHA-256, file-change records and scoped installed-source hashes. This is a third-party historical mirror, not independently authenticated Steam depot content. Missing files, omitted binaries and DLC coverage must be assessed from the actual trees and metadata. For current behavior, installed Vanilla definitions and versioned Engine exports remain the primary local evidence.

The tool reads committed blobs, so local edits or checkout changes cannot silently alter a version comparison. Pinned tag mismatches fail explicitly. Additional numeric versions can be requested by exact `base/` tag; they do not automatically change the lock. Review and date a new lock/evidence entry when adopting a new baseline. Git rename detection uses `-M50%` and is a heuristic, not proof of semantic identity.

## Commands from the workspace root

Set the portable interpreter for this PowerShell session:

```powershell
$vanillaPython = 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe'
& $vanillaPython Documentation/tools/vanilla_history.py versions
```

Fetch updated history and list newly fetched tags. This requires network access; it does not pull, change the checkout, prune references, force tags or rewrite the lock:

```powershell
& $vanillaPython Documentation/tools/vanilla_history.py fetch
```

Read and compare files without changing the checkout:

```powershell
& $vanillaPython Documentation/tools/vanilla_history.py show --version 1.19.0.6 --path common/character_interactions/00_religious_interactions.txt
& $vanillaPython Documentation/tools/vanilla_history.py diff --from 1.19.0.6 --to 1.20.0.3
& $vanillaPython Documentation/tools/vanilla_history.py diff --path common/character_interactions/00_religious_interactions.txt --patch
& $vanillaPython Documentation/tools/vanilla_history.py compare-local --path common/character_interactions/00_religious_interactions.txt
```

`show` and `diff --patch` emit original bytes; terminal decoding is a display concern. `compare-local` first checks exact bytes, then separately classifies BOM/CRLF-only differences without rewriting either source. Its scope is the requested paths, not a certification of the entire installation. Missing-in-mirror and missing-in-installation are distinct outcomes. Paths use game-relative forward slashes; traversal, absolute paths and Git pathspec expressions are not accepted as file selectors.

Search the current checkout directly by specifying its otherwise ignored path:

```powershell
rg -n 'run_interaction|puppet_or_actor' .reference-cache/ck3-mod-base/base/game/common/character_interactions
git -C .reference-cache/ck3-mod-base log --oneline -- base/game/common/character_interactions/00_religious_interactions.txt
```

Explicitly change the selected checkout only when needed:

```powershell
& $vanillaPython Documentation/tools/vanilla_history.py checkout --version 1.20.0.3
```

Checkout refuses tracked or untracked local changes. Save any personal experiments separately; this tool never discards them. `fetch` preserves even a dirty checkout. All commands other than `fetch` work offline once the required objects exist locally. A Git transport sandbox restriction may require the normal escalation path; changing script arguments cannot fix a blocked Git runtime.

## Evidence and maintenance

`report` writes the fixed initial-pair overview and the existing 295-path MDC seed comparison under Documentation, using a fresh UTC timestamp in the filename by default. An explicit `--output Documentation/research/<new-name>.json` is also supported; existing reports are never replaced. It intentionally does not archive full Vanilla patches. The [first findings](../research/vanilla-history-20261003.md) distinguish inventory coverage from semantic analysis.

The root ignore rule `/.*/` already excludes hidden local roots. Inventory and preservation tools explicitly prune `.reference-cache` and `.git` through [workspace_walk.py](../tools/workspace_walk.py). Existing preservation baselines are not regenerated. Other users must recreate the ignored clone locally; the clone is not delivered with a normal checkout of this workspace repository.

To recreate it, run `git -c core.autocrlf=false -c core.hooksPath=NUL clone --no-checkout https://github.com/jesec/ck3-mod-base.git .reference-cache/ck3-mod-base`, then set the clone's local `core.autocrlf` to `false`, local `core.hooksPath` to `NUL`, and use the tool's explicit checkout command above. Do not add the clone to the parent repository. Upstream source encodings are deliberately preserved as requested; the workspace BOM rule continues to apply to authored mod/example files.

Run the offline tests with `Documentation/tools/test_vanilla_history.py`. They create and clean disposable repositories under `.reference-cache/tests`; no game or tool installation occurs. A source diff supplies historical definitions and caller evidence, but never substitutes for the required complete feature audit or outstanding gameplay/GUI/multiplayer tests.
