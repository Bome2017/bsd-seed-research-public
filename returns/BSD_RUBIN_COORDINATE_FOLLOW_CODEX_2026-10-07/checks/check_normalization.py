"""Exact scalar controls; not a proof of image-lattice or Kato primitivity claims."""
from fractions import Fraction as F
import math, json
N=2**3*3*2243*4547**2*5843
cN=(1+F(1,3))*(1-F(1,2243))*(1+F(1,5843))
assert cN==F(17469664,13105849)
c,d=1+6*N,1+12*N
assert math.gcd(c,6*N)==math.gcd(d,6*N)==math.gcd(c,d)==1
assert (c-1)%N==(d-1)%N==0
for p in [5,7,11,17]:
    for a in [F(2),F(3),F(7,2)]:
        b=F(p)/a
        if a==1 or b==1: continue
        assert (1-1/a)/(1-1/b)*(1-1/a)*(1-1/b)==(1-1/a)**2
print(json.dumps({'N':N,'bad_euler_augmentation':str(cN),
 'fixed_smoothing_c':c,'fixed_smoothing_d':d,
 'fixed_smoothing_valid_away_from_its_support':True,
 'pointwise_lattice_indices_computed':False,
 'interpolation_factor_controls':'PASS','sha_bound_proved':False},indent=2))
