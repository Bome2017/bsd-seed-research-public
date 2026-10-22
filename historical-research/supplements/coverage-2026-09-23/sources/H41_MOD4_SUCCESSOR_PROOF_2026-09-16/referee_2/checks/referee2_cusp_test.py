#!/usr/bin/env python3
"""Referee 2: a necessary consequence of L2 at ALL cusps.
If delta := omega_f - s*theta lies in 4 H^0(X_R, Omega(cusps)) (s=+1 pos, s=-1 neg), then for every Atkin-Lehner
automorphism W_Q (Q || N) of the model, W_Q^* delta = eps_Q omega_f - s * dlog(F o W_Q) also lies in 4 H^0, so its
q-expansion at inf-bar is 0 mod 4. F o W_Q = const * prod eta(dz)^{r_{d*Q}}, d*Q = dQ/gcd(d,Q)^2; eps_Q = prod_{p|Q} (-a_p)."""
from fractions import Fraction as Fr
from math import gcd
import sympy as sp
def pos_r(l): return {1: 6*l+1, 2: -3*l-2, 3: -2*l-3, 6: l+6, l: -l-6, 2*l: 2*l+3, 3*l: 3*l+2, 6*l: -6*l-1}
def neg_r(p): return {1: 2*p-1, 2: 2-p, p: p-2, 2*p: 1-2*p}
def theta(r, M):
    th = [Fr(0)]*(M+1); th[0] = Fr(sum(d*e for d, e in r.items()), 24)
    for d, e in r.items():
        for k in range(1, M//d+1):
            for j in range(1, M//(d*k)+1): th[d*k*j] += -e*d*k
    return th
def ap_long(A, B, p):
    cnt = 1
    for x in range(p):
        g = (x**3 + A*x*x + B*x) % p
        cnt += 1 if g == 0 else (2 if pow(g, (p-1)//2, p) == 1 else 0)
    return p + 1 - cnt
def an_list(rr, N, M):
    a = [0]*(M+1); a[1] = 1; b = -rr//4
    for p in sp.primerange(2, M+1):
        if p == 2: ap = 2 - sum(1 for x in (0,1) for y in (0,1) if (y*y+x*y-b*y-x**3+b*x*x) % 2 == 0)
        else: ap = ap_long((1-2*rr), rr*rr, p)
        pk, prev, cur = p, 1, ap
        while pk <= M:
            a[pk] = cur; prev, cur = cur, ap*cur - (0 if N % p == 0 else p)*prev; pk *= p
    for n in range(2, M+1):
        f = sp.factorint(n)
        if len(f) > 1:
            v = 1
            for q, e in f.items(): v *= a[q**e]
            a[n] = v
    return a
M = 120
for kind, m in (("pos", 3), ("neg", 3), ("pos", 5), ("neg", 5), ("pos", 7)):
    rr = -2**m if kind == "pos" else 2**m; D = 1 - 4*rr
    if kind == "pos":
        l = 19 if m == 7 else D//3; N = 6*l; r = pos_r(l); s = +1
    else:
        p = -D; N = 2*p; r = neg_r(p); s = -1
    a = an_list(rr, N, M)
    ps = sp.primefactors(N)
    res = []
    for Q in sorted(d for d in r):
        if gcd(Q, N//Q) != 1: continue
        eps = 1
        for q in sp.primefactors(Q):
            bq = -rr//4
            aq = (2 - sum(1 for x in (0,1) for y in (0,1) if (y*y+x*y-bq*y-x**3+bq*x*x) % 2 == 0)) if q == 2 else ap_long(1-2*rr, rr*rr, q)
            eps *= -aq
        rQ = {d: r[d*Q//gcd(d, Q)**2] for d in r}
        th = theta(rQ, M)
        const_ok = th[0].denominator == 1 and int(th[0]) % 4 == 0
        coef_ok = all((eps*a[n] - s*th[n]) % 4 == 0 for n in range(1, M+1))
        bad = [n for n in range(1, M+1) if (eps*a[n] - s*th[n]) % 4 != 0][:5]
        res.append((Q, eps, str(th[0]), const_ok, coef_ok, bad))
    print(f"{kind} m={m} N={N}:")
    for row in res:
        print(f"   Q={row[0]:>4} eps_Q={row[1]:+d} theta'_0={row[2]:>10} const=0 mod 4: {row[3]}  eps*a_n == s*theta'_n mod 4 (n<={M}): {row[4]}  first failures: {row[5]}")
