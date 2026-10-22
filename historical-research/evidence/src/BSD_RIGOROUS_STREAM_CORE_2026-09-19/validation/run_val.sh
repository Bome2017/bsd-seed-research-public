#!/bin/bash
# Validation runner (rigorous core): producer -> verifier (wit, an) -> arbcore ms / msl / l2.  Outputs under runs/val/.
# Curves and signs: validation/curves.txt.  T per curve = max(4 * max_m TMIN(2 tail/Omega+ <= 1e-9), 20000); l2: T = ceil(40 sqrt(N)/(2 pi)).
set -e
R=~/BSD_RIGOROUS_STREAM_CORE_2026-09-19; P=~/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4
export DYLD_LIBRARY_PATH=$P/Odarwin-x86_64
SEGQ=8192; QB=4096; W=2
prep() {  # label "ainvs" T  -> prints run dir; producer (PARI trace, no fast path) + verifier + wverify an
  local d=$R/runs/val/$1_T$3; mkdir -p $d/wit $d/ap; local nseg=$(( $3 / SEGQ + 1 ))
  if [ ! -s $d/an.log ]; then
    $R/src/apwit $2 $3 $QB $SEGQ $d/wit 0 $nseg > $d/prod.log 2> $d/prod.err
    $R/verifier/wverify wit $2 $3 $QB $SEGQ $d/wit $d/ap 0 $nseg > $d/ver.log 2> $d/ver.err
    $R/verifier/wverify an $2 $3 $SEGQ $d/ap > $d/an.log 2>> $d/ver.err
  fi
  echo $d
}
grep -v '^#' $R/validation/curves.txt | while IFS='|' read lab ai N M ms s; do
  Q=$((N / M)); tmax=0
  for m in $ms; do t=$(awk -v l=$lab -v m=$m '$1==l && $2==m {print $4}' $R/validation/tmin_validation.txt); [ $t -gt $tmax ] && tmax=$t; done
  T=$(( 4 * tmax )); [ $T -lt 20000 ] && T=20000
  d=$(prep $lab "$ai" $T)
  for m in $ms; do
    for mode in ms msl; do
      [ -s $d/${mode}_m$m.txt ] || $R/src/arbcore $mode $ai $m $Q $s $T $SEGQ $d/ap $W $d/${mode}_m$m.units > $d/${mode}_m$m.txt 2> $d/${mode}_m$m.err
    done
  done
  echo "done $lab T=$T"
done
for spec in "389a1|0 1 1 -2 0|389" "446d1|1 -1 0 -4 4|446" "234446a1|1 -1 0 -79 289|234446"; do
  IFS='|' read lab ai N <<< "$spec"
  T=$(python3 -c "import math; print(math.ceil(40*math.sqrt($N)/(2*math.pi)))")
  d=$(prep $lab "$ai" $T)
  [ -s $d/l2.txt ] || $R/src/arbcore l2 $ai $N $T $SEGQ $d/ap $W $d/l2.units > $d/l2.txt 2> $d/l2.err
  echo "done l2 $lab T=$T"
done
