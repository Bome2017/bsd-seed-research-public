#!/usr/bin/env python3
"""Referee 2 extra regressions: (F) rational 2-torsion of the four vertices (closure of the 2-isogeny graph),
(G) Ligozat divisor of the positive eta unit symbolically in l (divisor lattice of 6l with l a symbol), and
(H) E(Q)_tors bound from F_3 on the negative branch."""
import sympy as sp
r, l = sp.symbols('r l')
D = 1 - 4*r
# (F) y^2 = x(x^2 + A x + B): number of rational 2-torsion points = 1 + 2*[A^2-4B is a nonzero square]
curves = {"E": (1-2*r, r**2), "B": (-(1+D), D), "F": (-2-8*r, D**2), "G": (-2+16*r, 1)}
for V, (A, B) in curves.items():
    disc = sp.factor(sp.expand(A**2 - 4*B))
    print(f"F. {V}: disc of quadratic factor = {disc}")
    for sgn in (-1, 1):
        for m in (3, 5, 7, 9, 11, 13, 15, 17):
            val = int(disc.subs(r, sgn*2**m))
            sq = val > 0 and sp.sqrt(val).is_integer
            if V == "B": assert sq, (V, sgn, m)
            else: assert not sq, (V, sgn, m)
print("F. for r = +-2^m (m = 3..17 odd): E, F, G have exactly one rational 2-torsion point, B has full 2-torsion -> 2-isogeny graph E-B, B-F, B-G is closed")
# (G) Ligozat orders for N = 6l, divisors d = 2^a 3^b l^c, symbolic in l (l prime > 3)
from itertools import product
divs = [(a, b, c) for a, b, c in product((0, 1), repeat=3)]
def val(t): a, b, c = t; return 2**a * 3**b * l**c
def g(t, u): return tuple(min(x, y) for x, y in zip(t, u))
rvec = {(0,0,0): 6*l+1, (1,0,0): -3*l-2, (0,1,0): -2*l-3, (1,1,0): l+6, (0,0,1): -l-6, (1,0,1): 2*l+3, (0,1,1): 3*l+2, (1,1,1): -6*l-1}
N = 6*l
ok = True
for c in divs:
    s = sum(val(g(c, d))**2 * rvec[d] / (val(c) * val(d)) for d in divs)   # gcd(c, N/c) = 1 (squarefree)
    order = sp.simplify(N/24 * s)
    exp = -(l**2-1) if c == (1,1,1) else ((l**2-1) if c == (0,0,0) else 0)
    ok &= sp.simplify(order - exp) == 0
    print(f"G. cusp 1/{val(c)}: order = {sp.factor(order)}")
print(f"G. positive eta unit has divisor (l^2-1)([0]-[inf]) identically in l: {ok}")
# (H) negative branch: #E(F_3) = 4 for r = 2^m, m odd  => E(Q)_tors injects into a group of order 4
for m in (3, 5, 7, 9, 11, 13, 15, 17):
    rr = 2**m % 3
    cnt = 1 + sum(1 if (x**3 + (1-2*rr)*x*x + rr*rr*x) % 3 == 0 else (2 if pow((x**3 + (1-2*rr)*x*x + rr*rr*x) % 3, 1, 3) == 1 else 0) for x in range(3))
    assert cnt == 4
print("H. negative branch: #E(F_3) = 4 for all odd m (so E(Q)_tors = C_4 given the rational 4-torsion point)")
