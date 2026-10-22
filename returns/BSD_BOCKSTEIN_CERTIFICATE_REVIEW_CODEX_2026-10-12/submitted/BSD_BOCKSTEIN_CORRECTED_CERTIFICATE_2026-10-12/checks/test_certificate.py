#!/usr/bin/env python3
"""Exact algebra controls, not calculations of any seed cohomology or Kato class."""
from __future__ import annotations

import itertools
import json
import random
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from refined_certificate import evaluate

INF = float("inf")


def vp(x, p):
    x = F(x)
    if not x:
        return INF
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def content(xs, p):
    return min((vp(x, p) for x in xs), default=INF)


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def det(a):
    if not a:
        return F(1)
    a = [list(map(F, row)) for row in a]
    sign = F(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        for i in range(k + 1, len(a)):
            ratio = a[i][k] / a[k][k]
            for j in range(k, len(a)):
                a[i][j] -= ratio * a[k][j]
    for i in range(len(a)):
        sign *= a[i][i]
    return sign


def first_minor_vector(d0, d1):
    n = len(d0)
    out = []
    for omitted in range(n + 1):
        cols = [j for j in range(n + 1) if j != omitted]
        coefficient = F(0)
        for row_from_d1 in range(n):
            minor = [[(d1 if i == row_from_d1 else d0)[i][j]
                      for j in cols] for i in range(n)]
            coefficient += det(minor)
        out.append((-1)**omitted * coefficient)
    return out


def smith_at_p(d0, p):
    """Exact Z_(p) row/column reduction, tracking both p-unimodular maps."""
    a = [list(map(F, row)) for row in d0]
    n, m = len(a), len(a[0])
    left, right = eye(n), eye(m)
    rank = 0
    for k in range(min(n, m)):
        candidates = [(vp(a[i][j], p), i, j)
                      for i in range(k, n) for j in range(k, m) if a[i][j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        a[k], a[i] = a[i], a[k]
        left[k], left[i] = left[i], left[k]
        for mat in (a, right):
            for row in mat:
                row[k], row[j] = row[j], row[k]
        for i in range(k + 1, n):
            q = a[i][k] / a[k][k]
            assert vp(q, p) >= 0
            a[i] = [x - q*y for x, y in zip(a[i], a[k])]
            left[i] = [x - q*y for x, y in zip(left[i], left[k])]
        for j in range(k + 1, m):
            q = a[k][j] / a[k][k]
            assert vp(q, p) >= 0
            for mat in (a, right):
                for row in mat:
                    row[j] -= q * row[k]
        rank += 1
    assert mul(mul(left, d0), right) == a
    assert vp(det(left), p) == vp(det(right), p) == 0
    return a, left, right, rank


def determinantal_torsion_length(d0, p):
    # Independent check: the valuation of the (n-1)-st determinantal divisor.
    n = len(d0)
    k = n - 1
    values = []
    for rows in itertools.combinations(range(n), k):
        for cols in itertools.combinations(range(n + 1), k):
            values.append(det([[d0[i][j] for j in cols] for i in rows]))
    return content(values, p)


def verify_jet(d0, d1, p):
    s, left, right, rank = smith_at_p(d0, p)
    n = len(d0)
    assert rank == n - 1
    tau = sum(vp(s[i][i], p) for i in range(rank))
    assert tau == determinantal_torsion_length(d0, p)
    transformed = mul(mul(left, d1), right)
    beta = transformed[-1][-2:]
    b = content(beta, p)
    lhs = content(first_minor_vector(d0, d1), p)
    assert lhs == tau + b, (p, d0, d1, lhs, tau, b)
    return tau, b


def change_basis(n, rng):
    a = eye(n)
    if n > 1:
        for _ in range(4):
            i, j = rng.sample(range(n), 2)
            k = rng.choice([-3, -2, -1, 1, 2, 3])
            a[i] = [x + k*y for x, y in zip(a[i], a[j])]
    # A rational prime-to-p unit change tests more than GL_n(Z) changes.
    a[0] = [F(2)*x for x in a[0]]
    return a


def packet(name, p, m, b, w=0, precision=None):
    n = precision or max(m, b, w) + 2
    modulus = p**n
    return {"case_id": name, "kind": "abstract_control", "p": p,
            "delta": {"precision": n, "residues": [p**m % modulus, 0]},
            "bockstein": {"precision": n, "residues": [0, p**b % modulus]},
            "local_log": {"precision": n, "residues": [p**w % modulus, 0]}}


def run():
    rng = random.Random(20261012)
    jet_count = 0
    source_count = 0
    zero_beta_count = 0
    basis_count = 0
    for p in [5, 7, 11, 17, 53, 97]:
        for n in range(1, 5):
            for trial in range(12):
                d0 = [[F(0) for _ in range(n + 1)] for _ in range(n)]
                for i in range(n - 1):
                    d0[i][i] = F(p**rng.randrange(4))
                d1 = [[F(rng.randrange(-5, 6)) for _ in range(n + 1)]
                      for _ in range(n)]
                b = trial % 5
                if trial % 6 == 0:
                    d1[-1][-2:] = [F(0), F(0)]
                    zero_beta_count += 1
                else:
                    d1[-1][-2:] = [F(p**b), F(-2*p**b)]
                expected = verify_jet(d0, d1, p)
                jet_count += 1
                left, right = change_basis(n, rng), change_basis(n + 1, rng)
                d0c = mul(mul(left, d0), right)
                d1c = mul(mul(left, d1), right)
                assert verify_jet(d0c, d1c, p) == expected
                jet_count += 1
                basis_count += 1
                # U-dependent changes: (I+U L1) D(U) (I+U R1).
                l1 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
                r1 = [[F(rng.randrange(-2, 3)) for _ in range(n + 1)]
                      for _ in range(n + 1)]
                d1u = add(add(d1c, mul(l1, d0c)), mul(d0c, r1))
                assert verify_jet(d0c, d1u, p) == expected
                jet_count += 1
                basis_count += 1
        for a in range(4):
            for b in range(5):
                for e in range(3):
                    # D=[[P,U,0,0],[0,P,U,0],[0,0,0,p^b U]].
                    # eta=(U^2,-P U,P^2,0), d=U p^b,
                    # z=U p^(b+e) eta. Finite R-errors have length 2a at U=0.
                    P = p**a
                    d0 = [[F(P), F(0), F(0), F(0)],
                          [F(0), F(P), F(0), F(0)],
                          [F(0), F(0), F(0), F(0)]]
                    d1 = [[F(0), F(1), F(0), F(0)],
                          [F(0), F(0), F(1), F(0)],
                          [F(0), F(0), F(0), F(p**b)]]
                    tau, beta_content = verify_jet(d0, d1, p)
                    delta = [0, 0, p**(b+e)*P**2, 0]
                    m = content(delta, p)
                    assert tau == 2*a and beta_content == b
                    assert m == tau + b + e
                    result = evaluate(packet(f"source-{p}-{a}-{b}-{e}", p, m, b))
                    assert result["corrected_length_upper_bound_conditional"] == 2*a+e
                    assert result["corrected_criterion_met"] == (2*a+e <= 1)
                    assert result["actual_seed_primary_vanishing_certified"] is False
                    source_count += 1

    cases = []
    improved = packet("old-fails-new-passes", 5, m=3, b=2)
    result = evaluate(improved)
    assert not result["old_criterion_met"] and result["corrected_criterion_met"]
    cases.append(result)
    (ROOT / "examples" / "abstract_improved.json").write_text(json.dumps(improved, indent=2)+"\n")

    # Only a LOWER Bockstein bound is needed; both beta entries may vanish at this precision.
    low = packet("bockstein-lower-bound-only", 7, m=3, b=2)
    low["bockstein"] = {"precision": 2, "residues": [0, 0]}
    result = evaluate(low)
    assert result["corrected_criterion_met"] and not result["bockstein_observation"]["content_is_exact"]
    cases.append(result)

    local_corrected = evaluate(packet("both-corrections-used", 13, m=5, b=2, w=2))
    assert local_corrected["corrected_criterion_met"] and not local_corrected["old_criterion_met"]
    cases.append(local_corrected)

    local_lower = packet("local-index-lower-bound-only", 13, m=3, b=1, w=1)
    local_lower["local_log"] = {"precision": 1, "residues": [0, 0]}
    result = evaluate(local_lower)
    assert result["corrected_criterion_met"] and not result["local_log_observation"]["content_is_exact"]
    cases.append(result)

    # A finite pair must survive even when all height-one ideals agree.
    surviving = evaluate(packet("finite-pair-not-erased", 5, m=5, b=3))
    assert surviving["even_length_upper_bound_conditional"] == 2
    assert not surviving["corrected_criterion_met"]
    cases.append(surviving)

    unknown = packet("zero-is-insufficient-precision", 11, m=3, b=0, precision=3)
    result = evaluate(unknown)
    assert result["status"] == "INCONCLUSIVE_DERIVATIVE_PRECISION"
    cases.append(result)

    impossible = evaluate(packet("inconsistent-normalization", 17, m=1, b=3))
    assert impossible["status"] == "REJECT_INCONSISTENT_VALUATION_INPUTS"
    cases.append(impossible)

    excluded = evaluate(packet("excluded-prime", 59, m=0, b=0))
    assert excluded["status"] == "OUTSIDE_RETAINED_PRIME_DOMAIN"
    cases.append(excluded)

    # Deliberately break the (p)-height-one Kato inequality: a=1,b=2,g=1.
    # Then m=2,b=2,tau=2, and an unauthenticated residue packet would 'pass'.
    # This demonstrates why the arithmetic source condition CANNOT be omitted.
    missing_p = evaluate(packet("missing-height-one-p-hypothesis", 5, m=2, b=2))
    assert missing_p["corrected_criterion_met"]
    assert not missing_p["actual_seed_primary_vanishing_certified"]
    missing_p["negative_control"] = "Full complex has tau=2; Kato inequality at (p) FAILS; no seed conclusion."
    cases.append(missing_p)

    invalid_count = 0
    for mutate in [lambda x: x.update(p=9),
                   lambda x: x.update(p=True),
                   lambda x: x.update(extra_field="not accepted"),
                   lambda x: x["delta"].update(residues=[-1, 0]),
                   lambda x: x["delta"].update(precision=0)]:
        bad = packet("bad-input", 5, 0, 0)
        mutate(bad)
        try:
            evaluate(bad)
        except ValueError:
            invalid_count += 1
        else:
            raise AssertionError("Malformed input accepted")

    summary = {"status": "PASS", "random_seed": 20261012,
               "exact_first_jet_checks": jet_count,
               "basis_and_first_order_gauge_variants": basis_count,
               "base_cases_with_zero_first_bockstein": zero_beta_count,
               "finite_error_and_source_defect_checks": source_count,
               "valuation_boundary_scenarios": len(cases),
               "malformed_inputs_rejected": invalid_count,
               "actual_seed_cohomology_matrices_evaluated": 0,
               "actual_seed_kato_derivatives_evaluated": 0,
               "new_seed_primary_results": 0,
               "formal_proof_assistant_verification": False,
               "external_review": False}
    (ROOT / "checks" / "RESULTS.json").write_text(json.dumps(summary, indent=2)+"\n")
    (ROOT / "checks" / "BOUNDARY_CASES.json").write_text(json.dumps(cases, indent=2)+"\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    run()
