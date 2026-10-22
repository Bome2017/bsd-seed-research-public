#!/usr/bin/env python3
"""Independent exact replay of the small Shii seed hypothesis arithmetic.

This does not prove the retained conductor/residual-image theorem or Shii's
theorem. It checks the arithmetic used in that theorem's application screen.
"""
import json
from math import gcd, isqrt
from pathlib import Path


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def val(n, ell):
    assert n != 0
    v = 0
    while n % ell == 0:
        n //= ell
        v += 1
    return v


def run():
    expected = json.loads(Path(__file__).with_name("SHII_SEED_ARITHMETIC.json").read_text())
    a1, a2, a3, a4, a6 = expected["model"]
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    assert (c4, delta) == (expected["c4"], expected["delta"])
    assert delta == 2**8 * 3**2 * 2243 * 4547**3 * 5843**2
    assert expected["N_plus"] == 2**3 * 4547**2
    assert expected["N_minus"] == 3 * 2243 * 5843
    assert expected["N"] == expected["N_plus"] * expected["N_minus"]
    assert gcd(7, expected["N"]) == 1
    assert (-7) % 8 == 1
    rows = []
    for r in expected["odd_prime_rows"]:
        ell = r["ell"]
        assert prime(ell)
        power = pow(-7, (ell-1)//2, ell)
        symbol = -1 if power == ell-1 else power
        actual = {"ell":ell, "kronecker_D_K":symbol,
                  "v_delta":val(delta, ell), "c4_mod_ell":c4 % ell}
        assert actual == r
        if ell in (3, 2243, 5843):
            assert symbol == -1 and c4 % ell != 0
            assert 0 < actual["v_delta"] < 5
        rows.append(actual)
    assert len({3,2243,5843}) == 3
    # With pi>3 and 7<9, the imaginary-quadratic Minkowski bound
    # 2*sqrt(7)/pi is <2. Thus its only possible integral ideal norm is 1.
    assert 7 < 3**2
    return {"status":"PASS", "method":"standard-library exact integer arithmetic",
            "rows":rows, "endpoints_changed":False,
            "not_recertified":["conductor theorem", "full residual image",
                               "Shii theorem", "class-field and Tate-curve inputs"]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2) + "\n", end="")
