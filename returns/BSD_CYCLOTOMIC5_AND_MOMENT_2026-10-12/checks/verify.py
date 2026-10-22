#!/usr/bin/env python3
"""Exact arithmetic replay and finite-level controls; NOT an end-to-end BSD verifier.

Run from any directory: python3 /path/to/checks/verify.py
Only the Python standard library is required. Historical symbol provenance and
published arithmetic theorems remain external inputs. No new symbol is evaluated.
"""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
from random import Random

ROOT = Path(__file__).resolve().parents[1]
BLOBS = {
    'SYMBOLS_m25.txt': 'b0d766f63e90ac9d17b2ca15ee2e387cd6b34ff6',
    'SYMBOLS_m5.txt': 'a9961d9d45bc22605a331c994a3dee4119c1c12b',
}

def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)

def is_prime(p: int) -> bool:
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

def validate_level(p: int, n: int) -> None:
    if not is_prime(p) or p < 5 or type(n) is not int or n < 2:
        raise ValueError('requires prime p >= 5 and integer n >= 2')

def residue(x: Fraction | int, modulus: int) -> int:
    a = Fraction(x)
    try:
        return a.numerator * pow(a.denominator, -1, modulus) % modulus
    except ValueError as exc:
        raise ValueError('a symbol denominator is not a p-unit') from exc

def load_table(name: str, modulus: int) -> dict[int, Fraction]:
    data = (ROOT / 'inputs' / name).read_bytes()
    git = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(git == BLOBS[name], 'historical Git blob mismatch: '+name)
    table = {}
    for line in data.decode('utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        if len(fields) != 3 or int(fields[0]) in table:
            raise ValueError('malformed or duplicate symbol row')
        table[int(fields[0])] = Fraction(fields[1])
    return table

def raw_moment(p: int, n: int, table: dict[int, Fraction]) -> tuple[Fraction, list[Fraction]]:
    """Return the raw quadratic moment in exactly the table's period convention.

    This validates finite input shape and denominators, not its arithmetic source.
    """
    validate_level(p, n)
    m, q = p**n, p**(n-1)
    if set(table) != {b for b in range(1, m) if b % p}:
        raise ValueError('table must contain every unit modulo p^n exactly once')
    for value in table.values():
        residue(value, p)
    weights = [Fraction(0) for _ in range(q)]
    seen = set()
    for a in range(1, p):
        b = pow(a, p**(n-1), m)  # Teichmuller lift modulo p^n
        for j in range(q):
            require(b not in seen, 'duplicate Teichmuller/gamma coordinate')
            seen.add(b)
            weights[j] += table[b]
            b = b*(1+p) % m
    require(seen == set(table), 'incomplete coordinate enumeration')
    return sum((comb(j, 2)*v for j,v in enumerate(weights)), Fraction(0)), weights

def known_valuation(a: int, p: int, precision: int) -> int | None:
    a %= p**precision
    if a == 0:
        return None  # only a lower bound; not a zero/nonzero decision
    v = 0
    while a % p == 0:
        v += 1
        a //= p
    return v

def numerator_test(p: int, n: int, moment: Fraction) -> dict:
    validate_level(p, n)
    k = n-1
    a = residue(moment, p**k)
    v = known_valuation(a, p, k)
    return {'precision': k, 'raw_moment_residue': a, 'valuation': v,
            'status': 'NONZERO_NUMERATOR_IF_SOURCE_MATCHED' if v is not None else 'INCONCLUSIVE',
            'sha_certified': False}

def project_gamma(coeff: list[int], q: int, modulus: int) -> list[int]:
    """F(U) -> F(z-1) mod (z^q-1, modulus), exact binomial implementation."""
    out = [0]*q
    for k, a in enumerate(coeff):
        for i in range(k+1):
            out[i % q] = (out[i % q] + a*comb(k,i)*(-1)**(k-i)) % modulus
    return out

def jet(weights: list[int | Fraction], k: int) -> int | Fraction:
    return sum(comb(j,k)*a for j,a in enumerate(weights) if j >= k)

def hensel_unit(p: int, ap: int, digits: int) -> int:
    a, mod = ap % p, p
    if not a:
        raise ValueError('not ordinary')
    for _ in range(1,digits):
        t = (-(a*a-ap*a+p)//mod)*pow(2*a-ap,-1,p) % p
        a += mod*t
        mod *= p
    require((a*a-ap*a+p) % mod == 0, 'Hensel check')
    return a

def main() -> dict:
    t25, t5 = load_table('SYMBOLS_m25.txt',25), load_table('SYMBOLS_m5.txt',5)
    A, weights = raw_moment(5,2,t25)
    require(weights == [-76,0,-76,76,76] and A == 608, 'seed raw moment')
    require(all(t25[b] == t25[25-b] for b in t25), 'plus symmetry')
    require(sum(t5.values()) == 0, 'lower-layer augmentation')
    for a in range(1,5):
        require(sum(t25[a+5*j] for j in range(5)) == -2*t5[a], 'Hecke T5')
    # Independent inversion of the principal-unit coordinate, rather than grouped sums.
    m, inverse_sum = 25, Fraction(0)
    for b, val in t25.items():
        omega = pow(b % 5,5,m)
        principal = b*pow(omega,-1,m) % m
        js = [j for j in range(5) if pow(6,j,m) == principal]
        require(len(js) == 1, 'discrete-log uniqueness')
        inverse_sum += comb(js[0],2)*val
    require(inverse_sum == A, 'independent seed moment')
    alpha = hensel_unit(5,-2,8)
    # Division by 2 converts the retained omega_1 table to Omega_E = 2 omega_1.
    neron_moment = A/2
    one_table_residue = (1-5*pow(alpha,-2,5))*pow(alpha,-2,5)*residue(neron_moment,5) % 5
    direct = Fraction(0)
    for a in range(1,5):
        for j in range(5):
            b = pow(a,5,25)*pow(6,j,25) % 25
            mu = (pow(alpha,-2,5)*residue(t25[b]/2,5)
                  -pow(alpha,-3,5)*residue(t5[b % 5]/2,5)) % 5
            direct += comb(j,2)*mu
    require(one_table_residue == direct % 5 == 1, 'standard coefficient residue')
    rng, synthetic = Random(20261012), 0
    for p,n in [(5,2),(5,3),(5,4),(7,2),(7,3),(11,2),(11,3)]:
        q, modulus = p**(n-1), p**(n+3)
        for trial in range(12):
            coeff = [rng.randrange(-20,21) for _ in range(q+3)]
            if trial % 2 == 0:
                coeff[0:2] = [0,0]
            alpha_s = rng.randrange(1,p)
            theta = [trial+3]  # arbitrary integral degree-zero first layer
            for layer in range(2,n+1):
                ql, qp = p**(layer-1), p**(layer-2)
                P = project_gamma(coeff,ql,modulus)
                theta = [(pow(alpha_s,layer,modulus)*P[j]
                          +pow(alpha_s,-1,modulus)*theta[j % qp]) % modulus for j in range(ql)]
            A_s = int(jet(theta,2)) % modulus
            estimate = (1-p*pow(alpha_s,-2,modulus))*pow(alpha_s,-n,modulus)*A_s % modulus
            require((estimate-coeff[2]) % p**(n-1) == 0, 'one-table congruence')
            synthetic += 1
    sharpness = []
    for p,n in [(5,2),(5,3),(7,2),(7,3),(11,2)]:
        q, mod = p**(n-1), p**(n+2)
        f0 = [0]*(q+2)
        f0[2] = q
        f1 = f0.copy()
        for k in range(1,q+1):
            f1[k+1] += (p-1)*comb(q,k)
        require(project_gamma(f0,q,mod) == project_gamma(f1,q,mod), 'same finite projection')
        require(known_valuation(f0[2],p,n+2) == n-1, 'first sharpness valuation')
        require(known_valuation(f1[2],p,n+2) == n, 'second sharpness valuation')
        sharpness.append({'p':p,'n':n,'same_projection':True,'valuations':[n-1,n]})
    bad_cases = [(4,2,t25),(3,2,t25),(5,1,t25),(True,2,t25),(5,True,t25),
                 (5,2,{b:v for b,v in t25.items() if b!=1}),
                 (5,2,{**t25,1:Fraction(1,5)}),(5,2,{**t25,0:Fraction(0)})]
    for p,n,t in bad_cases:
        try:
            raw_moment(p,n,t)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid table/level admitted')
    require(numerator_test(17,2,Fraction(0))['status']=='INCONCLUSIVE','zero residue guard')
    require(numerator_test(17,3,Fraction(17))['valuation']==1,'valuation-one boundary')
    require(numerator_test(17,4,Fraction(17**2))['valuation']==2,'valuation-two boundary')
    require(numerator_test(17,3,Fraction(17**2))['valuation'] is None,'insufficient precision')
    bindings = {name: {'git_blob':BLOBS[name], 'sha256':hashlib.sha256((ROOT/'inputs'/name).read_bytes()).hexdigest()}
                for name in sorted(BLOBS)}
    return {'status':'PASS_EXACT_REPLAY_AND_FORMAL_ARITHMETIC_CONTROLS',
            'input_bindings':bindings,
            'seed_p5':{'raw_gamma_weights':[int(x) for x in weights],
                       'raw_quadratic_moment':int(A),'neron_quadratic_moment':int(neron_moment),
                       'alpha_mod5':alpha%5,'standard_L2_mod5':int(one_table_residue),
                       'L2_valuation':0,'new_symbol_evaluation':False,
                       'new_base_field_primary_result':False},
            'synthetic_one_table_cases':synthetic,'sharpness_cases':sharpness,
            'invalid_input_cases':len(bad_cases),'precision_boundary_cases':4,
            'tower_theorem_grade':'WRITTEN_DERIVATION_NOT_VERIFIED_BY_THIS_SCRIPT',
            'new_actual_coefficients':0,'new_coefficient_primes_settled':0,
            'FIN':'UNCHANGED','ORDER9':'UNCHANGED','Q36':'UNCHANGED'}

if __name__ == '__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
