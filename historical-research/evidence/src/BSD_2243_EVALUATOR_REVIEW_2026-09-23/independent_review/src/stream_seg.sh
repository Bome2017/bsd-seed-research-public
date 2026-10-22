#!/bin/bash
# stream_seg.sh <segment> <dir> -- produce (untrusted fast producer) and verify (independent wverify) ONE a_q segment of the
# 2243 run, leaving <dir>/ap_<segment>.bin and <dir>/ap_<segment>.sha256 (the VERIFIER's own hash, which the accumulator
# compares with the hash of the bytes it consumes) in place only if the verifier exits 0 and prints its SEG line (fail
# closed: the verifier opens its output before checking, so it writes into a scratch directory and the files are renamed).
# Appends one line per segment to <dir>/stream_log.txt: segment, producer user s, verifier user s, primes, witnesses, ap_sha256.
# Environment: PRODUCER, VERIFIER (paths), T_RUN (run truncation), optional CURVE (default: the seed minimal model).
set -euo pipefail
s=$1; d=$2; S6=$(printf %06d "$s")
: "${PRODUCER:?}" "${VERIFIER:?}" "${T_RUN:?}"
read -r -a AI <<< "${CURVE:-0 -22735 0 106272484 0}"
SEGQ=16777216; QB=4096
mkdir -p "$d"; rm -rf "$d/wit" "$d/ap.tmp"; mkdir -p "$d/wit" "$d/ap.tmp"
/usr/bin/time -p "$PRODUCER" "${AI[@]}" "$T_RUN" $QB $SEGQ "$d/wit" "$s" $((s + 1)) fast > "$d/prod.log" 2> "$d/prod.time"
/usr/bin/time -p "$VERIFIER" wit "${AI[@]}" "$T_RUN" $QB $SEGQ "$d/wit" "$d/ap.tmp" "$s" $((s + 1)) > "$d/ver.log" 2> "$d/ver.time"
line=$(grep "^SEG $s " "$d/ver.log")                     # absent => grep fails => set -e aborts (fail closed)
h=$(echo "$line" | grep -o 'ap_sha256 [0-9a-f]*' | awk '{print $2}'); [ ${#h} -eq 64 ]
echo "$h" > "$d/ap.tmp/ap_$S6.sha256"                      # the VERIFIER's hash; the accumulator re-hashes what it consumes
mv "$d/ap.tmp/ap_$S6.sha256" "$d/ap_$S6.sha256"; mv "$d/ap.tmp/ap_$S6.bin" "$d/ap_$S6.bin"
pu=$(awk '/^user/{print $2}' "$d/prod.time"); vu=$(awk '/^user/{print $2}' "$d/ver.time")
echo "STREAM seg $s prod_user $pu ver_user $vu $(echo "$line" | grep -o 'primes [0-9]* witnesses [0-9]* ap_sha256 [0-9a-f]*')" >> "$d/stream_log.txt"
rm -rf "$d/wit" "$d/ap.tmp"
