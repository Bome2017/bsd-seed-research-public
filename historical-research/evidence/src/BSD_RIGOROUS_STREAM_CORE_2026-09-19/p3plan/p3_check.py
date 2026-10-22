#!/usr/bin/env python3
"""Stage C of run_p3.sh: consistency checks + exact symbol extraction.  usage: p3_check.py OUT SEGQ LATDEN ZERO_SYMBOL
Checks (all must pass): (1) each msl output's a_q segment root == SHA-256 over the verifier's per-segment ap_sha256 (same segments);
(2) count identity #smooth + #pairs = T; (3) every plus AND minus symbol identified (ball contains exactly one point of (1/LATDEN)Z);
(4) Hecke relations between targets m = p m':  a_p [b/m'] = sum_{j<p} [(b + m' j)/m]  (+ [0] if p does not divide N), both signs,
    with a_p read from the VERIFIED a_q file ap_000000.bin.  Writes OUT/SYMBOLS_m<m>.txt (b, [b/m]^+, [b/m]^- as exact fractions)."""
import sys, os, re, hashlib, struct
from fractions import Fraction as F
from math import gcd
OUT, SEGQ, LAT, ZERO = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), F(sys.argv[4])
fails = []
def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok: fails.append(msg)
targets = [tuple(int(x) for x in l.split()) for l in open(f'{OUT}/targets.txt')]   # m M s Q tmin T
seg = {}
for fn in os.listdir(f'{OUT}/logs'):
    if fn.startswith('ver_') and fn.endswith('.log'):
        for l in open(f'{OUT}/logs/{fn}'):
            p = l.split()
            if p and p[0] == 'SEG': seg[int(p[1])] = bytes.fromhex(p[-1])
# verified a_p for small primes (segment 0 lists one int32 per prime in increasing order)
raw = open(f'{OUT}/ap/ap_000000.bin', 'rb').read(4 * 200); vals = struct.unpack('<%di' % (len(raw) // 4), raw)
primes = [q for q in range(2, 2000) if all(q % d for d in range(2, int(q ** 0.5) + 1))][:len(vals)]; AP = dict(zip(primes, vals))
sym = {}
for (m, M, s, Q, tmin, T) in targets:
    fn = f'{OUT}/msl_m{m}.txt'; txt = open(fn).read()
    k = (T + 1) // SEGQ; root = hashlib.sha256(b''.join(seg[i] for i in range(k))).hexdigest()
    got = re.search(r'AP_SEGROOT_SHA256 (\w+) segments (\d+)', txt)
    check(got and got.group(1) == root and int(got.group(2)) == k, f'm={m}: a_q segment root over {k} verified segments = {root[:16]}')
    check('identity 1' in txt, f'm={m}: count identity ' + (re.search(r'COUNT .*', txt).group(0) if 'COUNT' in txt else 'missing'))
    plus, minus, nb, bad = {}, {}, 0, []
    for l in txt.splitlines():
        if not l.startswith('XB '): continue
        b = int(l.split()[1]); nb += 1
        mp = re.search(r'plus .*? cand (-?\d+)/(\d+) contains (\d) unique (\d) minus .*? cand (-?\d+)/(\d+) contains (\d) unique (\d)', l)
        hp, dp, cp, up, hm, dm, cm, um = mp.groups()
        if cp == '1' and up == '1' and int(dp) == LAT: plus[b] = F(int(hp), LAT)
        else: bad.append(f'plus b={b}')
        if cm == '1' and um == '1' and int(dm) == LAT: minus[b] = F(int(hm), LAT)
        else: bad.append(f'minus b={b}')
    phi = sum(1 for b in range(1, m) if gcd(b, m) == 1)
    check(nb == phi and not bad, f'm={m}: all {phi} plus and {phi} minus symbols identified in (1/{LAT})Z' + ('' if not bad else ' :: unidentified ' + ', '.join(bad[:6])))
    sym[m] = (M, plus, minus)
    with open(f'{OUT}/SYMBOLS_m{m}.txt', 'w') as f:
        f.write(f'# [b/{m}]^+ and [b/{m}]^- (exact, identified in (1/{LAT})Z; Q = {Q}, s = {s}, T = {T})\n')
        for b in sorted(plus): f.write(f'{b} {plus[b]} {minus.get(b)}\n')
# Hecke / U_p relations between targets
for m in sym:
    for mp in sym:
        if mp >= m or m % mp: continue
        p = m // mp
        if p < 2 or any(p % d == 0 for d in range(2, p)): continue
        M = sym[m][0]; ap = AP[p]; divides = (M % p == 0)
        n = 0; bad = []
        for sg, idx, z in ((1, 1, ZERO), (-1, 2, F(0))):
            for b in range(1, mp):
                if gcd(b, mp) != 1: continue
                if b not in sym[mp][idx] or any((b + mp * j) not in sym[m][idx] for j in range(p)): bad.append(f'missing b={b}'); continue
                lhs = ap * sym[mp][idx][b]; rhs = sum(sym[m][idx][b + mp * j] for j in range(p)) + (0 if divides else z); n += 1
                if lhs != rhs: bad.append(f'sign {sg} b={b}: {lhs} != {rhs}')
        kind = 'U_p (p | N)' if divides else 'T_p (p !| N, [0]^+ = %s)' % ZERO
        check(n > 0 and not bad, f'{kind} relation a_{p}[b/{mp}] = sum_j [(b+{mp}j)/{m}] (a_{p} = {ap} from the verified a_q file): {n} identities' + ('' if not bad else ' :: ' + '; '.join(bad[:4])))
print('P3_CHECK_' + ('PASS' if not fails else 'FAIL'), f'failures={len(fails)}')
sys.exit(1 if fails else 0)
