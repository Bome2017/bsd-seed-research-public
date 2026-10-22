# FG proxy, Gross-point side (k = 1). For (E, p, l): Brandt module of the definite algebra ramified at {l, inf} with
# Eichler level N; mod-p eigenfunction f of the level-raised system (T_q = a_q(E), q !| N l); for each field D: Gross
# points x_sigma of conductor p^2 (agent C's validated map, t3_gross.py), canonical anticyclotomic coordinate j(sigma)
# in the sqrt(D)-coordinate via sigma^h = rec(alpha), and D_l = sum_sigma j(sigma) f(x_sigma) mod p, S0 = sum f(x_sigma).
import sys, json, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from brandt_fast import FastBrandt
from sage.all import (Matrix as _M, BrandtModule, EllipticCurve, ZZ, QQ, GF, primes, gcd, kronecker, BinaryQF_reduced_representatives,
                      pari, Matrix, vector)
cfg = json.loads(sys.argv[1]); lab = cfg['curve']; p = ZZ(cfg['p']); l = ZZ(cfg['l']); Ds = [ZZ(d) for d in cfg['Ds']]
t00 = time.perf_counter(); E = EllipticCurve(lab); N = E.conductor(); F = GF(p)
B = BrandtModule(l, N); FB = FastBrandt(B); Is = FB.Is; h = FB.h; R = FB.R
LO = [I.left_order() for I in Is]
rec = {'curve': lab, 'p': int(p), 'l': int(l), 'num_classes': h, 't_classes_s': round(time.perf_counter() - t00, 1)}
# eigenfunction mod p (right kernel = function on classes)
V = None; used = []
import random as _rnd
_rnd.seed(20261014)
for q in primes(2, 60):
    if (N * l) % q == 0: continue
    if q <= 3 or V is None:
        T = FB.hecke(q, F)
        K = (T - F(E.ap(q))).right_kernel(); V = K if V is None else V.intersection(K)
    else:
        # V small: impose (T_q - a_q) v = 0 on sampled rows only, then verify on fresh rows
        Bv = V.basis_matrix(); d = Bv.nrows()
        rows = _rnd.sample(range(h), min(h, d + 12)); nb = FB.hecke_rows(q, rows)
        C = Matrix(F, [[sum(Bv[k][j] for j in nb[i]) - F(E.ap(q)) * Bv[k][i] for k in range(d)] for i in rows])
        ker = C.right_kernel()
        V = V.subspace([sum(c * Bv[k] for k, c in enumerate(kv)) for kv in ker.basis()])
        chk = _rnd.sample(range(h), min(h, 20)); nb2 = FB.hecke_rows(q, chk)
        for v in V.basis():
            assert all(sum(v[j] for j in nb2[i]) == F(E.ap(q)) * v[i] for i in chk), 'row-sampled kernel failed verification'
    used.append(int(q))
    if V.dimension() <= 1: break
rec['eigen_q_used'] = used; rec['eigen_dim'] = int(V.dimension())
assert V.dimension() == 1, 'mod-p eigenline not one-dimensional'
f = V.basis()[0]
rec['T_l_eigenvalue'] = None; rec['T_l_consistent'] = None
rec['t_eigen_s'] = round(time.perf_counter() - t00, 1)
tern = [O.ternary_quadratic_form(include_basis=True) for O in [I.left_order() for I in Is]]; Qalg = B.quaternion_algebra()
LO = [I.left_order() for I in Is]
identify = FB.identify
def first_optimal_embedding(n):
    for i in range(h):
        Qf, G = tern[i]; Hm = Qf.Hessian_matrix().change_ring(ZZ)
        res = pari.qfminim(pari(Hm), 2 * n)
        if int(res[0]) == 0: continue
        for col in res[2].sage().columns():
            r = [ZZ(x) for x in col]
            if gcd(r) != 1: continue
            b = sum(G[k] * r[k] for k in range(3))
            if b.reduced_norm() == n: return i, b
    return None
def gross_map(Dc, i0, beta, forms):
    t = Dc % 2; x = (t + beta) / 2; assert x in LO[i0]
    I0 = Is[i0]; out = []
    for fo in forms:
        A, Bq = fo[0], fo[1]; y = x - (Bq + t) / 2
        J = I0.scale(A, left=True) + I0.scale(y, left=True)
        J = Qalg.ideal(J.basis(), right_order=R, check=False)
        assert J.right_order() == R and J.norm() == A * I0.norm()
        out.append(identify(J))
    return out
def coprime_rep(fo):
    # an equivalent form (A',B',C') with p !| A' (same class): A' = fo(x,y) for coprime (x,y)
    a, b, c = fo[0], fo[1], fo[2]
    for (x, y) in [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (2, -1), (1, -2), (3, 1), (1, 3)]:
        A2 = a * x * x + b * x * y + c * y * y
        if A2 % p and gcd(x, y) == 1:
            # complete (x,y) to SL2: find (z,w) with x w - y z = 1
            g, w0, z0 = ZZ(x).xgcd(ZZ(y)); z, w = -z0, w0   # x*w0 + y*z0 = 1 -> x*w - y*z = 1 with z = -z0
            Mx = Matrix(ZZ, [[x, z], [y, w]]); assert Mx.det() == 1
            g2 = fo.matrix_action_right(Mx) if hasattr(fo, 'matrix_action_right') else fo * Mx
            assert g2[0] == A2 and g2.discriminant() == fo.discriminant()
            return g2
    raise RuntimeError('no coprime representative')
out_fields = []
for D in Ds:
    t0 = time.perf_counter(); c = p * p; Dc = D * c * c
    forms = BinaryQF_reduced_representatives(Dc, primitive_only=True); nf = len(forms)
    fo1 = first_optimal_embedding(-Dc); assert fo1 is not None, 'no optimal embedding'
    xs = gross_map(Dc, fo1[0], fo1[1], forms)
    # canonical anticyclotomic coordinate: sigma_a^h = rec(alpha), (alpha) = (a O_K)^h, j = sqrtD-coord of (alpha/alphabar)^(p+1)
    Kb = pari.bnfinit(pari('x^2 - (%s)' % D), 1); hK = int(Kb.bnf_get_no())
    assert hK % p, 'p | h_K'
    js = []
    for fo in forms:
        g2 = coprime_rep(fo); A2, B2 = g2[0], g2[1]
        # ideal of O_K generated by A2 and (-B2 + c*sqrt(D))/2   (x = sqrt(D) in the field polynomial)
        Iid = pari.idealhnf(Kb, A2, pari('(-(%s) + (%s)*x)/2' % (B2, c)))
        Ih = pari.idealpow(Kb, Iid, hK)
        res = pari.bnfisprincipal(Kb, Ih)
        assert all(int(z) == 0 for z in res[0]), 'not principal'
        al = pari.nfbasistoalg(Kb, res[1]).lift()           # polynomial a + b x, x = sqrt(D)
        a0 = QQ(pari.polcoef(al, 0)); b0 = QQ(pari.polcoef(al, 1))
        # u = alpha/alphabar = alpha^2 / N(alpha); compute u^(p+1) mod p^2 in Z_(p)[sqrt D]
        Nm = a0 * a0 - D * b0 * b0; mod = p * p
        def mul(u, v): return ((u[0] * v[0] + D * u[1] * v[1]) % mod, (u[0] * v[1] + u[1] * v[0]) % mod)
        inv = lambda q: ZZ(pari.Mod(q.numerator(), mod) / pari.Mod(q.denominator(), mod) if False else (q.numerator() * pow(q.denominator(), -1, mod)) % mod)
        al2 = mul((inv(a0), inv(b0)), (inv(a0), inv(b0)))
        Ninv = pow(int(inv(Nm)), -1, int(mod))
        u = ((al2[0] * Ninv) % mod, (al2[1] * Ninv) % mod)
        up = (1, 0)
        for _ in range(int(p + 1)): up = mul(up, u)
        assert up[0] % p == 1 and up[1] % p == 0, 'u^(p+1) not 1 mod p'
        jv = (ZZ(up[1]) // p) % p
        js.append(int((jv * pow(hK, -1, int(p))) % p))
    Dl = sum(F(js[k]) * f[xs[k]] for k in range(nf)); S0 = sum(f[xs[k]] for k in range(nf))
    out_fields.append({'D': int(D), 'h_K': hK, 'num_gross_points': nf, 'S0': int(S0), 'D_l': int(Dl),
                       'j_counts': {int(v): js.count(v) for v in set(js)}, 't_s': round(time.perf_counter() - t0, 1)})
    print(json.dumps(out_fields[-1]), flush=True)
rec['fields'] = out_fields; rec['isotests'] = FB.n_isotests; rec['ambiguous'] = FB.n_ambig; rec['t_total_s'] = round(time.perf_counter() - t00, 1)
print('RESULT', json.dumps(rec), flush=True)
