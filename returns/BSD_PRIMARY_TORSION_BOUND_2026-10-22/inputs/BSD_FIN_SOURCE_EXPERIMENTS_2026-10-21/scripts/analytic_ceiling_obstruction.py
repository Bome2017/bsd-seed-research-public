#!/usr/bin/env python3
"""Check exact constants in a lower bound on the existing UPPER-BOUND EXPRESSION.
Nothing in this script lower-bounds a true class group or Sha.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json
R=Path(__file__).resolve().parents[1]
# e<11/4 from positive series with an outward geometric tail.
e_upper=sum((Q(1,factorial(k)) for k in range(10)),Q(0))+Q(1,factorial(10))*Q(11,10)
assert Q(2)<e_upper<Q(11,4)
# e>2 follows already from the terms 1+1+1/2, without a numerical approximation.
assert Q(5,2)>2
assert Q(11,4)**8<4547   # hence log(4547)>8
assert Q(4547,4)>1000

def floor_log_int(a,p):
    lo,hi=0,a.bit_length()
    while lo+1<hi:
        m=(lo+hi)//2
        if pow(p,m)<=a: lo=m
        else: hi=m
    assert p**lo<=a<p**(lo+1)
    return lo
rows=[]
for p in [5,7,11,13,17,23,31,53,83,101]:
    n=p*p-1;d=n//4
    assert n%8==0 and d>=p
    assert p**4<1000**d
    f=floor_log_int(1000**d,p)
    rows.append({'p':p,'d_relative_unit_rank':d,
      'lower_bound_on_log_floor_of_bound_expression':f,
      'faithful_unit_dimension':(p+1)//2,
      'NOTE':'Not a lower bound on the actual class length. It limits the strength of this particular estimate.'})
result={'status':'PASS_EXACT_CONSTANT_AND_THRESHOLD_CHECKS',
 'expression_obstruction':'B_p > 1000^((p^2-1)/4) > p^4',
 'e_upper':str(e_upper),'eleven_over_four_power8':str(Q(11,4)**8),
 'rows':rows,
 'scope':'The October 20 expression (G), using its own shortest-vector regulator bound. Additional class-map constraints or stronger analytic input are not excluded.'}
(R/'results/ANALYTIC_OBSTRUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
