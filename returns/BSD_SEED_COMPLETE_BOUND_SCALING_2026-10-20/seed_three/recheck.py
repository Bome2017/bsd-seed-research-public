#!/usr/bin/env python3
"""Exact replay of existing source-coordinate evidence; no new class search."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "inputs/MATRICES.json").read_text())


def rref(matrix):
    a = [[int(x) % 3 for x in row] for row in matrix]
    pivots = []
    for column in range(len(a[0])):
        row = next((r for r in range(len(pivots), len(a)) if a[r][column]), None)
        if row is None:
            continue
        index = len(pivots)
        a[index], a[row] = a[row], a[index]
        inverse = pow(a[index][column], -1, 3)
        a[index] = [x * inverse % 3 for x in a[index]]
        for r in range(len(a)):
            if r != index:
                factor = a[r][column]
                a[r] = [(x - factor * y) % 3 for x, y in zip(a[r], a[index])]
        pivots.append(column)
        if len(pivots) == len(a):
            break
    return a, pivots


def rank(matrix):
    return len(rref(matrix)[1])


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, column)) % 3
             for column in zip(*b)] for row in a]


source = data["unramified_basis_rows"]
actual = data["actual_coordinates"]
reduced, pivots = rref([a + b for a, b in zip(source, actual)])
width = len(source[0])
assert pivots == list(range(width))
assert all(not any(row) for row in reduced[width:])
coordinates = [row[width:] for row in reduced[:width]]
assert multiply(source, coordinates) == actual
images = multiply(data["class_rows_on_unramified_basis"], coordinates)
assert images == [[0, 2, 2, 2], [0, 0, 2, 2]]
assert rank(actual) == 4
assert rank(multiply(data["residue_injectivity_matrix"], actual)) == 4
assert rank(images) == 2
assert not any(x for row in multiply(data["valuation_rows"], actual) for x in row)
assert not any(x for row in multiply(data["local_rows"], actual) for x in row)

receipt = json.loads((ROOT / "inputs/OLD_CERTIFICATION_RECEIPT.json").read_text())
assert receipt["status"] == "TIMEOUT"
assert receipt["internal_seconds"] == 90
assert any("226849291805255087108915200" in text for text in receipt["errors"])
result = {
    "status": "OLD_ARITHMETIC_REPLAYED_NO_NEW_SEED_BOUND",
    "coefficient_prime": 3,
    "existing_independent_source_rank": 4,
    "existing_class_image_matrix": images,
    "existing_class_image_rank": 2,
    "ordinary_unit_kernel_dimension_retained": 2,
    "ordinary_class_kernel_dimension_conditional": 2,
    "connecting_map_rank_conditional": 0,
    "ordinary_complete_kernel_dimension_conditional": 4,
    "S_complete_kernel_dimension_conditional": 4,
    "new_class_certification": False,
    "old_certification_status": receipt["status"],
    "new_number_field_job_launched": False,
    "known_Sha_order_used": False,
    "scope": "Matrix replay only. Exact norm cubes and all-place membership remain retained inputs.",
    "input_sha256": {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted((ROOT / "inputs").iterdir())
    },
}
(ROOT / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
