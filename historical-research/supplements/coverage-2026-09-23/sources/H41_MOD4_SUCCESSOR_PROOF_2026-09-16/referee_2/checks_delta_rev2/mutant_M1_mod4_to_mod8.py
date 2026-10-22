#!/usr/bin/env python3
"""REVISION 2 (fail-closed; adopted from the author-side recheck patch).
H41 mod-4 successor: ALL regression checks in one file. Usage: python3 run_all_checks.py [ECDATA_OPT_MAN_DIR]
Uniform statements are proved in PROOF.md; these are regressions/controls only. Exact integer/rational arithmetic; sympy for symbolic."""
import sys, os, itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
ECD = sys.argv[1] if len(sys.argv) > 1 else None
isp = sp.isprime
def sig(n): return int(sp.divisor_sigma(n))
# ---------- 1. T1 exponent-vector congruences (symbolic, both branches) ----------
L, k = sp.symbols('l k', integer=True)
pos = [(6*L+1, 1, 1), (-3*L-2, 2, -2), (-2*L-3, 3, -1), (L+6, 6, 2), (-L-6, L, -1), (2*L+3, 2*L, 2), (3*L+2, 3*L, 1), (-6*L-1, 6*L, -2)]
neg = [(2*L-1, 1, 1), (2-L, 2, -2), (L-2, L, -1), (1-2*L, 2*L, 2)]          # L plays p on the negative branch
for vec, sign in ((pos, +1), (neg, -1)):
    for rd, d, wd in vec:
        P = sp.Poly(sp.expand((-rd*d - sign*wd).subs(L, 4*k+3)), k)
        assert all(c % 4 == 0 for c in P.all_coeffs())
print("1. T1 eta side: -r_d d = +w_d (pos) / -w_d (neg) mod 4, identically in l = 4k+3")
# ---------- 2. model, local factors, f = E mod 4, Cremona optimality ----------
def ap(b, p):   # Y^2+XY-bY = X^3-bX^2 ; a_p = p - #affine for good or multiplicative p
    if p == 2: return 2 - sum(1 for x in (0,1) for y in (0,1) if (y*y+x*y-b*y-x**3+b*x*x) % 2 == 0)
    return p - sum(1 if g == 0 else (2 if pow(g, (p-1)//2, p) == 1 else 0)
                   for g in ((4*x**3+(1-4*b)*x*x-2*b*x+b*b) % p for x in range(p)))
def reduced(b):
    b2, b4, b6 = 1-4*b, -b, b*b; c4, c6 = b2*b2-24*b4, -b2**3+36*b2*b4-216*b6
    B2 = (-c6) % 12; B2 = B2-12 if B2 > 6 else B2; B4 = (B2*B2-c4)//24; B6 = (-B2**3+36*B2*B4-c6)//216
    a1, a3 = B2 % 2, B6 % 2; return [a1, (B2-a1)//4, a3, (B4-a1*a3)//2, (B6-a3)//4]
def levels(mmax=21):
    out = []
    for m in range(3, mmax+1, 2):
        Dp = 1 + 2**(m+2)                                   # positive: D = 1 - 4r, r = -2^m
        if Dp % 3 == 0 and isp(Dp//3): out.append(("pos", m, Dp//3, 6*(Dp//3)))
        elif Dp == 513: out.append(("pos", m, 19, 114))      # exceptional m = 7, D = 27*19
        if isp(2**(m+2)-1): out.append(("neg", m, 2**(m+2)-1, 2*(2**(m+2)-1)))
    return out
M = 400
for br, m, q, N in levels():
    b = 2**(m-2) if br == "pos" else -2**(m-2); bad = ({2:1, 3:3, q:q} if br == "pos" else {2:1, q:q})
    loc = {p: ap(b, p) for p in bad}; assert loc[2] == 1 and all(loc[p] == -1 for p in bad if p != 2)
    if N >= 500000:
        print(f"2. {br} m={m} (n={m+2}) N={N}: local factors {loc}; N >= 500000, outside Cremona range, not checked further"); continue
    a = [0]*(M+1); a[1] = 1
    for p in sp.primerange(2, M+1):
        x = ap(b, p); pk, prev, cur = p, 1, x
        while pk <= M: a[pk] = cur; prev, cur = cur, x*cur-(0 if N % p == 0 else p)*prev; pk *= p
    for n in range(2, M+1):
        f = sp.factorint(n)
        if len(f) > 1: a[n] = int(sp.prod([a[p**e] for p, e in f.items()]))
    def Ecoef(n):
        mm, v = n, 1
        for p, al in bad.items():
            while mm % p == 0: mm //= p; v *= al
        return v*sig(mm)
    ok = all((a[n]-Ecoef(n)) % 8 == 0 for n in range(1, M+1))
    if not ok:
        raise RuntimeError(f"newform/Eisenstein mod-4 check failed at {N}")
    opt = "ecdata not supplied"
    if ECD:
        lo = (N//10000)*10000; tgt = str(reduced(b)).replace(" ", "")
        rows = [r.split() for r in open(os.path.join(ECD, f"opt_man.{lo:05d}-{lo+9999:05d}")) if r.split()[0] == str(N)]
        matches = [r for r in rows if r[3] == tgt]
        if len(matches) != 1:
            raise RuntimeError(f"expected one matching ecdata model at {N}, found {len(matches)}")
        mine = matches[0]
        optimal_rows = [r for r in rows if r[1] == mine[1] and r[4] == "1"]
        if mine[4] != "1" or mine[5] != "1" or len(optimal_rows) != 1:
            raise RuntimeError(f"unexpected optimality/Manin data at {N}: {mine}")
        opt = f"H41 E = {N}{mine[1]}{mine[2]} opt={mine[4]} mc={mine[5]}; optimal in class: {[r[1]+r[2] for r in rows if r[1]==mine[1] and r[4]=='1']}"
    print(f"2. {br} m={m} (n={m+2}) N={N}: local factors {loc}; f = E mod 4 for n <= {M}: {ok}; {opt}")
# ---------- 3. positive graph: Hurwitz units acting on P^1(F_3) x P^1(F_l); stabilizers, mass, Smith form ----------
def hurwitz_mats(n):
    """24 Hurwitz units as 2x2 matrices mod n (odd n), via i -> [[0,-1],[1,0]], j -> [[a,b],[b,-a]], a^2+b^2 = -1."""
    a, b = next((a, b) for a in range(n) for b in range(n) if (a*a+b*b+1) % n == 0)
    I = sp.eye(2); i = sp.Matrix([[0,-1],[1,0]]); j = sp.Matrix([[a,b],[b,-a]]); kk = i*j; inv2 = pow(2, -1, n)
    units = [s*u for s in (1,-1) for u in (I, i, j, kk)]
    units += [((s0*I + s1*i + s2*j + s3*kk)*inv2).applyfunc(lambda t: t % n) for s0, s1, s2, s3 in itertools.product((1,-1), repeat=4)]
    return [u.applyfunc(lambda t: t % n) for u in units]
def lines(n): return [(1, t) for t in range(n)] + [(0, 1)]
def act(Mt, v, n):
    w = [(Mt[0,0]*v[0]+Mt[0,1]*v[1]) % n, (Mt[1,0]*v[0]+Mt[1,1]*v[1]) % n]
    if w[0] % n: inv = pow(w[0], -1, n); return (1, (w[1]*inv) % n)
    return (0, 1)
def graph_data(l):
    U3, Ul = hurwitz_mats(3), hurwitz_mats(l)   # same abstract unit list in the same order -> simultaneous action on E[3] x E[l]
    pts = [(x, y) for x in lines(3) for y in lines(l)]
    stab = {pt: sum(1 for g3, gl in zip(U3, Ul) if act(g3, pt[0], 3) == pt[0] and act(gl, pt[1], l) == pt[1]) // 2 for pt in pts}
    seen, orbits = set(), []
    for pt in pts:
        if pt in seen: continue
        orb = {(act(g3, pt[0], 3), act(gl, pt[1], l)) for g3, gl in zip(U3, Ul)}; seen |= orb; orbits.append(stab[pt])
    return orbits
for l in (11, 19, 43):
    e = graph_data(l); mass = sum(sp.Rational(1, x) for x in e)
    assert set(e) <= {1, 3} and mass == sp.Rational(l+1, 3) and e.count(3) == (2 if l % 3 == 1 else 0)
    # regular graph: vertices 0 = C_inf, 1 = C_0, plus e-1 internal vertices per chain; reduced Laplacian (delete C_inf)
    V = 2 + sum(x-1 for x in e); Lap = sp.zeros(V, V); nxt = 2
    for x in e:
        path = [0] + list(range(nxt, nxt+x-1)) + [1]; nxt += x-1
        for u, w in zip(path, path[1:]): Lap[u,u] += 1; Lap[w,w] += 1; Lap[u,w] -= 1; Lap[w,u] -= 1
    snf = smith_normal_form(Lap[1:, 1:], domain=sp.ZZ); diag = [abs(snf[t,t]) for t in range(V-1)]
    two = 1
    for dval in diag:
        while dval % 2 == 0 and dval: dval //= 2; two *= 2
    if two != 4 or sum(1 for dv in diag if dv % 2 == 0) != 1:
        raise RuntimeError(f"component group check failed at ell={l}")
    if {(3*(l-1)//x) % 4 for x in e} != {2}:
        raise RuntimeError(f"slope residue check failed at ell={l}")
    print(f"3. positive graph l={l}: #orbits={len(e)}, thickness-3 orbits={e.count(3)}, sum 1/e = {mass} = (l+1)/3; "
          f"Phi_J 2-part order {two} (cyclic: {sum(1 for dv in diag if dv % 2 == 0) <= 1}); slopes 3(l-1)/e mod 4 = {sorted({(3*(l-1)//x) % 4 for x in e})}")
# ---------- 4. duplication identity and twist-family 2-part ----------
X, Y, r = sp.symbols('x y r')
lam = (3*X**2 + 2*(1-2*r)*X + r**2)/(2*Y); x2 = lam**2 - (1-2*r) - 2*X
diff = sp.simplify((x2 - (X**2-r**2)**2/(4*Y**2)).subs(Y**2, X**3+(1-2*r)*X**2+r**2*X))
assert sp.simplify(sp.together(x2 - (X**2-r**2)**2/(4*Y**2)).subs(Y**2, X**3+(1-2*r)*X**2+r**2*X)) == 0 or diff == 0
cnt = 0
for br, m, q0, N in levels(15):
    rr = -2**m if br == "pos" else 2**m; D = 1-4*rr
    for q in sp.primerange(5, 400):
        if q % 8 != 5 or D % q == 0 or pow(D % q, (q-1)//2, q) != q-1: continue
        Nq = q + 1 + sum((lambda g: 0 if g == 0 else (1 if pow(g, (q-1)//2, q) == 1 else -1))((x**3+(1-2*rr)*x*x+rr*rr*x) % q) for x in range(q))
        assert Nq % 4 == 0 and Nq % 8 != 0; cnt += 1
print(f"4. x(2Q) = (x^2-r^2)^2/(4y^2) verified symbolically; v_2(#E(F_q)) = 2 at all {cnt} retained-family CURVE-PRIME PAIRS (q < 400, levels m <= 15)")
# ---------- 5. BH 2.13(v) Frobenius exclusions, uniform over odd m ----------
def ap_raw(rr, p): return -sum((lambda g: 0 if g == 0 else (1 if pow(g, (p-1)//2, p) == 1 else -1))((x**3+(1-2*rr)*x*x+rr*rr*x) % p) for x in range(p))
nsq = lambda t, l: t % l != 0 and pow(t % l, (l-1)//2, l) != 1
for sgn, name in ((-1, "pos"), (1, "neg")):
    for p, excl in ((5, (3, 7)), (7, (5,))) if name == "pos" else ((5, (3, 7)), (3, (5,))):
        for rr in sorted({(sgn*pow(2, m, p)) % p for m in range(1, 25, 2)}):
            assert (1-4*rr) % p != 0; t = ap_raw(rr, p)
            assert all(nsq(t*t-4*p, l) for l in excl), (name, p, rr)
print("5. BH 2.13(v): Frobenius at 5 excludes 3,7 and at 7 (pos) / 3 (neg) excludes 5, for every odd m")

print("DATABASE_STATUS=" + ("PASS_WITH_SUPPLIED_ECDATA" if ECD else "NOT_REPLAYED_NO_ECDATA"))
