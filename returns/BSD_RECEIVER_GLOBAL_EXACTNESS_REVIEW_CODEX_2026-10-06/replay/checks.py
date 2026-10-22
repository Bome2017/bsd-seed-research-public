#!/usr/bin/env python3
"""Exact seed arithmetic and elementary controls; no Selmer or BSD computation.

Python 3.9+. This script does not verify Galois cohomology, formal logarithms,
Pannekoek's theorem, the component number, or the global receiver inputs.
"""
from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("A finite valuation was requested for zero")
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def main() -> None:
    p = 4547
    require(all(p % d for d in range(2, isqrt(p) + 1)), "p is not prime")
    a2, a4, a6 = -1, -66020924, -65074271436
    x, y, h = -2394, 281520, 1516
    require(y*y == x**3+a2*x*x+a4*x+a6, "P2 is not on the exact curve")
    tr = [3*h+a2, 3*h*h+2*a2*h+a4, h**3+a2*h*h+a4*h+a6]
    require(all(c % p == 0 for c in tr), "Translated coefficient is not in p Z")
    b2, b4, b6, b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6-a4*a4
    c4 = b2*b2-24*b4
    delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    require(valuation(delta, p) == 3, "Unexpected discriminant valuation")
    require(valuation(c4, p) == 1, "Unexpected c4 valuation")
    X, Y = (x-h) % p, y % p
    require((Y*Y-X**3) % p == 0, "Point not on reduced cusp")
    require(2*Y % p != 0, "Smoothness derivative is zero")
    require(X != 0 and Y != 0, "Nonzero affine cusp point expected")
    quotients = {2: 4, 3: 8, 2243: 2242, 5843: 11688}
    require(all(gcd(p,n) == 1 for n in quotients.values()), "Extra bad-place exception")

    # Independent re-evaluation of the prior local addition certificate.
    # All affine denominators used below must be units. This is NOT a general
    # elliptic group implementation over Z/p^4: nonunit cases are rejected.
    modulus = p**4
    P = (x % modulus, y % modulus)
    denominators: list[int] = []

    def add(A, B):
        if A is None:
            return B
        if B is None:
            return A
        u, v = A
        r, s = B
        if A == B:
            num, den = 3*u*u+2*a2*u+a4, 2*v
        else:
            num, den = s-v, r-u
        require(den % p != 0, "Nonunit denominator: this check cannot proceed")
        denominators.append(den % p)
        slope = num*pow(den, -1, modulus) % modulus
        nx = (slope*slope-a2-u-r) % modulus
        ny = (slope*(u-nx)-v) % modulus
        require((ny*ny-nx**3-a2*nx*nx-a4*nx-a6) % modulus == 0,
                "Addition result is off curve")
        return nx, ny

    A = None
    for bit in bin(p-1)[2:]:
        A = add(A, A)
        if bit == '1':
            A = add(A, P)
    require(A is not None, "Unexpected point at infinity")
    dx = (A[0]-P[0]) % modulus
    dy = (A[1]+P[1]) % modulus
    require(valuation(dx, p) == 1, "The x difference is not valuation one")
    require(valuation(dy, p) == 1, "The y difference is not valuation one")
    require(dx//p % p == 1274, "Prior normalized residue not reproduced")

    # Linear algebra sanity controls, not arithmetic models of the seed.
    # Pairing on H=F_q^2 is the symmetric hyperbolic form, not a skew form:
    # b((a,b),(c,d))=a*d+b*c; f=span((1,0)).
    controls = []
    for q in [5,7,11]:
        def pairing(v, w):
            return (v[0]*w[1]+v[1]*w[0]) % q
        generator, complement = (1,0), (0,1)
        annihilator = [(a,b) for a in range(q) for b in range(q)
                       if pairing((a,b), generator) == 0]
        require(annihilator == [(a,0) for a in range(q)], "Wrong annihilator")
        require(pairing(generator, generator) == 0, "Finite line must survive")
        # A zero localized test vector cannot remove the complementary line.
        zero_test_allows_complement = pairing(complement, (0,0)) == 0
        require(zero_test_allows_complement, "Zero test control failed")
        require(pairing(complement, generator) != 0, "Nonzero test must detect complement")
        # Two possible bad places allow cancellation with one global test.
        left_pairing = pairing(complement, generator)
        right_pairing = pairing((0,q-1), generator)
        require((left_pairing+right_pairing) % q == 0, "Cancellation control failed")
        require(left_pairing != 0 and right_pairing != 0, "Control must be nontrivial")
        controls.append({
            "p": q,
            "annihilator_of_nonzero_f_generator_equals_f": True,
            "one_local_constraint_still_leaves_the_f_line": True,
            "zero_test_vector_does_not_control_the_complement": True,
            "two_relaxed_places_can_cancel_without_full_localization_rank": True,
        })

    result = {
        "status": "EXACT_ARITHMETIC_CONTROLS_PASS",
        "p": p,
        "p_is_prime": True,
        "P2_on_exact_curve": True,
        "translated_coefficients": tr,
        "translated_coefficients_divided_by_p": [c//p for c in tr],
        "c4": c4,
        "discriminant": delta,
        "v_p_c4": 1,
        "v_p_discriminant": 3,
        "P2_translated_reduction": [X,Y],
        "smoothness_derivative_2y_mod_p": 2*Y % p,
        "X_over_y_mod_p": X*pow(Y,-1,p) % p,
        "away_bad_quotient_orders_retained": quotients,
        "away_bad_quotients_prime_to_p": True,
        "addition_control": {
            "precision_modulus": modulus,
            "operations_with_unit_denominators": len(denominators),
            "point_p_minus_1_times_P2": list(A),
            "v_p_x_difference": 1,
            "v_p_y_sum": 1,
            "x_difference_over_p_mod_p": dx//p % p,
        },
        "linear_controls_not_seed_arithmetic": controls,
        "not_verified_by_script": [
            "component number 2",
            "Pannekoek theorem or local Tate duality",
            "global reciprocity or finite-group cohomology",
            "receiver identification or any upper bound",
            "new upper-control Lean modules",
        ],
    }
    out = Path(__file__).resolve().parent/'CHECK_RESULTS.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
