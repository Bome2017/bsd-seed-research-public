#!/usr/bin/env python3
"""Exact supporting checks only; does not compute any Galois image or Sha.

Run with Python 3.10+. Uses the standard library, no network or subprocesses.
The uniform theorem requires the mathematical proof in PROOF.md.
"""
from __future__ import annotations
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from time import process_time

ROOT = Path(__file__).resolve().parent
# Sparse polynomials over Z; coordinates are (m,n,u,X,Y,B).
Exp = tuple[int, int, int, int, int, int]
Poly = dict[Exp, int]

def constant(c: int) -> Poly:
    return {(0, 0, 0, 0, 0, 0): c} if c else {}

def variable(i: int) -> Poly:
    e = [0] * 6
    e[i] = 1
    return {tuple(e): 1}  # type: ignore[dict-item]

def add(*terms: Poly) -> Poly:
    out: Poly = {}
    for t in terms:
        for e, c in t.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}

def scale(a: Poly, c: int) -> Poly:
    return {e: c * x for e, x in a.items() if c * x}

def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for e, c in a.items():
        for f, d in b.items():
            ef = tuple(x + y for x, y in zip(e, f))
            out[ef] = out.get(ef, 0) + c * d
    return {e: c for e, c in out.items() if c}

def power(a: Poly, n: int) -> Poly:
    if n < 0:
        raise ValueError('negative polynomial exponent')
    ans = constant(1)
    for _ in range(n):
        ans = mul(ans, a)
    return ans

def polynomial_checks() -> dict[str, bool]:
    m, n, u, x, y, b = [variable(i) for i in range(6)]
    A = add(m, scale(power(n, 2), 16))
    B = add(m, scale(power(n, 2), 25))
    a2 = scale(A, -5)
    a4 = scale(mul(A, B), 4)
    c4 = add(scale(power(a2, 2), 16), scale(a4, -48))
    delta = scale(mul(power(a4, 2), add(power(a2, 2), scale(a4, -4))), 16)
    assert c4 == scale(mul(A, add(scale(m, 13), scale(power(n, 2), 100))), 16)
    assert delta == scale(mul(mul(m, power(A, 3)), power(B, 2)), 2**8 * 3**2)
    # Pull back original polynomial under A=u^4, x=u^2 X, y=u^3 Y.
    xold, yold, Aprime = mul(power(u, 2), x), mul(power(u, 3), y), power(u, 4)
    original = add(power(yold, 2), scale(power(xold, 3), -1),
                   scale(mul(Aprime, power(xold, 2)), 5),
                   scale(mul(mul(Aprime, b), xold), -4))
    scaled = mul(power(u, 6), add(power(y, 2), scale(power(x, 3), -1),
                         scale(mul(power(u, 2), power(x, 2)), 5),
                         scale(mul(b, x), -4)))
    assert original == scaled
    # Point identities on the family.
    def on_curve(px: Poly, py: Poly) -> bool:
        return not add(power(py, 2), scale(power(px, 3), -1),
                       scale(mul(A, power(px, 2)), 5),
                       scale(mul(mul(A, B), px), -4))
    assert on_curve(A, scale(mul(n, A), 6))
    assert on_curve(scale(power(n, 2), 36),
                    scale(mul(n, add(m, scale(power(n, 2), -2))), 12))
    return {'c4_identity': True, 'discriminant_identity': True,
            'good_model_scaling_identity': True, 'two_point_identities': True}

Matrix = tuple[int, int, int, int]
def mm(a: Matrix, b: Matrix, p: int) -> Matrix:
    return ((a[0]*b[0]+a[1]*b[2]) % p, (a[0]*b[1]+a[1]*b[3]) % p,
            (a[2]*b[0]+a[3]*b[2]) % p, (a[2]*b[1]+a[3]*b[3]) % p)

def inv(a: Matrix, p: int) -> Matrix:
    d = pow((a[0]*a[3]-a[1]*a[2]) % p, -1, p)
    return (d*a[3] % p, -d*a[1] % p, -d*a[2] % p, d*a[0] % p)

def elementary_generation(p: int) -> int:
    identity = (1, 0, 0, 1)
    gens = ((1, 1, 0, 1), (1, 0, 1, 1))
    seen = {identity}
    todo = [identity]
    while todo:
        a = todo.pop()
        for b in gens:
            c = mm(a, b, p)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    assert len(seen) == p*(p*p-1)
    return len(seen)

def local_matrix_check_5() -> dict[str, object]:
    p = 5
    T = (2, 0, 0, 3)
    assert mm(T, T, p) == (4, 0, 0, 4)
    assert (T[0]*T[3]-T[1]*T[2]) % p == 1
    lines = [(1, a) for a in range(p)] + [(0, 1)]
    def invariant(a: Matrix, v: tuple[int, int]) -> bool:
        w = ((a[0]*v[0]+a[1]*v[1]) % p, (a[2]*v[0]+a[3]*v[1]) % p)
        return (w[0]*v[1]-w[1]*v[0]) % p == 0
    checked = []
    for r in range(1, p):
        F = (0, -r % p, 1, 0)
        assert mm(mm(F, T, p), inv(F, p), p) == inv(T, p)
        assert not any(invariant(T, v) and invariant(F, v) for v in lines)
        checked.append(r)
    return {'T_squared': '-I', 'determinant_T': 1,
            'F_determinants_tested': checked,
            'F_conjugates_T_to_inverse': True,
            'common_F5_invariant_line': False,
            'scope': 'Model matrix consistency, NOT a computation of actual arithmetic inertia.'}

def prime_by_trial_division(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, math.isqrt(n)+1, 2):
        if n % d == 0:
            return False
    return True

def point_count(m: int, n: int, p: int) -> int:
    A, B = m+16*n*n, m+25*n*n
    return 1 + sum((y*y-(x*x*x-5*A*x*x+4*A*B*x)) % p == 0
                   for x in range(p) for y in range(p))

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    start = process_time()
    poly = polynomial_checks()
    residues = [a for a in range(24) if a*a % 24 == 0]
    assert residues == [0, 12]
    assert 11+16*12**2 > 163
    # Inclusion C1 -> C60 holds on congruences, without a search.
    assert 840 % 120 == 0 and 491 % 120 == 11 and 420 % 60 == 0
    assert 16*60**2 % 120 == 0 and 25*60**2 % 120 == 0
    examples = []
    for m,n in [(3491,60),(3011,420)]:
        A,B = m+16*n*n,m+25*n*n
        primes = [prime_by_trial_division(q) for q in (m,A,B)]
        assert all(primes)
        assert m % 120 == 11 and n % 60 == 0
        assert all(q % 24 == 11 for q in (m,A,B))
        count = point_count(m,n,5)
        assert count == 8
        examples.append({'m':m, 'n':n, 'A':A, 'B':B,
            'trial_division_primes':primes,
            'trial_division_max_divisors':[math.isqrt(q) for q in (m,A,B)],
            'C60_member':True, 'C1_member':m % 840 == 491 and n % 420 == 0,
            'F5_point_count':count, 'a5':6-count,
            'odd_conductor_part':3*m*A*A*B})
    old,new = examples[1]['odd_conductor_part'],examples[0]['odd_conductor_part']
    ratio=Fraction(old,new)
    receipt = {
        'status':'PASS_EXACT_SUPPORTING_CHECKS',
        'cpu_seconds':round(process_time()-start,6),
        'polynomial_identities':poly,
        'n_mod_24_from_n_squared_zero':residues,
        'lower_bound_A':11+16*12**2,
        'C1_contained_in_C60_congruences':True,
        'C60_polynomial_pattern_divisibility':True,
        'local_matrix_model':local_matrix_check_5(),
        'upper_lower_SL2_orders':{str(p):elementary_generation(p) for p in (3,5,7,11,13,17)},
        'examples':examples,
        'old_over_new_odd_conductor_ratio':{'numerator':ratio.numerator,
            'denominator':ratio.denominator, 'decimal':float(ratio)},
        'script_sha256':sha256(Path(__file__)),
        'input_review_sha256':sha256(ROOT/'input'/'00_REVIEW.md'),
        'NOT_EXECUTED':['number-field construction','class-group calculation','Selmer computation',
                        'Sha computation','actual arithmetic Galois-image computation',
                        'subgroup-lattice replay of the already-reviewed central theorem'],
        'NOT_PROVED_BY_SCRIPT':['uniform all-odd-prime theorem','Tao-Ziegler infinitude application',
                               'Tate-curve transvection theorem','Mazur prime-isogeny theorem'],
        'mathematical_status':'See PROOF.md; independent proof review required, no canonical seal.'
    }
    receipt['cpu_seconds']=round(process_time()-start,6)
    out=ROOT/'EXACT_CHECK_RECEIPT.json'
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
