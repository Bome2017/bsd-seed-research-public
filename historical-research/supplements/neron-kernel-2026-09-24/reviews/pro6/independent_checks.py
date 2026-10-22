#!/usr/bin/env python3
"""Small exact checks for the b358f75 Neron-normalization/denominator review.

No network, no floating arithmetic, and no imports from the author's Gauss script.
The curve, theta transformation, CNS and period-comparison theorems remain
mathematical inputs: these tests do not formally verify those theories.
Run: python3 independent_checks.py [--output results.json]
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import gcd, isqrt
import json
import random
import time
from pathlib import Path

N = 2**3 * 3 * 2243 * 4547**2 * 5843
B_THETA = 2**10 * 4547
B_JOIN = 2**17 * 4547


def add_pair_histogram(m: int, fn) -> list[int]:
    out = [0] * m
    for x in range(m):
        for y in range(m):
            out[fn(x, y) % m] += 1
    return out


def cyclic_product(a: list[int], b: list[int]) -> list[int]:
    m = len(a)
    out = [0] * m
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i+j) % m] += x*y
    return out


def zero_at_primitive_prime_power(poly: list[int], p: int, e: int) -> bool:
    """Exact divisibility by Phi_(p^e), for degree < p^e.

Phi_(p^e)(X)=1+X^s+...+X^((p-1)s), s=p^(e-1).
Such a polynomial is a multiple iff its coefficients in each column r+j*s
are equal. This criterion avoids numerical complex roots of unity.
"""
    s = p**(e-1)
    assert len(poly) == p*s
    return all(all(poly[r+j*s] == poly[r] for j in range(p))
               for r in range(s))


def gauss_polynomial(p: int, n: int, e: int, a: int, u: int,
                     v: int, ell: tuple[int, int, int, int]) -> list[int]:
    """The defining four-variable sum via two exact two-variable histograms.

The full exponent is vu[a(r1*r4-p^n*r2*r3)+l1*r4+l4*r1-l2*r3-l3*r2].
No support or completed-square simplification is used to form the histogram.
"""
    m = p**e
    l1, l2, l3, l4 = ell
    h14 = add_pair_histogram(m, lambda r1,r4: v*u*(a*r1*r4+l1*r4+l4*r1))
    h23 = add_pair_histogram(m, lambda r2,r3: v*u*(-a*p**n*r2*r3-l2*r3-l3*r2))
    out = cyclic_product(h14, h23)
    assert sum(out) == m**4
    return out


def gauss_test() -> dict:
    rng = random.Random(4547)
    # Four odd-prime blocks have the author's trial counts. Three dyadic blocks
    # additionally exercise the sharper 2-local bound, all in exact arithmetic.
    specs = [(5,2,1,60),(7,2,1,60),(11,2,1,40),(5,2,2,6),
             (2,3,1,32),(2,3,2,32),(2,3,3,32)]
    ncases = 0
    for p,n,e,trials in specs:
        m = p**e
        units = [j for j in range(1,m) if j % p]
        for _ in range(trials):
            a,u,v = (rng.choice(units) for _ in range(3))
            if rng.randrange(2) == 0:
                ell=(rng.randrange(m), m*rng.randrange(3), m*rng.randrange(3), rng.randrange(m))
            else:
                ell=tuple(rng.randrange(m) for _ in range(4))
            poly = gauss_polynomial(p,n,e,a,u,v,ell)
            if ell[1] % m == 0 and ell[2] % m == 0:
                power = (-u*v*ell[0]*ell[3]*pow(a,-1,m)) % m
                poly[power] -= p**(3*e)
            assert zero_at_primitive_prime_power(poly,p,e), (p,n,e,a,u,v,ell)
            ncases += 1
    # Deliberately reverse a genuinely nonreal phase or change its amplitude.
    p,n,e=5,2,2
    m=p**e
    poly=gauss_polynomial(p,n,e,1,1,1,(1,0,0,1))
    wrong_phase=poly.copy(); wrong_phase[1]-=p**(3*e)
    assert not zero_at_primitive_prime_power(wrong_phase,p,e)
    wrong_amp=poly.copy(); wrong_amp[-1]-=p**(2*e)
    assert not zero_at_primitive_prime_power(wrong_amp,p,e)
    return {'exact_cases':ncases,'dyadic_cases':96,
            'odd_prime_cases':166,'negative_controls_rejected':2,
            'method':'integer polynomials modulo prime-power cyclotomic polynomials',
            'finite_check_scope':'Eichler local sums only; division-place import retained'}


def cns_required(p: int, n: int, e: int) -> F:
    if e==0: return F(-n)
    if e==n: return F(0)
    return F(e-n)+F(1,p-1)


def thresholds() -> list[dict]:
    rows=[]
    for p,n,t in [(2,3,1),(3,1,0),(2243,1,0),(4547,2,1),(5843,1,0)]:
        for e in range(n+1):
            lower=F(e-n)
            target=cns_required(p,n,e)
            assert lower+t>=target
            rows.append({'prime':p,'level_exponent':n,'cusp_exponent':e,
                         'theta_bound':str(lower),'multiplier_exponent':t,
                         'CNS_threshold':str(target),'margin':str(lower+t-target)})
    return rows


def ceilq(x:F)->int:
    return -((-x.numerator)//x.denominator)


def interval_decision(lo:F,hi:F,p:int,B:int=B_THETA)->dict:
    """Arithmetic only, CONDITIONAL on the proved B*lattice membership.

An EMPTY_LATTICE result is an inconsistency, never a positive witness.
A positive result becomes a Sha consequence only after all theorem inputs,
prime admissibility, and actual seed interval are separately certified.
"""
    if lo>hi:raise ValueError('reversed interval')
    if p<5 or p%2==0 or any(p%d==0 for d in range(3,isqrt(p)+1,2)) or gcd(7*N,p)!=1 or gcd(B,p)!=1:
        raise ValueError('outside requested good-prime arithmetic scope')
    low,high=ceilq(B*lo),(B*hi).numerator//(B*hi).denominator
    if low>high: return {'status':'EMPTY_LATTICE_INCONSISTENCY'}
    if ceilq(F(low,p)) > high//p:
        return {'status':'UNIT_WITNESS_IF_MEMBERSHIP','integer_range':[low,high]}
    if low==high:
        return {'status':'DIVISIBLE_WITNESS_INCONCLUSIVE_FOR_SHA','integer':low}
    return {'status':'INCONCLUSIVE','integer_range':[low,high]}


def arithmetic_checks() -> dict:
    assert N==6503188012738584
    assert (B_THETA,B_JOIN)==(4656128,595984384)
    assert B_JOIN==128*B_THETA
    assert F('0.000000107') < F(1,2*B_THETA)
    # The rounded upper decimal is not a safe literal stopping threshold.
    assert F('0.000000000839') > F(1,2*B_JOIN)
    B=B_THETA;p=5
    assert interval_decision(F(3,4*B),F(5,4*B),p)['status'].startswith('UNIT')
    assert interval_decision(F(19,4*B),F(21,4*B),p)['status'].startswith('DIVISIBLE')
    assert interval_decision(F(1,B),F(4,B),p)['status'].startswith('UNIT')
    assert interval_decision(F(4,B),F(6,B),p)['status']=='INCONCLUSIVE'
    assert interval_decision(F(1,4*B),F(1,2*B),p)['status'].startswith('EMPTY')
    # Exact degree-zero relifting of arbitrary squared weights preserves reduction.
    for p in [5,7,11,13,17,23,29,31,43]:
        w=[(j*j+p//2)%p-p//2 for j in range(p)]
        assert sum(w)%p==0
        d=sum(w)
        w[0]-=d
        assert sum(w)==0 and all((w[j]-j*j)%p==0 for j in range(p))
    return {'seed_N':N,'B_theta':B_THETA,'B_join':B_JOIN,
            'exact_radius_theta':str(F(1,2*B_THETA)),
            'exact_radius_join':str(F(1,2*B_JOIN)),
            'rounded_8_39e_minus10_is_too_large':True,
            'interval_controls':5,'degree_zero_relift_primes':9,
            'actual_seed_witness_evaluated':False}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path); args=ap.parse_args()
    start=time.process_time()
    result={'gauss_sums':gauss_test(),'cusp_inequalities':thresholds(),
            'arithmetic':arithmetic_checks(),'no_new_seed_value':True}
    result['cpu_seconds']=time.process_time()-start
    text=json.dumps(result,indent=2)+'\n'
    if args.output: args.output.write_text(text)
    print(text)

if __name__=='__main__':main()
