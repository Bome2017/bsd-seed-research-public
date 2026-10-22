"""Isolated deterministic arithmetic replay; no GP or new source computation."""
from pathlib import Path
import json,shutil,tempfile,subprocess,sys,hashlib
R=Path(__file__).resolve().parent
outputs=['KERNEL_RESULTS.json','ADMISSION_FILTRATION.json','HOLDOUT_COMPARISON.json','433_COMMON_REPAIR.json','FRESH_433_LITERAL_REPLAY.json']
with tempfile.TemporaryDirectory(prefix='bsd-joint-kernel-replay-')as tmp:
 T=Path(tmp)/'joint_kernel';shutil.copytree(R,T,ignore=shutil.ignore_patterns('__pycache__','REPLAY_RECEIPT.json'))
 for script in ['calculate.py','compare_holdout.py','replay_433_literal.py']:
  z=subprocess.run([sys.executable,script],cwd=T,capture_output=True,timeout=60)
  if z.returncode:raise RuntimeError(script+' failed: '+z.stderr.decode())
 checked=[]
 for name in outputs:
  assert (R/name).read_bytes()==(T/name).read_bytes(),name
  checked.append({'path':name,'sha256':hashlib.sha256((R/name).read_bytes()).hexdigest(),'byte_identical':True})
 print(json.dumps({'status':'ISOLATED_JOINT_KERNEL_REPLAY_PASS','outputs':checked,'scope':'Full-source finite algebra, after-the-fact heldout comparison and624 literal433 evaluations. No upstream BNF, rank or norm-map rerun.'},indent=2))
