#!/usr/bin/env python3
"""Exact reconstruction from saved rational modular-symbol rows.

No L-function evaluation or rational recognition. This checks saved rows,
not the modular-symbol engine that generated them.
"""
import ast
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def legendre(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)


def point_count(p):
    return 1 + sum(
        (y*y + y - x*x*x - x*x + 36*x - 20) % p == 0
        for x in range(p) for y in range(p)
    )


def count_by_discriminant(p):
    if p == 2:
        return point_count(p)
    return 1 + sum(1 + legendre(1 + 4*(x*x*x+x*x-36*x+20), p)
                   for x in range(p))


def valuation(n, p):
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


out = {'curve': '6465c1', 'model': [0, 1, 1, -36, 20],
       'status': 'NOT_ADMITTED_NONUNIT_TWIST_FACTORS',
       'scope': 'exact saved-row arithmetic plus independent point counts',
       'twists': [], 'frobenius': [], 'hashes': {}}
for q in (83, 107):
    path = BASE / f'rows_{q}.gp'
    rows = ast.literal_eval(path.read_text())
    assert len(rows) == q - 1
    assert all(isinstance(c, int) for row in rows for c in row)
    for a, chi, symbol in rows:
        assert a in range(1, q)
        # For q = 3 mod 4, chi_{-q}(a) equals the Legendre symbol (a/q).
        assert chi == legendre(a, q)
        assert rows[q-a-1][2] == -symbol
    assert [row[0] for row in rows] == list(range(1, q))
    s = sum(chi*symbol for _, chi, symbol in rows)
    assert s == 20
    assert s % 2 == 0
    out['twists'].append({
        'D': -q, 'rows': len(rows), 'row_denominator': 1,
        'odd_symmetry': True, 'pure_imaginary_eigencycle_factor': s,
        'historical_twice_imaginary_period_factor': s // 2,
        'valuation_at_5': valuation(s, 5),
        'v5_of_historical_factor': valuation(s // 2, 5),
        'is_5_adic_unit': False,
        'character_at_2_3_5_431': [(-1 if (-q) % 8 == 5 else 1)] +
                                  [legendre(-q, p) for p in (3, 5, 431)]})
for p in (2, 7, 11, 13, 19):
    count = point_count(p)
    assert count == count_by_discriminant(p)
    a = p + 1 - count
    out['frobenius'].append({'prime': p, 'point_count': count, 'a': a,
                            'characteristic_discriminant_mod5': (a*a-4*p) % 5})
assert out['frobenius'][2]['characteristic_discriminant_mod5'] == 2
for name in ('exact_twists.gp', 'exact_twists.out', 'exact_twists.err',
             'exact_symbol.gp', 'rows_83.gp', 'rows_107.gp',
             'verify_symbol.gp', 'verify_symbol.out', 'verify_symbol.err'):
    out['hashes'][name] = hashlib.sha256((BASE/name).read_bytes()).hexdigest()
print(json.dumps(out, indent=2, sort_keys=True))
