"""Audit/verify MDC notifications without launching CK3 or replacing old evidence."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

from collect_mass_conversion_audit import objects, preservation
from audit_mass_conversion_migration import parse, get, leaves
from verify_documentation import check_braces

ROOT = Path(__file__).resolve().parents[2]
GAME = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
EVIDENCE = ROOT / 'Documentation/update-readiness/evidence'
AUDIT = EVIDENCE / 'mass-conversion-notification-audit-20261003.json'
VERIFY = EVIDENCE / 'mass-conversion-notification-verification-20261003.json'
EVENTS = {
    'religious_interaction.2002': ('events/religion_events/religious_interaction_events.txt', 'events/religion_events/accept_conversion_notification.txt'),
    'char_interaction.0181': ('events/interaction_events/character_interaction_events.txt', 'events/interaction_events/mdc_house_conversion_notification.txt'),
}
PINS = {'1.19.0.6': '85e1ca4fcee5a1e2238b9db13c70a335fa94dac8', '1.20.0.3': '0ec13350cde9e410b37a46d3616966838f4ba994'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return path.read_text(encoding='utf-8-sig')


def save_new(path, data):
    # Exclusive creation protects earlier reports/baselines.
    with path.open('xb') as stream:
        stream.write((json.dumps(data, ensure_ascii=False, indent=2) + '\n').replace('\n', '\r\n').encode('utf-8'))


def audit():
    version = GAME.parent / 'launcher/launcher-settings.json'
    result = {'date': '2026-10-03', 'game_root': str(GAME), 'version': json.loads(read(version))['version'],
              'launcher_sha256': sha(version.read_bytes()), 'native_sources': {}, 'historical': {},
              'before_workspace': preservation(ROOT),
              'before_documentation': {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in (ROOT / 'Documentation').rglob('*') if p.is_file() and '__pycache__' not in p.parts}}
    assert result['version'] == '1.20.0.3 (Crozier)'
    paths = ['events/_events.info', 'common/messages/_messages.info', 'common/messages/00_messages.txt',
             'common/messages/01_religious_messages.txt', 'common/messages/01_artifact_messages.txt',
             'common/messages/10_pam_messages.txt', 'common/character_interactions/00_religious_interactions.txt',
             'common/scripted_effects/00_interaction_effects.txt', 'common/scripted_effects/00_religious_interaction_effects.txt',
             'common/script_values/00_basic_values.txt', 'common/script_values/07_ep3_values.txt',
             'localization/english/messages_l_english.yml'] + [v[0] for v in EVENTS.values()]
    for rel in paths:
        raw = (GAME / rel).read_bytes()
        result['native_sources'][rel] = sha(raw)
        for version_name, commit in PINS.items():
            proc = subprocess.run(['git', '-C', str(ROOT / '.reference-cache/ck3-mod-base'), 'show', commit + ':base/game/' + rel], capture_output=True)
            if proc.returncode:
                assert b'does not exist' in proc.stderr or b'exists on disk, but not in' in proc.stderr, proc.stderr
                result['historical'].setdefault(version_name, {})[rel] = {'commit': commit, 'absent': True}
                continue
            blob = proc.stdout
            result['historical'].setdefault(version_name, {})[rel] = {'commit': commit, 'sha256': sha(blob), 'matches_installed': blob == raw}
            if rel in [v[0] for v in EVENTS.values()]:
                result['historical'][version_name][rel]['events'] = {n: {'lines': [s, e], 'text': b} for n, s, e, b in objects(blob.decode('utf-8-sig')) if n in EVENTS}
                print(version_name, rel, 'matches installed:', blob == raw)
                if version_name == '1.19.0.6':
                    for row in result['historical'][version_name][rel]['events'].values():
                        print(row['text'])
    interactions = read(GAME / 'common/character_interactions/00_religious_interactions.txt')
    result['callers'] = []
    for n, s, e, body in objects(interactions):
        for event in EVENTS:
            for match in re.finditer(r'trigger_event\s*=\s*' + re.escape(event) + r'\b', body):
                result['callers'].append({'interaction': n, 'event': event, 'line': s + body.count('\n', 0, match.start()), 'interaction_lines': [s, e], 'event_receiver': 'scope:puppet_or_actor'})
    assert len(result['callers']) == 4
    engine = json.loads(read(ROOT / 'Documentation/reference/engine-1.20.0.3.json'))
    names = ['send_interface_message', 'show_as_tooltip', 'change_influence', 'add_piety', 'change_fervor', 'add_prestige', 'trigger_event', 'send_interface_toast']
    result['exports'] = {n: [e for e in engine['entries'] if e['name'] == n] for n in names}
    assert all(result['exports'].values())
    for rows in result['exports'].values():
        for row in rows:
            assert sha((ROOT / 'Documentation' / row['source']['path']).read_bytes()) == row['source']['sha256']
    result['audit_boundary'] = 'Complete source audit for replacing these two acceptance notifications only; unchanged query/dispatch Engine defaults and runtime behavior remain open.'
    save_new(AUDIT, result)
    print('Source/export/original-state evidence saved:', AUDIT)


def verify():
    from urllib.parse import unquote, urlsplit
    baseline = json.loads(read(AUDIT))
    mod = ROOT / 'Mass Demand Conversion'
    allowed = {'Mass Demand Conversion.mod', 'Mass Demand Conversion/descriptor.mod',
               'Mass Demand Conversion/events/religion_events/accept_conversion_notification.txt',
               'Mass Demand Conversion/events/interaction_events/mdc_house_conversion_notification.txt',
               'Mass Demand Conversion/common/messages/mdc_conversion_messages.txt'}
    langs = ['english', 'german', 'french', 'spanish', 'polish', 'russian', 'korean', 'simp_chinese']
    allowed.update('Mass Demand Conversion/localization/' + lang + '/mod_mass_convert_subjects_l_' + lang + '.yml' for lang in langs)
    current = preservation(ROOT)
    changed = {p for p in set(current) | set(baseline['before_workspace']) if current.get(p) != baseline['before_workspace'].get(p)}
    assert changed == allowed, changed ^ allowed
    for rel, expected in baseline['native_sources'].items():
        assert sha((GAME / rel).read_bytes()) == expected, rel
    version = GAME.parent / 'launcher/launcher-settings.json'
    assert sha(version.read_bytes()) == baseline['launcher_sha256']
    historical = json.loads(read(ROOT / 'Documentation/research/vanilla-history-20261003.json'))
    for row in historical['installation_comparison']:
        assert sha((GAME / row['path']).read_bytes()) == row['installed_sha256'] == row['mirror_sha256'], row['path']
    for path in [mod / 'descriptor.mod', ROOT / 'Mass Demand Conversion.mod']:
        text = read(path)
        assert re.search(r'version\s*=\s*"1\.078"', text)
        assert re.search(r'supported_version\s*=\s*"1\.20\.\*"', text)
        assert 'remote_file_id="2753176859"' in text
        restored = path.read_bytes().replace(b'version="1.078"', b'version="1.077"').replace(b'supported_version="1.20.*"', b'supported_version="1.19.*"')
        assert sha(restored) == baseline['before_workspace'][path.relative_to(ROOT).as_posix()], 'Other metadata/encoding changed'
    checks = {}
    for event, (native_rel, mod_rel) in EVENTS.items():
        native = next(b for n, s, e, b in objects(read(GAME / native_rel)) if n == event)
        original = get(parse(native), event)[0]
        text = read(mod / mod_rel)
        parsed = parse(text)
        assert [k for k, op, val in parsed] == ['namespace', event]
        assert get(parsed, 'namespace') == [event.split('.')[0]]
        replacement = get(parsed, event)[0]
        assert get(replacement, 'id_override_priority') == ['1']
        assert get(replacement, 'hidden') == ['yes']
        assert get(replacement, 'type') == ['character_event']
        assert not get(replacement, 'option')
        new_immediate = get(replacement, 'immediate')[0]
        message = get(new_immediate, 'send_interface_message')[0]
        assert get(message, 'type') == ['mdc_conversion_accepted_message']
        assert get(message, 'left_icon') == ['scope:recipient']
        gameplay = [row for row in new_immediate if row[0] != 'send_interface_message']
        old_immediate = get(original, 'immediate')[0]
        old_option = [row for row in get(original, 'option')[0] if row[0] != 'name']
        if event == 'religious_interaction.2002':
            assert gameplay == old_immediate[2:] + old_option, 'Gameplay blocks differ'
            assert message[2:] == old_immediate[:2], 'Government-specific previews differ'
        else:
            assert gameplay == old_immediate
            assert message[2:] == old_option
        conversions = [row for row in leaves(new_immediate) if row[1] in {'demand_conversion_interaction_effect', 'demand_conversion_vassal_ruler_interaction_effect'}]
        assert conversions and all('show_as_tooltip' in row[0] for row in conversions)
        def reward_nodes(rows, path=()):
            found = []
            for key, op, val in rows:
                if key in {'add_piety', 'change_influence', 'change_fervor', 'add_prestige'}:
                    found.append((path, key))
                if isinstance(val, list):
                    found += reward_nodes(val, path + (key,))
            return found
        rewards = reward_nodes(new_immediate)
        assert not any('send_interface_message' in path for path, key in rewards)
        assert len(rewards) == (4 if event == 'religious_interaction.2002' else 0)
        assert len(get(new_immediate, 'notify_puppeteer_of_outcome_effect')) == 1
        checks[event] = {'gameplay_ast_identical': True, 'preview_ast_identical': True,
                         'conversion_calls_tooltip_only': len(conversions), 'explicit_reward_calls': len(rewards),
                         'puppet_helper_calls': 1, 'hidden': True, 'priority': 1}
    message = get(parse(read(mod / 'common/messages/mdc_conversion_messages.txt')), 'mdc_conversion_accepted_message')[0]
    for key, value in [('display', 'feed'), ('combine_into_one', 'yes'), ('icon', '"religious"'), ('style', 'good'),
                       ('title', 'mdc_conversion_accepted_title'), ('desc', 'mdc_conversion_accepted_desc'), ('tooltip', 'event_message_effect')]:
        assert get(message, key) == [value]
    assert not get(message, 'message_filter_type')
    for lang in langs:
        text = read(mod / ('localization/' + lang + '/mod_mass_convert_subjects_l_' + lang + '.yml'))
        assert text.startswith('l_' + lang + ':')
        for key in ['mdc_conversion_accepted_title', 'mdc_conversion_accepted_desc']:
            assert len(re.findall(r'^ ' + key + r':0 "[^"\n]+"\s*$', text, re.M)) == 1
        assert '[recipient.GetShortUIName]' in text
        raw = (mod / ('localization/' + lang + '/mod_mass_convert_subjects_l_' + lang + '.yml')).read_bytes()
        prefix = raw[:raw.index(b'\n # Acceptance only;')]
        rel = 'Mass Demand Conversion/localization/' + lang + '/mod_mass_convert_subjects_l_' + lang + '.yml'
        assert sha(prefix) == baseline['before_workspace'][rel], 'Original localization changed'
        native_loc = '\n'.join(read(p) for p in (GAME / 'localization' / lang).rglob('*messages*l_' + lang + '.yml'))
        assert re.search(r'^\s*event_message_effect:', native_loc, re.M), lang
    # Locate any additional native consumers without relying on a retrieval index.
    callsites = []
    collisions = []
    for path in GAME.rglob('*'):
        if not path.is_file() or path.suffix not in {'.txt', '.yml'}:
            continue
        # ASCII identifiers can be inventoried without assuming all Vanilla text is UTF-8.
        raw = path.read_bytes()
        if b'mdc_conversion_accepted' in raw:
            collisions.append(str(path))
        for match in re.finditer(rb'trigger_event\s*=\s*(religious_interaction\.2002|char_interaction\.0181)\b', raw):
            callsites.append({'path': path.relative_to(GAME).as_posix(), 'line': raw.count(b'\n', 0, match.start()) + 1, 'event': match.group(1).decode('ascii')})
    assert not collisions
    assert {(row['line'], row['event']) for row in callsites} == {(row['line'], row['event']) for row in baseline['callers']}
    authored_docs = {
        'Documentation/tools/audit_mass_conversion_notifications.py',
        'Documentation/update-readiness/mods/mass-demand-conversion-notifications-20261003.md',
        'Documentation/update-readiness/mods/mass-demand-conversion.md',
        'Documentation/update-readiness/mods/mass-demand-conversion-tests.md',
        *('Documentation/update-readiness/contracts/MC-' + name + '.md' for name in ['CANDIDATES', 'DISPATCH', 'VARIANTS']),
        'Documentation/update-readiness/evidence/mass-conversion-notification-audit-20261003.json',
    }
    docs_current = {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in (ROOT / 'Documentation').rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    docs_changed = {p for p in set(docs_current) | set(baseline['before_documentation']) if docs_current.get(p) != baseline['before_documentation'].get(p)}
    assert docs_changed <= authored_docs | {VERIFY.relative_to(ROOT).as_posix()}, docs_changed - authored_docs
    encoding_count = 0
    links_count = 0
    for rel in sorted(allowed | authored_docs):
        path = ROOT / rel
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig')
        preserved_lf = path.suffix == '.mod' or rel.startswith('Mass Demand Conversion/localization/')
        if preserved_lf:
            assert b'\r' not in raw, rel
        else:
            assert b'\n' not in raw.replace(b'\r\n', b'') and b'\r' not in raw.replace(b'\r\n', b''), rel
        if path.suffix in {'.txt', '.yml'}:
            assert raw.startswith(b'\xef\xbb\xbf'), rel
        if path.suffix == '.txt':
            assert check_braces(text), rel
            parse(text)
        encoding_count += 1
        if path.suffix == '.md':
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)', text):
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                resolved = (path.parent / unquote(target.split('#', 1)[0])).resolve()
                assert resolved.exists() or resolved == VERIFY, (rel, target)
                links_count += 1
    result = {'status': 'passed', 'date': '2026-10-03', 'version': baseline['version'], 'events': checks,
              'languages': langs, 'native_callers': callsites, 'native_hashes_checked': len(baseline['native_sources']),
              'historical_seed_hashes_checked': len(historical['installation_comparison']), 'changed_mod_files': sorted(changed),
              'unchanged_non_documentation_files': len(current) - len(changed), 'encoding_files_checked': encoding_count,
              'documentation_links_checked': links_count, 'mod_sha256': {p: current[p] for p in sorted(changed)},
              'gameplay': 'not run', 'GUI': 'not run', 'multiplayer': 'not run', 'Tiger': 'not run',
              'limits': 'Subset parser and source/AST comparison; no Engine load or runtime exactly-once proof.'}
    if VERIFY.exists():
        assert result == json.loads(read(VERIFY)), 'Verification drift; preserve original evidence'
    else:
        save_new(VERIFY, result)
    assert VERIFY.exists()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['audit', 'verify'])
    args = parser.parse_args()
    audit() if args.mode == 'audit' else verify()
