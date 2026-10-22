#!/usr/bin/env python3
"""Exact construction controls. No Mazur--Tate/seed Sha values are computed."""
import json
import sys
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import sympy as sp

sys.set_int_max_str_digits(100000)
HERE = Path(__file__).resolve().parent
A2, A4, A6 = -1, -66020924, -65074271436
P1 = (Q(-3031), Q(327384))
P2 = (Q(-2394), Q(281520))

def on_curve(P):
    return P is None or P[1]**2 == P[0]**3 + A2*P[0]**2 + A4*P[0] + A6

def add(P, R):
    if P is None:
        return R
    if R is None:
        return P
    x, y = P
    z, w = R
    if x == z and y == -w:
        return None
    slope = (3*x*x + 2*A2*x + A4)/(2*y) if P == R else (w-y)/(z-x)
    xx = slope*slope - A2 - x - z
    result = (xx, -y + slope*(x-xx))
    assert on_curve(result)
    return result

def mul(n, P):
    R = None
    while n:
        if n & 1:
            R = add(R, P)
        P = add(P, P)
        n //= 2
    return R

def den(P):
    d = isqrt(P[0].denominator)
    assert d*d == P[0].denominator
    assert (P[1]*d**3).denominator == 1
    return d

def encode(P):
    return {"x": str(P[0]), "y": str(P[1]), "d": str(den(P))}

assert on_curve(P1) and on_curve(P2)
Q1, Q2 = mul(16, P1), mul(16, P2)
points = {"P1": P1, "P2": P2, "Q1": Q1, "Q2": Q2,
          "Q1_plus_Q1": add(Q1,Q1), "Q1_plus_Q2": add(Q1,Q2),
          "Q2_plus_Q2": add(Q2,Q2)}
assert all(P is not None and on_curve(P) for P in points.values())
normalizers = {}
for i, Pi in enumerate((Q1,Q2), 1):
    for j, Pj in enumerate((Q1,Q2), 1):
        normalizers[f"c{i}{j}"] = str(Q(den(Pi)*den(Pj), den(add(Pi,Pj))))

# The universal quadratic determinant is primitive, and is GL2-equivariant.
a,b,c,d,z0,z1,z2 = sp.symbols("a b c d z0 z1 z2")
U2 = a*a*z0 + 2*a*b*z1 + b*b*z2
V2 = c*c*z0 + 2*c*d*z1 + d*d*z2
UV = a*c*z0 + (a*d+b*c)*z1 + b*d*z2
assert sp.expand(U2*V2 - UV**2 - (a*d-b*c)**2*(z0*z2-z1**2)) == 0
# Columns z0^2,z0*z1,z0*z2,z1^2,z1*z2,z2^2 map to binary quartics.
mu = sp.Matrix([[1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,1,1,0,0],
                [0,0,0,0,1,0], [0,0,0,0,0,1]])
q = sp.Matrix([0,0,1,-1,0,0])
assert mu*q == sp.zeros(5,1) and mu.rank() == 5
assert abs(mu[:,[0,1,2,4,5]].det()) == 1

# This is the G2 calibration matrix on the fixed Q_i=16P_i at p=17,l=103.
# Its arithmetic values are checked separately by the retained GP implementation.
p, ell, m = 17, 103, 106
Hformal = sp.Matrix([[1,12],[12,14]])
scale = 2*pow(16*pow(m,-1,p) % p, 2, p) % p
B = (scale*Hformal).applyfunc(lambda x: int(x)%p)
assert B == sp.Matrix([[15,10],[10,6]])
tensor_value = int(B[0,0]+B[1,1]-B[0,1]-B[1,0]) % p
det_value = int(B.det()) % p
assert (tensor_value, det_value) == (1,7)
Rproduction = int(Hformal.det())*pow(pow(m,4,p),-1,p) % p
assert det_value == 4*pow(16,4,p)*Rproduction % p

# A p-th power rational multiplier has zero tame character, not multiplier 1 mod p.
g = int(sp.primitive_root(ell))
logs = {pow(g,k,ell): k%p for k in range(ell-1)}
scalar = 2**p
assert logs[scalar % ell] == 0 and scalar % p == 2
assert (15 + logs[scalar % ell]) % p != ((scalar % p)*15) % p

# Finite augmentation: rational idempotence; mod p coefficient extraction.
def cyc_mul(x,y):
    n = len(x)
    return [sum(x[i]*y[(k-i)%n] for i in range(n)) for k in range(n)]

X = sp.symbols("X")
cyclic_cases = []
for n in (5,7,11,17):
    e = [Q(int(i==0))-Q(1,n) for i in range(n)]
    assert cyc_mul(e,e) == e
    # Genuine I^2 element in a test group ring, not seed modular symbols.
    v = [(j*j+3*j+1)%n for j in range(n)]
    x2 = [1,-2,1] + [0]*(n-3)
    coeffs = [int(x)%n for x in cyc_mul(x2,v)]
    expansion = sp.Poly(sum(coeffs[j]*(1+X)**j for j in range(n)),X)
    mom0 = sum(coeffs)%n
    mom1 = sum(j*coeffs[j] for j in range(n))%n
    mom2 = sum((j*(j-1)//2)*coeffs[j] for j in range(n))%n
    assert mom0 == mom1 == 0
    assert int(expansion.nth(2))%n == mom2
    cyclic_cases.append({"p":n,"C2_test_group_ring":mom2})

out = {
  "scope": "Exact rational seed-point normalization and algebra controls; no seed C2 or Sha computed",
  "points": {name:encode(P) for name,P in points.items()},
  "rational_fiber_normalizers": normalizers,
  "universal_determinant": {"GL2_symbolic_identity":True,"primitive_kernel":True},
  "seed_tame_matrix_control": {"p":p,"ell":ell,"formal_multiplier":m,
    "H_formal":[[int(x) for x in Hformal.row(i)] for i in range(2)],
    "B_on_Q16":[[int(x) for x in B.row(i)] for i in range(2)],
    "tensor_cross_value":tensor_value,"quadratic_determinant":det_value,
    "production_regulator":Rproduction},
  "rational_scalar_control": {"c":scalar,"c_mod_p":scalar%p,"tame_character":0,
    "primitive_root_ell":g,"unchanged_fiber_value":15,"incorrect_linear_prediction":13},
  "augmentation_controls":cyclic_cases,
  "status":"PASS"
}
(HERE/"CONSTRUCTION_RESULTS.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","rational_seed_points":len(points),
    "normalizers":len(normalizers),"symbolic_determinant":"PASS",
    "augmentation_cases":len(cyclic_cases),"largest_coordinate_digits":max(len(str(abs(v.numerator))) for P in points.values() for v in P)}))
