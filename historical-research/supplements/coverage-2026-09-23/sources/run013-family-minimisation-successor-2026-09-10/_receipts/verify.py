#!/usr/bin/env python3
"""
Standalone re-verification of the computational claims attached to Proposition A.
Dependency-free (pure Python 3).  Run:  python3 verify.py

Curve E  = Cremona 62a1 :  v^2 + u v + v = u^3 - u^2 - u + 1
Curve E1 = descent model:  Y^2 = X^3 - 15 X^2 + 64 X
identified by X = 4(u+1), Y = 8v + 4u + 4.

NOTE (v2): v1 printed violations but always exited 0, so a clean exit was not an
arithmetic certificate.  This version accumulates failures and exits 1 if any check
fails.  Note also that C4 uses the very duplication identity under review, so it
corroborates the identity's consequences rather than validating the identity itself.
"""
FAILURES = []
def require(cond, msg):
    if not cond: FAILURES.append(msg)
    return cond

def is_prime(n):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def primes(lo, hi):
    return (n for n in range(lo, hi) if is_prime(n))

def leg(a, p):
    """Legendre symbol (a/p), p an odd prime."""
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def count_min(q):
    """#E(F_q) on the MINIMAL model, affine points + 1."""
    qr = bytearray(q)
    for t in range(1, (q+1)//2): qr[(t*t) % q] = 1
    n = 1
    for u in range(q):
        rhs = (u*u*u - u*u - u + 1) % q
        b   = (u + 1) % q
        d   = (b*b + 4*rhs) % q
        n += 1 if d == 0 else (2 if qr[d] else 0)
    return n

def count_E1(q):
    """#E1(F_q) on the descent model, affine points + 1."""
    qr = bytearray(q)
    for t in range(1, (q+1)//2): qr[(t*t) % q] = 1
    n = 1
    for x in range(q):
        r = (x*x*x - 15*x*x + 64*x) % q
        n += 1 if r == 0 else (2 if qr[r] else 0)
    return n

def v2(n):
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k

def dbl_x(x, y, q):
    """x(2P) via ((x^2 - b)/(2y))^2 with b = 64.  None if P is 2-torsion."""
    if y % q == 0: return None
    return pow((x*x - 64) * pow(2*y % q, q-2, q), 2, q)

print("=" * 74)
print("C1.  v2 = 2 on the argument's own hypotheses  (2/q) = -1 and (-31/q) = -1")
print("=" * 74)
LIM = 40000
buckets = {}
for q in primes(3, LIM):
    if q == 31: continue
    key = (leg(2, q), leg(-31, q))
    if key[1] == 0: continue
    k = v2(count_min(q))
    buckets.setdefault(key, {}).setdefault(k, 0)
    buckets[key][k] += 1
names = {(-1,-1): "(2/q)=-1, (-31/q)=-1   <- Proposition A's hypotheses",
         ( 1,-1): "(2/q)=+1, (-31/q)=-1   (2-Sylow cyclic, but 8 IS a square)",
         (-1, 1): "(2/q)=-1, (-31/q)=+1   (full rational 2-torsion)",
         ( 1, 1): "(2/q)=+1, (-31/q)=+1   (full rational 2-torsion)"}
for key in [(-1,-1), (1,-1), (-1,1), (1,1)]:
    d = buckets.get(key, {})
    print(f"\n  {names[key]}\n    n = {sum(d.values()):5d}   v2 distribution = {dict(sorted(d.items()))}")
print("\n  EXPECTED: row 1 is {2: n} exactly; rows 3-4 contain no k=2; row 2 contains k>2.")

print("\n" + "=" * 74)
print("C2.  F_62 itself:  q = 5 (mod 8) and (q/31) = -1")
print("=" * 74)
bad = []
n = 0
for q in primes(3, 60000):
    if q % 8 != 5 or leg(q, 31) != -1: continue
    n += 1
    c = count_min(q); a = q + 1 - c
    if v2(c) != 2 or a == 0: bad.append((q, c, a, v2(c)))
    if leg(-1, q) != 1 or leg(31, q) != leg(q, 31) or leg(-31, q) != -1:
        bad.append(("symbol identity", q))
print(f"  primes q < 60000 in the family : {n}")
print(f"  violations of v2 = 2, a_q != 0, or the symbol identities : {len(bad)}  {bad[:5]}")

print("\n" + "=" * 74)
print("C3.  Model transfer:  #E_minimal(F_q) == #E1(F_q)")
print("=" * 74)
mis = [q for q in primes(3, 6000)
       if q != 31 and leg(2, q) == -1 and leg(-31, q) == -1 and count_min(q) != count_E1(q)]
print(f"  mismatches below 6000 : {len(mis)}  {mis[:5]}")

print("\n" + "=" * 74)
print("C4.  Direct search for a halving of T = (8,8) on E1(F_q)")
print("=" * 74)
hits = []
m = 0
for q in primes(3, 3000):
    if q == 31 or leg(2, q) != -1 or leg(-31, q) != -1: continue
    m += 1
    for x in range(q):
        r = (x*x*x - 15*x*x + 64*x) % q
        if r != 0 and leg(r, q) != 1: continue
        for y in ([0] if r == 0 else [y for y in range(q) if y*y % q == r]):
            if dbl_x(x, y, q) == 8 % q:
                hits.append((q, x, y))
print(f"  primes searched : {m}")
print(f"  P in E1(F_q) with x(2P) = 8 : {len(hits)}  {hits[:5]}")

print("\n" + "=" * 74)
print("C5.  Relative density among the primes")
print("=" * 74)
for LIM in (10000, 40000, 200000):
    fam = sum(1 for q in primes(3, LIM) if q % 8 == 5 and leg(q, 31) == -1)
    pi  = sum(1 for _ in primes(2, LIM))
    print(f"  x = {LIM:7d}:  |F_62 <= x| = {fam:5d}   pi(x) = {pi:6d}   ratio = {fam/pi:.5f}")
print("  claimed limit: 15/phi(248) = 15/120 = 0.125")

print("\n" + "=" * 74)
require(all(k == 2 for k in buckets[(-1,-1)]), "C1: v2 != 2 on the hypothesis set")
require(2 not in buckets.get((-1,1),{}) and 2 not in buckets.get((1,1),{}), "C1: v2 == 2 with full 2-torsion")
require(any(k > 2 for k in buckets.get((1,-1),{})), "C1: control (2/q)=+1 showed no k>2")
require(not bad, "C2: violation in the family")
require(not mis, "C3: model-count mismatch")
require(not hits, "C4: a halving of T was found")
if FAILURES:
    print("FAIL")
    for f in FAILURES: print("  -", f)
    raise SystemExit(1)
print("ALL CHECKS PASSED")
raise SystemExit(0)
