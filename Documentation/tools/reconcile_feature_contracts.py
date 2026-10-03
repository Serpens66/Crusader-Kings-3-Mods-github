"""Reconcile declarations, preserve sources, and expose remaining semantic gates."""
import hashlib
import json
import re
from pathlib import Path
from build_local_reference import definitions

DOC = Path(__file__).resolve().parents[1]
WORK = DOC.parent
READY = DOC / 'update-readiness'
GAME = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
PREFIX = {'CD': 'CustomDefines', 'GC': 'Gender Colour', 'GX': 'GFX-Mod',
          'GS': 'GFX-Mod Serp', 'LW': 'Leave Wars', 'MC': 'Mass Demand Conversion',
          'SA': 'SerpAlerts', 'SI': 'SerpInteractionsDecisions'}
SYMBOLS = {
 'CD-COMBAT': [], 'CD-DYNASTY': [], 'CD-MAP': [],
 'CD-RULES': ['ExecuteConsoleCommand'], 'CD-LOBBY': ['TryStartRulerDesigning','LobbyView.CanTryStartRulerDesigning'],
 'CD-TOOLTIPS': ['Character.GetHealth','Character.GetFertility','Character.GetStress'],
 'CD-KNIGHTS': ['has_character_flag','add_character_flag'],
 'LW-SELECT': ['is_participant','is_primary_war_attacker','is_primary_war_defender','save_scope_as','trigger_event'],
 'LW-EXIT': ['remove_participant','clear_saved_scope','pay_short_term_gold','add_prestige','add_prestige_experience'],
 'LW-RULES': ['highest_held_title_tier','remove_short_term_gold'],
 'MC-CANDIDATES': ['is_character_interaction_potentially_accepted','is_character_interaction_valid','every_courtier','every_tributary'],
 'MC-DISPATCH': ['run_interaction','is_character_interaction_potentially_accepted'],
 'MC-VARIANTS': ['run_interaction'],
 'SA-JOIN': ['is_character_interaction_valid','open_interaction_window'],
 'SA-STOP': ['is_character_interaction_valid','open_interaction_window'],
 'SA-EDUCATION': ['open_view_data'], 'SA-CONVERSION': ['is_character_interaction_potentially_accepted','open_interaction_window'],
 'SA-WAR-START': ['on_war_started','add_to_temporary_list','send_interface_message'],
 'SA-WAR-JOIN': ['on_join_war_as_secondary','send_interface_message'],
 'SA-DEATH': ['on_death','send_interface_message'], 'SA-COURT': ['on_leave_court','send_interface_message'],
 'SI-ABDICATE': ['depose','highest_held_title_tier'],
 'SI-RESOURCES': ['add_prestige','add_piety','remove_short_term_gold','add_character_modifier'],
 'SI-EDUCATION': ['trigger_event','save_scope_as','set_variable','remove_variable','add_character_modifier'],
 'SI-PARDON': ['use_hook','remove_hook'], 'SI-MONEY': ['pay_short_term_gold'],
 'SI-EXCOMM': ['use_hook','piety_level'], 'SI-CONVERSION': ['run_interaction'], 'SI-WARS': ['remove_participant']}
PROFILES = {
 'CD': ('GUI-selected character/player or namespace/key loader; no universal character root for defines.',
        'Retain original numeric settings; distinguish nested GUI overrides from whole-path files and embedded knight state.',
        'Native loader precedence, designer permissions, rendered values and combat/renown numerical outcomes remain test/audit gates.'),
 'GC': ('Texture consumer supplies UI state/frame; this is not an effect chain.',
        'Source atlas and path define presentation; alternate names have no proven live consumer.',
        'Render exact sexuality/status frames at two scales; do not infer consumption from basename matches.'),
 'GX': ('Portrait/artifact widget supplies selected object and frame.',
        'Public package identity and smaller footprint differ from the local Serp package.',
        'Current title-tier/frame mapping, alternate consumers and old atlas acceptance need rendered observations.'),
 'GS': ('UI/texture or map post-effect consumer, depending on the component.',
        'Keep local-only assets separate; file header does not prove engine acceptance of a container.',
        'Unmatched assets, container acceptance and post-effect transitions remain concrete render gates.'),
 'LW': ('Interaction actor is withdrawing secondary participant; recipient is leader; selected war is saved for event selection.',
        'Ten slots and original costs are the policy. Event branches touch actor, war, leader and receiver contexts separately.',
        'Recheck ended/changed wars, same-side membership, player leadership, accounting, alliance effects and saved-scope cleanup.'),
 'MC': ('Decision root is requester; iterator this is candidate; entering root makes candidate available through prev at that caller.',
        'Preview/count and dispatch must use the same category policy. Native query and dispatch initialization need separate tracing.',
        'Actor/puppet/redirect setup, duplicate memberships, protection/authority/rite rules, consent and native consequences require full branch audit and tests.'),
 'SA': ('Important-action creation starts in player context; on-action callbacks supply their own guaranteed and optional targets.',
        'UI-only discovery/click must be distinguished from synchronized state mutation. Recipient lists are built per callback and side.',
        'Selected-war context, optional killer/employer, relationship overlap, message duplication and per-player delivery remain behavioral gates.'),
 'SI': ('Decision root or interaction actor/recipient; queued student events and payer report are separate operations.',
        'Preserve original fees, self-study split, 250-gold AI exception, menu cancel cooldown and temporal excommunication purpose.',
        'Exactly-once rewards, expired/dead references, hook policy, authority/rite mapping, player succession and budget deltas remain component-specific gates.')}


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))


def dump(path, data):
    write(path, json.dumps(data, ensure_ascii=False, indent=2)+'\n')


def main():
    engine = json.loads((DOC/'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'))
    matrix = json.loads((READY/'feature-matrix.json').read_text(encoding='utf-8'))
    closure = json.loads((READY/'evidence/feature-source-closure.json').read_text(encoding='utf-8'))
    index = json.loads((DOC/'reference/local-index.json').read_text(encoding='utf-8'))
    native = {}
    for group in closure['groups'].values(): native.update(group['native_files'])
    for extra in ['common/character_interactions/00_gift.txt','common/on_action/birthday.txt',
                  'common/on_action/yearly_on_actions.txt','common/on_action/barter_on_actions.txt',
                  'common/scripted_guis/ce1_funeral_scripted_guis.txt',
                  'gui/activity_window_widgets/funeral_deceased_selection_button.gui',
                  'gui/scripted_widgets/_scripted_widgets.info','gui/hud.gui','gui/shared/portraits.gui']:
        path = GAME/extra
        native.setdefault(extra, {'sha256':hashlib.sha256(path.read_bytes()).hexdigest(), 'additional_recipe_source':True})
    source_reads = {}
    for rel, expected in native.items():
        raw=(GAME/rel).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=expected['sha256']: raise ValueError('Stale native source: '+rel)
        text=raw.decode('utf-8-sig', errors='replace')
        source_reads[rel]={'sha256':expected['sha256'],'full_file_read':True,
                          'decode_warning':'\ufffd' in text,'lines':len(text.splitlines())}
    # Read every existing mod text again; extract full definition boundaries, not arbitrary snippets.
    workspace = []; native_names={d['key'] for f in index['native'] for d in f['definitions']}
    by_root={}
    for folder in sorted(WORK.iterdir()):
        if not folder.is_dir() or folder==DOC or folder.name.startswith('.'):continue
        records=[]
        for path in sorted(folder.rglob('*')):
            if not path.is_file() or path.suffix not in {'.txt','.yml','.gui','.mod','.asset'}:continue
            raw=path.read_bytes();text=raw.decode('utf-8-sig', errors='replace');ds=definitions(text)
            lines=text.splitlines();objects=[]
            for i,d in enumerate(ds):
                end=ds[i+1]['line']-1 if i+1<len(ds) else len(lines)
                body='\n'.join(lines[d['line']-1:end]);active=re.sub(r'#[^\n]*','',body)
                keys=set(re.findall(r'([^\s{}=<>!]+)\s*(?:\?=|!=|>=|<=|=|>|<)',active))
                objects.append({'name':d['key'],'line':d['line'],'end':end,
                     'macro_parameters':sorted(set(re.findall(r'\$([A-Z_]+)\$',active))),
                     'engine_declarations':sorted(keys & {e['name'] for e in engine['entries']}),
                     'native_definition_candidates':sorted(keys & native_names),
                     'saved_scopes':re.findall(r'save_(?:temporary_)?scope_as\s*=\s*([^\s{}]+)',active),
                     'events':re.findall(r'\bid\s*=\s*([A-Za-z_][\w]*\.\d+)',active),
                     'state_tokens':sorted(set(re.findall(r'\b(?:kmc_|knight_manager_|doc_demo_|KnightManager_)[\w]+',active))),
                     'scope_references':sorted(set(re.findall(r'\b(?:scope|var|global_var|local_var):[\w]+',active))),
                     'interpretation':'Lexical contract surface; owner/context/parameter binding still requires the feature narrative and exact caller.'})
            record={'path':path.relative_to(WORK).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),
                    'definitions':objects,'full_file_read':True}
            workspace.append(record);records.append(record)
        by_root[folder.name]=records
    result={'date':'2026-10-03','version':engine['game_version'],'native_reads':source_reads,
            'workspace':workspace,'features':[],
            'semantic_boundary':'Complete-file reads and lexical helper candidates are not a completed semantic audit. Each behavioral gate below remains explicit. No unknown engine contract is replaced by assumptions.'}
    lines=['# Reconciled feature contracts','',
           'Current engine declarations are now indexed. These cards complement, rather than replace, the authored per-mod policy sheets. A signature confirmation is separate from initializer, side effects, lifetime, permissions and runtime validation.','',
           '[Engine reference](../../reference/engine-reference.md) · [Behavior guide](../../workspace/function-contracts.md) · [Evidence](evidence.json)','',
           '| Package | Declaration status | Behavioral gate |','|---|---|---|']
    for f in matrix['features']:
        key=f['id'];prefix=key.split('-')[0];group=PREFIX[prefix];names=SYMBOLS.get(key,['Title.GetTierFrame'] if 'RANK' in key else [])
        matches=[e for e in engine['entries'] if e['name'] in names]
        found={e['name'] for e in matches};missing=sorted(set(names)-found)
        status='export declarations available' if matches and not missing else 'mixed; missing names are not proof of unsupported API' if missing else 'source/asset contract, not an engine-command signature'
        row={'id':key,'source_sheet':f['sheet'],'declaration_status':status,
             'symbols_requested':names,'symbols_found':sorted(found),'unresolved_names':missing,
             'behavior_gate':f['resolution'],'runtime':'not run','source_root':group,
             'native_source_register':'../evidence/feature-source-closure.json',
             'context':PROFILES[prefix][0],'policy':PROFILES[prefix][1],
             'validation_focus':PROFILES[prefix][2]}
        result['features'].append(row)
        f['signature_status']=status;f['signature_symbols_available']=sorted(found)
        f['behavior_status']='specific source/caller/runtime gate retained';f['contract_card']='contracts/'+key+'.md'
        text=['# '+key+' contract card','',f'Family: **{group}**. Runtime: **not run**. Declaration status: **{status}**.','',
              f"[Original intent, costs, mechanics, variants and tests](../{f['sheet']}) · [Behavior guide](../../workspace/function-contracts.md)",'',
              '## Inputs, ownership and order','',PROFILES[prefix][0],PROFILES[prefix][1], '',
              '## Confirmed exported declarations','',
              '| Name | Kind | Scopes / targets / result as exported | Source |','|---|---|---|---|']
        for e in matches:
            desc='; '.join(e['supported_scopes']+e['supported_targets']+([e['return_type']] if e['return_type'] else [])) or 'See raw export fields; no invented type'
            target='../../'+e['source']['path']
            text.append(f"| `{e['name']}` | {e['category']} | {desc} | [line {e['line']}]({target}) |")
        if not matches:text.append('| No requested command declaration | source/asset | Native files and asset records remain primary | [Source register](../sources.md) |')
        text += ['','Unresolved discovery names: '+(', '.join('`'+n+'`' for n in missing) or 'none from this curated selection')+'. Missing names may have a different API owner/name; do not infer removal.','',
                 '## Exact remaining gate','',f['resolution'],'',PROFILES[prefix][2],'',
                 'No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.','',
                 '## Source retrieval','',
                 f'Root `{group}` has {len(by_root.get(group,[]))} read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.','',
                 'Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.']
        write(READY/'contracts'/ (key+'.md'), '\n'.join(text)+'\n')
        lines.append(f"| [{key}]({key}.md) | {status} | {f['resolution']} |")
    dump(READY/'contracts/evidence.json', result)
    write(READY/'contracts/README.md','\n'.join(lines)+'\n')
    dump(READY/'feature-matrix.json', matrix)
    print(json.dumps({'native_full_reads':len(source_reads),'workspace_text_reads':len(workspace),'feature_cards':len(result['features'])}))


if __name__=='__main__':main()
