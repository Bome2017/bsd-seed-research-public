#!/usr/bin/env python3
"""Independent F3 elimination on exported arithmetic matrices; no PARI kernel calls."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def rref(a,n):
    a=[[x%3 for x in row] for row in a]; piv=[]
    for j in range(n):
        z=next((i for i in range(len(piv),len(a)) if a[i][j]),None)
        if z is None: continue
        i=len(piv);a[i],a[z]=a[z],a[i]
        a[i]=[x*pow(a[i][j],-1,3)%3 for x in a[i]]
        for k in range(len(a)):
            if k!=i:
                c=a[k][j];a[k]=[(x-c*y)%3 for x,y in zip(a[k],a[i])]
        piv.append(j)
    return a,piv
def rank(a,n=None):return len(rref(a,n if n is not None else len(a[0]) if a else 0)[1])
def kernel(a,n):
    rr,piv=rref(a,n);ans=[]
    for j in range(n):
        if j in piv:continue
        v=[0]*n;v[j]=1
        for i,c in enumerate(piv):v[c]=-rr[i][j]%3
        ans.append(v)
    return list(map(list,zip(*ans))) if ans else [[] for _ in range(n)]
def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*b)] for row in a]
def join(a,b):return [x+y for x,y in zip(a,b)]
def zero(a):return all(x==0 for row in a for x in row)
out=[]
for name,expected in [('389a1',(10,4,2)),('433a1',(13,6,3)),('655a1',(11,4,2))]:
    p=root/'controls'/name/'matrices.json';d=json.loads(p.read_text());n=d['source_dimension']
    V,U,S,A,L,W=[d[k] for k in ['valuation','units','scalar','additivity','local','points']]
    D=S+A+L;H=kernel(V,n);KU=kernel(mul(D,U),4)
    assert n==expected[0] and n-rank(S)==expected[1] and n-rank(S+A)==expected[2]
    assert n-rank(D)==2 and rank(W)==2 and zero(mul(D,W))
    assert rank(U)==4 and zero(mul(V,U)) and len(H[0])==4
    assert len(KU[0])==2
    adm_units=mul(U,KU)
    intersection=rank(W)+rank(adm_units)-rank(join(W,adm_units))
    assert intersection==2
    class_lifts=len(H[0])-rank(mul(D,H))-len(KU[0]);assert class_lifts==0
    assert n-rank(L)==2
    extra=d['extra'];ed=len(extra[0]) if extra else 0
    if name=='433a1':
        assert ed==1 and zero(mul(S+A,extra)) and not zero(mul(V,extra))
        assert rank(mul(L,extra))==1
        for block in d['local_blocks']:assert rank(mul(block['rows'],extra))==1
    else:assert ed==0
    out.append({'curve':name,'source':n,'scalar_kernel':n-rank(S),
                'scalar_additivity_kernel':n-rank(S+A),'local_kernel':n-rank(L),
                'joint_kernel':n-rank(D),'admitted_units':len(KU[0]),
                'point_unit_intersection':intersection,'admitted_class_lifts':class_lifts,
                'extra_allowed_valuation_directions_removed_locally':ed,
                'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
result={'status':'INDEPENDENT_F3_RANK_CHECK_PASS','scope':'Arithmetic matrices retained; elimination independent of producer; not a formal theorem check.','rows':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
