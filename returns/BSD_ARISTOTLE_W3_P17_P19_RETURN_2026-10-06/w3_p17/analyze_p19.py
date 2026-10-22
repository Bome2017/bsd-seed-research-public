#!/usr/bin/env python3
"""Seed p = 19 (good ordinary, a_19 = 4): plus symbols at 19 and 361 from msl_sq, checks,
and ell_i mod 19 of the weight-two MTT p-adic L-function.  Output: P19_RESULTS.json"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'w3_source'))
from analyze_p17 import load, symbols, rounded, OMEGA_PLUS, N  # noqa: E402
from weight2_jet import low_coefficients_mod_p, unit_root  # noqa: E402

P, AP = 19, 4
S, T = load(os.path.join(HERE, 'runs', 'seed_m361_m19_tf2p5.out'))
sp, dp = rounded(symbols(S[P], P))
sq, dq = rounded(symbols(S[P * P], P * P))
zero = 0
res = {"p": P, "a_p": AP, "T": T, "max_distance_to_integer": {"m=19": dp, "m=361": dq}}
checks = {"level_p_sum_rule": sum(sp.values()) == (AP - 2) * zero,
          "Up_distribution_all_classes": all(
              sum(sq[(a + P * j) % (P * P)] for j in range(P)) == AP * sp[a] - zero for a in range(1, P)),
          "all_symbols_integral_within_1e-4": dp < 1e-4 and dq < 1e-4}
res["checks"] = checks
oracle = lambda a, m: zero if m == 1 else (sp[a % P] if m == P else sq[a % (P * P)])
ell = low_coefficients_mod_p(oracle, AP, P, imax=P - 1, level=2)
nz = [i for i, x in enumerate(ell) if x]
res.update({"alpha_mod_p": unit_root(AP, P, 1), "ell_mod_p": ell,
            "lambda_mu_from_level_p2": {"mu": 0, "lambda": nz[0]} if nz else "lambda >= p or mu > 0",
            "ell2_nonzero_mod_p": ell[2] != 0, "symbols_p": sp, "symbols_p2": sq,
            "gcd_of_all_symbols": math.gcd(*sp.values(), *sq.values())})
print(json.dumps({k: v for k, v in res.items() if not k.startswith('symbols_')}, indent=1))
json.dump(res, open(os.path.join(HERE, 'P19_RESULTS.json'), 'w'), indent=1)
