"""Search indexed CK3 definitions and observed uses without scanning the game again.

Usage: python Documentation/tools/lookup.py add_gold [--context 4]
Results are discoveries, not verified engine contracts.
"""
import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('symbol')
    parser.add_argument('--context', type=int, default=0)
    args = parser.parse_args()
    base = Path(__file__).resolve().parents[1] / 'reference'
    index = json.loads((base / 'local-index.json').read_text(encoding='utf-8'))
    observed = json.loads((base / 'observed-symbols.json').read_text(encoding='utf-8'))
    matches = [('use', x) for x in observed.get(args.symbol, [])]
    for group in ['native', 'mods']:
        for file in index[group]:
            for item in file['definitions']:
                if item['key'] == args.symbol:
                    matches.append((group, {'path': file['path'], 'line': item['line']}))
    for kind, row in matches:
        root = Path(index['workspace_root'] if kind == 'mods' else index['game_root'])
        path = root / row['path']
        print(f"{kind}: {path}:{row['line']}")
        if args.context and path.exists():
            lines = path.read_text(encoding='utf-8-sig', errors='replace').splitlines()
            for n in range(max(0,row['line']-1-args.context), min(len(lines),row['line']+args.context)):
                print(f'{n+1}: {lines[n]}')
    if not matches:
        print('No indexed match. This does not prove the symbol is unsupported.')

if __name__ == '__main__':
    main()
