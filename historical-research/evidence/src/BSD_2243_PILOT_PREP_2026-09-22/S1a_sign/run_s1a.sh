#!/bin/bash
# S1a: engine symbols at M || N (M = 5, 7; split and non-split; w = +-1) with predicted sign s = -w*aM and the
# opposite sign (negative control). Uses the stream core binaries READ-ONLY; all outputs under this folder.
set -e
R=/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19; P=/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4
export DYLD_LIBRARY_PATH=$P/Odarwin-x86_64
D=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S1a_sign; SEGQ=8192; QB=4096; W=2
grep -v '^#' $D/curves_s1a.txt | while IFS='|' read lab ai N M aM w; do
  Q=$((N / M)); s=$(( -w * aM )); tmax=0
  for m in $M $((M*M)) $((M*M*M)); do
    t=$($R/src/arbcore tmin $ai $m $Q 500000000 | awk '$1=="TMIN"{print $2}'); [ $t -gt $tmax ] && tmax=$t; done
  T=$(( 4 * tmax )); [ $T -lt 20000 ] && T=20000
  d=$D/runs/${lab}_T$T; mkdir -p $d/wit $d/ap; nseg=$(( T / SEGQ + 1 ))
  if [ ! -s $d/ver.log ]; then
    $R/src/apwit $ai $T $QB $SEGQ $d/wit 0 $nseg > $d/prod.log 2> $d/prod.err
    $R/verifier/wverify wit $ai $T $QB $SEGQ $d/wit $d/ap 0 $nseg > $d/ver.log 2> $d/ver.err
  fi
  for m in $M $((M*M)) $((M*M*M)); do
    for sg in $s $(( -s )); do
      tag=m${m}_s$sg; [ -s $d/msl_$tag.txt ] || $R/src/arbcore msl $ai $m $Q $sg $T $SEGQ $d/ap $W $d/msl_$tag.units > $d/msl_$tag.txt 2> $d/msl_$tag.err
    done
  done
  echo "done $lab N=$N M=$M aM=$aM w=$w s_pred=$s T=$T"
done
