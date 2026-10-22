"""Extract actual signed quadratic jets if certified theta arrays are supplied.

This code does not construct a quaternionic eigenform or certify input provenance.
Run with a JSON filename containing p, theta1, theta2, and source_metadata.
theta_n[a] is the coefficient of gamma**a, not of T**a.
"""
import json
from math import comb, isqrt
from pathlib import Path
import sys


def extract(p, theta1, theta2):
    if p < 5 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("p must be a prime at least 5")
    if len(theta1) != p or len(theta2) != p * p:
        raise ValueError("need p and p^2 group-basis coefficients")
    if any(type(x) is not int for x in theta1 + theta2):
        raise ValueError("coefficients must be exact integers")
    minus = [-sum(b * comb(a, k) for a, b in enumerate(theta1)) % p
             for k in range(3)]
    plus = [
        -sum(b for a, b in enumerate(theta2) if a % p == p - 1) % p,
        -sum((a // p) * b for a, b in enumerate(theta2)) % p,
        -sum((a % p) * (a // p) * b for a, b in enumerate(theta2)) % p,
    ]
    direct = [-sum(b * comb(a, p - 1 + k) for a, b in enumerate(theta2)) % p
              for k in range(3)]
    assert plus == direct
    return {
        "p": p,
        "coordinate": "T=gamma-1; theta arrays in gamma basis",
        "minus_jet_mod_p": minus,
        "plus_jet_mod_p": plus,
        "seed_augmentation_check": plus[0] == minus[0] == 0,
        "seed_residual_linear_check": plus[1] == minus[1] == 0,
        "scope": "extraction only; no provenance, theta recurrence, or BSD certification",
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 signed_theta_extractor.py INPUT.json")
    data = json.loads(Path(sys.argv[1]).read_text())
    if not data.get("source_metadata"):
        raise SystemExit("source_metadata is required; this extractor does not verify it")
    output = extract(data["p"], data["theta1"], data["theta2"])
    output["source_metadata_unverified"] = data["source_metadata"]
    print(json.dumps(output, indent=2))
