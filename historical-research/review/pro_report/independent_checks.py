#!/usr/bin/env python3
"""Small independent checks for seed_bsd.pdf v0.1.1.

Python standard library only. This script does NOT certify the L-series or real
regulator enclosures, replay saturation, prove the Manin bound, inspect the large
coefficient corpus, or compile Lean. Printed interval arithmetic checks only the
consistency of the manuscript's stated input bounds.

Run: python3 independent_checks.py [output.json]
"""
from __future__ import annotations

import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt, prod
from pathlib import Path

Q = Fraction
Point = tuple[Fraction | int, Fraction | int] | None
A2, A4, A6 = -22735, 106272484, 0
N = 2**3 * 3 * 2243 * 4547**2 * 5843


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def legendre(a: int, p: int) -> int:
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def add_points(left: Point, right: Point) -> Point:
    if left is None:
        return right
    if right is None:
        return left
    x, y = map(Q, left)
    z, w = map(Q, right)
    if x == z and y == -w:
        return None
    slope = ((w - y) / (z - x) if x != z
             else (3*x*x + 2*A2*x + A4) / (2*y))
    xx = slope*slope - A2 - x - z
    return xx, -y + slope*(x - xx)


def main() -> dict:
    b2, b4, b6, b8 = 4*A2, 2*A4, 4*A6, 4*A2*A6 - A4*A4
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    assert c4**3 - c6**2 == 1728*delta
    assert delta == 2**8 * 3**2 * 2243 * 4547**3 * 5843**2
    j = Q(c4**3, delta)
    points = [(0, 0), (4547, 327384), (5184, 281520), (5843, 210348)]
    assert all(y*y == x**3 + A2*x*x + A4*x + A6 for x, y in points)
    t, p1, p2, g = points
    relation = add_points(add_points((p1[0], -p1[1]), (p2[0], -p2[1])), t)
    assert relation == g
    aps = {
        p: -sum(legendre(x**3 + A2*x*x + A4*x + A6, p) for x in range(p))
        for p in range(3, 2000) if is_prime(p) and N % p != 0
    }
    ss = [p for p, ap in aps.items() if ap == 0]
    expected_ss = [23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823]
    assert ss == expected_ss
    possible_isogeny_primes = [3, 5, 7, 11, 13, 17, 19, 37, 43, 67, 163]
    witnesses = {}
    for ell in possible_isogeny_primes:
        q = 17 if ell == 5 else (7 if ell in [13, 17, 37] else 5)
        ap = aps[q]
        disc = ap*ap - 4*q
        assert q != ell and legendre(disc, ell) == -1
        witnesses[ell] = {"q": q, "a_q": ap, "Frobenius_discriminant": disc,
                          "discriminant_mod_ell": disc % ell, "Legendre_symbol": -1}
    with localcontext() as ctx:
        ctx.prec = 70
        or_lo = Decimal('0.99820315980984172437')
        or_hi = Decimal('0.99820315980984173470')
        q_lo = Decimal('35.929604') / or_hi
        q_hi = Decimal('35.941023') / or_lo
    height_det = 2127*764 - 1294**2
    shift = 7578
    triple = [2243, 2243 + 16*12**2, 2243 + 25*12**2]
    assert all(is_prime(q) and q % 24 == 11 for q in triple)
    return {
        "scope": __doc__,
        "N_product": N, "c4": c4, "c6": c6, "Delta": delta, "j": str(j),
        "translated_model": [0, 3*shift+A2, 0,
            3*shift**2+2*A2*shift+A4, shift**3+A2*shift**2+A4*shift+A6],
        "all_four_displayed_points_on_curve": True,
        "G_equals_minus_P1_minus_P2_plus_T": True,
        "Zywina_specialization": {"m": 2243, "n": 12, "triple": triple,
                                   "all_prime_and_11_mod_24": True},
        "good_prime_traces": {p: aps[p] for p in [5, 7, 11, 13, 17]},
        "supersingular_primes_below_2000": ss,
        "Frobenius_irreducibility_witnesses": witnesses,
        "multiplicative_sign_tests_Legendre_minus_c6": {
            p: legendre(-c6, p) for p in [3, 2243, 5843]},
        "j_mod_4547": j.numerator*pow(j.denominator, -1, 4547) % 4547,
        "D5_displayed_matrix_determinant": height_det,
        "D5_determinant_mod_2243": height_det % 2243,
        "q_bounds_from_printed_inputs_not_new_certification": [str(q_lo), str(q_hi)],
        "definite_Eichler_mass_formula": str(
            Q(prod(p-1 for p in [3, 2243, 5843]), 12)
            * 2**3 * 4547**2 * Q(3, 2) * Q(4548, 4547)),
        "unit_residues_mod_81": sum(b % 3 != 0 for b in range(1, 81)),
        "plus_and_minus_at_81_total": 108,
        "unit_residues_mod_27_plus_mod_81_per_sign": 18+54,
        "a4099_by_exhaustive_point_count": -sum(legendre(x**3 + A2*x*x + A4*x + A6, 4099) for x in range(4099)),
        "p3_reported_quadratic_coefficient_mod_27": 15480 % 27,
        "p3_reported_full_period_coefficient_mod_27": 7740 % 27,
        "Atkin_Lehner_coefficient_checks": {
            "minus996_mod2243": (-996) % 2243,
            "995_times996_times1991_over6_mod2243": (995*996*1991//6) % 2243},
    }


if __name__ == '__main__':
    output = main()
    text = json.dumps(output, indent=2)
    destination = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
    destination.write_text(text + '\n', encoding='utf-8')
    print(text)
