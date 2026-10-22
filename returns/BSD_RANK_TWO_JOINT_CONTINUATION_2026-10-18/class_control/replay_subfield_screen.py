#!/usr/bin/env python3
import pathlib, subprocess, time, json, sys
here=pathlib.Path(__file__).resolve().parent
gap=sys.argv[1] if len(sys.argv)>1 else '/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gap'
t=time.monotonic()
r=subprocess.run([gap,'-q','-b','-m','128m','-o','768m',str(here/'scalar_subgroup_screen.g')],capture_output=True,text=True,timeout=60,cwd=here)
assert r.returncode==0 and 'COMPLETED' in r.stdout and 'Error' not in r.stdout+r.stderr
rows=[list(map(int,line.split()[1:])) for line in r.stdout.splitlines() if line.startswith('SUBGROUP ')]
assert len(rows)==84
assert all(z>1 for n,i,z in rows if i<48)
assert min(i for n,i,z in rows if z==1)==48
old=json.loads((here/'SUBFIELD_SCREEN.json').read_text())
assert sorted(rows)==sorted(old['rows'])
print(json.dumps({'status':'PASS','subgroup_classes':84,'minimum_center_disjoint_index':48,'elapsed_seconds':time.monotonic()-t,'class_bound_proved':False},indent=2))
