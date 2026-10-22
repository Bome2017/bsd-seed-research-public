#!/usr/bin/env python3
"""Exact local-coordinate arithmetic only; does not verify the imported Sha theorem."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path

A2, A4, P = -22735, 106272484, 11
POINTS = {
    'P1': (Fraction(4547), Fraction(327384)),
    'P2': (Fraction(5184), Fraction(281520)),
}


def on_curve(point):
    if point is None:
        return True
    x, y = point
    return y*y == x*x*x + A2*x*x + A4*x


def add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and y == -v:
        return None
    slope = ((3*x*x + 2*A2*x + A4)/(2*y)
             if left == right else (v-y)/(u-x))
    x3 = slope*slope - A2 - x - u
    out = (x3, slope*(x-x3)-y)
    assert on_curve(out)
    return out


def multiply(n, point):
    out = None
    while n:
        if n & 1:
            out = add(out, point)
        point = add(point, point)
        n //= 2
    return out


def valuation(value):
    if value == 0:
        return None
    a, b = value.numerator, value.denominator
    va = vb = 0
    while a % P == 0:
        va += 1
        a //= P
    while b % P == 0:
        vb += 1
        b //= P
    return va-vb


def residue(value, modulus):
    assert value.denominator % P != 0
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def main():
    # Good reduction: discriminant of y^2=x^3+a2*x^2+a4*x.
    discriminant = 16*A4*A4*(A2*A2-4*A4)
    assert discriminant % P != 0
    reduction_order = 1 + sum(
        (y*y-x*x*x-A2*x*x-A4*x) % P == 0
        for x in range(P) for y in range(P))
    assert reduction_order == 14
    rows = {}
    for name, point in POINTS.items():
        assert on_curve(point)
        q = multiply(reduction_order, point)
        repeated = None
        for _ in range(reduction_order):
            repeated = add(repeated, point)
        assert q == repeated  # Different addition schedule, same implementation.
        assert q is not None and valuation(q[0]) < 0
        t = -q[0]/q[1]
        assert valuation(t) >= 1
        t_mod = residue(t, P*P)
        rows[name] = {
            'x14_valuation': valuation(q[0]),
            'y14_valuation': valuation(q[1]),
            't14_mod121': t_mod,
            'local_coordinate_mod11': (t_mod//P)*pow(reduction_order, -1, P) % P,
        }
    assert rows['P1']['t14_mod121'] == 33
    assert rows['P2']['t14_mod121'] == 66
    assert [rows[n]['local_coordinate_mod11'] for n in POINTS] == [1, 2]
    minus_p2 = (POINTS['P2'][0], -POINTS['P2'][1])
    candidate = add(multiply(2, POINTS['P1']), minus_p2)
    q = multiply(reduction_order, candidate)
    assert q is not None and valuation(q[0]) < 0
    t_candidate = -q[0]/q[1]
    assert valuation(t_candidate) >= 2
    assert residue(t_candidate, P*P) == 0
    out = {
        'status': 'EXACT_LOCAL_COORDINATES_PASS',
        'arithmetic': 'Python integer and Fraction arithmetic; no floating point',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'good_reduction_at11': True,
        'reduction_order': reduction_order,
        'coordinate_definition': '14^(-1) * t([14]Q)/11 mod11, t=-x/y',
        'points': rows,
        'kernel_coefficients_mod11': [2, 10],
        't_of_14_kernel_point_valuation': valuation(t_candidate),
        't_of_14_kernel_point_mod121': residue(t_candidate, P*P),
        'scope': 'Finite exact arithmetic supporting the written localization corollary; imported global theorem not checked here',
        'independent_implementation': False,
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
