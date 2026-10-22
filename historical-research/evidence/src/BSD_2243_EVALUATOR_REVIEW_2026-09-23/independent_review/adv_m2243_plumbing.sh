#!/bin/bash
# plumbing only (NOT a certified case): m = 2243 (> 400: symbols.bin path, prime-length acb_dft), tiny T = 2^24 - 1, Q = Q/2243
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review; B="$R/acc_review"; AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
for S in 1 -1; do D="$R/adv/m2243_s$S"; rm -rf "$D"
  "$B" run 0 -22735 0 106272484 0 2243 966441969496 $S 16777215 16777216 "$AP" 1 "$D" 500000000 40 > "$D.run" 2>&1; echo "sign $S run exit $?"
  for P in 0 1; do ACC_DFT=$P /usr/bin/time -p "$B" merge 0 -22735 0 106272484 0 2243 966441969496 $S 16777215 16777216 "$AP" "$D" 1024 > "$D.merge$P" 2>&1; echo "  merge dft=$P exit $?"
    cp "$D/symbols.bin" "$D/symbols_dft$P.bin"; done
  cmp "$D/symbols_dft0.bin" "$D/symbols_dft1.bin" && echo "  symbols.bin identical direct vs DFT (sign $S)"
  grep -h -E 'SYMBOLS_FILE|SYMBOL_PASS|XB_PLUS|^user' "$D.merge0" "$D.merge1" | sed 's/^/    /'
done
