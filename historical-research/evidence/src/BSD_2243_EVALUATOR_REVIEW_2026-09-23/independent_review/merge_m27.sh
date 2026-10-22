#!/bin/bash
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
C=(0 -22735 0 106272484 0 27 2167729337579528 1 4831838207 16777216 "$AP" "$R/m27" 1024)
ACC_DFT=0 /usr/bin/time -p "$R/acc_review" merge "${C[@]}" > "$R/m27_merge_direct.txt" 2> "$R/m27_merge_direct.err"; echo "direct exit $?"
ACC_DFT=1 /usr/bin/time -p "$R/acc_review" merge "${C[@]}" > "$R/m27_merge_dft.txt" 2> "$R/m27_merge_dft.err"; echo "dft exit $?"
# weights: n = 3 at m = 27 (p = 3, alpha = -1): r = 2 (A = 3262464, 3 | A), r = 6 and 7 (units), r = 1 alpha = +1 (sign), alpha = 2 (not validated)
for W in "3 3 2 -1" "3 3 6 -1" "3 3 7 -1" "3 3 1 1" "3 3 1 -1" "3 3 1 2"; do
  read -r -a WA <<< "$W"; tag=$(echo "$W" | tr ' ' '_')
  for D in 0 1; do ACC_DFT=$D "$R/acc_review" merge "${C[@]}" "${WA[@]}" > "$R/m27_merge_w${tag}_dft$D.txt" 2>&1; echo "weights $W dft $D exit $?"; done
done
