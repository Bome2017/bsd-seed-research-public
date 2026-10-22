#!/bin/bash
set -euo pipefail
TWIST_ROOT=$(cd "$(dirname "$0")" && pwd)
TWIST_DEPS=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations \
  -I"$TWIST_DEPS/include" "$TWIST_ROOT/twist.c" \
  -L"$TWIST_DEPS/lib" -Wl,-rpath,"$TWIST_DEPS/lib" \
  -lflint -lmpfr -lgmp -lpthread -o "$TWIST_ROOT/twist"
