#!/usr/bin/env python3
"""Seed source pilot at p=31: arithmetic bindings, exact required support, first failure.

Everything printed here is either exact arithmetic (also machine-checked in
RequestProject/SeedPilot31.lean where marked LEAN) or explicitly labelled ESTIMATE.
No seed modular-symbol VALUE is computed: the oracle for the seed eigen-symbol
at conductor N is not available in this environment (see FIRST_FAILURE).
"""
from __future__ import annotations
import hashlib
import json
from math import gcd

N = 6503188012738584
NFAC = {2: 3, 3: 1, 2243: 1, 4547: 2, 5843: 1}
AINV = (0, -1, 0, -66020924, -65074271436)      # minimal model
OLD = (0, -22735, 0, 106272484, 0)              # retained model, x_old = x_min + 7578
P = 31


def ap(p, a=AINV):
    a1, a2, a3, a4, a6 = a
    cnt = 1
    for x in range(p):
        r = (x ** 3 + a2 * x * x + a4 * x + a6) % p
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y - r) % p == 0:
                cnt += 1
    return p + 1 - cnt


def disc(a):
    a1, a2, a3, a4, a6 = a
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    return -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


class P1CRT:
    """Canonical representatives of P^1(Z/M) via CRT over prime powers."""

    def __init__(self, fac):
        self.fac = fac
        self.M = 1
        for l, e in fac.items():
            self.M *= l ** e

    def norm(self, c, d):
        key = []
        for l, e in sorted(self.fac.items()):
            m = l ** e
            cc, dd = c % m, d % m
            if dd % l:
                key.append((cc * pow(dd, -1, m) % m, 1))
            elif cc % l:
                key.append((1, dd * pow(cc, -1, m) % m))
            else:
                raise ValueError("not in P^1")
        return tuple(key)

    def size(self):
        s = 1
        for l, e in self.fac.items():
            s *= l ** e + l ** (e - 1)
        return s


def manin_support(P1, a, m):
    """Manin symbols in the continued-fraction expansion of {infinity, a/m}."""
    pk2, qk2, pk1, qk1 = 0, 1, 1, 0
    x, y = a, m
    out = []
    while y:
        t = x // y
        pk, qk = t * pk1 + pk2, t * qk1 + qk2
        if pk * qk1 - pk1 * qk == 1:
            out.append(P1.norm(qk, qk1))
        else:
            out.append(P1.norm(qk, -qk1))
        pk2, qk2, pk1, qk1 = pk1, qk1, pk, qk
        x, y = y, x - t * y
    return out


def main():
    p = P
    mod4 = p ** 4
    a31 = ap(p)
    roots = [x for x in range(mod4) if (x * x - a31 * x + p) % mod4 == 0]
    unit_roots = [x for x in roots if x % p]
    D = disc(AINV)
    out = {"bindings": {
        "N": N, "N_factorisation": NFAC,
        "N_check": N == 2 ** 3 * 3 * 2243 * 4547 ** 2 * 5843,              # LEAN
        "discriminant_min_model": D, "disc_old_model_equal": disc(OLD) == D,  # LEAN (variable change)
        "p": p, "p_good": D % p != 0 and N % p != 0,                         # LEAN
        "a_p": a31, "#E(F_p)": p + 1 - a31,                                  # LEAN
        "ordinary": a31 % p != 0,                                            # LEAN
        "a_p_not_pm1_mod_p": a31 % p not in (1, p - 1),                      # LEAN
        "roots_mod_p4_of_X2-apX+p": roots, "unit_root_alpha0": unit_roots,   # LEAN (exhaustive)
        "a_q_q_lt_100": {q: ap(q) for q in primes_upto(100) if N % q},
    }}
    # Tame characters at weights five and six on the weight-two component:
    # weight k = w+2, wild nebentypus omega^(-w).  Parity omega^(-w)(-1) = (-1)^k.
    g = next(x for x in range(2, p) if all(pow(x, (p - 1) // l, p) != 1 for l in (2, 3, 5)))
    def order(e):
        e %= p - 1
        return (p - 1) // gcd(p - 1, e)
    out["tame_characters"] = {
        "generator_mod_31": g,
        "weight5_w3": {"nebentypus": "omega^(-3)", "order": order(-3), "conductor": p,
                        "parity_ok": (-1) ** 3 == (-1) ** 5},
        "weight6_w4": {"nebentypus": "omega^(-4)", "order": order(-4), "conductor": p,
                        "parity_ok": (-1) ** 4 == (-1) ** 6},
        "consequence": "g_3, g_4 are p-new of level 31N with ramified wild character; they are "
                       "not p-stabilisations of level-N forms, and their symbols are not determined "
                       "by the seed's weight-two symbols without Hida lifting.",
    }
    # Sizes of the two candidate presentations.
    lvlNp = dict(NFAC)
    lvlNp[p] = 1
    sizeNp = P1CRT(lvlNp).size()
    sizeN = P1CRT(NFAC).size()
    out["presentation_sizes"] = {
        "|P^1(Z/31N)| (Manin symbols for Gamma_0(31N))": sizeNp,
        "|P^1(Z/N)| (Manin symbols for Gamma_0(N))": sizeN,
        "coefficient slots per symbol (ten-moment quotient)": 10,
        "unknown Z/p-digits in a full order-3 jet over Gamma_0(31N)": 20 * sizeNp,
    }
    # Exact sparse support for the weight-two route (level N, denominators 31, 31^2).
    P1N = P1CRT(NFAC)
    divisors = [(a, p) for a in range(1, p)] + [(a, p * p) for a in range(1, p * p) if a % p]
    supp = {}
    for a, m in divisors:
        for s in manin_support(P1N, a, m):
            supp[s] = supp.get(s, 0) + 1
    # Plus part also needs -a/m; include it.
    supp_plus = dict(supp)
    for a, m in divisors:
        for s in manin_support(P1N, -a, m):
            supp_plus[s] = supp_plus.get(s, 0) + 1
    h = hashlib.sha256(json.dumps(sorted(map(str, supp_plus))).encode()).hexdigest()
    out["weight2_route_support"] = {
        "divisors": "{infinity}-{a/31}, 1<=a<=30, and {infinity}-{a/961}, 31 not dividing a (and their negatives)",
        "number_of_divisors": len(divisors),
        "distinct_level_N_manin_symbols_needed": len(supp_plus),
        "support_sha256": h,
        "what_is_missing": "the values of the seed's primitive plus eigen-functional on these Manin symbols",
    }
    # ESTIMATE (not a theorem): period-integral cost of one level-961 plus symbol.
    sqrtN = int(N ** 0.5)
    out["FIRST_FAILURE"] = {
        "gate": "W2-ORACLE: seed primitive plus modular symbol on the support above",
        "exact_reason": "no seed eigen-symbol oracle exists in the supplied material, and neither "
                        "standard construction can be executed here: (a) Hecke/Manin linear algebra over "
                        f"{sizeN} level-N Manin symbols; (b) period integrals of f along paths to a/961.",
        "ESTIMATE_terms_per_period_integral_at_denominator_961": f"~ 961*sqrt(N)*O(1) = {961 * sqrtN:.3e}",
        "ESTIMATE_note": "requires a_n for n up to ~1e11 and a p-adic/archimedean comparison to the "
                         "primitive integral normalisation; this is a resource statement, not a theorem "
                         "that no cheaper method exists.",
        "seed_values_computed": 0,
    }
    return out


if __name__ == "__main__":
    print(json.dumps(main(), indent=1, default=str))
