#!/usr/bin/env python3
"""Pure-Python 2-isogeny descent on E^{-7}: y^2 = x^3 + A x^2 + B x (A=159145, B=5207351716).

Verifier check (not a lab deliverable): decides whether dim S^phi + dim S^phihat - 1 equals 1,
i.e. whether the assessment's conditional gain Sha(E^{-7}/Q)[2^inf]=0 is actually delivered
by a 2-isogeny descent.

Setup (Silverman AEC X.4.9 / Cremona ch.3): for E: y^2 = x^3 + a x^2 + b x and
E': y^2 = x^3 - 2a x^2 + (a^2-4b) x, the Selmer group S^(phi)(E'/Q)... we only need the two
groups of classes d (squarefree, sign allowed) with
   (I)  d | b          : homogeneous space  d w^2 = d^2 + a d z^2 + b z^4          (lifts of E(Q)/phihat(E'(Q)))
   (II) d | a^2-4b     : homogeneous space  d w^2 = d^2 - 2a d z^2 + (a^2-4b) z^4  (lifts of E'(Q)/phi(E(Q)))
Local solubility at all p | 2 b (a^2-4b) and at infinity. Group (I) always contains the class of b
(image of (0,0) in E) and group (II) the class of a^2-4b (image of (0,0) in E').
Then dim Sel_2(E) <= dim(I) + dim(II) - 1 and rank E(Q) <= dim(I) + dim(II) - 2.
"""
import sys
from itertools import product

A = 159145
B = 5207351716          # 2^2 * 7^2 * 4547 * 5843
C = A*A - 4*B           # = 49 * 9 * 2243 * 4547

def factor(n):
    n = abs(n); f = {}; p = 2
    while p*p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def vp(n, p):
    if n == 0: return 10**9
    v = 0
    while n % p == 0: n //= p; v += 1
    return v

def is_sq_unit(u, p):
    """u a p-adic unit (integer coprime to p): is it a square in Z_p?"""
    if p == 2: return u % 8 == 1
    return pow(u % p, (p-1)//2, p) == 1

def poly_eval(cs, x):  # cs[i] coefficient of x^i
    r = 0
    for c in reversed(cs): r = r*x + c
    return r

def poly_deriv(cs):
    return [i*cs[i] for i in range(1, len(cs))]

def zp_soluble(cs, p, x0, nu, depth_limit):
    """Is there x in Z_p, x = x0 mod p^nu, with f(x) a square in Z_p (0 allowed)?  f = cs."""
    # Hensel-root criterion: a root of f near x0 gives (x,0).
    fx = poly_eval(cs, x0)
    if fx == 0: return True
    v = vp(fx, p)
    fd = poly_eval(poly_deriv(cs), x0)
    vd = vp(fd, p) if fd != 0 else 10**9
    if v > 2*vd: return True
    # If v(f(x0)) < nu, every x = x0 mod p^nu has f(x) = f(x0) mod p^nu, so the square class is decided
    # provided nu >= v + 1 (odd p) or nu >= v + 3 (p=2).
    need = v + (3 if p == 2 else 1)
    if nu >= need:
        if v % 2 == 1: return False
        return is_sq_unit(fx // p**v, p)
    if nu > depth_limit:
        raise RuntimeError("depth limit exceeded at p=%d" % p)
    for t in range(p):
        if zp_soluble(cs, p, x0 + t*p**nu, nu+1, depth_limit):
            return True
    return False

def qp_soluble_quartic(q4, q2, q0, p):
    """w^2 = q4 u^4 + q2 u^2 v^2 + q0 v^4 soluble in Q_p (projectively, (u:v) != (0:0))?"""
    cs = [q0, 0, q2, 0, q4]      # v = 1, u in Z_p
    rcs = [q4, 0, q2, 0, q0]     # u = 1, v in p Z_p
    disc_bound = 60
    if zp_soluble(cs, p, 0, 0, disc_bound): return True
    # v in pZ_p, u = 1
    for t in range(1):  # x0 = 0 mod p
        pass
    return zp_soluble(rcs, p, 0, 1, disc_bound)

def real_soluble(q4, q2, q0):
    # exists real (u,v) != 0 with q4 u^4 + q2 u^2 v^2 + q0 v^4 >= 0 ?
    if q4 > 0 or q0 > 0: return True
    # both <= 0: s = u^2/v^2 >= 0, h(s) = q4 s^2 + q2 s + q0, max at s = -q2/(2 q4) if q2 > 0
    if q2 <= 0: return q4 == 0 or q0 == 0
    smax = -q2/(2*q4)
    return q4*smax*smax + q2*smax + q0 >= 0

def selmer_group(a, bcoef, label):
    """classes d | bcoef (squarefree, signed) with d w^2 = d^2 + a d z^2 + bcoef z^4 everywhere locally soluble.
    Divide by d: w'^2 = d z^4... use quartic q4 = d, q2 = a, q0 = bcoef/d (in u = z, v = 1 form)."""
    primes = sorted(factor(bcoef).keys())
    bad = sorted(set(primes) | set(factor(2*B*C).keys()))
    sel = []
    for signs in product([1, -1], *[[0, 1]]*len(primes)):
        d = signs[0]
        for pi, e in zip(primes, signs[1:]):
            if e: d *= pi
        q4, q2, q0 = d, a, bcoef // d
        ok = real_soluble(q4, q2, q0) and all(qp_soluble_quartic(q4, q2, q0, p) for p in bad)
        if ok: sel.append(d)
    print(f"{label}: candidate primes {primes}, bad places {bad}+inf; Selmer classes = {sel}; dim = {len(sel).bit_length()-1} (size {len(sel)})")
    return sel

if __name__ == "__main__":
    # sanity test on y^2 = x^3 - x (a=0, b=-1; E': y^2 = x^3 + 4x): known rank 0, Sel_2 = E[2] = (Z/2)^2, Sha[2]=0.
    # (I) d | -1 : {1,-1}; (II) d | 4: {1,-1,2,-2}. Expected sizes: (I) = {1,-1}? and (II) ... dim total - 2 = 0.
    print("--- control curve y^2 = x^3 - x ---")
    s1 = selmer_group(0, -1, "(I) d|b")
    s2 = selmer_group(0, 4, "(II) d|a^2-4b")
    print("rank bound =", (len(s1).bit_length()-1) + (len(s2).bit_length()-1) - 2)
    # control curve 2: y^2 = x^3 + x^2 - 2x? use X0(17)? Use y^2 = x^3 - 25x (rank 1, Sel_2 dim 3)
    print("--- control curve y^2 = x^3 - 25x (congruent number 5, rank 1) ---")
    s1 = selmer_group(0, -25, "(I) d|b")
    s2 = selmer_group(0, 100, "(II) d|a^2-4b")
    print("rank bound =", (len(s1).bit_length()-1) + (len(s2).bit_length()-1) - 2)
    print("--- E^{-7}: y^2 = x^3 + %d x^2 + %d x ---" % (A, B))
    print("B factor", factor(B), "A^2-4B =", C, factor(C))
    s1 = selmer_group(A, B, "(I) d|B")
    s2 = selmer_group(-2*A, C, "(II) d|A^2-4B")
    d1 = len(s1).bit_length()-1; d2 = len(s2).bit_length()-1
    print("dim Sel_2(E^{-7}) <= %d + %d - 1 = %d ; rank bound = %d" % (d1, d2, d1+d2-1, d1+d2-2))
    print("--- E itself: y^2 = x^3 - 22735 x^2 + 106272484 x (rank 2, Sha[2]=0 recorded; expect bound dim Sel_2 = 3) ---")
    a0, b0 = -22735, 106272484
    s1 = selmer_group(a0, b0, "(I) d|b")
    s2 = selmer_group(-2*a0, a0*a0-4*b0, "(II) d|a^2-4b")
    d1 = len(s1).bit_length()-1; d2 = len(s2).bit_length()-1
    print("dim Sel_2(E) <= %d + %d - 1 = %d ; rank bound = %d" % (d1, d2, d1+d2-1, d1+d2-2))
