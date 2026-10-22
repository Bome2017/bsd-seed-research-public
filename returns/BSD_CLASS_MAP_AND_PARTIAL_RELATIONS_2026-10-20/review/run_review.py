#!/usr/bin/env python3
"""Portable, fail-closed replay of the review's inexpensive arithmetic checks."""
from pathlib import Path
import argparse,json,subprocess,sys,shutil
R=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--gp',default='gp');a=p.parse_args()
gp=shutil.which(a.gp)
if not gp: raise SystemExit('PARI/GP executable not found; pass --gp /path/to/gp')
subprocess.run([sys.executable,str(R/'replay.py')],cwd=R,check=True,timeout=30)
checks=[('replay_pivots','INDEPENDENT_IDEAL_PIVOT_REPLAY_OK=80'),('replay_scalar','INDEPENDENT_SCALAR_ORBIT_REPLAY_OK=80'),('replay_class_map','INDEPENDENT_CLASS_IDEAL_AND_CONNECTING_REPLAY_OK=1664n1'),('replay_faithful_class','INDEPENDENT_FAITHFUL_CLASS_AND_RATIONAL_POINT_OCCUPANCY_OK=1664n1'),('replay_complete_norm','INDEPENDENT_FULL_UNIT_MAP_RANK_OK=1664n1'),('replay_valuation_allowance','INDEPENDENT_FAITHFUL_S_VALUATION_ALLOWANCE_ZERO=1664n1')]
result=[]
for name,marker in checks:
 q=subprocess.run([gp,'-q','-f','-s','256000000',name+'.gp'],cwd=R,capture_output=True,text=True,timeout=60)
 (R/(name+'.out')).write_text(q.stdout);(R/(name+'.err')).write_text(q.stderr)
 if q.returncode or q.stderr.strip() or marker not in q.stdout: raise SystemExit(f'REJECTED {name}: code={q.returncode}, stderr={q.stderr!r}, stdout={q.stdout!r}')
 result.append({'script':name+'.gp','status':'passed','required_marker':marker})
subprocess.run([sys.executable,str(R/'replay_private_support.py')],cwd=R,check=True,timeout=30)
(R/'PORTABLE_REVIEW_RESULT.json').write_text(json.dumps({'status':'PASSED','checks':result,'scope':'Exact saved arithmetic replay; no new BNF certification or source search'},indent=2)+'\n')
print('PORTABLE_INDEPENDENT_REVIEW_PASSED')
