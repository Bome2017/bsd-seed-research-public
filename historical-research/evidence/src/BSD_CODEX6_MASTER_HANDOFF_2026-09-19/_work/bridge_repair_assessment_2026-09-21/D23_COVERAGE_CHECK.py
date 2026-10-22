#!/usr/bin/env python3
"""Exact bounded check of the existing D=-23 comparison's prime hypotheses."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import struct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TWIST = ROOT / '_work/d23_twist_2026-09-21'
N = 2**3 * 3 * 2243 * 4547**2 * 5843
D = -23
LIMIT = 160
primes = [p for p in range(2, LIMIT + 1)
          if all(p % d for d in range(2, math.isqrt(p) + 1))]
binding = json.loads((TWIST / 'INPUT_BINDINGS.json').read_text())['segments'][0]['coefficients']
data = Path(binding['path']).read_bytes()
assert hashlib.sha256(data).hexdigest() == binding['sha256']
assert len(data) == binding['bytes']
coefficients = struct.unpack('<' + 'i' * len(primes), data[:4 * len(primes)])
rows = []
for p, retained_ap in zip(primes, coefficients):
    if p < 5:
        continue
    # Every tested p is good: the only bad primes below 160 are 2 and 3.
    assert N % p
    squares = [0] * p
    for y in range(p):
        squares[y*y % p] += 1
    card = 1 + sum(squares[(x**3 - 22735*x*x + 106272484*x) % p]
                   for x in range(p))
    ap = p + 1 - card
    assert ap == retained_ap, (p, ap, retained_ap)
    legendre = pow(D % p, (p - 1) // 2, p)
    if legendre == p - 1:
        legendre = -1
    failures = []
    if p in (19, 59, 487):
        failures.append('excluded by regime P')
    if ap % p == 0:
        failures.append('supersingular')
    if card % p == 0:
        failures.append('anomalous')
    if legendre == 0:
        failures.append('ramified in K')
    elif legendre == -1:
        failures.append('inert in K')
    rows.append({'p': p, 'a_p': ap, 'card_E_Fp': card,
                 'chi_minus23': legendre, 'served': not failures,
                 'exclusion_reasons': failures})
served = [r['p'] for r in rows if r['served']]
claimed = [13, 31, 41, 47, 71, 73, 101, 127, 139, 151]
assert served == claimed, served

# Exact rational enclosure arithmetic; no approximate printed equality is used.
center = Fraction('39.847278312318874')
radius = Fraction('4.28e-16')
tail = Fraction('0.335041797049')
lo = center - radius - tail
hi = center + radius + tail
final_lo = Fraction('39.512236')
final_hi = Fraction('40.182321')
assert final_lo <= lo <= hi <= final_hi

report = {
    'result': 'EXACT_COVERAGE_CHECK_PASS',
    'range': 'all primes 5 <= p <= 160',
    'D': D,
    'coefficient_source': binding,
    'independent_method': 'enumerate square multiplicities and count points over each finite field',
    'all_checked_good_prime_traces_match_retained_corpus': True,
    'checked_good_prime_count': len(rows),
    'served_primes': served,
    'rows': rows,
    'interval_arithmetic': {
        'lower_exact': str(lo), 'upper_exact': str(hi),
        'outward_final_interval_confirmed': True,
        'comparison': 'finite-ball lower endpoint exceeds the tail; no value is claimed equal to the midpoint',
    },
    'scope': 'Bounded local applicability check only; imports retained source composition and certified twist rank. No Stark ideal evaluation, Sha vanishing, FIN, ORDER9 or Q36.',
}
assert len(rows) == 35
(HERE / 'D23_COVERAGE_CHECK.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'result': report['result'], 'checked_good_prime_count': len(rows),
                  'served': [{k:r[k] for k in ['p','a_p','card_E_Fp']} for r in rows if r['served']],
                  'special': [r for r in rows if r['p'] in [11,19,23,29,59,131]],
                  'interval_arithmetic': report['interval_arithmetic']}, indent=2))
