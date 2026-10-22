#!/bin/bash
# stand-in: partially written segment (first half) with the full file's hash
set -euo pipefail; s=$1; d=$2; S6=$(printf %06d "$s"); C=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
shasum -a 256 "$C/ap_$S6.bin" | awk '{print $1}' > "$d/ap_$S6.sha256"; n=$(stat -f %z "$C/ap_$S6.bin"); head -c $((n / 2)) "$C/ap_$S6.bin" > "$d/ap_$S6.bin"
