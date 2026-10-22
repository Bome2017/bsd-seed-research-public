#!/usr/bin/env python3
"""Exact C13 evaluation; independent Fermat and full depth-two routes.

Uses the certified symbols as rational numbers, not their lattice numerators.
Checks the same formulas against the retained C7 and C11 results.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, isqrt
from datetime import datetime, timezone
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parent
MASTER = ROOT.parents[2]
RUN13 = Path('/Users/bsm/BSD_SEED_P13_RUN_2026-09-21/run')
GATE = MASTER / '_work/bridge_repair_assessment_2026-09-21/P13_EVALUATION_GATE.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_symbols(run, m):
    plus, minus = {}, {}
    for line in (run / f'SYMBOLS_m{m}.txt').read_text().splitlines():
        if not line or line.startswith('#'):
            continue
        b, x, y = line.split()
        b = int(b)
        assert b not in plus
        plus[b], minus[b] = Fraction(x), Fraction(y)
    return plus, minus


def evaluate(p, run, declared=None):
    checks = []

    def check(ok, label):
        checks.append({'name': label, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(label)

    def residue(q, modulus):
        q = Fraction(q)
        assert q.denominator % p
        return q.numerator * pow(q.denominator, -1, modulus) % modulus

    high, minus_high = read_symbols(run, p*p)
    low, minus_low = read_symbols(run, p)
    primes = [q for q in range(2, p+1) if all(q % d for d in range(2, isqrt(q)+1))]
    with (run/'ap/ap_000000.bin').open('rb') as handle:
        ap = struct.unpack('<'+'i'*len(primes), handle.read(4*len(primes)))[-1]
    card = 1 + sum(y*y % p == (x**3-22735*x*x+106272484*x) % p
                   for x in range(p) for y in range(p))
    check(ap == p+1-card, 'trace matches exact point count')
    for m, pos, neg in [(p*p, high, minus_high), (p, low, minus_low)]:
        check(set(pos) == set(neg) == {b for b in range(1,m) if b%p}, f'complete units at {m}')
        check(all(pos[b] == pos[m-b] and neg[b] == -neg[m-b] for b in pos), f'conjugation at {m}')
        check(all((1024*q).denominator == 1 and q.denominator%p
                  for q in [*pos.values(), *neg.values()]), f'lattice and p-integrality at {m}')
    check(sum(low.values()) == 0, 'zero-cusp Hecke sum')
    check(all(ap*l[b] == sum(h[b+p*j] for j in range(p))
              for l,h in [(low,high),(minus_low,minus_high)] for b in l), 'both-sign Hecke relations')

    # A: Fermat quotients, followed by conjugation folding.
    weights = {}
    for b in high:
        q = (pow(b,p-1,p*p)-1)//p
        j = q*pow(p-1,-1,p)%p
        weights[b] = pow(ap,-2,p)*comb(j,2)%p
    full = sum(weights[b]*high[b] for b in high)
    folded_weights = {b:(weights[b]+weights[p*p-b])%p
                      for b in high if b < p*p-b and (weights[b]+weights[p*p-b])%p}
    if declared is None:
        declared = {w:[b for b in folded_weights if folded_weights[b] == w]
                    for w in sorted(set(folded_weights.values()))}
    declared_flat = {b:int(w) for w,bs in declared.items() for b in bs}
    check(folded_weights == declared_flat, 'folded formula matches predeclared or regression groups')
    sums = {int(w):sum(high[b] for b in bs) for w,bs in declared.items()}
    folded = sum(w*q for w,q in sums.items())
    c = residue(full,p)
    check(residue(folded,p) == c, 'folded and full rational-symbol functional agree')

    # B: Hensel root and Teichmuller lifts, retaining the full lower-level term.
    k = 20
    modulus = p**k
    alpha = ap%p
    for _ in range(2*k):
        alpha = (alpha-(alpha*alpha-ap*alpha+p)*pow(2*alpha-ap,-1,modulus))%modulus
    check((alpha*alpha-ap*alpha+p)%modulus == 0 and alpha%p == ap%p, 'Hensel unit root')
    omega = {a:pow(a,p**k,modulus) for a in range(1,p)}
    check(all(pow(w,p-1,modulus) == 1 and w%p == a for a,w in omega.items()), 'Teichmuller lifts')
    ia = pow(alpha,-1,modulus)
    coefficients = [0,0,0]
    lower = 0
    seen = []
    for a,w in omega.items():
        for j in range(p):
            b = w*pow(1+p,j,p*p)%(p*p)
            seen.append(b)
            check(weights[b] == pow(ap,-2,p)*comb(j,2)%p, f'independent exponent b={b}')
            correction = ia**3*residue(low[b%p],modulus)%modulus
            measure = (ia**2*residue(high[b],modulus)-correction)%modulus
            for degree in range(3):
                coefficients[degree] = (coefficients[degree]+measure*comb(j,degree))%modulus
            lower = (lower+correction*comb(j,2))%modulus
    check(sorted(seen) == sorted(high), 'depth-two enumeration covers each unit once')
    check(coefficients[0] == 0, 'finite constant coefficient zero')
    check(coefficients[1]%p == 0, 'finite linear coefficient zero modulo p')
    check(lower%p == 0 and comb(p,3)%p == 0, 'lower-level quadratic correction zero modulo p')
    check(coefficients[2]%p == c, 'full depth-two measure agrees with Fermat route')

    result = {
        'p':p, 'a_p':ap, 'point_count':card, 'alpha_mod_p_squared':alpha%(p*p),
        'residue_omega1':c, 'residue_full_real_period':c*pow(2,-1,p)%p,
        'group_sums':{str(w):str(q) for w,q in sums.items()},
        'folded_exact_rational':str(folded),
        'folded_weights':{str(b):v for b,v in sorted(folded_weights.items())},
        'finite_P2_precision_exponent':k, 'finite_P2_coefficients':coefficients,
        'infinite_series_certified_digits':1, 'lower_correction_mod_p':lower%p,
        'all_checks_passed':all(c['passed'] for c in checks), 'checks':checks,
        'symbols':{f'SYMBOLS_m{m}.txt':{'path':str(run/f'SYMBOLS_m{m}.txt'),
                     'sha256':sha(run/f'SYMBOLS_m{m}.txt')} for m in [p*p,p]},
    }
    if p == 13:
        raw = sum(comb(-((pow(b,12,169)-1)//13)%13,2)*high[b] for b in high)
        check(1024%13 == 10 and pow(1024,-1,13) == 4, 'lattice scaling and inverse')
        check(pow(ap,-2,p) == 9 and pow(9,-1,p) == 3, 'missing alpha factor explains weight ratio')
        check(residue(1024*folded,p) == 7, 'reported gate residue reproduced from lattice numerators')
        check(residue(1024*raw,p) == 8, 'reported alternative residue reproduced with both missing factors')
        check(7*pow(1024,-1,p)%p == c == 8*pow(1024,-1,p)*9%p,
              'both returned residues correct to the same exact coefficient')
        result['normalization_reconciliation'] = {
            'lattice_numerator_factor_mod_13':10, 'lattice_inverse_mod_13':4,
            'unit_root_factor_mod_13':9, 'omission_ratio_mod_13':3,
            'raw_sum_without_unit_root':str(raw),
            'reported_7':residue(1024*folded,p), 'reported_8':residue(1024*raw,p),
            'corrected_from_7':7*4%p, 'corrected_from_8':8*4*9%p,
            'note':'The two occurrences of 4 (lattice inverse and interpolation factor) have different definitions.',
        }
        result['all_checks_passed'] = all(c['passed'] for c in checks)
    return result


receipt = json.loads((ROOT/'INPUT_BINDINGS.json').read_text())
for item in receipt['original_files']:
    assert sha(Path(item['path'])) == item['sha256'], item['path']
gate = json.loads(GATE.read_text())
regressions = []
for p, expected in [(7,1),(11,8)]:
    r = evaluate(p,ROOT.parent/f'p{p}/run')
    assert r['residue_omega1'] == expected
    regressions.append({k:r[k] for k in ['p','residue_omega1','residue_full_real_period','all_checks_passed','symbols']})
result = evaluate(13,RUN13,gate['predeclared_folded_groups'])
result.update({'status':'P13_COEFFICIENT_UNIT_PROVED' if result['residue_omega1'] else 'P13_UNIT_TEST_INCONCLUSIVE',
               'recorded_at_utc':datetime.now(timezone.utc).isoformat(), 'regressions':regressions,
               'scope':'Exact arithmetic on imported certified symbols; no additional digits of the infinite series or independent numerical implementation'})
(ROOT/'DOWNSTREAM.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','residue_omega1','residue_full_real_period','group_sums',
    'folded_exact_rational','normalization_reconciliation']},indent=2))
print('ALL_CHECKS_PASS',len(result['checks']),'C7_C11_REGRESSIONS_PASS')
