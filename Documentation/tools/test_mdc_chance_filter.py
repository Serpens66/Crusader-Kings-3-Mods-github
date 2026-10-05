"""Static MDC routing/regression checks. These do not execute CK3 or certify MP."""
import hashlib
import json
import re
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
from check_mod_updates import lex

ROOT = Path(__file__).resolve().parents[2]
MOD = ROOT / 'Mass Demand Conversion'
GROUPS = ['direct_vassals', 'indirect_vassals', 'tributaries', 'courtiers', 'house']
MODES = ['none', '80', '100']
AUDIT = ROOT / 'Documentation/update-readiness/evidence/mdc-chance-filter-source-audit-20261005.json'


def read(path):
    return path.read_text(encoding='utf-8-sig')


def parse(text):
    """Small ordered structural reader, preserving repeated GUI actions."""
    tokens = [t[0] for t in lex(text)]
    position = 0

    def content(nested=False):
        nonlocal position
        rows = []
        while position < len(tokens):
            key = tokens[position]
            position += 1
            if key == '}':
                if not nested:
                    raise ValueError('Unexpected closing brace')
                return rows
            if position < len(tokens) and tokens[position] in ('=', '?=', '>=', '<', '!='):
                position += 1
            elif key == 'blockoverride':
                key += ' ' + tokens[position]
                position += 1
            else:
                rows.append((key, None))
                continue
            value = tokens[position]
            position += 1
            if value == '{':
                value = content(True)
            rows.append((key, value))
        if nested:
            raise ValueError('Unclosed brace')
        return rows

    return content()


def all_values(rows, key):
    return [value for name, value in rows if name == key]


def one(rows, key):
    values = all_values(rows, key)
    assert len(values) == 1, (key, len(values))
    return values[0]


def walk(rows):
    yield rows
    for _, value in rows:
        if isinstance(value, list):
            yield from walk(value)


def named(rows, name):
    return next(node for node in walk(rows) if ('name', '"' + name + '"') in node)


def slice_indices(expression):
    end, start = map(int, re.findall(r"\(int32\)(\d+)", expression))
    return list(range(start, end))


def tokens_hash(text):
    return hashlib.sha256(json.dumps([t[0] for t in lex(text)], ensure_ascii=False).encode()).hexdigest()


def dispatch_effect(decision):
    return [(k, v) for k, v in one(decision, 'effect') if k != 'custom_tooltip']


def evaluate_filter(expression, value):
    """Interpret only the native boolean subset used by display visibility/radio state."""
    tokens = re.findall(r"'[^']*'|[A-Za-z_.][A-Za-z_0-9.]*|[(),]", expression)
    index = 0

    def call():
        nonlocal index
        name = tokens[index]
        index += 1
        if name.startswith("'"):
            return name[1:-1]
        assert tokens[index] == '('
        index += 1
        args = [call()]
        while tokens[index] == ',':
            index += 1
            args.append(call())
        assert tokens[index] == ')'
        index += 1
        if name == 'GetVariableSystem.HasValue':
            assert args[0] == 'mdc_conversion_filter_ui'
            return value == args[1]
        if name == 'Not':
            assert len(args) == 1
            return not args[0]
        if name == 'Or':
            assert len(args) == 2
            return args[0] or args[1]
        if name == 'BoolTo1And2':
            return 1 if args[0] else 2
        raise AssertionError('Unexpected GUI function: ' + name)

    result = call()
    assert index == len(tokens)
    return result


class FilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decision_text = read(MOD / 'common/decisions/mod_mass_convert_subjects.txt')
        cls.decision = one(parse(cls.decision_text), 'mod_mass_convert_subjects_decision')
        cls.entries = all_values(one(cls.decision, 'widget'), 'item')
        cls.flags = [one(entry, 'value') for entry in cls.entries]
        cls.gui_text = read(MOD / 'gui/decision_view_widgets/mdc_decision_chance_filter.gui')
        cls.gui = parse(cls.gui_text)
        cls.triggers_text = read(MOD / 'common/scripted_triggers/mdc_chance_filter_triggers.txt')
        cls.triggers = parse(cls.triggers_text)
        cls.values_text = read(MOD / 'common/script_values/mod_mass_convert_subjects_values.txt')
        cls.values = parse(cls.values_text)

    def test_fixed_registration_and_default(self):
        expected = []
        for group in GROUPS[:3]:
            expected += ['mod_convert_' + group] + ['mdc_convert_' + group + '_' + mode for mode in MODES[1:]]
        expected += ['mod_convert_courtiers', 'mod_convert_house']
        self.assertEqual(self.flags, expected)
        self.assertEqual(one(self.entries[0], 'is_default'), 'yes')
        for entry in self.entries:
            self.assertFalse(all_values(entry, 'is_shown'))

    def test_five_visible_groups_each_mode(self):
        for mode in MODES:
            selected = []
            for group in GROUPS:
                node = named(self.gui, 'mdc_group_' + group + '_' + (mode if group in GROUPS[:3] else 'any'))
                if group in GROUPS[:3]:
                    self.assertTrue(evaluate_filter(one(node, 'visible'), mode))
                indices = slice_indices(one(node, 'datamodel'))
                self.assertEqual(len(indices), 1)
                selected.append(self.flags[indices[0]])
            self.assertEqual(len(selected), 5)

    def test_all_filter_switches_keep_group(self):
        # Interpret actual emitted datamodel slices and button actions, not a second routing table.
        for group in GROUPS:
            wrapper = named(self.gui, 'mdc_filter_for_' + group)
            self.assertEqual(one(wrapper, 'visible'), '"[Entry.IsSelected]"')
            buttons = []
            for node in walk(wrapper):
                if all_values(node, 'datamodel'):
                    index = slice_indices(one(node, 'datamodel'))[0]
                    button = one(one(node, 'item'), 'button_radio_label')
                    actions = all_values(button, 'onclick')
                    self.assertEqual(len(actions), 2)
                    self.assertIn('OnSelect(Entry.Self)', actions[0])
                    mode = re.search(r"'mdc_conversion_filter_ui', '(none|80|100)'", actions[1])[1]
                    self.assertIn(group, self.flags[index])
                    self.assertEqual(self.flags[index], 'mod_convert_' + group if mode == 'none' or group in GROUPS[3:] else 'mdc_convert_' + group + '_' + mode)
                    buttons.append(mode)
            self.assertEqual(buttons, MODES)

    def test_group_switch_uses_current_filter(self):
        for group in GROUPS:
            for mode in MODES:
                node = named(self.gui, 'mdc_group_' + group + '_' + (mode if group in GROUPS[:3] else 'any'))
                index = slice_indices(one(node, 'datamodel'))[0]
                button = one(one(node, 'item'), 'button_radio_label')
                self.assertIn('OnSelect(Entry.Self)', one(button, 'onclick'))
                expected = 'mdc_convert_' + group + '_' + mode if mode != 'none' and group in GROUPS[:3] else 'mod_convert_' + group
                self.assertEqual(self.flags[index], expected)

    def test_local_lifecycle_and_native_reset(self):
        root = one(self.gui, 'vbox')
        states = all_values(root, 'state')
        created = next(s for s in states if one(s, 'name') == 'mdc_initialize_on_create')
        self.assertEqual(one(created, 'trigger_on_create'), 'yes')
        self.assertIn("Set('mdc_conversion_filter_ui', 'none')", one(created, 'on_start'))
        hidden = next(s for s in states if one(s, 'name') == '_hide')
        self.assertIn("Clear('mdc_conversion_filter_ui')", one(hidden, 'on_start'))
        reset = named(self.gui, 'mdc_native_default_reset')
        self.assertEqual(slice_indices(one(reset, 'datamodel')), [0])
        child = one(one(reset, 'item'), 'widget')
        states = all_values(child, 'state')
        state = next(s for s in states if one(s, 'name') == 'mdc_select_default_on_create')
        shown = next(s for s in states if one(s, 'name') == '_show')
        self.assertIn('OnSelect(Entry.Self)', one(shown, 'on_start'))
        self.assertEqual(one(state, 'trigger_on_create'), 'yes')
        self.assertIn('OnSelect(Entry.Self)', one(state, 'on_start'))

    def test_gameplay_never_reads_ui_state(self):
        common = '\n'.join(read(p) for p in (MOD / 'common').rglob('*.txt'))
        self.assertNotIn('mdc_conversion_filter_ui', common)
        self.assertNotIn('demand_conversion_likelihood_calculation', common)
        self.assertNotIn('set_variable', self.triggers_text)
        self.assertNotIn('execute_threshold', '\n'.join(line.split('#')[0] for line in self.decision_text.splitlines()))

    def test_cutoff_helper_has_native_signature(self):
        query = one(one(self.triggers, 'mdc_vassal_conversion_cutoff_query'), 'is_character_interaction_potentially_accepted')
        self.assertEqual(query, [('recipient', '$RECIPIENT$'), ('interaction', 'demand_conversion_vassal_ruler_interaction'), ('ai_accept', '$MINIMUM$')])

    def test_none_query_and_threshold_flags(self):
        selected = one(self.triggers, 'mdc_selected_vassal_conversion_query')
        for branch, cutoff in [('trigger_if', '100'), ('trigger_else_if', '80')]:
            node = one(selected, branch)
            self.assertEqual(one(one(node, 'mdc_vassal_conversion_cutoff_query'), 'MINIMUM'), cutoff)
            flags = [key for key, _ in one(one(node, 'limit'), 'OR')]
            self.assertEqual(flags, ['scope:mdc_convert_' + g + '_' + cutoff for g in GROUPS[:3]])
        query = one(one(selected, 'trigger_else'), 'is_character_interaction_potentially_accepted')
        self.assertEqual(query, [('recipient', '$RECIPIENT$'), ('interaction', 'demand_conversion_vassal_ruler_interaction')])

    def test_filtered_count_helpers_and_empty_start(self):
        for group in GROUPS[:3]:
            for cutoff in MODES[1:]:
                count = one(self.values, 'mdc_convert_' + group + '_' + cutoff + '_number')
                self.assertEqual(one(count, 'value'), '0')
                helpers = [one(node, 'mdc_vassal_conversion_cutoff_query') for node in walk(count) if all_values(node, 'mdc_vassal_conversion_cutoff_query')]
                self.assertEqual(helpers, [[('RECIPIENT', 'prev'), ('MINIMUM', cutoff)]])

    def test_dispatch_only_after_fresh_query(self):
        effect = dispatch_effect(self.decision)
        for branch, group in zip(effect[:3], GROUPS[:3]):
            flags = one(one(branch[1], 'limit'), 'OR')
            self.assertEqual([key for key, _ in flags], ['scope:mod_convert_' + group] + ['scope:mdc_convert_' + group + '_' + mode for mode in MODES[1:]])
            guarded = [node for node in walk(branch[1]) if all_values(node, 'run_interaction')]
            self.assertEqual(len(guarded), 1)
            limit = one(guarded[0], 'limit')
            helpers = [one(node, 'mdc_selected_vassal_conversion_query') for node in walk(limit) if all_values(node, 'mdc_selected_vassal_conversion_query')]
            self.assertEqual(helpers, [[('RECIPIENT', 'prev')]])
            send = one(guarded[0], 'run_interaction')
            self.assertEqual(one(send, 'actor'), 'root')
            self.assertEqual(one(send, 'recipient'), 'this')
            self.assertEqual(one(send, 'send_threshold'), 'decline')

    def test_unfiltered_and_other_group_regressions(self):
        baseline = json.loads(read(AUDIT))['preserved_token_hashes']
        # Hash the actual ordered trees, preserving duplicate keys and conditions.
        actual = {'is_shown': one(self.decision, 'is_shown')}
        for group in GROUPS:
            actual['mod_convert_' + group + '_number'] = one(self.values, 'mod_convert_' + group + '_number')
        effect = dispatch_effect(self.decision)
        actual['courtier_dispatch'] = effect[3][1]
        actual['house_dispatch'] = effect[4][1]
        for key, node in actual.items():
            self.assertEqual(hashlib.sha256(json.dumps(node, ensure_ascii=False).encode()).hexdigest(), baseline[key], key)

    def test_original_send_blocks_and_protection(self):
        baseline = json.loads(read(AUDIT))['preserved_token_hashes']
        sends = [one(node, 'run_interaction') for node in walk(dispatch_effect(self.decision)) if all_values(node, 'run_interaction')]
        self.assertEqual(hashlib.sha256(json.dumps(sends, ensure_ascii=False).encode()).hexdigest(), baseline['all_send_blocks'])
        for group in GROUPS[:2]:
            original = one(self.values, 'mod_convert_' + group + '_number')
            original_guards = [one(node, 'vassal_contract_has_flag') for node in walk(original) if all_values(node, 'vassal_contract_has_flag')]
            for mode in MODES[1:]:
                filtered = one(self.values, 'mdc_convert_' + group + '_' + mode + '_number')
                guards = [one(node, 'vassal_contract_has_flag') for node in walk(filtered) if all_values(node, 'vassal_contract_has_flag')]
                self.assertEqual(guards, original_guards)

    def test_filtered_counts_only_add_native_threshold(self):
        import copy
        for group in GROUPS[:3]:
            original = one(self.values, 'mod_convert_' + group + '_number')
            for mode in MODES[1:]:
                normalized = copy.deepcopy(one(self.values, 'mdc_convert_' + group + '_' + mode + '_number'))
                for node in walk(normalized):
                    for i, (key, value) in enumerate(node):
                        if key == 'mdc_vassal_conversion_cutoff_query':
                            self.assertEqual(one(value, 'MINIMUM'), mode)
                            node[i] = ('is_character_interaction_potentially_accepted', [
                                ('recipient', one(value, 'RECIPIENT')),
                                ('interaction', 'demand_conversion_vassal_ruler_interaction')])
                self.assertEqual(normalized, original, (group, mode))

    def test_dispatch_only_extends_selection_and_query(self):
        import copy
        baseline = json.loads(read(AUDIT))['preserved_token_hashes']
        for (_, branch), group in zip(dispatch_effect(self.decision)[:3], GROUPS[:3]):
            normalized = copy.deepcopy(branch)
            selection = one(normalized, 'limit')
            selection[:] = [('scope:mod_convert_' + group, 'yes')]
            for node in walk(normalized):
                for i, (key, value) in enumerate(node):
                    if key == 'mdc_selected_vassal_conversion_query':
                        node[i] = ('is_character_interaction_potentially_accepted', [
                            ('recipient', one(value, 'RECIPIENT')),
                            ('interaction', 'demand_conversion_vassal_ruler_interaction')])
            digest = hashlib.sha256(json.dumps(normalized, ensure_ascii=False).encode()).hexdigest()
            self.assertEqual(digest, baseline[group + '_dispatch'])

    def test_eight_localizations_complete(self):
        required = ['mdc_chance_filter_' + suffix for suffix in ['heading', 'none', '80', '100', 'scope_note', 'tooltip']]
        required += ['mdc_convert_' + group + '_' + mode + suffix for group in GROUPS[:3] for mode in MODES[1:] for suffix in ['_loc', '_tooltip']]
        files = list((MOD / 'localization').rglob('*.yml'))
        self.assertEqual(len(files), 8)
        for file in files:
            text = read(file)
            for key in required:
                self.assertEqual(len(re.findall(r'^ ' + key + r':', text, re.M)), 1, (file, key))
            for group in GROUPS[:3]:
                for mode in MODES[1:]:
                    line = re.search(r'^ mdc_convert_' + group + '_' + mode + r'_loc:.*$', text, re.M)[0]
                    self.assertIn('mdc_convert_' + group + '_' + mode + '_number', line)

    def test_unset_unknown_and_valid_modes_show_exactly_five_groups(self):
        for value in [None, '', 'unexpected', 'none', '80', '100']:
            expected_mode = value if value in ['80', '100'] else 'none'
            visible = []
            for group in GROUPS:
                variants = MODES if group in GROUPS[:3] else ['any']
                for mode in variants:
                    node = named(self.gui, 'mdc_group_' + group + '_' + mode)
                    if mode == 'any' or evaluate_filter(one(node, 'visible'), value):
                        visible.append((group, mode))
            self.assertEqual(visible, [(g, expected_mode if g in GROUPS[:3] else 'any') for g in GROUPS])
            wrapper = named(self.gui, 'mdc_filter_for_direct_vassals')
            buttons = [one(one(n, 'item'), 'button_radio_label') for n in walk(wrapper) if all_values(n, 'datamodel')]
            marked = [m for m, button in zip(MODES, buttons) if evaluate_filter(one(one(button, 'blockoverride "radio"'), 'frame'), value) == 1]
            self.assertEqual(marked, [expected_mode])

    def test_compact_row_bounds_scroll_and_no_permanent_explanation(self):
        def size(node, key):
            return tuple(int(k) for k, _ in one(node, key))
        root = one(self.gui, 'vbox')
        row = named(self.gui, 'mdc_filter_row')
        scroll = named(self.gui, 'mdc_recipient_scroll')
        for key in ['minimumsize', 'maximumsize']:
            self.assertEqual(size(root, key), (514, 250))
            self.assertEqual(size(row, key), (514, 32))
            self.assertEqual(size(scroll, key), (514, 210))
        self.assertEqual(one(root, 'spacing'), '8')
        self.assertNotIn('mdc_chance_filter_scope_note', self.gui_text)
        for group in GROUPS:
            wrapper = named(self.gui, 'mdc_filter_for_' + group)
            self.assertIn(wrapper, [v for n in walk(row) for k, v in n if k == 'hbox'])
            self.assertEqual(one(one(wrapper, 'text_single'), 'text'), '"mdc_chance_filter_heading"')
            columns = [n for n in walk(wrapper) if all_values(n, 'datamodel')]
            self.assertEqual(len(columns), 3)
            widths = sum(size(n, 'minimumsize')[0] for n in columns)
            self.assertLessEqual(size(one(wrapper, 'text_single'), 'size')[0] + widths + 3 * int(one(wrapper, 'spacing')), 514)

    def test_unconditional_effect_explanation_and_all_language_keys(self):
        effect = one(self.decision, 'effect')
        self.assertEqual(effect[0], ('custom_tooltip', 'mdc_mass_conversion_requests_effect'))
        self.assertEqual(len(dispatch_effect(self.decision)), 5)
        expected_keys = None
        for p in (MOD / 'localization').rglob('*.yml'):
            text = read(p)
            rows = re.findall(r'^ (\w+):(?:\d+)? "((?:\\.|[^"\\\r\n])*)"\r?$', text, re.M)
            self.assertEqual(len(rows), 35, str(p))
            loc = dict(rows)
            self.assertEqual(len(loc), 35)
            expected_keys = set(loc) if expected_keys is None else expected_keys
            self.assertEqual(set(loc), expected_keys)
            self.assertTrue(loc['mdc_mass_conversion_requests_effect'])
            self.assertTrue(loc['mdc_chance_filter_tooltip'].startswith('$mdc_chance_filter_scope_note$'))
            for value in loc.values():
                for key in re.findall(r'\$((?:mdc_|mod_)[^$]+)\$', value):
                    self.assertIn(key, loc)

    def test_encoding_and_balanced_source(self):
        for p in MOD.rglob('*'):
            if p.suffix not in ['.txt', '.yml', '.gui']:
                continue
            data = p.read_bytes()
            data.decode('utf-8-sig')
            if p.suffix in ['.txt', '.yml']:
                self.assertTrue(data.startswith(b'\xef\xbb\xbf'), str(p))
            if p.suffix in ['.txt', '.gui']:
                parse(data.decode('utf-8-sig'))


if __name__ == '__main__':
    unittest.main()
