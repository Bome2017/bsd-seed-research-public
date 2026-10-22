#!/usr/bin/env python3
"""Separate exact rational check with coarser constants and fixed radius."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json
R=Path(__file__).resolve().parent

def exp_upper(x,terms=30):
 assert 0<x<1
 partial=sum((x**k/Q(factorial(k)) for k in range(terms)),Q(0))
 first=x**terms/Q(factorial(terms))
 ratio=x/Q(terms+1)
 return partial+first/(1-ratio)
def sinh_upper(x):
 # Direct odd positive series; no cosh(sqrt(z)) identity used.
 terms=16
 partial=sum((x**(2*k+1)/Q(factorial(2*k+1)) for k in range(terms)),Q(0))
 first=x**(2*terms+1)/Q(factorial(2*terms+1))
 ratio=x*x/Q((2*terms+2)*(2*terms+3))
 return partial+first/(1-ratio)
def cosh_upper(x):
 terms=16
 partial=sum((x**(2*k)/Q(factorial(2*k)) for k in range(terms)),Q(0))
 first=x**(2*terms)/Q(factorial(2*terms))
 ratio=x*x/Q((2*terms+1)*(2*terms+2))
 return partial+first/(1-ratio)

delta=2**4*5*4547**6
radius=Q(41,100)
sqrt2upper=Q(141422,100000)
assert sqrt2upper**2>2
sep=2**24*7**20*sinh_upper(sqrt2upper*radius)**4*cosh_upper(radius)**16
assert sep<delta
# Recompute the retained analytic product before using the coarse integer.
a=json.loads((R.parent/'theory/RETAINED_ANALYTIC_INPUT.json').read_text())
pl=a['pi_interval'][0]
pi_input=Q(int(pl['numerator']),int(pl['denominator']))
can=Q(int(a['sqrtQ_upper_integer'])*int(a['L_value_upper_ceiling']))/(2*pi_input)**6
C=42*10**71
assert can<C
pi_lower=Q(314159,100000)
v6=pi_lower**3/6
bound=4*C/(2*v6*radius**6)
ceil=-(-bound.numerator//bound.denominator)
assert ceil<5**107
# Each ball radius .41 injects because2radius < old shortestunit lower8.
assert 2*radius<8
# Check every submitted radius with direct sinh/cosh series, not the producer's cosh-of-square implementation.
producer=json.loads((R.parent/'theory/PRIMARY_PACKING_RESULT.json').read_text())
sq2=Q(141421356237309504881,10**20)
assert sq2*sq2>2
for row in producer['all_prefixes']:
 rr=Q(*map(int,row['radius_lower'])); xx=row['max_norm']
 sep2=2**24*xx**20*sinh_upper(sq2*rr)**4*cosh_upper(rr)**16
 assert sep2<delta
 safe=4*can/(row['pairs']*(pi_input**3/6)*rr**6)
 assert -(-safe.numerator//safe.denominator)==int(row['torsion_order_upper_integer'])

out={'status':'PASS','submitted_prefix_radii_checked':len(producer['all_prefixes']),'fixed_radius':'41/100','split_pairs':2,'separation_ratio_upper_ceiling_1e9':-(-(sep/delta*10**9).numerator//(sep/delta*10**9).denominator),'analytic_product_upper':str(C),'torsion_order_upper_integer':str(ceil),'five_torsion_rank_upper':106,'weaker_than_retained_97':True,'independent_implementation':'direct sinh/cosh rational Taylor bounds, coarser C and pi, fixed radius; no import of producer code'}
(R/'INDEPENDENT_PRIMARY_PACKING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
