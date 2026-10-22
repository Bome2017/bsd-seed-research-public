#!/usr/bin/env python3
"""Validate the analytic plus-symbol formula used for the seed at composite m=p^2.

  [a/m]^+ * Omega = sum_b S_b ( cos(2 pi a b/m) + w_E cos(2 pi a' b/m) ),
  S_b = sum_{n = b mod m} a_n/n exp(-2 pi n/(m sqrt N)),  a' = (N a)^(-1) mod m,

against EXACT Manin-relation plus symbols (w3_source/modsym2.py) on small conductors,
at prime and composite (prime-square) denominators coprime to N.  The constant Omega
must be the same for every a and every m.
"""
import math, sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'w3_source'))
from weight2_jet import plus_eigensymbol
from modsym2 import ap_count

def an_table(coeffs, N, T):
    ap = {}
    a = [0]*(T+1); a[1] = 1
    # sieve smallest prime factor
    spf = list(range(T+1))
    for i in range(2, int(T**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, T+1, i):
                if spf[j] == j: spf[j] = i
    def apk(p, k):
        if p not in ap: ap[p] = ap_count(coeffs, p) if p < 400 else fast_ap(coeffs, p)
        if N % p == 0: return ap[p]**k
        x0, x1 = 1, ap[p]
        for _ in range(k-1): x0, x1 = x1, ap[p]*x1 - p*x0
        return x1 if k >= 1 else 1
    for n in range(2, T+1):
        p = spf[n]; k = 0; r = n
        while r % p == 0: r //= p; k += 1
        a[n] = a[r]*apk(p, k)
    return a

def fast_ap(coeffs, p):
    a1, a2, a3, a4, a6 = coeffs
    # y^2 + a1xy + a3y = f  ->  (2y+a1x+a3)^2 = 4f + (a1x+a3)^2
    sq = [0]*p
    for y in range(p): sq[y*y % p] += 1
    cnt = 1
    for x in range(p):
        r = (4*(x**3 + a2*x*x + a4*x + a6) + (a1*x + a3)**2) % p
        cnt += sq[r]
    return p + 1 - cnt

def analytic(a_n, N, m, w, a):
    X = m*math.sqrt(N)
    S = [0.0]*m
    for n in range(1, len(a_n)):
        if a_n[n]: S[n % m] += a_n[n]/n*math.exp(-2*math.pi*n/X)
    ap_ = pow(N*a, -1, m)
    return sum(S[b]*(math.cos(2*math.pi*a*b/m) + w*math.cos(2*math.pi*ap_*b/m)) for b in range(m))

def run(label, N, coeffs, w, ms):
    M, aq, plus = plus_eigensymbol(N, coeffs)
    T = int(9*max(ms)*math.sqrt(N))
    a_n = an_table(coeffs, N, T)
    rows = []; ratios = []
    for m in ms:
        for a in range(1, m):
            if math.gcd(a, m) != 1: continue
            ex = M.symbol_inf_to(plus, a, m) + M.symbol_inf_to(plus, -a, m)
            an = analytic(a_n, N, m, w, a)
            rows.append((m, a, ex, an))
            if ex: ratios.append(an/ex)
    Om = sum(ratios)/len(ratios)
    maxdev = max(abs(an - Om*ex) for (m, a, ex, an) in rows)
    return {"curve": label, "N": N, "w_E": w, "m": ms, "n_symbols": len(rows),
            "Omega_fit": Om, "max_abs_dev": maxdev, "ok": maxdev < 1e-6}

if __name__ == "__main__":
    out = [run("11a1", 11, (0, -1, 1, -10, -20), 1, [7, 9, 25, 49]),
           run("37a1", 37, (0, 0, 1, -1, 0), -1, [5, 7, 25, 49]),
           run("389a1", 389, (0, 1, 1, -2, 0), 1, [5, 7, 25, 49])]
    print(json.dumps(out, indent=1))
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "FORMULA_VALIDATION.json"), "w"), indent=1)
