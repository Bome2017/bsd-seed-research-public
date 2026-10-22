#!/usr/bin/env python3
"""Exact cyclotomic calculations on a pinned seed table. NOT a Sha verifier.
Run from any directory: python3 checks/verify.py > checks/RESULTS.json
Standard library only. Coefficients of all polynomials are in ascending order.
"""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHI5 = [1, 1, 1, 1, 1]
PHI25 = [1 if i % 5 == 0 else 0 for i in range(21)]
TABLE_BLOB = 'b0d766f63e90ac9d17b2ca15ee2e387cd6b34ff6'


def check(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def trim(a: list[int]) -> list[int]:
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)


def scale(a: list[int], c: int) -> list[int]:
    return trim([c * x for x in a])


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return trim(out)


def rem(a: list[int], f: list[int]) -> list[int]:
    check(f[-1] == 1, 'only monic moduli are allowed')
    a = trim(a)
    while len(a) >= len(f):
        k, c = len(a) - len(f), a[-1]
        for j, x in enumerate(f): a[k + j] -= c * x
        a = trim(a)
    return a


def power(a: list[int], n: int, f: list[int]) -> list[int]:
    check(type(n) is int and n >= 0, 'nonnegative integral exponent required')
    ans = [1]
    while n:
        if n & 1: ans = rem(mul(ans, a), f)
        a = rem(mul(a, a), f)
        n //= 2
    return ans


def compose(a: list[int], b: list[int], f: list[int]) -> list[int]:
    ans = [0]
    for c in reversed(a): ans = rem(add(mul(ans, b), [c]), f)
    return ans


def det(a: list[list[int]]) -> int:
    """Exact Gaussian elimination over Q, independent of cyclotomic conjugation."""
    n = len(a)
    check(all(len(row) == n for row in a), 'matrix must be square')
    b = [[Fraction(c) for c in row] for row in a]
    ans = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if b[i][j]), None)
        if pivot is None: return 0
        if pivot != j:
            b[j], b[pivot] = b[pivot], b[j]
            ans = -ans
        p = b[j][j]
        ans *= p
        for i in range(j + 1, n):
            ratio = b[i][j] / p
            for k in range(j + 1, n): b[i][k] -= ratio * b[j][k]
            b[i][j] = 0
    check(ans.denominator == 1, 'integral matrix has integral determinant')
    return ans.numerator


def norm(a: list[int], f: list[int]) -> int:
    d = len(f) - 1
    cols = [rem([0] * j + a, f) for j in range(d)]
    return det([[cols[j][i] if i < len(cols[j]) else 0
                 for j in range(d)] for i in range(d)])


def main() -> dict:
    raw = (ROOT / 'inputs/SYMBOLS_m25.txt').read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    check(blob == TABLE_BLOB, 'pinned input table changed')
    symbols = {}
    for line in raw.decode().splitlines():
        if not line or line.startswith('#'): continue
        b, plus, minus = map(int, line.split())
        check(b not in symbols, 'duplicate numerator')
        symbols[b] = (plus, minus)
    units = [a for a in range(1, 25) if a % 5]
    check(sorted(symbols) == units, 'exactly the 20 units are required')
    delta = [a for a in units if pow(a, 4, 25) == 1]
    check(delta == [1, 7, 18, 24], 'Teichmuller subgroup')
    logs = {}
    for j in range(5):
        for d in delta:
            a = d * pow(6, j, 25) % 25
            check(a not in logs, 'disjoint cosets')
            logs[a] = j
    for a in units:
        independent_j = 4 * ((pow(a, 4, 25) - 1) // 5) % 5
        check(logs[a] == independent_j, 'independent quartic-power character map')
        check(symbols[25-a][0] == symbols[a][0], 'even plus table')
        check(symbols[25-a][1] == -symbols[a][1], 'odd minus table')
    grouped = [sum(symbols[a][0] for a in units if logs[a] == j) for j in range(5)]
    check(grouped == [-76, 0, -76, 76, 76], 'grouped seed symbols')
    check(all(v % 2 == 0 for v in grouped), 'full real period factor')
    A = [v // 2 for v in grouped]
    factor = scale(mul(mul([0, 0, 1], [1, 1]), [1, -2, 1]), -38)
    check(rem(A, PHI5) == rem(factor, PHI5), 'exact factorization')
    conjugates = [compose(A, power([0, 1], k, PHI5), PHI5) for k in range(1, 5)]
    product = [1]
    for c in conjugates: product = rem(mul(product, c), PHI5)
    expected_norm = 38**4 * 25
    check(product == [expected_norm], 'product of the four conjugates')
    check(norm(A, PHI5) == expected_norm, 'independent multiplication-matrix norm')
    unit = scale(mul([0, 0, 1], [1, 1]), -1)
    check(norm(unit, PHI5) == 1 and norm([-1, 1], PHI5) == 5,
          'unit and cyclotomic prime norms')
    taus = []
    for k in range(1, 5):
        tau = [0]
        for a in units:
            exponent = (a + 5 * k * logs[a]) % 25
            tau = add(tau, [0] * exponent + [1])
        taus.append(rem(tau, PHI25))
    check(rem(mul(taus[0], taus[3]), PHI25) == [25], 'first exact Gauss pair')
    check(rem(mul(taus[1], taus[2]), PHI25) == [25], 'second exact Gauss pair')
    twist_product = Fraction(expected_norm, 625)
    check(twist_product == Fraction(38**4, 25), 'complex twist product')
    # Exact Gaussian-period model for the degree-five field, not its integral basis.
    eta = [0]
    for d in delta: eta = add(eta, power([0, 1], d, PHI25))
    minimal = [1, 10, 5, -10, 0, 1]
    check(compose(minimal, eta, PHI25) == [0], 'field polynomial')
    eta_conjugates = [compose(eta, power([0, 1], pow(6, j, 25), PHI25), PHI25)
                      for j in range(5)]
    check(len({tuple(c) for c in eta_conjugates}) == 5, 'field degree exactly five')
    derivative = [i * minimal[i] for i in range(1, len(minimal))]
    polynomial_disc = norm(derivative, minimal)  # sign (-1)^10 is positive
    field_disc = 25**4  # conductor-discriminant theorem, proved in PROOF.md
    check(polynomial_disc == 7**2 * field_disc, 'polynomial vs field discriminant')
    rows = []
    local = [(2, 'I1*', 2), (3, 'I2 nonsplit', 2), (2243, 'I1 split', 1),
             (4547, 'III', 2), (5843, 'I2 nonsplit', 2)]
    Cq = Cf = 1
    for q, reduction, c in local:
        j = logs[q % 25]
        degree = 1 if j == 0 else 5
        places = 5 // degree
        Cq *= c
        Cf *= c**places
        rows.append({'q': q, 'reduction_retained': reduction, 'character_exponent': j,
                     'residue_degree': degree, 'number_of_places': places,
                     'c_per_place_under_unramified_odd_degree_base_change': c})
    check(Cq == 16 and Cf == 256, 'Tamagawa products from retained local types')
    height_ratio = 5**2  # actual point equality plus degree-scaled height
    relative = twist_product * 625 / height_ratio * Fraction(Cq, Cf)
    check(relative == 19**4, 'relative BSD-normalized leading term')
    # Factorization above 19: both quadratic factors are irreducible.
    q1, q2 = [1, 5, 1], [1, -4, 1]
    check(all((a-b) % 19 == 0 for a,b in zip(mul(q1,q2), PHI5)), 'Phi5 mod 19')
    check(all(sum(c * pow(t, i, 19) for i,c in enumerate(q)) % 19
              for q in (q1,q2) for t in range(19)), 'quadratic irreducibility')
    # Show explicitly that commonly omitted normalization factors change the result.
    wrong = {'primitive_not_full_real_period': relative * 16,
             'absolute_not_relative_height': relative * 25,
             'polynomial_not_field_discriminant': relative * 7,
             'omitted_tamagawa_ratio': relative * 16}
    check(all(v != relative for v in wrong.values()), 'normalization countercontrols')
    return {'status': 'PASS_EXACT_RELATIVE_ANALYTIC_CALCULATION_NOT_A_SHA_ORDER',
            'input_git_blob': blob, 'input_sha256': hashlib.sha256(raw).hexdigest(),
            'input_symbol_rows': 20, 'character_map_controls': 20,
            'raw_grouped_symbols': grouped, 'full_period_coefficients': A,
            'normalized_character_values_mod_Phi5': conjugates,
            'norm_by_two_exact_methods': expected_norm, 'gauss_pair_products': [25,25],
            'product_twisted_L_over_Omega_to_four': str(twist_product),
            'field_polynomial_ascending': minimal, 'field_discriminant': field_disc,
            'polynomial_discriminant': polynomial_disc, 'power_basis_index': 7,
            'local_rows': rows, 'C_Q': Cq, 'C_F': Cf, 'Reg_F_over_Reg_Q': height_ratio,
            'relative_BSD_normalized_analytic_factor': int(relative),
            'Phi5_mod19_factors_ascending': [q1,q2],
            'normalization_countercontrols': {k:int(v) for k,v in wrong.items()},
            'conditional_value_if_Q36': 9*19**4,
            'actual_Sha_order_inferred': False, 'new_symbol_values': 0,
            'new_padic_coefficient_digits': 0, 'FIN':'UNCHANGED',
            'ORDER9':'UNCHANGED', 'Q36':'UNCHANGED'}

if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
