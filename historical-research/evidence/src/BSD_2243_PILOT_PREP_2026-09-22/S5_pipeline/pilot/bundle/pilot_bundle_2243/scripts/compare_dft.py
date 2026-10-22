#!/usr/bin/env python3
"""R2: compare a direct-sum merge and a DFT merge of the SAME checkpoints. Per symbol b (plus and minus): the lattice candidate,
the 'contains' flag and the 'unique' flag must be identical, and the two balls must overlap. A_EXACT / A_MOD_P lines must be
identical; the nonzero-only EXCLUDES flag must be identical. Exact rational arithmetic on the printed ball endpoints."""
import re, sys
from fractions import Fraction as Fr
BALL = re.compile(r'^\[([-+0-9.e]+) \+/- ([0-9.e+-]+)\]$')
ZERO = re.compile(r'^\[\+/- ([0-9.e+-]+)\]$')
def ball(s):
    m = BALL.match(s)
    if m: return Fr(m.group(1)), Fr(m.group(2))
    m = ZERO.match(s)
    if m: return Fr(0), Fr(m.group(1))                    # ball around 0 printed as [+/- r]
    return Fr(s), Fr(0)                                   # exact value printed without radius
def parse(fn):
    xb, other = {}, {}
    for L in open(fn):
        t = L.split()
        if not t: continue
        if t[0] == 'XB':
            # XB b plus <ball> cand h/L contains c unique u minus <ball> cand h/L contains c unique u ; ball may contain spaces
            m = re.match(r'XB (\d+) plus (\[.*?\]|\S+) cand (\S+) contains (\d) unique (\d) minus (\[.*?\]|\S+) cand (\S+) contains (\d) unique (\d)', L)
            b = int(m.group(1)); xb[b] = (m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), m.group(7), m.group(8), m.group(9))
        elif t[0] in ('A_EXACT', 'A_MOD_P', 'WEIGHTS'): other[t[0]] = L.strip()
        elif t[0] == 'NONZERO_ONLY': other['EXCL'] = t[-1]
    return xb, other
a, oa = parse(sys.argv[1]); b, ob = parse(sys.argv[2]); maxr = Fr(sys.argv[3]) if len(sys.argv) > 3 else None
ok = set(a) == set(b) and len(a) > 0; nover = 0; maxrat = Fr(0)
for k in a:
    x, y = a[k], b[k]
    if (x[1], x[2], x[3], x[5], x[6], x[7]) != (y[1], y[2], y[3], y[5], y[6], y[7]): ok = False; print('MISMATCH flags/cands b =', k, x, y)
    for i in (0, 4):
        (m1, r1), (m2, r2) = ball(x[i]), ball(y[i])
        if abs(m1 - m2) > r1 + r2: ok = False; print('NO OVERLAP b =', k, x[i], y[i])
        else: nover += 1
        if r1 > 0: maxrat = max(maxrat, r2 / r1)
if oa != ob: ok = False; print('certificate lines differ:', oa, ob)
if maxr is not None and maxrat > maxr: ok = False; print(f'radius ratio {float(maxrat)} exceeds {float(maxr)}')
print(f"CMP {'PASS' if ok else 'FAIL'}: {len(a)} symbols, {nover} ball pairs overlap, identical candidates/flags; max radius ratio second/first = {float(maxrat):.4f}; {sorted(oa)}")
