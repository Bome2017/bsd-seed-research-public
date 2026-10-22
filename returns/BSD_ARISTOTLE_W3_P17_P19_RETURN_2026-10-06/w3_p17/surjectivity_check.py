#!/usr/bin/env python3
"""Serre's criterion (Proprietes galoisiennes, 1972, section 2, Prop. 19) for rho-bar_p of the seed:
G ⊂ GL2(F_p), p >= 5, with det surjective, contains SL2(F_p) if it contains Frobenius elements with
 (a) tr^2-4det a nonzero square, (b) tr^2-4det a non-square, (c) u = tr^2/det not in {0,1,2,4} and u^2-3u+1 != 0.
Frobenius at good l != p has tr = a_l, det = l."""
import json, sys
A2, A4 = -22735, 106272484
BAD = {2, 3, 2243, 4547, 5843}
def ap(l):
    sq = [0]*l
    for y in range(l): sq[y*y % l] += 1
    return l - sum(sq[(x*x*x + A2*x*x + A4*x) % l] for x in range(l))
def is_sq(x, p): x %= p; return x != 0 and pow(x, (p-1)//2, p) == 1
def primes(n):
    s = [1]*(n+1); s[0] = s[1] = 0
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = [0]*len(s[i*i::i])
    return [i for i in range(n+1) if s[i]]
def check(p, lim=400):
    wa = wb = wc = None
    for l in primes(lim):
        if l in BAD or l == p: continue
        a = ap(l); d = (a*a - 4*l) % p
        if wa is None and d and is_sq(d, p): wa = l
        if wb is None and d and not is_sq(d, p): wb = l
        u = a*a*pow(l, -1, p) % p
        if wc is None and u not in (0, 1, 2, 4) and (u*u - 3*u + 1) % p: wc = l
        if wa and wb and wc: return {"p": p, "surjective": True, "witnesses_a_b_c": [wa, wb, wc]}
    return {"p": p, "surjective": "undetermined"}
out = [check(p) for p in (17, 19, 53)]
print(json.dumps(out)); json.dump(out, open('SURJECTIVITY.json', 'w'))
