#!/usr/bin/env python3
"""Exact local-module tests. Toy divisor assignments are NOT modular symbols."""
from __future__ import annotations
import json, random
from pathlib import Path
from fractions import Fraction
from math import comb
from jet_module import COORDS, NODES, JetModule, moments, transformed_moments, multiply, four_functional, principal_log


def determinant(a):
    a=[[Fraction(v) for v in row] for row in a]; d=Fraction(1); n=len(a)
    for j in range(n):
        r=next(i for i in range(j,n) if a[i][j])
        if r!=j:a[j],a[r]=a[r],a[j];d=-d
        pivot=a[j][j];d*=pivot
        for i in range(j+1,n):
            ratio=a[i][j]/pivot
            for k in range(j,n):a[i][k]-=ratio*a[j][k]
    assert d.denominator==1
    return int(d)


def independent_specialization(p,w,s,X,z):
    """Direct integer-character evaluation on assigned Dirac measures."""
    mod=p**4
    return ((-1)**s*sum(pow(pow(a,p**4,mod),-s,mod)*pow(a-p*z[a],s,mod)
                        *pow(1+p,w*X[a],mod) for a in range(1,p)))%mod


def seed_count(p):
    # Minimal model [0,-1,0,-66020924,-65074271436], exact exhaustive count.
    squares={y*y%p:0 for y in range(p)}
    for y in range(p):squares[y*y%p]+=1
    n=1+sum(squares.get((x*x*x-x*x-66020924*x-65074271436)%p,0) for x in range(p))
    ap=p+1-n
    root=ap%p
    if root==0:return {'p':p,'points':n,'a_p':ap,'ordinary':False}
    for k in range(1,4):
        root=(root-(root*root-ap*root+p)*pow(2*root-ap,-1,p**(k+1)))%p**(k+1)
    assert (root*root-ap*root+p)%p**4==0
    return {'p':p,'points':n,'a_p':ap,'ordinary':True,'unit_root_mod_p4':root,'modulus':p**4,
            'does_not_check_Hida_exceptional_domain':True}


def run():
    rng=random.Random(20261006); counts={}; details=[]
    def check(name, condition):
        if not condition:raise AssertionError(name)
        counts[name]=counts.get(name,0)+1
    raw=[[comb(x,i)*z**j if x>=i else 0 for i,j in COORDS] for x,z in NODES]
    det=determinant(raw);check('integral_interpolation_determinant_24',det==24)
    for p in (17,19,23,31,73,107):
        M=JetModule(p)
        gs=[(1,1,0,1),(1,0,p,1),(2,3,p,2*p+1),(1,5,0,p),(1+p,0,0,1+p),(-1,2,p,1)]
        for _ in range(14):
            a=rng.randrange(1,p**2)
            while a%p==0:a=rng.randrange(1,p**2)
            g=(a,rng.randrange(-p**2,p**2),p*rng.randrange(-p,p),rng.randrange(-p**2,p**2))
            if g[0]*g[3]-g[1]*g[2]!=0:gs.append(g)
        actions=[M.action(g) for g in gs]
        for g,A in zip(gs,actions):
            for _ in range(16):
                X,z=(rng.randrange(p**5) for _ in range(2))
                check('action_matches_dirac_evaluation',M.apply(A,moments(X,z,p))==transformed_moments(X,z,g,p))
            for _ in range(3):
                m=[rng.randrange(mo) for mo in M.precisions]
                mlift=[x+rng.randrange(-9,10)*mo for x,mo in zip(m,M.precisions)]
                check('independent_slot_lift_invariance',M.apply(A,m)==M.apply(A,mlift))
        for _ in range(40):
            r,t=rng.randrange(len(gs)),rng.randrange(len(gs))
            g,h=gs[r],gs[t]
            m=[rng.randrange(mo) for mo in M.precisions]
            # Right point action: first g, then h.
            check('semigroup_law_on_arbitrary_local_arrays',M.apply(actions[t],M.apply(actions[r],m))==M.apply(M.action(multiply(g,h)),m))
        center=M.action((1+p,0,0,1+p))
        for _ in range(8):
            m=[rng.randrange(mo) for mo in M.precisions]
            expected=[(m[k]+(m[COORDS.index((i-1,j))] if i else 0))%M.precisions[k] for k,(i,j) in enumerate(COORDS)]
            check('central_weight_shift',M.apply(center,m)==expected)
        X={a:a+2 for a in range(1,p)};z={a:a*a+1 for a in range(1,p)}
        source={a:moments(X[a],z[a],p) for a in range(1,p)}
        vals={}
        for w,s in ((3,2),(3,3),(4,3),(4,4)):
            v=four_functional(p,w,s,source);vals[f'{w},{s}']=v
            check('functional_matches_independent_character_evaluation',v==independent_specialization(p,w,s,X,z))
            lifted={a:[v+rng.randrange(-4,5)*mod for v,mod in zip(mm,M.precisions)] for a,mm in source.items()}
            check('functional_mixed_precision_invariance',v==four_functional(p,w,s,lifted))
        # A valuation-three contribution must not be discarded as zero.
        v3source={a:[0]*10 for a in range(1,p)}
        v3source[1][COORDS.index((3,0))]=1
        v=four_functional(p,3,2,v3source)
        check('valuation_three_retained',v%p**3==0 and v%p**4!=0)
        # A nonzero local source can have all four functionals zero. This is
        # an adversarial control against mistaking local primitivity for BSD.
        zerofour={a:[0]*10 for a in range(1,p)}
        zerofour[1][COORDS.index((3,0))]=1
        zerofour[2][COORDS.index((3,0))]=p-1
        check('nonzero_local_array_all_four_values_zero',
              all(four_functional(p,w,s,zerofour)==0 for w,s in ((3,2),(3,3),(4,3),(4,4))))
        # Changing t_w to t_w/p would already change this simple cubic input.
        t=((1+p)**3-1)
        check('wrong_weight_rescaling_detected',v!=(t//p)**3%(p**4))
        for u in (2,3,7,1+p,p*p+2):
            k=principal_log(u,p,4)
            check('principal_log_independent_power_identity',pow(1+p,(p-1)*k,p**5)==pow(u,p-1,p**5))
        details.append({'p':p,'local_action_matrices':len(gs),'toy_dirac_functionals':vals,
                        'toy_assignments_are_not_global_symbols':True})
    for p in (2,3,5,11,15,21):
        try:JetModule(p)
        except ValueError:check('out_of_scope_prime_rejected',True)
        else:raise AssertionError('out-of-scope p accepted')
    result={'status':'EXACT_LOCAL_TESTS_PASS','counts':counts,'total_checks':sum(counts.values()),
            'interpolation_determinant':det,'moment_slots':10,'base_p_digits_per_divisor':20,
            'test_details':details,'seed_local_checks':[seed_count(p) for p in (17,31)],
            'seed_global_symbol_computed':False,'seed_W3_values_computed':False,
            'new_primary_certificate':False,'uniform_bound_proved':False,'lean_replay_performed':False}
    return result

if __name__=='__main__':
    result=run();out=Path(__file__).with_name('TEST_RESULTS.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'total_checks':result['total_checks'],
                      'seed_local_checks':result['seed_local_checks'],'report':out.name},indent=2))
