#!/usr/bin/env python3
"""Independent integrity audit of a finished run_p3.sh output directory (no code shared with arbcore / p3_check.py).
usage: p3_integrity.py RUN_OUT_DIR [SEGQ]
Checks: every segment done + logged by the verifier with the tiling lo = s*SEGQ, hi = (s+1)*SEGQ; every verified a_q file has
4*primes bytes and the logged SHA-256; every kept witness file matches its logged SHA-256; producer witness counts + exhaustive
(small/bad) primes = verifier prime counts; every arbcore unit file (all targets) has a valid END self-hash, the right header
index, and (Part-L units) an a_q-segment hash equal to the verifier's; unit sets complete; PARAMS present; segment roots and
count identities of the msl outputs recomputed from the files."""
import sys, os, re, hashlib, glob
RUN = sys.argv[1]; SEGQ = int(sys.argv[2]) if len(sys.argv) > 2 else 2 ** 24; BLK = 2 ** 22
fails = []
def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok: fails.append(msg)
def sha(path, bufsize=1 << 22):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            b = f.read(bufsize)
            if not b: break
            h.update(b)
    return h.hexdigest()
targets = [tuple(int(x) for x in l.split()) for l in open(f'{RUN}/targets.txt')]      # m M s Q tmin T
TMAX = max(t[5] for t in targets); NSEG = (TMAX + 1) // SEGQ
check((TMAX + 1) % SEGQ == 0, f'TMAX + 1 = {TMAX + 1} is a multiple of SEGQ; NSEG = {NSEG}')
# ---- stage W ----
ver = {}
for fn in glob.glob(f'{RUN}/logs/ver_*.log'):
    for l in open(fn):
        p = l.split()
        if p and p[0] == 'SEG':
            s = int(p[1]); ver.setdefault(s, []).append((int(p[3]), int(p[5]), int(p[7]), int(p[9]), p[11]))
prod = {}
for fn in glob.glob(f'{RUN}/logs/prod_*.log'):
    for l in open(fn):
        p = l.split()
        if p and p[0] == 'SEG': prod.setdefault(int(p[1]), []).append(int(p[7]))
done = set(int(os.path.basename(x).split('.')[0]) for x in glob.glob(f'{RUN}/seg/*.done'))
check(done == set(range(NSEG)), f'done markers: {len(done)} of {NSEG}, none missing')
check(set(ver) == set(range(NSEG)) and all(len(v) == 1 for v in ver.values()), f'verifier logged each of the {NSEG} segments exactly once')
bad_tiling = [s for s in ver if ver[s][0][0] != s * SEGQ or ver[s][0][1] != (s + 1) * SEGQ]
check(not bad_tiling, f'verifier tiling lo = s*SEGQ, hi = (s+1)*SEGQ for every segment (violations: {bad_tiling[:5]})')
nprimes = sum(v[0][2] for v in ver.values()); nwit = sum(v[0][3] for v in ver.values())
print(f'INFO primes verified: {nprimes}; by witness: {nwit}; exhaustive (small/bad): {nprimes - nwit}')
check(all(prod.get(s, [None])[-1] == ver[s][0][3] for s in ver), 'producer witness count == verifier witness count, every segment')
badap, badwit, nwitkept = [], [], 0
for s in range(NSEG):
    lo, hi, np_, nw, h = ver[s][0]; f = f'{RUN}/ap/ap_{s:06d}.bin'
    if not os.path.exists(f) or os.path.getsize(f) != 4 * np_ or sha(f) != h: badap.append(s)
    w = f'{RUN}/wit/wit_{s:06d}.bin'; ws = f'{RUN}/logs/witsha_{s}.txt'
    if os.path.exists(w):
        nwitkept += 1
        if not os.path.exists(ws) or open(ws).read().split()[0] != sha(w): badwit.append(s)
check(not badap, f'all {NSEG} verified a_q files: size = 4*primes and SHA-256 = verifier log (bad: {badap[:5]})')
check(not badwit, f'kept witness files: {nwitkept}; every one matches its logged SHA-256 (bad: {badwit[:5]})')
# ---- stage A units ----
for (m, M, s_, Q, tmin, T) in targets:
    d = f'{RUN}/units_m{m}'; nseg = (T + 1) // SEGQ; nblk = (T + BLK - 1) // BLK
    params = open(f'{d}/PARAMS').read().strip() if os.path.exists(f'{d}/PARAMS') else ''
    check(params.startswith(f'msl 0 -22735 0 106272484 0 {m} {Q} {s_} {T} {SEGQ} ') and params.endswith(' 1024'),
          f'm={m}: PARAMS = "{params[:60]}... {params[-30:]}"')
    names = sorted(os.listdir(d)); units = [x for x in names if x.endswith('.txt')]; tmp = [x for x in names if x.endswith('.tmp')]
    want = [f'lseg_{i:06d}.txt' for i in range(nseg)] + [f'blk_{i:06d}.txt' for i in range(nblk)]
    check(sorted(units) == sorted(want) and not tmp, f'm={m}: unit set complete: {nseg} L-units + {nblk} S-units, no leftover .tmp')
    badh, badhdr = [], []
    for u in units:
        raw = open(f'{d}/{u}', 'rb').read(); e = raw.rstrip(b'\n').rfind(b'\n') + 1; last = raw[e:].decode().split()
        if len(last) != 2 or last[0] != 'END' or hashlib.sha256(raw[:e]).hexdigest() != last[1]: badh.append(u); continue
        hdr = raw[:raw.find(b'\n')].decode().split(); idx = int(u.split('_')[1].split('.')[0])
        if u.startswith('lseg'):
            if hdr[0] != 'LSEG' or int(hdr[1]) != idx or hdr[hdr.index('apsha') + 1] != ver[idx][0][4]: badhdr.append(u)
        elif hdr[0] != 'BLK' or int(hdr[1]) != idx: badhdr.append(u)
    check(not badh, f'm={m}: every unit self-hash valid ({len(units)} units; bad: {badh[:3]})')
    check(not badhdr, f'm={m}: unit headers index-consistent; every Part-L unit a_q hash = verifier ap_sha256 (bad: {badhdr[:3]})')
    txt = open(f'{RUN}/msl_m{m}.txt').read()
    root = hashlib.sha256(b''.join(bytes.fromhex(ver[i][0][4]) for i in range(nseg))).hexdigest()
    got = re.search(r'AP_SEGROOT_SHA256 (\w+) segments (\d+)', txt)
    check(got is not None and got.group(1) == root and int(got.group(2)) == nseg, f'm={m}: AP_SEGROOT = SHA-256 over {nseg} verifier segment hashes = {root}')
    c = re.search(r'COUNT smooth (\d+) pairs (\d+) sum (\d+) T (\d+) identity (\d)', txt)
    check(c is not None and int(c.group(1)) + int(c.group(2)) == T == int(c.group(4)) and c.group(5) == '1', f'm={m}: count identity {c.group(0) if c else "missing"}')
print('INTEGRITY_' + ('PASS' if not fails else 'FAIL'), f'failures={len(fails)}')
sys.exit(1 if fails else 0)
