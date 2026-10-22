#!/bin/bash
# real producer, then XOR one byte of a witness record (always a change); the verifier must reject the segment
/Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/producer_variant/apwit_v "$@" || exit $?
w=$(ls "${9}"/wit_*.bin | head -1)
python3 -c "import sys; f=open(sys.argv[1],'r+b'); f.seek(100); b=f.read(1); f.seek(100); f.write(bytes([b[0]^0xFF])); f.close()" "$w"
