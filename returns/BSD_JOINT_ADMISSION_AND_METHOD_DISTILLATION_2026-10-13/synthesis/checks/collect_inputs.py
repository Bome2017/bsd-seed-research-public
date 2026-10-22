from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[1]
base=Path('/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe')
lab=Path('/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/work/returns')
rows=[];bindings=[]
def copy(src,dst):
 src=Path(src);out=root/dst;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,out)
 bindings.append({'source':str(src),'copy':str(out.relative_to(root)),'bytes':src.stat().st_size,'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
 return str(out.relative_to(root))
configs=[('seed',17,103,'l103'),('seed',19,191,'p19_l191_v2'),('seed',23,47,'p23_l47'),('seed',29,59,'p29_l59'),('seed',29,233,'p29_l233_v2'),('seed',31,311,'p31_l311'),('seed',37,149,'p37_l149'),('seed',41,83,'p41_l83'),('seed',43,173,'p43_l173'),('seed',47,283,'p47_l283'),('seed',83,167,'p83_l167'),('seed',5,191,'p19_l191_v2'),('seed',5,311,'p31_l311'),('seed',3,103,'l103'),('389a1',7,29,'l29'),('389a1',7,379,'l379')]
for curve,p,l,run in configs:
 src=(base/('seed_runs' if curve=='seed' else 'launcher_runs')/run) if p!=83 else lab/'BSD_SEED_P83_CERTIFICATE_2026-10-13/production/p83_l167'
 paths={name:copy(src/name,Path('inputs/tame')/run/name) for name in ['msl.txt','RUN_MANIFEST.json','SINGLETON_REPORT.json']}
 rows.append({'curve':curve,'p':p,'ell':l,'run':run,'paths':paths,'role':'positive_excess_control' if p==3 else ('inconclusive_zero' if (curve,p,l) in [('seed',29,59),('389a1',7,379)] else 'nonzero_certificate_or_crosscheck')})
ordinary=[]
for p in [5,7,11,13]:
 if p==5: src=Path('/Users/bsm/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run')
 elif p==13: src=Path('/Users/bsm/BSD_SEED_P13_RUN_2026-09-21/run')
 else: src=Path(f'/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p{p}/run')
 ordinary.append({'p':p,'top':copy(src/f'SYMBOLS_m{p*p}.txt',f'inputs/ordinary/p{p}_top.txt'),'lower':copy(src/f'SYMBOLS_m{p}.txt',f'inputs/ordinary/p{p}_lower.txt')})
(root/'INPUTS.json').write_text(json.dumps({'tame':rows,'ordinary':ordinary},indent=2)+'\n')
uniq={r['copy']:r for r in bindings}
(root/'INPUT_BINDINGS.json').write_text(json.dumps(list(uniq.values()),indent=2)+'\n')
print(len(uniq),'input files bound')
