from pathlib import Path
import json,sys,hashlib,subprocess,datetime
b=Path(__file__).resolve().parent.parent; s=b/'selection'; f=b/'FROZEN_RUN_PACKAGE_p83_l167'
state=json.loads((b/'STATE.json').read_text())
assert state['returncode'] is not None, 'Refusing postrun while process has not finished'
assert state['stop_reason'] is None, 'Stopped run: no mathematical postrun verdict'
c=json.loads((f/'config/RUN_CONFIG.json').read_text());o=Path(c['outdir'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source_files=[o/'SINGLETON_REPORT.json',o/'RUN_MANIFEST.json',o/'msl.txt',o/'units/PARAMS',f/'checker/singleton_check.py',f/'runtime/src/arbcore']
before={str(p):sha(p) for p in source_files}
with (s/'POSTRUN_FREEZE_CHECK.json').open('w') as log:
 verify=subprocess.run([sys.executable,str(f/'verify_freeze.py')],stdout=log,stderr=subprocess.PIPE,text=True)
(s/'POSTRUN_FREEZE_CHECK.stderr.txt').write_text(verify.stderr)
assert verify.returncode==0,('freeze verification failed',verify.returncode,verify.stderr)
cmd=[sys.executable,str(f/'checker/singleton_check.py'),'--msl',str(o/'msl.txt'),'--units',str(o/'units'),'--manifest',str(o/'RUN_MANIFEST.json'),'--receipts',c['receipts_glob'],'--arbcore',str(f/'runtime/src/arbcore'),'--curve',c['curve'],'--N',str(c['N']),'--p',str(c['p']),'--l',str(c['l']),'--Q',str(c['Q']),'--sign',str(c['sign']),'--T',str(c['T']),'--segq',str(c['SEGQ']),'--latden',str(c['LATDEN']),'--apdir',c['apdir'],'--pinned-segroot',c['pinned_segroot'],'--out',str(s/'POSTRUN_CHECKER_REPORT.json')]
with (s/'POSTRUN_CHECKER.log').open('w') as log:
 result=subprocess.run(cmd,stdout=log,stderr=subprocess.PIPE,text=True)
(s/'POSTRUN_CHECKER.stderr.txt').write_text(result.stderr)
after={str(p):sha(p) for p in source_files}
assert before==after,'Producer or frozen files changed during read-only postrun checks'
report=json.loads((s/'POSTRUN_CHECKER_REPORT.json').read_text())
record={'status':'PASS' if result.returncode==0 else 'CHECKER_NONZERO_EXIT','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'run_returncode':state['returncode'],'freeze_check':json.loads((s/'POSTRUN_FREEZE_CHECK.json').read_text()),'checker_returncode':result.returncode,'checker_verdict':report.get('verdict'),'c2_mod_p':report.get('c2_mod_p'),'producer_and_source_hashes_before':before,'producer_and_source_hashes_after':after,'source_files_unchanged':before==after,'checker_command':cmd,'postrun_checker_sha256':sha(s/'POSTRUN_CHECKER_REPORT.json'),'producer_report_preserved':True,'scope':'Fresh checksum custody plus unchanged-checker replay, not independent modular-symbol production.'}
(s/'POSTRUN_CUSTODY.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
sys.exit(result.returncode)
