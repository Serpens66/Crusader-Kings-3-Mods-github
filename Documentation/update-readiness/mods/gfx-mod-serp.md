# GFX Mod Serp update sheet

Purpose: retain the fuller local graphics variant, including intense icon/illustration/trait styling and map post-effects. The original `info.txt` explicitly distinguishes this from the published GFX package. Evidence: [texture report](../texture-comparison.md), [all headers and native hashes](../evidence/textures.json), same-path difference record and current native post-effect file.

## Work packages

| ID | Surface | Evidence | Action or gate |
|---|---|---|---|
| GS-ICONS | Character/status/interaction icons, skills, trait frames and rank styling | 664 textures inventoried, 291 without native same-path file; 41 native size differences | **Blocked consumer mapping/render:** group by actual GUI/script/dynamic consumer, keep custom art where selected, remap replaced names only after proving the current consumer. Missing native path is not enough to mark an asset obsolete |
| GS-RANK | Shared `portrait_rank.dds` | Same short atlas issue as public package | Use the current frame mapping work from GX-RANK; preserve distribution-specific artwork and validate separately |
| GS-ILLUSTRATIONS | Men-at-arms and character UI illustrations | Included in the complete texture manifest | Verify clipping/aspect/frames in the current recruitment, regiment and character windows. Existing files cover only selected illustrations; no unrelated new-art commission |
| GS-CONTAINERS | `icon_prowess.dds`, `icon_skills.dds`, `icon_skills_martial.dds` | Actual headers are PNG under a `.dds` suffix | Do not silently transcode or rename. Establish current engine acceptance and consumer paths through logs/render tests; if a conversion is needed, explicitly preserve the image/color intent and choose the proven accepted format |
| GS-POST | `gfx/map/post_effects/posteffect_volumes.txt` | Only the six assignment changes below differ from current native content | Rebase these exact values onto current native content; add mandatory UTF-8 BOM when this file is edited. Do not copy an older whole-file definition over new native volumes |
| GS-PACKAGE | Descriptor, credits, info and previews | Same public identity as smaller package; no external `GFX-Mod Serp.mod` here | Preserve local role and credits. A local test registration can be prepared later; do not upload or overwrite the public package |

## Exact post-effect delta

Full native/mod files were read and compared. Current native is 119 lines, replacement is 120. Relative file path is identical.

| Named volume | Assignment | Native | Intended custom value |
|---|---|---|---|
| cold | saturation_scale | 1 | 0.8 |
| cold | colorbalance | { 1 1 1 } | { 1 1 1.1 } |
| hot | value_scale | 1.0 | 1.15 |
| hot | colorbalance | { 1.0 1 1 } | { 1.1 1 0.9 } |
| flatmap | saturation_scale | inherited/not explicitly assigned here | 1.05 |
| flatmap | exposure | 1.0 | 0.6 |

The authoritative delta is **six assignments**: two cold, two hot and two flatmap. Reapply those values to the current native file and preserve all unrelated content.

## Relevant mechanics and tests

Current rank tiers, new GUI consumers and map zoom/volume selection are relevant. New gameplay religion/war rules are not direct targets of this graphics package. New map regions matter only insofar as they select existing volumes/assets; no topology or map-history changes are planned.

Test warm/cold regions, seasons and the paper-map transition at multiple zooms, comparing standard and Serp rendering. Verify each dimension mismatch group from the table in its actual widget; a different icon size may be intentional. Test all rank tiers, trait frames, skills and men-at-arms categories. Collect loading/render warnings for the three PNG containers. Check host/client checksums and appearance; old comments claiming unchanged checksum are not current test evidence.

The post-effect assignments are plan ready. Texture adaptation remains blocked by actual consumers/frame mapping and render results. The 291 absent native same paths are an audit queue, not a deletion list. Source credits and any publication rights remain attached to assets; this preparation grants no redistribution permission.

## Static consumer findings

[The consumer scan](../asset-consumers.md) checked all 677 retained texture files against 5,830 native text files. It records exact paths separately from basename, symbolic icon and matching object-ID candidates. Use those current sources before choosing any adaptation. Remaining compiled/dynamic frame or path selection and actual rendering are explicit gates; assets without a match are not deleted automatically.

## Current-export reconciliation (2026-10-03)

Declarations are available separately from remaining semantic/runtime gates. Original intent and update status are retained.

| Feature | Signature intake | Separate contract |
|---|---|---|
| GS-ICONS | source/asset contract, not an engine-command signature | [Card](../contracts/GS-ICONS.md) |
| GS-RANK | export declarations available | [Card](../contracts/GS-RANK.md) |
| GS-ILLUSTRATIONS | source/asset contract, not an engine-command signature | [Card](../contracts/GS-ILLUSTRATIONS.md) |
| GS-CONTAINERS | source/asset contract, not an engine-command signature | [Card](../contracts/GS-CONTAINERS.md) |
| GS-POST | source/asset contract, not an engine-command signature | [Card](../contracts/GS-POST.md) |
| GS-PACKAGE | source/asset contract, not an engine-command signature | [Card](../contracts/GS-PACKAGE.md) |

## Maintenance after future game updates — 2026-10-03

Follow the [mandatory update workflow](../../handbook/mod-update-workflow.md). A request to check this mod includes established targeted corrections after the full affected-feature audit. Run `Documentation/tools/check_mod_updates.py --mod "GFX-Mod Serp"`; it is read-only and uses the [reviewed baseline index](../update-watch-index.json). The initial registration has **377 watches** against 1.20.0.3. Unchanged watches do not close the Engine/runtime gates above.

**Watched surfaces:** All native same-path replaced textures, current portrait/character/tooltip consumers and the complete native map post-effect file.

**Preserved intent and audit priorities:** Preserve the fuller local distribution and artwork. After native volume changes reapply only the six documented intended assignments, preserving unrelated new content. Audit new consumers/frame selection, 41 historical dimension differences, absent-native assets and PNG-under-DDS containers before remapping/transcoding.

**Required regression acceptance:** Warm/cold seasons, zoom/paper-map transitions, every rank tier and affected skill/trait/men-at-arms widget; container loading logs; rendering/checksums in two-player play. No automatic public Workshop upload.

Known watch lists are curated source registrations, not a complete semantic/transitive graph. Add newly discovered relevant dependencies after their source audit. Keep future reports and baselines dated; preserve older evidence, user edits and distribution identity. No source hash or successful parser run establishes gameplay/GUI/MP compatibility. Release metadata remains gated by the prescribed actual tests unless the user explicitly authorizes a separate target declaration.
