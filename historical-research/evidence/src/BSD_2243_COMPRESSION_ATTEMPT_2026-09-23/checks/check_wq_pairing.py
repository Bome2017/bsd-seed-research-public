#!/usr/bin/env python3
"""Exact checks on CERTIFIED seed symbols (p = 3 run, m = 27 and 81), in the certificate's own conventions:
 (1) Atkin-Lehner W_Q pairing used by the unitary-cusp formula: u_b = (Q b)^{-1} mod m  =>  [u_b/m]^+ = s [b/m]^+ and
     [u_b/m]^- = -s [b/m]^-  (s from the certified header);
 (2) the pairing on the wild coordinate: l(u_b) = -l(Q) - l(b) (mod p^{n-1}); hence the column sums Y_j satisfy
     Y_{-l(Q)-j} = s Y_j;
 (3) the U_p trace (row) relation: sum_{t mod p} [(c + t m/p)/m]^+ = a_p [c/(m/p)]^+  (m = 81 -> 27), a_3 = -1.
Nothing is produced; only retained certified files are read."""
import re
from math import gcd
R = '/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run'
def load(m):
    d = {}; hdr = ''
    for L in open(f'{R}/SYMBOLS_m{m}.txt'):
        if L.startswith('#'): hdr += L; continue
        t = L.split()
        if len(t) >= 3: d[int(t[0]) % m] = (int(t[1]), int(t[2]))
    Q = int(re.search(r'Q = (\d+)', hdr).group(1)); s = int(re.search(r's = (-?\d+)', hdr).group(1))
    full = {}
    for b in range(1, m):
        if gcd(b, m) != 1: continue
        if b in d: full[b] = d[b]
        elif (m - b) in d: pl, mi = d[m - b]; full[b] = (pl, -mi)      # [-b]^+ = [b]^+, [-b]^- = -[b]^-
        else: raise SystemExit(f'missing b={b}')
    return full, Q, s
def wild_log(b, p, n):
    m = p ** n; om = pow(b, p ** (n - 1), m); u = b * pow(om, -1, m) % m     # u in 1 + pZ
    g = 1 + p; x = 1
    for j in range(p ** (n - 1)):
        if x == u: return j
        x = x * g % m
    raise SystemExit('no dlog')
p = 3
for m, n in ((27, 3), (81, 4)):
    X, Q, s = load(m); ok_plus = ok_minus = 0
    for b in X:
        ub = pow(Q * b % m, -1, m)
        ok_plus += X[ub][0] == s * X[b][0]; ok_minus += X[ub][1] == -s * X[b][1]
    lQ = wild_log(Q % m, p, n); ok_l = all(wild_log(pow(Q * b % m, -1, m), p, n) == (-lQ - wild_log(b, p, n)) % p ** (n - 1) for b in X)
    Y = {}
    for b in X: j = wild_log(b, p, n); Y[j] = Y.get(j, 0) + X[b][0]
    ok_Y = all(Y.get((-lQ - j) % p ** (n - 1), 0) == s * Y.get(j, 0) for j in range(p ** (n - 1)))
    print(f"m={m}: s={s}  pairing plus {ok_plus}/{len(X)}  minus {ok_minus}/{len(X)}  l(u_b)=-l(Q)-l(b): {ok_l}  column-sum relation Y_(-l(Q)-j)=sY_j: {ok_Y}  l(Q)={lQ}")
X81, _, _ = load(81); X27, _, _ = load(27); a3 = -1
ok_tr = all(sum(X81[(c + 27 * t) % 81][0] for t in range(3)) == a3 * X27[c][0] for c in X27)
print(f"U_3 trace relation sum_t [(c+27t)/81]^+ = a_3 [c/27]^+ for all c: {ok_tr}")
