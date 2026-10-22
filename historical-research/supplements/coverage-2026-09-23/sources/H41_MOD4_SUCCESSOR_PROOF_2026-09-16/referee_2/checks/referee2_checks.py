#!/usr/bin/env python3
"""Referee 2 independent regression checks (exact arithmetic). Not part of any proof."""
from fractions import Fraction as Fr
from math import gcd
import sympy as sp

def divisors(n): return [d for d in range(1, n+1) if n % d == 0]

# ---------- A. Ligozat divisors of the eta units ----------
def eta_orders(N, r):
    # order at cusp 1/c (c | N, squarefree N) in the local parameter (Ligozat)
    out = {}
    for c in divisors(N):
        s = Fr(0)
        for d, rd in r.items():
            s += Fr(gcd(c, d)**2 * rd, gcd(c, N//c) * c * d)
        out[c] = s * N / 24
    return out
def pos_r(l):
    return {1: 6*l+1, 2: -3*l-2, 3: -2*l-3, 6: l+6, l: -l-6, 2*l: 2*l+3, 3*l: 3*l+2, 6*l: -6*l-1}
def neg_r(p):
    return {1: 2*p-1, 2: 2-p, p: p-2, 2*p: 1-2*p}
print("A. eta-unit divisors (Ligozat); cusp 1/c, c=N is inf, c=1 is 0")
for kind, par in (("pos", 11), ("pos", 19), ("pos", 43), ("pos", 683), ("pos", 2731), ("neg", 31), ("neg", 127), ("neg", 8191)):
    N = 6*par if kind == "pos" else 2*par
    r = pos_r(par) if kind == "pos" else neg_r(par)
    k = par*par-1 if kind == "pos" else (par*par-1)//8
    o = eta_orders(N, r)
    assert sum(r.values()) == 0
    sq = 1
    ok_sq = all(sum(e for d, e in r.items() if d % q == 0) % 2 == 0 for q in sp.primefactors(N))
    ok = all(v.denominator == 1 for v in o.values()) and o[N] == -k and o[1] == k and all(o[c] == 0 for c in o if c not in (1, N))
    print(f"   {kind} param={par} N={N}: orders at inf={o[N]}, at 0={o[1]}, others zero={all(o[c]==0 for c in o if c not in (1,N))}; "
          f"div=k([0]-[inf]) with k={k}: {ok}; prod d^r_d square: {ok_sq}; antisymmetry r_(N/d)=-r_d: {all(r[N//d]==-r[d] for d in r)}")
    assert ok and ok_sq

# ---------- B. T1 congruence from power series vs point counts ----------
def eta_quotient_logder(r, M):
    # theta = q F'/F; F = q^{t0} prod (1-q^{dk})^{r_d}; compute via log-derivative series directly (integer)
    th = [0]*(M+1)
    th[0] = Fr(sum(d*e for d, e in r.items()), 24)
    for d, e in r.items():
        # q d/dq log (1-q^{dk})^{e} = -e * sum_k dk q^{dk}/(1-q^{dk})
        for k in range(1, M//d+1):
            for j in range(1, M//(d*k)+1):
                th[d*k*j] += -e*d*k
    return th
def ap_long(a, p):  # y^2 = x^3 + A x^2 + B x with (A,B) ints, odd p good or multiplicative
    A, B = a
    cnt = 1
    for x in range(p):
        g = (x**3 + A*x*x + B*x) % p
        cnt += 1 if g == 0 else (2 if pow(g, (p-1)//2, p) == 1 else 0)
    return p + 1 - cnt
def ap_at2(b):  # minimal model Y^2+XY-bY = X^3-bX^2, b even -> reduction Y^2+XY = X^3 split node
    # count affine points mod 2 on nonsingular part plus infinity: #E_ns(F2) = 2 - a_2 ... use direct: a_2 = 2+1-#E(F_2) incl. singular? use standard: a_p = p - #affine(all) for mult.
    cnt = sum(1 for x in (0, 1) for y in (0, 1) if (y*y + x*y - b*y - x**3 + b*x*x) % 2 == 0)
    return 2 - cnt
print("B. T1: theta_n (power series) vs a_n(E) (point counts, independent code) mod 4")
for kind, m in (("pos", 3), ("neg", 3), ("pos", 5), ("neg", 5), ("pos", 7)):
    rr = -2**m if kind == "pos" else 2**m
    D = 1 - 4*rr
    if kind == "pos":
        l = 19 if m == 7 else D//3; N = 6*l; r = pos_r(l); sgn = +1
    else:
        p = -D; N = 2*p; r = neg_r(p); sgn = -1
    M = 150
    th = eta_quotient_logder(r, M)
    a = [0]*(M+1); a[1] = 1
    b = -rr//4
    for p_ in sp.primerange(2, M+1):
        ap = ap_at2(b) if p_ == 2 else ap_long((1-2*rr, rr*rr), p_)
        bad = (N % p_ == 0)
        pk, prev, cur = p_, 1, ap
        while pk <= M:
            a[pk] = cur
            prev, cur = cur, ap*cur - (0 if bad else p_)*prev
            pk *= p_
    for n in range(2, M+1):
        f = sp.factorint(n)
        if len(f) > 1:
            v = 1
            for q, e in f.items(): v *= a[q**e]
            a[n] = v
    good = all((th[n] - sgn*a[n]) % 4 == 0 for n in range(1, M+1))
    print(f"   {kind} m={m} N={N}: theta_0={th[0]} (mod 8 = {int(th[0]) % 8}); theta_n == {'+' if sgn>0 else '-'}a_n mod 4 for 1<=n<={M}: {good}; "
          f"a_2={a[2]}, bad a_p={[a[q] for q in sp.primefactors(N) if q!=2]}")
    assert good and th[0].denominator == 1 and int(th[0]) % 8 == 0

# ---------- C. I2 / R8: minimal models of the four vertices, symbolic in r ----------
print("C. I2/R8: vertex models (symbolic in r)")
R = sp.symbols('r')
def invariants(a1, a2, a3, a4, a6):
    b2 = a1**2 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3**2 + 4*a6
    b8 = a1**2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2
    c4 = b2**2 - 24*b4; c6 = -b2**3 + 36*b2*b4 - 216*b6
    Dl = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    return sp.expand(c4), sp.expand(c6), sp.factor(sp.expand(Dl))
Dd = 1 - 4*R
disp = {"E": (0, 1-2*R, 0, R**2, 0), "B": (0, -(1+Dd), 0, Dd, 0), "F": (0, -2-8*R, 0, Dd**2, 0), "G": (0, -2+16*R, 0, 1, 0)}
mini = {"E": (1, -R/2, 0, R**2/16, 0), "B": (1, R, 0, R/4, 0), "F": (1, -2*R, 0, R**2-3*R/2, R*(R-1)/4), "G": (1, 4*R, 0, 2*R, R/4)}
claimedD = {"E": R**4*Dd/256, "B": R**2*Dd**2/16, "F": R*Dd**4/4, "G": -R*Dd/4}
for V in "EBFG":
    c4d, c6d, Dld = invariants(*disp[V]); c4m, c6m, Dlm = invariants(*mini[V])
    # isomorphic over Q iff c4d = u^4 c4m, c6d = u^6 c6m for some u in Q^*; test u = 2 (standard for these families)
    u = 2
    iso = sp.simplify(c4d - u**4*c4m) == 0 and sp.simplify(c6d - u**6*c6m) == 0
    dmatch = sp.simplify(Dlm - claimedD[V]) == 0
    print(f"   {V}: displayed ~= claimed minimal model via u=2: {iso}; Delta(min) == claimed {claimedD[V]}: {dmatch}; c4(min) = {sp.factor(c4m)}")
    assert iso and dmatch
# the displayed curves are 2-isogenous as stated (E->B via (0,0); B->F via (1,0); B->G via (D,0))
def isog2(A, Bc):  # y^2 = x^3 + A x^2 + B x  ->  Y^2 = X^3 - 2A X^2 + (A^2-4B) X
    return (sp.expand(-2*A), sp.expand(A**2 - 4*Bc))
def shift(A, Bc, C, x0):  # y^2 = x^3 + A x^2 + Bc x + C, translate x -> x + x0
    X = sp.symbols('X'); poly = sp.expand((X+x0)**3 + A*(X+x0)**2 + Bc*(X+x0) + C)
    co = sp.Poly(poly, X).all_coeffs(); return co  # [1, A', B', C']
EB = isog2(1-2*R, R**2)
print(f"   E->B isogenous curve (A,B) = {EB}; B displayed (A,B) = {(sp.expand(-(1+Dd)), sp.expand(Dd))}: {sp.simplify(EB[0]+(1+Dd))==0 and sp.simplify(EB[1]-Dd)==0}")
c1 = shift(-(1+Dd), Dd, 0, 1); assert sp.simplify(c1[3]) == 0
BF = isog2(c1[1], c1[2]); c2 = shift(-(1+Dd), Dd, 0, Dd); assert sp.simplify(c2[3]) == 0
BG = isog2(c2[1], c2[2])
print(f"   B->F via (1,0): {sp.simplify(BF[0]-(-2-8*R))==0 and sp.simplify(BF[1]-Dd**2)==0}; B->G via (D,0): {sp.simplify(BG[0]-(-2+16*R))==0 and sp.simplify(BG[1]-1)==0}")
for sgn in (-1, 1):
    for m in (3, 5, 7, 9, 11, 13, 15):
        rv = sgn*2**m
        vals = {}
        for V in "EBFG":
            coeffs = [sp.nsimplify(sp.sympify(c).subs(R, rv)) for c in mini[V]]
            assert all(sp.Integer(c) == c for c in coeffs), (V, coeffs)
            c4m, c6m, Dlm = invariants(*[int(c) for c in coeffs])
            v2 = sp.multiplicity(2, int(Dlm)); vals[V] = v2
            assert int(c4m) % 2 == 1
        assert vals == {"E": 4*(m-2), "B": 2*(m-2), "F": m-2, "G": m-2}, (sgn, m, vals)
print("   integral minimal models with odd c4 and ord_2 Delta = (4,2,1,1)*(m-2) for r = +-2^m, m = 3..15 odd: OK")

# ---------- D. BH 2.13 local data ----------
print("D. BH 2.13 local data")
for sgn, name in ((-1, "pos"), (1, "neg")):
    for mod in (3, 5, 7):
        rs = sorted({(sgn*pow(2, m, mod)) % mod for m in range(1, 40, 2)})
        for rv in rs:
            Dm = (1 - 4*rv) % mod
            if Dm == 0: print(f"   {name}: r = {rv} mod {mod}: BAD REDUCTION (D = 0 mod {mod})"); continue
            print(f"   {name}: r = {rv} mod {mod}: a_{mod} = {ap_long(((1-2*rv) % mod, (rv*rv) % mod), mod)}")

# ---------- E. modular-degree consistency with u_x = 2 mod 4 (pos) / u_x odd (neg) via CS Thm 6.1: <u,u> = n0 * deg ----------
print("E. CS Theorem 6.1 consistency: sum e_x u_x^2 = n0*deg with the claimed residues of u_x")
data = {  # Cremona curvedata 'degree' column
    ("neg", 3): 2, ("pos", 3): 4, ("pos", 7): 60, ("neg", 5): 24, ("pos", 5): 60, ("pos", 9): 7980,
    ("neg", 11): 91008, ("pos", 11): 145332, ("neg", 15): 15060864, ("pos", 15): 35702628}
for (kind, m), deg in sorted(data.items(), key=lambda t: (t[0][1], t[0][0])):
    n0 = 4*(m-2)
    if kind == "pos":
        l = 19 if m == 7 else (1 + 2**(m+2))//3
        n3 = 2 if l % 3 == 1 else 0; n1 = (l+1)//3 - n3//3 if False else None
        # sum 1/e = n1 + n3/3 = (l+1)/3  ->  n1 = (l+1)/3 - n3/3
        n1 = Fr(l+1, 3) - Fr(n3, 3); assert n1.denominator == 1; n1 = int(n1)
        sum_e = n1 + 3*n3
        # u = 2w, w_x odd => sum e_x u_x^2 = 4 sum e_x w_x^2 = 4 sum e_x mod 32
        lhs_mod = (4*sum_e) % 32; rhs = (n0*deg) % 32
        print(f"   pos m={m} l={l}: #nodes={n1+n3}, n3={n3}, sum e_x={sum_e}; n0*deg mod 32 = {rhs}, required 4*sum e mod 32 = {lhs_mod}: {rhs == lhs_mod}; deg mod 8 = {deg % 8}")
    else:
        n3 = 2; n1 = (2**m - 2)//3; sum_e = n1 + 3*n3
        lhs_mod = sum_e % 8; rhs = (n0*deg) % 8
        print(f"   neg m={m}: #nodes={n1+n3}, sum e_x={sum_e}; n0*deg mod 8 = {rhs}, required sum e mod 8 = {lhs_mod}: {rhs == lhs_mod}")
