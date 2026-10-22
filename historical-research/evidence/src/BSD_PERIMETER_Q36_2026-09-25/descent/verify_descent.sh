#!/bin/bash
# Replay the descent certificate and require every load-bearing line. Exit 0 only if all hold. About 10 s.
set -u
BIN=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin
cd "$(dirname "$0")"; T=$(mktemp -d); ok=1
need() { grep -qF -- "$2" "$1" || { echo "MISSING in $(basename "$1"): $2"; ok=0; }; }
"$BIN/gp" -q -D parisizemax=4000000000 < pari_descent.gp > "$T/pari.out" 2>&1
need "$T/pari.out" "ellrank(E) [r1,r2,s] = [2, 2, 0]"
need "$T/pari.out" "ellrank(E') [r1,r2,s] = [2, 2, 0]"
need "$T/pari.out" "torsion [2, [2]]"
need "$T/pari.out" "alpha(T)  = 26568121   alpha(P1) = 4547"
need "$T/pari.out" "alpha'(T') = 10198921"
need "$T/pari.out" "alpha'(E' point 1) = -2243"
echo "[0,-22735,0,106272484,0]" | "$BIN/mwrank" -q -v 1 -d -S 0 > "$T/m1.log" 2>&1
echo "[0,-22735,0,106272484,0]" | "$BIN/mwrank" -q -v 1 -S 0 > "$T/m2.log" 2>&1
for f in "$T/m1.log" "$T/m2.log"; do need "$f" "Rank = 2"; need "$f" "Rank of S^2(E)  = 3"; done
need "$T/m1.log" "III(E/Q)[2]    is trivial"
need "$T/m2.log" "#III(E/Q)[2]       = 1"
"$BIN/sage" saturation.sage > "$T/sat.out" 2>&1
need "$T/sat.out" "Points were proved 2-saturated"
need "$T/sat.out" "saturation index: 1"
need "$T/sat.out" "saturated points equal input: True"
rm -rf "$T"
[ $ok = 1 ] && echo "DESCENT_CERTIFICATE_REPLAY_PASS" || { echo "DESCENT_CERTIFICATE_REPLAY_FAIL"; exit 1; }
