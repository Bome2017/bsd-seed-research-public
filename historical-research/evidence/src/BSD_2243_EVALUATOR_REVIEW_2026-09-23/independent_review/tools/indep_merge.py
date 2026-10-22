#!/usr/bin/env python3
"""Reviewer's INDEPENDENT merge + comparator (exact rationals; written from the checkpoint format read in acc2243v2.c,
not from the author's comparators).

usage: indep_merge.py CKPT_DIR M T Q SIGN CERT_MSL CERT_SYMBOLS ENGINE_MERGE_OUT [ENGINE_MERGE_OUT2 ...]

1. reads every ckpt_g*.bin (not .tmp) in CKPT_DIR: verifies the SHA-256 trailer, parses header / U records / ERR / ACC /
   i128 array; sums the arrays exactly (Python ints); checks unit coverage (each unit exactly once, units = 0..N-1 with N
   taken from the engine's RUN/MERGE line), fingerprint identity with an own splitmix64, count identity smooth + pairs = T.
2. recomputes CHUNK_DIGEST from the exact sums and compares with the engine's line(s).
3. compares the exact class sums tot_k 2^-96 with the certified arbcore balls (SDUMP lines, exact): |diff| <= E + rad_cert,
   and the engine's printed S_k balls with the certified printed balls (decimal overlap).
4. compares every XB line of each engine merge output with the certified SYMBOLS file (exact Fractions), including the
   contains/unique flags, and checks that the printed ball contains the certified value.
5. independent (non-rigorous, 80-digit mpmath) re-derivation of every symbol from the exact class sums with the direct formula
   Re/Im lambda(b/m) = sum_k S_k (cos 2pi kb/m + s cos 2pi k u_b/m), sum_k S_k (sin 2pi kb/m - s sin 2pi k u_b/m),
   u_b = (Q b)^-1 mod m, Omega+- by AGM; reports max |x_b(trunc) - x_b(cert)| against the (2 tail + 2E)/Omega budget.
"""
import sys, os, re, hashlib, struct, glob
from fractions import Fraction as F
from decimal import Decimal
import mpmath as mp

mp.mp.dps = 80
ckdir, M, T, Q, SIGN, cert_msl, cert_sym = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], sys.argv[7]
engine_outs = sys.argv[8:]
FB = 96
fails = []
def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok: fails.append(msg)

MASK64 = (1 << 64) - 1
def splitmix64(x):
    x = (x + 0x9E3779B97F4A7C15) & MASK64
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & MASK64
    return x ^ (x >> 31)

# ---------------- 1. checkpoints ----------------
names = sorted(f for f in os.listdir(ckdir) if f.startswith('ckpt_g') and '.bin' in f and '.tmp' not in f)
tot = [0] * M; err = 0; recs = []; params = None
for nm in names:
    data = open(os.path.join(ckdir, nm), 'rb').read()
    assert data[-70:-65] == b'\nEND ' and data[-1:] == b'\n', nm
    body = data[:-70]; want = data[-65:-1].decode()
    check(hashlib.sha256(body).hexdigest() == want, f'{nm}: SHA-256 trailer')
    arr = body[-16 * M:]; text = body[:-16 * M].decode()
    lines = text.split('\n')
    assert lines[0] == 'ACC2243CKPT v1' and lines[1].startswith('PARAMS ')
    p = lines[1][7:]
    if params is None: params = p
    check(p == params, f'{nm}: PARAMS identical to first checkpoint')
    assert lines[2] == f'FBITS {FB}'
    nrec = int(lines[3].split()[1])
    for i in range(nrec):
        f_ = lines[4 + i].split()
        assert f_[0] == 'U' and f_[2] == 'fp' and f_[4] == 'nterm' and f_[6] == 'cnt' and f_[8] == 'hash'
        recs.append(dict(u=int(f_[1]), fp=int(f_[3], 16), nterm=int(f_[5]), cnt=int(f_[7]), h=f_[9], file=nm))
    e_line = lines[4 + nrec]; a_line = lines[5 + nrec]
    assert e_line.startswith('ERR ') and a_line == f'ACC {M}' and lines[6 + nrec] == ''
    err += int(e_line[4:], 16)
    for k in range(M):
        tot[k] += int.from_bytes(arr[16 * k:16 * k + 16], 'little', signed=True)
print(f'checkpoints {len(names)}  records {len(recs)}  PARAMS "{params}"')

nunit = None
for fn in engine_outs:
    for l in open(fn):
        m_ = re.match(r'MERGE checkpoints (\d+) units (\d+)', l)
        if m_: nunit = int(m_.group(2))
us = sorted(r['u'] for r in recs)
check(nunit is not None and us == list(range(nunit)), f'coverage: every unit 0..{nunit - 1} exactly once ({len(us)} records, {len(set(us))} distinct)')
fpsum = sum(r['fp'] for r in recs) & MASK64
fparr = sum((t & MASK64) * splitmix64(k + 1) for k, t in enumerate(tot)) & MASK64
check(fpsum == fparr, f'fingerprint: sum_u fp(u) = {fpsum:016x}, sum_k S_k rho_k = {fparr:016x} (mod 2^64, own splitmix64)')
# L units are 0..NL-1, S blocks NL..: NL = number of units whose record is an L unit; engine RUN line gives NL
NL = None
for fn in [os.path.join(os.path.dirname(ckdir.rstrip('/')), os.path.basename(ckdir.rstrip('/')) + '_run.log')]:
    if os.path.exists(fn):
        for l in open(fn):
            m_ = re.search(r'L-subunits (\d+) \+ S-blocks (\d+)', l)
            if m_: NL = int(m_.group(1))
smooth = sum(r['cnt'] for r in recs if NL is not None and r['u'] >= NL)
pairs = sum(r['cnt'] for r in recs if NL is not None and r['u'] < NL)
nterm = sum(r['nterm'] for r in recs)
check(NL is not None and smooth + pairs == T, f'count identity: smooth {smooth} + pairs {pairs} = {smooth + pairs} vs T {T}')
E = F(err, 1 << FB)
print(f'error tally err = {err} units of 2^-96 = {float(E):.6e}   nterm = {nterm}   err/nterm = {err / max(nterm, 1):.4f}')

# ---------------- 2. CHUNK_DIGEST ----------------
h = hashlib.sha256()
for t in tot: h.update((t & ((1 << 128) - 1)).to_bytes(16, 'little'))
h.update(struct.pack('<QQ', err >> 64, err & MASK64)); h.update(struct.pack('<QQQ', smooth, pairs, nterm))
mydig = h.hexdigest()
print(f'CHUNK_DIGEST (reviewer, recomputed from checkpoints) {mydig}')
for fn in engine_outs:
    for l in open(fn):
        if l.startswith('CHUNK_DIGEST'):
            check(l.split()[1] == mydig, f'{os.path.basename(fn)}: engine CHUNK_DIGEST {l.split()[1][:16]}... == reviewer recomputation')

# ---------------- 3. class sums vs certified arbcore balls ----------------
def dump_to_frac(man, ex):
    return F(int(man, 16)) * (F(2) ** int(ex, 16))
cert = {}
cert_print = {}
for l in open(cert_msl):
    if l.startswith('SDUMP '):
        _, k, mm, me, rm, re_ = l.split()
        cert[int(k)] = (dump_to_frac(mm, me), dump_to_frac(rm, re_))
    elif l.startswith('S '):
        m_ = re.match(r'S (\d+) \[([-0-9.e+]+) \+/- ([0-9.e+-]+)\]', l)
        if m_: cert_print[int(m_.group(1))] = (F(Decimal(m_.group(2))), F(Decimal(m_.group(3))))
check(len(cert) == M, f'certified SDUMP balls read: {len(cert)} of {M}')
maxd = F(0); nov = 0
for k in range(M):
    mid = F(tot[k], 1 << FB); cm, cr = cert[k]
    d = abs(mid - cm); maxd = max(maxd, d)
    nov += d <= E + cr
check(nov == M, f'class sums: {nov} of {M} exact midpoints within E + rad_cert of the certified arbcore ball (max |diff| = {float(maxd):.3e}, E = {float(E):.3e})')
# engine's printed S_k balls vs certified printed balls
for fn in engine_outs:
    eng = {}
    for l in open(fn):
        m_ = re.match(r'S (\d+) \[([-0-9.e+]+) \+/- ([0-9.e+-]+)\]', l)
        if m_: eng[int(m_.group(1))] = (F(Decimal(m_.group(2))), F(Decimal(m_.group(3))))
    ov = sum(1 for k in range(M) if k in eng and abs(eng[k][0] - cert_print[k][0]) <= eng[k][1] + cert_print[k][1])
    ctn = sum(1 for k in range(M) if k in eng and abs(eng[k][0] - F(tot[k], 1 << FB)) <= eng[k][1])
    check(ov == M, f'{os.path.basename(fn)}: {ov} of {M} printed class-sum balls overlap the certified printed balls (msl file)')
    check(ctn == M, f'{os.path.basename(fn)}: {ctn} of {M} printed class-sum balls contain the reviewer\'s exact merged midpoint')

# ---------------- 4. symbols vs certified ----------------
cs = {}
for l in open(cert_sym):
    if l.startswith('#') or not l.strip(): continue
    b, p, q = l.split(); cs[int(b)] = (F(p), F(q))
units = [b for b in range(1, M) if __import__('math').gcd(b, M) == 1]
check(sorted(cs) == units, f'certified symbol set complete ({len(cs)} residues)')
def parse_ball(s):
    m_ = re.match(r'\[([-0-9.e+]+) \+/- ([0-9.e+-]+)\]', s)
    if m_: return F(Decimal(m_.group(1))), F(Decimal(m_.group(2)))
    m_ = re.match(r'\[\+/- ([0-9.e+-]+)\]', s)          # zero midpoint printed as [+/- r]
    if m_: return F(0), F(Decimal(m_.group(1)))
    return F(Decimal(s)), F(0)   # exact print
for fn in engine_outs:
    xb = {}
    for l in open(fn):
        m_ = re.match(r'XB (\d+) plus (\[[^\]]*\]|\S+) cand (-?\d+)/(\d+) contains (\d) unique (\d) minus (\[[^\]]*\]|\S+) cand (-?\d+)/(\d+) contains (\d) unique (\d)', l)
        if m_: xb[int(m_.group(1))] = m_.groups()
    okp = okm = inb = 0
    for b in units:
        g = xb.get(b)
        if g is None: continue
        pc = F(int(g[2]), int(g[3])); mc = F(int(g[7]), int(g[8]))
        okp += pc == cs[b][0] and g[4] == '1' and g[5] == '1'
        okm += mc == cs[b][1] and g[9] == '1' and g[10] == '1'
        (pm, pr), (mm_, mr) = parse_ball(g[1]), parse_ball(g[6])
        inb += (abs(pm - cs[b][0]) <= pr) + (abs(mm_ - cs[b][1]) <= mr)
    check(len(xb) == len(units), f'{os.path.basename(fn)}: {len(xb)} XB lines for {len(units)} residues')
    check(okp == len(units), f'{os.path.basename(fn)}: {okp} of {len(units)} PLUS symbols identified (contains=1, unique=1) and EXACTLY equal to certified')
    check(okm == len(units), f'{os.path.basename(fn)}: {okm} of {len(units)} MINUS symbols identified (contains=1, unique=1) and EXACTLY equal to certified')
    check(inb == 2 * len(units), f'{os.path.basename(fn)}: {inb} of {2 * len(units)} printed symbol balls contain the certified value')

# ---------------- 5. independent symbol re-derivation (mpmath, non-rigorous cross-check) ----------------
a1, a2, a3, a4, a6 = 0, -22735, 0, 106272484, 0
b2 = a1 * a1 + 4 * a2; b4 = 2 * a4 + a1 * a3; b6 = a3 * a3 + 4 * a6
roots = sorted([mp.re(r) for r in mp.polyroots([4, b2, 2 * b4, b6], maxsteps=200, extraprec=200)], reverse=True)
e1, e2, e3 = roots
omp = mp.pi / mp.agm(mp.sqrt(e1 - e3), mp.sqrt(e1 - e2)); omm = mp.pi / mp.agm(mp.sqrt(e1 - e3), mp.sqrt(e2 - e3))
kap = 2 * mp.pi / (M * mp.sqrt(Q))
tail = mp.e ** (-kap * T) * (2 * mp.sqrt(T) + ((mp.log(T) + 2) / kap + 1 / (kap ** 2 * T)) / mp.sqrt(T))
print(f'reviewer mpmath: Omega+ = {mp.nstr(omp, 25)}  Omega- = {mp.nstr(omm, 25)}  2*tail_MS(T) = {mp.nstr(2 * tail, 12)}')
S = [mp.mpf(t) / mp.mpf(2) ** FB for t in tot]
budget = (2 * tail + 2 * mp.mpf(E.numerator) / E.denominator)
maxdp = maxdm = mp.mpf(0)
for b in units:
    ub = pow(Q * b % M, -1, M)
    re_ = sum(S[k] * (mp.cos(2 * mp.pi * (k * b % M) / M) + SIGN * mp.cos(2 * mp.pi * (k * ub % M) / M)) for k in range(M))
    im_ = sum(S[k] * (mp.sin(2 * mp.pi * (k * b % M) / M) - SIGN * mp.sin(2 * mp.pi * (k * ub % M) / M)) for k in range(M))
    xp, xm = re_ / omp, im_ / omm
    dp = abs(xp - mp.mpf(cs[b][0].numerator) / cs[b][0].denominator); dm = abs(xm - mp.mpf(cs[b][1].numerator) / cs[b][1].denominator)
    maxdp = max(maxdp, dp); maxdm = max(maxdm, dm)
check(maxdp <= budget / omp, f'mpmath re-derivation: max |x_b^+ (truncated) - certified| = {mp.nstr(maxdp, 6)} <= budget (2 tail + 2E)/Omega+ = {mp.nstr(budget / omp, 6)}')
check(maxdm <= budget / omm, f'mpmath re-derivation: max |x_b^- (truncated) - certified| = {mp.nstr(maxdm, 6)} <= budget (2 tail + 2E)/Omega- = {mp.nstr(budget / omm, 6)}')
print(f'identification margin (plus): 1/(2*1024) - budget/Omega+ = {mp.nstr(mp.mpf(1) / 2048 - budget / omp, 6)}')
print('INDEP_MERGE_' + ('PASS' if not fails else 'FAIL'), f'failures={len(fails)}')
sys.exit(1 if fails else 0)
