#!/usr/bin/env python3
"""Fresh-directory exact replay; never appends to retained GP outputs."""
from pathlib import Path
import subprocess,tempfile,shutil,json,hashlib,os
R=Path(__file__).resolve().parent
GP=os.environ.get('BSD_GP','/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
with tempfile.TemporaryDirectory(prefix='bsd-primary-count-') as tmp:
 t=Path(tmp)
 for f in ['seed_nf.gp','nf12.gp','relative_fields.gp','split_prime_count.gp','summarize_ranges.gp','independent_relative_count.gp','point_count_check.py']:
  shutil.copy2(R/f,t/f)
 for gp,out in [('split_prime_count.gp','split_prime_count.out'),('summarize_ranges.gp','RANGE_DATA.json'),('independent_relative_count.gp','INDEPENDENT_RELATIVE_DATA.json')]:
  rr=subprocess.run([GP,'-q','-f','-s','512000000',gp],cwd=t,capture_output=True,text=True,timeout=130)
  if rr.returncode or rr.stderr.strip():raise RuntimeError((gp,rr.returncode,rr.stderr))
  (t/out).write_text(rr.stdout)
 for f in ['split_prime_count.out','split_prime_data.gp','RANGE_DATA.json','INDEPENDENT_RELATIVE_DATA.json']:
  assert (t/f).read_bytes()==(R/f).read_bytes(),f
  checks.append({'file':f,'sha256':sha(t/f),'byte_identical':True})
 subprocess.run(['python3','point_count_check.py'],cwd=t,capture_output=True,check=True,timeout=15)
 assert (t/'POINT_COUNT_CHECK.json').read_bytes()==(R/'POINT_COUNT_CHECK.json').read_bytes()
D,rg=json.loads((R/'RANGE_DATA.json').read_text());alt,allbase=json.loads((R/'INDEPENDENT_RELATIVE_DATA.json').read_text())
for e,c,np,nq,rr in rg:
 assert c**e<D<(c+1)**e
 aa=[r for r in alt if r[3]<=c]
 assert len(aa)==np
 assert sorted((r[0],r[3])for r in aa)==sorted((r[0],r[4])for r in rr)
out={'status':'PASS','primary_replay':checks,'independent_quadratic_residue_field_count_agrees':True,'independent_rational_point_count_agrees':True,'integer_threshold_checks':True,'scope':'actual split-prime supply only; no class rank, no small bound'}
(R/'REPLAY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','counts':[r[2]for r in rg]}))
