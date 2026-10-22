"""Exact normalization controls, not evaluations of a seed Kato class."""
from fractions import Fraction as Q
from itertools import product
from math import prod
import json

def primes(bound):
    return [p for p in range(5, bound+1)
            if all(p%d for d in range(2, int(p**0.5)+1))]

def red(a, p):
    a = Q(a)
    return a.numerator * pow(a.denominator, -1, p) % p

cN = prod(Q(n, q) for q, n in
          [(2, 2), (3, 4), (2243, 2242), (4547, 4547), (5843, 5844)])
assert cN == Q(17469664, 13105849)
assert cN == Q(2**5*19*59*487, 2243*5843)
N = 2**3*3*2243*4547**2*5843
assert N == 6503188012738584

# The bad nonsingular counts and period/regulator conventions above are imports.
# Here we verify their algebraic consequence, not those arithmetic inputs.
eligible = [p for p in primes(97) if cN.numerator % p and cN.denominator % p]
cases = negative = 0
for p in eligible:
    for alpha in [Q(36), Q(37, 2), Q(5, 7), Q(-11, 13)]:
        if alpha.denominator % p == 0 or alpha.numerator % p == 0:
            continue
        for a in range(p):
            if a == 2:
                continue
            for R in [1, 2, p-1]:
                e = (2-a) % p  # ell = 1 mod p
                C2 = 8*red(alpha, p)*(a-2)*R % p
                lhs = red(cN/2, p)*C2 % p
                rhs = -red(alpha*cN, p)*e*4*R % p
                assert lhs == rhs and lhs != 0
                assert (-lhs) % p != rhs       # wrong conductor sign
                assert (2*lhs) % p != rhs      # lost period factor
                assert (lhs*pow(4, -1, p)) % p != rhs  # lost regulator factor
                cases += 1
                negative += 3

# Exact good-prime count at 5 supports only the exceptional Hasse check.
affine = [(x,y) for x in range(5) for y in range(5)
          if (y*y - (x**3-x*x-66020924*x-65074271436)) % 5 == 0]
assert len(affine)+1 == 8

# Formal DVR length controls for the new proof; no Galois modules computed.
dvr_cases = 0
for count in range(1,5):
    for exponents in product(range(1,5), repeat=count):
        assert sum(exponents) >= count
        if sum(exponents) == 1:
            assert count == 1 and exponents == (1,)
        dvr_cases += 1

# U-divisibility alone cannot force primitive/nonzero divided augmentation.
divided = {'U': 1, 'pU_at_p_7': 7, 'U_squared': 0}
assert divided['U'] % 7 != 0
assert divided['pU_at_p_7'] != 0 and divided['pU_at_p_7'] % 7 == 0
assert divided['U_squared'] == 0

print(json.dumps({
    'status': 'EXACT_FORMULA_CONTROLS_PASS',
    'N': N, 'c_N': str(cN), 'conditional_scalar_cases': cases,
    'wrong_sign_or_factor_rejections': negative, 'dvr_length_cases': dvr_cases,
    'E_F5': len(affine)+1, 'divided_augmentation_controls': divided,
    'not_checked': ['Kato class value', 'Sha vanishing', 'source theorem proofs',
                    'independent review of weak-order deduction']
}, indent=2))
