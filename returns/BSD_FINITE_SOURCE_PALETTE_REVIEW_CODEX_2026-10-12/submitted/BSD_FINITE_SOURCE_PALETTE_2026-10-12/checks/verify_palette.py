#!/usr/bin/env python3
"""Exact controls for a finite Kato-source palette; this is NOT a Sha verifier.

Run: python3 checks/verify_palette.py > checks/RESULTS.json
Uses only the standard library. No modular symbols, Kato coefficients, heights,
Selmer groups, or global residual-image theorems are computed by this script.
"""
from __future__ import annotations
import json
from itertools import combinations
from math import gcd, isqrt

N = 2**3 * 3 * 2243 * 4547**2 * 5843
M = 6 * N
C = tuple(1 + i * M for i in (1, 2, 3))
PAIRS = tuple(combinations(range(3), 2))
EXCLUDED = {19, 59, 487}

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))

def smoothing(c: int, d: int) -> int:
    return c * d * (c - 1) * (d - 1)

def select_pair(p: int) -> tuple[int, int]:
    if not prime(p) or p < 5 or N % p == 0:
        raise ValueError('requires a good prime p >= 5')
    for i, j in PAIRS:
        if smoothing(C[i], C[j]) % p:
            return i, j
    raise AssertionError('palette coverage theorem failed')

def count_legendre(p: int) -> int:
    total = 1  # point at infinity
    for x in range(p):
        rhs = (x**3 - x*x - 66020924*x - 65074271436) % p
        total += 1 if rhs == 0 else (2 if pow(rhs, (p-1)//2, p) == 1 else 0)
    return total

def count_squares(p: int) -> int:
    multiplicity = [0] * p
    for y in range(p):
        multiplicity[y*y % p] += 1
    return 1 + sum(multiplicity[(x**3-x*x-66020924*x-65074271436) % p]
                   for x in range(p))

def main() -> dict:
    require(N == 6503188012738584, 'conductor product')
    require(all(gcd(c, 6*N) == 1 and (c-1) % N == 0 for c in C), 'source admissibility')
    require(all(gcd(C[i], C[j]) == 1 for i, j in PAIRS), 'pair coprimality')
    augmentations = [smoothing(C[i], C[j]) for i, j in PAIRS]
    require(gcd(*augmentations) == M*M, 'exact seed augmentation gcd')
    gcd_controls = 0
    for k in range(1, 101):
        m = 6*k
        cs = [1+i*m for i in (1, 2, 3)]
        require(gcd(*(smoothing(cs[i], cs[j]) for i,j in PAIRS)) == m*m,
                'universal-form gcd control')
        gcd_controls += 1
    coverage_controls = 0
    bad_modulus_controls = 0
    tested_primes = [p for p in range(5, 102) if prime(p)]
    for p in tested_primes:
        for residue in range(1, p):
            cs = [1+i*residue for i in (1,2,3)]
            active = [(i,j) for i,j in PAIRS if smoothing(cs[i], cs[j]) % p]
            require(bool(active), 'coverage for nonzero M residue')
            require(sum(c % p == 0 for c in cs) <= 1, 'at most one unavailable c')
            coverage_controls += 1
        require(all(smoothing(1,1) % p == 0 for _ in PAIRS), 'bad-modulus control')
        bad_modulus_controls += 1
    fixed_vector_controls = 0
    for p in (5,7,11,13):
        fixed = [(x,y) for x in range(p) for y in range(p)
                 if (x+y) % p == x and (x+y) % p == y]
        require(fixed == [(0,0)], 'common invariants of the two unipotents')
        fixed_vector_controls += p*p
    rows = []
    for p in (5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,487):
        n1, n2 = count_legendre(p), count_squares(p)
        require(n1 == n2, 'independent small-field point counts')
        ap = p+1-n1
        i,j = select_pair(p)
        require(gcd(C[i]*C[j], 6*p*N) == 1, 'selected source coprimality')
        require(smoothing(C[i], C[j]) % p != 0, 'selected augmentation unit')
        rows.append({'p': p, 'a_p': ap, 'pair': [i+1,j+1],
                     'ordinary': ap % p != 0,
                     'in_cohomological_domain': p not in EXCLUDED,
                     'ordinary_ratio_domain': p not in EXCLUDED and ap % p != 0,
                     'smoothing_augmentation_mod_p': smoothing(C[i], C[j]) % p,
                     'actual_coefficient_evaluated': False,
                     'sha_conclusion': None})
    invalid = (0,1,2,3,4,9,True,2243,4547,5843)
    for p in invalid:
        try:
            select_pair(p)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid input accepted')
    require(C[0] % 5 == 0, 'single-source countercontrol at p=5')
    require(select_pair(5) == (1,2), 'fallback at p=5')
    require(144 % 3 == 0 and all(144 % p for p in tested_primes), 'period-anchor support')
    return {'status': 'PASS_EXACT_SOURCE_CONTROLS_NOT_A_SHA_CERTIFICATE',
            'N': N, 'M': M, 'c_values': C,
            'augmentation_gcd': gcd(*augmentations),
            'universal_form_gcd_controls': gcd_controls,
            'residual_coverage_controls': coverage_controls,
            'bad_modulus_controls': bad_modulus_controls,
            'unipotent_fixed_vector_inputs': fixed_vector_controls,
            'invalid_input_controls': len(invalid),
            'independent_seed_point_counts': len(rows),
            'rows': rows,
            'retained_not_replayed': ['global residual surjectivity', 'Manin-constant input',
                                     'symbol [1/5]^+=144', 'all Kato/BKS hypotheses'],
            'new_K_values': 0, 'new_primary_conclusions': 0,
            'FIN': 'UNCHANGED', 'ORDER9': 'UNCHANGED', 'Q36': 'UNCHANGED'}

if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
