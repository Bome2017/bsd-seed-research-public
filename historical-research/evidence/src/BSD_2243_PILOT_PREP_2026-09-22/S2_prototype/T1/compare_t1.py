#!/usr/bin/env python3
import re
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 80
S1 = '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S1a_sign'
ball_re = re.compile(r'\[([-+0-9.e]+)? ?\+/- ([0-9.e+-]+)\]')
def ball(s):
    m = ball_re.search(s); return (F(Decimal(m.group(1))) if m.group(1) else F(0), F(Decimal(m.group(2))))
sym = {}
for l in open(S1 + '/ref_output.txt'):
    p = l.split()
    if p and p[0] == 'SYM': sym[(p[1], int(p[2]), int(p[3]), int(p[4]))] = F(p[5])
fails = checks = nsym = 0
for l in open(S1 + '/curves_s1a.txt'):
    if l.startswith('#'): continue
    lab, ai, N, M, aM, w = l.strip().split('|'); M = int(M)
    for m in (M*M, M**3):
        txt = open(f'T1/{lab}_m{m}.merge.txt').read(); bad = []; nb = 0
        ok_meta = 'match 1' in txt and 'identity 1' in txt and 'missing 0' in txt
        for line in txt.splitlines():
            if not line.startswith('XB '): continue
            b = int(line.split()[1]); i = line.index(' minus '); pl, mi = ball(line[:i]), ball(line[i:])
            for sg, bb in ((1, pl), (-1, mi)):
                ref = sym[(lab, sg, m, b)]; nb += 1
                if abs(ref - bb[0]) > bb[1]: bad.append((b, sg))
        checks += 1; ok = ok_meta and not bad and nb > 0; fails += not ok; nsym += nb
        print(('PASS ' if ok else 'FAIL ') + f'{lab} m={m}: {nb} exact symbols contained in new-engine balls; coverage/fingerprint/count ok={ok_meta}' + ('' if ok else f' bad={bad[:4]}'))
print(f'SYMBOLS_COMPARED {nsym}')
print(f'T1_{"PASS" if fails == 0 else "FAIL"} checks={checks} fails={fails}')
