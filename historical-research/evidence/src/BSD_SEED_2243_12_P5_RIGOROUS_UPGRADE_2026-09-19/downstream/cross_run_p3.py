#!/usr/bin/env python3
"""Cross-run check: this run's verified a_q files and witness-file hashes for segments 0..NSEG-1 versus the p = 3 run
(same tiling: SEGQ = 2^24 and both T + 1 multiples of 2^24).  Two independent executions of producer + verifier must agree byte for byte."""
import os, glob, hashlib
P5 = os.path.expanduser('~/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run'); P3 = os.path.expanduser('~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run')
def ver(run):
    d = {}
    for fn in glob.glob(run + '/logs/ver_*.log'):
        for l in open(fn):
            p = l.split()
            if p and p[0] == 'SEG': d[int(p[1])] = (int(p[3]), int(p[5]), int(p[7]), int(p[9]), p[11])
    return d
v5, v3 = ver(P5), ver(P3); n = len(v5)
same_log = all(v5[s] == v3[s] for s in range(n))
def wsha(run, s): return open(f'{run}/logs/witsha_{s}.txt').read().split()[0]
same_wit = all(wsha(P5, s) == wsha(P3, s) for s in range(n))
def fsha(path): return hashlib.sha256(open(path, 'rb').read()).hexdigest()
same_files = all(fsha(f'{P5}/ap/ap_{s:06d}.bin') == fsha(f'{P3}/ap/ap_{s:06d}.bin') for s in range(n))
root5 = hashlib.sha256(b''.join(bytes.fromhex(v5[s][4]) for s in range(n))).hexdigest()
root3 = hashlib.sha256(b''.join(bytes.fromhex(v3[s][4]) for s in range(n))).hexdigest()
print(f'segments compared: {n}; primes {sum(v5[s][2] for s in range(n))}')
print(f'{"PASS" if same_log else "FAIL"} verifier SEG records (lo, hi, primes, witnesses, ap_sha256) identical to the p = 3 run for all {n} segments')
print(f'{"PASS" if same_files else "FAIL"} verified a_q files byte-identical to the p = 3 run (re-hashed from disk) for all {n} segments')
print(f'{"PASS" if same_wit else "FAIL"} witness-file SHA-256 identical to the p = 3 run for all {n} segments (producer determinism)')
print(f'a_q root over segments 0..{n-1}: this run {root5}; p = 3 run {root3}; {"EQUAL" if root5 == root3 else "DIFFERENT"}')
print('CROSS_RUN_' + ('PASS' if same_log and same_files and same_wit and root5 == root3 else 'FAIL'))
