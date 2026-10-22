#!/usr/bin/env python3
"""Exact algebra controls. No seed Kato or Selmer values are computed."""
import json
import math
import random
from fractions import Fraction

PAIRS = [(a, d-a) for d in range(4) for a in range(d+1)]
PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def determinant(mat):
    mat = [[Fraction(x) for x in row] for row in mat]
    det = Fraction(1)
    for i in range(len(mat)):
        pivot = next(j for j in range(i, len(mat)) if mat[j][i])
        if pivot != i:
            mat[i], mat[pivot] = mat[pivot], mat[i]
            det = -det
        v = mat[i][i]
        det *= v
        for j in range(i+1, len(mat)):
            q = mat[j][i]/v
            for k in range(i, len(mat)):
                mat[j][k] -= q*mat[i][k]
    assert det.denominator == 1
    return int(det)

def inverse_mod(mat, modulus):
    n = len(mat)
    m = [[x % modulus for x in row] + [int(i == j) for j in range(n)] for i, row in enumerate(mat)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if math.gcd(m[j][i], modulus) == 1)
        m[i], m[pivot] = m[pivot], m[i]
        u = pow(m[i][i], -1, modulus)
        m[i] = [u*x % modulus for x in m[i]]
        for j in range(n):
            if j != i:
                v = m[j][i]
                m[j] = [(x-v*y) % modulus for x, y in zip(m[j], m[i])]
    assert [row[:n] for row in m] == [[int(i == j) for j in range(n)] for i in range(n)]
    return [row[n:] for row in m]

def apply(mat, v, modulus):
    return [sum(a*b for a, b in zip(row, v)) % modulus for row in mat]

def valuation(x, p, cap=4):
    for i in range(cap):
        if x % p:
            return i
        x //= p
    return cap

def point_matrix(p):
    nodes = [(((1+p)**(10+i)-1)//p, ((1+p)**(7+j)-1)//p) for i, j in PAIRS]
    return [[pow(x, a, p**4)*pow(y, b, p**4) % (p**4) for a, b in PAIRS] for x, y in nodes]

def poly_mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def main():
    nodes = []
    for i, j in PAIRS:
        w, s = 10+i, 7+j
        k, r = w+2, w+1-s
        assert 1 <= r and 2*r < k
        assert 0 <= s <= w
        assert 1 <= s+1 <= k-1
        nodes.append(dict(i=i,j=j,w=w,s=s,weight=k,kato_twist=r))
    grid = [[(10+i)**a*(7+j)**b for a,b in PAIRS] for i,j in PAIRS]
    det = determinant(grid)
    assert det == math.prod(math.factorial(a)*math.factorial(b) for a,b in PAIRS) == 576
    rng = random.Random(20261004)
    trials = 0
    controls = []
    for p in PRIMES:
        modulus = p**4
        v = point_matrix(p)
        assert determinant(v) % p == 576 % p
        vinv = inverse_mod(v, modulus)
        for _ in range(100):
            coeff = [rng.randrange(p**(4-a-b)) for a,b in PAIRS]
            weighted = [x*p**(a+b) for x,(a,b) in zip(coeff,PAIRS)]
            values = apply(v, weighted, modulus)
            assert apply(vinv, values, modulus) == weighted
            assert min(valuation(x,p) for x in values) == min(valuation(x,p) for x in weighted)
            trials += 1
        # Two permitted formal jets missed by the original diagonal.
        for name, raw in [
            ("quadratic_diagonal_zero", {(2,0):1,(1,1):-2,(0,2):1}),
            ("cubic_diagonal_zero", {(1,0):p*p,(0,1):-p*p}),
        ]:
            c = [(raw.get(pair,0)*p**sum(pair)) % modulus for pair in PAIRS]
            e = apply(v,c,modulus)
            assert sum(c) % modulus == 0
            assert any(e)
            assert min(valuation(x,p) for x in e) in (2,3)
        # All terms of J lie in m^4; no comaximality assumption is used.
        polynomial = [1]
        for u in range(4):
            polynomial = poly_mul(polynomial, [-((1+p)**(10+u)-1),1])
        assert all(valuation(c,p,4)+d >= 4 for d,c in enumerate(polynomial))
        assert all(valuation(math.comb(p**3,d),p,4)+d >= 4 for d in (1,2,3))
        assert all(pow((1+p)**(10+i)-1,4,modulus) == 0 for i,j in PAIRS)
        controls.append(dict(p=p,det_mod_p=576%p,nonzero_jet_detection=True,source_product_in_m4=True))
    return {
        "grade":"EXACT_FORMAL_CONTROLS_NOT_SEED_KATO_VALUES",
        "integer_grid_determinant":det,
        "nodes":nodes,
        "prime_controls":controls,
        "random_jet_reconstructions":trials,
        "actual_seed_jet_evaluated":False,
        "uniform_nonvanishing_proved":False,
        "passed":True,
    }

if __name__ == "__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
