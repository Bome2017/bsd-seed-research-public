#!/usr/bin/env python3
"""S4: assemble rates.json ONLY from measured logs (S3 benchmark, S3b loaded-host test, feasibility measurements).
All times are single-thread user seconds on the idle host (Intel i9-10910, 10 cores / 20 threads) unless marked loaded."""
import json, re, glob, os
S3 = '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S3_bench'; F = '/Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22'
def user(fn): return float(re.search(r'^user\s+([0-9.]+)', open(fn).read(), re.M).group(1))
def seglog(fn):
    s = open(fn).read(); lo = int(re.search(r' lo (\d+)', s).group(1)); hi = int(re.search(r' hi (\d+)', s).group(1))
    n = int(re.search(r'(?:witnesses|primes) (\d+)', s).group(1)); return lo, hi, n, s
prod, ver = [], []
for seg in (0, 59, 5960, 596046):
    lo, hi, nw, _ = seglog(f'{S3}/logs/prod_{seg}.log'); u = user(f'{S3}/logs/prod_{seg}.time')
    _, _, npv, s = seglog(f'{S3}/logs/ver_{seg}.log'); npv = int(re.search(r'primes (\d+)', s).group(1)); v = user(f'{S3}/logs/ver_{seg}.time')
    qm = (lo + hi) / 2 if seg else 2 ** 23
    prod.append([qm, u / nw, seg, nw, u]); ver.append([qm, v / npv, seg, npv, v])
for seg, pl, pt, vl, vt in ((2331725, f'{F}/producer_variant/prod.log', f'{F}/producer_variant/prod.time', f'{F}/measure/ver_2331725.log', f'{F}/measure/ver_2331725.time'),
                            (10055539, f'{F}/producer_variant/prod2.log', f'{F}/producer_variant/prod2.time', f'{F}/measure/ver_10055539.log', f'{F}/measure/ver_10055539.time')):
    lo, hi, nw, _ = seglog(pl); u = user(pt); _, _, _, s = seglog(vl); npv = int(re.search(r'primes (\d+)', s).group(1)); v = user(vt)
    prod.append([(lo + hi) / 2, u / nw, seg, nw, u]); ver.append([(lo + hi) / 2, v / npv, seg, npv, v])
units = {}
for fn in glob.glob(f'{S3}/logs/unit*_p*.txt'):
    s = open(fn).read().strip(); lvl = int(fn[-5])
    if s.startswith('UNIT L'):
        m = re.search(r'seg (\d+) sub \S+ m \[(\d+),(\d+)\) pairs (\d+) terms (\d+) seconds ([0-9.]+)', s)
        key = f'L{m.group(1)}'; units.setdefault(key, {}).update({f'p{lvl}': float(m.group(6)), 'pairs': int(m.group(4)), 'terms': int(m.group(5)) if lvl == 2 else units.get(key, {}).get('terms', int(m.group(5)))})
    else:
        m = re.search(r'blk (\d+) smooth (\d+) terms (\d+) seconds ([0-9.]+)', s)
        key = f'S{m.group(1)}'; units.setdefault(key, {}).update({f'p{lvl}': float(m.group(4)), 'smooth': int(m.group(2))})
        if lvl == 2: units[key]['terms'] = int(m.group(3))
ck = re.search(r'CKPT_WRITE bytes (\d+) seconds ([0-9.]+)', open(f'{S3}/logs/ckpt_bench.txt').read())
dft = re.search(r'DFTBENCH m (\d+) seconds ([0-9.]+)', open(f'{S3}/logs/dftbench.txt').read())
conc = {}
for c in (10, 20):
    pu = [user(f) for f in glob.glob(f'{S3}/conc/logs/prod_c{c}_*.time')]; vu = [user(f) for f in glob.glob(f'{S3}/conc/logs/ver_c{c}_*.time')]
    conc[c] = {'producer_user_mean_s_per_top_segment': sum(pu) / len(pu), 'verifier_user_mean_s': sum(vu) / len(vu), 'n': len(pu)}
drv = open(f'{S3}/conc/s3b_driver.log').read()
for c in (10, 20): conc[c]['batch_wall_produce_s'] = int(re.search(rf'BATCH c {c} .*produce_wall (\d+)', drv).group(1)); conc[c]['batch_wall_verify_s'] = int(re.search(rf'BATCH c {c} .*verify_wall (\d+)', drv).group(1))
single_top = prod[4][4]; single_top_v = ver[4][4]
conc['factors'] = {'producer_throughput_per_core_10proc': single_top / conc[10]['producer_user_mean_s_per_top_segment'],
                   'producer_throughput_per_core_20proc_SMT': 2 * single_top / conc[20]['producer_user_mean_s_per_top_segment'],
                   'verifier_throughput_per_core_10proc': single_top_v / conc[10]['verifier_user_mean_s'],
                   'verifier_throughput_per_core_20proc_SMT': 2 * single_top_v / conc[20]['verifier_user_mean_s']}
out = {'host': 'Intel i9-10910 3.6 GHz (10C/20T), macOS, idle; single-thread user seconds', 'producer_points_q_s_per_prime': [p[:2] for p in prod],
       'producer_detail': prod, 'verifier_points_q_s_per_prime': [v[:2] for v in ver], 'verifier_detail': ver, 'units': units,
       'ckpt_write': {'bytes': int(ck.group(1)), 's': float(ck.group(2))}, 'dft': {'m': int(dft.group(1)), 's': float(dft.group(2))}, 'loaded_host': conc,
       'setup_s_per_process': 2.9}
json.dump(out, open('/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost/rates.json', 'w'), indent=1)
for p in prod: print(f"producer q~{p[0]:.3e}  {1e6 * p[1]:7.2f} us/prime  (seg {p[2]}, {p[3]} primes, {p[4]:.2f} s)")
for v in ver: print(f"verifier q~{v[0]:.3e}  {1e6 * v[1]:7.2f} us/prime")
for k in sorted(units, key=lambda x: (x[0], int(x[1:]))): print(k, units[k])
print('ckpt', out['ckpt_write'], 'dft', out['dft']); print('loaded', json.dumps(conc['factors']))
