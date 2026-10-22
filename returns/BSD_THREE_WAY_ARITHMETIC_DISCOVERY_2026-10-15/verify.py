#!/usr/bin/env python3
"""Verify custody then replay small Python arithmetic in an isolated copy.
This does not regenerate the PARI source elements or prove retained inputs.
"""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
R=Path(__file__).resolve().parent
manifests=list(R.rglob('MANIFEST.sha256'));entries=0
for manifest in manifests:
 for line in manifest.read_text().splitlines():
  if not line:continue
  digest,name=line.split(None,1);name=name.strip().removeprefix('*');p=(manifest.parent/name).resolve()
  if not p.is_relative_to(R):raise RuntimeError(('manifest path outside packet',name))
  if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:raise RuntimeError(('hash mismatch',str(p)))
  entries+=1
jobs=[('incidence_review/check_incidence.py','incidence_review/RESULT.json'),('independent_review/check_local.py','independent_review/LOCAL_REPLAY.json'),('independent_review/check_frobenius.py','independent_review/FROBENIUS_REPLAY.json'),('local_signatures/density_enumeration.py','local_signatures/DENSITY_ENUMERATION.json')]
results=[]
with tempfile.TemporaryDirectory(prefix='bsd-three-way-check-') as tmp:
 dst=Path(tmp)/R.name;shutil.copytree(R,dst,ignore=shutil.ignore_patterns('__pycache__'))
 for script,result in jobs:
  proc=subprocess.run([sys.executable,str(dst/script)],cwd=dst,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=60)
  if proc.returncode or proc.stderr:raise RuntimeError((script,proc.returncode,proc.stderr,proc.stdout[-1000:]))
  old=json.loads((R/result).read_text());new=json.loads((dst/result).read_text())
  for obj in [old,new]:obj.pop('sealed_prediction_path',None)
  if old!=new:raise RuntimeError(('replay differs',result))
  results.append({'script':script,'result_matches':True})
print(json.dumps({'status':'CUSTODY_AND_BOUNDED_ARITHMETIC_REPLAY_PASSED','manifest_files':len(manifests),'manifest_entries_including_nested':entries,'replays':results,'scope':'Does not rerun imported rank/saturation/descent inputs or certify an endpoint.'},indent=2))
