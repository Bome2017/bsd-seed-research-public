#!/bin/bash
# T2: retained certified seed cases (p = 3 run): m = 27 and m = 81 with the certified verified a_q; W = 12.
set -u
P=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S2_prototype; cd $P/T2
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
for spec in "27 4831838207" "81 14847836159"; do
  set -- $spec; m=$1; T=$2; C=(0 -22735 0 106272484 0 $m 2167729337579528 1 $T 16777216 $AP)
  { time $P/acc2243 run "${C[@]}" 12 run_m$m 500000000 40 ; } > run_m$m.txt 2>&1
  if [ $m = 81 ]; then $P/acc2243 merge "${C[@]}" run_m$m 1024 3 4 2 -1 > merge_m$m.txt 2>&1; else $P/acc2243 merge "${C[@]}" run_m$m 1024 > merge_m$m.txt 2>&1; fi
  echo "m=$m done: $(grep -E '^(MERGE|FINGERPRINT|COUNT|XB_PLUS_DETERMINED|A_EXACT|A_MOD_P)' merge_m$m.txt | tr '\n' ' ')"
done
