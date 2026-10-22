#!/usr/bin/env python3
"""Exact check (integers only): can any Gamma_0(N) or Atkin-Lehner move of the depth-2 cusps b/p^2
be evaluated at a smaller analytic scale than the current direct one, c*sqrt(width) = p^2*sqrt(Q)?

Scale model (the one the engine uses): the symbol {inf, a/c} costs c*sqrt(width(a/c)) up to a constant,
width(a/c) = N / gcd(c^2, N).  A symbol {r, s} between two finite cusps costs the max over its endpoints.

(1) loop route: gamma_b in Gamma_0(N) with gamma_b(1/p) = b/p^2 has lower-left entry c = N*k with k fixed mod p^2
    by b; the base-point evaluation of the loop period needs scale |c|.
(2) W_Q route: some W_Q maps b/p^2 to inf and inf to x/p^2 with x = +-u_b, u_b = (Qb)^{-1} (mod p^2):
    this is exactly the pairing R1 (no new information).
(3) W_p route: W_p(inf) = x/(Qz) with z != 0, scale >= Q*sqrt(p).
(4) W_N route: W_N(b/p^2) = -p/(Q b'), b' = b + k p^2 != 0, scale >= Q*sqrt(p).
"""
from math import gcd, isqrt, sqrt

p = 2243
N = 2**3 * 3 * 2243 * 4547**2 * 5843
Q = N // p
m = p * p
assert N == 6503188012738584 and Q * p == N and gcd(p, Q) == 1

def width(c):
    return N // gcd(c * c, N)

def scale(c):
    return abs(c) * sqrt(width(c))

direct = scale(m)
print(f"direct scale p^2*sqrt(Q) = {direct:.4e}   (width of b/p^2 = {width(m)} = Q: {width(m) == Q})")

bs = [2, 3, 5, 7, 11, 1000, 123456, 2243 * 1000 + 17, m - 2]
bs = [b for b in bs if b % p]

# (1) loops
worst = 0
for b in bs:
    k = (-(1 - b * p) * pow(b * Q, -1, m)) % m
    k = k - m if k > m // 2 else k
    c = N * k
    d = p - Q * k
    bp = (b * p - b * Q * k - 1)
    assert bp % m == 0
    bp //= m
    a = b - bp * p
    assert a * d - bp * c == 1 and c % N == 0
    assert (a + bp * p) == b and (c + d * p) == m          # gamma_b(1/p) = b/p^2 exactly
    worst = max(worst, abs(k))
    print(f"(1) b={b:>8}: k_b={k:>9}  |c|=N|k| = {abs(c):.3e}  = {abs(c)/direct:.2e} x direct")
print(f"(1) min over k != 0 of N|k| = N = {N:.4e} = {N/direct:.1f} x direct; k_b is fixed mod p^2 by b")

# (2) W_Q with W_Q(b/p^2) = inf:  z = p t, w = -b t, t = +-1, need Q x b + p^2 y = -t ... from Q x w - p z y = 1
for b in bs:
    for t in (1, -1):
        # Q x (-b t) - p (p t) y = 1  ->  -t (Q b x + p^2 y) = 1  ->  Q b x + p^2 y = -t
        x = (-t * pow(Q * b, -1, m)) % m
        y = (-t - Q * b * x)
        assert y % m == 0
        y //= m
        z, w = p * t, -b * t
        WQ = ((Q * x, y), (N * z, Q * w))
        det = WQ[0][0] * WQ[1][1] - WQ[0][1] * WQ[1][0]
        assert det == Q
        # image of b/p^2: (Q x b + y p^2) / (N z b + Q w p^2); denominator must vanish
        assert N * z * b + Q * w * m == 0
        # image of inf: Q x / (N z) = x / (p z) = x / (t p^2)  -> cusp +-x/p^2
        u = pow(Q * b, -1, m)
        assert (t * x) % m in (u % m, (-u) % m)
print("(2) W_Q route: for every tested b, W_Q(b/p^2) = inf and W_Q(inf) = +-u_b/p^2 -> exactly the pairing R1")

# (3) W_p = [[p x, y],[N z, p w]], det p  <=>  p x w - Q z y = 1 ; W_p(inf) = x/(Q z), z != 0
print(f"(3) W_p route: scale of x/(Qz) >= Q*sqrt(p) = {Q*sqrt(p):.4e} = {Q*sqrt(p)/direct:.2f} x direct (width(Q) = {width(Q)} = p)")

# (4) W_N(b/p^2) = -p/(Q b')
print(f"(4) W_N route: c = Q|b'| >= Q, scale >= {scale(Q):.4e} = {scale(Q)/direct:.2f} x direct")
print(f"conclusion: min over tested orbit moves = direct scale; every alternative is >= {min(Q*sqrt(p), N)/direct:.2f} x")
