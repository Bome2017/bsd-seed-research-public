#!/usr/bin/env python3
"""Finite exact checks used by A.4; does not prove the geometric 2-adic lemma.

The imported historical script is preserved. This independent implementation
tests each denominator separately and exits nonzero on failure. --inject-failure
is a negative control for the release verifier.
"""
import argparse
import math
from fractions import Fraction


def valuation(n, p):
    if not n:
        raise ValueError('zero has no finite valuation')
    n = abs(n)
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def invariants(a, b):
    # y^2 = x^3 + a*x^2 + b*x: independently simplified integral formulas.
    c4 = 16 * (a*a - 3*b)
    c6 = -64*a*a*a + 288*a*b
    delta = 16*b*b*(a*a - 4*b)
    if c4**3 - c6**2 != 1728*delta:
        raise ArithmeticError('invariant identity')
    return c4, c6, delta


def main(inject_failure=False):
    p = 4547
    if any(p % q == 0 for q in range(2, math.isqrt(p)+1)):
        raise ArithmeticError('4547 must be prime')
    a, b = -22735, 106272484
    for name, u, v in [('seed', a, b), ('2-isogenous partner', -2*a, a*a-4*b)]:
        c4, c6, delta = invariants(u, v)
        vals = tuple(valuation(n, p) for n in (c4, c6, delta))
        if vals != (1, 2, 3):
            raise ArithmeticError(name + ': incorrect valuations')
        j = Fraction(c4**3, delta)
        residue = j.numerator * pow(j.denominator, -1, p) % p
        if residue != 1728 % p:
            raise ArithmeticError(name + ': j residue')
        print(f'PASS {name}: valuations(c4,c6,Delta)={vals}; j=1728 mod 4547')

    # Check a good curve with this j directly; a_4547=0 for an additive model
    # alone would not prove potentially supersingular reduction.
    def chi(n):
        u = pow(n % p, (p-1)//2, p)
        return 0 if u == 0 else (1 if u == 1 else -1)
    count = p + 1 + sum(chi(x*x*x-x) for x in range(p))
    if count != p+1 or p % 4 != 3:
        raise ArithmeticError('j=1728 good-reduction check')
    print('PASS y^2=x^3-x over F_4547 has 4548 points; trace zero')

    N = 2**3 * 3 * 2243 * 4547**2 * 5843
    retained = [3, 9, 27, 81, 5, 25, 7, 49, 11, 121, 13, 169]
    proposed = [2243, 2243**2, 5843, 5843**2]
    for label, ds in [('retained', retained), ('uncomputed bad-prime route', proposed)]:
        for d in ds:
            g = math.gcd(d, N)
            if math.gcd(g, N//g) != 1:
                raise ArithmeticError(f'nonunitary denominator {d}')
            print(f'PASS {label}: d={d}, gcd(d,N)={g}, exact divisor')
    g = math.gcd(4547, N)
    if math.gcd(g, N//g) == 1:
        raise ArithmeticError('negative cusp control was incorrectly admitted')
    print('PASS excluded denominator 4547 is correctly nonunitary')
    if inject_failure:
        raise ArithmeticError('intentional negative control')
    print('ALL PASS')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inject-failure', action='store_true')
    args = parser.parse_args()
    try:
        main(args.inject_failure)
    except (ArithmeticError, ValueError) as exc:
        parser.exit(1, 'CHECK_FAILED: ' + str(exc) + '\n')
