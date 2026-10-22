#!/bin/bash
# pilot_run.sh -- the bounded 2243 cloud pilot, run ON the rented machine after scripts/bootstrap.sh.
# NOT a certificate run: it measures cost and checks correctness of the pipeline. Unit subsets only; no symbol it prints
# is a symbol value, and no coefficient / unit test is computed on a subset (the engine refuses unless timing-labelled).
#
# Stages (each with its own wall-clock limit; the machine's shutdown timer, set before this script starts, is the hard cap):
#  P1  correctness replay: (a) v2 merge of the S2 checkpoints == S2 (direct and DFT); (b) m = 27 and (c) m = 81 FULL runs from
#      scratch with streamed a_q (produce -> verify -> accumulate) == the certified symbols / a_{4,2} = 15480, and the class-sum
#      digests == the local reference digests (bit identity across machines); streamed segment hashes == certified a_q hashes
#  P2  component rates at the 2243 heights (q ~ 1e9, 1e11, 1e13, 3.912e13), loaded (one process per core) and single:
#      producer, verifier, Part L / Part S traversal-kernel-summation profiles, checkpoint write, full-length DFT
#  P3  2243-scale data flow (the local R5 test): streamed + stored a_q, crash/restart, two pooled shards: digests == local R5;
#      full-size merge path (DFT + 5.03e6 symbol identifications + weights, timing-labelled) time and memory
#  P4  sustained throughput: streamed top-range chunks at full load, whole process group killed (kill -9) mid-run and
#      restarted; mixed heights. Output: fully verified, accumulated chunks per hour and $ per chunk (PRICE_PER_HOUR)
# Usage (as the launcher does): STAGES=P1,P2,P3,P4 PRICE_PER_HOUR=<usd> P4_MINUTES=40 scripts/pilot_run.sh
set -u
export LC_ALL=C
B=$(cd "$(dirname "$0")/.." && pwd); BIN=$B/bin; REF=$B/reference; R=$B/results; WK=$B/work; mkdir -p $R $WK
NC=$(nproc); export LD_LIBRARY_PATH=$B/local/lib PRODUCER=$BIN/apwit_v VERIFIER=$BIN/wverify
STAGES=${STAGES:-P1,P2,P3,P4}; P4_MINUTES=${P4_MINUTES:-40}; PRICE=${PRICE_PER_HOUR:-0}
SEED=(0 -22735 0 106272484 0); T=39119887532031; M=5031049; Q=2899325908488; SG=16777216
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a $R/pilot.log; }
check() { if [ "$2" = 0 ]; then echo "CHECK $1 PASS $3" | tee -a $R/checks.txt; else echo "CHECK $1 FAIL $3" | tee -a $R/checks.txt; fi; }
key() { grep -E '^(FINGERPRINT|COUNT |AP_SEGROOT|ROUNDING_ERR_TOTAL|TAIL_MS|S |OMEGA|XB |WEIGHTS|A_EXACT|A_MOD_P|NONZERO_ONLY)' "$1"; }
dig() { grep '^CHUNK_DIGEST' "$1" 2>/dev/null | awk '{print $2}'; }
keyx() { grep -E '^(FINGERPRINT|COUNT |AP_SEGROOT|ROUNDING_ERR_TOTAL|TAIL_MS|S |OMEGA|WEIGHTS|A_EXACT|A_MOD_P)' "$1"; }
vs_s2() { diff <(keyx "$1") <(keyx "$2") > /dev/null && python3 $B/scripts/compare_dft.py "$1" "$2" 1.0 | grep -q '^CMP PASS'; }   # S2 printed the same symbols with (slightly) larger radii
refv() { grep "^$1 " $REF/expected.txt | cut -d' ' -f2-; }
same() { [ -n "$1" ] && [ "$1" = "$2" ]; }
hashcmp() { join <(sort -k1,1 "$1") <(sort -k1,1 "$2") | awk '$2 != $3 {b++} END {print NR " common, " b+0 " mismatches"; exit (b > 0 || NR == 0)}'; }   # "seg hash" files
{ echo "host $(hostname) nproc $NC"; lscpu | grep -E 'Model name|Socket|Core|Thread|MHz|L3'; free -g | head -2
  TOK=$(curl -s -m 2 -X PUT http://169.254.169.254/latest/api/token -H 'X-aws-ec2-metadata-token-ttl-seconds: 60' 2>/dev/null)
  [ -n "$TOK" ] && echo "aws_instance_type $(curl -s -m 2 -H "X-aws-ec2-metadata-token: $TOK" http://169.254.169.254/latest/meta-data/instance-type)" \
               && echo "aws_lifecycle $(curl -s -m 2 -H "X-aws-ec2-metadata-token: $TOK" http://169.254.169.254/latest/meta-data/instance-life-cycle)"
  echo "price_per_hour_usd $PRICE"; cat $B/logs/build_hashes.txt 2>/dev/null; } > $R/machine.txt
log "pilot start: stages $STAGES, nproc $NC, price/h $PRICE"
# produce + verify segments, one process per core; moves ap_<s>.bin + ap_<s>.sha256 (verifier hash) into $2; log lines to results
batch_segments() { local tr=$1 out=$2 tag=$3; shift 3; mkdir -p $out; [ $# -eq 0 ] && return 0
  printf '%s\n' "$@" | xargs -P $NC -I{} env T_RUN=$tr $B/scripts/stream_seg.sh {} $WK/prod_$tag/w{} > /dev/null 2>&1
  for s in "$@"; do S6=$(printf %06d $s); mv $WK/prod_$tag/w$s/ap_$S6.bin $WK/prod_$tag/w$s/ap_$S6.sha256 $out/ 2>/dev/null
    cat $WK/prod_$tag/w$s/stream_log.txt 2>/dev/null; done >> $R/${tag}_stream.txt
  rm -rf $WK/prod_$tag; }
need_segments() { local tr=$1 out=$2 tag=$3; shift 3; local miss=(); for s in "$@"; do [ -f $out/ap_$(printf %06d $s).bin ] || miss+=($s); done
  batch_segments $tr $out $tag "${miss[@]}"; }
# ------------------------------------------------------------------------------------------------------------------ P1
if [[ $STAGES == *P1* ]]; then
  log "P1 correctness replay"; mkdir -p $WK/none
  C27=("${SEED[@]}" 27 2167729337579528 1 4831838207 $SG); C81=("${SEED[@]}" 81 2167729337579528 1 14847836159 $SG)
  ACC_DFT=0 $BIN/acc2243v2 merge "${C27[@]}" $WK/none $REF/T2/run_m27 1024 > $R/p1a_m27.txt 2>&1
  ACC_DFT=0 $BIN/acc2243v2 merge "${C81[@]}" $WK/none $REF/T2/run_m81 1024 3 4 2 -1 > $R/p1a_m81.txt 2>&1
  ACC_DFT=1 $BIN/acc2243v2 merge "${C81[@]}" $WK/none $REF/T2/run_m81 1024 3 4 2 -1 > $R/p1a_m81_dft.txt 2>&1
  for m in 27 81; do diff <(key $REF/v23/merge_m$m.txt) <(key $R/p1a_m$m.txt) > /dev/null; check P1a_m${m}_merge_bit_identical_to_local $? "$(key $R/p1a_m$m.txt | wc -l) lines"
    vs_s2 $REF/T2/merge_m$m.txt $R/p1a_m$m.txt; check P1a_m${m}_symbols_equal_S2 $? "candidates/flags identical, radii <= S2"; done
  diff <(key $REF/v23/merge_m81_dft.txt) <(key $R/p1a_m81_dft.txt) > /dev/null; check P1a_m81_dft_bit_identical_to_local $? ""
  python3 $B/scripts/compare_dft.py $R/p1a_m81.txt $R/p1a_m81_dft.txt > $R/p1a_dft.txt; grep -q '^CMP PASS' $R/p1a_dft.txt; check P1a_m81_dft_equals_direct $? "$(cat $R/p1a_dft.txt)"
  for spec in "27 4831838207 0" "81 14847836159 0 1"; do set -- $spec; m=$1; tr=$2; shift 2
    mkdir -p $WK/m$m/ap; t0=$(date +%s); batch_segments $tr $WK/m$m/ap pre_m$m "$@"
    ( cd $WK/m$m && timeout 3600 env T_RUN=$tr ACC_TIMING_LOG=1 ACC_STREAM_CMD=$B/scripts/stream_seg.sh /usr/bin/time -v $BIN/acc2243v2 run "${SEED[@]}" $m 2167729337579528 1 $tr $SG $WK/m$m/ap $NC run 500000000 40 > $R/p1_m${m}_run.txt 2> $R/p1_m${m}_run.time )
    w=$(( $(date +%s) - t0 ))
    if [ $m = 81 ]; then ACC_DFT=0 $BIN/acc2243v2 merge "${SEED[@]}" 81 2167729337579528 1 $tr $SG $WK/m$m/ap $WK/m$m/run 1024 3 4 2 -1 > $R/p1_m81_merge.txt 2>&1
    else ACC_DFT=0 $BIN/acc2243v2 merge "${SEED[@]}" 27 2167729337579528 1 $tr $SG $WK/m$m/ap $WK/m$m/run 1024 > $R/p1_m27_merge.txt 2>&1; fi
    diff <(key $REF/v23/merge_m$m.txt) <(key $R/p1_m${m}_merge.txt) > /dev/null; check P1_m${m}_full_replay_bit_identical_to_local $? "$(grep -E '^(XB_PLUS_DETERMINED|A_EXACT)' $R/p1_m${m}_merge.txt | tr '\n' ' ')"
    vs_s2 $REF/T2/merge_m$m.txt $R/p1_m${m}_merge.txt; check P1_m${m}_full_replay_equals_certified $? "symbols vs S2 (which T2 matched to the certified SYMBOLS files)"
    same "$(dig $R/p1_m${m}_merge.txt)" "$(refv m${m}_digest)"; check P1_m${m}_digest_equals_local $? "$(dig $R/p1_m${m}_merge.txt)"
    cat $WK/m$m/run/stream_g*_w*/stream_log.txt $R/pre_m${m}_stream.txt 2>/dev/null | awk '{print $3, $NF}' > $R/p1_m${m}_hashes.txt
    hashcmp $R/p1_m${m}_hashes.txt $REF/certified_ap_sha256.txt > $R/p1_m${m}_hashcmp.txt; check P1_m${m}_streamed_ap_equals_certified $? "$(cat $R/p1_m${m}_hashcmp.txt)"
    log "P1 m=$m produce+verify+accumulate+merge wall ${w}s; $(grep -E 'Elapsed|Maximum resident' $R/p1_m${m}_run.time | tr -s ' ' | tr '\n' ' ')"
  done
fi
# ------------------------------------------------------------------------------------------------------------------ P2
if [[ $STAGES == *P2* ]]; then
  log "P2 component rates"; A2=$WK/ap2243; mkdir -p $A2
  cp $WK/m27/ap/ap_000000.bin $WK/m27/ap/ap_000000.sha256 $A2/ 2>/dev/null; need_segments $T $A2 seg0 0
  top0=$((2331725 - NC + 1))
  for h in "top $top0 2331725" "e13 596046 $((596046 + NC - 1))" "e11 5960 $((5960 + NC - 1))" "e9 59 $((59 + NC - 1))"; do set -- $h
    t0=$(date +%s); batch_segments $T $A2 p2_$1 $(seq $2 $3); echo "P2 batch $1 segments $2..$3 ($((1 + $3 - $2))) wall_s $(( $(date +%s) - t0 ))" | tee -a $R/pilot.log; done
  cat $R/p2_*_stream.txt | awk '{print $3, $NF}' > $R/p2_hashes.txt
  hashcmp $R/p2_hashes.txt $REF/local_ap_sha256_2243.txt > $R/p2_hashcmp.txt; check P2_ap_hashes_equal_local $? "$(cat $R/p2_hashcmp.txt)"
  CU=("${SEED[@]}" $M $Q -1 $T $SG $A2); BTOP=$(( (T - 4194304) / 4194304 ))
  for lvl in 0 1 2; do
    for seg in 0 59 5960 596046 2331725; do echo "p$lvl $(ACC_PROFILE=$lvl $BIN/acc2243v2 unit "${CU[@]}" 100000000 L $seg 0 2>&1)"; done
    for b in 2384 238418 $BTOP; do echo "p$lvl $(ACC_PROFILE=$lvl $BIN/acc2243v2 unit "${CU[@]}" 100000000 S $b 2>&1)"; done
  done > $R/p2_units_single.txt
  seq 1 $NC | xargs -P $NC -I{} $BIN/acc2243v2 unit "${CU[@]}" 100000000 L 59 0 > $R/p2_units_loaded_L59.txt 2>&1
  seq 1 $NC | xargs -P $NC -I{} $BIN/acc2243v2 unit "${CU[@]}" 100000000 S 238418 > $R/p2_units_loaded_S.txt 2>&1
  ACC_CKPT_BENCH=$WK/ckb $BIN/acc2243v2 unit "${CU[@]}" 100000000 L 2331725 0 > $R/p2_ckpt.txt 2>&1; rm -rf $WK/ckb
  $BIN/acc2243v2 dftbench $M > $R/p2_dft.txt 2>&1
  log "P2 done: $(cat $R/p2_dft.txt)"
fi
# ------------------------------------------------------------------------------------------------------------------ P3
if [[ $STAGES == *P3* ]]; then
  log "P3 2243-scale data flow (the local R5 selection)"; A2=$WK/ap2243; D3=$WK/p3; rm -rf $D3; mkdir -p $D3/ap $D3/apD
  PRE=(0 59 5960 596046 $(seq 2331695 2331725)); STR=(2331680 2331681 2331682 2331683 2331684)
  need_segments $T $A2 p3pre "${PRE[@]}" "${STR[@]}"
  for s in "${PRE[@]}"; do S6=$(printf %06d $s); for d in ap apD; do ln -s $A2/ap_$S6.bin $A2/ap_$S6.sha256 $D3/$d/; done; done
  for s in "${STR[@]}"; do ln -s $A2/ap_$s.bin $A2/ap_$s.sha256 $D3/apD/; done                # stored path for D only; A/B/C stream them
  SEL5=$(refv r5_selection); UTT=100000000; C3=("${SEED[@]}" $M $Q -1 $T $SG $D3/ap); CD=("${SEED[@]}" $M $Q -1 $T $SG $D3/apD)
  cd $D3; export T_RUN=$T
  ACC_SELECT=$SEL5 ACC_TIMING_LOG=1 ACC_STREAM_CMD=$B/scripts/stream_seg.sh $BIN/acc2243v2 run "${C3[@]}" 8 A $UTT 4 > $R/p3_A_run.txt 2>&1
  ACC_SELECT=$SEL5 ACC_STREAM_CMD=$B/scripts/stream_seg.sh $BIN/acc2243v2 run "${C3[@]}" 6 B $UTT 1 12 > $R/p3_B1.txt 2>&1
  ACC_SELECT=$SEL5 ACC_STREAM_CMD=$B/scripts/stream_seg.sh $BIN/acc2243v2 run "${C3[@]}" 3 B $UTT 1 > $R/p3_B2.txt 2>&1
  ACC_SELECT=$SEL5 ACC_SHARD=0/2 ACC_TAG=A ACC_STREAM_CMD=$B/scripts/stream_seg.sh $BIN/acc2243v2 run "${C3[@]}" 4 CA $UTT 3 > $R/p3_CA.txt 2>&1 &
  ACC_SELECT=$SEL5 ACC_SHARD=1/2 ACC_TAG=B ACC_STREAM_CMD=$B/scripts/stream_seg.sh $BIN/acc2243v2 run "${C3[@]}" 4 CB $UTT 3 > $R/p3_CB.txt 2>&1 &
  wait; mkdir -p Cpool; cp CA/ckpt_*.bin CB/ckpt_*.bin Cpool/
  ACC_SELECT=$SEL5 $BIN/acc2243v2 run "${CD[@]}" 8 Dr $UTT 4 > $R/p3_D.txt 2>&1
  for x in A B Cpool Dr; do if [ $x = Dr ]; then cc=("${CD[@]}"); else cc=("${C3[@]}"); fi
    ACC_NOSYMBOLS=1 $BIN/acc2243v2 merge "${cc[@]}" $x 1024 > $R/p3_merge_$x.txt 2>&1
    same "$(dig $R/p3_merge_$x.txt)" "$(refv r5_digest)"; check P3_${x}_digest_equals_local_R5 $? "$(dig $R/p3_merge_$x.txt)"; done
  grep '^RUN units' $R/p3_B2.txt | grep -q 'already done [1-9]'; check P3_B_restart_resumed_from_checkpoints $? "$(grep '^RUN units' $R/p3_B2.txt)"
  ACC_PARTIAL_WEIGHTS_TIMING=1 /usr/bin/time -v $BIN/acc2243v2 merge "${C3[@]}" A 1024 2243 2 3 1 > $R/p3_M_merge.txt 2> $R/p3_M_merge.time
  log "P3 full-size merge: $(grep -E '^(DFT|SYMBOL_PASS|SYMBOL_RADIUS_BUDGET)' $R/p3_M_merge.txt | tr '\n' ' ') $(grep -E 'Maximum resident|Elapsed' $R/p3_M_merge.time | tr -s ' ' | tr '\n' ' ')"
  python3 -c "import re,sys; t=open(sys.argv[1]).read(); m=re.search(r'max plus radius ([0-9.e+-]+) \(unique iff < ([0-9.e+-]+)\)', t); sys.exit(0 if m and float(m.group(1)) < float(m.group(2)) else 1)" $R/p3_M_merge.txt
  check P3_full_size_symbol_radius_below_threshold $? "$(grep -o 'max plus radius .*' $R/p3_M_merge.txt)"
  cd $B
fi
# ------------------------------------------------------------------------------------------------------------------ P4
if [[ $STAGES == *P4* ]]; then
  log "P4 sustained streamed throughput"; D4=$WK/p4; rm -rf $D4; mkdir -p $D4/ap
  ln -s $WK/ap2243/ap_000000.bin $WK/ap2243/ap_000000.sha256 $D4/ap/
  K=$(( P4_MINUTES * 60 * NC * 45 / 100 / 230 ))                  # top chunks for ~45% of the stage at ~230 s per chunk per core
  hi=$((2331725 - NC)); lo=$((hi - K + 1)); SEL4="L$lo-$hi"; C4=("${SEED[@]}" $M $Q -1 $T $SG $D4/ap); export T_RUN=$T
  log "P4 selection $SEL4 ($K top-range chunks, UNIT_TERMS 1e9, checkpoint every 300 s)"; cd $D4; t0=$(date +%s)
  ENVS=(ACC_SELECT=$SEL4 ACC_TIMING_LOG=1 ACC_CKPT_SECS=300 ACC_STREAM_CMD=$B/scripts/stream_seg.sh)
  setsid env "${ENVS[@]}" $BIN/acc2243v2 run "${C4[@]}" $NC run 1000000000 1000000 > $R/p4_run1.txt 2>&1 &
  pid=$!; sleep $(( P4_MINUTES * 60 * 30 / 100 )); kill -9 -- -$pid 2>/dev/null; wait $pid 2>/dev/null; sleep 2; t1=$(date +%s)
  fin1=$(cat run/timing_g001_*.txt 2>/dev/null | wc -l)
  timeout $(( P4_MINUTES * 60 * 65 / 100 )) env "${ENVS[@]}" $BIN/acc2243v2 run "${C4[@]}" $NC run 1000000000 1000000 > $R/p4_run2.txt 2>&1; rc=$?; t2=$(date +%s)
  rec1=$(grep '^RUN units' $R/p4_run2.txt | sed 's/.*already done \([0-9]*\) in.*/\1/')
  log "P4 process group killed at $((t1 - t0)) s: units finished $fin1, durable in checkpoints $rec1, lost to the kill $((fin1 - rec1)); restart exit $rc after $((t2 - t1)) s"
  ACC_NOSYMBOLS=1 $BIN/acc2243v2 merge "${C4[@]}" run 1024 > $R/p4_merge.txt 2>&1; grep -q '^CHUNK_DIGEST' $R/p4_merge.txt
  check P4_all_chunks_verified_accumulated_merged $? "$(grep -E '^(MERGE|COUNT_SELECTION)' $R/p4_merge.txt | tr '\n' ' ')"
  cat run/stream_g*_w*/stream_log.txt | awk '{print $3, $NF}' > $R/p4_stream_hashes.txt; grep ^SEGHASH $R/p4_merge.txt | awk '{print $2, $3}' > $R/p4_merge_hashes.txt
  hashcmp $R/p4_merge_hashes.txt $R/p4_stream_hashes.txt > $R/p4_hashcmp.txt; check P4_verifier_hashes_equal_accumulator $? "$(cat $R/p4_hashcmp.txt)"
  wall=$((t2 - t0)); log "P4 RESULT chunks $K wall_s $wall (including the kill and restart) chunks_per_hour $(python3 -c "print(round($K*3600/$wall,1))") usd_per_chunk $(python3 -c "print(f'{$PRICE*$wall/3600/$K:.6f}')")"
  cat run/stream_g*_w*/stream_log.txt > $R/p4_stream_log.txt; cat run/timing_*.txt > $R/p4_timing.txt; cd $B
  for h in 600000 6000; do D5=$WK/p4_$h; rm -rf $D5; mkdir -p $D5/ap; ln -s $WK/ap2243/ap_000000.bin $WK/ap2243/ap_000000.sha256 $D5/ap/
    cd $D5; t0=$(date +%s); timeout 1800 env ACC_SELECT=L$h-$((h + 2 * NC - 1)) ACC_TIMING_LOG=1 ACC_STREAM_CMD=$B/scripts/stream_seg.sh $BIN/acc2243v2 run "${SEED[@]}" $M $Q -1 $T $SG $D5/ap $NC run 1000000000 1000000 > $R/p4_mix_$h.txt 2>&1
    w=$(( $(date +%s) - t0 )); log "P4 MIX segments L$h-$((h + 2 * NC - 1)) wall_s $w chunks_per_hour $(python3 -c "print(round(2*$NC*3600/max($w,1),1))") usd_per_chunk $(python3 -c "print(f'{$PRICE*$w/3600/(2*$NC):.6f}')")"
    cat run/stream_g*_w*/stream_log.txt > $R/p4_mix_${h}_stream.txt; cat run/timing_*.txt > $R/p4_mix_${h}_timing.txt; cd $B; done
fi
log "pilot end"; echo "checks passed: $(grep -c ' PASS ' $R/checks.txt) failed: $(grep -c ' FAIL ' $R/checks.txt)" | tee -a $R/pilot.log; grep ' FAIL ' $R/checks.txt | tee -a $R/pilot.log
tar czf $B/pilot_results_$(hostname)_$(date -u +%Y%m%dT%H%MZ).tar.gz -C $B results logs
echo PILOT_DONE | tee -a $R/pilot.log
