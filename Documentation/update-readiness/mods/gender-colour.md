# Gender Colour update sheet

Purpose: retain gender-specific sexuality-icon coloring without adding gameplay rules. Evidence: descriptor, five texture hashes and headers in [baseline](../evidence/workspace-baseline.json) and [texture comparison](../texture-comparison.md); native same-path replacements and GUI consumer discovery. No rendered test was performed.

## Content and action

| ID | Content | Evidence | Action or gate |
|---|---|---|---|
| GC-ICONS | `gfx/interface/icons/character_status/sexuality_icons_female.dds` and `sexuality_icons_male.dds` | Native same paths exist; current and replacement header dimensions match | Retain coloring for the current frames. **Blocked render/consumer check:** verify frame count and all sexualities/genders in the current GUI; same dimensions do not prove correct frame order |
| GC-EXTRAS | `sexuality_icons_female_alt.dds`, `sexuality_icons_male_grey.dds`, `sexuality_icons_male_wrongicon.dds` | No native same-path texture found | Preserve these variants initially. Determine whether any mod/native static or dynamic consumer uses them before classifying them as backups. Do not infer broken packaging or delete them just from filename |
| GC-PACKAGE | Descriptor and preview | Workshop ID 2602590291; descriptor points at `thumbnail.png` | Check the actual preview payload before publication. Preserve identity; current supported-version wildcard is 1.5.* and remains unchanged until testing |

## Mechanics and compatibility

New religions, governments and war mechanics are not relevant to this asset-only feature. Current portrait/status GUI consumers are relevant; additional genders/frame selection are unresolved until the current UI contract and render tests are checked. No script/DLC requirement is inferred from the graphics tag.

Both GFX variants replace the same two active textures. Their simultaneous use needs an explicit choice of authoritative coloring and a byte/render comparison. Until then, test Gender Colour separately, not by relying on load order.

## Tests and release gate

Compare male/female characters across each available sexuality/status frame, selection/hover state, portrait size and UI scale. Confirm that the coloring requested by this mod remains visible and no icon is clipped or misassigned. In MP, inspect one host and one client and record checksum/connection behavior instead of assuming all graphics are checksum-neutral. Expected gameplay behavior is unchanged.

After those checks, the update may require only packaging/metadata and any confirmed frame adaptation. Do not expand the icon collection to unrelated new mechanics. Render and consumer checks are the concrete blocker; resolve them through UI dump/source inspection followed by the user test protocol.

## Static consumer findings

[The consumer scan](../asset-consumers.md) checked all 677 retained texture files against 5,830 native text files. It records exact paths separately from basename, symbolic icon and matching object-ID candidates. Use those current sources before choosing any adaptation. Remaining compiled/dynamic frame or path selection and actual rendering are explicit gates; assets without a match are not deleted automatically.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| GC-ICONS | source/asset contract, not an engine-command signature | [Card](../contracts/GC-ICONS.md) |
| GC-EXTRAS | source/asset contract, not an engine-command signature | [Card](../contracts/GC-EXTRAS.md) |
| GC-PACKAGE | source/asset contract, not an engine-command signature | [Card](../contracts/GC-PACKAGE.md) |

## Maintenance after future game updates — 2026-10-03

Follow the [mandatory update workflow](../../handbook/mod-update-workflow.md). A request to check this mod includes established targeted corrections after the full affected-feature audit. Run `Documentation/tools/check_mod_updates.py --mod "Gender Colour"`; it is read-only and uses the [reviewed baseline index](../update-watch-index.json). The initial registration has **4 watches** against 1.20.0.3. Unchanged watches do not close the Engine/runtime gates above.

**Watched surfaces:** Both native sexuality atlases and their current consumers in `gui/window_character.gui` and `gui/shared/cooltip.gui`.

**Preserved intent and audit priorities:** Preserve existing coloring and distribution identity. Native asset byte/header changes require frame/order/consumer auditing; unchanged dimensions are not rendering proof. Variants without native same paths remain an unresolved consumer queue, not automatic deletion candidates.

**Required regression acceptance:** All available sexuality/gender frames, hover/selection, portrait sizes and two UI scales; host/client appearance/checksum. Test separately from competing GFX packages.

Known watch lists are curated source registrations, not a complete semantic/transitive graph. Add newly discovered relevant dependencies after their source audit. Keep future reports and baselines dated; preserve older evidence, user edits and distribution identity. No source hash or successful parser run establishes gameplay/GUI/MP compatibility. Release metadata remains gated by the prescribed actual tests unless the user explicitly authorizes a separate target declaration.
