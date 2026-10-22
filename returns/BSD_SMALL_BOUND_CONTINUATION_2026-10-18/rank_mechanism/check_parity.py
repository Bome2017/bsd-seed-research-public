from pathlib import Path
import json, hashlib
BASE=Path('/Users/bsm/BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15')
R=Path(__file__).resolve().parent
D=json.loads((BASE/'p5_norm_upper/NORM_UPPER.json').read_text())
row=next(x for x in D['rows'] if x.get('q')==1831)
q=row['q']; pts=[tuple(P) for P in row['points']]; lookup={P:i for i,P in enumerate(pts)}
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v+1)%q==0:return None
    if P==Q:m=(3*x*x+2*x-2)*pow(2*y+1,-1,q)%q
    else:m=(v-y)*pow(u-x,-1,q)%q
    z=(m*m-1-x-u)%q
    return z,(-y+m*(x-z)-1)%q
def mul(P,n):
    Z=None
    for _ in range(n):Z=add(Z,P)
    return Z
perms={a:[lookup[mul(P,a)] for P in pts] for a in range(1,5)}
weights={a:(4*pow(a,-1,5))%5 for a in range(1,5)}
def project(vals):
    return [__import__('functools').reduce(lambda x,av:x*pow(vals[perms[av[0]][i]],av[1],q)%q,weights.items(),1) for i in range(24)]
candidates=[]
for a in range(1,5):
    vals=[(2*pts[perms[a][i]][1]+1)%q for i in range(24)]
    candidates.append((f'w({a}T)', vals))
for a in range(1,5):
    for b in range(a+1,5):
        if (a+b)%5:
            vals=[(pts[perms[a][i]][0]-pts[perms[b][i]][0])%q for i in range(24)]
            candidates.append((f'x({a}T)-x({b}T)', vals))
        vals=[(2*pts[perms[a][i]][1]+1)*pow((2*pts[perms[b][i]][1]+1)%q,-1,q)%q for i in range(24)]
        candidates.append((f'w({a}T)/w({b}T)',vals))
records=[]
for name,vals in candidates:
    assert all(vals)
    projected=project(vals)
    residues=[pow(v,(q-1)//5,q) for v in projected]
    assert set(residues)=={1}
    records.append({'candidate':name,'projected_fifth_power_residues':residues})
# Exact group algebra argument over every tested prime: odd projection
# annihilates the plus-invariant subspace. Independent of actual units.
primes=[3,5,7,11,13,17,19,23,29,31,37,41,43]
formal=[]
for p in primes:
    weights={a:pow(p-1,-1,p)*pow(a,-1,p)%p for a in range(1,p)}
    pairs=[(a,p-a) for a in range(1,(p+1)//2)]
    assert all((weights[a]+weights[b])%p==0 for a,b in pairs)
    formal.append({'p':p,'paired_projection_sums':[int((weights[a]+weights[b])%p) for a,b in pairs]})
result={'actual_curve':'389a1','coefficient_prime':5,'split_prime':q,'candidate_count':len(records),'actual_evaluations':24*len(records),'projected_power_residue':1,'checks':records,'formal_checks':formal,'scope':'Parity controls on actual torsion evaluations; no global unitness or new seed norm-rank claimed.'}
(R/'PARITY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('checks','formal_checks')},indent=2))
