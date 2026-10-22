#!/usr/bin/env python3
"""Replay the finite actual-seed basis-pair source pilot; no full BNF."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile,time
root=Path(__file__).resolve().parent
gp=sys.argv[1] if len(sys.argv)>1 else shutil.which('gp')
if not gp: raise SystemExit('Provide the PARI/GP executable as the first argument.')
for row in json.loads((root/'INPUT_BINDINGS.json').read_text()):
    assert hashlib.sha256((root/row['local_path']).read_bytes()).hexdigest()==row['sha256']
with tempfile.TemporaryDirectory(prefix='bsd_basis_source_') as td:
    wd=Path(td);shutil.copytree(root/'inputs',wd/'inputs')
    shutil.copy2(root/'basis_unit_scan.gp',wd/'basis_unit_scan.gp')
    start=time.monotonic()
    cp=subprocess.run([gp,'-q','-s','512000000','basis_unit_scan.gp'],cwd=wd,capture_output=True,text=True,timeout=120)
    elapsed=time.monotonic()-start
    assert cp.returncode==0 and not cp.stderr, (cp.returncode,cp.stderr)
    marker='BASIS_UNIT_COMPLETE;CHECKED=2232;UNITS=1;RELATIVE_NONTORSION=0'
    assert marker in cp.stdout
    output=(wd/'BASIS_UNIT_RESULT.gp').read_bytes()
    assert output==(root/'BASIS_UNIT_RESULT.gp').read_bytes(), 'Exact result mismatch'
    (root/'basis_unit_replay.out').write_text(cp.stdout)
    record={'status':'PASS','checked':2232,'ordinary_unit_candidates':1,'nontrivial_relative_units':0,'exact_result_matches':True,'elapsed_seconds':elapsed,'gp_stack_bytes':512000000,'timeout_seconds':120,'input_hashes_verified':True,'scope':'Exact finite source pilot only; retained maximal order and scalar action, no class bound'}
    (root/'REPLAY_RESULT.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
