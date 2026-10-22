from pathlib import Path
from collections import defaultdict
import json,hashlib
R=Path(__file__).resolve().parent
A=R.parent/'small_conductor7/eval_data.json';B=R.parent/'local_rank/compact_units_11a1.json'
a=json.loads(A.read_text());b=json.loads(B.read_text());assert a[:4]==b[:4]
def key(x):return (tuple(x[0]),x[1])
base={key(v):i for i,v in enumerate(b[4])};assert len(base)==144
K=b[5];assert len(K)==864 and len(K[0])==26
E=[[0]*26 for _ in range(864)]
for j,u in enumerate(a[4]):
 for fac,powr in u:E[6*base[key(fac)]][j]+=powr
assert E==K
res={'status':'PASS','geometry_identity':True,'exported_compact_units':26,'distinct_atoms':144,'integer_exponents_preserved':True,'nonzero_initial_scalar_orbit':'j=0 only; projector applied separately','sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [A,B]}}
(R/'EVALUATOR_BINDING.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
