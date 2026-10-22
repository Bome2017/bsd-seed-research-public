#!/usr/bin/env python3
"""Reviewer's own depth-n coefficient from the CERTIFIED symbols (exact), for comparison with the engine's A_EXACT line.

usage: weights.py CERT_SYMBOLS p n alpha LATDEN [ENGINE_MERGE_OUT ...]
Definition (certified p = 3 run, downstream/p3_downstream.py docstring; SW Sect. 3): mu(b + p^n Z_p) = alpha^-n [b/p^n]^+,
P_n(T) = sum_b mu(b) (1+T)^{j(b)} with b = omega(b) (1+p)^{j(b)}, omega = Teichmueller; a_{n,r} = coefficient of T^r.
Implementation independent of the engine: omega by Hensel iteration t -> t^p (n+2 times), j by brute-force search.
"""
import sys, re
from fractions import Fraction as F
from math import comb, gcd
sym, p, n, alpha, LAT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
outs = sys.argv[6:]
m = p ** n
x = {}
for l in open(sym):
    if l.startswith('#') or not l.strip(): continue
    b, pl, mi = l.split(); x[int(b)] = F(pl)
def teich(b):
    t = b % m
    for _ in range(n + 2): t = pow(t, p, m)
    assert t % p == b % p and pow(t, p - 1, m) == 1
    return t
pw = {}
g = 1
for j in range(p ** (n - 1)): pw[g] = j; g = g * (1 + p) % m
assert len(pw) == p ** (n - 1)
fails = 0
for r in (0, 1, 2, 3, 6, 7):
    A = F(0)
    for b in range(1, m):
        if b % p == 0: continue
        onep = b * pow(teich(b), -1, m) % m
        j = pw[onep]
        A += comb(j, r) * x[b]
    A *= F(alpha) ** (-n)
    AL = A * LAT
    unit = (AL.denominator == 1 and AL.numerator % p != 0)
    print(f'reviewer: p={p} n={n} r={r} alpha={alpha}: a_(n,r) = {A}   LATDEN*a = {AL}   mod p = {AL.numerator % p if AL.denominator == 1 else "n/a"}   unit={unit}')
    for fn in outs:
        cur = None
        for l in open(fn):
            mw = re.match(r'WEIGHTS p (\d+) n (\d+) r (\d+) alpha (-?\d+)', l)
            if mw: cur = tuple(int(v) for v in mw.groups())
            ma = re.match(r'A_EXACT LATDEN\*a_\{n,r\} = (-?\d+)', l)
            if ma and cur == (p, n, r, alpha):
                ok = int(ma.group(1)) == AL
                fails += not ok
                print(f'   {"PASS" if ok else "FAIL"} engine {fn.split("/")[-1]} A_EXACT {ma.group(1)} vs reviewer {AL}')
sys.exit(1 if fails else 0)
