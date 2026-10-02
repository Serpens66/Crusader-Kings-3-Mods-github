"""Verify this collection without launching CK3 or installing a validator.

Checks files/links, UTF-8+BOM policy, CRLF, fixture structure/references and
unchanged indexed workspace sources. It is not a complete Jomini validator.
"""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from build_local_reference import OUT, definitions, write

def check_braces(text):
    depth, quoted, comment, escaped = 0, False, False, False
    for char in text:
        if comment:
            if char == '\n': comment = False
            continue
        if quoted:
            if escaped: escaped = False
            elif char == '\\': escaped = True
            elif char == '"': quoted = False
            continue
        if char == '#': comment = True
        elif char == '"': quoted = True
        elif char == '{': depth += 1
        elif char == '}':
            depth -= 1
            if depth < 0: return False
    return depth == 0 and not quoted

def main():
    issues, checks = [], {'internal_links':0, 'text_files':0, 'fixture_structures':0,
                          'workspace_hashes':0, 'audit_source_hashes':0, 'fixture_identifiers':0}
    index = json.loads((OUT/'reference/local-index.json').read_text(encoding='utf-8'))
    for path in sorted(OUT.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        raw = path.read_bytes()
        try: text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            issues.append(f'{path.relative_to(OUT)}: not UTF-8')
            continue
        checks['text_files'] += 1
        if path.suffix in {'.txt','.yml'} and not raw.startswith(b'\xef\xbb\xbf'):
            issues.append(f'{path.relative_to(OUT)}: missing required BOM')
        if b'\n' in raw.replace(b'\r\n',b'') or b'\r' in raw.replace(b'\r\n',b''):
            issues.append(f'{path.relative_to(OUT)}: non-CRLF line ending')
        if path.suffix == '.md':
            # Do not interpret bracketed expressions inside fenced code as links.
            prose = re.sub(r'```.*?```','',text,flags=re.S)
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)',prose):
                target = target.strip().strip('<>')
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith('#'):
                    continue
                relative = unquote(target.split('#',1)[0])
                resolved = (path.parent/relative).resolve()
                checks['internal_links'] += 1
                if not resolved.exists():
                    issues.append(f'{path.relative_to(OUT)}: broken link {target}')
        if OUT/'examples' in path.parents and path.suffix in {'.txt','.gui','.mod'}:
            checks['fixture_structures'] += 1
            if not check_braces(text):
                issues.append(f'{path.relative_to(OUT)}: unbalanced braces or quote')
    # Verify user files have their initially recorded contents; never fix them.
    for row in index['mods']:
        path = Path(index['workspace_root'])/row['path']
        checks['workspace_hashes'] += 1
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            issues.append('Workspace source changed since indexed: '+row['path'])
    audit = json.loads((OUT/'reference/audit-evidence.json').read_text(encoding='utf-8'))
    for rel, row in audit['files'].items():
        path = Path(index['game_root'])/rel
        checks['audit_source_hashes'] += 1
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            issues.append('Audited installation source changed: '+rel)
    fixture = OUT/'examples/mini-mod'
    defs, texts = {}, {}
    for path in fixture.rglob('*'):
        if path.is_file():
            text = path.read_text(encoding='utf-8-sig')
            texts[path.relative_to(fixture).as_posix()] = text
            if path.suffix == '.txt':
                for entry in definitions(text):
                    if entry['key'].startswith('doc_demo'):
                        if entry['key'] in defs:
                            issues.append('Duplicate example definition: '+entry['key'])
                        defs[entry['key']] = path
    required = {'doc_demo_can_request_trigger','doc_demo_has_gold_trigger','doc_demo_request_effect',
                'doc_demo_grant_gold_effect','doc_demo_reward_value','doc_demo_payment_value',
                'doc_demo_arithmetic_value','doc_demo_decision','doc_demo.0001','doc_demo.0002',
                'doc_demo_transfer_interaction','doc_demo_birthday','doc_demo_request_gui'}
    for key in required:
        checks['fixture_identifiers'] += 1
        if key not in defs: issues.append('Missing example definition: '+key)
    localizations = texts.get('localization/english/doc_demo_l_english.yml','')
    expected_loc = {'doc_demo_decision','doc_demo_decision_desc','doc_demo_decision_tooltip',
                    'doc_demo_decision_confirm','doc_demo_transfer_interaction',
                    'doc_demo_transfer_interaction_desc','doc_demo_gui_button'}
    for key in expected_loc:
        if not re.search(r'(?m)^\s+'+re.escape(key)+r':\d*\s+"',localizations):
            issues.append('Missing example localization: '+key)
    if not localizations.startswith('l_english:'):
        issues.append('Example localization header is incorrect')
    native = Path(index['game_root'])
    for rel in ['gfx/interface/illustrations/decisions/decision_personal_religious.dds']:
        if not (native/rel).is_file(): issues.append('Example references absent native asset: '+rel)
    combined = '\n'.join(texts.values())
    for match in re.finditer(r'\bid\s*=\s*(doc_demo\.\d+)',combined):
        if match.group(1) not in defs: issues.append('Unresolved example event: '+match.group(1))
    for path,text in texts.items():
        if '$AMOUNT$' in text and '/scripted_' not in '/'+path:
            issues.append('Unexpanded helper parameter outside helper definitions: '+path)
    result = {'date':'2026-10-03','status':'passed' if not issues else 'failed','checks':checks,'issues':issues,
              'limits':['No CK3 execution','No external Tiger run','No GUI rendering','No full grammar/type validation',
                        'Workspace preservation check covers initially indexed text/reference files; no writes were made outside Documentation.']}
    write('research/verification.json',json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    lines = ['# Verification results','',f"Date: 2026-10-03. Status: **{result['status']}**.",'',
             '| Check | Count |','|---|---:|']
    lines += [f'| {k.replace("_"," ")} | {v} |' for k,v in checks.items()]
    lines += ['','## Issues',''] + (['- '+x for x in issues] if issues else ['No issues found by the checks above.'])
    lines += ['','## Limits',''] + ['- '+x for x in result['limits']]
    lines += ['','This result is structural/source verification only. It does not certify gameplay compatibility or completeness of the engine API. The original untracked workspace `.gitignore` was not modified.','']
    write('research/verification.md','\n'.join(lines))
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if not issues else 1)

if __name__ == '__main__':
    main()
