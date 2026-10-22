#!/usr/bin/env python3
"""Independently classify private prime support and audit complete-bound rank."""
import ast
import hashlib
import json
from pathlib import Path
from check_support_rank import rank, factor_through_private

ROOT = Path(__file__).resolve().parent
BOUND = 419775


def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2, int(n ** 0.5) + 1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b'\x00' * ((n-q*q)//q+1)
    return [q for q in range(2, n+1) if sieve[q]]


def main():
    source = ROOT/'private_support_audit_input.gp'
    rows = ast.literal_eval(source.read_text())
    original, private, r2, r3 = ast.literal_eval(
        (ROOT/'matrix_audit_input.gp').read_text())
    primes = primes_to(BOUND)
    assert len(primes) == 35373
    inside, outside, cofactors = [], [], []
    for col, atom, norm, claimed_outside, ideal_factors in rows:
        remainder = norm
        for q in primes:
            while remainder % q == 0:
                remainder //= q
            if remainder == 1:
                break
        if remainder > 1:
            # Every rational prime factor of this residual is >BOUND.
            # Such a factor in the ideal norm proves outside prime support.
            assert claimed_outside == 1
            outside.append(col)
            cofactors.append([col, str(remainder)])
        else:
            # Small rational factors alone are insufficient: a prime ideal
            # may have norm q^f>BOUND. The exact GP factorization authenticates
            # each degree and exponent and reconstructs the actual ideal.
            assert claimed_outside == 0 and ideal_factors
            product = 1
            for q, degree, exponent, ideal_norm in ideal_factors:
                assert q ** degree == ideal_norm <= BOUND
                product *= ideal_norm ** exponent
            assert product == norm
            inside.append(col)
    assert len(inside) == 21 and len(outside) == 156
    assert sorted(inside + outside) == sorted(private)
    bounded_selected = sorted(original + inside)
    results, factors = [], []
    for chi, matrix in [(2, r2), (3, r3)]:
        total_rank = rank(matrix, list(range(185)))
        outside_rank = rank(matrix, [j-1 for j in outside])
        assert total_rank == outside_rank == 156
        factors.append({'character_eigenvalue': chi,
                        'outside_to_bounded_selected': factor_through_private(
                            matrix, bounded_selected, outside)})
        results.append({'character_eigenvalue': chi,
                        'total_relation_rank': total_rank,
                        'outside_support_rank': outside_rank,
                        'net_relation_rank_on_bounded_generators':
                            total_rank-outside_rank,
                        'retained_GRH_complete_generator_count': 8918,
                        'formal_complete_bound_after_adding_rows':
                            8918+len(outside)-total_rank})
    cert = ROOT/'OUTSIDE_SUPPORT_FACTOR_CERTIFICATE.json'
    cert.write_text(json.dumps({
        'identity':'R_bounded_selected=R_outside*T over F5',
        'bounded_selected_columns_1_based': bounded_selected,
        'outside_columns_1_based': outside,
        'factor_certificates': factors},indent=2)+'\n')
    result = {
        'status':'COMPLETE_GRH_GENERATOR_BOUND_UNIMPROVED',
        'support_cutoff':BOUND,'rational_primes_tested_per_norm_up_to':BOUND,
        'classification_method':'Independent exhaustive integer trial division; actual ideal factorizations and residue degrees for all21 inside symbols',
        'inside_private_orbits':len(inside),'outside_private_orbits':len(outside),
        'outside_cofactors_after_all_small_primes_removed':cofactors,
        'characters':results,
        'unconditional_generation_certified':False,
        'new_seed_complete_bound':False,
        'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'factor_certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
