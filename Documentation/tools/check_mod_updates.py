"""Read-only CK3 source comparison. Changes require an audit, not an automatic patch.

The lexer preserves ordered tokens/repeated keys; it is not a Jomini validator.
No cache, baseline refresh, game launch, network request or output file is written.
"""
import argparse
import difflib
import hashlib
import json
import re
import struct
import subprocess
import sys
from collections import Counter
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / 'Documentation/update-readiness/update-watch-20261003.json'
BASELINE_INDEX = ROOT / 'Documentation/update-readiness/update-watch-index.json'
DEFAULT_GAME = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
ATOM = re.compile(r'[=<>!?]+|[^\s{}=<>!?#"]+')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def token_hash(tokens):
    return sha(json.dumps(tokens, ensure_ascii=False, separators=(',', ':')).encode('utf-8'))


def safe_relative(value):
    path = PurePosixPath(value)
    if not value or value.startswith('/') or '\\' in value or ':' in value or '..' in path.parts:
        raise ValueError('Expected a relative forward-slash path: ' + value)
    return path.as_posix()


def decode(raw):
    return raw.decode('utf-8-sig').replace('\r\n', '\n').replace('\r', '\n')


def lex(text):
    """Strict lexical boundaries; no interpretation of gameplay or field grammar."""
    tokens = []
    pos = 0
    while pos < len(text):
        char = text[pos]
        if char.isspace():
            pos += 1
        elif char == '#':
            end = text.find('\n', pos)
            pos = len(text) if end == -1 else end
        elif char == '"':
            start = pos
            pos += 1
            while pos < len(text):
                if text[pos] == '\\':
                    pos += 2
                elif text[pos] == '"':
                    pos += 1
                    tokens.append((text[start:pos], start, pos))
                    break
                else:
                    pos += 1
            else:
                raise ValueError('Unclosed quoted string')
        elif char in '{}':
            tokens.append((char, pos, pos + 1))
            pos += 1
        else:
            match = ATOM.match(text, pos)
            if match is None:
                raise ValueError('Unrecognized lexical boundary at ' + str(pos))
            end = match.end()
            tokens.append((match.group(), pos, end))
            pos = end
    return tokens


def assignments(raw):
    """Read top-level scalar/block assignments; reject ambiguous/unbalanced input."""
    text = decode(raw)
    tokens = lex(text)
    rows = []
    pos = 0
    while pos < len(tokens):
        start = pos
        # Native event files also contain named local scripted_effect/trigger declarations.
        if tokens[pos][0] in {'scripted_effect', 'scripted_trigger'} and pos + 3 < len(tokens) and tokens[pos + 2][0] == '=':
            pos += 1
        if pos + 2 >= len(tokens) or tokens[pos + 1][0] != '=' or tokens[pos][0] in '{}':
            raise ValueError('Unrecognized top-level assignment')
        name = tokens[pos][0]
        pos += 2
        if tokens[pos][0] == '{':
            depth = 0
            while pos < len(tokens):
                depth += (tokens[pos][0] == '{') - (tokens[pos][0] == '}')
                pos += 1
                if depth == 0:
                    break
            if depth:
                raise ValueError('Unbalanced block')
        else:
            if tokens[pos][0] == '}':
                raise ValueError('Unexpected closing brace')
            pos += 1
        values = [t[0] for t in tokens[start:pos]]
        begin, end = tokens[start][1], tokens[pos - 1][2]
        rows.append({'symbol': name, 'text': text[begin:end], 'tokens': values,
                     'token_sha256': token_hash(values), 'line': text.count('\n', 0, begin) + 1})
    return rows


def diff(old, new, old_label, new_label):
    return ''.join(difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True),
                                        fromfile=old_label, tofile=new_label))


def asset_header(raw):
    if raw.startswith(b'DDS ') and len(raw) >= 128:
        return {'container': 'DDS', 'width': struct.unpack_from('<I', raw, 16)[0],
                'height': struct.unpack_from('<I', raw, 12)[0], 'fourcc': raw[84:88].hex()}
    if raw.startswith(b'\x89PNG\r\n\x1a\n') and len(raw) >= 24:
        width, height = struct.unpack_from('>II', raw, 16)
        return {'container': 'PNG', 'width': width, 'height': height}
    return {'container': 'unknown'}


def text_format(raw):
    return {'utf8_bom': raw.startswith(b'\xef\xbb\xbf'), 'crlf': raw.count(b'\r\n'),
            'bare_lf': raw.replace(b'\r\n', b'').count(b'\n'), 'byte_length': len(raw)}


class GitReference:
    def __init__(self, root, reference):
        self.repo = root / safe_relative(reference['repository'])
        self.commit = reference['commit']
        if not re.fullmatch(r'[0-9a-f]{40}', self.commit):
            raise ValueError('Baseline commit must be an exact SHA-1')
        self.prefix = safe_relative(reference.get('tree_prefix', 'base/game'))
        self.cache = {}

    def read(self, rel):
        rel = safe_relative(rel)
        if rel not in self.cache:
            proc = subprocess.run(['git', '-c', 'core.hooksPath=NUL', '-c', 'core.autocrlf=false',
                                   '-C', str(self.repo), 'show', self.commit + ':' + self.prefix + '/' + rel],
                                  capture_output=True)
            if proc.returncode:
                raise ValueError('Baseline blob unavailable: ' + rel + ': ' + proc.stderr.decode('utf-8', errors='replace').strip())
            self.cache[rel] = proc.stdout
        return self.cache[rel]


class InstalledSources:
    def __init__(self, game):
        self.game = game
        self.cache = {}
        self.script_paths = None

    def read(self, rel):
        rel = safe_relative(rel)
        if rel not in self.cache:
            self.cache[rel] = (self.game / rel).read_bytes()
        return self.cache[rel]

    def scripts(self):
        if self.script_paths is None:
            self.script_paths = sorted(p for p in self.game.rglob('*.txt') if p.is_file())
        return self.script_paths

    def locate(self, symbol):
        pattern = re.compile(rb'(?m)^\s*(?:(?:scripted_effect|scripted_trigger)\s+)?' + re.escape(symbol.encode('utf-8')) + rb'\s*=')
        hits, errors = [], []
        for path in self.scripts():
            rel = path.relative_to(self.game).as_posix()
            raw = self.read(rel)
            if not pattern.search(raw):
                continue
            try:
                for row in assignments(raw):
                    if row['symbol'] == symbol:
                        hits.append((rel, row))
            except (ValueError, UnicodeError) as exc:
                errors.append(rel + ': ' + str(exc))
        return hits, errors


def callers(sources, events):
    """Inventory both scalar trigger_event and block-form id dispatches."""
    result = []
    for path in sources.scripts():
        rel = path.relative_to(sources.game).as_posix()
        raw = sources.read(rel)
        if not any(event.encode('utf-8') in raw for event in events):
            continue
        for owner in assignments(raw):
            tokens = owner['tokens']
            for pos, token in enumerate(tokens):
                if token != 'trigger_event' or tokens[pos + 1:pos + 2] != ['=']:
                    continue
                if pos + 2 >= len(tokens):
                    raise ValueError('Incomplete event dispatch in ' + rel)
                target = tokens[pos + 2]
                if target == '{':
                    depth = 0
                    for i in range(pos + 2, len(tokens)):
                        depth += (tokens[i] == '{') - (tokens[i] == '}')
                        if depth == 1 and tokens[i:i + 2] == ['id', '=']:
                            target = tokens[i + 2]
                        if depth == 0:
                            break
                if target in events:
                    result.append({'path': rel, 'owner': owner['symbol'], 'event': target,
                                   'owner_token_sha256': owner['token_sha256']})
    return sorted(result, key=lambda r: (r['path'], r['owner'], r['event'], r['owner_token_sha256']))


def compare_watch(watch, sources, reference):
    if watch['kind'] not in {'object', 'file', 'text', 'asset', 'callers'}:
        raise ValueError('Unknown watch kind: ' + watch['kind'])
    rel = safe_relative(watch['native_path'])
    result = {'id': watch['id'], 'feature': watch['feature'], 'surface': watch['surface'],
              'native_path': rel, 'symbol': watch.get('symbol'), 'local_definitions': watch['local_definitions'],
              'baseline_version': watch['baseline_version'], 'audit_scope': watch['audit_scope']}
    if watch['kind'] == 'callers':
        current = callers(sources, watch['events'])
        old = watch['baseline_callers']
        result.update(status='unchanged' if current == old else 'callers_changed',
                      current_callers=current, baseline_callers=old)
        if current != old:
            # Retain full owning-block diffs for changed/added/removed dispatches.
            result['diff'] = diff(json.dumps(old, indent=2) + '\n', json.dumps(current, indent=2) + '\n', 'baseline callers', 'installed callers')
            old_keys = {(r['path'], r['owner']) for r in old}
            new_keys = {(r['path'], r['owner']) for r in current}
            changes = []
            for path, owner in sorted(old_keys | new_keys):
                before = [r for r in old if r['path'] == path and r['owner'] == owner]
                after = [r for r in current if r['path'] == path and r['owner'] == owner]
                if before == after:
                    continue
                old_rows = assignments(reference.read(path)) if before else []
                new_rows = assignments(sources.read(path)) if after else []
                old_text = '\n'.join(r['text'] for r in old_rows if r['symbol'] == owner)
                new_text = '\n'.join(r['text'] for r in new_rows if r['symbol'] == owner)
                changes.append(diff(old_text + '\n', new_text + '\n', 'baseline ' + path + ':' + owner, 'installed ' + path + ':' + owner))
            result['owner_diffs'] = changes
        return result
    if watch['kind'] == 'asset':
        current = sources.read(rel)
        header = asset_header(current)
        result.update(status='unchanged' if sha(current) == watch['source_sha256'] else 'asset_changed',
                      current_sha256=sha(current), baseline_sha256=watch['source_sha256'], current_header=header,
                      baseline_header=watch['baseline_header'], comparison_reference='recorded byte hash and header; no archived binary')
        if result['status'] != 'unchanged':
            result['diff'] = diff(json.dumps({'sha256': watch['source_sha256'], 'header': watch['baseline_header']}, indent=2) + '\n',
                                  json.dumps({'sha256': sha(current), 'header': header}, indent=2) + '\n', 'baseline asset', 'installed asset')
        return result
    old = reference.read(rel)
    if sha(old) != watch['source_sha256']:
        raise ValueError('Baseline source checksum mismatch: ' + rel)
    current_path = rel
    if watch['kind'] == 'object':
        old_hits = [row for row in assignments(old) if row['symbol'] == watch['symbol']]
        if len(old_hits) != 1:
            raise ValueError('Missing/ambiguous baseline object: ' + watch['symbol'])
        old_row = old_hits[0]
        if old_row['token_sha256'] != watch['object_token_sha256']:
            raise ValueError('Baseline object token checksum mismatch')
        hits, errors = sources.locate(watch['symbol'])
        if errors:
            raise ValueError('Unreadable candidate definitions: ' + '; '.join(errors))
        if len(hits) != 1:
            result.update(status='missing_definition' if not hits else 'ambiguous_definition',
                          locations=[{'path': p, 'line': r['line']} for p, r in hits])
            if not hits:
                result['diff'] = diff(old_row['text'] + '\n', '', 'baseline ' + rel, 'installed missing')
            return result
        current_path, new_row = hits[0]
        result['current_path'] = current_path
        result['current_line'] = new_row['line']
        current = sources.read(current_path)
        if current_path != rel:
            result['status'] = 'moved_definition'
        elif old_row['tokens'] != new_row['tokens']:
            result['status'] = 'object_changed'
        elif old_row['text'] != new_row['text']:
            result['status'] = 'format_only'
        elif old != current:
            result['status'] = 'format_only' if decode(old) == decode(current) else 'file_changed_object_unchanged'
        else:
            result['status'] = 'unchanged'
        if old_row['tokens'] != new_row['tokens'] or old_row['text'] != new_row['text'] or current_path != rel:
            result['diff'] = diff(old_row['text'] + '\n', new_row['text'] + '\n', 'baseline ' + rel + ':' + watch['symbol'], 'installed ' + current_path + ':' + watch['symbol'])
        result['baseline_object_token_sha256'] = old_row['token_sha256']
        result['current_object_token_sha256'] = new_row['token_sha256']
    else:
        current = sources.read(rel)
        if old == current:
            result['status'] = 'unchanged'
        else:
            before, after = decode(old), decode(current)
            if before == after:
                result['status'] = 'format_only'
            elif watch['kind'] == 'text':
                result['status'] = 'reference_changed'
            elif [t[0] for t in lex(before)] == [t[0] for t in lex(after)]:
                result['status'] = 'format_only'
            else:
                result['status'] = 'file_changed'
            result['diff'] = diff(before, after, 'baseline ' + rel, 'installed ' + rel)
    result.update(baseline_sha256=sha(old), current_sha256=sha(current))
    if old != current:
        result['baseline_format'] = text_format(old)
        result['current_format'] = text_format(current)
        if result['baseline_format'] != result['current_format']:
            result['format_diff'] = diff(json.dumps(result['baseline_format'], indent=2) + '\n', json.dumps(result['current_format'], indent=2) + '\n', 'baseline byte format', 'installed byte format')
        if watch['kind'] == 'object' and 'diff' not in result:
            result['file_diff'] = diff(decode(old), decode(current), 'baseline file ' + rel, 'installed file ' + current_path)
    return result


def check(manifest, names, game, root=ROOT):
    if manifest['schema_version'] != 1:
        raise ValueError('Unsupported watch schema')
    unknown = set(names) - set(manifest['mods'])
    if unknown:
        raise ValueError('Unknown or excluded mod(s): ' + ', '.join(sorted(unknown)))
    version_file = game.parent / 'launcher/launcher-settings.json'
    version = json.loads(decode(version_file.read_bytes()))['rawVersion']
    references = {}
    sources = InstalledSources(game)
    output = {'installed_version': version, 'baseline_version': manifest['baseline_version'],
              'baseline_date': manifest['date'], 'version_changed': version != manifest['baseline_version'],
              'scope': 'Registered source watches only; not compatibility certification or a complete feature audit.', 'mods': {}}
    exports = manifest['engine_reference']
    export_drift = [rel for rel, expected in exports['files'].items() if not (root / safe_relative(rel)).is_file() or sha((root / rel).read_bytes()) != expected]
    output['engine_reference'] = {'version': exports['version'], 'status': 'stale_for_installed_version' if version != exports['version'] else 'recorded_exports_unchanged', 'changed_or_missing_exports': export_drift}
    if export_drift:
        output['engine_reference']['status'] = 'exports_changed_or_missing'
    for name in names:
        config = manifest['mods'][name]
        ids = [watch['id'] for watch in config['watches']]
        if not ids or len(ids) != len(set(ids)):
            raise ValueError('Empty/duplicate watch registration for ' + name)
        rows = []
        for watch in config['watches']:
            try:
                provenance = watch.get('comparison_reference', manifest['comparison_reference'])
                reference_key = json.dumps(provenance, sort_keys=True)
                if reference_key not in references:
                    references[reference_key] = GitReference(root, provenance)
                reference = references[reference_key]
                rows.append(compare_watch(watch, sources, reference))
            except (OSError, ValueError, UnicodeError, KeyError, IndexError) as exc:
                rows.append({'id': watch['id'], 'feature': watch['feature'], 'native_path': watch['native_path'],
                             'symbol': watch.get('symbol'), 'status': 'comparison_incomplete', 'reason': str(exc)})
        local_changes = []
        for rel, expected in config['local_sources'].items():
            path = root / safe_relative(rel)
            if not path.is_file() or sha(path.read_bytes()) != expected:
                local_changes.append(rel)
        counts = dict(Counter(row['status'] for row in rows))
        review = any(row['status'] not in {'unchanged', 'format_only', 'file_changed_object_unchanged'} for row in rows)
        context_review = any(row['status'] == 'file_changed_object_unchanged' for row in rows)
        output['mods'][name] = {'sheet': config['sheet'], 'coverage': config['coverage'], 'open_gates': config['open_gates'],
                                'counts': counts, 'source_review_required': review, 'file_context_review_required': context_review, 'local_sources_changed': local_changes,
                                'watches': rows, 'gameplay': 'not evaluated'}
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mod', action='append', help='Exact registered mod name; repeat for several mods')
    parser.add_argument('--all', action='store_true', help='Check all retained distributions, not excluded Knight/test packages')
    parser.add_argument('--manifest', type=Path, help='Explicit dated baseline; otherwise use the reviewed baseline index')
    parser.add_argument('--game', type=Path, default=DEFAULT_GAME)
    parser.add_argument('--json', action='store_true', help='Emit machine-readable report to stdout only')
    args = parser.parse_args(argv)
    if bool(args.mod) == args.all:
        parser.error('Choose --mod NAME (repeatable) or --all')
    try:
        manifest_path = args.manifest
        if manifest_path is None:
            index = json.loads(BASELINE_INDEX.read_text(encoding='utf-8-sig'))
            manifest_path = BASELINE_INDEX.parent / safe_relative(index['current_baseline'])
        manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
        names = list(manifest['mods']) if args.all else list(dict.fromkeys(args.mod))
        result = check(manifest, names, args.game)
    except (OSError, ValueError, KeyError, UnicodeError) as exc:
        print('Comparison unavailable: ' + str(exc), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print('Installed: ' + result['installed_version'] + '; baseline: ' + result['baseline_version'])
        print('Engine reference: ' + result['engine_reference']['status'])
        for name, mod in result['mods'].items():
            print('\n' + name + ': ' + json.dumps(mod['counts'], sort_keys=True))
            print('Coverage: ' + mod['coverage'])
            if mod['local_sources_changed']:
                print('Local changes requiring review: ' + ', '.join(mod['local_sources_changed']))
            for row in mod['watches']:
                if row['status'] == 'unchanged':
                    continue
                print(row['id'] + ': ' + row['status'] + ' (' + row['native_path'] + ')')
                if row.get('reason'):
                    print(row['reason'])
                if row.get('diff'):
                    print(row['diff'])
                if row.get('file_diff'):
                    print('File context changed; the registered object is unchanged:\n' + row['file_diff'])
                if row.get('format_diff'):
                    print(row['format_diff'])
                for change in row.get('owner_diffs', []):
                    print(change)
        print('\nSource findings require the update workflow. No mod update or runtime claim is made by this tool.')
    incomplete = any(row['status'] in {'comparison_incomplete', 'missing_definition', 'ambiguous_definition'} for mod in result['mods'].values() for row in mod['watches'])
    needs_review = result['version_changed'] or any(mod['source_review_required'] or mod['file_context_review_required'] or mod['local_sources_changed'] for mod in result['mods'].values()) or result['engine_reference']['status'] != 'recorded_exports_unchanged'
    return 2 if incomplete else 1 if needs_review else 0


if __name__ == '__main__':
    # JSON/text stdout must preserve non-ASCII paths and script text on Windows pipes.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
