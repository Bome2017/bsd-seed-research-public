#!/bin/bash
# S3b: loaded-host scaling of the producer and verifier at the top of the 2243 range (q ~ 3.912e13).
# c concurrent producers on distinct segments (c = 10 physical cores, c = 20 with SMT), then c concurrent verifiers.
# Every produced segment must verify (ap_sha256 printed); timings are per-process user time and batch wall time.
set -u
F=/Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22; R=/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19
PARI=/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4; export DYLD_LIBRARY_PATH=$PARI/Odarwin-x86_64
D=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S3_bench/conc; cd $D; mkdir -p wit ap logs
T=39119887532031; SEGQ=16777216; AI=(0 -22735 0 106272484 0)
batch() { local c=$1 s0=$2; local t0=$(date +%s)
  for ((i=0;i<c;i++)); do s=$((s0+i)); /usr/bin/time -p $F/producer_variant/apwit_v "${AI[@]}" $T 4096 $SEGQ wit $s $((s+1)) fast > logs/prod_c${c}_$s.log 2> logs/prod_c${c}_$s.time & done; wait
  local t1=$(date +%s)
  for ((i=0;i<c;i++)); do s=$((s0+i)); /usr/bin/time -p $R/verifier/wverify wit "${AI[@]}" $T 4096 $SEGQ wit ap $s $((s+1)) > logs/ver_c${c}_$s.log 2> logs/ver_c${c}_$s.time & done; wait
  local t2=$(date +%s); rm -f wit/wit_*.bin
  echo "BATCH c $c segs $s0..$((s0+c-1)) produce_wall $((t1-t0)) verify_wall $((t2-t1))"; }
uptime
batch 10 2331715
batch 20 2331695
echo S3B_DONE
