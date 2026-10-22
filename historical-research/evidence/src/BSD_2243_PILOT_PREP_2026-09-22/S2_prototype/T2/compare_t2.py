#!/usr/bin/env python3
"""T2 comparator: new-engine symbols vs the certified SYMBOLS files; class sums vs certified msl S_k balls; a_{4,2}."""
import re
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 80
R = '/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run'
ball_re = re.compile(r'\[([-+0-9.e]+)? ?\+/- ([0-9.e+-]+)\]')
def ball(s):
    m = ball_re.search(s); return (F(Decimal(m.group(1))) if m.group(1) else F(0), F(Decimal(m.group(2))))
fails = checks = 0
def check(ok, msg):
    global fails, checks; checks += 1; fails += (not ok); print(('PASS ' if ok else 'FAIL ') + msg)
for m in (27, 81):
    cert = {}
    for l in open(f'{R}/SYMBOLS_m{m}.txt'):
        if l.startswith('#') or not l.strip(): continue
        b, pl, mi = l.split(); cert[int(b)] = (int(pl), int(mi))
    Sc = {}
    for l in open(f'{R}/msl_m{m}.txt'):
        if l.startswith('S '): Sc[int(l.split()[1])] = ball(l)
    txt = open(f'T2/merge_m{m}.txt').read(); Sn = {}; xb = {}
    for l in txt.splitlines():
        if l.startswith('S '): Sn[int(l.split()[1])] = ball(l)
        if l.startswith('XB '):
            p = l.split(); b = int(p[1]); i = l.index(' minus ')
            candp = int(re.search(r'cand (-?\d+)/1024 contains (\d) unique (\d)', l[:i]).group(1)); okp = ' contains 1 unique 1 minus' in l
            candm = int(re.search(r'cand (-?\d+)/1024 contains (\d) unique (\d)', l[i:]).group(1)); okm = l.rstrip().endswith('contains 1 unique 1')
            xb[b] = (candp, okp, candm, okm)
    check('match 1' in txt and 'identity 1' in txt and 'missing 0' in txt, f'm={m} coverage, fingerprint and count identity')
    check(len(Sn) == m and all(abs(Sn[k][0] - Sc[k][0]) <= Sn[k][1] + Sc[k][1] for k in range(m)), f'm={m} all {m} class sums overlap the certified msl balls')
    good = all(xb[b][1] and xb[b][3] and xb[b][0] == 1024 * cert[b][0] and xb[b][2] == 1024 * cert[b][1] for b in cert)
    check(good and len(xb) == len(cert), f'm={m} all {len(cert)} (+/-) symbols identified and equal to the certified values ({2*len(cert)} numbers)')
    if m == 81:
        a = re.search(r'A_EXACT LATDEN\*a_\{n,r\} = (-?\d+)', txt)
        v = int(a.group(1)) if a else None
        check(v == 1024 * 15480, f'm=81 a_{{4,2}} (Lane 3 convention, alpha=-1): LATDEN*a = {v} == 1024*15480 -> a_{{4,2}} = {None if v is None else v/1024}')
print(f'T2_{"PASS" if fails == 0 else "FAIL"} checks={checks} fails={fails}')
