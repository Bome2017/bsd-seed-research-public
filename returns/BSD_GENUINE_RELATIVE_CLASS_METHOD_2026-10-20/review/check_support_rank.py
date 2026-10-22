#!/usr/bin/env python3
"""Independent F5 elimination of the saved projected ideal relations."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def rank(rows, columns):
    a = [[r[c] % 5 for c in columns] for r in rows]
    pivot = 0
    for c in range(len(columns)):
        k = next((j for j in range(pivot, len(a)) if a[j][c]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        inv = pow(a[pivot][c], -1, 5)
        a[pivot] = [(x * inv) % 5 for x in a[pivot]]
        for j in range(pivot + 1, len(a)):
            q = a[j][c]
            if q:
                a[j] = [(x - q * y) % 5 for x, y in zip(a[j], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def factor_through_private(rows, original, private):
    a = [[r[j - 1] % 5 for j in private + original] for r in rows]
    n, k = len(private), len(original)
    pivots = []
    for c in range(n):
        i = len(pivots)
        at = next((j for j in range(i, len(a)) if a[j][c]), None)
        if at is None:
            continue
        a[i], a[at] = a[at], a[i]
        inv = pow(a[i][c], -1, 5)
        a[i] = [x * inv % 5 for x in a[i]]
        for j in range(len(a)):
            q = a[j][c] if j != i else 0
            if q:
                a[j] = [(x - q * y) % 5 for x, y in zip(a[j], a[i])]
        pivots.append(c)
    assert all(not any(r[n:]) for r in a[len(pivots):])
    transform = [[0] * k for _ in range(n)]
    for i, c in enumerate(pivots):
        transform[c] = a[i][n:]
    for row in rows:
        for j, col in enumerate(original):
            assert sum(row[private[t] - 1] * transform[t][j]
                       for t in range(n)) % 5 == row[col - 1] % 5
    return transform


def main():
    src = ROOT / 'matrix_audit_input.gp'
    original, private, chi2, chi3 = ast.literal_eval(src.read_text())
    assert len(original) == 8 and len(private) == 177
    assert sorted(original + private) == list(range(1, 186))
    assert len(chi2) == len(chi3) == 196
    assert all(len(r) == 185 for r in chi2 + chi3)
    out, certificates = [], []
    for chi, rows in [(2, chi2), (3, chi3)]:
        full = rank(rows, list(range(185)))
        priv = rank(rows, [j - 1 for j in private])
        assert (full, priv) == (156, 156)
        certificates.append({'character_eigenvalue': chi,
                             'private_to_original': factor_through_private(
                                 rows, original, private)})
        out.append({'character_eigenvalue': chi, 'full_rank': full,
                    'private_rank': priv,
                    'rank_of_relations_supported_on_originals': full - priv,
                    'expanded_formal_quotient_dimension': 185 - full,
                    'original_image_upper_bound_from_these_rows': 8})
    certificate_path = ROOT / 'PRIVATE_FACTOR_CERTIFICATE.json'
    certificate_path.write_text(json.dumps({
        'identity': 'R_original = R_private * T over F5',
        'original_columns_1_based': original,
        'private_columns_1_based': private,
        'certificates': certificates}, indent=2) + '\n')
    result = {
        'status': 'NO_NEW_RELATION_BOUND_ON_ORIGINAL_EIGHT_GENERATORS',
        'rows': 196, 'columns': 185, 'original_columns': 8,
        'private_columns': 177, 'characters': out,
        'complete_class_bound': False,
        'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
        'private_factor_certificate_sha256': hashlib.sha256(
            certificate_path.read_bytes()).hexdigest(),
        'scope': 'Independent Python elimination after exact GP reconstruction of every divisor row. The 29-dimensional expanded formal quotient does not generate the full class group.'
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
