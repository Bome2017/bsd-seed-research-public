#!/usr/bin/env python3
"""Seed p = 17: plus modular symbols at denominators 17 and 289 (and the 103 calibration),
consistency checks, and the low cyclotomic coefficients ell_i mod 17 of the weight-two
Mazur-Tate-Teitelbaum p-adic L-function (formula of w3_source/weight2_jet.py).

Inputs: the bucket-sum files written by msl_sq (runs/*.out).
Output: P17_RESULTS.json
"""
import json, math, os, re, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'w3_source'))
from weight2_jet import low_coefficients_mod_p, unit_root  # noqa: E402

N = 6503188012738584
OMEGA_PLUS = 0.0280449015194364044483094018079   # retained msl receipt (P17_MSL.txt)
A17 = -6                                          # a_17 of the seed (point count)


def load(path):
    S, T = {}, {}
    for line in open(path):
        w = line.split()
        if not w:
            continue
        if w[0] == 'MOD':
            T[int(w[1])] = int(w[3])
        if w[0] == 'S':
            S.setdefault(int(w[1]), {})[int(w[2])] = float(w[3])
    return S, T


def symbols(Sm, m):
    out = {}
    for a in range(m):
        if math.gcd(a, m) != 1:
            continue
        ap = pow(N * a, -1, m)
        v = sum(Sm[b] * (math.cos(2 * math.pi * a * b / m) + math.cos(2 * math.pi * ap * b / m))
                for b in range(m)) / OMEGA_PLUS
        out[a] = v
    return out


def rounded(vals):
    ints = {a: round(v) for a, v in vals.items()}
    dev = max(abs(v - ints[a]) for a, v in vals.items())
    return ints, dev


def main():
    res = {"curve": "[0,-22735,0,106272484,0]", "N": N, "p": 17, "a_p": A17,
           "Omega_plus": OMEGA_PLUS}
    S17, T17 = load(os.path.join(HERE, 'runs', 'seed_m17_tf3.out'))
    big = os.path.join(HERE, 'runs', 'seed_m289_m103_tf2p5.out')
    Sbig, Tbig = load(big)
    s17, d17 = rounded(symbols(S17[17], 17))
    s289, d289 = rounded(symbols(Sbig[289], 289))
    res["T"] = {"17": T17[17], "289": Tbig[289], "103": Tbig.get(103)}
    res["max_distance_to_integer"] = {"m=17": d17, "m=289": d289}

    # [0]^+ = L(E,1)/Omega^+ : from the m=1 run if present, else 0 (rank >= 2)
    zero = 0
    p1 = os.path.join(HERE, 'runs', 'seed_m1_tf3.out')
    if os.path.exists(p1):
        S1, _ = load(p1)
        z = 2 * S1[1][0] / OMEGA_PLUS
        res["symbol_0_numeric"] = z
        zero = round(z)
    res["symbol_0"] = zero

    checks = {}
    # (a) calibration against the retained authenticated receipt at l = 103
    if 103 in Sbig:
        s103, d103 = rounded(symbols(Sbig[103], 103))
        receipt = {}
        for line in open(os.path.join(HERE, '..', 'retained', 'P17_MSL.txt')):
            m = re.match(r'XB (\d+) plus \[([-0-9.]+)', line)
            if m:
                receipt[int(m.group(1))] = round(float(m.group(2)))
        checks["receipt_103_all_102_symbols_equal"] = all(s103[a] == receipt[a] for a in receipt) and len(receipt) == 102
        checks["receipt_103_max_distance_to_integer"] = d103
    # (b) T_17 at the cusp 0:  sum_{a=1}^{16} [a/17]^+ = (a_17 - 2) [0]^+
    checks["level17_sum_rule"] = sum(s17.values()) == (A17 - 2) * zero
    # (c) U_17 distribution: sum_j [(a+17j)/289]^+ = a_17 [a/17]^+ - [0]^+
    dist = {}
    for a in range(1, 17):
        lhs = sum(s289[(a + 17 * j) % 289] for j in range(17))
        dist[a] = (lhs, A17 * s17[a] - zero)
    checks["U17_distribution_all_16_classes"] = all(l == r for l, r in dist.values())
    # (d) plus-part symmetry is automatic in the formula; record integrality instead
    checks["all_symbols_integral_within_1e-4"] = d17 < 1e-4 and d289 < 1e-4
    res["checks"] = checks

    def oracle(a, m):
        if m == 1:
            return zero
        if m == 17:
            return s17[a % 17]
        if m == 289:
            return s289[a % 289]
        raise ValueError(m)

    ell = low_coefficients_mod_p(oracle, A17, 17, imax=16, level=2)
    nz = [i for i, x in enumerate(ell) if x]
    res["lambda_mu_from_level_289"] = ({"mu": 0, "lambda": nz[0]} if nz else "lambda >= 17 or mu > 0")
    res["ell2_nonzero_mod_17"] = ell[2] != 0
    res["alpha_mod_17"] = unit_root(A17, 17, 1)
    res["ell_mod_17"] = ell
    res["symbols_17"] = s17
    res["symbols_289"] = s289
    res["gcd_of_all_symbols"] = math.gcd(*list(s17.values()), *list(s289.values()))
    print(json.dumps({k: v for k, v in res.items() if not k.startswith('symbols_')}, indent=1))
    json.dump(res, open(os.path.join(HERE, 'P17_RESULTS.json'), 'w'), indent=1)


if __name__ == "__main__":
    main()
