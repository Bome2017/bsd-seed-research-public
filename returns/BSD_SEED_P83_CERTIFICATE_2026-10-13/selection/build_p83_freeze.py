from pathlib import Path
import hashlib,json,shutil,datetime,os
base=Path('/Users/bsm/BSD_UNRESOLVED_SEED_PUSH_2026-10-13'); sel=base/'selection'; out=base/'FROZEN_RUN_PACKAGE_p83_l167'
sp=Path('/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe')
core=Path('/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19')
assert not out.exists(),str(out)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cp(src,dst):
 d=out/dst;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,d);return d
for name in ['singleton_check.py','run_singleton.sh','test_singleton_check.py','CONTROLS.json']:
 cp(sp/'FROZEN_RUN_PACKAGE_l103/checker'/name,'checker/'+name)
cp(core/'src/arbcore','runtime/src/arbcore'); cp(core/'src/arbcore.c','runtime/src/arbcore.c')
assert sha(out/'runtime/src/arbcore')=='47d07f2e856e82d2fece7834085aa99d30fa65d32137f0fde843022050fd89db'
for name in ['SINGLETON_SPEC.md','SINGLETON_ROUTE_NOTE.md']:
 cp(sp/'FROZEN_RUN_PACKAGE_l103/spec'/name,'spec/'+name)
cp(Path('/Users/bsm/BSD_P53_L743_RUN_2026-10-01/FROZEN_RUN_PACKAGE_p53_l743/spec/SINGLETON_SPEC_v1_audited.md'),'spec/SINGLETON_SPEC_v1_audited.md')
for name in ['CUSTODY_STATUS.json','PREFIX_3420_CUSTODY.json','CHECKER_BINDINGS.json','CONTROLS_REPLAY.txt','tmin167_L1024.txt','tmin167_L4096.txt','P83_OTA_THEOREM_CHECK.md','check_p83.py','check_p83.json']:
 cp(sel/name,('corpus/' if 'CUSTODY' in name else 'checks/')+name)
cp(sel/'controls/checker/CONTROLS.json','checks/CONTROLS_REPLAY.json')
cp(sp/'corpus_ext_6445/CORPUS_CHECK_6445.json','corpus/RETAINED_CORPUS_CHECK_6445.json')
cp(sel/'hash_prefix.py','corpus/hash_prefix_source.py')
# Copy each original verified receipt byte-for-byte; sources and their hashes stay in the custody JSON.
r=json.loads((sel/'PREFIX_3420_CUSTODY.json').read_text())
receipts=sorted({row['receipt_path'] for row in r['rows']})
for src in receipts:cp(src,'corpus/receipts/'+Path(src).name)
cp(sp/'mt_prescreen/PREDICTIONS_2026-09-26.md','diagnostic/PREDICTIONS_2026-09-26.md')
assert sha(out/'diagnostic/PREDICTIONS_2026-09-26.md')=='4853a5fbdb0a6a16a63c13681a010f19d47d7e439c493c565988372b51396ffd'
for name in ['p83_prescreen.gp','p83_prescreen.out']:cp(sel/name,'diagnostic/'+name)
cp(sp/'mt_prescreen/tame_reg.gp','diagnostic/tame_reg.gp')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
config={'frozen_utc':now,'status':'FROZEN_NOT_LAUNCHED','curve':'0 -22735 0 106272484 0','minimal_model':[0,-1,0,-66020924,-65074271436], 'N':6503188012738584,'p':83,'l':167,'Q':6503188012738584,'sign':1,'T':57378078719,'SEGQ':16777216,'segments':3420,'LATDEN':1024,'planner_LATDEN':4096,'planner_TMIN':57366635244,'workers':8,'primitive_root':5,'apdir':str(sp/'corpus_ext_6445/view/ap'),'receipts_glob':str(out/'corpus/receipts/ver_*.log'),'pinned_segroot':r['prefix_root'],'outdir':str(base/'production/p83_l167'),'arbcore_path':str(out/'runtime/src/arbcore'),'arbcore_sha256':sha(out/'runtime/src/arbcore'),'PARI':'/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4','stage_W_permitted':False,'corpus_extension_permitted':False,'estimated_wall_minutes':[45,60],'caps':{'cpu_hours':20,'wall_hours':3,'new_bytes':5000000000,'minimum_free_bytes':60000000000,'external_spend_USD':0},'authorization_basis':'Current human instruction to continue the actual seed work, carried out by the parent as one bounded cached-corpus p83 calculation; not a claim that the historical p53 launch was authorized. Root approved this p83 freeze and caps on 2026-10-13.','prediction':{'value':44,'modulus':83,'grade':'UNPROVED_K288_DIAGNOSTIC_ONLY','used_by_acceptance':False,'source_sha256':sha(out/'diagnostic/PREDICTIONS_2026-09-26.md')}}
config['expected_PARAMS']=' '.join(['msl']+config['curve'].split()+[str(config[x]) for x in ['l','Q','sign','T','SEGQ']]+[os.path.realpath(config['apdir']),os.path.realpath(config['outdir']+'/units'),str(config['LATDEN'])])
(out/'config').mkdir();(out/'config/RUN_CONFIG.json').write_text(json.dumps(config,indent=2)+'\n')
# This command documents the exact calculation. The parent runs it under its resource monitor.
cmd=f'''C={out}/runtime PARI={config['PARI']} LATDEN=1024 SEGQ=16777216 SIGN=1 SINGLETON_AUTHORIZED=yes caffeinate -i {out}/checker/run_singleton.sh "{config['curve']}" {config['N']} 83 167 {config['T']} {config['apdir']} "{config['receipts_glob']}" {config['outdir']} 8 {config['pinned_segroot']}'''
(out/'LAUNCH_COMMAND.txt').write_text(cmd+'\n')
(out/'PREREGISTRATION.md').write_text('''# Frozen seed singleton p83 / ell167

Date: 2026-10-13. This package is frozen before the target run. It contains no evaluated target numerator and no claim of a new prime certificate yet.

The current user has authorized continuing actual seed work. The parent selected this bounded cached-data calculation and approved W=8 and the caps below. This is not a revival of the unlaunched p53 job or permission to extend the coefficient corpus. No paid service or external job is involved.

## Calculation and custody

Run the unchanged arbcore binary, SHA256 `47d07f2e856e82d2fece7834085aa99d30fa65d32137f0fde843022050fd89db`, on the seed pipeline model with p=83, ell=167, Q=N=6503188012738584, sign=+1, T=57378078719, SEGQ=16777216, LATDEN=1024, and eight workers. Parameters and exact absolute paths are in `config/RUN_CONFIG.json` and `LAUNCH_COMMAND.txt`. The 14-field engine PARAMS is predeclared. Workers affect scheduling, not the mathematical parameters.

The 3420 existing coefficient segments have total size 9,673,187,648 bytes. They have all been freshly SHA256-checked against their verifier receipts without regenerating them. The pinned receipt root is `53de8838b356300dbb7aed6cfc57cab3498c82bd585954fd244095e338f997da`. Raw receipts are copied byte-for-byte into this package; the source receipt paths, source hashes, coefficient hashes, resolved paths and stable file metadata are in `corpus/PREFIX_3420_CUSTODY.json`. The historical full-corpus arithmetic acceptance remains a retained input; fresh hashes authenticate its bytes, not a second independent coefficient computation.

## Tail margin: keep the two denominators distinct

**The planner alone uses LATDEN4096. The evaluator and acceptance checker use LATDEN1024.** The fresh rigorous planner cutoff is TMIN57366635244. Aligning upward gives T57378078719. This makes the normalized truncation tail at most one quarter of the (1/1024)Z identification budget, following the historical p43 practice. Changing the engine or checker to LATDEN4096 would tighten the identification budget by another factor four and lose that reserved quarter margin. No such change is allowed.

## Acceptance, fixed before the arithmetic

The unchanged acceptance checker must verify input root, engine/output hashes, exact PARAMS, row completeness, count identity, rigorous unique lattice identification, symmetry, c0=0, and c1=0 modulo83. Only then:

- `NONZERO`, exit0, with c2 nonzero modulo83: the retained Ota theorem gives Sha(E/Q)[83^infinity]=0.
- `INCONCLUSIVE_ZERO`, exit3: the certified residue is zero and this auxiliary gives no vanishing result.
- `INVALID`, refusal, crash, inconsistent record or resource breach: stop with no mathematical verdict; do not reinterpret it as zero.

The theorem hypotheses and local arithmetic are separately recorded in `checks/P83_OTA_THEOREM_CHECK.md`. The checker passed all20 unchanged positive/negative controls. Global rank/image/Manin/Tamagawa facts retain their existing grades.

## Prediction is independent of acceptance

The separate diagnostic predicts c2=44 modulo83 from the unproved K288 relation. Its source was sealed September26 and is hashed here. A fresh tame-regulator replay gives R_E=42 modulo83, reproducing that diagnostic. The checker never reads this prediction, a regulator, a Sha order or a desired residue. A certified nonzero disagreement still has the Ota consequence; the prediction must be recorded as a disagreement and investigated without recalibration. A certified zero is both inconclusive for Sha and a diagnostic disagreement. No alternate auxiliary run is admitted automatically.

## Resources and stop rules

Expected wall time is45–60 minutes from a comparable historical job and fresh bounded timing. W=8 was selected because W12/W16 supplied no measured speed benefit. Caps:20 CPU-hours,3 wall-hours,5GB new files,60GB available-space floor, external spend$0. The parent must use its monitored launch; the unchanged historical launcher does not itself enforce these resource caps. No StageW, new coefficient generation, corpus extension, p53 calculation, automatic next prime or modification of frozen source data is permitted. Preserve incomplete outputs and the failure reason if stopped.

A successful p83 result adds actual base-field primary coverage. It does not settle the smallest unresolved prime53, does not raise the conditional ORDER9 floor25281, and does not prove FIN, ORDER9, Q36 or the infinite-prime theorem.
''')
(out/'README.md').write_text('''# p83 / ell167 frozen input package

Read `PREREGISTRATION.md`, then `config/RUN_CONFIG.json`. Run `python3 verify_freeze.py` for read-only byte/corpus verification. The parent launches the literal `LAUNCH_COMMAND.txt` under its resource monitor after inspection. Nothing in this package initiates the full job automatically.

`MANIFEST.sha256` binds all files other than itself. `FREEZE_MANIFEST.json` binds the input inventory, config and pinned receipt root. Source and checker are unmodified; data producers are not present or invoked. Diagnostics are separate from acceptance.
''')
print(out)
