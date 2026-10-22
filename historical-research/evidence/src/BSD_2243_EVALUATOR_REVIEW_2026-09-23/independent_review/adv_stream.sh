#!/bin/bash
# streaming fail-closed tests (W = 1, one selected unit each)
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
B="$R/acc_review"; CUR=(0 -22735 0 106272484 0); P=(27 2167729337579528 1 4831838207 16777216)
OUTF="$R/adv_stream_results.txt"; : > "$OUTF"
t() {  # name cmd apdir select UT
  local n=$1 cmd=$2 ap=$3 sel=$4 ut=${5:-500000000} od="$R/adv/stream_$1"; rm -rf "$od"
  if [ -n "$cmd" ]; then ACC_SELECT=$sel ACC_STREAM_CMD=$cmd /usr/bin/time -p "$B" run "${CUR[@]}" "${P[@]}" "$ap" 1 "$od" "$ut" 40 > "$od.out" 2>&1; else ACC_SELECT=$sel /usr/bin/time -p "$B" run "${CUR[@]}" "${P[@]}" "$ap" 1 "$od" "$ut" 40 > "$od.out" 2>&1; fi
  local ec=$?
  { echo "=== $n  (select $sel, UT $ut, stream cmd: ${cmd:-none}, apdir $(basename $ap))  exit=$ec"
    grep -E 'FATAL|^RUN|^user' "$od.out" | sed 's/^/    /'
    echo "    files: $(cd "$od" 2>/dev/null && find . -type f | sort | tr '\n' ' ')"
    for c in "$od"/ckpt_*.bin; do [ -f "$c" ] && grep -a '^U ' "$c" | sed 's/^/    record: /'; done; } >> "$OUTF"
}
t S1_fail "$R/tools/stream/fail.sh" "$R/adv/apdir_s" L100
t S2_tampered "$R/tools/stream/tampered.sh" "$R/adv/apdir_s" L100
t S3_nohash "$R/tools/stream/nohash.sh" "$R/adv/apdir_s" L100
t S4_partial "$R/tools/stream/partial.sh" "$R/adv/apdir_s" L100
t S5_wrongparams "$R/tools/stream/wrongparams.sh" "$R/adv/apdir_s" L100
t S6_copy_ok "$R/tools/stream/copy_ok.sh" "$R/adv/apdir_s" L100
t S7_multi_absent "$R/tools/stream/copy_ok.sh" "$R/adv/apdir_s" L1 100000000
t S8_notexec "$R/tools/stream/README_not_executable" "$R/adv/apdir_s" L100
t S9_pre_badsha "" "$R/adv/apdir_pre" L101
t S10_pre_goodsha "" "$R/adv/apdir_pre_ok" L101
t S11_absent_nostream "" "$R/adv/apdir_s" L100
t S12_select_nothing "" "$R/adv/apdir_pre_ok" S99999
t S13_real_stream_seg "$R/tools/stream/real.sh" "$R/adv/apdir_s" L100
echo "=== full-run records for comparison (u 105 = segment 100, u 106 = segment 101)" >> "$OUTF"
grep -a -h '^U 105 \|^U 106 ' "$R"/m27/ckpt_g001_w0*.bin | sed 's/^/    /' >> "$OUTF"
echo done
