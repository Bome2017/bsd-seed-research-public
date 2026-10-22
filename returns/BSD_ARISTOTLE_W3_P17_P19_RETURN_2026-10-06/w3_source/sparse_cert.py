#!/usr/bin/env python3
"""Order-0 sparse dual certificates  lambda J = v  over F_p, on growing supports.

Rows of J (all exact, on Manin symbols (c:d) in P^1(Z/M), weight two):
  S-row      x_i + x_{iS}                       = 0
  tau-row    x_i + x_{i tau} + x_{i tau^2}      = 0
  star-row   x_i - x_{i*}                       = 0      (plus part)
  Hecke-row  sum_{h in Merel(q)} x_{ih} - a_q x_i = 0    (q in Q, q prime to M)
  nu-row     x_{i0}                             = 1      (normalisation)
Target v = sum of indicator rows of the Manin symbols of {infinity, a/m}.

lambda J = v  (exact, with every column cancelled except those of v)  computes
v(Phi) = lambda_nu for every Phi satisfying the rows.  Support R(r): all rows
attached to symbols within graph distance r of the target/nu symbols.
Duality: no certificate on R  <=>  there is an assignment on the touched columns
satisfying every row of R with nu=1 on which v takes two different values
(a ball-local "fake" symbol).  The unresolved boundary columns are recorded.
"""
from __future__ import annotations
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modsym2 import heilbronn_merel, is_prime, ap_count  # noqa: E402


class P1:
    def __init__(self, M):
        assert is_prime(M)
        self.M = M
        self.n = M + 1

    def idx(self, c, d):
        M = self.M
        c %= M
        d %= M
        if c == 0:
            return M
        return d * pow(c, -1, M) % M

    def rep(self, i):
        return (0, 1) if i == self.M else (1, i)


def cf_symbols(P, a, m):
    pk2, qk2, pk1, qk1 = 0, 1, 1, 0
    x, y = a, m
    out = []
    while y:
        t = x // y
        pk, qk = t * pk1 + pk2, t * qk1 + qk2
        out.append(P.idx(qk, qk1) if pk * qk1 - pk1 * qk == 1 else P.idx(qk, -qk1))
        pk2, qk2, pk1, qk1 = pk1, qk1, pk, qk
        x, y = y, x - t * y
    return out


class Rows:
    def __init__(self, P, aq, p):
        self.P, self.aq, self.p = P, aq, p
        self.H = {q: heilbronn_merel(q) for q in aq}

    def rows_of(self, i):
        P, p = self.P, self.p
        c, d = P.rep(i)
        out = []
        r = {}
        for k in (i, P.idx(d, -c)):
            r[k] = (r.get(k, 0) + 1) % p
        out.append(("S", i, r))
        r = {}
        for k in (i, P.idx(d, -c - d), P.idx(-c - d, c)):
            r[k] = (r.get(k, 0) + 1) % p
        out.append(("tau", i, r))
        j = P.idx(-c, d)
        if j != i:
            out.append(("star", i, {i: 1, j: p - 1}))
        for q, H in self.H.items():
            r = {}
            for (a, b, cc, dd) in H:
                k = P.idx(c * a + d * cc, c * b + d * dd)
                r[k] = (r.get(k, 0) + 1) % p
            r[i] = (r.get(i, 0) - self.aq[q]) % p
            out.append((f"T{q}", i, {k: v for k, v in r.items() if v}))
        return out


class Elim:
    """Incremental row-echelon form over F_p (pivot = largest column)."""

    def __init__(self, p):
        self.p = p
        self.piv = {}

    def reduce(self, r):
        p = self.p
        r = {k: x % p for k, x in r.items() if x % p}
        out = {}
        while r:
            k = max(r)
            x = r.pop(k)
            if k in self.piv:
                for kk, vv in self.piv[k].items():
                    if kk == k:
                        continue
                    nv = (r.get(kk, 0) - x * vv) % p
                    if nv:
                        r[kk] = nv
                    else:
                        r.pop(kk, None)
            else:
                out[k] = x
        return out

    def add(self, r):
        r = self.reduce(r)
        if not r:
            return False
        pc = max(r)
        inv = pow(r[pc], -1, self.p)
        self.piv[pc] = {k: v * inv % self.p for k, v in r.items()}
        return True


def functional(P, a, m, p):
    v = {}
    for k in cf_symbols(P, a, m):
        v[k] = (v.get(k, 0) + 1) % p
    return {k: x for k, x in v.items() if x}


def certificate_experiment(M, coeffs, p, Q, target, nu, rmax=6, max_symbols=4000):
    """Search lambda with  v = sum lambda_r row_r + c * nu  on balls R(r).

    target, nu: (a, m) pairs giving {infinity, a/m}.  Returns the history with the
    unresolved boundary at each radius; on success, c = v(Phi)/nu(Phi) mod p for
    every Phi satisfying the rows (or 'nu in span' if nu vanishes on all of them)."""
    P = P1(M)
    aq = {q: ap_count(coeffs, q) % p for q in Q if M % q}
    R = Rows(P, aq, p)
    v = functional(P, *target, p)
    n = functional(P, *nu, p)
    E = Elim(p)
    added, frontier = set(), set(v) | set(n)
    hist = []
    for r in range(rmax + 1):
        for i in sorted(frontier):
            for (_, _, row) in R.rows_of(i):
                E.add(row)
        added |= frontier
        touched = set()
        for i in added:
            for (_, _, row) in R.rows_of(i):
                touched |= set(row)
        boundary = touched - added
        rn = E.reduce(n)
        rv = E.reduce(v)
        rec = {"radius": r, "symbols_with_rows": len(added), "touched_columns": len(touched),
               "unresolved_boundary_columns": len(boundary)}
        if not rn:
            rec["certificate"] = "nu lies in the row span: nu(Phi)=0 for every solution"
            rec["v_also_zero"] = not rv
            hist.append(rec)
            break
        # v - c*nu in span  <=>  rv = c*rn
        k = max(rn)
        c = rv.get(k, 0) * pow(rn[k], -1, p) % p
        diff = {kk: (rv.get(kk, 0) - c * rn.get(kk, 0)) % p for kk in set(rv) | set(rn)}
        ok = not any(diff.values())
        rec["certificate"] = ok
        if ok:
            rec["v_over_nu_mod_p"] = c
        else:
            rec["residual_columns"] = sum(1 for x in diff.values() if x)
        hist.append(rec)
        if ok or not boundary or len(added) > max_symbols:
            break
        frontier = boundary
    return {"M": M, "p": p, "Q": list(aq), "a_q_mod_p": aq, "target": f"{{inf,{target[0]}/{target[1]}}}",
            "nu": f"{{inf,{nu[0]}/{nu[1]}}}", "P1_size": P.n, "history": hist}


if __name__ == "__main__":
    print(json.dumps(certificate_experiment(389, (0, 1, 1, -2, 0), 31, [2, 3, 5], (1, 31), (2, 31)), indent=1))
