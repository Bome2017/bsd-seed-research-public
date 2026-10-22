#!/usr/bin/env python3
"""Referee 2 delta check (regression): rev 2 sec 11.R3 explicit automorphisms of E: y^2 + y = x^3 over Fbar_2.
Arithmetic in GF(64) = GF(2)[z]/(z^6 + z + 1). Checks: the maps (x,y) -> (a^2 x + s^2, y + a^2 s x + t), a in F_4^x, s in F_4, t^2 + t = s^6,
preserve E(F_64) bijectively; there are 24; the two t for fixed (a,s) differ by 1 (= [-1]); E(F_4) \\ {O} = E[3] has x in F_4 (3-division poly x^4+x);
the induced action on the four x-values is AGL_1(F_4) of order 12 (kernel {+-1}), point stabilizers of order 3."""
MOD = 0b1000011  # z^6 + z + 1
def mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a & 0b1000000: a ^= MOD
    return r
def pw(a, n):
    r = 1
    for _ in range(n): r = mul(r, a)
    return r
F = list(range(64))
assert all(pw(g, 63) == 1 for g in F if g)            # field sanity
F4 = [x for x in F if pw(x, 4) == x]; assert len(F4) == 4
F4x = [x for x in F4 if x]
def on_curve(x, y): return mul(y, y) ^ y ^ pw(x, 3) == 0
pts = [(x, y) for x in F for y in F if on_curve(x, y)]
print("#E(F_64) affine points:", len(pts), "(expected 80 = 81 - 1)")
autos = []
for a in F4x:
    for s in F4:
        for t in F:
            if mul(t, t) ^ t != pw(s, 6): continue
            a2 = mul(a, a)
            img = [(mul(a2, x) ^ mul(s, s), y ^ mul(mul(a2, s), x) ^ t) for (x, y) in pts]
            if all(on_curve(*p) for p in img) and len(set(img)) == len(pts):
                autos.append((a, s, t))
print("automorphisms found:", len(autos))
by_as = {}
for a, s, t in autos: by_as.setdefault((a, s), []).append(t)
print("each (a,s) has two t differing by 1:", all(len(v) == 2 and (v[0] ^ v[1]) == 1 for v in by_as.values()))
e4 = [(x, y) for (x, y) in pts if x in F4 and y in F4]
print("E(F_4) affine points:", len(e4), "(8 = E[3] minus O); all x in F_4:", all(x in F4 for x, _ in e4))
# 3-division polynomial x^4 + x vanishes exactly on F_4
print("roots of x^4 + x in F_64 are exactly F_4:", sorted(x for x in F if pw(x, 4) ^ x == 0) == sorted(F4))
perms = set()
for a, s, t in autos:
    a2 = mul(a, a); perms.add(tuple(mul(a2, x) ^ mul(s, s) for x in F4))
print("induced permutation group on the four 3-subgroups has order", len(perms), "(AGL_1(F_4) = A_4 has 12)")
stabs = [sum(1 for pmap in perms if pmap[i] == F4[i]) for i in range(4)]
print("stabilizer orders of the four 3-subgroups:", stabs)
kernel = [(a, s, t) for (a, s, t) in autos if all(mul(mul(a, a), x) ^ mul(s, s) == x for x in F4)]
print("kernel of the action (should be {+-1}: a=1, s=0, t in {0,1}):", kernel)
