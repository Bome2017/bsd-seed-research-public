#!/usr/bin/env python3
"""Finite algebra controls only. Does not evaluate an elliptic Selmer group."""
from __future__ import annotations
from itertools import product
import json

def matmul(a: list[list[int]], b: list[list[int]], p: int) -> list[list[int]]:
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]

def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]

def rank(a: list[list[int]], p: int) -> int:
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][j] % p, -1, p)
        a[r] = [x*inverse % p for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j]
                a[i] = [(x-c*y) % p for x,y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r

def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)

def main() -> dict:
    cases = 0
    minimal_cases = 0
    for p in (5,7,11):
        # O/(pi^d), d <= p-1: mod p models with sigma=1+J_d.
        for count in (2,3,4):
            for lengths in product((1,2,3), repeat=count):
                n = sum(lengths)
                j = [[0]*n for _ in range(n)]
                offset = 0
                for d in lengths:
                    for i in range(d-1):
                        j[offset+i][offset+i+1] = 1
                    offset += d
                sigma = [[(j[a][b]+int(a == b)) % p for b in range(n)]
                         for a in range(n)]
                norm = [[0]*n for _ in range(n)]
                power = identity(n)
                for _ in range(p):
                    norm = [[(norm[a][b]+power[a][b]) % p for b in range(n)]
                            for a in range(n)]
                    power = matmul(power, sigma, p)
                check(power == identity(n), 'cyclic action')
                check(not any(any(row) for row in norm), 'norm zero')
                invariant_dim = n-rank(j,p)
                check(invariant_dim == count, 'one socle per block')
                check(0 <= invariant_dim-2 <= n-2, 'quotient dimension bound')
                if n <= 2:
                    check(invariant_dim == 2, 'length threshold')
                    minimal_cases += 1
                cases += 1
    coefficient_controls = []
    for degree in (5,7,11):
        for p in (5,7,11,19):
            # Norm on an invariant F_p line is multiplication by degree.
            kernel_dimension = int(degree % p == 0)
            check(kernel_dimension == int(degree == p), 'coefficient/degree distinction')
            coefficient_controls.append([degree,p,kernel_dimension])
    finiteness_only_controls = []
    for p in (5,7,11):
        for a in (1,2,3,4):
            # Analytic model: S=(Qp/Zp)^(2+2a), W=(Qp/Zp)^2.
            # S[N]=S[p] is finite but its quotient excess has corank 2a.
            finiteness_only_controls.append({'p':p,'even_excess_corank':2*a,
                'finite_norm_kernel_order':p**(2+2*a), 'upper_bound_2_holds':False})
    return {'status':'PASS_ABSTRACT_ALGEBRA_ONLY', 'module_cases':cases,
            'minimal_length_cases':minimal_cases,
            'coefficient_degree_controls':coefficient_controls,
            'finiteness_only_controls':finiteness_only_controls,
            'new_seed_values':0, 'new_seed_upper_bounds':0,
            'FIN':'UNCHANGED','ORDER9':'UNCHANGED','Q36':'UNCHANGED'}

if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
