#!/bin/bash
set -euo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
SE=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env
want=295a14c2dc59451266463684e00a6df397c3a75ce197ec80142fccb6a068a730
got=$(shasum -a 256 "$R/src/acc2243v2.c" | awk '{print $1}')
[ "$got" = "$want" ] || { echo "SOURCE HASH MISMATCH $got"; exit 1; }
cc --version | head -2
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations -I"$SE/include" "$R/src/acc2243v2.c" -L"$SE/lib" -Wl,-rpath,"$SE/lib" -lflint -lmpfr -lgmp -lpthread -o "$R/acc_review"
shasum -a 256 "$R/acc_review" /Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline/acc2243v2
ls "$SE/lib" | grep -i -E 'flint|mpfr|gmp' | head
