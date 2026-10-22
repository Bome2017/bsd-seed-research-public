#!/usr/bin/env python3
"""Exact finite-ring extractor for the conditional four-value Kato certificate.

This program does NOT calculate Kato classes, modular symbols, or Sha. It accepts
four claimed arithmetic residues, checks the finite-ring format, and reconstructs
four weighted coefficients in the specified source normalization. Its conclusions
require the arithmetic provenance and hypotheses in DERIVATION.md.

Run: python3 four_value.py --self-test
Or:  python3 four_value.py --input residues.json
Input: {"p": 17, "N": 6503188012738584, "values": [e32,e33,e43,e44]}
Each entry is F(t_w,t_s) modulo p^4 in the common SOURCE Coleman coordinate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
import random
from typing import Any

N_SEED = 6503188012738584
NODES = ((3, 2), (3, 3), (4, 3), (4, 4))
MONOMIALS = ((2, 0), (0, 2), (3, 0), (1, 2))


def is_prime_small(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True


def validate_p(p: int) -> None:
    # The supplied proof remains conditional on its arithmetic exceptional set.
    if isinstance(p, bool) or not isinstance(p, int) or p < 17:
        raise ValueError("p must be an integer prime >=17")
    if p > 1_000_000:
        raise ValueError("This standalone input guard is capped at p=10^6; use a certified prime test above it")
    if not is_prime_small(p):
        raise ValueError("p is not prime")


def mat_vec(M: list[list[int]], x: list[int], q: int) -> list[int]:
    return [sum(a * b for a, b in zip(row, x)) % q for row in M]


def matrix_inverse(M: list[list[int]], q: int) -> list[list[int]]:
    n = len(M)
    if any(len(row) != n for row in M):
        raise ValueError("matrix must be square")
    A = [[x % q for x in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(M)]
    for c in range(n):
        piv = next((r for r in range(c, n) if gcd(A[r][c], q) == 1), None)
        if piv is None: raise ValueError("matrix has no unit pivot")
        A[c], A[piv] = A[piv], A[c]
        u = pow(A[c][c], -1, q)
        A[c] = [u * x % q for x in A[c]]
        for r in range(n):
            if r == c: continue
            fac = A[r][c]
            A[r] = [(x - fac * y) % q for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def principal_root(value: int, power: int, p: int, precision: int) -> int:
    """Unique power-th root in 1+pZ_p modulo p^precision (power prime to p)."""
    q = p ** precision
    if value % p != 1 or gcd(power, p) != 1:
        raise ValueError("root requires a principal unit and power prime to p")
    exponent = pow(power, -1, p ** (precision - 1))
    root = pow(value % q, exponent, q)
    assert root % p == 1 and pow(root, power, q) == value % q
    return root


def principal_part(N: int, p: int, precision: int = 4) -> int:
    q = p ** precision
    if N % p == 0: raise ValueError("p divides N")
    omega = pow(N % q, p ** precision, q)
    assert pow(omega, p - 1, q) == 1
    return N * pow(omega, -1, q) % q


def evaluation_matrix(p: int) -> list[list[int]]:
    """TRUE finite-ring coordinates, not their mod-p approximations."""
    q = p ** 4
    high = p ** 5   # enough to divide t and Y by p and retain mod p^4
    M = []
    for w, s in NODES:
        tw = (pow(1 + p, w, high) - 1) % high
        ts1 = pow(1 + p, s, high)
        sqrt_tw1 = principal_root((1 + tw) % high, 2, p, 5)
        zeta = ts1 * pow(sqrt_tw1, -1, high) % high
        Y = (zeta - pow(zeta, -1, high)) * pow(2, -1, high) % high
        assert tw % p == 0 and Y % p == 0
        x, y = (tw // p) % q, (Y // p) % q
        assert x % p == w % p
        assert y % p == (s - w * pow(2, -1, p)) % p
        M.append([x*x % q, y*y % q, x*x*x % q, x*y*y % q])
    return M


def normalizing_units(p: int, N: int = N_SEED) -> list[int]:
    q = p ** 4
    r = principal_root(principal_part(N, p), 4, p, 4)
    return [pow(r, e, q) for e in (1, 3, 2, 4)]


def extract(p: int, values: list[int], N: int = N_SEED) -> dict[str, Any]:
    validate_p(p)
    q = p ** 4
    if len(values) != 4 or any(isinstance(x, bool) or not isinstance(x, int) for x in values):
        raise ValueError("values must be four integer residues in node order (3,2),(3,3),(4,3),(4,4)")
    if any(x < 0 or x >= q for x in values):
        raise ValueError("residues must be in [0,p^4)")
    if any(x % (p*p) for x in values):
        raise ValueError("input contradicts the retained J^2 divisibility at these nodes")
    M = evaluation_matrix(p)
    units = normalizing_units(p, N)
    Hvalues = [u * x % q for u, x in zip(units, values)]
    c = mat_vec(matrix_inverse(M, q), Hvalues, q)
    divisors = (p*p, p*p, p**3, p**3)
    if any(x % div for x, div in zip(c, divisors)):
        raise ValueError("residues fail the invariant-quartic-jet compatibility constraints in the supplied normalization")
    coeffs = {name: x // div for name, x, div in zip(("A", "B", "C", "D"), c, divisors)}
    assert mat_vec(M, c, q) == Hvalues
    nonzero = any(values)
    return {
        "p": p, "N": N, "nodes": [list(n) for n in NODES],
        "formal_status": "NONZERO_FOURTH_ORDER_JET" if nonzero else "ZERO_JET_INCONCLUSIVE",
        "F_values_mod_p4": values, "H_values_mod_p4": Hvalues,
        "normalizing_units_mod_p4": units,
        "weighted_coefficients_mod_p4": c,
        "coefficients": coeffs,
        "coefficient_moduli": {"A": p*p, "B": p*p, "C": p, "D": p},
        "arithmetic_provenance_verified": False,
        "meaning": "Only a finite-ring calculation. A seed conclusion requires certified genuine Kato inputs and all hypotheses in DERIVATION.md. Zero is inconclusive."
    }


def determinant_fraction(M: list[list[Fraction]]) -> Fraction:
    A = [row[:] for row in M]
    d = Fraction(1)
    n = len(A)
    for j in range(n):
        r = next((r for r in range(j, n) if A[r][j]), None)
        if r is None: return Fraction(0)
        if r != j: A[r], A[j] = A[j], A[r]; d = -d
        piv = A[j][j]; d *= piv
        for r in range(j+1, n):
            fac = A[r][j]/piv
            for c in range(j+1, n): A[r][c] -= fac*A[j][c]
            A[r][j] = 0
    return d


def evaluate_synthetic(p: int, abcd: list[int], N: int = N_SEED) -> list[int]:
    q = p**4
    weighted = [(p**deg)*a % q for a, deg in zip(abcd, (2, 2, 3, 3))]
    Hvalues = mat_vec(evaluation_matrix(p), weighted, q)
    return [x*pow(u,-1,q)%q for x,u in zip(Hvalues,normalizing_units(p,N))]


def self_test() -> dict[str, Any]:
    V0 = [[Fraction(w*w), (Fraction(s)-Fraction(w,2))**2,
           Fraction(w**3), w*(Fraction(s)-Fraction(w,2))**2] for w,s in NODES]
    assert determinant_fraction(V0) == 864
    integer_scaled = [[4*x for x in row] for row in V0]
    assert determinant_fraction(integer_scaled) == 4**4*864
    # An independently stated inverse, checked by rational multiplication.
    V0inv = [[Fraction(1,2),Fraction(-1,18),Fraction(-1,4),Fraction(1,16)],
             [Fraction(-2),Fraction(2),Fraction(1),Fraction(-1)],
             [Fraction(-1,8),Fraction(1,72),Fraction(1,12),Fraction(-1,48)],
             [Fraction(1,2),Fraction(-1,2),Fraction(-1,3),Fraction(1,3)]]
    for i in range(4):
        for j in range(4):
            assert sum(V0inv[i][k]*V0[k][j] for k in range(4)) == int(i==j)
    primes = [p for p in range(17,180) if is_prime_small(p) and N_SEED%p]
    rng = random.Random(20261004)
    cases = 0
    index_three_cases = 0
    compatibility_rejections = 0
    for p in primes:
        q = p**4; M = evaluation_matrix(p); invM = matrix_inverse(M,q)
        for i in range(4):
            assert mat_vec(invM,[row[i] for row in M],q) == [int(i==j) for j in range(4)]
        assert determinant_fraction([[Fraction(x%p) for x in row] for row in M]) % p == 864 % p
        for _ in range(120):
            abcd = [rng.randrange(p*p),rng.randrange(p*p),rng.randrange(p),rng.randrange(p)]
            values = evaluate_synthetic(p,abcd)
            result = extract(p,values)
            assert list(result["coefficients"].values()) == abcd
            assert any(values) == any(abcd)
            cases += 1
        # Every top-layer basis class must be detected, including p times a quadratic.
        for abcd in ([p,0,0,0],[0,p,0,0],[0,0,1,0],[0,0,0,1]):
            values=evaluate_synthetic(p,list(abcd)); r=extract(p,values)
            assert any(values) and all(x%p**3==0 for x in values)
            assert r["formal_status"]=="NONZERO_FOURTH_ORDER_JET"
            index_three_cases += 1
        assert extract(p,[0]*4)["formal_status"]=="ZERO_JET_INCONCLUSIVE"
        # Correct inverse need not be V0^{-1} beyond first residue digit.
        # Deliberately choose a putative nonintegral cubic weighted coordinate.
        fake=mat_vec(M,[0,0,p*p,0],q)
        values=[x*pow(u,-1,q)%q for x,u in zip(fake,normalizing_units(p))]
        try: extract(p,values)
        except ValueError: compatibility_rejections += 1
        else: raise AssertionError("invalid cubic precision accepted")
    ranges=[]
    for w,s in NODES:
        k,r=w+2,w+1-s
        assert 1<=r and 2*r<k
        ranges.append({"w":w,"s":s,"weight":k,"r":r,"twist_exponent":w-s})
    # Formal minimum of four scalar measurements: rank of any <=3 rows <=3
    # on a four-dimensional top layer. This is mathematical linear algebra,
    # not a seed lower bound or an exhaustive search.
    return {
        "scope":"EXACT_FORMAL_CONTROLS_ONLY; no actual Kato value evaluated",
        "status":"PASS", "determinant":864,
        "rational_inverse_checked":True,
        "primes":primes, "random_reconstruction_cases":cases,
        "index_three_basis_cases":index_three_cases,
        "incompatible_precision_cases_rejected":compatibility_rejections,
        "critical_ranges":ranges,
        "source_theorems_reproved":False,
        "seed_primary_certificate":False
    }


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test",action="store_true")
    group.add_argument("--input",type=Path)
    ns=ap.parse_args()
    try:
        if ns.self_test: out=self_test()
        else:
            data=json.loads(ns.input.read_text(encoding="utf-8"))
            out=extract(data["p"],data["values"],data.get("N",N_SEED))
        print(json.dumps(out,indent=2,sort_keys=True))
    except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as exc:
        ap.exit(2,f"INVALID_INPUT: {exc}\n")

if __name__=="__main__":main()
