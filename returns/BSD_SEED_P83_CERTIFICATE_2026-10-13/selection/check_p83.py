#!/usr/bin/env python3
"""Small independent point-count/theorem gate. Does not compute the witness."""
import json, math
from pathlib import Path

def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))

def count(q):
    squares={y*y%q for y in range(q)}
    n=1
    for x in range(q):
        rhs=(x**3-22735*x*x+106272484*x)%q
        n += 1 if rhs==0 else 2 if rhs in squares else 0
    # Distinct implementation: direct (x,y) pair enumeration.
    direct=1+sum((y*y-x**3+22735*x*x-106272484*x)%q==0
                 for x in range(q) for y in range(q))
    assert n==direct
    return n

N=6503188012738584
p,ell=83,167
np,nl=count(p),count(ell)
g=next(g for g in range(2,ell) if len({pow(g,i,ell) for i in range(ell-1)})==ell-1)
assert prime(p) and prime(ell)
assert math.gcd(p,6*N*16*np)==1
assert math.gcd(ell,p*N)==1
assert (ell-1)%p==0 and (ell-1)%(p*p)!=0
assert nl%p!=0
out={
  'status':'LOCAL_ADMISSIBILITY_PASS_RETAINED_GLOBAL_INPUTS_REQUIRED',
  'p':p,'ell':ell,'N':N,'p_prime':prime(p),'ell_prime':prime(ell),
  'point_count_p':np,'trace_p':p+1-np,'ordinary':(p+1-np)%p!=0,
  'point_count_ell':nl,'trace_ell':ell+1-nl,
  'p_torsion_at_ell':'zero; order prime to p',
  'vp_ell_minus_one':1,'smallest_primitive_root':g,
  'gcd_p_6N_Tam_EFp':math.gcd(p,6*N*16*np),
  'symbol_denominator':1024,'symbol_denominator_mod_p':1024%p,
  'c2':'NOT_COMPUTED','Sha83':'NOT_DEDUCED',
  'retained_inputs':['rank two','non-CM','full 83-adic image',
                     'Tamagawa product16','pipeline period and lattice authentication']
}
print(json.dumps(out,sort_keys=True,indent=2))
