#!/usr/bin/env python3
"""Seed-specific dual certificates lambda J = v on Gamma_0(31N), with explicit multipliers.

Everything is built from the actual seed data: level 31N, a_5 = -2, a_7 = -2 (exact
point counts), alpha_0 = 57776 mod 31^4, the ten-slot jet action of
original/jet_module.py, and the Gamma-equivariance / Hecke conventions of seed_sparse.py
(validated on a genuine level-389*31 symbol by validate_presentation.py).

Each row is a named equation: (type, coset, layer, slot).  The elimination keeps the
provenance (the explicit multipliers lambda_r).  Every claimed identity is re-checked by
INDEPENDENT RECOMBINATION: the rows are rebuilt from scratch and
    v - sum_r lambda_r row_r
is recomputed column by column and compared with the reported remainder.

Layer 0 (order T^0, slot m_(0,0), mod 31): base symbol Xi_0.
Layer 1 (order T^1, slots m_(1,j), j=0,1,2, mod 31): the first-order lift Xi_1.  Its rows
contain (i) Xi_1 columns, (ii) base columns m_(0,j) (the inhomogeneous right-hand side
D_1 Xi_0, H_(q,1) Xi_0), and (iii) eigenvalue-derivative columns  b_q * m_(0,j)(k0),
alpha_1 * m_(0,j)(k0), kept as separate unknown symbols.
"""
from __future__ import annotations
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from seed_sparse import (SeedPresentation, sigma, matmul, target_functional, key_str,  # noqa: E402
                         path_inf_to)
from jet_module import COORDS  # noqa: E402
from seed_pilot31 import NFAC, ap  # noqa: E402

P = 31
ALPHA0 = 57776
X2, X1, X0, DER = 3, 2, 1, 0    # column types; pivots prefer X2 > X1 > X0 > DER
SLOT = {c: COORDS.index(c) for c in COORDS}


class ProvElim:
    """Row echelon form over F_p keeping the combination of original rows."""

    def __init__(self, p):
        self.p = p
        self.piv = {}            # col -> (row dict, provenance dict)

    def reduce(self, r, prov):
        p = self.p
        r = {k: x % p for k, x in r.items() if x % p}
        prov = dict(prov)
        out = {}
        while r:
            k = max(r)
            x = r.pop(k)
            if k in self.piv:
                row, pv = self.piv[k]
                for kk, vv in row.items():
                    if kk != k:
                        nv = (r.get(kk, 0) - x * vv) % p
                        if nv:
                            r[kk] = nv
                        else:
                            r.pop(kk, None)
                for rid, c in pv.items():
                    nv = (prov.get(rid, 0) - x * c) % p
                    if nv:
                        prov[rid] = nv
                    else:
                        prov.pop(rid, None)
            else:
                out[k] = x
        return out, prov

    def add(self, r, rid):
        red, prov = self.reduce(r, {rid: 1})
        if not red:
            return False
        k = max(red)
        inv = pow(red[k], -1, self.p)
        self.piv[k] = ({kk: v * inv % self.p for kk, v in red.items()},
                       {q: v * inv % self.p for q, v in prov.items()})
        return True


class SeedRows:
    def __init__(self, p=P, aq=None, alpha0=ALPHA0, fac=None):
        self.pres = SeedPresentation(p=p, fac=dict(fac or NFAC))
        self.p = p
        self.aq = dict(aq or {5: ap(5), 7: ap(7)})
        self.alpha0 = alpha0
        self.cid = {}

    def c(self, k):
        if k not in self.cid:
            self.cid[k] = len(self.cid)
        return self.cid[k]

    def blocks(self, rtype, key):
        """{coset: 10x10 matrix} and the eigenvalue (or None) for a row type at a coset."""
        pr = self.pres
        prec = pr.jet.precisions
        if rtype == "S":
            terms, ev = [(s, k, None, g) for s, k, g in pr.relation_S(key)], None
        elif rtype == "tau":
            terms, ev = [(s, k, None, g) for s, k, g in pr.relation_tau(key)], None
        else:
            q = int(rtype[1:])
            terms = pr.hecke_terms(q, key)
            ev = self.alpha0 if q == self.p else self.aq[q]
        out = {}
        for s, k, outer, g in terms:
            A = pr.act(sigma(g))
            if outer is not None:
                A = matmul(pr.act(outer), A, prec)
            B = out.setdefault(k, [[0] * 10 for _ in range(10)])
            for i in range(10):
                for j in range(10):
                    B[i][j] = (B[i][j] + s * A[i][j]) % prec[i]
        return out, ev

    def rows(self, rtype, key, layer):
        """Named scalar equations of the given layer (mod p)."""
        p = self.p
        B, ev = self.blocks(rtype, key)
        out = []
        if layer == 0:
            o = SLOT[(0, 0)]
            r = {}
            for k, M in B.items():
                if M[o][o] % p:
                    col = (X0, self.c(k), 0)
                    r[col] = (r.get(col, 0) + M[o][o]) % p
            if ev is not None:
                col = (X0, self.c(key), 0)
                r[col] = (r.get(col, 0) - ev) % p
            out.append(((rtype, key_str(key), 0, (0, 0)), {k: v for k, v in r.items() if v}))
            return out
        if layer == "0f":
            for j in range(4):
                o = SLOT[(0, j)]
                r = {}
                for k, M in B.items():
                    for jj in range(4):
                        x = M[o][SLOT[(0, jj)]] % p
                        if x:
                            col = (X0, self.c(k), jj)
                            r[col] = (r.get(col, 0) + x) % p
                if ev is not None:
                    col = (X0, self.c(key), j)
                    r[col] = (r.get(col, 0) - ev) % p
                out.append(((rtype, key_str(key), "0f", (0, j)), {k: v for k, v in r.items() if v}))
            return out
        if layer == 2:
            for j in range(2):
                o = SLOT[(2, j)]
                r = {}
                for k, M in B.items():
                    for (ii, jj) in COORDS:
                        x = M[o][SLOT[(ii, jj)]] % p
                        if x and ii <= 2:
                            col = ({2: X2, 1: X1, 0: X0}[ii], self.c(k), jj)
                            r[col] = (r.get(col, 0) + x) % p
                if ev is not None:
                    q = int(rtype[1:])
                    col = (X2, self.c(key), j)
                    r[col] = (r.get(col, 0) - ev) % p
                    for code in (1_000_000 + 100 * q + j, 2_000_000 + 100 * q + j):
                        col = (DER, self.c(key), code)
                        r[col] = (r.get(col, 0) - 1) % p
                out.append(((rtype, key_str(key), 2, (2, j)), {k: v for k, v in r.items() if v}))
            return out
        for j in range(3):
            o = SLOT[(1, j)]
            r = {}
            for k, M in B.items():
                for jj in range(3):
                    x = M[o][SLOT[(1, jj)]] % p
                    if x:
                        col = (X1, self.c(k), jj)
                        r[col] = (r.get(col, 0) + x) % p
                for jj in range(4):
                    x = M[o][SLOT[(0, jj)]] % p
                    if x:
                        col = (X0, self.c(k), jj)
                        r[col] = (r.get(col, 0) + x) % p
            if ev is not None:
                col = (X1, self.c(key), j)
                r[col] = (r.get(col, 0) - ev) % p
                # derivative term: - a_(q,1) * m_(0,j)(key), a separate unknown symbol
                col = (DER, self.c(key), 100 * int(rtype[1:]) + j)
                r[col] = (r.get(col, 0) - 1) % p
            out.append(((rtype, key_str(key), 1, (1, j)), {k: v for k, v in r.items() if v}))
        return out


def target_layer(sr, w, s, layer):
    """Order-0 part (slot (0,0)) mod p, or the order-1 part (slot (1,0), divided by p) mod p."""
    p = sr.p
    row = target_functional(sr.pres, w, s)
    out = {}
    for k, vec in row.items():
        if layer == 0:
            x = vec[SLOT[(0, 0)]] % p
            col = (X0, sr.c(k), 0)
        elif layer == 2:
            assert vec[SLOT[(2, 0)]] % (p * p) == 0
            x = (vec[SLOT[(2, 0)]] // (p * p)) % p
            col = (X2, sr.c(k), 0)
        else:
            x = (vec[SLOT[(1, 0)]] // p) % p      # the coefficient of m_(1,0) is p * t_w/p * ...
            assert vec[SLOT[(1, 0)]] % p == 0
            col = (X1, sr.c(k), 0)
        if x:
            out[col] = (out.get(col, 0) + x) % p
    return out


def functional_inf_to(sr, a, m):
    """Order-0 functional Xi_0({infinity, a/m}) on slot (0,0)."""
    r = {}
    for s, k, g in sr.pres.divisor_inf_to(a, m):
        col = (X0, sr.c(k), 0)
        r[col] = (r.get(col, 0) + s) % sr.p
    return {k: v for k, v in r.items() if v}


def recombine_check(builder, names, lam, v, remainder, p):
    """Rebuild rows from scratch and verify v - sum lambda row == remainder on every column."""
    fresh = {}
    for (rtype, kstr, layer, slot), key in names.items():
        for nm, row in builder.rows(rtype, key, layer):
            fresh[nm] = row
    tot = dict(v)
    for nm, c in lam.items():
        for col, x in fresh[nm].items():
            tot[col] = (tot.get(col, 0) - c * x) % p
    support = set(v)
    for nm in lam:
        support |= set(fresh[nm])
    tot = {k: x for k, x in tot.items() if x}
    rem = {k: x for k, x in remainder.items() if x % p}
    return tot == rem, len(support)


def attempt(sr, v, row_specs, nu=None, label=""):
    """Try v = sum lambda_r row_r (+ c*nu) using exactly the listed (type, coset, layer) rows."""
    p = sr.p
    E = ProvElim(p)
    names = {}
    for rtype, key, layer in row_specs:
        for nm, row in sr.rows(rtype, key, layer):
            names[nm] = key
            E.add(row, nm)
    if nu is not None:
        E.add(nu, ("nu", "", -1, None))
    red, prov = E.reduce(v, {})
    lam = {nm: (-c) % p for nm, c in prov.items()}   # v - sum lam row = red
    nu_coeff = lam.pop(("nu", "", -1, None), 0)
    x1_left = [k for k in red if k[0] in (X1, X2)]
    x0_left = [k for k in red if k[0] == X0]
    der_left = [k for k in red if k[0] == DER]
    res = {"label": label, "rows_used": len(names), "nonzero_multipliers": len(lam),
           "nu_multiplier": nu_coeff,
           "remaining_X1_columns": len(x1_left), "remaining_base_columns": len(x0_left),
           "remaining_derivative_columns": len(der_left)}
    # independent recombination (nu handled separately)
    v_adj = dict(v)
    if nu is not None and nu_coeff:
        for col, x in nu.items():
            v_adj[col] = (v_adj.get(col, 0) - nu_coeff * x) % p
    if nu is not None:
        v_adj = dict(v_adj)
    ok, ncols = recombine_check(sr, names, lam, v_adj, red, p)
    res["recombination_verified"] = ok
    res["columns_checked"] = ncols
    return res, lam, red


def divisor_level_checks(sr):
    """The U_31 identity at the divisor {inf,0}, in divisor coordinates Y_a = Xi({inf,a/31}).

    (i) sigma(adj beta_a) = [[1,-a],[0,31]] fixes every slot functional e_(n,0) of the jet
        module (u is unchanged, z^0), so the (n,0) slot of the U_31 row is
        sum_{a=0}^{30} m_(n,0)(Y_a) = sum_r alpha_r m_(n-r,0)(Y_0).
    (ii) the divisor-level coefficient of m_(n,0)(Xi(D_a)) in V_(w,s), divided by 31^n, is
        (-1)^s w^n (mod 31) for every a: uniform in a.
    Hence  sum_a m_(n,0)(Xi(D_a)) = -[(alpha_0-1) Lam_n + sum_{r>=1} alpha_r Lam_(n-r)],
    Lam_n = m_(n,0)(Xi({inf}-{0}))... with D_a = -{inf,a/31} and {inf,0} = -({0}-{inf})."""
    p = sr.p
    pr = sr.pres
    prec = pr.jet.precisions
    ok_i = True
    for a in range(p):
        A = pr.act((1, -a, 0, p))
        for n in range(4):
            o = SLOT[(n, 0)]
            row = [A[o][c] % prec[o] for c in range(10)]
            want = [1 if c == o else 0 for c in range(10)]
            if row != want:
                ok_i = False
    from math import comb
    mod = p ** 4
    ok_ii = True
    for (w, s) in [(3, 2), (3, 3), (4, 3), (4, 4)]:
        t = (pow(1 + p, w, mod) - 1) % mod
        for a in range(1, p):
            om = pow(a, p ** 3, mod)
            for n in range(4):
                c = (-1) ** s * pow(om, -s, mod) * pow(a, s, mod) * pow(t, n, mod) % mod
                if c % p ** n or (c // p ** n - (-1) ** s * w ** n) % p:
                    ok_ii = False
    return {"(i) U_31 pushes fix the (n,0) slots": ok_i,
            "(ii) (n,0) coefficients of V uniform = (-1)^s w^n mod 31": ok_ii}


def main():
    p = P
    sr = SeedRows()
    pres = sr.pres
    out = {"level": pres.P1.M, "a_q": sr.aq, "alpha0": ALPHA0, "alpha0_mod_31": ALPHA0 % p}
    k_zero = pres.divisor_inf_to(0, 1)          # {infinity, 0}
    K0 = [k for _, k, _ in k_zero]
    nu0 = functional_inf_to(sr, 0, 1)            # Xi_0({infinity,0}) = -Xi_0({0}-{infinity})
    tcos = sorted({k for a in range(1, p) for _, k, _ in pres.divisor_inf_to(a, p)}, key=key_str)
    out["cosets_of_{inf,0}"] = [key_str(k) for k in K0]
    out["divisor_level_identity_checks"] = divisor_level_checks(sr)
    out["target_cosets"] = len(tcos)

    # ---- Order 0: the U_31 row at the coset of {0,infinity} -------------------------------
    order0 = {}
    for (w, s) in [(3, 2), (3, 3), (4, 3), (4, 4)]:
        v = target_layer(sr, w, s, 0)
        specs = [("T31", k, 0) for k in K0]
        res, lam, red = attempt(sr, v, specs, nu=nu0, label=f"V_{w}{s} mod 31, order 0")
        res["identity"] = (f"V_{w}{s} == {res['nu_multiplier']} * Xi_0({{inf,0}})  (mod 31)"
                           if not red else "not closed")
        res["multipliers"] = {f"{nm[0]}@{nm[1]}": c for nm, c in lam.items()}
        order0[f"V_{w}{s}"] = res
    out["order0_certificates"] = order0

    # ---- Order 1: try to eliminate every Xi_1 column ---------------------------------------
    order1 = []
    v1 = target_layer(sr, 3, 2, 1)
    specs = [("T31", k, 1) for k in K0]
    res, lam, red = attempt(sr, v1, specs, label="V_32 order-1 slot (1,0): U_31 row at {0,inf} only")
    order1.append(res)
    t0 = time.time()
    specs2 = specs + [(rt, k, 1) for k in tcos for rt in ("S", "tau", "T5", "T31")]
    res, lam, red = attempt(sr, v1, specs2, label="radius 0: + S, tau, T5, U31 rows at all target cosets")
    res["seconds"] = round(time.time() - t0, 1)
    order1.append(res)
    # boundary: cosets whose X1 columns occur but which have no rows
    have = {key_str(k) for k in tcos} | {key_str(k) for k in K0}
    inv = {i: k for k, i in sr.cid.items()}
    left = sorted({key_str(inv[c[1]]) for c in red if c[0] == X1})
    res["unresolved_X1_cosets"] = len(left)
    res["unresolved_X1_cosets_without_rows"] = len([k for k in left if k not in have])
    # add all layer-0 (base z-moment) rows at the same cosets: reduce the base remainder
    specs3 = specs2 + [(rt, k, "0f") for k in set(tcos) | set(K0) for rt in ("S", "tau", "T5", "T31")]
    t0 = time.time()
    res3, lam3, red3 = attempt(sr, v1, specs3, label="radius 0 with base z-moment rows")
    res3["seconds"] = round(time.time() - t0, 1)
    k0ids = {sr.c(k) for k in K0}
    res3["remaining_columns_by_type"] = {
        "Xi_1 at {0,inf} coset": sorted(str(c[2]) for c in red3 if c[0] == X1 and c[1] in k0ids),
        "Xi_1 elsewhere": len([c for c in red3 if c[0] == X1 and c[1] not in k0ids]),
        "Xi_0 slots at {0,inf} coset": sorted(c[2] for c in red3 if c[0] == X0 and c[1] in k0ids),
        "Xi_0 slots at target cosets": len([c for c in red3 if c[0] == X0 and c[1] not in k0ids]),
        "eigenvalue-derivative symbols": [str(c) for c in red3 if c[0] == DER],
    }
    order1.append(res3)
    inv = {i: k for k, i in sr.cid.items()}
    def cname(c):
        kind = {X2: "Xi_2", X1: "Xi_1", X0: "Xi_0", DER: "deriv"}[c[0]]
        if c[0] == DER:
            r, rest = divmod(c[2], 1_000_000)
            q, j = divmod(rest, 100)
            r = r or 1
            return f"a_({q},{r})*m_({2 - r if c[2] >= 1_000_000 else 0},{j})[{key_str(inv[c[1]])}]"
        slot = ({X2: 2, X1: 1, X0: 0}[c[0]], c[2])
        return f"{kind} m_{slot}[{key_str(inv[c[1]])}]"
    with open(os.path.join(HERE, "CERT_ORDER1_RESIDUAL.json"), "w") as f:
        json.dump({"statement": "V_32 order-1 coefficient (slot (1,0) part, /31) == sum of the listed "
                   "remainder terms (mod 31) for every solution of the listed rows",
                   "rows": res3["rows_used"], "multipliers": {str(k): c for k, c in lam3.items()},
                   "remainder": {cname(c): x for c, x in sorted(red3.items())}}, f, indent=0)
    out["order1_attempts"] = order1
    v2 = target_layer(sr, 3, 2, 2)
    specs4 = [("T31", k, 2) for k in K0] + [(rt, k, 2) for k in tcos for rt in ("S", "tau", "T5", "T31")]
    t0 = time.time()
    res4, lam4, red4 = attempt(sr, v2, specs4, label="V_32 order-2 slot (2,0), radius 0")
    res4["seconds"] = round(time.time() - t0, 1)
    res4["remaining_columns_by_type"] = {
        "Xi_2 at {0,inf} coset": sorted(str(c[2]) for c in red4 if c[0] == X2 and c[1] in k0ids),
        "Xi_2 elsewhere": len([c for c in red4 if c[0] == X2 and c[1] not in k0ids]),
        "Xi_1 slots (retained RHS)": len([c for c in red4 if c[0] == X1]),
        "Xi_0 slots (retained RHS)": len([c for c in red4 if c[0] == X0]),
        "eigenvalue-derivative symbols": [cname(c) for c in red4 if c[0] == DER],
    }
    out["order2_attempt"] = res4
    with open(os.path.join(HERE, "CERT_ORDER2_RESIDUAL.json"), "w") as f:
        json.dump({"statement": "V_32 order-2 coefficient (slot (2,0) part, /31^2) == listed remainder (mod 31)",
                   "rows": res4["rows_used"], "multipliers": {str(k): c for k, c in lam4.items()},
                   "remainder": {cname(c): x for c, x in sorted(red4.items())}}, f, indent=0)
    with open(os.path.join(HERE, "CERT_ORDER0_MULTIPLIERS.json"), "w") as f:
        json.dump(order0, f, indent=1)
    return out


if __name__ == "__main__":
    print(json.dumps(main(), indent=1, default=str))
