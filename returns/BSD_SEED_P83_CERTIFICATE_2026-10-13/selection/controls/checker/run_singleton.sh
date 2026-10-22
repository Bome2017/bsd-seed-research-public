#!/bin/bash
# run_singleton.sh: launcher for one singleton Ota witness (SINGLETON_SPEC v1.1; audit findings F3 and F6).
# usage: run_singleton.sh "a1 a2 a3 a4 a6" N p l T APDIR RECEIPTS_GLOB OUTDIR [W] [PINNED_SEGROOT]
#   env: SEGQ (default 16777216), SIGN (default 1), LATDEN (default 1024)
# - Never runs Stage W. Coefficients are READ from APDIR; only OUTDIR is written. After the run it checks that no file
#   under APDIR (links followed) was modified.
# - Refuses an existing OUTDIR, so stale outputs are never reused.
# - On the seed curve it refuses unless SINGLETON_AUTHORIZED=yes.
# - Writes OUTDIR/RUN_MANIFEST.json (engine hash, parameters, output hash, receipts, times). It then runs the
#   acceptance checker, whose verdict is the only certificate: NONZERO=0, INCONCLUSIVE_ZERO=3, INVALID=2.
set -euo pipefail
CURVE=$1; N=$2; P=$3; L=$4; T=$5; APDIR=$6; RECEIPTS=$7; OUT=$8; W=${9:-8}; PIN=${10:-}
SEGQ=${SEGQ:-16777216}; SIGN=${SIGN:-1}; LATDEN=${LATDEN:-1024}
C=${C:-$HOME/BSD_RIGOROUS_STREAM_CORE_2026-09-19}
PARI=${PARI:-$HOME/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4}
HERE=$(cd "$(dirname "$0")" && pwd)
export DYLD_LIBRARY_PATH=$PARI/Odarwin-x86_64
if [ "$CURVE" = "0 -22735 0 106272484 0" ] && [ "${SINGLETON_AUTHORIZED:-no}" != yes ]; then
  echo "REFUSED: a seed run needs SINGLETON_AUTHORIZED=yes"; exit 2; fi
[ -e "$OUT" ] && { echo "REFUSED: $OUT already exists (no reuse of stale outputs)"; exit 2; }
mkdir -p "$OUT/units" "$OUT/logs"; touch "$OUT/logs/start_marker"
read -r a1 a2 a3 a4 a6 <<< "$CURVE"
START=$(date -u +%Y-%m-%dT%H:%M:%SZ)
/usr/bin/time -l "$C/src/arbcore" msl $a1 $a2 $a3 $a4 $a6 "$L" "$N" "$SIGN" "$T" "$SEGQ" "$APDIR" "$W" "$OUT/units" "$LATDEN" \
  > "$OUT/msl.txt" 2> "$OUT/logs/msl.err"
END=$(date -u +%Y-%m-%dT%H:%M:%SZ)
CHANGED=$(find -L "$APDIR" -type f -newer "$OUT/logs/start_marker" | head -5)
[ -z "$CHANGED" ] || { echo "INVALID: coefficient files changed during the run: $CHANGED"; exit 2; }
python3 - "$OUT" "$C/src/arbcore" "$START" "$END" "$CURVE" "$N" "$P" "$L" "$T" "$SEGQ" "$SIGN" "$LATDEN" "$APDIR" "$RECEIPTS" "$W" "$PIN" <<'PY'
import hashlib, json, sys
out, arb, start, end, curve, N, p, l, T, segq, sign, lat, apdir, receipts, W, pin = sys.argv[1:17]
sha = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()
json.dump({'curve': curve, 'N': int(N), 'p': int(p), 'l': int(l), 'Q': int(N), 'sign': int(sign), 'T': int(T), 'SEGQ': int(segq),
           'LATDEN': int(lat), 'apdir': apdir, 'receipts_glob': receipts, 'pinned_segroot': pin or None, 'threads': int(W),
           'arbcore_path': arb, 'arbcore_sha256': sha(arb), 'msl_output_sha256': sha(f'{out}/msl.txt'),
           'params': open(f'{out}/units/PARAMS').read().strip(), 'start_utc': start, 'end_utc': end,
           'stage_W_run': False}, open(f'{out}/RUN_MANIFEST.json', 'w'), indent=1)
PY
set +e
python3 "$HERE/singleton_check.py" --msl "$OUT/msl.txt" --units "$OUT/units" --manifest "$OUT/RUN_MANIFEST.json" \
  --receipts "$RECEIPTS" --arbcore "$C/src/arbcore" --curve "$CURVE" --N "$N" --p "$P" --l "$L" --Q "$N" --sign "$SIGN" \
  --T "$T" --segq "$SEGQ" --latden "$LATDEN" --apdir "$APDIR" ${PIN:+--pinned-segroot "$PIN"} --out "$OUT/SINGLETON_REPORT.json" \
  > "$OUT/logs/check.log"
CODE=$?; tail -n 25 "$OUT/logs/check.log" | grep -E '"verdict"|"c2_mod_p"|"reasons"' ; exit $CODE
