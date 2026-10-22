#!/bin/bash
# stand-in for stream_seg.sh run with parameters that differ from the accumulator's (e.g. CURVE env for another curve): the
# "verifier" output has the right length (prime count does not depend on the curve) and its OWN consistent hash.
set -euo pipefail; s=$1; d=$2; S6=$(printf %06d "$s"); C=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
python3 -c "import sys,struct; b=bytearray(open(sys.argv[1],'rb').read()); v=struct.unpack_from('<i',b,400)[0]; struct.pack_into('<i',b,400,v+2); open(sys.argv[2],'wb').write(b)" "$C/ap_$S6.bin" "$d/ap_$S6.bin"
shasum -a 256 "$d/ap_$S6.bin" | awk '{print $1}' > "$d/ap_$S6.sha256"
