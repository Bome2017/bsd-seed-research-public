#!/usr/bin/env python3
"""Exact F3 class-image/point-image comparison; no arithmetic producer imports."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) % 3
             for col in transpose(b)] for row in a]


def rref(a, width=None):
    a = [[x % 3 for x in row] for row in a]
    width = len(a[0]) if a else width or 0
    pivots, i = [], 0
    for j in range(width):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        inv = pow(a[i][j], -1, 3)
        a[i] = [inv * x % 3 for x in a[i]]
        for k in range(len(a)):
            if k != i:
                factor = a[k][j]
                a[k] = [(x - factor * y) % 3 for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def null_rows(a, width):
    """A row list forming the kernel of a matrix with the given width."""
    r, pivots = rref(a, width)
    result = []
    for j in range(width):
        if j not in pivots:
            v = [0] * width
            v[j] = 1
            for i, p in enumerate(pivots):
                v[p] = -r[i][j] % 3
            result.append(v)
    return result


def unique_solve(a, b):
    """Full-column-rank A: solve AX=B, checking exact reconstruction."""
    n, k = len(a[0]), len(b[0])
    augmented = [x + y for x, y in zip(a, b)]
    r, pivots = rref(augmented)
    assert pivots == list(range(n)), 'basis incomplete or inconsistent solve'
    x = [row[n:n+k] for row in r[:n]]
    assert multiply(a, x) == b
    return x


def span_rows(a):
    """Exhaustive column span, as a set of tuples."""
    n = len(a[0])
    return {tuple(sum(a[i][j] * x[j] for j in range(n)) % 3
                  for i in range(len(a)))
            for x in itertools.product(range(3), repeat=n)}


def all_zero(a):
    return all(not x for row in a for x in row)


def run_case(case):
    m = json.loads((ROOT / 'inputs' / f'{case}_matrices.json').read_text())
    k = json.loads((ROOT / 'inputs' / f'{case}_coordinates.json').read_text())
    known, points, h0, units = k['known'], k['points'], m['valuation_zero_basis'], m['units']
    assert points == m['points']
    assert rank(known) == len(known[0])
    assert rank(points) == len(points[0])
    assert all_zero(multiply(m['valuation'], known))
    assert all_zero(multiply(m['valuation'], points))
    hk, hp, hu = [unique_solve(h0, x) for x in [known, points, units]]
    ck, cp = [multiply(m['class_boundary_H0'], x) for x in [hk, hp]]
    assert all_zero(multiply(m['class_boundary_H0'], hu))
    q = null_rows(transpose(cp), len(cp))
    qk = multiply(q, ck) if q else []
    sk, sp, su = span_rows(known), span_rows(points), span_rows(units)
    sck, scp = span_rows(ck), span_rows(cp)
    assert sp <= sk and scp <= sck
    unit_intersection = sk & su
    point_unit_intersection = sp & su
    # Exhaustive comparison independently checks the quotient rank calculation.
    cosets = {frozenset(tuple((x-y) % 3 for x, y in zip(c, p))
                       for p in scp) for c in sck}
    qrank = rank(ck) - rank(cp)
    assert len(cosets) == 3 ** qrank
    assert rank(qk) == qrank
    class_zero_in_known = []
    class_point_in_known = []
    for x in itertools.product(range(3), repeat=len(known[0])):
        image = tuple(sum(ck[i][j] * x[j] for j in range(len(x))) % 3
                      for i in range(len(ck)))
        if not any(image):
            class_zero_in_known.append(list(x))
        if image in scp:
            class_point_in_known.append(list(x))
    assert len(class_zero_in_known) == len(unit_intersection)
    if case == 'seed3':
        witnessed_unit = [[1, 0], [0, 0], [0, 1], [0, 2]]
        assert span_rows(multiply(known, witnessed_unit)) == unit_intersection
        assert span_rows([[row[0]] for row in points]) == point_unit_intersection
        labels = ['P1', 'P2', 'beta1', 'beta2']
    else:
        witnessed_unit = [[0, 0], [1, 0], [0, 1]]
        assert span_rows(multiply(known, witnessed_unit)) == unit_intersection
        labels = ['P', 'unit1', 'unit2']
    return {
        'case': case,
        'known_column_labels': labels,
        'source_dimension': m['source_dimension'],
        'known_rank': rank(known), 'point_rank': rank(points),
        'all_known_and_point_valuations_zero': True,
        'H0_basis': h0, 'class_boundary_on_H0': m['class_boundary_H0'],
        'known_H0_coordinates': hk, 'point_H0_coordinates': hp,
        'known_class_image': ck, 'point_class_image': cp,
        'point_image_annihilator': q, 'class_quotient_matrix': qk,
        'known_class_image_rank': rank(ck), 'point_class_image_rank': rank(cp),
        'class_supported_excess_image_rank': qrank,
        'provided_unit_intersection_size': len(unit_intersection),
        'point_unit_intersection_size': len(point_unit_intersection),
        'unit_excess_quotient_size': len(unit_intersection) // len(point_unit_intersection),
        'unit_witness_coordinates_in_known_basis': witnessed_unit,
        'class_zero_known_coordinates': class_zero_in_known,
        'class_in_point_image_known_coordinates': class_point_in_known,
        'enumerated_class_quotient_cosets': len(cosets),
        'all_exhaustive_and_matrix_checks_pass': True,
    }


def main():
    bindings = json.loads((ROOT / 'INPUT_BINDINGS.json').read_text())
    for row in bindings:
        assert hashlib.sha256((ROOT / row['copy']).read_bytes()).hexdigest() == row['sha256']
    result = {'field': 'F3', 'cases': [run_case(c) for c in ['seed3', '28042a1']]}
    (ROOT / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    for row in result['cases']:
        print(row['case'], 'class image=', row['known_class_image'],
              'point image=', row['point_class_image'],
              'quotient=', row['class_quotient_matrix'],
              'quotient rank=', row['class_supported_excess_image_rank'])
    print('CLASS_IMAGE_QUOTIENT_CHECK_PASSED')


if __name__ == '__main__':
    main()
