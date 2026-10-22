#!/usr/bin/env python3
"""Low Taylor coefficients, modulo p, of the weight-two cyclotomic p-adic L-function.

Given an integral (primitive) plus modular-symbol oracle r -> [r]^+ for an
ordinary weight-two eigenform, with a_p a p-unit and alpha the unit root of
X^2 - a_p X + p, the Mazur-Tate-Teitelbaum measure is

    mu(a + p^n Z_p) = alpha^(-n) [a/p^n]^+ - alpha^(-(n+1)) [a/p^(n-1)]^+ .

In the source variable S, with nu_S(x) = (1+S)^(log<x>/log(1+p)),

    L_p(S) = int_{Z_p^*} nu_S dmu = sum_i ell_i S^i.

For 0 <= i < p, binom(u, i) mod p depends only on u mod p, and
u(x) = log<x>/log(1+p) mod p depends only on x mod p^2.  Hence

    ell_i mod p = sum_{a in (Z/p^2)^*} mu(a + p^2 Z_p) binom(u(a), i)  mod p,

an exact finite formula using the 2 levels of symbols [a/p^2]^+, [a/p]^+.
(The same identity at level n>=2 is checked as a distribution control.)

This is a weight-two formula.  It needs no Hida lifting.  It is NOT a seed
value: the seed symbol oracle at conductor 6503188012738584 is not available.
"""
from __future__ import annotations
from math import comb
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modsym2 import ModSym2, ap_count  # noqa: E402


def principal_log_mod_p(a: int, p: int) -> int:
    """u = log(a/omega(a))/log(1+p) modulo p, exactly (needs a mod p^2)."""
    if a % p == 0:
        raise ValueError("unit required")
    m = p * p
    v = pow(a, p - 1, m)            # = <a>^(p-1) mod p^2, a principal unit
    # log(1+p k) / log(1+p) = k mod p ; so log_gamma(v) = (v-1)/p mod p
    k = ((v - 1) // p) % p
    return k * pow(p - 1, -1, p) % p


def unit_root(ap: int, p: int, prec: int) -> int:
    mod = p ** prec
    roots = [x for x in range(p) if (x * x - ap * x + p) % p == 0 and x % p]
    if len(roots) != 1:
        raise ValueError("not ordinary")
    x = roots[0]
    for _ in range(prec + 1):  # Newton lift
        f = (x * x - ap * x + p) % mod
        df = (2 * x - ap) % mod
        x = (x - f * pow(df, -1, mod)) % mod
    assert (x * x - ap * x + p) % mod == 0
    return x


def measure_level(symbol, ap: int, p: int, n: int, prec: int):
    mod = p ** prec
    al = unit_root(ap, p, prec)
    ai = pow(al, -1, mod)
    mu = {}
    pn, pn1 = p ** n, p ** (n - 1)
    for a in range(pn):
        if a % p == 0:
            continue
        mu[a] = (pow(ai, n, mod) * symbol(a, pn) - pow(ai, n + 1, mod) * symbol(a % pn1, pn1)) % mod
    return mu


def low_coefficients_mod_p(symbol, ap: int, p: int, imax: int = 3, level: int = 2):
    if level < 2:
        raise ValueError("level >= 2 is required for exactness of S^i, i>=1")
    mu = measure_level(symbol, ap, p, level, 1)
    out = []
    for i in range(imax + 1):
        s = 0
        for a, m in mu.items():
            s += m * comb(principal_log_mod_p(a, p), i)
        out.append(s % p)
    return out


def validate_oracle(M, phi, aq):
    """Reject anything that is not a global plus eigen-symbol for the given a_q."""
    reasons = []
    if not M.check_relations(phi):
        reasons.append("violates Manin relations (not a global modular symbol)")
    elif not M.is_eigen(phi, aq):
        reasons.append("global symbol but not in the specified Hecke eigenspace")
    if phi != M.star(phi):
        reasons.append("not in the plus part")
    return reasons


def plus_eigensymbol(N: int, coeffs, qs=(2, 3, 5, 7, 11, 13)):
    M = ModSym2(N)
    aq = {q: ap_count(coeffs, q) for q in qs if N % q}
    plus = None
    for phi in M.eigen_functionals(aq):
        cand = [x + y for x, y in zip(phi, M.star(phi))]
        if any(cand):
            plus = M.primitive(cand)
            break
    if plus is None or validate_oracle(M, plus, aq):
        raise ArithmeticError("no validated plus eigensymbol")
    return M, aq, plus


def validator_controls(N: int, coeffs):
    """Deliberately non-global / wrong-branch assignments must be rejected."""
    import random
    M, aq, plus = plus_eigensymbol(N, coeffs)
    rng = random.Random(20261006)
    out = {}
    # (i) a single local perturbation of one Manin-symbol value
    bad = list(plus)
    bad[rng.randrange(1, len(bad))] += 1
    out["perturbed_one_value"] = validate_oracle(M, bad, aq)
    # (ii) a random assignment, symmetrised to look like a plus symbol
    rnd = [rng.randrange(-5, 6) for _ in plus]
    rnd = [x + y for x, y in zip(rnd, M.star(rnd))]
    out["random_plus_assignment"] = validate_oracle(M, rnd, aq)
    # (iii) a genuine global symbol on a different eigensystem (Eisenstein: a_q = q+1)
    eis = M.eigen_functionals({q: q + 1 for q in aq})
    e = None
    for phi in eis:
        cand = [x + y for x, y in zip(phi, M.star(phi))]
        if any(cand):
            e = M.primitive(cand)
            break
    out["eisenstein_global_symbol"] = validate_oracle(M, e, aq) if e else ["none found"]
    out["all_rejected"] = all(bool(v) for v in out.values())
    return out


def calibration(N: int, coeffs, primes):
    M, aq, plus = plus_eigensymbol(N, coeffs)
    sym = lambda a, m: M.symbol_inf_to(plus, a, m)
    rows = []
    for p in primes:
        if N % p == 0:
            continue
        ap = ap_count(coeffs, p)
        if ap % p == 0:
            rows.append({"p": p, "ap": ap, "status": "supersingular_skipped"})
            continue
        # U_p distribution control at the first two levels (exact integers):
        # sum_j [ (a+j p^n)/p^(n+1) ] = a_p [a/p^n] - [a/p^(n-1)]
        for n in (1, 2):
            for a in range(p ** n):
                lhs = sum(sym(a + j * p ** n, p ** (n + 1)) for j in range(p))
                rhs = ap * sym(a, p ** n) - sym(a % p ** (n - 1), p ** (n - 1))
                assert lhs == rhs, ("Hecke U_p identity failed", p, n, a)
        c2 = low_coefficients_mod_p(sym, ap, p, 3, 2)
        c3 = low_coefficients_mod_p(sym, ap, p, 3, 3) if p < 40 else None
        rows.append({"p": p, "ap": ap, "ell_mod_p_level2": c2, "ell_mod_p_level3": c3})
    return rows


if __name__ == "__main__":
    import json
    out = {
        "scope": "CALIBRATION_ON_SMALL_CONDUCTORS_ONLY; no seed value",
        "11a1_rank0": calibration(11, (0, -1, 1, -10, -20), [17, 19, 23, 29, 31]),
        "37a1_rank1": calibration(37, (0, 0, 1, -1, 0), [17, 19, 23, 29, 31]),
        "389a1_rank2": calibration(389, (0, 1, 1, -2, 0), [17, 19, 23, 29, 31, 37, 41, 43]),
        "validator_controls_389a1": validator_controls(389, (0, 1, 1, -2, 0)),
    }
    r2 = out["389a1_rank2"]
    out["checks"] = {
        "rank2_ell0_ell1_zero_mod_p": all(r["ell_mod_p_level2"][:2] == [0, 0] for r in r2 if "ell_mod_p_level2" in r),
        "rank1_ell0_zero_ell1_nonzero": all(r["ell_mod_p_level2"][0] == 0 and r["ell_mod_p_level2"][1] != 0
                                            for r in out["37a1_rank1"] if "ell_mod_p_level2" in r),
        "level2_equals_level3": all(r["ell_mod_p_level3"] in (None, r["ell_mod_p_level2"])
                                    for k in ("11a1_rank0", "37a1_rank1", "389a1_rank2") for r in out[k]
                                    if "ell_mod_p_level2" in r),
        "nonglobal_assignments_rejected": out["validator_controls_389a1"]["all_rejected"],
    }
    print(json.dumps(out, indent=1))
