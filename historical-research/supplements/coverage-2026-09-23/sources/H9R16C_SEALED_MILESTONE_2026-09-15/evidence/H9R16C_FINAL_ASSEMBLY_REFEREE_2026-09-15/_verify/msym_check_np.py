#!/usr/bin/env python3
"""numpy-accelerated matrix arithmetic for msym_check.py (same operators, same checks)."""
import sys, numpy as np
import msym_check as M

def mmul(A, B, ell):
    A = np.asarray(A, dtype=np.int64); B = np.asarray(B, dtype=np.int64)
    return (A @ B) % ell          # entries < ell ~ 1e6, dims <= 2000: products < 2e15 < 2^63
def madd(A, B, ell, cb=1):
    return (np.asarray(A, dtype=np.int64) + cb * np.asarray(B, dtype=np.int64)) % ell
def mscale(A, c, ell):
    return (c * np.asarray(A, dtype=np.int64)) % ell
def is_zero(A):
    return not np.any(np.asarray(A) % 1 != 0) and not np.any(np.asarray(A))
def identity(n):
    return np.eye(n, dtype=np.int64)
def rank_mod(A, ell):
    A = np.array(A, dtype=np.int64) % ell; rows, cols = A.shape; r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]: piv = i; break
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), ell - 2, ell)
        A[r] = (A[r] * inv) % ell
        nz = np.nonzero(A[:, c])[0]
        for i in nz:
            if i != r:
                A[i] = (A[i] - A[i, c] * A[r]) % ell
        r += 1
    return r
M.mmul, M.madd, M.mscale, M.is_zero, M.identity, M.rank_mod = mmul, madd, mscale, is_zero, identity, rank_mod
if __name__ == "__main__":
    cases = [tuple(int(x) for x in arg.split(",")) for arg in sys.argv[1:]]
    allok = True
    for (Ng, p, r) in cases:
        for ell in (1000003, 999983):
            res = M.run_case(Ng, p, r, ell)
            allok &= all(res.values())
    print("ALL PASS" if allok else "SOME FAIL")
