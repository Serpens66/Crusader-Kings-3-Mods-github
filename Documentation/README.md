# CK3 modding knowledge base

This is a working reference for building new Crusader Kings III mods in this workspace. Start here in a new session. The main language is English; script identifiers remain unchanged.

**Research date:** 2026-10-03. **Installed launcher version:** 1.20.0.3 (Crozier). This is an installation-specific baseline, not a claim about the newest public release. Old user logs identify 1.16.3 and are not current API evidence.

## Reading and retrieval map

| Need | Read |
|---|---|
| Develop a new mod safely | [Development workflow](handbook/development-workflow.md) |
| Understand the language | [Syntax and execution contexts](handbook/script-language.md) |
| Work with scopes | [Scopes and contracts](handbook/scopes.md) |
| Conditions, loops and reusable helpers | [Control flow and macros](handbook/control-flow.md) |
| Store data and calculate numbers | [State and script values](handbook/state-and-values.md) |
| Events, decisions and hooks | [Events, decisions and on actions](systems/events-decisions-on-actions.md) |
| Character interactions | [Interactions](systems/interactions.md) |
| Player-facing text and buttons | [Localization and GUI](systems/localization-and-gui.md) |
| Traits, modifiers and balance | [Traits, modifiers and defines](systems/traits-modifiers-defines.md) |
| Other game systems | [Subsystem guide](systems/subsystem-guide.md) |
| Start from concrete files | [Examples and test scenarios](examples/README.md) |
| Learn from existing work | [Workspace case studies](workspace/case-studies.md) and [inventory](reference/workspace-inventory.md) |
| Find a function or an object | [Command quick reference](reference/commands.md), [local lookup](reference/index-guide.md) |
| Check confidence and gaps | [Audit findings](research/vanilla-audit.md), [coverage](research/coverage.md), [sources](research/sources.md) |

## Rules for future agents

1. Read the workspace `AGENTS.md` again. It is authoritative and can change independently of this collection.
2. Establish the user's requested behavior before choosing implementation details. Find the corresponding native entry point and complete the feature-specific Vanilla audit before proposing behavior or writing code.
3. Use this handbook to find evidence; never treat an observed symbol as a complete engine contract. Trace the relevant definition, caller, helper dependencies, scopes, targets and localization.
4. Verify installation version and source hashes when relying on local references after an update. Current generated dumps outrank historical tables for engine API signatures.
5. Prefer a new uniquely named file/object when the loader supports it. Audit the actual override mechanism before overriding existing content.
6. Use a unique prefix for new public identifiers, variables, flags and localization. Follow this workspace's UTF-8 BOM rule for `.txt`/`.yml` and CRLF rule for text files.
7. State exactly what was validated: structural check, source audit, external validator, or gameplay test. Only a gameplay test supports a claim that the feature works in the engine.

## What is available offline

The authored handbook, annotated examples, topic matrix, workspace inventory, 183 developer-reference paths, native definition index and observed command uses can be searched without internet access. The installation itself remains the source for complete Vanilla scripts; it is not copied into the repository. Internet sources are linked and summarized rather than archived wholesale.

The example mod is **not installed or activated**. Its descriptor is a teaching fixture. The GUI example is an explicitly marked insertion fragment requiring a real window context.

## Validation report

See the [static verification report](research/verification.md) for checked links, encodings, example structures and source preservation. Engine execution, Tiger validation and GUI rendering have not been performed.

## Maintaining this reference

See [index tools](reference/index-guide.md). Regenerate indexes after a patch, compare the relevant hashes and review affected teaching statements. Update source dates and coverage explicitly; a new index alone does not revalidate the handbook. No recurring upkeep or automatic game launch is configured.
