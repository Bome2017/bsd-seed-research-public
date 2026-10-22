#!/usr/bin/env python3
"""Exact downstream test for the retained p7 modular-symbol criterion.

The high precision below concerns P2, not extra digits of the infinite L-function.
Only its residue modulo7 is used to infer the leading coefficient is a unit.
"""
from pathlib import Path
from fractions import Fraction
from math import comb
import hashlib
import json
import struct
import sys

root = Path(__file__).resolve().parent
run = root / "run"
p, k = 7, 20
mod = p**k
checks = []

def check(ok, name):
    checks.append({"name": name, "passed": bool(ok)})
    if not ok:
        raise AssertionError(name)

def read_symbols(m):
    result = ({}, {})
    for line in (run / f"SYMBOLS_m{m}.txt").read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        b, pos, neg = line.split()
        result[0][int(b)], result[1][int(b)] = Fraction(pos), Fraction(neg)
    return result

def residue(value, modulus=mod):
    value = Fraction(value)
    check(value.denominator % p != 0, "symbol denominator prime to7")
    return value.numerator * pow(value.denominator, -1, modulus) % modulus

s49, n49 = read_symbols(49)
s7, n7 = read_symbols(7)
a7 = struct.unpack("<4i", (run / "ap/ap_000000.bin").open("rb").read(16))[3]
point_count = 1 + sum(
    y*y % p == (x**3 - 22735*x*x + 106272484*x) % p
    for x in range(p) for y in range(p)
)
check(point_count == 10 and a7 == p + 1 - point_count == -2,
      "exact point count equals verified a7")
for m, pos, neg in [(49, s49, n49), (7, s7, n7)]:
    check(set(pos) == set(neg) == {b for b in range(1, m) if b % p},
          f"complete plus and minus unit symbol sets at{m}")
    check(all(pos[b] == pos[m-b] and neg[b] == -neg[m-b] for b in pos),
          f"both conjugation symmetries at{m}")
    check(all((1024*x).denominator == 1 for x in [*pos.values(), *neg.values()]),
          f"retained lattice at{m}")
check(sum(s7.values()) == 0, "T7 relation at zero cusp")
check(all(a7*low[c] == sum(high[c+7*j] for j in range(7))
          for high, low in [(s49, s7), (n49, n7)] for c in low),
      "T7 relations for all six cusps and both signs")

# Route A: recover the cyclotomic exponent independently from Fermat quotients.
inv_a2 = pow(a7 % p, -2, p)
qa_weights = {}
for b in s49:
    q = (pow(b, p-1, p*p) - 1) // p
    j = q * pow(p-1, -1, p) % p
    qa_weights[b] = inv_a2 * comb(j, 2) % p
full_exact_a = sum(qa_weights[b] * s49[b] for b in s49)
folded_exact = (5*sum(s49[b] for b in [2,4,11,13,22,23])
                +4*sum(s49[b] for b in [6,9,10,15,16,24])
                +3*sum(s49[b] for b in [12,17,20]))
route_a = residue(full_exact_a, p)
check(residue(folded_exact, p) == route_a,
      "predeclared fifteen-symbol formula equals Fermat-quotient computation")

# Route B: full depth-two measure, with lower-level contribution retained.
alpha = a7 % p
for _ in range(2*k):
    alpha = (alpha - (alpha*alpha-a7*alpha+p)
             * pow(2*alpha-a7, -1, mod)) % mod
check((alpha*alpha-a7*alpha+p) % mod == 0 and alpha % p == a7 % p,
      "Hensel unit root")
omega = {a: pow(a, p**k, mod) for a in range(1,p)}
check(all(pow(w, p-1, mod) == 1 and w % p == a for a,w in omega.items()),
      "Teichmuller representatives")
ia = pow(alpha, -1, mod)
coef = [0,0,0]
seen = []
lower = 0
for a,w in omega.items():
    for j in range(p):
        b = w * pow(1+p,j,p*p) % (p*p)
        seen.append(b)
        check(qa_weights[b] == inv_a2*comb(j,2) % p,
              "Fermat exponent agrees with Teichmuller enumeration")
        correction = ia**3 * residue(s7[b % p]) % mod
        mu = (ia**2*residue(s49[b]) - correction) % mod
        for degree in range(3):
            coef[degree] = (coef[degree]+mu*comb(j,degree)) % mod
        lower = (lower+correction*comb(j,2)) % mod
check(sorted(seen) == sorted(s49), "every unit modulo49 used exactly once")
check(coef[0] == 0, "constant coefficient of P2 zero")
check(coef[1] % p == 0, "linear coefficient of P2 zero modulo7")
check(lower % p == 0 and sum(comb(j,2) for j in range(p)) == 35,
      "lower-level contribution vanishes modulo7")
check(coef[2] % p == route_a, "independent coefficient evaluations agree")

answer = {
    "status": "P7_COEFFICIENT_UNIT_PROVED" if route_a else "P7_UNIT_TEST_INCONCLUSIVE",
    "a7": a7,
    "finite_P2_precision_exponent": k,
    "finite_P2_coefficients_mod_7pow20": coef,
    "infinite_L7_leading_coefficient_certified_digits": 1,
    "residue_omega1": route_a,
    "residue_neron_full_period": route_a*pow(2,-1,p) % p,
    "folded_exact_integer_or_rational": str(folded_exact),
    "lower_contribution_mod_7": lower % p,
    "alpha_mod_49": alpha % 49,
    "all_checks_passed": all(c["passed"] for c in checks),
    "checks": checks,
    "symbol_file_sha256": {
        f"SYMBOLS_m{m}.txt": hashlib.sha256((run/f"SYMBOLS_m{m}.txt").read_bytes()).hexdigest()
        for m in [49,7]
    },
    "plus_symbols_49": {str(b):str(v) for b,v in sorted(s49.items())},
    "plus_symbols_7": {str(b):str(v) for b,v in sorted(s7.items())},
}
(root/"DOWNSTREAM.json").write_text(json.dumps(answer,indent=2)+"\n")
print(json.dumps({key:value for key,value in answer.items()
                  if key not in ["checks","plus_symbols_49","plus_symbols_7"]},indent=2))
