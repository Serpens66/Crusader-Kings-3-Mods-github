"""Verify conservation and retrieval; no CK3 launch or source changes."""
import hashlib
import json
import subprocess
import sys
import unittest
from build_engine_reference import DOC, decode, parse


class EngineReferenceTests(unittest.TestCase):
    def test_duplicate_datatypes_survive(self):
        text = 'GetPlayer\nDefinition type: Global promote\nReturn type: Character\n\n-----------------------\nGetPlayer( Arg0 )\nDefinition type: Global function\nReturn type: [unregistered]\n'
        entries, spans = parse(text, 'datatype', {'path': 'fixture'})
        self.assertEqual([e['name'] for e in entries], ['GetPlayer', 'GetPlayer'])
        self.assertEqual(''.join(s['text'] for s in spans), text)

    def test_unknown_tail_is_preserved(self):
        text = 'Effect Documentation:\n--------------------\nx - description\nSupported Scopes: none\n--------------------\nUnexplained tail!\n'
        entries, spans = parse(text, 'effect', {'path': 'fixture'})
        self.assertEqual(entries[0]['supported_scopes'], ['none'])
        self.assertEqual(spans[-1]['kind'], 'unparsed')
        self.assertEqual(''.join(s['text'] for s in spans), text)

    def test_scope_modifier_and_saved_target(self):
        for category, text, expected in [
            ('scope', 'Scope Types:\ncharacter:\nStores Variables: yes\n', 'character'),
            ('modifier', 'Printing Modifier Definitions:\nTag: $TYPE$_opinion\nUse areas: character\n', '$TYPE$_opinion'),
            ('target', 'Event Targets Saved from Code:\nactor\nactor\n', 'actor')]:
            entries, spans = parse(text, category, {'path': 'fixture'})
            self.assertEqual(entries[0]['name'], expected)
            self.assertEqual(''.join(s['text'] for s in spans), text)
        self.assertEqual(len(entries), 2)

    def test_decode_keeps_non_utf8_bytes(self):
        raw = b'engine \x97 text'
        text, encoding, note = decode(raw)
        self.assertEqual(text.encode(encoding), raw)
        self.assertIn('candidate', note)

    def test_all_real_sources_conserved_and_hash_verified(self):
        index = json.loads((DOC / 'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'))
        self.assertEqual(len(index['sources']), 11)
        for source, coverage in zip(index['sources'], index['coverage']):
            raw = (DOC / source['path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), source['sha256'])
            self.assertEqual(''.join(s['text'] for s in coverage['segments']), raw.decode(source['decode_encoding']))
            previous = 0
            for segment in coverage['segments']:
                self.assertEqual(segment['start'], previous + 1)
                previous = segment['end']
            self.assertEqual(previous, coverage['lines'])

    def test_lookup_categories_and_context(self):
        for symbol, expected in [('save_temporary_scope_as', ['engine/effect', 'engine/trigger']),
                                 ('TryStartRulerDesigning', ['engine/datatype', 'Arg0, Arg1']),
                                 ('is_alive', ['engine/trigger', 'Supported Scopes: character'])]:
            result = subprocess.run([sys.executable, '-B', str(DOC / 'tools/lookup.py'), symbol, '--context', '1'],
                                    capture_output=True, check=True, encoding='utf-8', errors='replace',
                                    env={**__import__('os').environ, 'PYTHONIOENCODING': 'utf-8'})
            for text in expected:
                self.assertIn(text, result.stdout)


if __name__ == '__main__':
    unittest.main()
