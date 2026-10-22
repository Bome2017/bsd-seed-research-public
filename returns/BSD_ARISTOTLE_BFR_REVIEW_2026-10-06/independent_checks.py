"""Audit controls only: no Selmer/class-group computation or BSD inference.

Run with Python 3.8+ from any directory. Reproduces
checks/INDEPENDENT_LOCAL_AND_GENUS.json using only integer arithmetic.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
a, b = 66020924, 65074271436
p, m = 4547, 4547**4
P = (-2394 % m, 281520 % m)
denoms = []


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if P == Q:
        nom, den = 3*x*x - 2*x - a, 2*y
    else:
        nom, den = v-y, u-x
    assert den % p
    denoms.append(den % p)
    lam = nom * pow(den, -1, m) % m
    xx = (lam*lam + 1 - x - u) % m
    return xx, (-y + lam*(x-xx)) % m


R = None
for digit in bin(p-1)[2:]:
    R = add(R, R)
    if digit == "1":
        R = add(R, P)
assert (R[1]**2 - (R[0]**3 - R[0]**2 - a*R[0] - b)) % m == 0
xd = (R[0] - P[0]) % m
translation = [3*1516-1, 3*1516**2-2*1516-a,
               1516**3-1516**2-a*1516-b]


def disc(c):
    a2, a4, a6 = c
    b2, b4, b6, b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6-a4*a4
    return -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6


def count(q, c):
    a2, a4, a6 = c
    # Enumerate squares independently of the returned Legendre-symbol method.
    squares = [0]*q
    for y in range(q):
        squares[y*y % q] += 1
    return 1 + sum(squares[(x**3+a2*x*x+a4*x+a6) % q]
                   for x in range(q))


e, e2 = (-1, -a, -b), (-a, b, b*b)
traces = []
for q in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    if disc(e) % q == 0 or disc(e2) % q == 0:
        continue
    n1, n2 = count(q, e), count(q, e2)
    traces.append(dict(q=q, nE=n1, nE2=n2, aE=q+1-n1,
                       aE2=q+1-n2, difference=n2-n1))

out = dict(
    method="binary addition modulo p^4 with independently written affine formulas",
    p=p, additions=len(denoms), all_denominators_units=True,
    x_difference_mod_p2=xd % (p*p),
    normalized_x_difference_mod_p=(xd//p) % p,
    point_mod_p4=R, translated_coefficients=translation,
    coefficients_divided_by_p=[x//p for x in translation],
    all_translated_coefficients_p_divisible=all(x % p == 0 for x in translation),
    E2_discriminant=disc(e2), frobenius_counts=traces,
)
assert out["normalized_x_difference_mod_p"] == 1274
assert all(next(t for t in traces if t["q"] == q)["difference"] == 4
           for q in [11, 19])
target = ROOT / "checks/INDEPENDENT_LOCAL_AND_GENUS.json"
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
