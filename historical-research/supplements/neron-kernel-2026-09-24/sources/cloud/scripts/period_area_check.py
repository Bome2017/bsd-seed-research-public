#!/usr/bin/env python3
"""Cross-check of the period-area factor 4*pi^2/A_E for the seed (PROOF.md (9)), independent code.

omega = dx/(2y) on y^2 = x(x^2 - 22735x + 106272484) (= Neron differential; A.1(i), u = 1).
Delta > 0, roots e1 > e2 > e3 = 0, rectangular lattice Omega_1 Z + i Omega_2 Z.
(a) direct quadrature of the real and imaginary cycles of dx/(2y), after the substitutions
    x = e1 + (e1-e2) tan^2(phi)  and  x = e2 + (e1-e2) sin^2(theta)  (smooth integrands),
(b) AGM formulas Omega_1 = pi/g1, |Omega_2| = pi/g2,
and compares 4 pi^2/(Omega_1 |Omega_2|) with 4 g1 g2 and with the packet's seed_period_multiplier.
"""
import json, math, sys
from decimal import Decimal, getcontext
getcontext().prec = 60
a2, a4 = Decimal(-22735), Decimal(106272484)
disc = a2*a2 - 4*a4
r = disc.sqrt()
e1, e2, e3 = (-a2 + r)/2, (-a2 - r)/2, Decimal(0)
def agm(x, y):
    for _ in range(200):
        x, y = (x + y)/2, (x*y).sqrt()
        if abs(x - y) < Decimal(10)**-55: break
    return x
g1 = agm((e1 - e3).sqrt(), (e1 - e2).sqrt())
g2 = agm((e1 - e3).sqrt(), (e2 - e3).sqrt())
pi = Decimal("3.14159265358979323846264338327950288419716939937510582097494")
def trap(f, n):              # trapezoid on [0, pi/2]; integrands are smooth and even-periodic
    h = pi/2/n
    s = (f(Decimal(0)) + f(pi/2))/2 + sum(f(h*k) for k in range(1, n))
    return s*h
def dsin(x):                 # Decimal sin/cos via float-free Taylor (sufficient here)
    x = +x; s, t, k = Decimal(0), x, 1
    while abs(t) > Decimal(10)**-58:
        s += t; t = -t*x*x/((2*k)*(2*k+1)); k += 1
    return s
def dcos(x): return dsin(pi/2 - x)
A, B, C = e1 - e2, e1 - e3, e2 - e3
# real cycle: Omega_1 = 2 * int_{e1}^inf dx/(2y) = int_0^{pi/2} 2 dphi / sqrt(A sin^2 + B cos^2)
O1 = trap(lambda t: 2/((A*dsin(t)**2 + B*dcos(t)**2).sqrt()), 64)
# imaginary cycle: |Omega_2| = int_{e2}^{e1} dx/sqrt(-f) = int_0^{pi/2} 2 dtheta / sqrt(C cos^2 + B sin^2)
O2 = trap(lambda t: 2/((C*dcos(t)**2 + B*dsin(t)**2).sqrt()), 64)
mult_quad = 4*pi*pi/(O1*O2)
mult_agm = 4*g1*g2
seed = json.load(open(sys.argv[1]))["seed_period_multiplier"]["display"] if len(sys.argv) > 1 else None
out = {"e1": str(e1)[:30], "e2": str(e2)[:30], "Omega1_quad": str(O1)[:30], "Omega1_agm": str(pi/g1)[:30],
       "Omega2_quad": str(O2)[:30], "Omega2_agm": str(pi/g2)[:30],
       "multiplier_quadrature": str(mult_quad)[:32], "multiplier_4g1g2": str(mult_agm)[:32],
       "rel_diff": float(abs(mult_quad - mult_agm)/mult_agm), "packet_seed_display": seed}
print(json.dumps(out, indent=1))
