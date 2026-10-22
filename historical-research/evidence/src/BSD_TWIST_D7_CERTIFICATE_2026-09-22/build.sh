#!/bin/bash
set -euo pipefail
R=$(cd "$(dirname "$0")" && pwd)
DEPS=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations \
  -I"$DEPS/include" "$R/central7.c" \
  -L"$DEPS/lib" -Wl,-rpath,"$DEPS/lib" \
  -lflint -lmpfr -lgmp -lpthread -o "$R/central7"
