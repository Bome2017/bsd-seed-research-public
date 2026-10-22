#!/usr/bin/env python3
"""Exact weight-two modular symbols for Gamma_0(N), N prime (calibration only).

Manin symbols (c:d) in P^1(Z/N); right action (c,d)g = (c a + d c', c b + d d').
Relations: x + xS = 0 and x + x tau + x tau^2 = 0, S=[[0,-1],[1,0]], tau=[[0,-1],[1,-1]].
Hecke operators via Merel's Heilbronn set {ad-bc=q, a>b>=0, d>c>=0}.

The dual space W = {phi : P^1 -> Q satisfying the relations} carries the transpose
Hecke action (T_q phi)(x) = sum_h phi(x h).  An eigenfunctional for the curve's a_q
gives the classical modular symbol r -> phi({infinity, r}) up to a scalar.

This file is a development/calibration tool on small conductors.  It does NOT
construct anything at the seed level N=6503188012738584.
"""
from __future__ import annotations
from fractions import Fraction
from math import gcd


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


class P1Prime:
    def __init__(self, N: int):
        if not is_prime(N):
            raise ValueError("calibration module supports prime level only")
        self.N = N
        self.elems = [(0, 1)] + [(1, d) for d in range(N)]
        self.index = {e: i for i, e in enumerate(self.elems)}

    def norm(self, c: int, d: int) -> int:
        N = self.N
        c %= N
        d %= N
        if c == 0:
            if d == 0:
                raise ValueError("not in P^1")
            return 0
        return self.index[(1, d * pow(c, -1, N) % N)]


def heilbronn_merel(q: int):
    out = []
    for a in range(1, q + 1):
        for b in range(0, a):
            for d in range(1, q + 1):
                for c in range(0, d):
                    if a * d - b * c == q:
                        out.append((a, b, c, d))
    return out


def nullspace(rows, ncols):
    """Exact nullspace over Q.  rows: iterable of dict col->number."""
    piv = {}  # pivot col -> fully reduced row (dict), pivot entry 1
    for r in rows:
        r = {k: Fraction(v) for k, v in r.items() if v}
        while r:
            pc = next((k for k in r if k in piv), None)
            if pc is None:
                break
            f = r[pc]
            for k, v in piv[pc].items():
                nv = r.get(k, 0) - f * v
                if nv:
                    r[k] = nv
                else:
                    r.pop(k, None)
        if not r:
            continue
        pc = min(r)
        f = r[pc]
        r = {k: v / f for k, v in r.items()}
        for rr in piv.values():
            if pc in rr:
                g = rr[pc]
                for k, v in r.items():
                    nv = rr.get(k, 0) - g * v
                    if nv:
                        rr[k] = nv
                    else:
                        rr.pop(k, None)
        piv[pc] = r
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for pc, rr in piv.items():
            v[pc] = -rr.get(fc, Fraction(0))
        basis.append(v)
    return basis


class ModSym2:
    def __init__(self, N: int):
        self.P = P1Prime(N)
        self.N = N
        n = len(self.P.elems)
        rows = []
        for (c, d) in self.P.elems:
            i = self.P.index[(c, d)]
            r = {}
            for k in (i, self.P.norm(d, -c)):
                r[k] = r.get(k, 0) + 1
            rows.append(r)
            r = {}
            for k in (i, self.P.norm(d, -c - d), self.P.norm(-c - d, c)):
                r[k] = r.get(k, 0) + 1
            rows.append(r)
        self.rel_rows = rows
        self.W = nullspace(rows, n)

    def check_relations(self, phi) -> bool:
        return all(sum(phi[k] * v for k, v in r.items()) == 0 for r in self.rel_rows)

    def hecke(self, q: int, phi):
        H = heilbronn_merel(q)
        return [sum(phi[self.P.norm(c * a + d * cc, c * b + d * dd)] for (a, b, cc, dd) in H)
                for (c, d) in self.P.elems]

    def is_eigen(self, phi, aq: dict) -> bool:
        return all([x - a * y for x, y in zip(self.hecke(q, phi), phi)] == [0] * len(phi)
                   for q, a in aq.items() if self.N % q)

    def eigen_functionals(self, aq: dict):
        """Subspace of W on which T_q^t = a_q for all supplied q (q prime to N)."""
        basis = self.W
        n = len(self.P.elems)
        for q, a in aq.items():
            if self.N % q == 0:
                continue
            m = len(basis)
            imgs = [[x - a * y for x, y in zip(self.hecke(q, v), v)] for v in basis]
            rows = []
            for col in range(n):
                r = {i: imgs[i][col] for i in range(m) if imgs[i][col]}
                if r:
                    rows.append(r)
            ker = nullspace(rows, m)
            basis = [[sum(t[i] * basis[i][col] for i in range(m)) for col in range(n)] for t in ker]
        return basis

    @staticmethod
    def primitive(v):
        den = 1
        for x in v:
            x = Fraction(x)
            den = den * x.denominator // gcd(den, x.denominator)
        w = [int(Fraction(x) * den) for x in v]
        g = 0
        for x in w:
            g = gcd(g, x)
        return [x // g for x in w]

    def star(self, phi):
        """phi composed with the involution {a,b} -> {-a,-b}; on Manin symbols (c:d)->(-c:d)."""
        return [phi[self.P.norm(-c, d)] for (c, d) in self.P.elems]

    def symbol_inf_to(self, phi, a: int, m: int):
        """phi({infinity, a/m}) via continued-fraction convergents (Manin's trick)."""
        if m <= 0:
            raise ValueError("denominator must be positive")
        pk2, qk2, pk1, qk1 = 0, 1, 1, 0
        x, y = a, m
        s = 0
        while y:
            t = x // y
            pk, qk = t * pk1 + pk2, t * qk1 + qk2
            # g=[[pk,pk1],[qk,qk1]], g{0,inf} = {pk1/qk1, pk/qk}
            if pk * qk1 - pk1 * qk == 1:
                s += phi[self.P.norm(qk, qk1)]
            else:
                s += phi[self.P.norm(qk, -qk1)]
            pk2, qk2, pk1, qk1 = pk1, qk1, pk, qk
            x, y = y, x - t * y
        return s


def ap_count(coeffs, p):
    a1, a2, a3, a4, a6 = coeffs
    cnt = 1
    for x in range(p):
        rhs = (x ** 3 + a2 * x * x + a4 * x + a6) % p
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y - rhs) % p == 0:
                cnt += 1
    return p + 1 - cnt
