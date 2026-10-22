#!/usr/bin/env python3
"""Exact formula controls, not computations of seed Selmer or Kato indices."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]

def val(n, p):
    n = F(n)
    assert n
    def power(x):
        count = 0
        while x % p == 0:
            x //= p
            count += 1
        return count
    return power(abs(n.numerator)) - power(n.denominator)

def teich(b, p, k):
    modulus = p**k
    return pow(b, p**(k-1), modulus)

def mul_group(x, y, p, modulus):
    z = {a: 0 for a in range(1, p)}
    for a, u in x.items():
        for b, v in y.items():
            z[a*b % p] = (z[a*b % p] + u*v) % modulus
    return z

results = {"scope": "Exact algebra/formula controls; no seed index evaluated"}
idempotents = []
gauss = []
frob = []
euler = []
formal = []
basechange = []

for p in PRIMES:
    k = 5
    modulus = p**k
    w = {a: teich(a, p, k) for a in range(1, p)}
    for a in w:
        assert w[a] % p == a and pow(w[a], p-1, modulus) == 1
    norm = pow(p-1, -1, modulus)
    eps = {a: norm*w[a] % modulus for a in w}
    assert sum(eps.values()) % modulus == 0
    assert mul_group(eps, eps, p, modulus) == eps
    for h in range(1, p):
        translated = {h*a % p: eps[a] for a in eps}
        scalar = pow(w[h], -1, modulus)
        assert translated == {a: scalar*eps[a] % modulus for a in eps}
    idempotents.append({"p": p, "precision": k, "idempotent": True,
                        "augmentation_zero": True, "character": "omega^-1"})

    coeff = [sum(a*comb(a, j) for a in range(1, p)) % p for j in range(p)]
    invcoeff = [sum(pow(a, -1, p)*comb(a, j) for a in range(1, p)) % p
                for j in range(p)]
    first = next(j for j, c in enumerate(coeff) if c)
    wrong = next(j for j, c in enumerate(invcoeff) if c)
    assert first == p-2 and wrong == 1
    gauss.append({"p": p, "omega_first_degree": first,
                  "inverse_omega_first_degree": wrong,
                  "valuation": str(F(p-2, p-1))})

    for a in range(2, p):
        assert val(1-F(1, a), p) == 0
        for fz, f0 in [(F(2, 3), F(5, 7)), (F(11, 13), F(0))]:
            F0 = f0/(1-F(p, a))
            Fz = fz + F(p, a)*F0
            direct = F(a, p*p)*Fz
            printed = F(a, p*p)*fz + F(1, p)*f0/(1-F(p, a))
            assert direct == printed
        assert val(F(a, (p-1)*p*p), p) == -2
        frob.append({"p": p, "unramified_unit": a,
                     "cokernel_factor_unit": True, "exponent": -2})
        for n in [0, 1, 2, 3, 4, 7]:
            critical = F(p**n, 1+p)
            xi = (1-F(a, p*p))*critical
            assert p*p*xi == (p*p-a)*critical
            assert val(p*p-a, p) == 0
            assert val(p*p*xi, p) == val(critical, p) == n
            euler.append([p, a, n])

    for m in range(1, 9):
        S = F(p*p, 1+p)
        value = p**m*S + S**(m+1)
        assert val(value, p) == m+2
        for t in [F(2, 3), F(p), F(-2, 5)]:
            invol = -t/(1+t)
            assert invol**2/(1+invol) == t*t/(1+t)
        formal.append({"p": p, "m": m, "valuation_at_p": val(value, p)})

for e in [1, 2, 3, 4, 7]:
    for uval in [0, 1, 2]:
        b = 2*e + uval
        basechange.append({"v_pi_p": e, "v_pi_U": uval, "index": b,
                           "threshold_3": b <= 3})
assert any(x["v_pi_U"] <= 1 and not x["threshold_3"] for x in basechange)

# A formal rational basis change can have arbitrary integral index.
for p in PRIMES:
    for m in [1, 2, 5]:
        x, d = F(7, 11), F(1, p*p)
        basis_scale = p**m
        assert x/d == (x/basis_scale)/(d/basis_scale)
        assert val(d/basis_scale, p) == -2-m

results.update({"tame_idempotents": idempotents, "gauss_orientation": gauss,
                "rank_one_frobenius": frob, "euler_cancellation": euler,
                "formal_family_controls": formal,
                "coefficient_ramification": basechange,
                "status": "PASS",
                "nonclaim": "These controls do not prove the imported cohomological isomorphisms or any b_p bound."})
out = Path(__file__).with_name("EXACT_CONTROLS.json")
out.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "tame_primes": len(idempotents),
                  "rank_one_cases": len(frob), "euler_cases": len(euler),
                  "formal_family_cases": len(formal),
                  "ramification_cases": len(basechange)}, sort_keys=True))
