from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,time,json
R=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
def run(x):
 name,budget,marker=x;start=time.monotonic()
 with (R/(name+'.out')).open('w') as out,(R/(name+'.err')).open('w') as err:
  p=subprocess.Popen([GP,'-q','-f','-s','256M',name],stdout=out,stderr=err,cwd=R)
  try:rc=p.wait(timeout=budget);timeout=False
  except subprocess.TimeoutExpired:p.kill();rc=p.wait();timeout=True
 text=(R/(name+'.out')).read_text();res={'script':name,'budget_seconds':budget,'elapsed_seconds':time.monotonic()-start,'returncode':rc,'timeout':timeout,'required_marker':marker,'success':marker in text}
 (R/(name+'.receipt.json')).write_text(json.dumps(res,indent=2)+'\n');return res
with ThreadPoolExecutor(max_workers=2) as p:
 for r in p.map(run,[('certify_quotient.gp',60,'CLASS_QUOTIENT_CERTIFIED;'),('authenticate_units.gp',110,'EXACT_FREE_UNIT_AUTHENTICATION_PASS;')]):print(json.dumps(r),flush=True)
