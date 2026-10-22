#!/bin/bash
# independent replay, m = 81, W = 3 (leaves one slot of the coordinator's 4 for W=1 adversarial runs), own binary
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
CURVE=(0 -22735 0 106272484 0)
ARGS=(81 2167729337579528 1 14847836159 16777216 "$AP")
echo "START $(date '+%F %T')" > "$R/m81_run.log"
/usr/bin/time -l "$R/acc_review" run "${CURVE[@]}" "${ARGS[@]}" 3 "$R/m81" 500000000 40 >> "$R/m81_run.log" 2> "$R/m81_run.time"
echo "EXIT $? $(date '+%F %T')" >> "$R/m81_run.log"
