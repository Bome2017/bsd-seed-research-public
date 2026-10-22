#!/bin/bash
# stand-in: consumed bytes differ from the bytes the verifier hashed (one a_q changed after verification)
set -euo pipefail; s=$1; d=$2; S6=$(printf %06d "$s"); C=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
shasum -a 256 "$C/ap_$S6.bin" | awk '{print $1}' > "$d/ap_$S6.sha256"
python3 -c "import sys; b=bytearray(open(sys.argv[1],'rb').read()); b[400]^=1; open(sys.argv[2],'wb').write(b)" "$C/ap_$S6.bin" "$d/ap_$S6.bin"
