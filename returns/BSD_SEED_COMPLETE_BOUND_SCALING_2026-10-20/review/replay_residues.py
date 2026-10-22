#!/usr/bin/env python3
"""Independent direct multiplicative extraction at one sufficient split prime."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "same_curve_scaling"
q = 18541
F, X, Y, sigma, units = json.loads((SOURCE / "eval_data.json").read_text())
table = dict(json.loads((SOURCE / "split_primes.json").read_text()))
roots = table[q]
assert all(q % d for d in range(2, 137))
assert (q - 1) % 5 == 0 and len(set(roots)) == 24


def pack(v):
    return tuple(v[0]), v[1]


@lru_cache(None)
def evaluation(v, r):
    coefficients, denominator = v
    assert denominator % q
    return sum(c * pow(r, i, q) for i, c in enumerate(coefficients)) * pow(denominator, -1, q) % q


def plus(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    xx, yy = Q
    if x == xx and (y + yy) % q == 0:
        return None
    numerator, denominator = ((3 * x * x - 4, 2 * y) if P == Q else (yy - y, xx - x))
    slope = numerator * pow(denominator, -1, q) % q
    xxx = (slope * slope - x - xx) % q
    return xxx, (slope * (x - xxx) - y) % q


def times(P, n):
    result = None
    for _ in range(n):
        result = plus(result, P)
    return result


def rank(M):
    M = [[x % 5 for x in row] for row in M]
    i = 0
    for j in range(len(M[0])):
        pivot = next((k for k in range(i, len(M)) if M[k][j]), None)
        if pivot is None:
            continue
        M[i], M[pivot] = M[pivot], M[i]
        scalar = pow(M[i][j], -1, 5)
        M[i] = [x * scalar % 5 for x in M[i]]
        for k in range(i + 1, len(M)):
            scalar = M[k][j]
            M[k] = [(x - scalar * y) % 5 for x, y in zip(M[k], M[i])]
        i += 1
        if i == len(M):
            break
    return i


points = [(evaluation(pack(X), r), evaluation(pack(Y), r)) for r in roots]
assert len(set(points)) == 24
for r, (x, y) in zip(roots, points):
    assert sum(c * pow(r, i, q) for i, c in enumerate(F)) % q == 0
    assert (y * y - x**3 + 4 * x - 16) % q == 0
    assert times((x, y), 5) is None

R = points[0]
line = {times(R, i) for i in range(5)}
S = next(P for P in points if P not in line)
coordinates = {
    plus(times(R, a), times(S, b)): (a, b)
    for a in range(5) for b in range(5)
}
assert len(coordinates) == 25 and None in coordinates
point_index = {P: i for i, P in enumerate(points)}
scalar_indices = [[point_index[times(P, pow(2, j, 5))] for j in range(4)] for P in points]
assert all(points[roots.index(evaluation(pack(sigma), r))] == times(P, 2) for r, P in zip(roots, points))

# Multiply actual field-element residues first. This does not reuse the
# producer's factor-by-factor discrete-log extraction.
values = []
for r in roots:
    row = []
    for factors in units:
        value = 1
        for factor, exponent in factors:
            f = evaluation(pack(factor), r)
            assert f
            value = value * pow(f, exponent % (q - 1), q) % q
        row.append(value)
    values.append(row)

projected = []
for orbit in scalar_indices:
    row = []
    for column in range(13):
        z = 1
        for index, power in zip(orbit, [4, 2, 1, 3]):
            z = z * pow(values[index][column], power, q) % q
        row.append(z)
    projected.append(row)

mu = next(pow(a, (q - 1) // 5, q) for a in range(2, q) if pow(a, (q - 1) // 5, q) != 1)
mu = mu * mu % q  # choose another generator from the producer's first choice
logs = {pow(mu, i, q): i for i in range(5)}
rows = [[logs[pow(value, (q - 1) // 5, q)] for value in row] for row in projected]
cosets = []
norm_rows = []
for c in range(5):
    for d in range(5):
        if c == d == 0:
            continue
        coset = [i for i, P in enumerate(points) if (c * coordinates[P][0] + d * coordinates[P][1]) % 5 == 1]
        assert len(coset) == 5
        cosets.append(coset)
        values_in_target = []
        for column in range(13):
            z = 1
            for index in coset:
                z = z * projected[index][column] % q
            values_in_target.append(logs[pow(z, (q - 1) // 5, q)])
        norm_rows.append(values_in_target)

assert len({tuple(sorted(C)) for C in cosets}) == 24
assert rank(rows) == 3 and rank(norm_rows) == 1
result = {
    "status": "INDEPENDENT_DIRECT_MULTIPLICATIVE_REPLAY_PASS",
    "split_prime": q,
    "unit_residue_rank": rank(rows),
    "affine_norm_residue_rank": rank(norm_rows),
    "unit_kernel_upper_under_retained_character_dimension": 2,
    "complete_class_group_certified_here": False,
    "source_rows": rows,
    "target_rows": norm_rows,
    "input_hashes": {
        name: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
        for name in ["eval_data.json", "split_primes.json"]
    },
}
(ROOT / "RESIDUE_REPLAY.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if not k.endswith("_rows")}, indent=2))
