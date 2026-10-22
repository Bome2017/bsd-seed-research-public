#!/usr/bin/env python3
"""Independent finite-algebra checks. No number-field ideal or Selmer computation."""
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def rank_mod(rows,p):
    a=[[x%p for x in row] for row in rows]
    m=len(a); n=len(a[0]); pivot=0
    for col in range(n):
        hit=next((i for i in range(pivot,m) if a[i][col]),None)
        if hit is None:continue
        a[pivot],a[hit]=a[hit],a[pivot]
        inv=pow(a[pivot][col],-1,p)
        a[pivot]=[(x*inv)%p for x in a[pivot]]
        for i in range(m):
            if i==pivot:continue
            factor=a[i][col]
            a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==m:break
    return pivot

results=[]
for p in [3,5,7,11,13]:
    mod=p*p
    reps=[(1,a) for a in range(p)]+[(0,1)]
    omega=[0]+[pow(a,p,mod) for a in range(1,p)]
    assert all(pow(omega[a],p-1,mod)==1 for a in range(1,p))
    N=[[[0]*len(reps) for _ in reps] for _ in range(p)]
    for i,lam in enumerate(reps):
        for j,v in enumerate(reps):
            dot=(lam[0]*v[0]+lam[1]*v[1])%p
            for scale in range(1,p):
                t=scale*dot%p
                N[t][i][j]=(N[t][i][j]+omega[scale])%mod
    assert all(x==0 for row in N[0] for x in row)
    for t in range(1,p):
        assert all(N[t][i][j]==omega[t]*N[1][i][j]%mod
                   for i in range(p+1) for j in range(p+1))
    rank=rank_mod(N[1],p)
    assert rank==p-1
    for k in [0,1]:
        f=[v[k] for v in reps]
        assert all(sum(a*b for a,b in zip(row,f))%p==0 for row in N[1])
    # Enumeration on all vectors and covectors checks all orbit cardinalities.
    X=[(a,b) for a in range(p) for b in range(p) if a or b]
    counts=[0]*p
    for lam in X:
        for v in X:counts[(lam[0]*v[0]+lam[1]*v[1])%p]+=1
    assert counts[0]==(p-1)*(p*p-1)
    assert counts[1:]==[p*(p*p-1)]*(p-1)
    results.append({'p':p,'modulus':mod,'operator_span_rank':1,
                    'N1_rank_mod_p':rank,'coordinate_kernel_dimension':2,
                    'orbit_sizes':counts})
# Literal projector identities for a, s, ta, ts are monomial identities.
monomial_checks=[]
for weights,root_t_exp in [([1,3,4,2],0),([1,2,4,3],1)]:
    exp_a=weights[0]+weights[2]; exp_s=weights[1]+weights[3]
    exp_t=weights[2]+weights[3]
    assert exp_a==5 and exp_s==5
    assert (exp_t-5*root_t_exp)%2==0
    monomial_checks.append({'weights':weights,'a_exponent':exp_a,'s_exponent':exp_s,
                            'sign_exponent':exp_t,'root_sign_exponent':root_t_exp})
# A surjection Z/p^2 -> Z/p need not surject on elements killed by p.
for p in [3,5,7,11,13]:
    p_torsion=[x for x in range(p*p) if p*x%(p*p)==0]
    assert {x%p for x in p_torsion}=={0}
# The published scaling constants are justified by integer comparisons.
assert 4547**9 > 1600**10
for p in [5,7,11,13,17,53,83,131]:
    d=(p*p-1)//4;m=(p*p-1)//2
    assert 2*400**d > m*p**4
out={'status':'PASS_FINITE_ALGEBRA', 'incidence_checks':results,
     'fifth_power_monomial_checks':monomial_checks,
     'integral_presentation_counterexample':'Z/p^2 onto Z/p induces zero on p-torsion for all five tested primes',
     'scaling_constant_integer_tests':'PASS',
     'scope':'Finite algebra and exact monomial identities. Actual seed field, ideals, and scalar action remain retained inputs.'}
(BASE/'ALGEBRA_CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
