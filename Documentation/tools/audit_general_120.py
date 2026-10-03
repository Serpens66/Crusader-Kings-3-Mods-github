"""Collect/check dated documentation evidence without launching CK3.

Build writes the new supplement; --check writes only a fresh report. Native reads and
lexical field locations are retrieval evidence, not a semantic gameplay audit.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from workspace_walk import workspace_files
from urllib.parse import unquote, urlsplit

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parent
GAME = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
DEST = OUT / 'research/general-120-evidence.json'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, text):
    path.write_bytes(text.replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8'))


def preserved():
    return {p.relative_to(ROOT).as_posix(): sha(p.read_bytes())
            for p in workspace_files(ROOT) if p.is_file()
            and p.relative_to(ROOT).parts[0] not in {'Documentation', '.git'}
            and '__pycache__' not in p.parts and p.suffix != '.pyc'}


def build():
    before = preserved()
    rows = json.loads((OUT / 'research/general-120-topics.json').read_text(encoding='utf-8'))
    engine = json.loads((OUT / 'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'))
    sources = {}
    # Complete reference reads support schema retrieval; no claim that all fields
    # or consumers in these databases were semantically audited.
    for p in GAME.rglob('*.info'):
        raw = p.read_bytes()
        try:
            text = raw.decode('utf-8-sig')
            encoding = 'utf-8-sig'
        except UnicodeDecodeError:
            text = raw.decode('utf-8', errors='replace')
            encoding = 'UTF-8 replacement for inventory only; exact textual claims need separate byte review'
        sources[p.relative_to(GAME).as_posix()] = {
            'sha256': sha(raw), 'lines': len(text.splitlines()), 'decoding': encoding}
    for row in rows:
        row['engine_hits'] = [dict(name=e['name'], category=e['category'], line=e['line'],
                                  source=e['source']) for e in engine['entries']
                              if e['name'] in row['symbols']]
        row['native_locations'] = []
        for rel in row['native_paths']:
            p = GAME / rel
            raw = p.read_bytes()
            text = raw.decode('utf-8-sig')
            lines = text.splitlines()
            sources[rel] = {'sha256': sha(raw), 'lines': len(lines), 'decoding': 'utf-8-sig'}
            hits = [i+1 for i, line in enumerate(lines)
                    if any(s in line for s in row['symbols'])]
            row['native_locations'].append({'path': rel, 'matching_lines': hits,
                                           'read_boundary': 'complete file'})
    after = preserved()
    if before != after:
        raise SystemExit('Non-Documentation changed while collecting')
    payload = {'date': '2026-10-03', 'version': '1.20.0.3', 'game_root': str(GAME),
               'version_sha256': sha((GAME.parent/'launcher/launcher-settings.json').read_bytes()),
               'boundary': 'Schema/declaration documentation supplement; not a completed semantic feature audit or runtime acceptance.',
               'sources': sources, 'topics': rows, 'preserved_non_documentation': before,
               'web_sources': [
                   {'url': 'https://store.steampowered.com/news/posts/?appids=1158310&feed=steam_community_announcements',
                    'accessed': '2026-10-03', 'sections': ['Diary #8 Modding, 2026-09-29', 'Release Modding, 2026-09-30', '1.20.0.3 hotfix, 2026-10-01'],
                    'role': 'Discovery and explicitly qualified developer/release notes; local API/schema details independently checked'},
                   {'url': 'https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Effects_list.md', 'role': 'Historical declaration mirror'},
                   {'url': 'https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Triggers_list.md', 'role': 'Historical abbreviated declaration mirror'},
                   {'url': 'https://github.com/amtep/tiger', 'role': 'Validator capabilities and limitations'},
                   {'url': 'https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/triggers.rs.html', 'role': 'Validator schema; header says CK3 1.18.1'},
                   {'url': 'https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/effects.rs.html', 'role': 'Validator schema; malformed update-version header'},
                   {'url': 'https://github.com/amtep/tiger/blob/main/filter.md', 'role': 'Validator filter configuration'},
                   {'url': 'https://github.com/amtep/tiger/blob/main/annotations.md', 'role': 'Validator suppression annotations'}],
               'runtime': 'not run', 'external_validator': 'not run',
               'historical_evidence': 'Unchanged; current AGENTS.md snapshot is preservation for this operation, not a rebaseline of earlier reports.'}
    write(DEST, json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    lines = ['# Crozier source coverage', '', 'Date: **2026-10-03**. Installed **1.20.0.3**. Runtime: **not run**.', '',
             'Every scoped discovery point is assigned below. Integrated means a sourced declaration/schema or an explicitly qualified note; it does not mean a working implementation. Native locations and whole-file hashes are in [evidence](general-120-evidence.json).', '',
             'Scope: diary #8 modding sections; 1.20 release Modding section and directly relevant correction/diagnostic notes; 1.20.0.3 hotfix; previously found interaction callers; Wiki declaration mirrors; Tiger README and trigger/effect tables plus configuration/suppression guides. Art/music production narratives and achievement lists are excluded because they do not specify modding contracts. Unrelated balance tuning is outside this documentation supplement.', '',
             '| ID | Topic / symbols | Treatment | Chapter | Evidence boundary / remaining question |',
             '|---|---|---|---|---|']
    for row in rows:
        lines.append('| '+row['id']+' | '+row['label']+' | '+row['status']+' | ['+row['chapter'].split('/')[-1]+'](../'+row['chapter']+') | '+row['limit']+' |')
    lines += ['', 'The machine record retains original symbol spelling and native paths. Some announcement names differ from the installation; those discrepancies are deliberate open findings, not normalized APIs. Each chapter distinguishes current local contracts from release-only observations. General Wiki tables do not supersede the local Engine index. No full game-text archive is distributed.']
    write(OUT/'research/crozier-source-coverage.md', '\n'.join(lines)+'\n')
    print(json.dumps({'topics': len(rows), 'native_sources': len(sources), 'preserved': len(before)}))


def check(report_path=None):
    data = json.loads(DEST.read_text(encoding='utf-8'))
    issues = []
    for rel, row in data['sources'].items():
        if sha((GAME/rel).read_bytes()) != row['sha256']:
            issues.append('Native drift: '+rel)
    if sha((GAME.parent/'launcher/launcher-settings.json').read_bytes()) != data['version_sha256']:
        issues.append('Version source drift')
    if preserved() != data['preserved_non_documentation']:
        issues.append('Non-Documentation drift during supplement')
    checked_exports = set()
    for row in data['topics']:
        for hit in row['engine_hits']:
            source = hit['source']
            if source['path'] not in checked_exports:
                checked_exports.add(source['path'])
                if sha((OUT/source['path']).read_bytes()) != source['sha256']:
                    issues.append('Export drift: '+source['path'])
    links = 0
    for p in OUT.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts or p.suffix not in {'.md', '.json', '.py', '.txt', '.yml', '.gui', '.mod'}:
            continue
        if any(s in p.relative_to(OUT).parts for s in {'runtime-evidence', 'run-evidence'}):
            continue
        raw = p.read_bytes()
        text = raw.decode('utf-8-sig')
        if p.suffix in {'.txt', '.yml'} and not raw.startswith(b'\xef\xbb\xbf'):
            issues.append('BOM: '+p.relative_to(OUT).as_posix())
        if b'\n' in raw.replace(b'\r\n', b''):
            issues.append('CRLF: '+p.relative_to(OUT).as_posix())
        if p.suffix == '.json':
            json.loads(text)
        if p.suffix == '.md':
            prose = re.sub(r'```.*?```', '', text, flags=re.S)
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)', prose):
                target = target.strip().strip('<>')
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                links += 1
                if not (p.parent/unquote(target.split('#')[0])).resolve().exists():
                    issues.append('Link: '+p.relative_to(OUT).as_posix()+' -> '+target)
    for row in data['topics']:
        if not row['status'] or not row['limit'] or not (OUT/row['chapter']).exists():
            issues.append('Incomplete coverage: '+row['id'])
    old = json.loads((OUT/'update-readiness/evidence/mass-conversion-audit-20261003.json').read_text(encoding='utf-8'))
    prior_drift = [p for p, h in old['preserved_non_documentation_files'].items()
                   if not (ROOT/p).exists() or sha((ROOT/p).read_bytes()) != h]
    result = {'date': '2026-10-03', 'status': 'failed' if issues else 'passed',
              'issues': issues, 'internal_links': links, 'native_hashes': len(data['sources']),
              'coverage_topics': len(data['topics']), 'export_hashes': len(checked_exports), 'preserved_non_documentation': len(data['preserved_non_documentation']),
              'historical_workspace_drift': prior_drift, 'historical_baseline_rewritten': False,
              'gameplay': 'not run', 'GUI': 'not run', 'multiplayer': 'not run', 'Tiger': 'not run'}
    # A fresh report only; earlier verification reports are intentionally retained.
    write(report_path or OUT/'research/general-120-verification.json', json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify sources and write only the fresh verification report')
    parser.add_argument('--report', type=Path, help='separate report destination inside Documentation; preserve historical checks')
    args = parser.parse_args()
    if args.report and not args.report.resolve().is_relative_to(OUT.resolve()):
        parser.error('--report must stay inside Documentation')
    check(args.report) if args.check else build()
