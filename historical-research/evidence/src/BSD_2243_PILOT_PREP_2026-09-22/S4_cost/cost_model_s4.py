#!/usr/bin/env python3
"""S4 all-in cost model for the 2243 certificate stream, built ONLY from measured rates (rates.json) and exact-structure counts
(term_counts.py, from the verified a_q). Unit: single-thread core-hours of the measurement host (i9-10910, idle, turbo) =
"local core-hours" (lch). Components are reported separately, as requested:
  production (untrusted fast producer), verification (independent wverify), traversal (L: segment sieve + a_q read + SHA +
  pair loop; S: block a_n generation + SHA), kernel (Arb ball products), interval summation (exact fixed-point add + error
  tally + fingerprint), checkpointing (writes; restart loss shown separately), storage (GB, GB-months), merge + final DFT.
Three stopping points: per-symbol exact identification at T_min (the design), the nonzero-only scalar screen (best case),
exact scalar identification. Production/verification cost per prime is interpolated between measured heights (linear in
q^(1/4) resp. log q; flat below the lowest point); every other rate is a measured constant or a measured height profile."""
import json, math, sys
import numpy as np
sys.path.insert(0, '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost')
from term_counts import counts, pi_approx
import os
R = json.load(open(os.environ.get('RATES', '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost/rates.json')))   # RATES=<cloud rates> for the pilot projection
SEGQ, BLK, UT = 1 << 24, 1 << 22, 10 ** 9
def interp(points, x, tf):
    xs = [tf(q) for q, _ in points]; ys = [c for _, c in points]; t = tf(x)
    if t <= xs[0]: return ys[0]
    for i in range(1, len(xs)):
        if t <= xs[i]: return ys[i - 1] + (ys[i] - ys[i - 1]) * (t - xs[i - 1]) / (xs[i] - xs[i - 1])
    return ys[-1] + (ys[-1] - ys[-2]) * (t - xs[-1]) / (xs[-1] - xs[-2])       # linear extrapolation (not needed below 1.687e14)
def over_primes(fun, T, steps=6000):
    """sum_{p <= T} fun(p) via the prime-counting approximation on a geometric grid"""
    xs = np.geomspace(2.0, float(T), steps + 1); pc = pi_approx(xs); s = 0.0
    for i in range(steps): s += fun(math.sqrt(xs[i] * xs[i + 1])) * (pc[i + 1] - pc[i])
    return s
def sub_units(T):
    """number of L sub-units (production UNIT_TERMS = 1e9) with the engine's integer estimate; and the segments with > 1 sub-unit"""
    RT = math.isqrt(T); nseg = T // SEGQ + 1; extra = 0; multi = 0; ilog = lambda x: max(x.bit_length() - 1, 1)
    for s in range(nseg):
        lo = s * SEGQ; hi = min(lo + SEGQ, T + 1); qlo = max(lo, RT + 1)
        if qlo >= hi: continue
        mmax = T // qlo; est = 0
        for i in range(ilog(qlo), 64):
            a, b = 1 << i, (1 << (i + 1)) if i < 63 else (1 << 64) - 1; x0 = max(qlo, a); x1 = min(hi, b)
            if x0 >= hi: break
            if x0 >= x1: continue
            est += (T // a) * ((x1 - x0) // (i * 7 // 10 + 1))
        J = min(max((est + UT - 1) // UT, 1), mmax)
        if J == 1 and s > 16: return nseg, extra, multi, s                  # est decreases with s: J = 1 from here on
        extra += J - 1; multi += J > 1
    return nseg, extra, multi, nseg
def lsq(xs, ys):
    A = np.array(xs, dtype=float); y = np.array(ys, dtype=float); c, *_ = np.linalg.lstsq(A, y, rcond=None); return c
U = R['units']
# L: traversal t0 = a + b*pairs ; kernel (p1-p0) = kp*primes + kt*terms ; summation (p2-p1) = st*terms
Lk = [k for k in U if k[0] == 'L']
tr_a, tr_b = lsq([[1, U[k]['pairs']] for k in Lk], [U[k]['p0'] for k in Lk])
def primes_in_unit(k):
    seg = int(k[1:]); return {0: 649_000, 59: 809_619, 5960: 662_078, 596046: 560_910, 2331725: 536_236}[seg]  # seg 0: primes in (RT, 2^24)
kp, kt = lsq([[primes_in_unit(k), U[k]['terms']] for k in Lk], [U[k]['p1'] - U[k]['p0'] for k in Lk])
st = lsq([[U[k]['terms']] for k in Lk], [U[k]['p2'] - U[k]['p1'] for k in Lk])[0]
Sk = sorted([k for k in U if k[0] == 'S'], key=lambda k: int(k[1:]))
Sprof = {lvl: [((int(k[1:]) + 0.5) * BLK, U[k][lvl]) for k in Sk] for lvl in ('p0', 'p1', 'p2')}
def S_block_avg(T, lvl):                        # average over blocks of the measured profile, linear in log n
    nb = math.ceil(T / BLK); xs = np.geomspace(BLK, T, 400); w = np.diff(xs); mids = np.sqrt(xs[:-1] * xs[1:])
    return float(sum(interp(Sprof[lvl], x, math.log) * dw for x, dw in zip(mids, w)) / (T - BLK)), nb
def model(T, ckpt_secs=600.0, W=96, generations=10):
    c = counts(T); c.pop('N'); nseg, extra, multi, s_single = sub_units(T); nsub = nseg + extra
    prod = over_primes(lambda q: interp(R['producer_points_q_s_per_prime'], q, lambda x: x ** 0.25), T)
    ver = over_primes(lambda q: interp(R['verifier_points_q_s_per_prime'], q, math.log), T)
    s0, nb = S_block_avg(T, 'p0'); s1, _ = S_block_avg(T, 'p1'); s2, _ = S_block_avg(T, 'p2')
    comp = {'production': prod, 'verification': ver,
            'traversal_L': nsub * tr_a + tr_b * c['pairs_L'], 'traversal_S': nb * s0,
            'kernel_L': kp * c['primes_gt_RT'] + kt * c['terms_L'], 'kernel_S': nb * (s1 - s0),
            'summation_L': st * c['terms_L'], 'summation_S': nb * (s2 - s1)}
    work = sum(comp.values())
    comp['checkpoint_writes'] = work / ckpt_secs * R['ckpt_write']['s']
    comp['setup_per_process'] = W * generations * R['setup_s_per_process']
    ckpt_files = W * generations; merge = R['dft']['s'] + ckpt_files * 0.5 + 60.0            # DFT + reading/verifying checkpoints + symbol pass allowance
    comp['merge_and_dft'] = merge
    lch = {k: v / 3600 for k, v in comp.items()}
    # storage (GB): low segments pre-produced (several sub-units), checkpoints, logs, final artifacts; transient per worker
    primes_low = sum(SEGQ / math.log(max((s + 0.5) * SEGQ, 3)) for s in range(s_single))
    storage = {'pre_produced_low_segments_GB': 4 * primes_low / 1e9, 'checkpoints_GB': ckpt_files * R['ckpt_write']['bytes'] / 1e9,
               'stream_and_timing_logs_GB': 2 * nseg * 140 / 1e9, 'final_class_sums_and_symbols_GB': (R['ckpt_write']['bytes'] + 25 * 5028806) / 1e9,
               'transient_per_worker_MB': (27 * 540_000 + 4 * 540_000) / 1e6}
    return c, (nseg, extra, multi, s_single), lch, storage
if __name__ == '__main__':
    targets = [('per-symbol exact identification (T_run, the design)', 39119887532031),
               ('nonzero-only scalar screen, best case', int(5.7406e13)), ('exact scalar identification', int(6.7981e13))]
    print(f"fits: L traversal {tr_a:.3f} s/sub-unit + {tr_b * 1e9:.2f} ns/pair; L kernel {kp * 1e9:.0f} ns/prime + {kt * 1e9:.1f} ns/term; "
          f"L summation {st * 1e9:.1f} ns/term")
    out = {}
    for label, T in targets:
        c, su, lch, sto = model(T); tot = sum(lch.values())
        print(f"\n== {label}: T = {T:.4e}  primes {c['primes_total']:.4e}  L pairs {c['pairs_L']:.4e}  L terms {c['terms_L']:.4e}  S blocks {math.ceil(T / BLK)}")
        print(f"   L sub-units {su[0] + su[1]} (segments {su[0]}, extra sub-units {su[1]} in {su[2]} low segments; single-unit from segment {su[3]})")
        for k, v in lch.items(): print(f"   {k:20s} {v:12.1f} lch  ({100 * v / tot:6.3f}%)")
        print(f"   {'TOTAL':20s} {tot:12.1f} lch")
        print("   storage:", ", ".join(f"{k} {v:.1f}" for k, v in sto.items()))
        out[label] = {'T': T, 'counts': {k: v for k, v in c.items()}, 'components_lch': lch, 'total_lch': tot, 'storage': sto}
    json.dump(out, open(os.environ.get('COST_OUT', '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost/cost_s4.json'), 'w'), indent=1, default=float)
