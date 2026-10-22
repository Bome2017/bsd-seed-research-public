#!/bin/bash
set -e
S1=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S1a_sign; P=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S2_prototype
grep -v '^#' $S1/curves_s1a.txt | while IFS='|' read lab ai N M aM w; do
  Q=$((N / M)); s=$(( -w * aM )); d=$(ls -d $S1/runs/${lab}_T* | head -1); T=${d##*_T}
  for m in $((M*M)) $((M*M*M)); do
    o=$P/T1/${lab}_m$m; rm -rf $o
    $P/acc2243 run $ai $m $Q $s $T 8192 $d/ap 2 $o 2000 3 > $o.run.txt
    $P/acc2243 merge $ai $m $Q $s $T 8192 $d/ap $o 1024 > $o.merge.txt
  done
  echo "done $lab"
done
