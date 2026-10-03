"""Read Knight variants and current native contracts; author learning-only evidence."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote
from build_local_reference import definitions
from complete_contract_handbook import D, W, G, write, append

def main():
    records=[]; sections=[]
    for folder in ['Knight Manager (MP)','Knight Manager Continued (MP)','test']:
        files=[]; state={}; helpers=[]
        for p in sorted((W/folder).rglob('*')):
            if not p.is_file() or p.suffix not in {'.txt','.yml','.gui','.mod','.lnk'}:continue
            raw=p.read_bytes()
            row={'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'full_file_read':True}
            if p.suffix!='.lnk':
                text=raw.decode('utf-8-sig',errors='replace'); row['decode_warning']='\ufffd' in text
                row['definitions']=definitions(text)
                for n,line in enumerate(text.splitlines(),1):
                    for name in re.findall(r'\b(?:kmc_|knight_manager_|KnightManager_)[A-Za-z0-9_]+',line.split('#')[0]):
                        state.setdefault(name,[]).append({'path':row['path'],'line':n})
                if '/scripted_triggers/' in '/'+row['path']:helpers.append(row['path'])
            else:row['interpretation']='Windows shortcut, not a loadable GUI/script definition'
            files.append(row)
        records.append({'variant':folder,'files':files,'state_tokens':state,'status':'learning-only; excluded from updates'})
        sections += ['## '+folder,'','| State/helper token | Exact first occurrence |','|---|---|']
        for token,refs in sorted(state.items()):
            ref=refs[0]; url='../../'+quote(ref['path'],safe='/')
            sections.append(f"| `{token}` | [{ref['path']}:{ref['line']}]({url}) |")
        sections += ['','All occurrences and source hashes are retained in [evidence](knight-manager-evidence.json). Token presence does not establish an active caller or correct native contract.','']
    # Read actual native definition/caller files in their entirety; summarize, do not copy.
    callers=[]
    for p in sorted(G.rglob('*.txt')):
        raw=p.read_bytes();text=raw.decode('utf-8-sig',errors='replace')
        hits=[n for n,line in enumerate(text.splitlines(),1) if re.search(r'\bcan_be_(?:knight|warrior)_trigger\b',line.split('#')[0])]
        if hits:callers.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'full_file_read':True,'lines':hits})
    native=G/'common/scripted_triggers/00_war_and_peace_triggers.txt'
    text=native.read_text(encoding='utf-8-sig');ds=definitions(text);lines=text.splitlines()
    surfaces=[]
    for i,d in enumerate(ds):
        if d['key'] not in {'can_be_knight_trigger','can_be_warrior_trigger'}:continue
        end=ds[i+1]['line']-1 if i+1<len(ds) else len(lines)
        body='\n'.join(lines[d['line']-1:end])
        surfaces.append({'name':d['key'],'line':d['line'],'end':end,
            'parameters':sorted(set(re.findall(r'\$([A-Z_]+)\$',body))),
            'lexical_keys':sorted(set(re.findall(r'([\w.]+)\s*(?:\?=|>=|<=|=|>|<)',re.sub(r'#[^\n]*','',body))))})
    write('workspace/knight-manager-evidence.json',json.dumps({'date':'2026-10-03','version':'1.20.0.3','variants':records,'native_full_read_callers':callers,'native_contract_surfaces':surfaces,'limits':['No updates','No game tests','Caller discovery is lexical; no complete engine permission/semantic inference']},indent=2))
    write('workspace/knight-manager-contracts.md', '''
# Knight Manager variants: learning-only contracts

All three packages and their text/GUI/descriptors/shortcut bytes were reread and hashed. Current `can_be_knight_trigger`, `can_be_warrior_trigger` and their discovered native `.txt` callers were read in full. [Evidence](knight-manager-evidence.json) preserves exact paths, current parameters, definition ranges, caller lines and state uses. This audit explains local preference wiring; it does not certify complete modern knight eligibility or authorize updating any variant.

## Ownership and execution

The custom `KM_can_be_knight_trigger` evaluates a **candidate character**. `$ARMY_OWNER$` is a required caller substitution pointing to the army owner's character. Relationship predicates compare candidate to owner, but preference flags are read on `$ARMY_OWNER$`. Calling the toggle GUI with a selected knight instead of the player/army owner changes the wrong preference owner. The older actual window constructs `GetPlayer.MakeScope` for group preferences and `Character.MakeScope` for the candidate's manual allowance. These are distinct roots; never copy one for both.

Both variants' custom predicate allows an AI army owner, an acclaimed candidate, or a manually allowed candidate before testing its exclusion set. That bypass applies to the **custom filter only**; it does not prove that all native warrior eligibility can be bypassed. The enclosing copied `can_be_knight_trigger` applies its other conditions as well. Both copies include candidate `is_ai = yes`; this is different from the custom owner's AI check.

Older/manual allowances use candidate character flag `knight_manager_manually_allowed`; Continued uses candidate variable `kmc_manually_allowed`. Group preferences are character flags on owner, not global player settings. Code toggle presence/removal establishes local storage choice; reset on player succession, persistence, invalidation and MP safety require explicit tests and are not guaranteed by a comment saying “MP”. The older startup child sets `KnightManager_is_loaded` globally as an integration marker, not per-player preferences. Its hidden orphan event only references that marker to suppress a validator warning.

## Older filter policy

Older/test preferences cover dynasty kin, vassals, children/grandchildren, spouse plus spouses of descendants, public/secret lover or soulmate, player heir, prowess <6 and 6–12, councillors/court-position holders. Bodyguard/garuda positions are excluded from the latter combined exclusion. The source includes optional dynasty matching and special existence guards in spouse iteration; comments describing null workarounds are historical observations, not engine-contract proof. Group flags toggle in shared ScriptedGui definitions; the real window is a complete native-path replacement.

## Continued filter policy

Continued separates dynasty, house, spouse, descendant, descendant's spouse, heir, lovers/soulmates, councillors, court-position holders, unlanded, highborn/lowborn, above-baron landed and baron-or-lower filters. Its prowess bands are <5, 5–8, 9–12, 13–16 and >16, plus `wounded`. Court-position filter excludes bodyguard/garuda. Manual allowance uses a candidate variable. Exact state names and all occurrences are below.

There is **no actual `.gui` window in the Continued workspace package**. Its `.info.lnk` shortcut is not engine-loaded content. ScriptedGui definitions therefore do not prove that toggles are exposed here. Localization is also absent in this package. Treat incomplete packaging as a concrete learning/consumer gap, rather than claiming a full functional standalone mod. Both variants define native `can_be_knight_trigger` and shared `KM_*` IDs, so they are alternatives and must not be co-enabled.

## Current Vanilla boundaries

Current native definitions have parameterized warrior/knight contracts and are not interchangeable with old full copied predicates. The evidence records exact current keys and callers; [lookup](../tools/lookup.py) retrieves their definitions. The old copies differ in hostage/clergy/cultural/court-position coverage. A modern update would require a complete helper-parameter and eligibility branch comparison plus GUI rebase; it is explicitly out of scope. The current docs retain this blocker rather than manufacturing a “best practice” native replacement from historical code.

For CustomDefines, embedded knight toggles/state/helper dependencies remain a removal-only preparation task. Use the [removal candidate list](../update-readiness/evidence/knight-removal-candidates.json) and CD-KNIGHTS card to preserve unrelated GUI changes; removing an entire shared GUI file would discard other behavior. Existing standalone/test packages stay untouched.

## Learning acceptance cases

Inspect candidate versus owner, acclaimed/manual override versus base eligibility, no-dynasty/spouse contexts, bodyguard/garuda exceptions, exact prowess boundaries, UI checkbox state versus predicate, player succession/save-load and two owners with opposite flags. These are proposed learning tests, **not required updates or completed tests**. The Continue package's absent widget/translation is a prerequisite blocker for its UI cases.

'''+ '\n'.join(sections))
    append('workspace/case-studies.md','## State and contract supplement\n\nSee [function-level owner/lifetime guide](function-contracts.md), [43 engine-reconciled cards](../update-readiness/contracts/README.md) and [Knight variants learning audit](knight-manager-contracts.md). These retain alternatives and unresolved context/lifecycle questions rather than treating old workspace code as a current best-practice reference.')

if __name__=='__main__':main()
