#!/usr/bin/env python3
"""Independent exact arithmetic controls, not a GZ or graph-model certificate."""
from pathlib import Path
import gzip, hashlib, json
from math import gcd

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent
base_path=PARENT/'checks/BASE_BRANDT.json'
mat_path=PARENT/'checks/BASE_BRANDT_MATRICES.json.gz'
b=json.loads(base_path.read_text())
f=b['primitive_right_eigenvector']
assert len(f)==176 and sum(f)==0 and sum(x*x for x in f)==144
assert set(map(int,b['weights']))=={1}
with gzip.open(mat_path,'rt') as fp: mats=json.load(fp)

def rank_mod(rows,p):
    a=[[x%p for x in r] for r in rows]
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,p)
        a[rank]=[(x*inv)%p for x in a[rank]]
        for i in range(rank+1,len(a)):
            if a[i][j]:
                c=a[i][j]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a[0]): break
    return rank

stack=[]; dimensions=[]
trace={2:-1,13:-7,17:-3}
for item in mats:
    q=item['q'];a=item['matrix'];t=trace[q]
    assert len(a)==176 and all(len(r)==176 for r in a)
    assert all(sum(r)==q+1 for r in a)
    assert all(a[i][j]==a[j][i] for i in range(176) for j in range(176))
    assert [sum(x*y for x,y in zip(r,f)) for r in a]==[t*x for x in f]
    stack.extend([[v-(t if i==j else 0) for j,v in enumerate(r)] for i,r in enumerate(a)])
    dimensions.append(176-rank_mod(stack,5))
assert dimensions==[11,4,1]

def ap(a,q):
    pts=1+sum((y*y+a[0]*x*y+a[2]*y-x**3-a[1]*x*x-a[3]*x-a[4])%q==0
              for x in range(q) for y in range(q))
    return q+1-pts
E=[1,1,1,3,12];E1=[1,1,1,1878418,-485198548]
counts={label:{str(q):ap(curve,q) for q in [2,5,13]} for label,curve in [('base',E),('raised',E1)]}
source_base=2*(counts['base']['5']-6)-(counts['base']['13']-14)
source_raised=2*(counts['raised']['5']-6)-(counts['raised']['13']-14)
assert (source_base,source_raised)==(3,-2)
assert source_raised*pow(source_base,-1,5)%5==1

norm_factor=(-36*2*sum(x*x for x in f))%5
delta0=20576640;deltaX=delta0//70
assert delta0==70*deltaX and deltaX==293952 and norm_factor==2
assert gcd(delta0,11)==1
component_square=deltaX*pow(norm_factor,-1,5)%5
normalized_source_square=9*(source_raised*pow(source_base,-1,5))**2%5
assert component_square==1 and normalized_source_square==4
i=f.index(1);j=f.index(0)
assert f[i]-f[j]==1

result={'status':'EXACT_ARITHMETIC_CONTROLS_PASS',
 'scope':'Checks recorded Brandt matrices and arithmetic constants; does not rederive quaternion model, C3, GZ or analytic enclosures.',
 'matrix_dimensions_mod5':dimensions,'point_counts_traces':counts,
 'base_norm':144,'doubled_norm':288,
 'even_source_indices_zero_based':[i,j],'source_evaluation':1,
 'raw_source_scalar_base':source_base,'raw_source_scalar_raised':source_raised,
 'normalized_source_multiplier_mod5':1,'graph_degree_over_component_square_mod5':norm_factor,
 'retained_classical_degree':delta0,'derived_shimura_degree':deltaX,
 'conditional_component_square':component_square,
 'conditional_normalized_source_ratio_square':normalized_source_square}
(ROOT/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
paths=[base_path,mat_path,PARENT/'component/COMPONENT_UNIT.md',PARENT/'component/BASIS_AND_DEGREE_REVIEW.md',
 PARENT/'cm/RESULT.md',PARENT/'cm/CERTIFIED_GZ_INGREDIENTS.json',PARENT/'cm/alldegphi.420000-429999',
 Path('/Users/bsm/BSD_EXACT_BD_CONSTANT_2026-10-07/construction/CONSTRUCTION.md'),
 Path('/Users/bsm/BSD_COMPARISON_EXPERIMENT_CODEX_2026-10-11/geometry/MIXED_PLACE_DIAGRAM.md')]
bindings=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in paths]
(ROOT/'INPUT_BINDINGS.json').write_text(json.dumps(bindings,indent=2)+'\n')
print(json.dumps(result,indent=2))
