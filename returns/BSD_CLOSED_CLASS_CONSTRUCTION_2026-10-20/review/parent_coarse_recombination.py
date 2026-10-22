#!/usr/bin/env python3
"""Coarse rational recombination of the producer's certified enclosures."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

r = Path(__file__).resolve().parent.parent
a = json.loads((r / "theory/EXACT_BOUND.json").read_text())
b = json.loads((r / "theory/FIELD_INPUTS.json").read_text())

def f(o):
    return F(int(o["numerator"]), int(o["denominator"]))

assert f(a["lambda_lower"]) > F(171, 20)
assert f(a["e_upper"]) < F(68, 25)
assert f(a["pi_interval"][0]) > F(31415, 10000)
assert f(a["log_Q_interval"][1]) < 273
q = int(b["D_A"]) // int(b["D_Aplus"])
assert q * int(b["D_Aplus"]) == int(b["D_A"])
s = isqrt(q) + 1
reg = F(31415, 10000)**3 * F(171, 20)**6 / 768
lu = 2 * (F(68, 25) * 273 / 24)**12
upper = F(s) * lu / ((2 * F(31415, 10000))**6 * reg)
bound = -(-upper.numerator // upper.denominator)
assert bound < 5**98
print(json.dumps({
    "scope": "independent coarse rational recombination, retaining certified transcendental enclosures; not fresh field construction",
    "sqrtQ_ceiling": str(s),
    "coarse_regulator_lower": str(reg),
    "coarse_L_upper": str(lu),
    "coarse_class_order_bound": str(bound),
    "less_than_5_power_98": True,
    "primary_length_upper": 97,
}, indent=2))
