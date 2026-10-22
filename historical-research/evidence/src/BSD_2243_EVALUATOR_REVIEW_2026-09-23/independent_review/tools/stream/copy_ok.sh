#!/bin/bash
# stand-in stream command: a correct, verified segment (copied from the certified ap dir) with its correct hash
set -euo pipefail; s=$1; d=$2; S6=$(printf %06d "$s"); C=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
cp "$C/ap_$S6.bin" "$d/ap_$S6.bin.x"; shasum -a 256 "$d/ap_$S6.bin.x" | awk '{print $1}' > "$d/ap_$S6.sha256"; mv "$d/ap_$S6.bin.x" "$d/ap_$S6.bin"
