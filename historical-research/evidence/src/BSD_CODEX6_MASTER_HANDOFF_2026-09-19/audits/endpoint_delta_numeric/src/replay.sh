#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
runtime=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations \
  -I"$runtime/include" src/delta.c -L"$runtime/lib" \
  -Wl,-rpath,"$runtime/lib" -lflint -lmpfr -lgmp -lpthread -o src/delta
python3 - <<'PY'
from pathlib import Path
import hashlib
for line in Path('evidence/retained_inputs.txt').read_text().splitlines():
    digest,path=line.split('  ',1)
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,path
PY
moments=/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/midpoint_delta_numeric/evidence/moments.bin
python3 src/run_bounded.py replay128 src/delta eval "$moments" 128 1
python3 src/extract_certificate.py replay128.log
