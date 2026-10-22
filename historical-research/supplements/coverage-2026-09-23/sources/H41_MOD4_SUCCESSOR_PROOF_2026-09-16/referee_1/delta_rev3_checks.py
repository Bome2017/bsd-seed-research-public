#!/usr/bin/env python3
"""Referee 1, delta rev 2 -> rev 3: regression of the explicit c_4 values in R8 (not a proof)."""
import sympy as sp
r = sp.symbols('r')
models = {"E": (1, -r/2, 0, r**2/16, 0), "B": (1, r, 0, r/4, 0), "F": (1, -2*r, 0, r**2 - 3*r/2, r*(r-1)/4), "G": (1, 4*r, 0, 2*r, r/4)}
claimed = {"E": r**2 - 4*r + 1, "B": 16*r**2 - 4*r + 1, "F": 16*r**2 + 56*r + 1, "G": 256*r**2 - 64*r + 1}
ok = True
for V, (a1, a2, a3, a4, a6) in models.items():
    b2 = a1**2 + 4*a2; b4 = 2*a4 + a1*a3
    c4 = sp.expand(b2**2 - 24*b4)
    same = sp.simplify(c4 - claimed[V]) == 0
    odd = all(int(c4.subs(r, e*2**m)) % 2 == 1 for e in (-1, 1) for m in range(3, 40, 2))
    integral = all(sp.sympify(c).subs(r, e*2**m).is_integer for c in (a1, a2, a3, a4, a6) for e in (-1, 1) for m in range(3, 40, 2))
    ok &= same and odd and integral
    print(f"R8 {V}: c_4 = {c4} ; matches rev 3 value: {same}; odd for r = +-2^m (m odd 3..39): {odd}; model integral: {integral}")
assert ok
print("DELTA_REV3_CHECKS_OK")
