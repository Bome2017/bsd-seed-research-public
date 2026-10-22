#!/usr/bin/env python3
"""parse_cloud_rates.py <results dir> -- turn the pilot's logs into (1) a rates file in the S4 schema, measured on the cloud
machine UNDER FULL LOAD (one producer/verifier per core), (2) the per-height speed ratio f = local single-thread time /
cloud loaded time per prime, (3) the S4 cost model re-run with the cloud rates, and (4) the directly measured $ per fully
verified, accumulated chunk (P4). Nothing here is extrapolated beyond the measured heights except the model's own
interpolation (S4); the run's top height 3.912e13 is measured directly."""
import json, os, re, subprocess, sys, statistics as st
RD = sys.argv[1]; S4 = '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost'; LOCAL = json.load(open(f'{S4}/rates.json'))
def stream_rows(fn):
    out = []
    for L in open(fn):
        m = re.search(r'STREAM seg (\d+) prod_user ([0-9.]+) ver_user ([0-9.]+) primes (\d+)', L)
        if m: out.append((int(m.group(1)), float(m.group(2)), float(m.group(3)), int(m.group(4))))
    return out
prod, ver, ratio = [], [], []
for tag, f in (('seg0', 'pre_m27_stream.txt'), ('e9', 'p2_e9_stream.txt'), ('e11', 'p2_e11_stream.txt'), ('e13', 'p2_e13_stream.txt'), ('top', 'p2_top_stream.txt')):
    fn = os.path.join(RD, f)
    if not os.path.exists(fn): continue
    rows = [r for r in stream_rows(fn) if tag != 'seg0' or r[0] == 0]
    if not rows: continue
    q = st.mean(r[0] for r in rows) * 2 ** 24 + 2 ** 23
    pp = st.mean(r[1] / r[3] for r in rows); vv = st.mean(r[2] / r[3] for r in rows)
    prod.append([q, pp]); ver.append([q, vv])
    lp = min(LOCAL['producer_points_q_s_per_prime'], key=lambda x: abs(x[0] / q - 1)); lv = min(LOCAL['verifier_points_q_s_per_prime'], key=lambda x: abs(x[0] / q - 1))
    ratio.append((tag, q, len(rows), 1e6 * pp, 1e6 * lp[1], lp[1] / pp, 1e6 * vv, lv[1] / vv, st.pstdev(r[1] / r[3] for r in rows) / pp))
print("height  q          segments  cloud_prod_us  local_prod_us  f_prod  cloud_ver_us  f_ver  prod_spread")
for t in ratio: print(f"{t[0]:6s} {t[1]:.3e} {t[2]:8d} {t[3]:13.2f} {t[4]:13.2f} {t[5]:7.3f} {t[6]:12.2f} {t[7]:6.3f} {100 * t[8]:6.2f}%")
cloud = dict(LOCAL); cloud['host'] = 'cloud pilot, loaded (one process per core)'
cloud['producer_points_q_s_per_prime'] = sorted(prod); cloud['verifier_points_q_s_per_prime'] = sorted(ver)
units = {}
for L in open(os.path.join(RD, 'p2_units_single.txt')):
    lvl = int(L[1]); s = L[3:]
    m = re.search(r'UNIT L seg (\d+) .* pairs (\d+) terms (\d+) seconds ([0-9.]+)', s)
    if m: k = f'L{m.group(1)}'; units.setdefault(k, {}).update({f'p{lvl}': float(m.group(4)), 'pairs': int(m.group(2))}); units[k]['terms'] = int(m.group(3)) if lvl == 2 else units[k].get('terms', int(m.group(3)))
    m = re.search(r'UNIT S blk (\d+) smooth (\d+) terms (\d+) seconds ([0-9.]+)', s)
    if m: k = f'S{m.group(1)}'; units.setdefault(k, {}).update({f'p{lvl}': float(m.group(4)), 'smooth': int(m.group(2))})
if len(units) == len(LOCAL['units']): cloud['units'] = units
ck = re.search(r'CKPT_WRITE bytes (\d+) seconds ([0-9.]+)', open(os.path.join(RD, 'p2_ckpt.txt')).read()); cloud['ckpt_write'] = {'bytes': int(ck.group(1)), 's': float(ck.group(2))}
dft = re.search(r'DFTBENCH m (\d+) seconds ([0-9.]+)', open(os.path.join(RD, 'p2_dft.txt')).read()); cloud['dft'] = {'m': int(dft.group(1)), 's': float(dft.group(2))}
json.dump(cloud, open(os.path.join(RD, 'rates_cloud.json'), 'w'), indent=1)
env = dict(os.environ, RATES=os.path.join(RD, 'rates_cloud.json'), COST_OUT=os.path.join(RD, 'cost_cloud.json'))
print(subprocess.run([sys.executable, f'{S4}/cost_model_s4.py'], env=env, capture_output=True, text=True).stdout)
price = float(re.search(r'price_per_hour_usd ([0-9.]+)', open(os.path.join(RD, 'machine.txt')).read()).group(1))
nproc = int(re.search(r'nproc (\d+)', open(os.path.join(RD, 'machine.txt')).read()).group(1))
cc = json.load(open(os.path.join(RD, 'cost_cloud.json')))
for label, d in cc.items():
    core_h = d['total_lch']; print(f"CLOUD PROJECTION {label}: {core_h:.0f} cloud core-h = {core_h / nproc:.0f} instance-h of this type = ${core_h / nproc * price:,.0f} at ${price}/h (+ ops 1-6%, storage ~$25, merge ~$7)")
for L in open(os.path.join(RD, 'pilot.log')):
    if 'RESULT' in L or 'MIX' in L or 'killed' in L: print(L.strip())
