#!/usr/bin/env python3
"""Exact arithmetic checks, NOT an autonomous Sha or main-conjecture verifier.

The p-adic coefficients, regulators, ranks, saturation and older seed Sha17
certificate are retained inputs identified in SOURCE_BINDINGS.json. This script
rechecks the small image-hypothesis witnesses, the Eisenstein local character,
and the integer valuation arithmetic in the written proof. Standard library only.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt
import json

CURVES = {
    '433a1': [1,0,0,0,1],
    '655a1': [0,0,1,-13,18],
    'seed': [0,-1,0,-66020924,-65074271436],
    'A': [0,0,1,-19766893413,-1937478573143510],
    'F': [0,0,1,-14959712463303,-22270654620235278500],
}

def require(test: bool, message: str) -> None:
    if not test:
        raise AssertionError(message)

def prime(n: int) -> bool:
    return type(n) is int and n >= 2 and all(n % d for d in range(2,isqrt(n)+1))

def vp(n: int, p: int) -> int:
    if type(n) is not int or n == 0 or not prime(p):
        raise ValueError('valuation requires a nonzero integer and a prime')
    n = abs(n); v = 0
    while n % p == 0:
        v += 1; n //= p
    return v

def residue_valuation(a: int, p: int, precision: int) -> int | None:
    if not prime(p) or type(precision) is not int or precision < 1 or type(a) is not int:
        raise ValueError('invalid residue data')
    r = a % (p**precision)
    return None if r == 0 else vp(r,p)

def invariants(a: list[int]) -> tuple[int,int]:
    a1,a2,a3,a4,a6 = a
    b2 = a1*a1+4*a2; b4 = a1*a3+2*a4; b6 = a3*a3+4*a6
    b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    return b2*b2-24*b4, -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6

def legendre(a: int,p: int) -> int:
    require(prime(p) and p%2==1,'Legendre prime')
    r = pow(a%p,(p-1)//2,p)
    return 0 if r==0 else (1 if r==1 else -1)

def cardinality_brute(a: list[int],q: int) -> int:
    a1,a2,a3,a4,a6 = a
    return 1+sum((y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6)%q==0
                 for x in range(q) for y in range(q))

def cardinality_discriminants(a: list[int],q: int) -> int:
    if q==2:
        # Count roots in each of the two x-fibres explicitly.
        a1,a2,a3,a4,a6=a
        return 1+sum(sum((y*y+(a1*x+a3)*y-(x**3+a2*x*x+a4*x+a6))%2==0
                         for y in (0,1)) for x in (0,1))
    a1,a2,a3,a4,a6=a
    return q+1+sum(legendre((a1*x+a3)**2+4*(x**3+a2*x*x+a4*x+a6),q)
                   for x in range(q))

def on_curve(a: list[int],P: tuple[Q,Q] | None) -> bool:
    if P is None: return True
    a1,a2,a3,a4,a6=a; x,y=P
    return y*y+a1*x*y+a3*y == x**3+a2*x*x+a4*x+a6

def add(a: list[int],P: tuple[Q,Q] | None,R: tuple[Q,Q] | None) -> tuple[Q,Q] | None:
    if P is None: return R
    if R is None: return P
    a1,a2,a3,a4,a6=a; x,y=P; z,w=R
    if x==z and y+w+a1*x+a3==0: return None
    if P==R:
        m=(3*x*x+2*a2*x+a4-a1*y)/(2*y+a1*x+a3)
    else:
        m=(w-y)/(z-x)
    b=y-m*x
    xx=m*m+a1*m-a2-x-z
    yy=-(m+a1)*xx-b-a3
    ans=(xx,yy)
    require(on_curve(a,ans),'addition left curve')
    return ans

def main() -> dict:
    # One unramified Frobenius with irreducible characteristic polynomial, and
    # a distinct multiplicative place of discriminant valuation one. The latter
    # supplies BCS condition (im) by the Tate-curve inertia representation.
    specs=[('655a1',7,2,131),('433a1',13,2,433),('655a1',31,2,131),
           ('433a1',7,3,433),('655a1',11,2,131),('seed',17,7,2243)]
    image=[]
    for name,p,q,tame in specs:
        a=CURVES[name]; c4,disc=invariants(a)
        require(prime(p) and prime(q) and prime(tame),'primality')
        require(disc%p and disc%q,'good primes')
        np=cardinality_discriminants(a,p); nq=cardinality_discriminants(a,q)
        require(np==cardinality_brute(a,p) and nq==cardinality_brute(a,q),'counts disagree')
        ap=p+1-np; aq=q+1-nq; dd=(aq*aq-4*q)%p
        require(ap%p!=0 and np%p!=0,'ordinary/nonanomalous check')
        require(legendre(dd,p)==-1,'irreducibility witness')
        require(vp(disc,tame)==1 and c4%tame!=0,'multiplicative index-one witness')
        image.append({'curve':name,'p':p,'a_p':ap,'number_of_points_mod_p':np,
                      'irreducibility_Frobenius_prime':q,'a_q':aq,
                      'Frobenius_discriminant_mod_p':dd,
                      'multiplicative_prime':tame,'v_tame_discriminant':1,
                      'im_input':'Tate inertia with a unit upper-right entry; written proof'})
    base=[0,-1,1,-10,-20]; P=(Q(5),Q(5)); R=None; pts=[]
    require(on_curve(base,P),'base point')
    for n in range(1,6):
        R=add(base,R,P)
        require((R is None)==(n==5),'base point exact order')
        pts.append(None if R is None else [str(R[0]),str(R[1])])
    d=43737
    require(d==3*61*239 and d%4==1 and all(prime(q) for q in (3,61,239)), 'fundamental discriminant')
    require(legendre(d,5)==-1,'local quadratic character')
    F=CURVES['F']; require(invariants(F)[1]%5!=0,'F good at 5'); fcount=cardinality_brute(F,5)
    require(fcount==cardinality_discriminants(F,5)==7,'F at 5')
    require(on_curve(F,(Q(6288329),Q(-11502941299))), 'Q1')
    require(on_curve(F,(Q(8502485),Q(21568458354))), 'Q2')
    # Only the leading precision needed for a valuation is transcribed.
    retained=[('655a1',7,4*7+2*7**2,3,2*7+3*7**2,3,2,1),
              ('433a1',13,3*13+10*13**2,3,13+7*13**2,3,1,1),
              ('655a1',31,13*31,2,27*31,2,2,1),
              ('F',5,4*5**2,3,4,1,4,1)]
    vals=[]
    for name,p,l2,kl,reg,kr,C,t in retained:
        vl=residue_valuation(l2,p,kl); vr=residue_valuation(reg,p,kr)
        require(vl is not None and vr is not None,'insufficient coefficient precision')
        ap=p+1-cardinality_discriminants(CURVES[name],p)
        alpha=ap%p
        epsilon=(1-pow(alpha,-1,p))**2%p
        require(epsilon!=0,'Euler factor is not a unit')
        s=vl-vr-vp(C,p)+2*vp(t,p)
        leading=(l2//p**vl)%p
        denominator=((reg//p**vr)%p)*epsilon*((C//p**vp(C,p))%p)%p
        u=leading*pow(denominator,-1,p)*pow((t//p**vp(t,p))%p,2,p)%p
        require(s in (0,2),'unexpected corrected valuation')
        require(u==1,'reported leading corrected unit')
        vals.append({'curve':name,'p':p,'v_L2':vl,'v_R_U':vr,
                     'v_Tamagawa':vp(C,p),'v_torsion':vp(t,p),
                     'Euler_factor_mod_p':epsilon,'corrected_valuation':s,
                     'leading_corrected_unit_mod_p':u,
                     'conditional_sha_order_from_written_theorem':p**s,
                     'numerator_and_regulator':'retained, not generated by this script'})
    boundary=[]
    for a,p,k,expected in [(0,5,3,None),(125,5,3,None),(100,5,3,2),(17,17,2,1)]:
        v=residue_valuation(a,p,k);require(v==expected,'precision boundary')
        boundary.append({'residue':a,'p':p,'precision':k,'exact_valuation':v})
    # Seed17: no numerator digit is supplied. This is arithmetic on the premises
    # of the reverse implication, not a new Sha17 proof or numerator evaluation.
    seed_r=1;seed_sha_length=0
    require(46298%17==7,'old tame witness scalar arithmetic only')
    return {'status':'PASS_ARITHMETIC_CHECKS_NOT_END_TO_END_CERTIFICATION',
            'image_hypothesis_checks':image,
            'Eisenstein_check':{'d':d,'d_mod_5':d%5,'chi_d_Frob_5':-1,
                                'base_point_order':5,'base_point_multiples':pts,
                                'F_a5':6-fcount,'characters':'chi_d and omega*chi_d; neither locally 1 or omega'},
            'retained_coefficient_comparisons':vals,'precision_boundaries':boundary,
            'seed17_reverse_inference':{'retained_sha17_length':seed_sha_length,
                                       'retained_regulator_valuation':seed_r,
                                       'deduced_L2_valuation':seed_r+seed_sha_length,
                                       'coefficient_residue_computed':False,
                                       'independent_new_sha17_certificate':False},
            'new_numerator_computations':0,'new_seed_primary_results':0,
            'full_seed_FIN':'OPEN','seed_ORDER9':'OPEN','seed_Q36':'OPEN',
            'retained_inputs_not_verified_by_this_script':['rank bounds','point saturation',
                'modular-symbol and height producer correctness','old Ota certificate',
                'global theorem proofs','all-prime seed residual-image theorem']}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
