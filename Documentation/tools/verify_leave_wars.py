"""Read-only structural regression checks for the targeted Leave Wars update.

These checks compare actual script tokens with the preserved original commit.
They are not a Jomini grammar/type validator or gameplay/GUI/MP tests.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

from check_mod_updates import assignments, decode, lex, sha, text_format

ROOT = Path(__file__).resolve().parents[2]
MOD = ROOT / 'Leave Wars'
AUDIT = ROOT / 'Documentation/update-readiness/evidence/leave-wars-source-audit-20261003.json'


def children(tokens):
    """Split a block into ordered assignment token lists; preserve duplicate keys."""
    assert tokens[2] == '{' and tokens[-1] == '}', tokens[:3]
    result, i = [], 3
    while i < len(tokens) - 1:
        begin = i
        assert tokens[i + 1] in {'=', '<', '>=', '?='}, tokens[i:i+4]
        i += 2
        if tokens[i] == '{':
            depth = 0
            while i < len(tokens):
                depth += (tokens[i] == '{') - (tokens[i] == '}')
                i += 1
                if depth == 0:
                    break
            assert depth == 0
        else:
            i += 1
        result.append(tokens[begin:i])
    return result


def one(nodes, key):
    found = [node for node in nodes if node[0] == key]
    assert len(found) == 1, (key, len(found))
    return found[0]


def load(relative, raw=None):
    return {row['symbol']: row['tokens'] for row in assignments(
        raw if raw is not None else (ROOT / relative).read_bytes())}


def baseline(relative, commit):
    return subprocess.check_output(['git', '-c', 'core.hooksPath=NUL', '-C', str(ROOT),
                                    'show', commit + ':' + relative])


def flat(nodes):
    return [token for node in nodes for token in node]


def has(tokens, sequence):
    return any(tokens[i:i+len(sequence)] == sequence for i in range(len(tokens)))


def check():
    audit = json.loads(AUDIT.read_text(encoding='utf-8'))
    commit = audit['original_commit']
    checks = []
    relative = 'Leave Wars/events/leave_war_mod_events.txt'
    old = load(relative, baseline(relative, commit))['leave_war_mod.0001']
    new = load(relative)['leave_war_mod.0001']
    old_options = [n for n in children(old) if n[0] == 'option']
    new_options = [n for n in children(new) if n[0] == 'option']
    assert len(old_options) == len(new_options) == 11
    expected_cleanup = [['clear_saved_scope', '=', name]
                        for name in ['leaving_war'] + [f'leaving_war_{n}' for n in range(1, 11)]]
    helpers = load('Leave Wars/common/scripted_effects/leave_war_mod_effects.txt')
    assert children(helpers['lw_mod_clear_war_scopes_effect']) == expected_cleanup
    for n, (before, after) in enumerate(zip(old_options[:10], new_options[:10]), 1):
        a, b = children(before), children(after)
        assert one(b, 'name') == one(a, 'name')
        guard = one(b, 'if')
        guarded = children(guard)
        gate = one(guarded, 'limit')
        assert children(gate) == [
            ['lw_mod_can_select_war_trigger', '=', '{', 'WAR', '=', f'scope:leaving_war_{n}', '}'],
            ['lw_mod_can_pay_war_exit_trigger', '=', 'yes']]
        effects = [node for node in guarded if node[0] != 'limit']
        preserved = [token for token in flat(effects)]
        addition = ['lw_mod_war_departure_commitments_effect', '=', 'yes']
        assert sum(preserved[i:i+3] == addition for i in range(len(preserved))) == 1
        i = next(i for i in range(len(preserved)) if preserved[i:i+3] == addition)
        del preserved[i:i+3]
        original_effects = [node for node in a if node[0] not in {'name','trigger','show_as_unavailable','clear_saved_scope'}]
        assert preserved == flat(original_effects), ('legacy effects changed', n)
        # No payment, message, opinion or departure is outside the live effect guard.
        assert [node for node in b if node[0] not in {'name','trigger','show_as_unavailable','if'}] == expected_cleanup
        for key in ('trigger','show_as_unavailable'):
            original = one(a, key)
            changed = one(b, key)
            replaced = ['lw_mod_can_select_war_trigger', '=', '{', 'WAR', '=', f'scope:leaving_war_{n}', '}']
            assert has(changed, replaced)
            j = next(j for j in range(len(changed)) if changed[j:j+7] == replaced)
            restored = changed[:j] + ['exists', '=', f'scope:leaving_war_{n}'] + changed[j+7:]
            assert restored == original, ('legacy option eligibility changed beyond war guard', n, key)
    cancel = children(new_options[-1])
    assert one(cancel, 'lw_mod_clear_war_scopes_effect') == ['lw_mod_clear_war_scopes_effect','=','yes']
    assert one(cancel, 'name') == one(children(old_options[-1]), 'name')
    checks.append('All ten guarded branches preserve every legacy effect, preview price and explicit cleanup; cancel cleans all eleven scopes.')

    interaction = load('Leave Wars/common/character_interactions/leave_war_mod_interaction.txt')['leave_war_interaction_mod']
    fields = children(interaction)
    assert has(one(fields,'is_available'), ['is_ai','=','no'])
    assert has(one(fields,'is_available'), ['is_landless_adventurer','=','no'])
    assert has(one(fields,'is_shown'), ['lw_mod_can_leave_war_trigger','=','yes'])
    send = children(one(fields,'on_send'))
    assert send[0] == ['lw_mod_clear_war_scopes_effect','=','yes']
    assert has(one(send,'scope:recipient'), ['lw_mod_can_leave_war_trigger','=','yes'])
    triggers = load('Leave Wars/common/scripted_triggers/leave_war_mod_triggers.txt')
    permission = triggers['lw_mod_can_leave_war_trigger']
    for required in [ ['exists','=','scope:actor'], ['exists','=','scope:recipient'],
                      ['is_war_leader','=','scope:recipient'], ['NOT','=','{','is_war_leader','=','scope:actor','}'],
                      ['AND','=','{','is_attacker','=','scope:actor','is_attacker','=','scope:recipient','}'],
                      ['AND','=','{','is_defender','=','scope:actor','is_defender','=','scope:recipient','}'] ]:
        assert has(permission, required)
    assert has(triggers['lw_mod_can_select_war_trigger'], ['limit','=','{','exists','=','$WAR$','}'])
    assert has(triggers['lw_mod_can_select_war_trigger'], ['trigger_else','=','{','always','=','no','}'])
    checks.append('Display, enumeration, all ten option guards and execution share current war permission; absent selection fails closed; AI/adventurers excluded.')

    departure = helpers['lw_mod_war_departure_commitments_effect']
    actor = children(one(children(departure), 'scope:actor'))
    contract, personality = [node for node in actor if node[0] == 'if']
    assert children(one(children(contract),'limit')) == [
        ['has_variable','=','owed_contract_assistance_war'],
        ['var:owed_contract_assistance_war','=','scope:leaving_war']]
    assert [node[2] for node in children(contract) if node[0] == 'remove_variable'] == [
        'owed_contract_assistance_war','owed_contract_assistance_contribution','owed_contract_assistance_gold']
    failure = one(children(contract), 'if')
    assert children(one(children(failure), 'limit')) == [['has_game_rule','=','lw_mod_contract_failure_on']]
    assert one(children(failure), 'add_character_flag') == ['add_character_flag','=','{','flag','=','fp2_contract_assistance_failure','years','=','10','}']
    assert children(one(children(personality), 'limit')) == [['has_game_rule','=','lw_mod_personality_on']]
    assert one(children(personality), 'stress_impact') == ['stress_impact','=','{','loyal','=','40','just','=','20','disloyal','=','-30','callous','=','-5','arbitrary','=','-5','}']
    frankokratia = one(children(departure), 'if')
    assert has(frankokratia, ['using_cb','=','crusading_claim_cb'])
    assert has(frankokratia, ['every_war_attacker','=','{'])
    assert has(frankokratia, ['type','=','frankokratia_story'])
    assert has(frankokratia, ['remove_list_variable','=','{','name','=','frankokratia_leaders','target','=','scope:actor','}'])
    assert not any(token.startswith('random_') for token in departure)
    assert not has(departure, ['stress_and_fulfillment_impact','='])
    checks.append('Only matching promise is abandoned; independently gated failure flag (10 years) and exact additive pure-stress profile; Frankokratia is selected-war-scoped, without random war selection.')

    rules_rel = 'Leave Wars/common/game_rules/leave_war_mod_rules.txt'
    rules = load(rules_rel)
    assert rules['leave_war_mod_costs'] == load(rules_rel,baseline(rules_rel,commit))['leave_war_mod_costs']
    for key in ('lw_mod_personality','lw_mod_contract_failure'):
        assert one(children(rules[key]),'default')[2] == key+'_on'
        assert len(children(rules[key])) == 3
    messages = load('Leave Wars/common/messages/leave_war_mod_messages.txt')
    for key,value in [('serp_msg_war_ally_removed','war_participation_ally'),('serp_msg_war_enemy_removed','war_participation_enemy'),('serp_msg_war_player_removed','war_participation')]:
        assert one(children(messages[key]),'message_filter_type')[2] == value
    checks.append('Six old settings retained; both new rules default on and independently disabled; all three native message filters present.')

    sets = []
    new_keys = set()
    for path in sorted((MOD/'localization').rglob('*.yml')):
        text = decode(path.read_bytes())
        original_text = decode(baseline(path.relative_to(ROOT).as_posix(), commit))
        assert text.startswith(original_text), ('original localization changed',path)
        keys = re.findall(r'^\s+([\w.]+):\s*"',text,re.M)
        assert len(keys) == len(set(keys)) == 50
        for line in text.splitlines()[1:]:
            if re.match(r'^\s+[\w.]+:',line):
                assert re.fullmatch(r'\s+[\w.]+:\s*"(?:[^"\\]|\\.)*"',line), (path,line)
        sets.append(set(keys));new_keys.update(key for key in keys if key.startswith(('rule_lw_mod','setting_lw_mod','lw_mod_')))
    assert len(sets)==7 and all(s==sets[0] for s in sets)
    referenced = {m.group(1) for path in MOD.rglob('*.txt')
                  for m in re.finditer(r'custom_tooltip\s*=\s*(lw_mod_\w+)', decode(path.read_bytes()))}
    assert referenced <= sets[0]
    assert len(new_keys)==12
    checks.append('Seven languages have the same 50 unique keys; original strings retained byte-for-text; all new tooltip/rule keys provided.')

    for path in MOD.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        if path.suffix in {'.txt','.yml'}:
            assert raw.startswith(b'\xef\xbb\xbf'), path
            raw.decode('utf-8-sig')
        if path.suffix == '.txt':
            assignments(raw)
        if rel in audit['original_mod_files']:
            current = text_format(raw)
            prior = audit['original_mod_files'][rel]['format']
            assert current['utf8_bom'] == prior['utf8_bom']
            assert bool(current['bare_lf']) == bool(prior['bare_lf'])
            assert bool(current['crlf']) == bool(prior['crlf'])
    unchanged = ['Leave Wars.mod','Leave Wars/descriptor.mod','Leave Wars/thumbnail.png',
                 'Leave Wars/common/opinion_modifiers/leave_war_mod_opinions.txt',
                 'Leave Wars/common/script_values/leave_war_mod_cost_values.txt',
                 'Leave Wars/common/effect_localization/leave_war_mod_effect_loc.txt']
    for rel in unchanged:
        assert sha((ROOT/rel).read_bytes()) == audit['original_mod_files'][rel]['sha256'], rel
    bundle = subprocess.check_output(['git','-c','core.hooksPath=NUL','-C',str(ROOT),'status','--porcelain','--','SerpInteractionsDecisions'])
    assert not bundle, 'bundle changed'
    checks.append('All scripts structurally balanced; UTF-8 BOM and existing newline conventions retained; amounts, opinions, effect text, descriptors, thumbnail and bundle unchanged.')
    return {'game_version': '1.20.0.3', 'static_status': 'passed', 'checks': checks,
            'runtime': {'gameplay': 'not_run', 'gui': 'not_run', 'multiplayer': 'not_run', 'external_validator': 'not_run'},
            'limits': ['Token/structure and preservation checks do not establish Jomini engine behavior or runtime compatibility.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    result = check()
    if args.json:
        print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        for line in result['checks']:
            print('PASS:',line)
        print('Gameplay, GUI, multiplayer and external validator: NOT RUN.')
