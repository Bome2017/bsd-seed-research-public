#!/usr/bin/env python3
"""Validation comparator for the rigorous core.  Every check is exact rational/decimal arithmetic on the rigorous printed balls
(arb_get_str output encloses the ball).  Prints one line per check and a final VALIDATION_PASS/FAIL."""
import re, glob, os, sys, hashlib
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 80
R = os.path.expanduser('~/BSD_RIGOROUS_STREAM_CORE_2026-09-19'); os.chdir(R + '/validation')
ball_re = re.compile(r'\[([-+0-9.e]+)? ?\+/- ([0-9.e+-]+)\]')
def ball(s):
    m = ball_re.search(s); mid = F(Decimal(m.group(1))) if m.group(1) else F(0); return mid, F(Decimal(m.group(2)))
def contains(b, v): return abs(v - b[0]) <= b[1]
def overlaps(a, b): return abs(a[0] - b[0]) <= a[1] + b[1]
fails = 0; checks = 0
def check(ok, msg):
    global fails, checks; checks += 1
    if not ok: fails += 1
    print(('PASS ' if ok else 'FAIL ') + msg)
# references
sym = {}
for fn in ['ref/sage_symbols_output.txt', 'ref/sage_234446_output.txt']:
    if not os.path.exists(fn): continue
    for l in open(fn):
        p = l.split()
        if p and p[0] == 'SYM': sym[(p[1], int(p[2]), int(p[3]), int(p[4]))] = F(p[5])
lp5 = {}  # LP5 Sage/eclib [b/25]^+ list for 234446a1 (fallback)
v = [-5, 8, 8, -7, 0, -5, 6, 6, -8, 0, -7, 4, 4, -7, 0, -8, 6, 6, -5, 0, -7, 8, 8, -5]
for b in range(1, 25):
    if b % 5: lp5[('234446a1', 1, 25, b)] = F(v[b - 1])
lp5[('234446a1', 1, 27, 1)] = F(0); lp5[('234446a1', 1, 27, 2)] = F(0); lp5[('234446a1', 1, 7, 1)] = F(0); lp5[('234446a1', 1, 7, 2)] = F(0)
lp5[('234446a1', -1, 7, 1)] = F(1)   # Wuthrich 2018 (published), confirmed by LP5
per = {}; l2ref = {}
for l in open('ref/pari_ref_output.txt'):
    p = l.split()
    if p[0] == 'PER': per[p[1]] = (F(Decimal(p[11])), abs(F(Decimal(p[13]))))
    if p[0] == 'L2HALF':
        s = p[2]; e = 0
        if len(p) > 3 and p[3].startswith('E'): e = int(p[3][1:])
        l2ref[p[1]] = F(Decimal(s)) * F(10) ** e
curves = {}
for l in open('curves.txt'):
    if l.startswith('#'): continue
    lab, ai, N, M, ms, s = l.strip().split('|'); curves[lab] = (ai, int(N), int(M), [int(x) for x in ms.split()], int(s))
def segroot(verlog):
    ds = [bytes.fromhex(l.split()[-1]) for l in open(verlog) if l.startswith('SEG ')]
    return hashlib.sha256(b''.join(ds)).hexdigest()
def parse(fn):
    out = {'S': {}, 'XB': {}}
    for l in open(fn):
        p = l.split()
        if not p: continue
        if p[0] in ('AP_SEGROOT_SHA256', 'AN_MERKLE_SHA256', 'SMOOTH_MERKLE_SHA256'): out[p[0]] = p[1]
        elif p[0] == 'S': out['S'][int(p[1])] = ball(l)
        elif p[0] in ('OMEGA_PLUS', 'OMEGA_MINUS'): out[p[0]] = ball(l)
        elif p[0] == 'COUNT': out['COUNT'] = l.strip()
        elif p[0] == 'XB':
            b = int(p[1]); i = l.index(' minus ')
            out['XB'][b] = (ball(l[:i]), ball(l[i:]), ' contains 1 unique 1 minus' in l, l.rstrip().endswith('contains 1 unique 1'))
        elif p[0] in ('L2HALF_BALL',): out['L2'] = ball(l)
        elif p[0] == 'ZERO_EXCLUDED': out['ZX'] = int(p[1])
    return out
nsym = 0
for lab, (ai, N, M, ms, s) in curves.items():
    d = [x for x in glob.glob(f'{R}/runs/val/{lab}_T*') if os.path.exists(x + '/ms_m%d.txt' % ms[0])][0]
    an_root = open(d + '/an.log').read().split()[1]; sroot = segroot(d + '/ver.log')
    for m in ms:
        o = parse(f'{d}/ms_m{m}.txt'); ol = parse(f'{d}/msl_m{m}.txt'); tag = f'{lab} m={m}'
        check(o['AN_MERKLE_SHA256'] == an_root, f'{tag} ms a_n Merkle root == wverify an ({an_root[:16]})')
        check(o['AP_SEGROOT_SHA256'] == sroot and ol['AP_SEGROOT_SHA256'] == sroot, f'{tag} ms+msl a_q segment root == verifier SEG lines ({sroot[:16]})')
        check('identity 1' in ol.get('COUNT', ''), f'{tag} msl count identity: {ol.get("COUNT", "missing")}')
        check(all(overlaps(o['S'][k], ol['S'][k]) for k in range(m)), f'{tag} ms and msl class sums S_k overlap for all {m} classes')
        om = per[lab]
        check(contains(o['OMEGA_PLUS'], om[0]) and contains(o['OMEGA_MINUS'], om[1]), f'{tag} Omega+ / Omega- balls contain PARI omega1 / |Im omega2|')
        nb = 0; bad = []
        for b, (pb, mb, pdet, mdet) in o['XB'].items():
            pl, mi = ol['XB'][b][0], ol['XB'][b][1]
            if not (overlaps(pb, pl) and overlaps(mb, mi)): bad.append(f'b={b} ms/msl disjoint')
            for sg, bb in ((1, pb), (-1, mb)):
                key = (lab, sg, m, b); ref = sym.get(key, lp5.get(key))
                if ref is None: continue
                nb += 1
                if not (contains(bb, ref) and contains(ol['XB'][b][0 if sg == 1 else 1], ref)): bad.append(f'b={b} sign={sg} ref={ref} ball={float(bb[0]):.6g}+-{float(bb[1]):.1e}')
        nsym += nb
        check(not bad and nb > 0, f'{tag} (s={s:+d}) {nb} exact symbols [b/{m}]^+- each contained in the ms AND msl balls' + ('' if not bad else ' :: ' + '; '.join(bad[:4])))
for lab in ['389a1', '446d1', '234446a1']:
    fn = glob.glob(f'{R}/runs/val/{lab}_T*/l2.txt')[0]; o = parse(fn); d = os.path.dirname(fn)
    check(o['AN_MERKLE_SHA256'] == open(d + '/an.log').read().split()[1], f'{lab} l2 a_n Merkle root == wverify an')
    ref = l2ref[lab]
    if lab == '234446a1': check(contains(o['L2'], F(0)) and o['ZX'] == 0, f'{lab} (rank 4) L2HALF ball contains 0 (negative control); PARI value {float(ref):.3e}')
    else: check(contains(o['L2'], ref) and o['ZX'] == 1, f'{lab} (rank 2) L2HALF ball {float(o["L2"][0]):.18f} +- {float(o["L2"][1]):.2e} contains PARI {float(ref):.18f}; zero excluded')
print(f'SYMBOLS_COMPARED {nsym}')
print(f'VALIDATION_{"PASS" if fails == 0 else "FAIL"} checks={checks} fails={fails}')
