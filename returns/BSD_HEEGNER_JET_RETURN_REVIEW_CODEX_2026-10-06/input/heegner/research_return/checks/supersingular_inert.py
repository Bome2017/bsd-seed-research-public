"""Exact producer: supersingular (a_l = 0) good primes l of the seed curve that are
inert in K = Q(sqrt(-23)), l < LIMIT, with the primes p >= 5 dividing l+1.
Model: y^2 = x^3 - 22735 x^2 + 106272484 x (u = 1 change of the minimal model; same
point counts at every odd good prime). Point count by a full Legendre-symbol sum."""
import json, sys
A2, A4 = -22735, 106272484
BAD = {2, 3, 2243, 4547, 5843}
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
def primes(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def a_l(l):
    sq = bytearray(l); 
    for t in range(l): sq[t*t % l] = 1
    tot = 0
    for x in range(l):
        v = (x*x*x + A2*x*x + A4*x) % l
        tot += 1 if v == 0 else (2 if sq[v] else 0)
    return l - tot  # #E = tot + 1 (point at infinity), a_l = l + 1 - #E = l - tot
def factor(n):
    f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f
out = []
for l in primes(LIMIT):
    if l in BAD or l == 23: continue
    if pow(-23 % l, (l - 1) // 2, l) != l - 1: continue   # inert in K
    if a_l(l) == 0:
        ps = sorted({p for p in factor(l + 1) if p >= 5})
        out.append({"l": l, "l_plus_1_factors": factor(l + 1), "covered_p_ge_5": ps})
print(json.dumps({"limit": LIMIT, "count": len(out), "primes": out}, indent=1))
