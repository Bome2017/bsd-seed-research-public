#!/usr/bin/env python3
"""Independent recomputation of the certified Mazur-Tate coefficients from the certified symbol tables.

This implements the depth-n formula of the manuscript (section 4.1) from scratch:
  good ordinary p:     P_n(T) = sum_{a in (Z/p)^x} sum_{j < p^(n-1)} ( alpha^-n [w(a) g^j / p^n]^+  -  alpha^-(n+1) [w(a) g^j / p^(n-1)]^+ ) (1+T)^j
  multiplicative p:    the same without the second term (f is already U_p-stabilized, alpha = a_p = +-1)
with g = 1 + p, w the Teichmueller lift, and alpha the unit root of X^2 - a_p X + p (good ordinary case).
It reads only the certified tables SYMBOLS_m*.txt (values are exact; all happen to be integers) and prints the
coefficients next to the values recorded in the theorem records. It shares no code with the recorded downstream scripts.
"""
import sys
from math import comb, gcd
from pathlib import Path

REL = Path(__file__).resolve().parents[2]
S = REL / 'evidence' / 'src'
TABLES = {
    3: ('BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run', 4, -1, True),       # p: (folder, depth n, a_p, multiplicative)
    5: ('BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run', 2, -2, False),
    7: ('BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p7/run', 2, -2, False),
    11: ('BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p11/run', 2, -2, False),
    13: ('BSD_SEED_P13_RUN_2026-09-21/run', 2, -4, False),
}
RECORDED = {3: ('a_{4,2} (exact integer)', 15480), 5: ('C_5 mod 5', 2), 7: ('C_7 mod 7', 1), 11: ('C_11 mod 11', 8), 13: ('C_13 mod 13', 2)}


def load(folder, m):
    """Return {b: [b/m]^+} for all b in (Z/m)^x, using [-b]^+ = [b]^+ for the half-table."""
    d = {}
    for line in (S / folder / f'SYMBOLS_m{m}.txt').read_text().splitlines():
        if line.startswith('#') or not line.strip():
            continue
        t = line.split()
        d[int(t[0]) % m] = int(t[1])
    full = {}
    for b in range(1, m):
        if gcd(b, m) == 1:
            full[b] = d[b] if b in d else d[(m - b) % m]
    return full


def unit_root(ap, p, k):
    """The p-adic unit root of X^2 - ap X + p modulo p^k (Hensel from alpha = ap mod p)."""
    mod = p ** k
    x = ap % p
    for _ in range(k + 2):
        f = (x * x - ap * x + p) % mod
        df = (2 * x - ap) % mod
        x = (x - f * pow(df, -1, mod)) % mod
    assert (x * x - ap * x + p) % mod == 0 and x % p
    return x


def coefficients(p):
    folder, n, ap, mult = TABLES[p]
    m, mlow = p ** n, p ** (n - 1)
    K = n + 3                                            # p-adic working precision for alpha
    mod = p ** K
    top = load(folder, m)
    low = None if mult else load(folder, mlow)
    if mult:                                             # alpha = a_p = +-1: exact integer arithmetic, no reduction
        mod = 10 ** 60
        ai = ap                                          # (+-1)^-1 = +-1
    else:
        alpha = unit_root(ap, p, K)
        ai = pow(alpha, -1, mod)
    g = 1 + p
    c = [0, 0, 0]                                        # T^0, T^1, T^2 coefficients (p-adic, mod p^K)
    for a in range(1, p):
        w = pow(a, p ** (n - 1), m)                      # Teichmueller lift mod p^n
        for j in range(mlow):
            b = w * pow(g, j, m) % m
            val = (ai ** n if mult else pow(ai, n, mod)) * top[b]
            if not mult:
                val -= pow(ai, n + 1, mod) * low[b % mlow]
            for r in range(3):
                c[r] = (c[r] + comb(j, r) * val) % mod
    return c, mod


ok = True
for p in (3, 5, 7, 11, 13):
    c, mod = coefficients(p)
    label, rec = RECORDED[p]
    if p == 3:
        sym = lambda x: x - mod if x > mod // 2 else x
        got = sym(c[2])
        good = got == rec and sym(c[0]) == 0 and sym(c[1]) == -54
        print(f"{'PASS' if good else 'FAIL'}  p=3: a_4,0 = {sym(c[0])}, a_4,1 = {sym(c[1])}, {label} = {got} "
              f"(recorded {rec}; 15480 = 9 mod 27: {got % 27 == 9})")
    else:
        got = c[2] % p
        good = got == rec and c[0] % p == 0 and c[1] % p == 0
        print(f"{'PASS' if good else 'FAIL'}  p={p}: {label} = {got} (recorded {rec}); constant and linear terms = 0 mod p: {c[0] % p == 0 and c[1] % p == 0}")
    ok &= good
print('ALL PASS' if ok else 'SOME CHECKS FAILED')
sys.exit(0 if ok else 1)
