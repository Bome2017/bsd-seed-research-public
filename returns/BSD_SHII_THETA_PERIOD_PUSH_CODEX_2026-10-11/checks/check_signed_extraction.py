"""Exact synthetic controls. None of the input arrays are seed theta values."""
from fractions import Fraction
from math import comb
import json
import random
from signed_theta_extractor import extract


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def cyclo(p, j):
    # Phi_(p^j)(1+T) = sum_(a=0)^(p-1) (1+T)^(a*p^(j-1)).
    out = [0] * ((p-1)*p**(j-1)+1)
    for a in range(p):
        k = a*p**(j-1)
        for i in range(k+1):
            out[i] += comb(k, i)
    return out


def factors(p, n):
    A, H = [1], [0, 1]
    for j in range(1, n+1):
        f = cyclo(p, j)
        if (j-n) % 2:
            A = mul(A, f)
        else:
            H = mul(H, f)
    omega = [0] + [comb(p**n, k) for k in range(1, p**n+1)]
    assert mul(A, H) == omega
    return A, H, omega


def to_group(poly, size):
    # T^k=(gamma-1)^k, degree strictly less than size in these controls.
    assert len(poly) <= size
    out = [0]*size
    for k, b in enumerate(poly):
        for a in range(k+1):
            out[a] += b*comb(k, a)*(-1)**(k-a)
    return out


def monic_remainder(a, f, modulus):
    a = trim([x % modulus for x in a])
    while len(a) >= len(f):
        coefficient, shift = a[-1], len(a)-len(f)
        for j, x in enumerate(f):
            a[shift+j] = (a[shift+j]-coefficient*x) % modulus
        trim(a)
    return a


rng = random.Random(20261011)
cases = 0
for p, n in [(p, n) for p in (5, 7, 11, 17) for n in (1, 2)] + [(5, 3), (7, 3)]:
    A, H, omega = factors(p, n)
    d = len(A)-1
    assert [x % p for x in A] == [0]*d+[1]
    for r in (1, 2, 3):
        modulus = p**r
        for c in range(12):
            q = [rng.randrange(-modulus, modulus) for _ in range(min(7, len(H)-1))]
            q[0] = 1
            content = c % r
            q = [p**content*x for x in q]
            theta = mul(A, q)
            group = to_group(theta, p**n)
            for k in range(3):
                moment = sum(b*comb(a, d+k) for a, b in enumerate(group)) % p
                assert moment == q[k] % p
            if n >= 2:
                assert all(x % p == 0 for x in theta[:3])
            # Representatives differing by H give the same source in Lambda/(omega).
            altered = theta + [0]*max(0, len(omega)+1-len(theta))
            ambiguity = mul(omega, [2, 3])
            for j, x in enumerate(ambiguity):
                altered[j] += x
            assert monic_remainder(altered, omega, modulus) == trim([x % modulus for x in theta])
            # Multiplication by the monic factor does not erase genuine p-content.
            assert all(x % (p**content) == 0 for x in theta)
            assert any(x % (p**(content+1)) != 0 for x in theta)
            cases += 1

lucas_cases = 0
for p in (5, 7, 11, 17, 19, 23, 29):
    for a in range(p*p):
        a0, a1 = a % p, a // p
        assert comb(a, p-1) % p == int(a0 == p-1)
        assert comb(a, p) % p == a1
        assert comb(a, p+1) % p == a0*a1 % p
        lucas_cases += 1
    A2, H2, _ = factors(p, 2)
    for _ in range(20):
        qminus = [rng.randrange(p) for _ in range(3)]
        qplus = [rng.randrange(p) for _ in range(3)]
        theta1 = to_group([-x for x in qminus], p)
        theta2 = to_group(mul(A2, [-x for x in qplus]), p*p)
        output = extract(p, theta1, theta2)
        assert output["minus_jet_mod_p"] == qminus
        assert output["plus_jet_mod_p"] == qplus

valuation_cases = []
for p in (5, 7, 17):
    for n in range(1, 9):
        denom = p**(n-1)*(p-1)
        s = Fraction(int(n % 2 == 0), denom)
        for k in range(1, n):
            if (k-n) % 2:
                # Difference of valuations of the two root-of-unity factors.
                diff = Fraction(1, p**(n-k-1)*(p-1))-Fraction(1, p**(n-k)*(p-1))
                term = Fraction(p**k-p**(k-1), denom)
                assert diff == term
                s += term
        h = (n+1)//2
        period = Fraction(n+1, 2)-h
        delta = s-Fraction(n+1, 2)
        assert period+delta == s-h
        assert period == (0 if n % 2 else Fraction(1, 2))
        valuation_cases.append({"p": p, "n": n, "s": str(s), "period": str(period), "delta": str(delta)})

print(json.dumps({"status": "PASS", "scope": "synthetic polynomial and rational valuation controls, no seed values", "finite_ring_cases": cases, "lucas_indices": lucas_cases, "two_layer_reconstructions": 140, "valuation_controls": valuation_cases}, indent=2))
