#!/usr/bin/env python3
"""L'(E^(-23), 1) for the quadratic twist of the seed by Q(sqrt(-23)) (conductor 23^2 N,
root number -1), from the E_1-kernel bucket sums mod 23 written by msl_e1:
    L'(E^K, 1) = 2 sum_b chi(b) S_b,  chi(b) = (b/23),  S_b = sum_{n=b (23)} a_n/n E_1(2 pi n/(23 sqrt N)).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    S = {}
    for line in open(os.path.join(HERE, 'runs', name)):
        w = line.split()
        if w and w[0] == 'S':
            S[int(w[2])] = float(w[3])
    return S
S = load('twist23_E1_tf3.out')
chi = lambda b: 0 if b % 23 == 0 else (1 if pow(b, 11, 23) == 1 else -1)
Lp = 2 * sum(chi(b) * S[b] for b in range(23))
out = {"twist": "E^(-23)", "conductor": 23 ** 2 * 6503188012738584, "root_number": -1,
       "L_prime_at_1": Lp,
       "check_chi_matches_kronecker_minus23": [chi(q) for q in (2, 3, 2243, 4547, 5843)]}
# functional-equation test (root number -1): with split parameter t,
#   L'(1) = sum a_n chi(n)/n [E1(2 pi n t/X) + E1(2 pi n/(t X))]   independent of t.
fa, fb = os.path.join(HERE, 'runs', 'twist23_E1_tf3_xs0.833.out'), os.path.join(HERE, 'runs', 'twist23_E1_tf3_xs1.2.out')
if os.path.exists(fa) and os.path.exists(fb):
    Sa, Sb = load('twist23_E1_tf3_xs0.833.out'), load('twist23_E1_tf3_xs1.2.out')
    Lt = sum(chi(b) * (Sa[b] + Sb[b]) for b in range(23))
    out["L_prime_split_t_1.2"] = Lt
    out["functional_equation_discrepancy"] = abs(Lt - Lp)
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(HERE, 'TWIST23_RESULTS.json'), 'w'), indent=1)
