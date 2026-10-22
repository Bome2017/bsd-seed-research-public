"""Exact finite-field arithmetic on all projected units, not named Selmer classes."""
from pathlib import Path
from functools import lru_cache
import json, time, hashlib
R=Path(__file__).resolve().parent
F,XP,YP,SIG,raw_units=json.loads((R/'eval_data.json').read_text())
splits=json.loads((R/'split_primes.json').read_text())
def pack(p): return (tuple(p[0]),p[1])
XP,YP,SIG=map(pack,[XP,YP,SIG])
units=[[(pack(a),int(e)) for a,e in v] for v in raw_units]
def rank(a,p=5):
    a=[[x%p for x in row] for row in a]; row=0
    if not a:return 0
    for j in range(len(a[0])):
        k=next((k for k in range(row,len(a)) if a[k][j]),None)
        if k is None:continue
        a[row],a[k]=a[k],a[row]; c=pow(a[row][j],-1,p)
        a[row]=[x*c%p for x in a[row]]
        for k in range(len(a)):
            if k!=row:
                c=a[k][j];a[k]=[(x-c*y)%p for x,y in zip(a[k],a[row])]
        row+=1
        if row==len(a):break
    return row
def add(P,Q,q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v)%q==0:return None
    if P==Q:m=(3*x*x-4)*pow(2*y,-1,q)%q
    else:m=(v-y)*pow(u-x,-1,q)%q
    z=(m*m-x-u)%q
    return z,(-y+m*(x-z))%q
def mul(P,n,q):
    T=None
    for _ in range(n):T=add(T,P,q)
    return T
rows_all=[];norm_all=[];out=[];start=time.monotonic()
for q,roots in splits:
    assert q>2 and all(q%d for d in range(2,int(q**.5)+1))
    assert len(set(roots))==24
    assert all(sum(c*pow(r,i,q) for i,c in enumerate(F))%q==0 for r in roots)
    @lru_cache(None)
    def ev(a,r):
        coeff,d=a
        if d%q==0:raise ZeroDivisionError('denominator')
        v=0
        for c in reversed(coeff):v=(v*r+c)%q
        return v*pow(d,-1,q)%q
    try:
        pts=[(ev(XP,r),ev(YP,r)) for r in roots]
        assert len(set(pts))==24
        assert all((y*y-x*x*x+4*x-16)%q==0 and mul((x,y),5,q) is None for x,y in pts)
        idx={P:i for i,P in enumerate(pts)}
        perm=[roots.index(ev(SIG,r)) for r in roots]
        assert all(pts[perm[i]]==mul(pts[i],2,q) for i in range(24))
        z=next(pow(a,(q-1)//5,q) for a in range(2,q) if pow(a,(q-1)//5,q)!=1)
        dlog={pow(z,i,q):i for i in range(5)}
        logs=[]
        for r in roots:
            row=[]
            for factors in units:
                val=0
                for a,e in factors:
                    v=ev(a,r)
                    if not v:raise ZeroDivisionError('factor')
                    val+=e*dlog[pow(v,(q-1)//5,q)]
                row.append(val%5)
            logs.append(row)
        projected=[]
        for i in range(24):
            inds=[i]
            for _ in range(3):inds.append(perm[inds[-1]])
            projected.append([sum(c*logs[t][j] for c,t in zip([4,2,1,3],inds))%5 for j in range(13)])
        assert all(projected[perm[i]]==[(2*a)%5 for a in projected[i]] for i in range(24))
        cosets=set()
        for T in pts:
            line={mul(T,j,q) for j in range(5)}
            for P in pts:
                if P in line:continue
                cosets.add(tuple(sorted(idx[add(P,mul(T,j,q),q)] for j in range(5))))
        assert len(cosets)==24
        cosets=sorted(cosets)
        nr=[[sum(projected[i][j] for i in C)%5 for j in range(13)] for C in cosets]
        rows_all+=projected;norm_all+=nr
        out.append(dict(q=q,roots=roots,points=pts,scalar_permutation=perm,mu5_generator=z,
            projected_residue_rows=projected,affine_cosets=cosets,norm_rows=nr,
            projected_rank=rank(projected),norm_rank=rank(nr),
            cumulative_projected_rank=rank(rows_all),cumulative_norm_rank=rank(norm_all)))
    except ZeroDivisionError as exc:
        out.append(dict(q=q,excluded_reason=str(exc)))
result=dict(coefficient_prime=5,curve='1664n1',free_unit_candidates=13,
    source_character='sigma_2 acts as 2',projector_coefficients=[4,2,1,3],
    ordinary_character_unit_dimension=3,unit_residue_rank=rank(rows_all),
    norm_residue_rank=rank(norm_all),unit_kernel_upper=3-rank(norm_all),rows=out,
    class_condition='separate class quotient certification required; no class claim made by this evaluator',
    scope='complete unit-space bound once actual unit identities are authenticated; whole source also needs class control')
assert result['unit_residue_rank']<=3
assert result['norm_residue_rank']<=result['unit_residue_rank']
(R/'NORM_UPPER.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
print('ELAPSED_SECONDS',time.monotonic()-start)
