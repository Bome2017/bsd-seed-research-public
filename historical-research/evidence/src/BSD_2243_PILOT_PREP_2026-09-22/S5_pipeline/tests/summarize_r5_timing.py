#!/usr/bin/env python3
"""Summarize R5 run A: per-unit wall seconds from the timing logs (stream = produce + verify, acc = accumulate) and the
stream logs (producer / verifier user seconds). The streamed top-range segments are complete-path chunks at the upper end
of the planned range; R5 ran 8 workers on a 10-core host, so these are loaded-host walls (the local analogue of pilot P4)."""
import glob, re, statistics as st
D = '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline/tests/r5/A'
rows = [L.split() for f in glob.glob(f'{D}/timing_*.txt') for L in open(f)]
stream = {}
for f in glob.glob(f'{D}/stream_g*_w*/stream_log.txt'):
    for L in open(f):
        m = re.search(r'STREAM seg (\d+) prod_user ([0-9.]+) ver_user ([0-9.]+) primes (\d+)', L)
        if m: stream[int(m.group(1))] = (float(m.group(2)), float(m.group(3)), int(m.group(4)))
# timing line: U <unit> <L|S> <segment|block> stream_s <x> acc_s <y> nterm <n> cnt <c>
tops = [r for r in rows if r[2] == 'L' and float(r[5]) > 0]
print(f"units timed {len(rows)}; streamed segments {len(tops)}")
for r in sorted(tops, key=lambda r: int(r[3])):
    s = int(r[3]); pu, vu, npr = stream.get(s, (0, 0, 0))
    print(f"  streamed chunk seg {s}: wall stream {float(r[5]):7.2f} s (producer user {pu:.2f} s + verifier user {vu:.2f} s, {npr} primes) + accumulate {float(r[7]):.3f} s")
if tops:
    w = [float(r[5]) + float(r[7]) for r in tops]; print(f"  complete-path wall per top chunk: mean {st.mean(w):.1f} s (min {min(w):.1f}, max {max(w):.1f})")
for kind, lab in (('L', 'pre-produced L units'), ('S', 'S blocks')):
    sel = [float(r[7]) for r in rows if r[2] == kind and float(r[5]) == 0]
    if sel: print(f"  {lab}: {len(sel)} units, accumulate wall mean {st.mean(sel):.3f} s, total {sum(sel):.1f} s")
