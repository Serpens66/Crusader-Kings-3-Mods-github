"""Reproduce standalone MDC static migration evidence without running CK3.

This limited ordered-block reader checks the mod's syntax subset, not all Jomini.
Native helpers remain source evidence; unknown engine behavior is not inferred.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from build_local_reference import TOKEN
from collect_mass_conversion_audit import objects
from verify_documentation import check_braces
from audit_general_120 import preserved
import vanilla_history as history

DOC = history.DOC
DEST = DOC / 'update-readiness/evidence/mass-conversion-static-migration-20261003.json'
COMMANDS = ['any_vassal', 'every_vassal', 'any_vassal_or_below', 'every_vassal_or_below',
            'any_tributary', 'every_tributary', 'any_courtier', 'every_courtier',
            'any_house_member', 'every_house_member', 'vassal_contract_has_flag', 'exists',
            'is_character_interaction_potentially_accepted', 'run_interaction']
BINDINGS = ['Scope.ScriptValue', 'DecisionViewWidgetOptionList.GetEntries', 'DecisionViewWidgetOptionList.OnSelect']
POLICY = [('direct_vassals', 'any_vassal', 'every_vassal', 'demand_conversion_vassal_ruler_interaction'),
          ('indirect_vassals', 'any_vassal_or_below', 'every_vassal_or_below', 'demand_conversion_vassal_ruler_interaction'),
          ('tributaries', 'any_tributary', 'every_tributary', 'demand_conversion_vassal_ruler_interaction'),
          ('courtiers', 'any_courtier', 'every_courtier', 'ask_for_conversion_courtier_interaction'),
          ('house', 'any_house_member', 'every_house_member', 'demand_conversion_interaction')]


def parse(text):
    tokens = [m.group() for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    pos = 0
    def block():
        nonlocal pos
        rows = []
        while pos < len(tokens) and tokens[pos] != '}':
            key, op = tokens[pos:pos + 2]; pos += 2
            if op not in {'=', '!=', '?=', '>', '<', '>=', '<='}:
                raise ValueError('Outside checked mod syntax subset: ' + key + ' ' + op)
            if tokens[pos] == '{':
                pos += 1; value = block()
                assert tokens[pos] == '}'; pos += 1
            else:
                value = tokens[pos]; pos += 1
            rows.append((key, op, value))
        return rows
    result = block()
    assert pos == len(tokens), 'Unconsumed mod tokens'
    return result


def get(rows, key):
    return [value for name, _, value in rows if name == key]


def leaves(rows, path=()):
    result = []
    for key, op, value in rows:
        if isinstance(value, list):
            result += leaves(value, path + (key,))
        else:
            result.append((path, key, op, value))
    return result


def collect():
    before = preserved()
    root = DOC.parent / 'Mass Demand Conversion'
    engine_path = DOC / 'reference/engine-1.20.0.3.json'
    engine = json.loads(engine_path.read_text(encoding='utf-8'))
    declarations = {}
    for name in COMMANDS + BINDINGS:
        hits = [e for e in engine['entries'] if e['name'] == name]
        assert hits, 'Missing declaration: ' + name
        declarations[name] = hits
    exports = {e['source']['path']: e['source']['sha256'] for e in engine['entries']}
    for path, expected in exports.items():
        assert history.sha((DOC / path).read_bytes()) == expected, 'Export drift: ' + path
    mod_sources = {}
    for path in sorted(root.rglob('*')):
        if path.is_file() and path.suffix in {'.txt', '.yml', '.mod'}:
            raw = path.read_bytes(); text = raw.decode('utf-8-sig')
            assert path.suffix not in {'.txt', '.yml'} or raw.startswith(b'\xef\xbb\xbf'), 'Missing BOM: ' + str(path)
            assert path.suffix != '.txt' or check_braces(text), 'Unbalanced mod file: ' + str(path)
            mod_sources[path.relative_to(DOC.parent).as_posix()] = {'sha256': history.sha(raw), 'bom': raw.startswith(b'\xef\xbb\xbf')}
    # The external launcher descriptor is also preserved, but is not one of the 12 package text files.
    launcher = DOC.parent / 'Mass Demand Conversion.mod'
    descriptor = (root / 'descriptor.mod').read_text(encoding='utf-8-sig')
    assert re.search(r'version\s*=\s*"1\.077"', descriptor)
    assert re.search(r'supported_version\s*=\s*"1\.19\.\*"', descriptor)
    decision = parse((root / 'common/decisions/mod_mass_convert_subjects.txt').read_text(encoding='utf-8-sig'))[0][2]
    values = {key: body for key, _, body in parse((root / 'common/script_values/mod_mass_convert_subjects_values.txt').read_text(encoding='utf-8-sig'))}
    visibility = get(get(decision, 'is_shown')[0], 'OR')[0]
    branches = get(decision, 'effect')[0]
    categories = []
    for i, (category, anykey, everykey, interaction) in enumerate(POLICY):
        shown = get(visibility, anykey)
        if category == 'house':
            shown = get(get(get(visibility, 'AND')[0], 'house')[0], anykey)
        branch = get(branches, 'if')[0] if i == 0 else get(branches, 'else_if')[i - 1]
        assert ('scope:mod_convert_' + category, '=', 'yes') in get(branch, 'limit')[0]
        sent, counted, visible = leaves(branch), leaves(values['mod_convert_' + category + '_number']), leaves(shown[0])
        assert get(values['mod_convert_' + category + '_number'], 'value') == ['0']
        assert len([x for x in counted if x[1] == 'add']) == 1
        assert next(x for x in counted if x[1] == 'add')[3] == '1'
        assert any(everykey in x[0] for x in sent) and any(everykey in x[0] for x in counted)
        for dataset in [visible, counted, sent]:
            queries = [x for x in dataset if x[1] == 'interaction' and 'is_character_interaction_potentially_accepted' in x[0]]
            assert len(queries) == 1 and queries[0][3] == interaction
            query_path = queries[0][0]
            assert query_path[-2:] == ('root', 'is_character_interaction_potentially_accepted')
            assert (query_path, 'recipient', '=', 'prev') in dataset
            protections = [x for x in dataset if x[1] == 'vassal_contract_has_flag']
            assert bool(protections) == (i < 2)
            if protections:
                assert protections[0][0][-1] == 'NOT' and protections[0][3] == 'religiously_protected'
            indirect = [x for x in dataset if x[1] == 'liege' and x[3] == 'root']
            assert bool(indirect) == (i == 1)
            if indirect:
                assert indirect[0][0][-1] == 'NOT'
                assert any(x[1:] == ('exists', '=', 'liege') for x in dataset)
        dispatch = [x for x in sent if x[1] == 'interaction' and 'run_interaction' in x[0]]
        assert len(dispatch) == 1 and dispatch[0][3] == interaction
        for key, value in [('actor', 'root'), ('recipient', 'this'), ('send_threshold', 'decline')]:
            assert (dispatch[0][0], key, '=', value) in sent
        assert not any(x[1] == 'execute_threshold' for x in sent)
        if category == 'house':
            for dataset in [leaves(get(visibility, 'AND')[0]), counted, sent]:
                assert any(x[1:] == ('exists', '=', 'house') for x in dataset)
        categories.append({'category': category, 'enumeration': [anykey, everykey], 'interaction': interaction,
                           'query': {'scope': 'root', 'recipient': 'prev'},
                           'send': {'actor': 'root', 'recipient': 'this', 'send_threshold': 'decline'},
                           'protected_contract_exclusion': i < 2, 'indirect_liege_guard': i == 1})
    widget = get(decision, 'widget')[0]
    assert get(widget, 'controller') == ['decision_option_list_controller']
    assert get(widget, 'gui') == ['"decision_view_widget_decision_option_list_controller"']
    assert get(decision, 'ai_check_interval') == ['0']
    assert get(get(decision, 'ai_will_do')[0], 'base') == ['0']
    assert len(get(widget, 'item')) == 5
    assert {get(x, 'value')[0] for x in get(widget, 'item')} == {'mod_convert_' + p[0] for p in POLICY}
    languages = {}
    for path in sorted((root / 'localization').rglob('*.yml')):
        text = path.read_text(encoding='utf-8-sig')
        references = re.findall(r"ScriptValue\('([^']+)'\)", text)
        assert sorted(references) == sorted(values), 'Localization count mismatch: ' + str(path)
        languages[path.parent.name] = references
    assert len(languages) == 8
    historical_path = DOC / 'research/vanilla-history-20261003.json'
    historical = json.loads(historical_path.read_text(encoding='utf-8'))
    game = Path(historical['installation_root'])
    version_file = game.parent / 'launcher/launcher-settings.json'
    version_raw = version_file.read_bytes()
    assert json.loads(version_raw.decode('utf-8-sig'))['version'] == '1.20.0.3 (Crozier)', 'Installed version drift'
    native_hashes = {}
    for row in historical['installation_comparison']:
        digest = history.sha((game / row['path']).read_bytes())
        assert digest == row['installed_sha256'] == row['mirror_sha256'], 'Source drift: ' + row['path']
        native_hashes[row['path']] = digest
    followup_names = {
        'valid_demand_conversion_conditions_trigger', 'refusing_conversion_is_crime_trigger',
        'religion_demand_conversion_default_modifier', 'religion_demand_conversion_christian_situation_modifier',
        'demand_conversion_interaction_effect', 'demand_conversion_vassal_ruler_interaction_effect',
        'grab_spouses_and_family_to_convert_effect', 'convert_family_to_faith_effect',
        'convert_to_rite_with_consequences_effect', 'clean_convert_modifier_effect',
        'demand_conversion_influence_cost_value', 'pam_tax_nonbelievers_conversion_concession_effect',
        'conversion_tenet_acts_of_the_apostles_effect', 'conversion_tenet_mendicant_preachers_effect',
        'accept_faith_conversion_add_clan_unity_effect', 'refuse_faith_conversion_add_clan_unity_effect',
        'add_clan_unity_interaction_effect', 'apply_clan_unity_interaction_effect',
        'state_faith_conversion_add_piety_effect', 'give_piety_for_clinging_to_state_faith_effect',
        'mandala_converter_piety_effect', 'notify_puppeteer_of_outcome_effect',
        'religious_interaction.2002', 'religious_interaction.2003', 'religious_interaction.2011',
        'religious_interaction.2012', 'religious_interaction.2015', 'religious_interaction.2016',
        'char_interaction.0181', 'char_interaction.0182', 'false_conversion.0900',
        'false_conversion.1000', 'false_conversion.1010', 'study_faith',
        'study_faith_success', 'study_faith_failure', 'study_faith_has_anything_to_learn_trigger',
        'study_faith_outcome.0100', 'study_faith_outcome.0101',
        'study_faith_outcome.0110', 'study_faith_outcome.0111'}
    discovery = json.loads((DOC / 'update-readiness/evidence/mass-conversion-audit-20261003.json').read_text(encoding='utf-8'))
    followup_spans = []
    for row in discovery['objects'].values():
        if row['symbol'] in followup_names:
            raw = (game / row['path']).read_bytes()
            lines = raw.decode('utf-8-sig').splitlines()
            followup_spans.append({'symbol': row['symbol'], 'path': row['path'],
                'first_line': row['first_line'], 'last_line': row['last_line'],
                'whole_file_sha256': history.sha(raw),
                'decoded_line_span_sha256': history.sha('\n'.join(lines[row['first_line'] - 1:row['last_line']]).encode('utf-8')),
                'macro_parameters': row['parameters']})
    assert followup_names <= {r['symbol'] for r in followup_spans}, 'Missing followup definition'
    lock = history.load_lock(); snapshots = {}; native_objects = {}
    native_path = 'common/character_interactions/00_religious_interactions.txt'
    gui_path = 'gui/decision_view_widgets/decision_view_widget_decision_option_list_controller.gui'
    gui_bytes = []
    for version in ['1.19.0.6', '1.20.0.3']:
        commit = history.resolve(history.DEFAULT_REPO, version, lock)
        snapshots[version] = commit
        raw = history.git(history.DEFAULT_REPO, 'show', commit + ':base/game/' + native_path)
        for name, first, last, body in objects(raw.decode('utf-8-sig')):
            if name in {p[3] for p in POLICY}:
                assert 'cooldown_against_recipient = { years = 15 }' in body
                native_objects.setdefault(name, {})[version] = {'path': native_path, 'first_line': first, 'last_line': last,
                    'whole_file_sha256': history.sha(raw), 'decoded_block_sha256': history.sha(body.encode('utf-8')),
                    'recipient_cooldown_years': 15}
        gui_bytes.append(history.git(history.DEFAULT_REPO, 'show', commit + ':base/game/' + gui_path))
    assert gui_bytes[0] == gui_bytes[1] == (game / gui_path).read_bytes(), 'GUI changed'
    picture = game / 'gfx/interface/illustrations/decisions/decision_personal_religious.dds'
    assert picture.is_file(), 'Missing native picture'
    assert before == preserved(), 'Non-Documentation file changed during collection'
    return {'date': '2026-10-03', 'scope': 'standalone MDC 1.077 only; bundle port not certified',
            'conclusion': 'No necessary functional 1.20 mod patch demonstrated by these static checks; not proof of runtime compatibility.',
            'full_feature_audit_status': 'not closed; remaining Engine and runtime contracts explicit',
            'assumption': 'User states the mod worked correctly under 1.19; exact tested patch unknown.',
            'snapshots': snapshots, 'history_report_sha256': history.sha(historical_path.read_bytes()),
            'installed_version': '1.20.0.3 (Crozier)', 'launcher_version_sha256': history.sha(version_raw),
            'engine_index_sha256': history.sha(engine_path.read_bytes()), 'export_hashes': exports,
            'declarations': declarations, 'script_interface_count': len(COMMANDS), 'gui_binding_count': len(BINDINGS),
            'mod_sources': mod_sources, 'external_descriptor_sha256': history.sha(launcher.read_bytes()),
            'categories': categories, 'translation_count_references': languages,
            'current_native_hashes': native_hashes, 'native_entry_spans': native_objects,
            'followup_source_spans': sorted(followup_spans, key=lambda r: (r['path'], r['first_line'])),
            'widget': {'path': gui_path, 'sha256': history.sha(gui_bytes[1]), 'byte_identical_between_versions_and_installation': True},
            'native_picture': {'path': picture.relative_to(game).as_posix(), 'sha256': history.sha(picture.read_bytes())},
            'preserved_non_documentation_count': len(before),
            'preserved_non_documentation_inventory_sha256': history.sha(json.dumps(before, sort_keys=True).encode('utf-8')),
            'gameplay': 'not run', 'GUI': 'not run', 'multiplayer': 'not run', 'Tiger': 'not run',
            'limits': ['Subset syntax reader, not an Engine parser or complete Jomini validator',
                       'Category mappings/bindings and selected guards checked; dynamic execution/count equality not proven',
                       'Native source hashes and spans are retrieval evidence, not automatic semantic branch coverage',
                       'Script query/dispatch option initialization, hardcoded validation and lifecycle remain unknown where not documented']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='read-only recomputation; never rewrites evidence')
    args = parser.parse_args()
    result = collect()
    if args.check:
        assert result == json.loads(DEST.read_text(encoding='utf-8')), 'Static migration evidence drift'
    else:
        if DEST.exists():
            parser.error('Evidence exists; use --check. Preserve historical evidence.')
        history.write_json(DEST, result)
    print(json.dumps({'status': 'passed', 'script_interfaces': 14, 'gui_bindings': 3, 'categories': 5,
                      'languages': 8, 'mod_text_files': len(result['mod_sources']),
                      'current_native_hashes': len(result['current_native_hashes']),
                      'non_documentation_preserved': result['preserved_non_documentation_count'],
                      'runtime': 'not run'}, indent=2))
