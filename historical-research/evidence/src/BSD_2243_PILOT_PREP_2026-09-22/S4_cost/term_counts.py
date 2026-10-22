#!/usr/bin/env python3
"""S4 input: exact-structure term and pair counts of the 2243 stream for a given T, from the VERIFIED a_q of segment 0.
  nz[m] = (a_m != 0) for m <= RT = isqrt(T), built multiplicatively from the verified a_p (p < 2^24): a_m = 0 iff 2 | m or
  4547 | m (additive, a_p = 0) or v_p(m) odd for a good p with a_p = 0 (a_{p^e} = 0 exactly then; a_p^2 = p or 2p impossible).
  Part L pairs  = sum_{m < RT} (pi(T/m) - pi(RT))    (n = m q, q prime > RT);   terms = the same over m with a_m != 0
                  (minus primes q with a_q = 0: density ~ q^{-1/2}, negligible and ignored).
  Part S n-count = T - pairs (checked against the smooth-count identity).  pi(x) ~ li(x) - li(sqrt x)/2 (relative error << 1e-5).
Checks: per-segment term counts of the measured S3 units are reproduced."""
import sys, math, numpy as np
from scipy.special import expi
AP = '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S3_bench/ap/ap_000000.bin'
def sieve(n):
    s = np.ones(n, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]: s[p * p::p] = False
    return np.nonzero(s)[0]
def li(x): x = np.asarray(x, dtype=float); return expi(np.log(x))
def pi_approx(x): x = np.asarray(x, dtype=float); return li(x) - 0.5 * li(np.sqrt(x))
def counts(T):
    RT = math.isqrt(T)
    pr = sieve(1 << 24); ap = np.fromfile(AP, dtype='<i4'); assert len(ap) == len(pr), (len(ap), len(pr))
    apd = dict(zip(pr[pr <= RT].tolist(), ap[:np.searchsorted(pr, RT, 'right')].tolist()))
    nz = np.ones(RT + 1, dtype=bool); nz[0] = False
    for p, a in apd.items():
        if a != 0: continue
        bad = p in (2, 3, 2243, 4547, 5843) and p in (2, 4547)          # additive primes of the seed: a_p = 0, all p^e
        if p in (2, 4547): nz[p::p] = False; continue
        pe, e = p, 1                                                       # good supersingular p: odd exponents vanish
        while pe <= RT:
            idx = np.arange(pe, RT + 1, pe); idx = idx[(idx // pe) % p != 0]
            if e % 2: nz[idx] = False
            pe *= p; e += 1
    ms = np.arange(1, RT + 1); lim = T // ms; keep = lim > RT
    base = pi_approx(RT)
    cnt = pi_approx(lim[keep].astype(float)) - base
    pairs = float(cnt.sum()); terms = float(cnt[nz[1:][keep]].sum())
    nprimes_L = float(pi_approx(T) - base)
    return dict(T=T, RT=RT, pairs_L=pairs, terms_L=terms, primes_gt_RT=nprimes_L, primes_total=float(pi_approx(T)),
                smooth_S=T - pairs, nz_density_RT=float(nz[1:].mean()), N=lambda X: int(nz[1:X + 1].sum()))
if __name__ == '__main__':
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 39119887532031
    c = counts(T); N = c.pop('N')
    for k, v in c.items(): print(f"{k:14s} {v:.6e}" if isinstance(v, float) else f"{k:14s} {v}")
    print("N(X) for X = 1..4, 68, 98, 177:", [N(x) for x in (1, 2, 3, 4, 68, 98, 177)])
    # reproduce S3 unit term counts: terms = sum over primes q in the segment (> RT) of #{m in [m0, min(m1-1, T/q)] : a_m != 0}
    pr = sieve(1 << 24)
    for s, m0, m1, meas in ((0, 1, 178, 51887600), (59, 1, 69, 25907200)):
        lo, hi = s << 24, (s + 1) << 24
        if s == 0: qs = pr[pr > c['RT']]
        else:
            seg = np.ones(1 << 24, dtype=bool); ps = sieve(1 << 16)
            for p in ps:
                st = max(p * p, (lo + p - 1) // p * p); seg[st - lo::p] = False
            qs = lo + np.nonzero(seg)[0]
        tot = 0
        for q in qs.tolist():
            me = min(m1 - 1, T // q); tot += N(me) - N(m0 - 1) if me >= m0 else 0
        print(f"check seg {s} m[{m0},{m1}): model terms {tot}  measured {meas}  (a_q = 0 primes excluded in the measurement)")
