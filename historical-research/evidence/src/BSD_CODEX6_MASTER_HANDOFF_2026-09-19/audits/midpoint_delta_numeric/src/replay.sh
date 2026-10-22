#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
runtime=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations \
  -I"$runtime/include" src/delta.c -L"$runtime/lib" \
  -Wl,-rpath,"$runtime/lib" -lflint -lmpfr -lgmp -lpthread -o src/delta
# Regenerate the coefficient moments, checking both independently certified roots.
src/delta prep evidence/moments_replay.bin
src/delta eval evidence/moments_replay.bin 128 1 > evidence/replay.log
python3 src/extract_certificate.py replay.log
