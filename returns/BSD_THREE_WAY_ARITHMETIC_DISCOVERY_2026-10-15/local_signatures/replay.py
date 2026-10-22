"""Replay saved arithmetic in an isolated copy; never overwrite retained outputs.
This verifies literal arithmetic/quotients, not fresh global source membership.
"""
from pathlib import Path
import shutil,tempfile,subprocess,sys,json,hashlib
R=Path(__file__).resolve().parent
scripts=['analyze_signatures.py','literal_replay.py','representative_controls.py','density_enumeration.py']
outputs=['RESULTS.json','LITERAL_REPLAY.json','REPRESENTATIVE_CONTROLS.json','DENSITY_ENUMERATION.json']
with tempfile.TemporaryDirectory(prefix='bsd-local-replay-') as t:
 root=Path(t);p=root/'local_signatures'
 shutil.copytree(R,p,ignore=shutil.ignore_patterns('__pycache__','REPLAY_RECEIPT.json'))
 (root/'incidence_review').mkdir()
 shutil.copy2(R.parent/'incidence_review/JOINT_DENSITY_PREDICTIONS.md',root/'incidence_review/JOINT_DENSITY_PREDICTIONS.md')
 for script in scripts:
  z=subprocess.run([sys.executable,script],cwd=p,capture_output=True,timeout=60)
  if z.returncode:raise RuntimeError(script+' failed: '+z.stderr.decode())
 receipt=[]
 for fn in outputs:
  a=json.loads((R/fn).read_text());b=json.loads((p/fn).read_text())
  if fn=='DENSITY_ENUMERATION.json':
   a.pop('sealed_prediction_path',None);b.pop('sealed_prediction_path',None)
  assert a==b,fn
  receipt.append({'output':fn,'canonical_sha256':hashlib.sha256((R/fn).read_bytes()).hexdigest(),'replay_equal':True})
 print(json.dumps({'status':'ISOLATED_ARITHMETIC_REPLAY_PASS','outputs':receipt,'scope':'All 120 local blocks, literal representatives, quotient controls and sealed finite matrix enumeration. No new GP scan, BNF, rank or global Selmer membership computation.'},indent=2))
