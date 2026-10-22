"""Fail-closed arithmetic replay; does not replace the written source audit."""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--gp',required=True)
p.add_argument('--sage-python',required=True)
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
jobs=[('certified_field',[a.gp,'-fq','-s','128M','checks/certified_field.gp']),
      ('independent_exact',[sys.executable,'checks/independent_exact.py']),
      ('fisher_model',[a.sage_python,'implementation/fisher_model.py']),
      ('geometry',[a.sage_python,'implementation/geometry_check.py']),
      ('audit_exact',[a.sage_python,'audit/independent_exact.py'])]
rows=[]
for name,cmd in jobs:
    cp=subprocess.run(cmd,cwd=root,capture_output=True,text=True,timeout=90)
    (root/f'outputs/{name}.replay.out').write_text(cp.stdout)
    (root/f'outputs/{name}.replay.err').write_text(cp.stderr)
    ok=cp.returncode==0 and not cp.stderr
    if name=='certified_field': ok=ok and 'ALL_CERTIFIED_FIELD_ASSERTIONS_PASS' in cp.stdout
    rows.append({'name':name,'command':cmd,'exit_code':cp.returncode,'stderr_empty':not cp.stderr,'passed':ok})
    print(name, 'PASS' if ok else 'FAIL',flush=True)
    if not ok: raise RuntimeError(name+': '+cp.stderr)
receipt={'status':'ALL_CHECKS_PASS','checks':rows,
         'executables':{str(Path(z).resolve()):hashlib.sha256(Path(z).read_bytes()).hexdigest() for z in [a.gp,a.sage_python]},
         'scope':'Arithmetic and geometry replay, not a fresh rank descent, formal proof or seed bound.'}
(root/'outputs/REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n')
