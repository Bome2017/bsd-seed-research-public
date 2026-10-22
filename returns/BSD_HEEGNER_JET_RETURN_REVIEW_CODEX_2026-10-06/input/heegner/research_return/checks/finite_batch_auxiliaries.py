"""Exact producer (revision 2): inert auxiliary primes l with p | gcd(a_l, l+1), a_l allowed
nonzero, for the primes p = 37, 41 missed by the exact-supersingular table, and for p = 53.
Also records a_p for the primes p covered by the earlier table (ordinary vs supersingular).
Model: y^2 = x^3 - 22735 x^2 + 106272484 x (u = 1 change of the minimal model).
Point count by a full Legendre-symbol sum. Search: l = -1 mod p, increasing, first hits."""
import json, math
A2, A4 = -22735, 106272484
BAD = {2, 3, 23, 2243, 4547, 5843}
def isprime(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
def a_l(l):
    sq = bytearray(l)
    for t in range(l): sq[t * t % l] = 1
    tot = 0
    for x in range(l):
        v = (x * x * x + A2 * x * x + A4 * x) % l
        tot += 1 if v == 0 else (2 if sq[v] else 0)
    return l - tot
def factor(n):
    f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f
def search(p, want):
    out = []; l = 2 * p - 1
    while len(out) < want:
        if isprime(l) and l not in BAD and pow(-23 % l, (l - 1) // 2, l) == l - 1:
            a = a_l(l)
            if a % p == 0:
                M = math.gcd(a, l + 1)
                out.append({"l": l, "a_l": a, "l_plus_1_factors": factor(l + 1),
                            "M_l": M, "M_l_factors": factor(M),
                            "kolyvagin_for_p_ge_5": sorted({q for q in factor(M) if q >= 5 and q != 23})})
        l += p
    return out
res = {"finite_batch": {str(p): search(p, n) for p, n in ((37, 2), (41, 2), (53, 2))}}
cov = [5,7,11,13,17,19,29,31,43,47,53,59,61,71,73,83,89,113,137,139,331,353,401,487,883,1399,5077]
res["a_p_of_covered_primes"] = {str(p): {"a_p": a_l(p), "type": "supersingular" if a_l(p) % p == 0 else "ordinary"} for p in cov}
print(json.dumps(res, indent=1))
