#!/usr/bin/env python3
"""Exact checks for the symbol-lattice import audit (standard library only).
(1) Both curves of the seed's 2-isogeny class: v_4547(Delta) = 3, 4547 | c4, 4547 | c6 (additive, Kodaira type III for p >= 5),
    models minimal at 4547 (v(Delta) < 12), j == 1728 mod 4547, and 4547 == 3 mod 4 (so the potentially good reduction is
    supersingular: j = 1728 is supersingular exactly when p == 3 mod 4).
(2) Every modular-symbol denominator used by the retained certificates has gcd(d, N) an exact (Hall) divisor of N.
"""
from fractions import Fraction
from math import gcd
N = 2**3 * 3 * 2243 * 4547**2 * 5843
p = 4547

def inv(a1, a2, a3, a4, a6):
    b2 = a1*a1 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4; c6 = -b2**3 + 36*b2*b4 - 216*b6
    D = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    return c4, c6, D

def v(n, q):
    n = abs(n); e = 0
    while n and n % q == 0:
        n //= q; e += 1
    return e

a, b = -22735, 106272484                      # E: y^2 = x^3 + a x^2 + b x
curves = {'E (seed)': (0, a, 0, b, 0), "E' (2-isogenous)": (0, -2*a, 0, a*a - 4*b, 0)}
ok = True
for name, A in curves.items():
    c4, c6, D = inv(*A)
    j = Fraction(c4**3, D)
    jm = j.numerator * pow(j.denominator, -1, p) % p
    good = v(D, p) == 3 and v(c4, p) >= 1 and v(c6, p) >= 2 and jm == 1728 % p
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  {name}: v_4547(Delta)={v(D,p)} v(c4)={v(c4,p)} v(c6)={v(c6,p)} j mod 4547={jm} (type III, minimal at 4547)")
print(f"{'PASS' if p % 4 == 3 else 'FAIL'}  4547 = {p % 4} mod 4 -> j = 1728 reduction is supersingular")
ok &= p % 4 == 3
dens = {'p=5 (m=25)': 25, 'p=7 (m=49)': 49, 'p=11 (m=121)': 121, 'p=13 (m=169)': 169, 'p=3 (m=27)': 27,
        'p=3 (m=81)': 81, 'p=2243 route (m=2243^2)': 2243**2, 'lower levels 5,7,11,13,3,9': 5*7*11*13*9}
for name, d in dens.items():
    g = gcd(d, N); hall = gcd(g, N // g) == 1
    ok &= hall
    print(f"{'PASS' if hall else 'FAIL'}  {name}: gcd(d,N)={g}, exact divisor of N: {hall}")
print('ALL PASS' if ok else 'SOME CHECKS FAILED')
