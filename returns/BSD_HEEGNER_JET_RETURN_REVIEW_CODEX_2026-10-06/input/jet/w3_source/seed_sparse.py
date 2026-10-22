#!/usr/bin/env python3
"""Seed-level sparse construction attempt at p=31 on Gamma_0(31N).

Conventions (derived in SPARSE_ATTEMPT.md, section 1):
  * Coset generators D_i = g_i{0,infinity}, g_i in SL_2(Z) a fixed lift of the Manin
    symbol (c:d) in P^1(Z/31N).
  * Gamma-equivariance of the measure-valued family symbol
        Xi(gamma D) = sigma(gamma)_* Xi(D),   sigma([[a,b],[c,d]]) = [[d,b],[c,a]],
    pushforward along (x,y) -> (x,y) sigma(gamma).  This is forced by the classical
    integral I_g(D;X,Y)=int g(z)(X-zY)^w dz and gives, after specialisation at <x>^w,
    the character omega(d)^(-w): weight five carries omega^(-3), weight six omega^(-4).
  * Hecke: (T_q Xi)(D) = sum_beta sigma(adj beta)_* Xi(beta D),
    beta in {[[1,j],[0,q]] (0<=j<q), [[q,0],[0,1]] (q not dividing 31N)};
    U_31 uses beta=[[1,j],[0,31]] only.  sigma(adj beta) lies in Sigma_0(31).
Jet coordinates: the ten slots m_(i,j) of original/jet_module.py (precision p^(4-i-j)).
"""
from __future__ import annotations
import hashlib
import json
import os
import sys
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "original"))
from jet_module import JetModule, COORDS  # noqa: E402
from seed_pilot31 import N, NFAC, ap  # noqa: E402

P = 31


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


def crt(res):
    x, m = 0, 1
    for r, mm in res:
        g, s, t = egcd(m, mm)
        x = (x + (r - x) * s % mm * m) % (m * mm)
        m *= mm
    return x


class P1Level:
    def __init__(self, fac):
        self.fac = dict(sorted(fac.items()))
        self.M = 1
        for l, e in self.fac.items():
            self.M *= l ** e

    def key(self, c, d):
        out = []
        for l, e in self.fac.items():
            m = l ** e
            cc, dd = c % m, d % m
            if dd % l:
                out.append((cc * pow(dd, -1, m) % m, 1))
            elif cc % l:
                out.append((1, dd * pow(cc, -1, m) % m))
            else:
                raise ValueError("not in P^1")
        return tuple(out)

    def lift(self, key):
        """A matrix g in SL_2(Z) whose bottom row represents key."""
        mods = [l ** e for l, e in self.fac.items()]
        c = crt([(k[0], m) for k, m in zip(key, mods)])
        d = crt([(k[1], m) for k, m in zip(key, mods)])
        if c == 0:
            c = self.M
        while gcd(c, d) != 1:
            d += self.M
        g, x, y = egcd(d, c)          # x d + y c = 1
        a, b = x, -y                  # a d - b c = 1
        assert a * d - b * c == 1
        return (a, b, c, d)

    def gamma_and_key(self, g):
        a, b, c, d = g
        k = self.key(c, d)
        r = self.lift(k)
        ra, rb, rc, rd = r
        inv = (rd, -rb, -rc, ra)
        gm = mul(g, inv)
        assert gm[2] % self.M == 0 and gm[0] * gm[3] - gm[1] * gm[2] == 1
        return k, gm


def mul(g, h):
    a, b, c, d = g
    e, f, k, l = h
    return (a * e + b * k, a * f + b * l, c * e + d * k, c * f + d * l)


def sigma(g):
    a, b, c, d = g
    return (d, b, c, a)


def adj(g):
    a, b, c, d = g
    return (d, -b, -c, a)


def path_inf_to(a, m):
    """{infinity, a/m} = sum_k g_k{0,infinity}, g_k in SL_2(Z) (convergent matrices)."""
    pk2, qk2, pk1, qk1 = 0, 1, 1, 0
    x, y = a, m
    out = []
    while y:
        t = x // y
        pk, qk = t * pk1 + pk2, t * qk1 + qk2
        g = (pk, pk1, qk, qk1)
        if pk * qk1 - pk1 * qk != 1:
            g = (pk, -pk1, qk, -qk1)
        out.append(g)
        pk2, qk2, pk1, qk1 = pk1, qk1, pk, qk
        x, y = y, x - t * y
    return out


def path_between(r1, r2):
    """{r1, r2} = {inf, r2} - {inf, r1}; r = (num, den) with den>0, or None for infinity."""
    terms = []
    if r2 is not None:
        terms += [(+1, g) for g in path_inf_to(*r2)]
    if r1 is not None:
        terms += [(-1, g) for g in path_inf_to(*r1)]
    return terms


def apply_to_cusp(g, r):
    a, b, c, d = g
    if r is None:
        num, den = a, c
    else:
        x, y = r
        num, den = a * x + b * y, c * x + d * y
    if den == 0:
        return None
    if den < 0:
        num, den = -num, -den
    h = gcd(num, den)
    return (num // h, den // h)


class SeedPresentation:
    def __init__(self, p=P, fac=None):
        self.p = p
        fac = dict(fac or NFAC)
        fac[p] = fac.get(p, 0) + 1
        self.P1 = P1Level(fac)
        self.jet = JetModule(p)
        self._act = {}

    def act(self, g):
        """10x10 jet matrix of the Sigma_0(p) element g (pushforward along (x,y)g)."""
        p4 = self.p ** 5
        key = tuple(x % p4 for x in g)
        if key not in self._act:
            self._act[key] = self.jet.action(g)
        return self._act[key]

    def decompose(self, terms):
        """sum sign*g{0,inf} -> list (sign, coset key, gamma) with g = gamma g_key."""
        out = []
        for s, g in terms:
            k, gm = self.P1.gamma_and_key(g)
            out.append((s, k, gm))
        return out

    def divisor_inf_to(self, a, m):
        return self.decompose([(1, g) for g in path_inf_to(a, m)])

    def relation_S(self, key):
        g = self.P1.lift(key)
        gs = mul(g, (0, -1, 1, 0))
        k2, gm = self.P1.gamma_and_key(gs)
        return [(1, key, (1, 0, 0, 1)), (1, k2, gm)]

    def relation_tau(self, key):
        g = self.P1.lift(key)
        out = [(1, key, (1, 0, 0, 1))]
        t = (0, -1, 1, -1)
        h = g
        for _ in range(2):
            h = mul(h, t)
            k2, gm = self.P1.gamma_and_key(h)
            out.append((1, k2, gm))
        return out

    def hecke_terms(self, q, key):
        """(T_q Xi)(D_key) = sum (sign, coset, outer, gamma): outer=sigma(adj beta)."""
        g = self.P1.lift(key)
        betas = [(1, j, 0, q) for j in range(q)]
        if self.P1.M % q:
            betas.append((q, 0, 0, 1))
        out = []
        for be in betas:
            bg = mul(be, g)
            r1 = apply_to_cusp(bg, (0, 1))
            r2 = apply_to_cusp(bg, None)
            for s, k, gm in self.decompose(path_between(r1, r2)):
                out.append((s, k, sigma(adj(be)), gm))
        return out


def jet_row(pres, terms_with_outer, mod_slots=True):
    """Combine terms into {coset: 10x10 matrix} acting on Xi(D_coset)."""
    p = pres.p
    prec = pres.jet.precisions
    rows = {}
    for t in terms_with_outer:
        if len(t) == 3:
            s, k, gm = t
            A = pres.act(sigma(gm))
        else:
            s, k, outer, gm = t
            A = matmul(pres.act(outer), pres.act(sigma(gm)), prec)
        B = rows.setdefault(k, [[0] * 10 for _ in range(10)])
        for i in range(10):
            for j in range(10):
                B[i][j] = (B[i][j] + s * A[i][j]) % prec[i]
    return rows


def matmul(A, B, prec):
    return [[sum(A[i][k] * B[k][j] for k in range(10)) % prec[i] for j in range(10)] for i in range(10)]


def omega(a, p, k):
    return pow(a, p ** (k - 1), p ** k)


def target_functional(pres, w, s):
    """V_(w,s) of FINITE_MOMENT_MODULE (F) as an exact row {coset: 10 coefficients mod p^4}.

    D_a = {infinity}-{a/p} is the path from a/p to infinity = -{infinity, a/p}."""
    p = pres.p
    mod = p ** 4
    t = (pow(1 + p, w, mod) - 1) % mod
    from math import comb
    row = {}
    for a in range(1, p):
        coef_slots = [0] * 10   # functional on Xi(D_a) moments
        for h in range(min(s, 3) + 1):
            for i in range(4 - h):
                idx = COORDS.index((i, h))
                c = pow(omega(a, p, 4), -s, mod) * comb(s, h) * pow(a, s - h, mod) * pow(-p, h, mod) * pow(t, i, mod)
                coef_slots[idx] = (coef_slots[idx] + c * (-1) ** s) % mod
        for sg, k, gm in pres.divisor_inf_to(a, p):
            A = pres.act(sigma(gm))
            vec = row.setdefault(k, [0] * 10)
            for col in range(10):
                vec[col] = (vec[col] - sg * sum(coef_slots[r] * A[r][col] for r in range(10))) % mod
    return row


def key_str(k):
    return ";".join(f"{c}:{d}" for c, d in k)


def main():
    pres = SeedPresentation()
    out = {"level_M": pres.P1.M, "p": pres.p}
    # 1. target functionals with exact coset identifiers
    tf = {}
    for (w, s) in [(3, 2), (3, 3), (4, 3), (4, 4)]:
        row = target_functional(pres, w, s)
        tf[f"V_{w}{s}"] = {key_str(k): v for k, v in row.items()}
    cos = sorted({c for r in tf.values() for c in r})
    out["target"] = {
        "cosets_in_support": len(cos),
        "per_functional_support": {k: len(v) for k, v in tf.items()},
        "sha256": hashlib.sha256(json.dumps(tf, sort_keys=True).encode()).hexdigest(),
    }
    with open(os.path.join(HERE, "TARGET_FUNCTIONALS.json"), "w") as f:
        json.dump({"convention": "row[coset] . Xi(D_coset) summed = V mod 31^4; coset key = "
                   "canonical (c:d) per prime power of 31N in the order " + str(list(pres.P1.fac)),
                   "functionals": tf}, f, indent=0, sort_keys=True)
    # 2. one relation and one Hecke row at the first target coset, with first-order RHS
    k0 = pres.divisor_inf_to(1, pres.p)[0][1]
    S = jet_row(pres, pres.relation_S(k0))
    Tq = jet_row(pres, pres.hecke_terms(5, k0))
    out["example_rows_at_coset"] = key_str(k0)
    out["S_relation_cosets"] = len(S)
    out["T5_row_cosets"] = len(Tq)
    # first-order part: slots (1,j) receive D_1-terms from slots (0,j') of every coset
    i1 = [COORDS.index((1, j)) for j in range(3)]
    i0 = [COORDS.index((0, j)) for j in range(4)]
    rhs = {}
    for name, R in (("S", S), ("T5", Tq)):
        terms = []
        for k, B in R.items():
            for r in i1:
                for c in i0:
                    if B[r][c]:
                        terms.append({"coset": key_str(k), "out_slot": COORDS[r], "base_slot": COORDS[c],
                                      "coeff_mod_p^(3-j)": B[r][c]})
        rhs[name] = terms
    out["first_order_rhs_terms"] = {k: len(v) for k, v in rhs.items()}
    out["first_order_rhs_required_base_evaluations"] = sorted(
        {(t["coset"], str(t["base_slot"])) for v in rhs.values() for t in v}).__len__()
    with open(os.path.join(HERE, "FIRST_ORDER_RHS.json"), "w") as f:
        json.dump({"coset": key_str(k0),
                   "equation": "sum_k B_k^(1<-1) Xi_1(D_k) - a_(q,0) Xi_1(D_0) - b_q Xi_0(D_0) "
                               "= - sum_k B_k^(1<-0) Xi_0(D_k)   (T5 row; S row has no eigenvalue terms)",
                   "unknown_eigenvalue_derivatives": ["b_5 = a_(5,1)"],
                   "rhs_terms": rhs}, f, indent=0)
    return out


if __name__ == "__main__":
    print(json.dumps(main(), indent=1))
