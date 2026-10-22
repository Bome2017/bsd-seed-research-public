#!/bin/bash
# R5: complete path at the REAL 2243 parameters (m = 2243^2, T = T_run), local host. Nothing here is a certificate run:
# a unit subset is accumulated (selection), so no symbol value means anything. What is tested:
#  A  reference run: pre-produced heights (q ~ 1e7, 1e9, 1e11, 1e13, 31 top segments at 3.912e13) + 5 top segments STREAMED
#     (produce -> verify -> accumulate -> delete) + 3 Part S blocks (n ~ 1e10, 1e12, 3.9e13); per-unit timing log
#  B  crash after 12 units (spot interruption stand-in), restart with a different W: digest must equal A
#  C  two shards (tags A/B) pooled into one merge directory: digest must equal A
#  D  the 5 streamed segments produced once into a directory (stored path), non-stream run: digest must equal A;
#     verifier hashes (stream logs) must equal the accumulator's segment hashes
#  M  full-size merge path at m = 5 031 049 on run A: acb_dft + 5.03e6 symbol identifications + weights (timing, memory)
set -u
P5=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline; S3=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S3_bench
F=/Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22; R=/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19
export DYLD_LIBRARY_PATH=/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4/Odarwin-x86_64
export PRODUCER=$F/producer_variant/apwit_v VERIFIER=$R/verifier/wverify
D=$P5/tests/r5; rm -rf $D; mkdir -p $D/ap; cd $D
T=39119887532031; export T_RUN=$T
for f in $S3/ap/ap_*.bin $S3/conc/ap/ap_*.bin; do ln -s $f ap/; done
C=(0 -22735 0 106272484 0 5031049 2899325908488 -1 $T 16777216 $D/ap)
SEL5="L0/0-1,L59/0-0,L5960,L596046,L2331695-2331725,L2331680-2331684,S2384,S238418,S9326906"
dig() { grep '^CHUNK_DIGEST' "$1" | awk '{print $2}'; }
UTT=100000000
echo "ap files: $(ls ap | wc -l | tr -d ' ')"; uptime
# A
ACC_SELECT=$SEL5 ACC_TIMING_LOG=1 ACC_STREAM_CMD=$P5/stream_seg.sh /usr/bin/time -l $P5/acc2243v2 run "${C[@]}" 8 A $UTT 4 > A_run.txt 2> A_run.time
echo "A run exit $? : $(grep '^RUN' A_run.txt | tr '\n' ' ') maxRSS $(grep 'maximum resident' A_run.time | awk '{print $1}')"
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C[@]}" A 1024 > A_merge.txt 2>&1; grep -E '^(MERGE|FINGERPRINT|COUNT_SELECTION|AP_SEGROOT|CHUNK_DIGEST|ROUNDING)' A_merge.txt
# B
ACC_SELECT=$SEL5 ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run "${C[@]}" 6 B $UTT 2 12 > B_run1.txt 2>&1; echo "B first attempt exit $?"
ACC_SELECT=$SEL5 ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run "${C[@]}" 3 B $UTT 2 > B_run2.txt 2>&1; grep '^RUN units' B_run2.txt
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C[@]}" B 1024 > B_merge.txt 2>&1
[ -n "$(dig A_merge.txt)" ] && [ "$(dig A_merge.txt)" = "$(dig B_merge.txt)" ] && echo "R5-B PASS crash/restart digest == A" || echo "R5-B FAIL"
# C
mkdir -p C_pool
ACC_SELECT=$SEL5 ACC_SHARD=0/2 ACC_TAG=A ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run "${C[@]}" 4 C_A $UTT 3 > C_A.txt 2>&1 &
ACC_SELECT=$SEL5 ACC_SHARD=1/2 ACC_TAG=B ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run "${C[@]}" 4 C_B $UTT 3 > C_B.txt 2>&1 &
wait; cp C_A/ckpt_*.bin C_B/ckpt_*.bin C_pool/
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C[@]}" C_pool 1024 > C_merge.txt 2>&1
[ -n "$(dig C_merge.txt)" ] && [ "$(dig A_merge.txt)" = "$(dig C_merge.txt)" ] && echo "R5-C PASS two pooled shards digest == A ($(ls C_pool | wc -l | tr -d ' ') checkpoints)" || echo "R5-C FAIL"
# D
mkdir -p apD; for f in ap/*.bin; do ln -s $(readlink $f) apD/; done
for s in 2331680 2331681 2331682 2331683 2331684; do $P5/stream_seg.sh $s $D/Dprod/w$s & done; wait
for s in 2331680 2331681 2331682 2331683 2331684; do mv Dprod/w$s/ap_$s.bin apD/; done          # %06d of a 7-digit segment = the number
CD=(0 -22735 0 106272484 0 5031049 2899325908488 -1 $T 16777216 $D/apD)
ACC_SELECT=$SEL5 $P5/acc2243v2 run "${CD[@]}" 8 Dr $UTT 4 > D_run.txt 2>&1
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${CD[@]}" Dr 1024 > D_merge.txt 2>&1
[ -n "$(dig D_merge.txt)" ] && [ "$(dig A_merge.txt)" = "$(dig D_merge.txt)" ] && echo "R5-D PASS stored-path digest == streamed-path digest" || echo "R5-D FAIL"
cat A/stream_g*_w*/stream_log.txt | awk '{print $3, $NF}' | LC_ALL=C sort -k1,1 > A_stream_hashes.txt
grep ^SEGHASH A_merge.txt | awk '{print $2, $3}' | LC_ALL=C sort -k1,1 | LC_ALL=C join - A_stream_hashes.txt | awk '$2 != $3 {bad++} END {print (NR == 5 && bad == 0 ? "R5-H PASS" : "R5-H FAIL") " verifier-vs-accumulator hashes: " NR " streamed segments (expect 5), mismatches " bad+0}'
# M
ACC_PARTIAL_WEIGHTS_TIMING=1 /usr/bin/time -l $P5/acc2243v2 merge "${C[@]}" A 1024 2243 2 3 1 > M_merge.txt 2> M_merge.time
grep -E '^(PARTIAL|DFT|SYMBOLS_FILE|SYMBOL_PASS|SYMBOL_RADIUS_BUDGET|XB_PLUS|WEIGHTS)' M_merge.txt; echo "M maxRSS $(grep 'maximum resident' M_merge.time | awk '{print $1}') real $(grep ' real' M_merge.time | awk '{print $1}')"
# radius budget at the FULL run's tail (T = T_run): the partial selection only lowers the rounding term, which is negligible either way
python3 - M_merge.txt <<'EOP'
import re, sys
t = open(sys.argv[1]).read(); m = re.search(r'XB_PLUS_DETERMINED (\d+) of (\d+) .* max plus radius ([0-9.e+-]+) \(unique iff < ([0-9.e+-]+)\)', t)
b = re.search(r'tail 2tail/Omega\+ ([0-9.e+-]+) \+ rounding 2E/Omega\+ ([0-9.e+-]+)', t)
ok = bool(m) and float(m.group(3)) < float(m.group(4))       # uniqueness is a radius property; 'contains' is value-dependent (meaningless here)
print(("R5-M PASS" if ok else "R5-M FAIL") + f" full-size DFT symbol radius at T_run: max {m.group(3)} vs threshold {m.group(4)} (tail {b.group(1)}, rounding {b.group(2)}); (determined-by-chance {m.group(1)} of {m.group(2)}: values meaningless for a partial selection; the radius budget is the full run's)")
EOP
echo R5_DONE
