#!/usr/bin/env python3
"""Validate the Gamma_0(Mp) presentation code of seed_sparse.py on a genuine symbol.

Calibration (development tool, not the seed): f = 389a1, p = 31, level 389*31.
phi = primitive plus eigensymbol of level 389 (exact, from Manin relations);
phi_alpha({r,s}) = phi({r,s}) - alpha^(-1) phi({31 r, 31 s})   (31-stabilisation).
Checks, for every sampled coset of P^1(Z/12059): S-relation, tau-relation, T_5 row
with a_5, U_31 row with alpha mod 31^4, all through seed_sparse's decomposition code.
Also checks a deliberately wrong eigenvalue is rejected.
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from seed_sparse import SeedPresentation, path_between, apply_to_cusp
from weight2_jet import plus_eigensymbol, unit_root
from modsym2 import ap_count

p = 31; mod = p ** 4
M389, aq, plus = plus_eigensymbol(389, (0, 1, 1, -2, 0))
a31 = ap_count((0, 1, 1, -2, 0), 31); alpha = unit_root(a31, p, 4); ai = pow(alpha, -1, mod)
a5 = ap_count((0, 1, 1, -2, 0), 5)

def phi_inf(r):
    return 0 if r is None else M389.symbol_inf_to(plus, r[0], r[1])

def phi_path(r1, r2):
    return phi_inf(r2) - phi_inf(r1)

def scale(r):
    return None if r is None else apply_to_cusp((p, 0, 0, 1), r)

def phi_alpha_path(r1, r2):
    return (phi_path(r1, r2) - ai * phi_path(scale(r1), scale(r2))) % mod

def X(g):  # value on g{0,inf}
    return phi_alpha_path(apply_to_cusp(g, (0, 1)), apply_to_cusp(g, None))

pres = SeedPresentation(p=p, fac={389: 1})
rng = random.Random(7)
keys = []
for _ in range(40):
    c, d = rng.randrange(pres.P1.M), rng.randrange(pres.P1.M)
    try:
        keys.append(pres.P1.key(c, d))
    except ValueError:
        pass
res = {"S": True, "tau": True, "T5": True, "U31": True, "wrong_eigenvalue_rejected": True}
for k in keys:
    g = pres.P1.lift(k)
    val = lambda kk: X(pres.P1.lift(kk))
    if sum(s * val(kk) for s, kk, gm in pres.relation_S(k)) % mod: res["S"] = False
    if sum(s * val(kk) for s, kk, gm in pres.relation_tau(k)) % mod: res["tau"] = False
    t5 = sum(s * val(kk) for s, kk, o, gm in pres.hecke_terms(5, k))
    if (t5 - a5 * val(k)) % mod: res["T5"] = False
    u = sum(s * val(kk) for s, kk, o, gm in pres.hecke_terms(31, k))
    if (u - alpha * val(k)) % mod: res["U31"] = False
wrong = [k for k in keys if (sum(s * X(pres.P1.lift(kk)) for s, kk, o, gm in pres.hecke_terms(5, k)) - (a5 + 1) * X(pres.P1.lift(k))) % mod]
res["wrong_eigenvalue_rejected"] = len(wrong) > 0
res["cosets_tested"] = len(keys)
print(json.dumps(res, indent=1))
