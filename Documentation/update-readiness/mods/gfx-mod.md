# GFX Mod update sheet

Purpose: preserve the smaller published graphics package. Keep it separate from the fuller local Serp distribution, which deliberately retains more intense changes. Workshop identity remains `2637472200`. Evidence: original `credits.txt`, descriptor, [texture comparison](../texture-comparison.md), native portrait GUI consumers and [conflicts](../conflicts.md).

## Work packages

| ID | Existing feature | Current evidence | Planned action or gate |
|---|---|---|---|
| GX-RANK | `gfx/portraits/portrait_rank.dds` | Mod 1176 × 194, native 1374 × 194; current `gui/shared/portraits.gui:24–25` uses 196 × 194 frames and title-tier selection | **Blocked atlas mapping:** enumerate current tier frames from UI export/native title definitions; rebuild against the current native frame count/layout while preserving established artistic changes. Keep every currently selected frame; adding a blank strip is not a validated fix |
| GX-ARTIFACT | `artifact_bg.dds`, `artifact_unique.dds` | Native same-path headers match size | Preserve styling; inspect current artifact inventory/detail consumers and empty/unique states. Render acceptance pending |
| GX-GENDER | Active female/male sexuality textures | Shared replacement paths also present in Gender Colour and Serp distribution | Retain published coloring; choose a single graphical distribution for each test playset |
| GX-EXTRAS | `sexuality_icons_female_mies.dds`, male grey/wrongicon | Three files have no native same-path texture | Preserve until static/dynamic consumer check establishes their role; do not rename/delete automatically |
| GX-PACKAGE | Descriptor/credits/preview | Current wildcard 1.7.*; shared publication identity with Serp | Maintain original credits and public scope; verify preview and identity after render tests |

Current higher title ranks are relevant to the rank atlas. New artifact mechanics matter only if they select additional states on the existing consumers. Religion/war gameplay changes are not relevant to this package. Whether missing atlas frames actually produce clipping or wrong art is a runtime question, not a passed failure diagnosis from dimensions alone.

## Tests

Render portraits for every current selectable title tier, including the highest available tier, plus ruler/non-ruler/clergy/regent branches. Native uses separate regency imagery; do not merge it into this atlas without evidence. Compare artifact backgrounds for common and unique items, empty slots, equipped/inventory views and tooltips. Verify gender colors and all sexuality frames. Repeat at two UI scales and in a two-player connection with identical package selections.

GX-RANK is blocked until the tier/frame mapping is established. The other styling packages are source-inventoried, with current consumer and render checks pending. After implementation, compare the public archive against its intended smaller footprint so local-only Serp assets are not inadvertently published.

## Static consumer findings

[The consumer scan](../asset-consumers.md) checked all 677 retained texture files against 5,830 native text files. It records exact paths separately from basename, symbolic icon and matching object-ID candidates. Use those current sources before choosing any adaptation. Remaining compiled/dynamic frame or path selection and actual rendering are explicit gates; assets without a match are not deleted automatically.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| GX-RANK | export declarations available | [Card](../contracts/GX-RANK.md) |
| GX-ARTIFACT | source/asset contract, not an engine-command signature | [Card](../contracts/GX-ARTIFACT.md) |
| GX-GENDER | source/asset contract, not an engine-command signature | [Card](../contracts/GX-GENDER.md) |
| GX-EXTRAS | source/asset contract, not an engine-command signature | [Card](../contracts/GX-EXTRAS.md) |
| GX-PACKAGE | source/asset contract, not an engine-command signature | [Card](../contracts/GX-PACKAGE.md) |

## Maintenance after future game updates — 2026-10-03

Follow the [mandatory update workflow](../../handbook/mod-update-workflow.md). A request to check this mod includes established targeted corrections after the full affected-feature audit. Run `Documentation/tools/check_mod_updates.py --mod "GFX-Mod"`; it is read-only and uses the [reviewed baseline index](../update-watch-index.json). The initial registration has **8 watches** against 1.20.0.3. Unchanged watches do not close the Engine/runtime gates above.

**Watched surfaces:** All five native same-path replaced textures plus portraits, character-window and tooltip consumers.

**Preserved intent and audit priorities:** Preserve the smaller public package, its artwork and credits; do not import local Serp assets. Check title-tier/frame changes and artifact state consumers. Three no-native-path extras remain unresolved and preserved.

**Required regression acceptance:** Every current rank/tier and regent/clergy/ruler branch; artifact common/unique/empty states; sexuality frames; two UI scales and identical host/client selection.

Known watch lists are curated source registrations, not a complete semantic/transitive graph. Add newly discovered relevant dependencies after their source audit. Keep future reports and baselines dated; preserve older evidence, user edits and distribution identity. No source hash or successful parser run establishes gameplay/GUI/MP compatibility. Release metadata remains gated by the prescribed actual tests unless the user explicitly authorizes a separate target declaration.
