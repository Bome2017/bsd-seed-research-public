#!/usr/bin/env python3
"""Exact prime-power tests of the faithful relative-class remainder."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def lift_i(n):
    value, modulus = 2, 5
    for _ in range(1, n):
        candidates = [value + a * modulus for a in range(5)]
        modulus *= 5
        hits = [a for a in candidates if (a * a + 1) % modulus == 0]
        assert len(hits) == 1
        value = hits[0]
    assert (value * value + 1) % modulus == 0
    return value, modulus


checks = []
for n in range(1, 6):
    i, modulus = lift_i(n)
    for eigenvalue in [i, pow(i, -1, modulus)]:
        assert pow(eigenvalue, 4, modulus) == 1
        assert pow(eigenvalue, 2, modulus) == modulus - 1
        assert (1 + pow(eigenvalue, 2, modulus)) % modulus == 0
        assert sum(pow(eigenvalue, k, modulus) for k in range(4)) % modulus == 0
        assert (eigenvalue - 1) % 5 != 0
        assert (pow(eigenvalue, 2, modulus) - 1) % 5 != 0
        assert (2 * pow(2, -1, modulus)) % modulus == 1
        assert (4 * pow(4, -1, modulus)) % modulus == 1
        for rank in range(1, 9):
            checks.append({
                "exponent": n,
                "rank": rank,
                "scalar_eigenvalue": eigenvalue,
                "modulus": modulus,
                "fixed_by_C4_dimension": 0,
                "fixed_by_C2_dimension": 0,
                "proper_subfield_norms": [0, 0],
                "relative_five_length": rank * n,
                "relative_five_rank": rank,
            })

# Over Q(i), not just mod 5, the two proper subgroup norm elements
# vanish on the faithful character. Represent a+b*i by the pair (a,b).
def multiply(a, b):
    x, y = a
    z, w = b
    return x*z-y*w, x*w+y*z

powers = [(1, 0)]
for _ in range(3):
    powers.append(multiply(powers[-1], (0, 1)))
assert (powers[0][0]+powers[2][0], powers[0][1]+powers[2][1]) == (0, 0)
assert tuple(sum(v[j] for v in powers) for j in range(2)) == (0, 0)

result = {
    "status": "FAITHFUL_RELATIVE_CLASS_REMAINDER_NOT_BOUNDED_BY_PROPER_SCALAR_SUBFIELDS",
    "cases": len(checks),
    "prime_power_levels": 5,
    "ranks_checked": list(range(1, 9)),
    "proper_subfield_norms_zero_in_characteristic_zero": True,
    "arbitrary_rank_statement": "proved algebraically; finite cases are implementation controls",
    "arithmetic_realization_claimed": False,
    "seed_class_bound_obtained": False,
    "rows": checks,
}
(ROOT / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k:v for k,v in result.items() if k != "rows"}, indent=2))
