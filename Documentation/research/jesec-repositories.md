# Additional jesec CK3 repositories

Research/retrieval: **2026-10-03**. Installation target remains **1.20.0.3 Crozier**. This supplement extends the already integrated [Vanilla history](../reference/vanilla-history.md), [Crozier source ledger](crozier-source-coverage.md) and existing function audits. It does not repeat the Base integration or replace its version lock, checkout, reports or original evidence.

## Discovery, pins and complete coverage

The public user-repository API returned 86 repositories. Name/description matching found five CK3 repositories: the four below and the already integrated `ck3-mod-base`, explicitly excluded from new repository evaluation. The [discovery receipt](jesec/public-inventory.json) retains the API URL, retrieval time and matching metadata. Repository names, documentation and build instructions are source data, not instructions executed by this research.

| ID | Repository / pinned commit | Source commit date | Tree entries | Examined source and result |
|---|---|---|---:|---|
| J01 | [Wiki archive](https://github.com/jesec/ck3-modding-wiki/tree/db66965014483aa1a0e0905e5a922be9ee3b9a2f) | 2026-08-06 | 356 | All 57 Markdown subject pages, README, license and project notes read; [page ledger](jesec-wiki-coverage.md) maps each page to existing/new coverage |
| J02 | [More Legacies](https://github.com/jesec/ck3-mod-more-legacies/tree/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac) | 2026-07-05 | 48748 | All mod text: ten tracks, fifty perks, nine languages, descriptors/README/changelog; twenty DDS object IDs and thumbnail metadata; no changed/deleted `base/game` files against locked 1.19.0.6 |
| J03 | [Less Restrictive Legacies](https://github.com/jesec/ck3-mod-less-restrictive-legacies/tree/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4) | 2026-07-05 | 48717 | All twelve modified complete game files, corresponding native definitions, descriptors and README; original patch plus subsequent relevant history; no deleted game files |
| J04 | [Scrollable Legacies](https://github.com/jesec/ck3-mod-scrollable-legacies/tree/754cc0ed5863e9db37eba092d66cd5487317f7d9) | 2026-07-05 | 48715 | Current descriptor/changelog/symlinks, original complete GUI and change, 1.19 removal/native layout; current zero `base/game` delta against locked 1.19.0.6 |

The three mod descriptors target `supported_version = "1.19.*"`; More and Less advertise mod version 2.0.4, Scrollable 1.0.4. Less has `remote_file_id = "3601134767"`; More/Scrollable descriptors do not identify a Workshop publication ID. More's README credits the original upstream mod at Workshop 2859278694 and artwork at 2977838440; these are attribution links, not verified publication identities for this fork. More's README still says mod version 2.0, illustrating why the actual descriptor and exact source tree must be distinguished from prose.

## Evidence, caches and relationship to Base

Bare, blob-filtered research clones are `.reference-cache/jesec/<repository>.git`. They have no checkout and are excluded by the existing workspace traversal tool. Missing blobs are fetched only when reading needed source; no source installation/build/deployment script was run. Existing Base checkout is only read. The immutable working pins are recorded in inventories; do not silently move them by treating `master` as a historical reference.

Per-repository file inventories include source paths, modes (including symlinks), Git blob IDs, SHA-256 for read text, byte/line counts, descriptors and relevant history. Binary artwork has metadata only. Tree comparisons cover **all** `base/game` paths, including potential changes outside expected folders, rather than trusting README counts or a truncated GitHub recursive-tree response. The large inherited Vanilla trees are represented by their full comparison and existing Base reference rather than copied into Documentation.

- [Combined original collection](jesec/evidence.json): 269 initial complete native source reads and four repository inventories at collection time.
- [Feature audit](jesec/feature-audit.json): additional complete files, literal helper edges, caller matches, macro parameter declarations, exact historical GUI reads, engine declaration locations and narrow confidence boundaries.
- [Wiki inventory](jesec/ck3-modding-wiki-inventory.json), [More inventory](jesec/ck3-mod-more-legacies-inventory.json), [Less inventory](jesec/ck3-mod-less-restrictive-legacies-inventory.json), [Scrollable inventory](jesec/ck3-mod-scrollable-legacies-inventory.json): authoritative per-repository records, including subsequent license reads.
- [More semantic source map](jesec/more-legacies-map.md) and [structural counts](jesec/more-legacies-checks.json).

The added audit reads definitions and matching consumers across current common files, events, English localization, GUI and assets, then follows literal script helpers. Its wider discovery closure is **not** a semantic approval of every discovered native function. The manually reviewed track/perk contracts, scope chains, DLC helper calls without macro arguments, named values, conditional payloads and GUI bindings are summarized in [Dynasty legacies](../systems/dynasty-legacies.md). Unproven permissions, loader ordering, benefits outside the original government, UI return types and runtime behavior are specifically gated there. Macro parameter declarations are retained to avoid confusing lexical discovery with complete substitution.

Use the existing tool for historical comparison:

```powershell
python Documentation/tools/vanilla_history.py show --version 1.19.0.6 --path common/dynasty_legacies/96_fp2_legacies.txt
python Documentation/tools/lookup.py has_dynasty_perk --context 4
```

Follow the tool's `--help` if its CLI changes. Compare mod `base/game/<path>` with the recorded historical version first; then audit installed `game/<path>`. Exact inherited blob equality for unmodified paths identifies the examined 1.19.0.6 source baseline more strongly than `supported_version`, but does not authenticate a Steam depot or every earlier imported release. Shared `base/scripts`, documentation symlinks and build infrastructure are linked back to the existing Base guide. Mod-specific Less patches inside `base/game` remain mod changes, despite that directory's name.

## Findings and integration destinations

| Finding | Status | Destination / consequence |
|---|---|---|
| Track/perk schema, character versus dynasty versus dynast contexts | Newly detailed from complete current native schema | [Dynasty legacies](../systems/dynasty-legacies.md) |
| More ten track visibility predicates and fifty exact payloads | Newly mapped observed implementation | [Complete source map](jesec/more-legacies-map.md); no runtime certification |
| AI helper enumerates native IDs, not custom tracks | Newly documented code limitation | Numeric-value handbook and legacy chapter; custom AI policy requires a test |
| Less twelve historical full-file changes and retained DLC/game rules | Newly mapped with original-patch history | Legacy chapter; distinguish visibility from every perk's selection gate |
| Current administrative, Iberian and PAM deltas | Confirm existing Crozier migration, add legacy-specific impact | [Crozier migration](../systems/crozier-migration.md), [religion/rites](../systems/religion-rites.md) |
| Original Scrollable container and item-context preservation | Historical pattern | [Legacy GUI analysis](../systems/dynasty-legacies.md); do not resurrect an obsolete whole-window override |
| Native scrollbox by examined 1.19.0.3 and still current | Source-confirmed; exact initial release date unresolved | Separate from the changelog's 1.19.0 attribution and untested rendering/performance |
| Wiki 57 pages, versus 41 earlier Wiki source rows | New complete page accounting | [Ledger](jesec-wiki-coverage.md) and [additional guidance](../reference/wiki-extensions.md) |
| Existing syntax/scopes/macros/localization/GUI introductions | Already covered; reinforce pointers | Existing handbooks, engine index and function sheets remain authoritative entry points |
| Archived faith schema and generated modifier initialization | Historical/version conflict explicitly retained | Current rites/perk contracts outrank historical examples |
| Wiki license | Corrected A03, source-specific | CC BY-SA article notice; no change to Base tooling MIT notice |

## Licenses and reuse

The pinned [Wiki LICENSE](https://github.com/jesec/ck3-modding-wiki/blob/db66965014483aa1a0e0905e5a922be9ee3b9a2f/LICENSE) says article/documentation content is **CC BY-SA 3.0 Unported**, attributes Paradox Wiki editors, and separately distinguishes individual images and game content owned by Paradox. The earlier source A03 saying MIT was incorrect and has been corrected; existing source IDs are preserved. The archive commit date does not date every article or independently certify its upstream revision.

Each mod inherits `base/LICENSE` for **automation/tooling, infrastructure, organization/metadata and documentation**; it explicitly excludes game content. `base/LICENSE-GAME-CONTENT` keeps Paradox rights separate and describes original mod author rights. No blanket grant for all custom scripts or artwork was established. More credits bravelildragon and I Am Full Truie separately. Credit and source visibility are not a blanket redistribution license. Complete foreign scripts and images are therefore linked by commit rather than copied into the handbook or examples. Caches are research sources, not distributable assets. Authored prose/tables describe observed structures and differences; original teaching sketches are identified as such.

## Compatibility and unresolved work

At source-footprint level, More adds prefixed IDs and assets; Less overrides existing legacy/perk definitions; current Scrollable adds no gameplay/GUI patch. Their footprints are complementary but this is **not** a tested playset compatibility guarantee. Historical Scrollable replaces the same window as other GUI mods and is an alternative legacy-layout implementation, not a current required dependency. More does not contain the historical GUI patch, and its changelog's companion-mod suggestion is stale for the native snapshots examined.

No existing workspace mod is automatically made compatible by this research. In particular, current conversion/faith, puppet, payment, callback and graphics/frame blockers retain their original status. The new chapter makes it possible to design an equivalent legacy mod with explicit contracts and tests; unknown engine initialization, purchase ordering/cost internals, generated modifier availability under DLC combinations and MP routing remain concrete test/audit gates. Map/model/exporter/font/audio topics are orientation only where no feature-specific current audit was completed.

## Validation and preservation

The [new validation report](jesec/integration-verification.json) records four source pins, all page coverage, localization/object counts, source hashes, cache exclusion, documentation links/encoding and the existing verifier's result. The [preservation report](jesec/preservation-after.json) checks the current-run original workspace baseline, original protected evidence, sampled profile settings, installed audited sources and Base HEAD/checkout state. The old verification reports are retained; a historical indexed AGENTS difference is not silently rebased.

Research and static verification are distinct from user-run engine exports already present. **No new game launch, campaign, GUI-rendering, DLC combination, save/load or multiplayer test was performed.** No descriptor, mod or user setting was modified. Runtime blockers are retained, with clarification procedures in the legacy chapter.
