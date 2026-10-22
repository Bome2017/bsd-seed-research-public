"""Independent integer/mod-5 check of saved exact Brandt matrices, not their construction."""
from pathlib import Path
import json,gzip,math
r=Path(__file__).resolve().parent
d=json.loads((r/'BASE_BRANDT.json').read_text()); ms=json.load(gzip.open(r/'BASE_BRANDT_MATRICES.json.gz','rt'))
v=d['primitive_right_eigenvector']; h=len(v)
def rank5(rows):
    a=[[x%5 for x in row] for row in rows]; n=len(a); piv=0
    for j in range(h):
        k=next((i for i in range(piv,n) if a[i][j]),None)
        if k is None:continue
        a[piv],a[k]=a[k],a[piv]; u=pow(a[piv][j],-1,5)
        a[piv]=[(x*u)%5 for x in a[piv]]
        for i in range(piv+1,n):
            t=a[i][j]
            if t:a[i]=[(x-t*y)%5 for x,y in zip(a[i],a[piv])]
        piv+=1
        if piv==h:break
    return piv
stack=[]; out=[]
for rec,raw in zip(d['rows'],ms):
    q,a,T=rec['q'],rec['a_q'],raw['matrix']
    assert q==raw['q'] and len(T)==h and all(len(row)==h for row in T)
    assert all(T[i][j]==T[j][i] for i in range(h) for j in range(h))
    assert all(sum(row)==q+1 for row in T)
    assert all(sum(T[i][j]*v[j] for j in range(h))==a*v[i] for i in range(h))
    stack.extend([[x-(a if i==j else 0) for j,x in enumerate(row)] for i,row in enumerate(T)])
    dim=h-rank5(stack);assert dim==rec['F5_dimension'];out.append({'q':q,'dimension':dim})
assert all(x=='1' for x in d['weights'])
assert sum(v)==0 and math.gcd(*v)==1 and sum(x*x for x in v)==144
z={'status':'EXACT_SAVED_MATRIX_CHECK_PASS','class_number':h,'residual_dimensions':out,'primitive_eigenvector_norm':144,'doubled_vertex_norm':288,'component_degree_ratio_mod5':(-36*288)%5,'limits':'Verifies saved matrices and linear algebra; does not independently reconstruct Brandt correspondences.'}
(r/'BASE_BRANDT_VERIFY.json').write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))
