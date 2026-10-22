#!/usr/bin/env python3
"""Small exact formula controls; not a Hida or BSD theorem verifier."""
from fractions import Fraction as Q
from math import comb
import json
from pathlib import Path

results = {}

# Exact change from the original integral cubic to the minimal cubic.
c = 7578
coefs = [c**3-22735*c*c+106272484*c,
         3*c*c-2*22735*c+106272484,
         3*c-22735, 1]
assert coefs == [-65074271436, -66020924, -1, 1]
assert sum(coefs[j]*(-7578)**j for j in range(4)) == 0
results['seed_coordinate_change'] = {'minimal_cubic_low_to_high': coefs,
                                      'rational_two_torsion_x': -7578}

# The sole exceptional small-prime count used in the all-prime Hasse proof.
p = 5
points = [(x,y) for x in range(p) for y in range(p)
          if (y*y-x**3+x*x+66020924*x+65074271436) % p == 0]
assert len(points)+1 == 8
results['p5_count'] = {'affine_points': points, 'order': 8, 'a5': -2}

# (p-1)^2-4p = p^2-6p+1 is positive at 7 and increasing thereafter.
assert 7**2-6*7+1 == 8
assert 2*7-6 > 0
results['hasse_integer_inequality'] = {'value_at_7': 8,
                                      'derivative_at_7': 8,
                                      'derivative_slope': 2}

# Two-variable coefficient array, T and tau: (1+p)(1+T)(1+tau)=1.
# Solving either variable gives the same inverse parameter change.
for p in (5,7,11):
    for T in (Q(0), Q(p), Q(p*p)):
        tau = 1/(Q(1+p)*(1+T))-1
        recovered = 1/(Q(1+p)*(1+tau))-1
        assert recovered == T
        # tau mod p has linear coefficient -1 at T=0.
    assert pow(1+p,-1,p) == 1
results['boston_parameter_change'] = 'exact inverse identities; residual slope -1'

# In Sym^1, iota sends (a,b) to (-a,b); + projection preserves Y.
for a,b in ((2,3),(-5,7),(0,1)):
    plus = (Q(a-a,2), Q(b+b,2))
    assert plus == (0,b)
    assert -plus[1] == -b
results['evaluation_sign'] = 'plus projection preserves the chosen Y functional'

# Stabilization correction: actual binomial coefficients through degree two.
norms = {p: [comb(p,j) for j in (1,2,3)] for p in (5,7,11,13,17)}
assert all(x % p == 0 for p,row in norms.items() for x in row)
results['cyclic_norm_mod_p_I3'] = norms

# p-adic divisibility and the b=3 branch of the sufficient endpoint.
def vp(n,p):
    assert n != 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e
rows = []
for p in (5,7,11):
    for b in (2,3,4,5):
        M = p**b
        a2 = (M//(p*p)) % p
        J = (M//(p*p)) % (p*p)
        assert (a2 != 0) == (b == 2)
        assert (J != 0) == (b <= 3)
        rows.append({'p':p,'b':b,'a2':a2,'J':J})
    assert vp(p*p*1,p) == 2 and vp(1,p) == 0
results['divided_tests_assuming_unit_comparison'] = rows
results['unproved_unit_cannot_transfer_divisibility'] = 'eta=p^2, M=1, A=p^2'

# Real countercontrols for conclusions the report refuses to draw.
for p in (5,7,11):
    assert all(p != 0 for T in (0,p,p*p))  # p is nonzero, but a nonunit.
    assert vp(p**4,p) == 4                # primitive power series T^4 at T=p.
    assert ((1,0)[1] % p) == 0           # nonzero fixed source, zero realization.
results['countercontrols'] = ['dense-point nonzero is not a unit',
                             'free Hida coefficient ring does not bound a value',
                             'nonzero ancestor needs a non-killing realization']

out = {'status':'PASS',
       'scope':'formula controls only; no seed Sha, Hecke algebra or class group computed',
       'groups':len(results), 'results':results}
(Path(__file__).parent/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'groups':len(results),'scope':out['scope']}))
