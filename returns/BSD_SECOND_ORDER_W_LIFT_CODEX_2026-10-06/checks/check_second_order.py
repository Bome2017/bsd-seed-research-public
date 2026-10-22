#!/usr/bin/env python3
"""Exact algebra controls. No seed Selmer or Galois cohomology is computed."""
import itertools, json, math, random
from pathlib import Path

rng=random.Random(20261006)
counts={}

def check(name, statement):
    assert statement, name
    counts[name]=counts.get(name,0)+1

def mul(a,b,p,n):
    c=[0]*n
    for i,x in enumerate(a[:n]):
        for j,y in enumerate(b[:n-i]): c[i+j]=(c[i+j]+x*y)%p
    return c

def power(a,m,p,n):
    out=[1]+[0]*(n-1)
    while m:
        if m&1: out=mul(out,a,p,n)
        a=mul(a,a,p,n); m//=2
    return out

def expcoef(x,p,n):
    return [pow(x,i,p)*pow(math.factorial(i),-1,p)%p for i in range(n)]

def pair(v,w,p,n):
    return sum((-1)**j*(v[i][0]*w[j][1]-v[i][1]*w[j][0])
               for i in range(n) for j in range(n) if i+j==n-1)%p

def ttimes(v): return [[0,0]]+v[:-1]

def act(v,A,c,p,n):
    out=[[0,0] for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            z=v[j]
            for a in range(2):
                out[i][a]=(out[i][a]+c[i-j]*sum(A[a][b]*z[b] for b in range(2)))%p
    return out

def rank(rows,p):
    if not rows: return 0
    A=[list(r) for r in rows]; r=0
    for j in range(len(A[0])):
        k=next((k for k in range(r,len(A)) if A[k][j]%p),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]; c=pow(A[r][j],-1,p)
        A[r]=[(x*c)%p for x in A[r]]
        for k in range(len(A)):
            if k!=r:
                c=A[k][j]; A[k]=[(x-c*y)%p for x,y in zip(A[k],A[r])]
        r+=1
        if r==len(A): break
    return r

for p in (5,7,11,17,19):
    for n in (2,3,4):
        for x,y in itertools.product(range(p),repeat=2):
            check('exponential_character',mul(expcoef(x,p,n),expcoef(y,p,n),p,n)==expcoef((x+y)%p,p,n))
        for _ in range(50):
            v=[[rng.randrange(p),rng.randrange(p)] for _ in range(n)]
            w=[[rng.randrange(p),rng.randrange(p)] for _ in range(n)]
            check('J_symmetry',pair(w,v,p,n)==((-1)**n*pair(v,w,p,n))%p)
            check('t_skew_adjoint',pair(ttimes(v),w,p,n)==(-pair(v,ttimes(w),p,n))%p)
            while True:
                A=[[rng.randrange(p) for _ in range(2)] for _ in range(2)]
                det=(A[0][0]*A[1][1]-A[0][1]*A[1][0])%p
                if det: break
            c=expcoef(rng.randrange(p),p,n)
            check('Galois_pairing_similitude',pair(act(v,A,c,p,n),act(w,A,c,p,n),p,n)==det*pair(v,w,p,n)%p)
    for n in (2,3,4,6,8):
        rows=[]
        for i in range(n):
            for j in range(i,n):
                A=[[0]*n for _ in range(n)]; A[i][j]=A[j][i]=1
                rows.append(A[0]+A[1])
        check('common_correction_codimension_one',rank(rows,p)==2*n-1)
        for _ in range(100):
            alpha=rng.randrange(p)
            O=[[rng.randrange(p) for _ in range(n)] for _ in range(2)]
            O[0][0]=O[1][1]=0; O[0][1]=alpha; O[1][0]=-alpha%p
            eta=[[0]*n for _ in range(n)]
            for i in range(2):
                for j in range(n): eta[i][j]=eta[j][i]=-O[i][j]%p
            works=all((eta[i][j]+O[i][j])%p==0 for i in range(2) for j in range(n))
            check('same_eta_iff_alpha_zero',works==(alpha==0))
            # B=diag(0,0,1,...,1). First-lift changes can cancel all
            # columns beyond W, but cannot alter the W block.
            corrected=[r[:] for r in O]
            for i in range(2):
                for j in range(2,n): corrected[i][j]=0
            check('eta_zero_with_radical_W',all(x%p==0 for row in corrected for x in row)==(alpha==0))
    for a in range(p):
        # pi=u+u^2/2; (1+pi)^a equals exp(a u) mod u^3.
        pi=[0,1,pow(2,-1,p)]
        got=power([1,pi[1],pi[2]],a,p,3)
        check('cyclotomic_jet_matches',got==expcoef(a,p,3))
    poly=[math.comb(p,i+1) for i in range(p)]
    check('shifted_cyclotomic_Eisenstein',poly[-1]==1 and poly[0]==p and all(x%p==0 for x in poly[:-1]))

# A separate exhaustive 2-by-2 search checks that one symmetric correction
# cannot kill a nonzero alternating obstruction.
p=5
for alpha in range(p):
    solutions=0
    for a,b,c in itertools.product(range(p),repeat=3):
        if a==0 and c==0 and (b+alpha)%p==0 and (b-alpha)%p==0: solutions+=1
    check('exhaustive_shared_correction',bool(solutions)==(alpha==0))

for p,q in ((5,11),(5,101),(7,29),(7,197),(11,23),(11,727)):
    assert all(q%d for d in range(2,math.isqrt(q)+1))
    m=q-1; a=0
    while m%p==0: a+=1; m//=p
    n=p**a+1
    for _ in range(5):
        c=rng.randrange(1,p)
        u=[1,c]+[rng.randrange(p) for _ in range(n-2)]
        value=power(u,q-1,p,n)
        check('tame_formal_failure',value[0]==1 and all(x==0 for x in value[1:-1]) and value[-1]==m*pow(c,p**a,p)%p and value[-1]!=0)

# Honest control, not an arithmetic realization: t B+t^2 C has the
# required adjoint symmetry but can obstruct the two special directions.
for p in (5,7,11):
    B=[[0]*4 for _ in range(4)]; B[2][2]=B[3][3]=1
    C=[[0]*4 for _ in range(4)]; C[0][1]=1; C[1][0]=-1%p
    check('formal_countercontrol_symmetry',all(B[i][j]==B[j][i] and (C[i][j]+C[j][i])%p==0 for i in range(4) for j in range(4)))
    check('formal_countercontrol_nonlift',C[0][1]!=C[1][0])

out={'status':'PASS','scope':'Exact algebra and character controls only; no seed alpha_lambda or Selmer group calculated','counts':counts,'total_assertions':sum(counts.values()),'random_seed':20261006}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
