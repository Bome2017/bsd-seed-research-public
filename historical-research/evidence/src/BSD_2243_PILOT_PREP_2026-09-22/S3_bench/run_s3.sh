#!/bin/bash
# S3: complete-path benchmark for p = 2243 at representative heights (per-symbol T_min route). Single-threaded timings.
# Components: production (fixed untrusted producer), verification (independent verifier), engine traversal / kernel /
# fixed-point summation (profile levels 0/1/2), checkpoint write, final DFT. Nothing here is a certificate run.
set -u
F=/Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22; P=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S2_prototype
R=/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19; PARI=/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4
export DYLD_LIBRARY_PATH=$PARI/Odarwin-x86_64
D=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S3_bench; mkdir -p $D/wit $D/ap $D/logs; cd $D
SEGQ=16777216; TMIN=39119884424954; K=$(( (TMIN + SEGQ) / SEGQ )); T=$(( K * SEGQ - 1 ))
AI=(0 -22735 0 106272484 0); M=5031049; Q=2899325908488; S=-1; BLK=4194304
echo "T_run $T (least k*2^24-1 >= T_min $TMIN)" | tee logs/params.txt
for s in 0 59 5960 596046; do
  /usr/bin/time -p $F/producer_variant/apwit_v "${AI[@]}" $T 4096 $SEGQ wit $s $((s+1)) fast > logs/prod_$s.log 2> logs/prod_$s.time
  /usr/bin/time -p $R/verifier/wverify wit "${AI[@]}" $T 4096 $SEGQ wit ap $s $((s+1)) > logs/ver_$s.log 2> logs/ver_$s.time
  rm -f wit/wit_*.bin
  echo "seg $s: $(grep SEG logs/prod_$s.log | tail -1) | verifier $(grep -E '^user' logs/ver_$s.time)"
done
cp $F/measure/ap/ap_2331725.bin ap/
C=("${AI[@]}" $M $Q $S $T $SEGQ $D/ap)
BTOP=$(( (T - BLK) / BLK ))
for lvl in 0 1 2; do
  for seg in 0 59 5960 596046 2331725; do
    ACC_PROFILE=$lvl $P/acc2243_prof unit "${C[@]}" 100000000 L $seg 0 > logs/unitL_${seg}_p$lvl.txt 2>&1; echo "p$lvl $(cat logs/unitL_${seg}_p$lvl.txt)"
  done
  for b in 2384 238418 $BTOP; do
    ACC_PROFILE=$lvl $P/acc2243_prof unit "${C[@]}" 100000000 S $b > logs/unitS_${b}_p$lvl.txt 2>&1; echo "p$lvl $(cat logs/unitS_${b}_p$lvl.txt)"
  done
done
ACC_CKPT_BENCH=$D/ckpt_bench ACC_PROFILE=2 $P/acc2243_prof unit "${C[@]}" 100000000 L 2331725 0 > logs/ckpt_bench.txt 2>&1; cat logs/ckpt_bench.txt; rm -rf $D/ckpt_bench
$P/acc2243_prof dftbench $M > logs/dftbench.txt 2>&1; cat logs/dftbench.txt
echo S3_DONE
