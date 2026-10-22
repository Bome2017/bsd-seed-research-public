#!/usr/bin/env python3
"""Separate coarse rational certification of the same five-length threshold."""
import json
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path

root=Path(__file__).resolve().parent
data=json.loads((root.parent/'theory/FIELD_INPUTS.json').read_text())
DA,DK,delta=map(int,(data['D_A'],data['D_Aplus'],data['norm_relative_discriminant']))
assert DA==DK*DK*delta and delta==2**4*5*4547**6
Q=DK*delta

# Positive exponential series gives a lower bound; a geometric estimate bounds
# the tail after term8. These certify both decimal rational constants exactly.
s8=sum((F(1,factorial(k)) for k in range(9)),F(0))
e_lower=F(1359,500)
e_tight_upper=F(271829,100000)
assert s8>e_lower
assert s8+F(10,9*factorial(9))<e_tight_upper
assert e_tight_upper<F(68,25)

# log(delta)>54.9 and log(Q)<273, using rational integer powers only.
assert delta**10>e_tight_upper**549
assert Q<e_lower**273
# exp(.694)>2, so log(2)<.694.
x=F(347,500)
assert sum((x**k/factorial(k) for k in range(9)),F(0))>2
sqrt5_upper=F(2237,1000)
assert sqrt5_upper**2>5
assert (F(549,10)-24*x)/(2*sqrt5_upper)>F(17,2)

# Machin identity and alternating-series bounds prove pi>3.14.
pi_lower=F(157,50)
assert 16*(F(1,5)-F(1,3*5**3))-F(4,239)>pi_lower
sqrtQ_upper=isqrt(Q)+1
assert sqrtQ_upper**2>Q

reg_lower=pi_lower**3*F(17,2)**6/768
L_upper=2*(F(68,25)*273/24)**12
bound=sqrtQ_upper*L_upper/((2*pi_lower)**6*reg_lower)
coarse=280*10**66
assert bound<coarse<5**98
assert bound>5**97
out={
 'status':'INDEPENDENT_EXACT_COARSE_FIVE_LENGTH_BOUND_PASS',
 'relative_regulator_ratio_lower':{'numerator':str(reg_lower.numerator),'denominator':str(reg_lower.denominator)},
 'relative_class_order_bound_independent_integer':str(coarse),
 'five_power_98':str(5**98),
 'five_primary_length_upper':97,
 'sum_faithful_five_ranks_upper':97,
 'method':'Independent coarse rational constants, exponential series and integer powers; no floating-point or original interval routine',
 'scope':'Numerical certification conditional on the written analytic and unit-index argument; no GRH or elliptic Sha input',
}
print(json.dumps(out,indent=2,sort_keys=True))
