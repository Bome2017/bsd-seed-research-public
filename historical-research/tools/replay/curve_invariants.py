#!/usr/bin/env python3
"""Exact replay of the curve data used by claims A.1, A.2 and R.1 (standard library only; no PARI/Sage).

Checks, each printed as PASS/FAIL:
  * c4, c6, Delta and j of E: y^2 = x^3 - 22735x^2 + 106272484x, and the prime support of Delta and N;
  * the global minimal model obtained by x = X + 7578 (same c4, c6, Delta; u = 1);
  * T = (0,0), P1 = (4547, 327384), P2 = (5184, 281520) lie on E (and their images on the minimal model);
  * a_p for the good primes p < 2000 by exact point counting: a_p is even, p never divides #E(F_p),
    and the supersingular primes below 2000 are exactly the recorded list.
"""
from fractions import Fraction
import sys

A = (0, -22735, 0, 106272484, 0)                        # a1, a2, a3, a4, a6
N = 2**3 * 3 * 2243 * 4547**2 * 5843
BAD = (2, 3, 2243, 4547, 5843)
SS_RECORDED = [23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823]
ok = True


def check(name, cond):
    global ok
    ok &= bool(cond)
    print(f"{'PASS' if cond else 'FAIL'}  {name}")


def invariants(a1, a2, a3, a4, a6):
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    disc = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    return c4, c6, disc


def support(n):
    n = abs(n)
    out = {}
    for p in BAD:
        while n % p == 0:
            n //= p
            out[p] = out.get(p, 0) + 1
    return out, n


c4, c6, D = invariants(*A)
check('c4 = 3169004368', c4 == 3169004368)
check('c6 = 56243184546880', c6 == 56243184546880)
check('Delta = 16586638656786071143743744 = 2^8 3^2 2243 4547^3 5843^2', D == 16586638656786071143743744 == 2**8 * 3**2 * 2243 * 4547**3 * 5843**2)
check('1728*Delta = c4^3 - c6^2', 1728 * D == c4 ** 3 - c6 ** 2)
sup, rest = support(D)
check('Delta is supported exactly on {2, 3, 2243, 4547, 5843}', rest == 1 and set(sup) == set(BAD))
j = Fraction(c4 ** 3, D)
check('j = 1322372123614064/689197281363, not an integer (no CM)', j == Fraction(1322372123614064, 689197281363) and j.denominator != 1)
check('N = 6503188012738584', N == 6503188012738584)

# minimal model: x = X + 7578, y = Y (u = 1, s = t = 0): a2' = a2 + 3r, a4' = a4 + 2 a2 r + 3 r^2, a6' = a6 + a4 r + a2 r^2 + r^3
r = 7578
a2m, a4m, a6m = A[1] + 3 * r, A[3] + 2 * A[1] * r + 3 * r * r, A[4] + A[3] * r + A[1] * r * r + r ** 3
check('minimal model [0,-1,0,-66020924,-65074271436]', (a2m, a4m, a6m) == (-1, -66020924, -65074271436))
check('minimal model has the same c4, c6, Delta (u = 1)', invariants(0, a2m, 0, a4m, a6m) == (c4, c6, D))


def on_curve(P, a2, a4, a6):
    x, y = P
    return y * y == x ** 3 + a2 * x * x + a4 * x + a6


for name, P in (('T', (0, 0)), ('P1', (4547, 327384)), ('P2', (5184, 281520))):
    check(f'{name} = {P} lies on E', on_curve(P, A[1], A[3], A[4]))
    check(f'{name} - (7578, 0) lies on the minimal model', on_curve((P[0] - r, P[1]), a2m, a4m, a6m))


def primes(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def ap(p):
    """a_p = -sum_x legendre(x^3 + a2 x^2 + a4 x + a6, p) for odd good p (Euler's criterion)."""
    s = 0
    for x in range(p):
        v = (x * x * x + A[1] * x * x + A[3] * x + A[4]) % p
        if v:
            s += 1 if pow(v, (p - 1) // 2, p) == 1 else -1
    return -s


good = [p for p in primes(2000) if p not in BAD]
aps = {p: ap(p) for p in good}
check('a_5, a_7, a_11, a_13 = -2, -2, -2, -4', (aps[5], aps[7], aps[11], aps[13]) == (-2, -2, -2, -4))
check('#E(F_5) = 8', 5 + 1 - aps[5] == 8)
check('a_p is even for every good p < 2000 (rational 2-torsion)', all(a % 2 == 0 for a in aps.values()))
check('p never divides #E(F_p) for good p < 2000', all((p + 1 - a) % p for p, a in aps.items()))
check('supersingular primes < 2000 are exactly the recorded 15', [p for p, a in aps.items() if a == 0] == SS_RECORDED)
print('ALL PASS' if ok else 'SOME CHECKS FAILED')
sys.exit(0 if ok else 1)
