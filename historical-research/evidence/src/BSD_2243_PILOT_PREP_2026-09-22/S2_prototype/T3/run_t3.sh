#!/bin/bash
# T3: restart / recombination bit-identity on the seed at m = 27, T = 12*2^24-1, certified verified a_q of the p = 3 run.
set -u
P=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S2_prototype; cd $P/T3; rm -rf w1 w8 crash *.txt
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
C=(0 -22735 0 106272484 0 27 2167729337579528 1 201326591 16777216 $AP)
{ time $P/acc2243 run "${C[@]}" 1 w1 20000000 5 ; } > w1.run.txt 2>&1;  $P/acc2243 merge "${C[@]}" w1 1024 > w1.merge.txt
{ time $P/acc2243 run "${C[@]}" 8 w8 20000000 5 ; } > w8.run.txt 2>&1;  $P/acc2243 merge "${C[@]}" w8 1024 > w8.merge.txt
$P/acc2243 run "${C[@]}" 4 crash 20000000 5 23 > crash1.run.txt 2>&1; echo "crash run exit=$? (expect 9); ckpt files after crash: $(ls crash | grep -c ckpt_)"
$P/acc2243 run "${C[@]}" 3 crash 20000000 5 > crash2.run.txt 2>&1; echo "restart exit=$?"
$P/acc2243 merge "${C[@]}" crash 1024 > crash.merge.txt
