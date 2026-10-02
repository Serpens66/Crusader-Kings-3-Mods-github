# Localization, custom text and GUI integration

Evidence: [Localization and Interface sources](../research/sources.md); native `gui/preload/textformatting.gui`, `common/customizable_localization/_custom_loc.info`, GUI-to-script callers and scripted GUI definitions in [audit findings](../research/vanilla-audit.md).

## Localization files

This workspace requires UTF-8 BOM and CRLF. Put content under `localization/<language>`, use the `_l_<language>.yml` filename convention, and match the file's first-line language header. These files use CK3's localization reader; arbitrary YAML library normalization can break their conventions.

```yaml
l_english:
 doc_demo_decision:0 "Request a demonstration"
 doc_demo_decision_desc:0 "Run the documentation example."
```

The `:0` style is common in local files. Preserve quoted strings and language identifiers. The marker is not gameplay arithmetic. Use exact localization keys in scripts. Missing text in another language can show raw identifiers; choose translated text or clearly identified fallback copies rather than assuming English loads for every language.

String substitution `$OTHER_KEY$`, formatting such as `#P ...#!`, line breaks written as `\n`, icons and bracketed data calls are additional interfaces. A bracket expression only works if its context supplies the object or function used. Close formatting styles so following text is not accidentally recolored.

Keep localization names prefixed. For overriding native strings, use the documented `replace` convention and verify the actual winner in the playset; don't assume script object priority rules apply to localization.

## Dynamic text and custom localization

Dynamic descriptions select text based on conditions. Use a fallback when no condition matches, and audit scope availability in text previews as well as gameplay. Native event and trait references support dynamic text but have different optional-context requirements.

`common/customizable_localization` defines reusable text selectors. Its native reference requires a matching `type`, selects the first matching `text` entry unless `random_valid` is chosen, and allows `setup_scope` before the trigger. The provided scopes can be used in the selected localization. A random selector is a deliberate text behavior; it should not silently drive persistent gameplay.

## GUI data binding is a separate interface

`.gui` files define widgets, layout, templates and data contexts. Quoted bracketed expressions call exposed UI/data-type functions. They cannot execute arbitrary Jomini effects directly. A widget's current data context determines available objects; an expression working in the character window may be invalid in another window.

The native GUI/data-type dump is the reference for exposed functions and return types. The online Data Types table is an orientation; no current local dump was found. Therefore unobserved function signatures need a fresh dump or exact current Vanilla caller.

When modifying an existing GUI file, compare the entire current Vanilla file first. The Knight Manager variants replace `gui/window_knights.gui`, creating an update-sensitive whole-file footprint. Adding a button to an obsolete window can remove unrelated native features even when the new button works.

## Scripted GUI bridge

Define the action under `common/scripted_guis`, with a scope type and applicable `is_shown`, `is_valid` and/or `effect` blocks. Build the context in the GUI and use that same context for visibility, validation and execution.

```text
# GUI expression pattern observed in a native funeral button.
onclick = "[GetScriptedGui('doc_demo_request_gui').Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"
```

This is a GUI fragment, not a standalone window. `GetPlayer` is appropriate here only because the intended button acts for the GUI user's player character. A button acting on the selected character must use that actual selected object and a matching scope contract. Multiplayer gameplay code must not infer an actor from a local UI context unrelated to the synchronized request.

`GuiScope.AddScope(...)` passes additional named targets when required by a verified caller. A `scope = character` declaration is not enough to guarantee that the GUI built a character root. The native `rename_character_after_birth` definition and its interaction-menu caller demonstrate why both sides must be read together.

## UI calculation and feedback

Use simple localization and cheap values in frequently evaluated widgets. Deep scans inside GUI expressions or script values can be repeatedly evaluated. If caching is needed, explicitly define initialization, refresh and invalidation; stale cached state can mislead the player.

The visible enabled state and actual execution should agree. Also revalidate within the action when state can change between rendering and clicking. Provide feedback or a preview for effects that change gameplay rather than hiding a mutation behind an unexplained label.

## Testing

Check correct language/header, every referenced key, long and multiline strings, tooltip formatting, missing/optional scopes, disabled-button tooltip, correct click actor, selected-target changes and repeated clicks. Verify the original window still renders all native elements. A `.gui` fragment passing a brace check does not prove the UI template, layout or expression is supported.
