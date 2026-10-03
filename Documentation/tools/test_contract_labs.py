"""Cross-file/reference checks and offline read-only collector acceptance tests."""
import hashlib
import json
import re
import shutil
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch
import capture_fixture_logs as collector
from build_local_reference import definitions
from verify_documentation import check_braces

DOC=Path(__file__).resolve().parents[1]

class FixtureContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine=json.loads((DOC/'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'))

    def test_independent_ids_bom_and_localizations(self):
        defs={};locs={};texts=[]
        for p in (DOC/'examples/contract-lab').rglob('*'):
            if not p.is_file() or p.suffix not in {'.txt','.yml'}:continue
            raw=p.read_bytes();self.assertTrue(raw.startswith(b'\xef\xbb\xbf'),str(p))
            self.assertNotIn(b'\n',raw.replace(b'\r\n',b''),str(p))
            text=raw.decode('utf-8-sig');texts.append(text)
            self.assertTrue(check_braces(text),str(p))
            if p.suffix=='.txt':
                for d in definitions(text):
                    self.assertTrue(d['key'].startswith('doclab_') or d['key']=='on_birthday',d)
                    if d['key'].startswith('doclab_'):
                        self.assertNotIn(d['key'],defs);defs[d['key']]=p
            else:
                language='english' if '/english/' in p.as_posix() else 'german'
                self.assertTrue(text.startswith('l_'+language+':'))
                locs[language]=set(re.findall(r'^\s+(doclab_\w+):',text,re.M))
        self.assertEqual(locs['english'],locs['german'])
        combined='\n'.join(texts)
        # All own script references must resolve as a definition or localized text.
        refs=set(re.findall(r'\bdoclab_\w+\b',re.sub(r'#[^\n]*','',combined)))
        self.assertFalse(refs-set(defs)-locs['english'])

    def test_gui_cross_package_and_assets_resolve(self):
        text=(DOC/'examples/gui-frame-lab/gui/doclab_panel.gui').read_text(encoding='utf-8')
        self.assertTrue(check_braces(text))
        targets=re.findall(r"GetScriptedGui\('([^']+)'\)",text)
        self.assertEqual(set(targets),{'doclab_panel_action'})
        own=(DOC/'examples/contract-lab/common/scripted_guis/doclab_guis.txt').read_text(encoding='utf-8-sig')
        self.assertIn('doclab_panel_action',own)
        for texture in re.findall(r'texture\s*=\s*"([^"]+)"',text):
            self.assertTrue((DOC/'examples/gui-frame-lab'/texture).is_file(),texture)
        for symbol in ['ScriptedGui.Execute','ScriptedGui.IsValid','ScriptedGui.IsShown','TopScope.SetRoot','Character.MakeScope']:
            self.assertTrue(any(x['name']==symbol for x in self.engine['entries']),symbol)

    def test_native_recipe_hashes_remain_current(self):
        rows=json.loads((DOC/'examples/native-recipe-audit.json').read_text(encoding='utf-8'))
        self.assertGreater(len(rows),10)
        for row in rows:
            self.assertTrue(row['full_file_read'])
            self.assertEqual(hashlib.sha256(Path(row['path']).read_bytes()).hexdigest(),row['sha256'])

class OfflineCollector(unittest.TestCase):
    def setUp(self):
        self.temp=DOC/('collector-test-'+uuid.uuid4().hex)
        self.temp.mkdir(mode=0o777)
        self.profile=self.temp/'profile';self.profile.mkdir(mode=0o777)
        (self.profile/'logs').mkdir(mode=0o777);(self.profile/'crashes').mkdir(mode=0o777)

    def tearDown(self):
        self.assertTrue(self.temp.resolve().is_relative_to(DOC.resolve()))
        shutil.rmtree(self.temp)

    def test_changed_logs_new_crash_and_no_source_mutation(self):
        log=self.profile/'logs/error.log';log.write_bytes(b'old\x97')
        settings=self.profile/'dlc_load.json';settings.write_bytes(b'{"enabled_mods":["test.mod"]}')
        crash=self.profile/'crashes/new';crash.mkdir(mode=0o777)
        (crash/'exception.txt').write_bytes(b'old crash')
        with patch.object(collector,'PROFILE',self.profile),patch.object(collector,'OUT',self.temp/'output'):
            begin=collector.collect('offline','begin')
            unchanged=collector.collect('offline','end')
            self.assertTrue(all(x['classification']=='byte-identical to begin' for x in unchanged['files']))
            self.assertTrue(all(x['copy'] is None for x in unchanged['files'] if x['relative'].startswith('crashes/')))
            log.write_bytes(b'new log')
            (crash/'exception.txt').write_bytes(b'new crash')
            (crash/'memory.dmp').write_bytes(b'do not copy')
            (crash/'savegame.ck3').write_bytes(b'do not copy')
            result=collector.collect('offline','end')
            self.assertEqual(len(result['files']),3)
            self.assertTrue(any(x['copy'] for x in result['files'] if x['relative'].startswith('crashes/')))
            self.assertEqual(settings.read_bytes(),b'{"enabled_mods":["test.mod"]}')
            self.assertEqual(log.read_bytes(),b'new log')
            for row in result['files']:
                if row['copy']:
                    self.assertEqual(hashlib.sha256((DOC/row['copy']).read_bytes()).hexdigest(),row['sha256'])
            self.assertFalse(result['errors'])

    def test_missing_begin_does_not_claim_freshness(self):
        (self.profile/'logs/error.log').write_bytes(b'log')
        with patch.object(collector,'PROFILE',self.profile),patch.object(collector,'OUT',self.temp/'output'):
            result=collector.collect('offline','end')
        self.assertIn('freshness unknown',result['files'][0]['classification'])

    def test_label_traversal_rejected_before_writing(self):
        with self.assertRaises(ValueError):collector.collect('../escape','begin')

if __name__=='__main__':unittest.main()
