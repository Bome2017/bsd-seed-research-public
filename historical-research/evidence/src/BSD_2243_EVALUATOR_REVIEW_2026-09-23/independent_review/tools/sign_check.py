#!/usr/bin/env python3
"""reviewer: engine XB balls (any sign) vs an mpmath evaluation of the truncated formula from the exact merged class sums.
usage: sign_check.py CKPT_DIR M Q SIGN MERGE_OUT"""
import os, re, sys, mpmath as mp
mp.mp.dps = 60
d, M, Q, S, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
tot = [0] * M
for f in os.listdir(d):
    if f.startswith('ckpt_g') and f.endswith('.bin') and '.tmp' not in f:
        b = open(os.path.join(d, f), 'rb').read()[:-70]; arr = b[-16 * M:]
        for k in range(M): tot[k] += int.from_bytes(arr[16 * k:16 * k + 16], 'little', signed=True)
Sk = [mp.mpf(t) / mp.mpf(2) ** 96 for t in tot]
b2, b4, b6 = 4 * -22735, 2 * 106272484, 0
e1, e2, e3 = sorted([mp.re(r) for r in mp.polyroots([4, b2, 2 * b4, b6], maxsteps=200, extraprec=200)], reverse=True)
omp = mp.pi / mp.agm(mp.sqrt(e1 - e3), mp.sqrt(e1 - e2)); omm = mp.pi / mp.agm(mp.sqrt(e1 - e3), mp.sqrt(e2 - e3))
bad = n = 0; worst = 0
for l in open(out):
    m = re.match(r'XB (\d+) plus \[([-+0-9.e]*) ?\+/- ([0-9.e+-]+)\] cand \S+ contains \d unique \d minus \[([-+0-9.e]*) ?\+/- ([0-9.e+-]+)\]', l)
    if not m: continue
    b = int(m.group(1)); ub = pow(Q * b % M, -1, M)
    xp = sum(Sk[k] * (mp.cos(2 * mp.pi * (k * b % M) / M) + S * mp.cos(2 * mp.pi * (k * ub % M) / M)) for k in range(M)) / omp
    xm = sum(Sk[k] * (mp.sin(2 * mp.pi * (k * b % M) / M) - S * mp.sin(2 * mp.pi * (k * ub % M) / M)) for k in range(M)) / omm
    pm, pr, qm, qr = mp.mpf(m.group(2) or 0), mp.mpf(m.group(3)), mp.mpf(m.group(4) or 0), mp.mpf(m.group(5))
    n += 2; bad += (abs(xp - pm) > pr) + (abs(xm - qm) > qr); worst = max(worst, abs(xp - pm) / pr, abs(xm - qm) / qr)
print(f'sign {S}: {n - bad} of {n} engine symbol balls contain the reviewer mpmath value (max |diff|/radius = {mp.nstr(worst, 4)})')
sys.exit(1 if bad else 0)
