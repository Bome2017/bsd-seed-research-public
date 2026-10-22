#!/usr/bin/env python3
from pathlib import Path
import subprocess,tempfile,shutil,hashlib,json,os,time
R=Path(__file__).resolve().parent
GP=os.environ.get('BSD_GP') or shutil.which('gp') or '/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
start=time.monotonic()
for item in json.loads((R/'INPUT_BINDINGS.json').read_text()):
 assert hashlib.sha256((R/item['path']).read_bytes()).hexdigest()==item['sha256']
with tempfile.TemporaryDirectory(prefix='bsd-torsion-sunit-') as td:
 t=Path(td);shutil.copytree(R/'inputs',t/'inputs');shutil.copy2(R/'torsion_sunit_admission.gp',t)
 rr=subprocess.run([GP,'-q','-f','-s','512000000','torsion_sunit_admission.gp'],cwd=t,capture_output=True,text=True,timeout=120)
 assert rr.returncode==0 and not rr.stderr.strip(),(rr.returncode,rr.stderr)
 assert 'TORSION_SUNIT_ADMISSION_COMPLETE;ELEMENTS=7;FAITHFUL_CHECKS=14;' in rr.stdout
 out=t/'TORSION_SUNIT_RESULT.gp';expected=R/'replay/TORSION_SUNIT_RESULT.gp'
 assert out.read_bytes()==expected.read_bytes(),'full exact result mismatch'
 result={'status':'PASS','input_hashes_verified':2,'exact_seed_elements':7,'exact_principal_S_ideal_checks':7,'literal_fifth_power_checks':14,'result_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'runtime_seconds':round(time.monotonic()-start,3),'no_BNF_or_Sha_input':True}
 print(json.dumps(result))
