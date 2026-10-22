#!/usr/bin/env python3
"""Referee 1 independent regression checks (NOT proofs). Exact arithmetic except section F (database floats).
Single process, no parallelism. Usage: nice -n 19 python3 referee_checks.py [CREMONA_ECDATA_DIR]"""
import sys, os
from fractions import Fraction
from math import gcd
import sympy as sp

ECD = sys.argv[1] if len(sys.argv) > 1 else None

# ---------- A. Ligozat orders of the eta units at EVERY cusp (symbolic in l, resp. p) ----------
# N squarefree: ord_{1/c}(prod eta(dz)^{r_d}) = (N/24) sum_d gcd(c,d)^2 r_d / (c d)
L = sp.symbols('l', positive=True)
def cusp_orders(Nfac, rvec, small):
    out = {}
    for c0 in small:
        for cl in (0, 1):
            s = 0
            for (d0, dl), rr in rvec.items():
                g = gcd(c0, d0) * (L if (cl == 1 and dl == 1) else 1)
                s += g**2 * rr / ((c0 * (L if cl else 1)) * (d0 * (L if dl else 1)))
            out[(c0, cl)] = sp.factor(sp.simplify(Nfac * L * s / 24))
    return out
posr = {(1,0): 6*L+1, (2,0): -3*L-2, (3,0): -2*L-3, (6,0): L+6, (1,1): -L-6, (2,1): 2*L+3, (3,1): 3*L+2, (6,1): -6*L-1}
negr = {(1,0): 2*L-1, (2,0): 2-L, (1,1): L-2, (2,1): 1-2*L}
po = cusp_orders(6, posr, (1, 2, 3, 6)); no = cusp_orders(2, negr, (1, 2))
okA = all(sp.simplify(v - ((L**2-1) if k == (1,0) else (-(L**2-1) if k == (6,1) else 0))) == 0 for k, v in po.items())
okA &= all(sp.simplify(v - ((L**2-1)/8 if k == (1,0) else (-(L**2-1)/8 if k == (2,1) else 0))) == 0 for k, v in no.items())
print("A. Ligozat: div F = (l^2-1)([0]-[inf]) (8 cusps of X0(6l)); div F_p = ((p^2-1)/8)([0]-[inf]) (4 cusps of X0(2p)):", okA)

# ---------- B. theta = qF'/F expanded directly from the eta PRODUCT vs a_n(E) by point counts, mod 4 ----------
def count_affine(b, p):   # Y^2+XY-bY = X^3-bX^2
    return sum(1 for x in range(p) for y in range(p) if (y*y + x*y - b*y - x**3 + b*x*x) % p == 0)
def an_list(b, N, M):
    a = [0]*(M+1); a[1] = 1
    for p in sp.primerange(2, M+1):
        ap = p - count_affine(b, p); pk, prev, cur = p, 1, ap
        while pk <= M:
            a[pk] = cur; prev, cur = cur, ap*cur - (0 if N % p == 0 else p)*prev; pk *= p
    for n in range(2, M+1):
        f = sp.factorint(n)
        if len(f) > 1:
            a[n] = 1
            for p, e in f.items(): a[n] *= a[p**e]
    return a
def theta_direct(rd, M):   # theta_0 = sum r_d d/24 ; q d/dq log(1-q^k) = -sum_j k q^{kj}
    th = [Fraction(0)]*(M+1)
    th[0] = Fraction(sum(rr*d for d, rr in rd.items()), 24)
    for d, rr in rd.items():
        for k in range(1, M//d + 1):
            n0 = d*k
            for n in range(n0, M+1, n0):
                th[n] -= rr * n0
    return th
M = 200
okB = True
for m, l in ((3, 11), (5, 43), (7, 19)):
    rv = -2**m; b = -rv//4; N = 6*l
    rd = {1: 6*l+1, 2: -3*l-2, 3: -2*l-3, 6: l+6, l: -l-6, 2*l: 2*l+3, 3*l: 3*l+2, 6*l: -6*l-1}
    th = theta_direct(rd, M); a = an_list(b, N, M)
    ok = th[0] == -(l*l-1) and th[0] % 8 == 0 and all((th[n] - a[n]) % 4 == 0 for n in range(1, M+1))
    okB &= ok
    print(f"B. pos m={m} N={N}: theta_0={th[0]}, theta_1={th[1]}, theta_2={th[2]}, a_2={a[2]}, a_3={a[3]}; theta_n = +a_n mod 4 (1<=n<={M}), 8|theta_0: {ok}")
for m in (3, 5):
    p = 2**(m+2)-1; rv = 2**m; b = -rv//4; N = 2*p
    rd = {1: 2*p-1, 2: 2-p, p: p-2, 2*p: 1-2*p}
    th = theta_direct(rd, M); a = an_list(b, N, M)
    ok = th[0] == -Fraction(p*p-1, 8) and th[0] % 8 == 0 and all((th[n] + a[n]) % 4 == 0 for n in range(1, M+1))
    okB &= ok
    print(f"B. neg m={m} N={N}: theta_0={th[0]}, a_2={a[2]}, a_3={a[3]}; theta_n = -a_n mod 4 (1<=n<={M}), 8|theta_0: {ok}")

# ---------- C. vertex models of master map sec G: Delta, c4 parity, n_V, and 2-isogeny edges via Phi_2 ----------
r = sp.symbols('r')
def invariants(a1, a2, a3, a4, a6):
    b2 = a1**2 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3**2 + 4*a6
    b8 = a1**2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2
    c4 = sp.expand(b2**2 - 24*b4); Dsc = sp.factor(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
    return c4, Dsc, sp.cancel(c4**3 / Dsc)
Dq = 1 - 4*r
verts = {"E": (1, -r/2, 0, r**2/16, 0), "B": (1, r, 0, r/4, 0), "F": (1, -2*r, 0, r**2 - 3*r/2, r*(r-1)/4), "G": (1, 4*r, 0, 2*r, r/4)}
expectD = {"E": r**4*Dq/256, "B": r**2*Dq**2/16, "F": r*Dq**4/4, "G": -r*Dq/4}
J = {}; okC = True
for V, ai in verts.items():
    c4, Dsc, j = invariants(*ai); J[V] = j
    okC &= sp.simplify(Dsc - expectD[V]) == 0
    for eps in (-1, 1):
        for m in (3, 5, 7, 9, 11, 13, 15):
            rv = eps * 2**m
            okC &= all(sp.sympify(x).subs(r, rv).is_integer for x in ai)
            okC &= int(c4.subs(r, rv)) % 2 == 1
            okC &= sp.multiplicity(2, int(abs(expectD[V].subs(r, rv)))) == {"E": 4*(m-2), "B": 2*(m-2), "F": m-2, "G": m-2}[V]
X, Y = sp.symbols('X Y')
Phi2 = X**3 + Y**3 - X**2*Y**2 + 1488*(X**2*Y + X*Y**2) - 162000*(X**2 + Y**2) + 40773375*X*Y + 8748000000*(X + Y) - 157464000000000
okPhi = Phi2.subs({X: 1728, Y: 1728}) == 0 and Phi2.subs({X: 0, Y: 54000}) == 0   # self-tests: j=1728 self-2-isogeny; j=0 -> j=54000
edges = {P+Q: sp.simplify(sp.together(Phi2.subs({X: J[P], Y: J[Q]}))) == 0 for P, Q in (("E","B"), ("B","F"), ("B","G"), ("E","F"), ("E","G"), ("F","G"))}
print("C. master-map minimal models: Delta formulas, integrality, c4 odd, n_E=4(m-2), n_B=2(m-2), n_F=n_G=m-2 (eps=+-1, m=3..15):", okC)
print("C. Phi_2 self-tests:", okPhi, "; Phi_2(j_P,j_Q)=0 identically in r:", edges)

# ---------- D. BH 2.13(v): Frobenius data on the minimal model for all odd m (two full periods of 2^m mod p) ----------
def nsq(t, ell): return t % ell != 0 and pow(t % ell, (ell-1)//2, ell) != 1
okD = True; seen = set()
for eps, name, tests in ((-1, "pos", ((5, (3, 7)), (7, (5,)))), (1, "neg", ((5, (3, 7)), (3, (5,))))):
    for p, excl in tests:
        for m in range(3, 3 + 4*(p-1), 2):
            rv = eps * 2**m; b = -rv//4
            okD &= (1 - 4*rv) % p != 0 and (name == "neg" or p != 3)
            ap = p - count_affine(b, p)
            okD &= all(nsq(ap*ap - 4*p, ell) for ell in excl)
            seen.add((name, p, ap))
print("D. BH(v) Frobenius exclusions on the minimal model, all odd m:", okD, sorted(seen))

# ---------- E. twist 2-part on the retained family (both branches), q < 1200 ----------
okE = True; cntE = 0
for eps in (-1, 1):
    for m in (3, 5, 7, 11):
        rv = eps * 2**m; Dv = 1 - 4*rv
        for q in sp.primerange(5, 1200):
            if q % 8 != 5 or Dv % q == 0 or pow(Dv % q, (q-1)//2, q) != q-1: continue
            Nq = q + 1 + sum((0 if g == 0 else (1 if pow(g, (q-1)//2, q) == 1 else -1)) for g in ((x**3 + (1-2*rv)*x*x + rv*rv*x) % q for x in range(q)))
            okE &= (Nq % 4 == 0 and Nq % 8 != 0) and pow(rv % q, (q-1)//2, q) == q-1 and ((q + 1 - Nq) % 8 == 2)
            cntE += 1
print(f"E. v2(#E(F_q)) = 2, (r/q) = -1, a_q = 2 mod 8 at {cntE} retained (eps,m,q), q<1200:", okE)

# ---------- F. Cremona curvedata regression: lambda = L(E,1)/Omega_R for the ten displayed curves (floats) ----------
if ECD:
    want = ["62a1", "66b1", "114c1", "254d1", "258d1", "4098f1", "16382b1", "16386a1", "262142c1", "262146b1"]
    found = {}
    for fn in sorted(os.listdir(os.path.join(ECD, "curvedata"))):
        with open(os.path.join(ECD, "curvedata", fn)) as fh:
            for line in fh:
                if line.split(" ", 1)[0] in want:
                    t = line.split()
                    k = [i for i, x in enumerate(t) if x.count('.') == 1 and len(x) > 20][0]
                    found[t[0]] = (t[10], t[k], t[k+4])
    for lab in want:
        if lab in found:
            ainv, Om, Lv = found[lab]
            lam = sp.Float(Lv, 40) / sp.Float(Om, 40)
            print(f"F. {lab} {ainv}: Omega_R={Om[:14]} L={Lv[:14]} lambda~{sp.N(lam, 10)} 4*lambda~{sp.N(4*lam, 10)}")
        else:
            print(f"F. {lab}: not found")
