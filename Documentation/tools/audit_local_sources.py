"""Collect reproducible lexical dependency evidence for the documentation.

Reads complete developer .info files and representative sources, then follows
literal references to native scripted helpers/events/values in their full files.
This is discovery evidence; parameter-expanded and engine contracts need review.
"""
import collections
import hashlib
import json
import re
from pathlib import Path
from build_local_reference import OUT, write

def main():
    idx = json.loads((OUT/'reference/local-index.json').read_text(encoding='utf-8'))
    root = Path(idx['game_root'])
    records = {r['path']:r for r in idx['native']}
    helpers = collections.defaultdict(set)
    areas = ('common/scripted_effects/', 'common/scripted_triggers/', 'common/script_values/',
             'common/scripted_lists/', 'common/scripted_modifiers/', 'events/')
    for row in idx['native']:
        if row['path'].startswith(areas):
            for definition in row['definitions']:
                if definition['key'] != 'namespace':
                    helpers[definition['key']].add(row['path'])
    seeds = [row['path'] for row in idx['native'] if row['path'].endswith('.info')]
    seeds += ['common/character_interactions/00_gift.txt','common/on_action/birthday.txt',
              'common/scripted_guis/00_character.txt','common/scripted_guis/ce1_funeral_scripted_guis.txt',
              'common/scripted_guis/pam_scripted_guis.txt','common/scripted_lists/00_scripted_lists.txt',
              'common/scripted_triggers/00_activity_triggers.txt','common/scripted_effects/00_accolades_scripted_effects.txt',
              'common/script_values/00_basic_values.txt','common/modifiers/00_activity_feast_modifiers.txt',
              'common/defines/00_defines.txt','gui/window_knights.gui','gui/interaction_menu_window.gui',
              'gui/activity_window_widgets/funeral_deceased_selection_button.gui','gui/preload/textformatting.gui',
              'events/birth_events.txt']
    # One actual definition file per additional subsystem; .info contracts remain separate.
    for area in ['common/traits/','common/culture/cultures/','common/religion/faith_types/',
                 'common/religion/religion_types/','common/religion/rite_types/','common/landed_titles/',
                 'common/buildings/','common/casus_belli_types/','common/activities/activity_types/',
                 'common/travel/travel_options/','common/artifacts/templates/','common/schemes/',
                 'common/story_cycles/','common/lifestyles/','common/game_rules/','history/characters/',
                 'history/titles/','history/provinces/','map_data/geographical_regions/']:
        candidates = [row for row in idx['native'] if row['path'].startswith(area) and row['path'].endswith('.txt') and row['bytes'] > 200 and row['definitions']]
        if candidates:
            seeds.append(min(candidates,key=lambda x:x['bytes'])['path'])
    seeds += ['map_data/default.map']
    queue = collections.deque(sorted(set(seeds)))
    visited, edges, absent = {}, [], []
    while queue:
        rel = queue.popleft()
        if rel in visited:
            continue
        path = root/rel
        if not path.exists():
            absent.append(rel)
            continue
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig',errors='replace')
        visited[rel] = {'sha256':hashlib.sha256(raw).hexdigest(),'lines':len(text.splitlines()),'seed':rel in seeds}
        if rel.endswith('.info'):
            continue # schematic examples are not executable dependencies
        tokens = set(re.findall(r'[A-Za-z_][\w.]*', re.sub(r'#[^\n]*','',text)))
        own_keys = {x['key'] for x in records.get(rel,{}).get('definitions',[])}
        for token in sorted(tokens & helpers.keys() - own_keys):
            for target in sorted(helpers[token]):
                edges.append({'from':rel,'symbol':token,'to':target})
                if target not in visited:
                    queue.append(target)
    result = {'date':'2026-10-03','version':idx['installed_launcher_version'],
              'method':'Complete file reads; literal helper dependency closure; no engine/runtime proof or macro expansion.',
              'files':visited,'edges':edges,'absent_requested_files':absent}
    write('reference/audit-evidence.json', json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n')
    print(json.dumps({'full_files_read':len(visited),'literal_dependency_edges':len(edges),'missing':absent},indent=2))

if __name__ == '__main__':
    main()
