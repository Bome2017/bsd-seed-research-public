#!/usr/bin/env python3
"""S1a comparator: exact eclib symbols vs engine balls (exact rational arithmetic on printed Arb balls)."""
import re, glob, hashlib
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 80
ball_re = re.compile(r'\[([-+0-9.e]+)? ?\+/- ([0-9.e+-]+)\]')
def ball(s):
    m = ball_re.search(s); return (F(Decimal(m.group(1))) if m.group(1) else F(0), F(Decimal(m.group(2))))
def contains(b, v): return abs(v - b[0]) <= b[1]
sym = {}
for l in open('ref_output.txt'):
    p = l.split()
    if p and p[0] == 'SYM': sym[(p[1], int(p[2]), int(p[3]), int(p[4]))] = F(p[5])
def parse(fn):
    xb, count, root = {}, '', ''
    for l in open(fn):
        p = l.split()
        if not p: continue
        if p[0] == 'XB':
            i = l.index(' minus '); xb[int(p[1])] = (ball(l[:i]), ball(l[i:]))
        elif p[0] == 'COUNT': count = l.strip()
        elif p[0] == 'AP_SEGROOT_SHA256': root = p[1]
    return xb, count, root
def segroot(verlog):
    ds = [bytes.fromhex(l.split()[-1]) for l in open(verlog) if l.startswith('SEG ')]
    return hashlib.sha256(b''.join(ds)).hexdigest()
fails = checks = nsym = 0; control_rejects = 0; control_total = 0
for l in open('curves_s1a.txt'):
    if l.startswith('#'): continue
    lab, ai, N, M, aM, w = l.strip().split('|'); M, aM, w = int(M), int(aM), int(w); s = -w * aM
    d = glob.glob(f'runs/{lab}_T*')[0]; sroot = segroot(d + '/ver.log')
    for m in (M, M*M, M**3):
        for sg in (s, -s):
            xb, count, root = parse(f'{d}/msl_m{m}_s{sg}.txt')
            bad = []; nb = 0
            for b, (pl, mi) in xb.items():
                for sign, bb in ((1, pl), (-1, mi)):
                    ref = sym[(lab, sign, m, b)]; nb += 1
                    if not contains(bb, ref): bad.append((b, sign))
            if sg == s:
                checks += 1; ok = (not bad) and nb > 0 and 'identity 1' in count and root == sroot
                fails += (not ok); nsym += nb
                print(('PASS ' if ok else 'FAIL ') + f'{lab} M={M} aM={aM:+d} w={w:+d} m={m} s_pred={s:+d}: {nb} exact symbols contained; count identity; a_q root == verifier' + ('' if ok else f' :: bad={bad[:4]} count={count[:40]}'))
            else:
                control_total += 1; rejected = len(bad) > 0; control_rejects += rejected
                print(('CTRL-REJECTS ' if rejected else 'CTRL-NO-REJECT ') + f'{lab} m={m} wrong sign {sg:+d}: {len(bad)}/{nb} symbols excluded')
print(f'SYMBOLS_COMPARED {nsym}  CONTROLS_REJECTING {control_rejects}/{control_total}')
print(f'S1A_{"PASS" if fails == 0 else "FAIL"} checks={checks} fails={fails}')
