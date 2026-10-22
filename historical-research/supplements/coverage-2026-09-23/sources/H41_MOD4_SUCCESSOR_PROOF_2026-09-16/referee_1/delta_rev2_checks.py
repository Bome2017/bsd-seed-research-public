#!/usr/bin/env python3
"""Referee 1, delta review of rev 2: regression checks of NEW finite claims (not proofs). Exact arithmetic, one process.
Usage: nice -n 19 python3 delta_rev2_checks.py"""
import itertools
import sympy as sp

# ---------- F_16 = F_2[w]/(w^4+w+1); F_4 = {0,1,z,z^2} with z = w^5 ----------
MOD = 0b10011
def gmul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a & 0b10000: a ^= MOD
    return r
def gpow(a, n):
    r = 1
    for _ in range(n): r = gmul(r, a)
    return r
F16 = list(range(16))
z = gpow(0b10, 5)
F4 = [0, 1, z, gmul(z, z)]
assert all(gpow(c, 4) == c for c in F4) and len(set(F4)) == 4

# ---------- R3 "Stabilizers (explicit)": automorphisms of E: y^2 + y = x^3 over Fbar_2 ----------
def curve(x, y): return gmul(y, y) ^ y ^ gpow(x, 3)
autos = []
for a in F4[1:]:
    for s in F4:
        for t in F16:
            if gmul(t, t) ^ t != gpow(s, 6): continue
            a2 = gmul(a, a)
            # (x, y) -> (a^2 x + s^2, y + a^2 s x + t): must preserve the curve polynomial identically;
            # deg_x <= 3 and deg_y <= 2 < 16, so vanishing of the difference on F_16^2 is an identity.
            ok = all(curve(gmul(a2, x) ^ gmul(s, s), y ^ gmul(gmul(a2, s), x) ^ t) == curve(x, y) for x in F16 for y in F16)
            if ok: autos.append((a, s, t))
nA = len(autos)
t_in_F4 = all(t in F4 for _, _, t in autos)
# [-1](x, y) = (x, y + 1): the two t for fixed (a, s) differ by 1
pairs_ok = all(sum(1 for (a1, s1, t1) in autos if (a1, s1) == (a, s)) == 2 and ((a, s, t ^ 1) in autos) for a, s, t in autos)
# 3-division polynomial of y^2 + a3 y = x^3 (a1=a2=a4=a6=0, a3=1): psi_3 = 3x^4 + b2 x^3 + 3 b4 x^2 + 3 b6 x + b8 with b2=b4=b8=0, b6=1
X = sp.symbols('x')
psi3 = sp.Poly(3*X**4 + 3*X, X, modulus=2)
roots_F4 = all(gpow(c, 4) ^ c == 0 for c in F4)
# induced permutations of the four x-coordinates (= the four cyclic 3-subgroups)
perms = {tuple(F4.index(gmul(gmul(a, a), c) ^ gmul(s, s)) for c in F4) for a, s, t in autos}
stab_sizes = sorted({sum(1 for p in perms if p[i] == i) for i in range(4)})
print(f"R3 stabilizers: #automorphisms (x->a^2x+s^2, y->y+a^2sx+t) preserving y^2+y=x^3: {nA}; t in F_4: {t_in_F4}; "
      f"t-pairs differ by [-1]: {pairs_ok}; psi_3 = {psi3.as_expr()} (mod 2), roots = F_4: {roots_F4}; "
      f"effective group on 3-subgroups has order {len(perms)} (AGL_1(F_4) = A_4 has 12); point-stabilizer sizes {stab_sizes}")
assert nA == 24 and t_in_F4 and pairs_ok and len(perms) == 12 and stab_sizes == [3]

# ---------- R3 rigidity degree bound and FREE (Z/3)^x action: no alpha != 1 fixes a point of order l ----------
def hurwitz_mats(n):
    a, b = next((a, b) for a in range(n) for b in range(n) if (a*a + b*b + 1) % n == 0)
    I = sp.eye(2); i = sp.Matrix([[0, -1], [1, 0]]); j = sp.Matrix([[a, b], [b, -a]]); k = i*j; inv2 = pow(2, -1, n)
    units = [sgn*u for sgn in (1, -1) for u in (I, i, j, k)]
    units += [((s0*I + s1*i + s2*j + s3*k)*inv2) for s0, s1, s2, s3 in itertools.product((1, -1), repeat=4)]
    return [u.applyfunc(lambda e: e % n) for u in units]
free_ok = True
for l in (11, 19, 43):
    U = hurwitz_mats(l)
    assert len({tuple(u) for u in U}) == 24
    for u in U:
        if u == sp.eye(2): continue
        free_ok &= (u - sp.eye(2)).det() % l != 0          # alpha - 1 invertible on E[l]: no fixed point of order l
print(f"R3 free quotient: for l = 11, 19, 43 every Hurwitz unit alpha != 1 has det(alpha - 1) != 0 mod l (no fixed point of order l): {free_ok}; "
      f"deg(alpha-1) = 2 - Tr(alpha) <= 4 < l")
assert free_ok

# ---------- R3 counts h_3, h_1 (orbits of A_4 on P^1(F_3) x P^1(F_l)) ----------
def lines(n): return [(1, t) for t in range(n)] + [(0, 1)]
def act(M, v, n):
    w0 = (M[0, 0]*v[0] + M[0, 1]*v[1]) % n; w1 = (M[1, 0]*v[0] + M[1, 1]*v[1]) % n
    return (1, (w1*pow(w0, -1, n)) % n) if w0 % n else (0, 1)
counts_ok = True
for l in (11, 19, 43, 67, 131):
    U3, Ul = hurwitz_mats(3), hurwitz_mats(l)
    pts = [(p, q) for p in lines(3) for q in lines(l)]
    seen, orb = set(), []
    for pt in pts:
        if pt in seen: continue
        o = {(act(g3, pt[0], 3), act(gl, pt[1], l)) for g3, gl in zip(U3, Ul)}; seen |= o
        orb.append(12 // len(o))
    h3, h1 = orb.count(3), orb.count(1)
    exp_h3 = 2 if l % 3 == 1 else 0; exp_h1 = (l - 1)//3 if l % 3 == 1 else (l + 1)//3
    counts_ok &= (h3 == exp_h3 and h1 == exp_h1 and set(orb) <= {1, 3} and sp.Rational(h1) + sp.Rational(h3, 3) == sp.Rational(l + 1, 3))
    print(f"R3 counts l={l} (l mod 3 = {l % 3}): h_3={h3} (claim {exp_h3}), h_1={h1} (claim {exp_h1}), Sum 1/e_x = {sp.Rational(h1) + sp.Rational(h3, 3)}")
assert counts_ok

# ---------- sec 5 residue wording: constant Laurent coefficient after V = 2^e/U ----------
U, V = sp.symbols('U V')
for e in (1, 3):
    g = 5 + 7*U + 11*V + 13*U*V + 17*U**2*V**2 + 19*U**2*V
    lau = sp.expand(g.subs(V, 2**e/U))
    const = lau.as_coefficients_dict().get(sp.Integer(1), 0)
    assert const == 5 + 13*2**e + 17*2**(2*e)
print("sec 5: residue = sum_i a_ii 2^{e i} (checked on a sample g for e = 1, 3); UV dU/U has residue 2^e")

# ---------- I1 pointer: 4l is not a Mazur-Kenku rational cyclic isogeny degree for primes l >= 5 ----------
KENKU = set(range(1, 20)) | {21, 25, 27, 37, 43, 67, 163}
bad = [l for l in sp.primerange(5, 2000) if 4*l in KENKU]
print(f"I1 pointer: primes 5 <= l < 2000 with 4l in the Kenku list {sorted(KENKU)}: {bad} (claim: none); 4*3 = 12 is in the list (hence Frobenius for l = 3)")
assert bad == [] and 12 in KENKU

# ---------- R6: a_3 = 0 on the negative branch (r = 2^m, m odd), direct count on y^2 = x^3 + (1-2r)x^2 + r^2 x ----------
ok6 = True
for m in (3, 5, 7, 9, 11, 13, 15, 17):
    r = 2**m
    cnt = 1 + sum(1 for x in range(3) for y in range(3) if (y*y - (x**3 + (1 - 2*r)*x*x + r*r*x)) % 3 == 0)
    ok6 &= (cnt == 4)
print("R6: #E(F_3) = 4 (a_3 = 0) for negative r = 2^m, m = 3..17 odd:", ok6)
assert ok6
print("DELTA_REV2_CHECKS_OK")
