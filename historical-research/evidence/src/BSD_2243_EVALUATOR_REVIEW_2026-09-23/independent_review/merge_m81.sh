#!/bin/bash
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
C=(0 -22735 0 106272484 0 81 2167729337579528 1 14847836159 16777216 "$AP" "$R/m81" 1024)
ACC_DFT=0 /usr/bin/time -p "$R/acc_review" merge "${C[@]}" 3 4 2 -1 > "$R/m81_merge_direct.txt" 2> "$R/m81_merge_direct.err"; echo "direct exit $?"
ACC_DFT=1 /usr/bin/time -p "$R/acc_review" merge "${C[@]}" 3 4 2 -1 > "$R/m81_merge_dft.txt" 2> "$R/m81_merge_dft.err"; echo "dft exit $?"
for W in "3 4 1 -1" "3 4 6 -1" "3 4 7 -1"; do read -r -a WA <<< "$W"; tag=$(echo "$W" | tr ' ' '_')
  ACC_DFT=1 "$R/acc_review" merge "${C[@]}" "${WA[@]}" > "$R/m81_merge_w${tag}_dft1.txt" 2>&1; echo "weights $W exit $?"; done
