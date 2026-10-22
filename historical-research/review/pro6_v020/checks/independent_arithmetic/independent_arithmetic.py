#!/usr/bin/env python3
"""Fresh standard-library exact checks; no project module imports.
This does not replay the bulk L-series or saturation computations.
"""
from fractions import Fraction as F
from math import isqrt, prod
from decimal import Decimal, localcontext
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def trace(p,a2=-22735,a4=106272484):
    # Count solutions through an independently constructed square-root multiplicity table.
    roots=[0]*p
    for y in range(p): roots[y*y%p]+=1
    return p-sum(roots[(x*x*x+a2*x*x+a4*x)%p] for x in range(p))

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and y==-v:return None
    m=(3*x*x-45470*x+106272484)/(2*y) if P==Q else (v-y)/(u-x)
    xx=m*m+22735-x-u
    return xx,-y+m*(x-xx)

m,n=2243,12
ps=[m,m+16*n*n,m+25*n*n]
assert ps==[2243,4547,5843] and all(prime(p) and p%24==11 for p in ps)
a2=-5*ps[1]; a4=4*ps[1]*ps[2]
assert (a2,a4)==(-22735,106272484)
b2=4*a2; b4=2*a4; b6=0; b8=-a4*a4
c4=b2*b2-24*b4; c6=-b2**3+36*b2*b4
Delta=-b2*b2*b8-8*b4**3
assert (c4,c6,Delta)==(3169004368,56243184546880,16586638656786071143743744)
assert Delta==2**8*3**2*2243*4547**3*5843**2
N=2**3*3*2243*4547**2*5843
assert N==6503188012738584
P=(F(4547),F(327384));Q=(F(5184),F(281520));T=(F(0),F(0))
for x,y in [P,Q,T]:assert y*y==x*x*x+a2*x*x+a4*x
assert add(add((P[0],-P[1]),(Q[0],-Q[1])),T)==(5843,210348)
traces={p:trace(p) for p in [5,7,11,13,17,4099]}
assert traces=={5:-2,7:-2,11:-2,13:-4,17:-6,4099:86}
assert trace(4547,0,-1)==0
witnesses=[(5,[3,7,11,19,43,67,163]),(7,[13,17,37]),(17,[5])]
for q,ells in witnesses:
    for ell in ells:
        assert pow((traces[q]**2-4*q)%ell,(ell-1)//2,ell)==ell-1
# Recover the certificate's actual Arb radius exactly from its hexadecimal dump.
mid=int('8fbdc2e36e453517571bc5e5f9400837',16)*F(2)**(-int('7a',16))
rad=int('17625463',16)*F(2)**(-int('24',16))
paper_rad=F('0.005709')
assert rad>paper_rad
assert F('35.929604')<=mid-rad and mid+rad<=F('35.941023')
# An outward-rounded replacement radius for the printed midpoint.
printed_mid=F('35.93531375275170089')
assert abs(mid-printed_mid)+rad<F('0.00570901')
with localcontext() as c:
    c.prec=60
    fmt=lambda x:str(Decimal(x.numerator)/Decimal(x.denominator))
    dump={'midpoint':fmt(mid),'radius':fmt(rad),'paper_radius':fmt(paper_rad),'certified_lower':fmt(mid-rad),'certified_upper':fmt(mid+rad),'safe_replacement_radius':'0.00570901'}
report={'zywina_primes':ps,'family_matches':True,'invariants':{'c4':c4,'c6':c6,'Delta':Delta,'N':N},'point_relation':True,'traces':traces,'j1728_trace_at_4547':0,'frobenius_witnesses_pass':True,'arb_dump_exact_check':dump,'main_L2_interval_contains_dump':True,'scope':'No Tate algorithm, full saturation, original L-series, Selmer computation, or full modular-curve geometry replay.'}
(OUT/'independent_arithmetic.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
