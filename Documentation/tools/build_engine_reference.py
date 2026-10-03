"""Index verified local engine exports without altering the source bytes."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

DOC = Path(__file__).resolve().parents[1]
READY = DOC / 'update-readiness'
CATEGORIES = {'effects': 'effect', 'triggers': 'trigger', 'event_scopes': 'scope',
              'event_targets': 'target', 'modifiers': 'modifier', 'on_actions': 'on_action'}


def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=2) + '\n'
    path.write_bytes(text.replace('\n', '\r\n').encode('utf-8'))


def decode(raw):
    if raw.startswith(b'\xef\xbb\xbf'):
        return raw.decode('utf-8-sig'), 'utf-8-sig', 'BOM'
    try:
        return raw.decode('utf-8'), 'utf-8', 'UTF-8 compatible; no BOM'
    except UnicodeDecodeError:
        # Lossless candidate, not a claim about the engine's configured code page.
        text = raw.decode('cp1252')
        if text.encode('cp1252') != raw:
            raise ValueError('Source cannot be decoded reversibly')
        return text, 'cp1252', 'Reversible Windows-1252 candidate; original bytes retained'


def spans(lines, category):
    boundaries = {0, len(lines)}
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.fullmatch('-{10,}', stripped):
            boundaries.update([i, i + 1])
        if category == 'scope' and re.fullmatch(r'[A-Za-z_][\w]*:', stripped):
            boundaries.add(i)
        if category == 'modifier' and stripped.startswith('Tag:'):
            boundaries.add(i)
        if category == 'target' and stripped == 'Event Targets Saved from Code:':
            boundaries.update([i, i + 1])
            boundaries.update(range(i + 1, len(lines) + 1))
    boundaries = sorted(boundaries)
    return list(zip(boundaries, boundaries[1:]))


def parse(text, category, source):
    lines = text.splitlines(keepends=True)
    entries, segments = [], []
    saved = False
    for start, end in spans(lines, category):
        body = ''.join(lines[start:end])
        nonempty = [(start + j + 1, line.strip()) for j, line in enumerate(lines[start:end]) if line.strip()]
        head = nonempty[0][1] if nonempty else ''
        kind = 'unparsed'
        name, description, effective = None, None, category
        if not head:
            kind = 'empty'
        elif re.fullmatch('-{10,}', head):
            kind = 'separator'
        elif head == 'Event Targets Saved from Code:':
            kind, saved = 'header', True
        elif category == 'target' and saved and re.fullmatch(r'[\w.]+', head):
            name, effective = head, 'saved_target'
        elif category in {'effect', 'trigger', 'target'}:
            match = re.match(r'^([^\s]+)\s+-\s*(.*)', head)
            if match:
                name, description = match.groups()
        elif category in {'scope', 'on_action'} and re.fullmatch(r'[\w.]+:', head):
            name = head[:-1]
        elif category == 'modifier' and head.startswith('Tag:'):
            name = head[4:].strip()
        elif category == 'datatype' and any(line.startswith('Definition type:') for _, line in nonempty):
            name = head.split('(', 1)[0].strip()
        if name is not None:
            kind = 'entry'
            fields = []
            for _, line in nonempty[1:]:
                match = re.match(r'^([A-Za-z][A-Za-z ]+):\s*(.*)', line)
                if match:
                    fields.append({'key': match[1], 'value': match[2]})
            def field(key):
                return [x['value'] for x in fields if x['key'] == key]
            entry = {'category': effective, 'name': name,
                     'signature': head if effective == 'datatype' else None,
                     'description': description or (field('Description') or [None])[0],
                     'documented_fields': fields,
                     'supported_scopes': field('Supported Scopes'),
                     'supported_targets': field('Supported Targets'),
                     'return_type': (field('Return type') or [None])[0],
                     'definition_type': (field('Definition type') or [None])[0],
                     'parameter_documentation': [line for _, line in nonempty if re.match(r'^\w+\s*=|^\w+\s+\([^)]*\)\s*=', line)],
                     'raw_text': body, 'source': source,
                     'line': nonempty[0][0], 'span_start': start + 1, 'span_end': end,
                     'limits': 'Fields are exported declarations; missing parameter types/optionality and runtime permissions are not inferred.'}
            entries.append(entry)
        elif kind == 'unparsed' and (head.endswith('Documentation:') or head in {'Scope Types:', 'Printing Modifier Definitions:'}):
            kind = 'header'
        segments.append({'kind': kind, 'start': start + 1, 'end': end, 'text': body})
    return entries, segments


def build():
    intake = json.loads((READY / 'evidence/runtime-intake.json').read_text(encoding='utf-8'))
    records = intake['retained_script_export_files'] + intake['datatype_files']
    result = {'schema_version': 1, 'game_version': intake['executed_version'].split()[0],
              'game_commit': intake['game_commit'], 'date': '2026-10-03',
              'sources': [], 'entries': [], 'coverage': [],
              'limits': ['No gameplay compatibility claim', 'none scope token is preserved literally',
                         'Saved-from-code names have no invented scope/lifetime',
                         'Exported parameter examples are not a complete formal parameter schema']}
    for record in records:
        path = READY / record['copy']
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != record['sha256']:
            raise ValueError('Export hash mismatch: ' + str(path))
        text, encoding, note = decode(raw)
        source = {'path': path.relative_to(DOC).as_posix(), 'sha256': record['sha256'],
                  'original_path': record['source'], 'mtime_ns': record['mtime_ns'],
                  'decode_encoding': encoding, 'decode_note': note}
        name = path.name.split('.')[0]
        category = CATEGORIES.get(name, 'datatype')
        entries, segments = parse(text, category, source)
        # Every source line, including headers and unexplained tails, has one owner.
        if ''.join(s['text'] for s in segments) != text:
            raise ValueError('Incomplete export conservation: ' + str(path))
        result['sources'].append(source)
        result['entries'].extend(entries)
        result['coverage'].append({'source': source['path'], 'lines': len(text.splitlines()),
                                   'entry_count': len(entries), 'segments': segments})
    result['counts'] = dict(Counter(e['category'] for e in result['entries']))
    result['unparsed_segments'] = sum(s['kind'] == 'unparsed' for f in result['coverage'] for s in f['segments'])
    write(DOC / 'reference/engine-1.20.0.3.json', result)
    print(json.dumps({'sources': len(records), 'counts': result['counts'],
                      'unparsed_segments': result['unparsed_segments']}, indent=2))
    return result


if __name__ == '__main__':
    build()
