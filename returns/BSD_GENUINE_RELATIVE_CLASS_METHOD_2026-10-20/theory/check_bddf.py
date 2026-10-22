#!/usr/bin/env python3
"""Reject one explicit unconditional generator criterion, not generation itself."""
import ast
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INV = ROOT.parent / "review" / "norm_inventory_result.gp"
DISC = ROOT.parent / "review" / "DISCRIMINANT_GENERATION_BOUND.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ceil_div(a, b):
    return (a + b - 1) // b


def main():
    bound, ideals, rational_primes, rows = ast.literal_eval(INV.read_text())
    assert (bound, ideals, rational_primes, len(rows)) == (419775, 35749, 35373, 8515)
    assert sum(row[2] for row in rows) == ideals
    assert len({(q, f) for q, f, count in rows}) == len(rows)
    assert all(q >= 2 and f >= 1 and count >= 1 and q ** f <= bound
               for q, f, count in rows)
    d = json.loads(DISC.read_text())
    fact = {2: 32, 3: 16, 5: 23, 2243: 16, 4547: 18, 5843: 16}
    delta = 1
    for q, e in fact.items():
        delta *= q ** e
    assert delta == int(d["D_A"])
    assert delta == int(d["D_Aplus"]) ** 2 * (2 ** 4 * 5 * 4547 ** 6)

    # ln(2)>2/3 from its positive atanh series. ln(2)<7/10 because
    # the positive Taylor polynomial for exp(7/10) already exceeds 2.
    x = Fraction(7, 10)
    term = Fraction(1)
    exp_lower = term
    for k in range(1, 6):
        term *= x / k
        exp_lower += term
    assert exp_lower > 2
    # gamma<1; log(4*pi)<3 follows from pi<4 and this exp(3)>16 witness.
    term = Fraction(1)
    exp3_lower = term
    for k in range(1, 5):
        term *= Fraction(3, k)
        exp3_lower += term
    assert exp3_lower > 16

    # Corollary 5.2 has nonnegative triangular weight <=1. Discard it.
    # Use ln(N)<(7/10)*bit_length(N), then round each positive summand UP.
    scale = 10 ** 9
    lhs_upper_scaled = 0
    powers_with_multiplicity = 0
    for q, f, count in rows:
        norm = q ** f
        power = norm
        while power <= bound:
            numerator = 4 * count * 7 * norm.bit_length() * scale
            denominator = 10 * (1 + power)
            lhs_upper_scaled += ceil_div(numerator, denominator)
            powers_with_multiplicity += count
            power *= norm
    lhs_upper = Fraction(lhs_upper_scaled, scale)

    # Drop positive 1/log(T) correction terms from the RHS, and use
    # ln(delta) > (2/3) sum e*floor(log2(q)), gamma+ln(4*pi)<4.
    log_delta_lower = Fraction(2, 3) * sum(e * (q.bit_length() - 1)
                                                   for q, e in fact.items())
    rhs_lower = log_delta_lower - 24 * 4 - 4
    assert lhs_upper < rhs_lower

    # Diagnostic, not the proof: evaluate the displayed weighted left side.
    # Constant Euler gamma is used only in this decimal diagnostic.
    with localcontext() as ctx:
        ctx.prec = 60
        T = Decimal(bound + 1)
        logT = T.ln()
        lhs = Decimal(0)
        for q, f, count in rows:
            norm = q ** f
            logN = Decimal(norm).ln()
            power, k = norm, 1
            while power <= bound:
                lhs += (Decimal(4 * count) * logN / Decimal(1 + power)
                        * (1 - Decimal(k) * logN / logT))
                power *= norm
                k += 1
        gamma = Decimal("0.577215664901532860606512090082402431042159335939923598805767")
        pi = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
        rhs = (Decimal(delta).ln()
               - 24 * (gamma + (4 * pi).ln() - pi * pi / (4 * logT))
               - 4 * (1 - Decimal(4).ln() / logT))
        diagnostic = {"lhs": str(lhs), "rhs": str(rhs), "gap_rhs_minus_lhs": str(rhs - lhs)}

    out = {
        "status": "FAIL_AT_THIS_CUTOFF",
        "criterion": "Belabas-Diaz y Diaz-Friedman Corollary 5.2, inequality (23), unconditional",
        "T": bound + 1,
        "n": 24,
        "r1": 4,
        "prime_ideals": ideals,
        "norm_rows": len(rows),
        "prime_power_terms_with_multiplicity": powers_with_multiplicity,
        "input_hashes": {str(INV.relative_to(ROOT.parent)): sha(INV),
                         str(DISC.relative_to(ROOT.parent)): sha(DISC)},
        "exact_lhs_upper": str(lhs_upper),
        "exact_rhs_lower": str(rhs_lower),
        "exact_failure_margin_lower": str(rhs_lower - lhs_upper),
        "diagnostic_decimal_not_certificate": diagnostic,
        "generation_disproved": False,
        "generator_defect_bounded": False,
        "new_class_bound": False,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
