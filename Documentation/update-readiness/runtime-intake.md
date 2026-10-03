# Runtime evidence intake

Reviewed 2026-10-03. The [normal debug run](runtime-evidence/20261003T112558.279918Z/run.json) ended normally with **exit code 0**, no new/changed captured crash reports, and **five fresh datatype files** totaling **2,679,725 bytes**. All **21 captured stage files** match their recorded SHA-256 values. The current mod selection matches the backed-up original byte-for-byte.

The fresh runtime debug log feeds **1.20.0.3** into checksum calculation. The nonempty code-revisions log identifies game commit **4fe04c7143e6288cf1da609145c22d0ddc3c8878**, matching the first run's crash metadata. A displayed checksum value was not found in the reviewed logs; it remains unrecorded rather than inferred from the executable or installation checksum file.

The datatype output covers common, GUI, internal Clausewitz GUI, script and uncategorized definitions. The six earlier script-reference exports also still match their recorded hashes. These complementary runs provide current source material for reviewing command signatures and GUI contracts. Export availability is now established; individual feature behavior and mod compatibility are not established by export generation.

The run retains existing-profile AGOT rule references and an unavailable `no_stark_wolf.dds` emblem, plus localization diagnostics. It is a usable main-menu reference with recorded profile warnings, not an error-free clean-profile baseline. No settings, presets or saves were cleaned. The previous automatic-run crash remains unexplained; normal completion here does not identify its cause.

Detailed file paths, sizes and hashes are in [intake evidence](evidence/runtime-intake.json). The original run manifests/raw exports remain unchanged. Next work is per-feature signature comparison against the existing source audits; only documented signature gaps can then be closed. Lifetime, side effects, permissions, UI behavior, campaigns, save/load and multiplayer still require their planned tests.
