#!/usr/bin/env python3
"""p = 2243 (s = -1): what the W_Q column relation Y_{-L-j} = s Y_j (L = l(Q)) determines about c_r = [T^r] sum_j Y_j (1+T)^j.
Exact linear algebra over F_p on the constraint space. Also the Gauss periods eta_1(t) = sum_{zeta in mu_{p-1}} cos(2 pi zeta g^t / p^2),
needed to price aggregation to column sums. Nothing is produced; no coefficient is computed."""
import math
from fractions import Fraction
p = 2243; m = p * p; s = -1; N = 6503188012738584; Q = N // p
def wl(b):                                   # wild log l(b) = -q_p(b) mod p  (= dlog_{1+p} of the principal-unit part)
    return (-((pow(b, p - 1, m) - 1) // p)) % p
L = wl(Q % m)
g = 1 + p; assert wl(g) == 1 and all(wl(pow(a, p, m)) == 0 for a in (2, 3, 5, 1000))
j0 = (-L * pow(2, -1, p)) % p
print(f"Q = N/p = {Q};  L = l(Q) = {L} (mod {p});  self-paired column j0 = -L/2 = {j0}")
def C(j, r):                                 # binomial C(j, r) mod p as a polynomial function of j (r < p)
    num = 1
    for i in range(r): num = num * (j - i) % p
    return num * pow(math.factorial(r), -1, p) % p
# basis of the constraint space {Y : Y_{-L-j} = s Y_j}: for s = -1, e_j - e_{-L-j} over pairs {j, -L-j} with j != j0 (Y_{j0} = 0)
pairs, seen = [], set()
for j in range(p):
    k = (-L - j) % p
    if j == k or j in seen: continue
    seen.update((j, k)); pairs.append((j, k))
print(f"constraint space dimension = {len(pairs)} (= (p-1)/2 = {(p - 1) // 2})")
V = {r: [(C(j, r) - C(k, r)) % p for j, k in pairs] for r in range(6)}      # functional c_r on the basis vectors
print("c0 vanishes identically on the constraint space:", all(x == 0 for x in V[0]))
lam = (-(1 + L) * pow(2, -1, p)) % p
print("c2 = -(1+L)/2 * c1 identically:", all((V[2][i] - lam * V[1][i]) % p == 0 for i in range(len(pairs))))
def rank(rows):
    M = [r[:] for r in rows]; rk = 0; ncol = len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] % p), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]; inv = pow(M[rk][c], -1, p)
        M[rk] = [x * inv % p for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] % p:
                f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
print("rank{c0,c1,c2} =", rank([V[0], V[1], V[2]]), "; rank{c0,c1,c2,c3} =", rank([V[0], V[1], V[2], V[3]]),
      " -> c3 is NOT determined by c0..c2 on the constraint space" if rank([V[0], V[1], V[2], V[3]]) > rank([V[0], V[1], V[2]]) else " -> c3 determined")
mu4 = (-(3 + L) * pow(2, -1, p)) % p
print("c4 lies in span{c1, c3} on the constraint space:", rank([V[1], V[3], V[4]]) == rank([V[1], V[3]]))
# direct check of the c4 relation on the sub-space c1 = 0: solve c4 = a*c3 + b*c1 and compare a with -(3+L)/2
import itertools
i1, i2 = 0, 1
det = (V[3][i1] * V[1][i2] - V[3][i2] * V[1][i1]) % p
a = ((V[4][i1] * V[1][i2] - V[4][i2] * V[1][i1]) * pow(det, -1, p)) % p
b_ = ((V[3][i1] * V[4][i2] - V[3][i2] * V[4][i1]) * pow(det, -1, p)) % p
ok = all((V[4][i] - a * V[3][i] - b_ * V[1][i]) % p == 0 for i in range(len(pairs)))
print(f"c4 = a*c3 + b*c1 identically on all {len(pairs)} basis vectors: {ok};  a = {a} vs -(3+L)/2 = {mu4}: {a == mu4};  b = {b_}")
# Gauss periods for pricing aggregation
mu = [pow(a_, p, m) for a_ in range(1, p)]
eta = []
for t in range(p):
    c = pow(g, t, m); eta.append(sum(math.cos(2 * math.pi * (c * z % m) / m) for z in mu))
mx, mn = max(eta), min(eta)
print(f"Gauss periods over mu_(p-1) cosets: max {mx:.3f}, min {mn:.3f}, max|eta| {max(abs(mx), abs(mn)):.3f};"
      f" aggregated coefficient bound max|G| = max - min = {mx - mn:.3f} (s = -1); per-symbol bound is 2")
kappa = 2 * math.pi / (m * math.sqrt(Q))
print(f"kappa = {kappa:.6e}; extra cutoff to identify column sums exactly: ln(max|G|/2)/kappa = {math.log((mx - mn) / 2) / kappa:.4e}")
