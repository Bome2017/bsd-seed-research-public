#!/usr/bin/env python3
"""Brute-force check of 03 Lemma 4'(a) at Eichler level p^2 (the 4547 structure), p = 5, 7, 11.

O_p = [[Z_p, Z_p],[p^2 Z_p, Z_p]], Q(r) = u det(r), (l,r) = u trd(l adj r), dual vectors
l = [[l1, l2 p^-2],[l3, l4]] (l_i in Z_p).  For e <= 2 and c = p^e c' (p ∤ c'), ubar = c'^{-1} mod p^e:

  Gs_p(l) := sum_{r in O_p/p^e O_p} e( ubar (a Q(r) + (l,r)) / p^e )
          = p^{3e} 1[l2 ≡ l3 ≡ 0 (mod p^e)] e( -u ubar l1 l4 / (a p^e) ).

The brute force uses only the definitions (Q, the pairing, the quotient O_p/p^e O_p).
Only |Gs_p| = p^{3e} (or 0) is used in Lemma N2; the phase is checked as well.
"""
import cmath, itertools, json, random

def brute(p, e, a, u, ub, l):
    m = p**e
    l1, l2, l3, l4 = l
    tot = 0j
    for r1, r2, r3, r4 in itertools.product(range(m), repeat=4):
        Q = u*(r1*r4 - p*p*r2*r3)
        B = u*(l1*r4 + l4*r1 - l2*r3 - l3*r2)
        tot += cmath.exp(2j*cmath.pi*((ub*(a*Q + B)) % m)/m)
    return tot

def closed(p, e, a, u, ub, l):
    m = p**e
    l1, l2, l3, l4 = l
    if l2 % m or l3 % m: return 0j
    ainv = pow(a, -1, m)
    return p**(3*e) * cmath.exp(2j*cmath.pi*((-u*ub*l1*l4*ainv) % m)/m)

rng = random.Random(4547)
res, maxdiff, n = [], 0.0, 0
for p, e, trials in ((5, 1, 60), (7, 1, 60), (11, 1, 40), (5, 2, 6)):
    m = p**e
    for _ in range(trials):
        a = rng.choice([x for x in range(1, m) if x % p])
        u = rng.choice([x for x in range(1, m) if x % p])
        ub = rng.choice([x for x in range(1, m) if x % p])
        if rng.random() < 0.5:     # force the support condition half the time
            l = (rng.randrange(m), m*rng.randrange(3), m*rng.randrange(3), rng.randrange(m))
        else:
            l = tuple(rng.randrange(m) for _ in range(4))
        b, c = brute(p, e, a, u, ub, l), closed(p, e, a, u, ub, l)
        d = abs(b - c); maxdiff = max(maxdiff, d); n += 1
    res.append({"p": p, "e": e, "trials": trials})
out = {"cases": n, "max_abs_diff": maxdiff, "sizes": res,
       "pass": maxdiff < 1e-6 * 5**6}
print(json.dumps(out, indent=1))
