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
