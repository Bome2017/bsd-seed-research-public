#!/bin/bash
# stand-in: segment delivered without the verifier's .sha256 companion
set -euo pipefail; s=$1; d=$2; S6=$(printf %06d "$s"); C=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
cp "$C/ap_$S6.bin" "$d/ap_$S6.bin"
