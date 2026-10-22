#!/bin/bash
# run_p3.sh -- PREPARED, NOT EXECUTED on the seed in the RIGOROUS_STREAM_CORE task (2026-09-19).
# p = 3 (depth 4: m = 81, plus the m = 27 U_3 cross-check) and optional p = 7 (m = 49, plus m = 7 T_7 cross-check) modular-symbol
# run for the seed with the rigorous core.  Refuses to start on the seed unless P3_AUTHORIZED=yes.  Every stage is restartable.
#   Stage W: per a_q segment (SEGQ = 2^24): apwit (producer) -> wverify wit (independent verifier) -> sha256 of the witness file;
#            witness file kept (KEEP_WIT=1, default if >= 60 GB free) or deleted after hashing.  Done markers per segment.
#   Stage A: arbcore msl per target m (T_m = least k*SEGQ - 1 >= TMIN_m, TMIN from `arbcore tmin` at LATDEN), W threads.
#   Stage C: p3_check.py: segment-root equality, count identities, all phi(m) symbols identified, Hecke/U_p relations exact.
# Parameters (env): AI N TARGETS="m:M:s ..." (Q = N/M; s = -eps_Q) LATDEN SEGQ J (witness processes) W (arbcore threads) OUT FAST.
set -euo pipefail
R=${R:-$HOME/BSD_RIGOROUS_STREAM_CORE_2026-09-19}; P=${P:-$HOME/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4}
export DYLD_LIBRARY_PATH=$P/Odarwin-x86_64
SEED_AI="0 -22735 0 106272484 0"
AI=${AI:-$SEED_AI}; N=${N:-6503188012738584}
TARGETS=${TARGETS:-"81:3:1 27:3:1"}          # seed: M = 3 -> s = -w a_3 = +1;  add "49:1:1 7:1:1" for p = 7 (M = 1 -> s = w = +1)
LATDEN=${LATDEN:-1024}; SEGQ=${SEGQ:-16777216}; QB=4096; J=${J:-12}; W=${W:-12}; OUT=${OUT:-$R/runs/p3}; FAST=${FAST-fast}   # FAST="" for curves without the seed-type 2-torsion point (0,0)
ZERO_SYMBOL=${ZERO_SYMBOL:-0}                 # [0]^+ = L(E,1)/Omega+ (= 0 for the seed: rank 2 => L(E,1) = 0, Kolyvagin); [0]^- = 0
if [ "$AI" = "$SEED_AI" ] && [ "${P3_AUTHORIZED:-no}" != "yes" ]; then
  echo "REFUSED: run_p3.sh on the seed needs P3_AUTHORIZED=yes (operator decision; see P3_RUN_PLAN.md)"; exit 2; fi
mkdir -p $OUT/wit $OUT/ap $OUT/logs $OUT/seg
stamp() { echo "$(date '+%Y-%m-%dT%H:%M:%S') $*" | tee -a $OUT/logs/timeline.log; }
trap 'stamp "FAILED at line $LINENO (exit $?); see $OUT/logs"' ERR
read -a A5 <<< "$AI"
# ---- truncation points (exact, Arb) ----
: > $OUT/targets.txt; TMAX=0
for tg in $TARGETS; do IFS=: read m M s <<< "$tg"; Q=$((N / M))
  tmin=$($R/src/arbcore tmin $AI $m $Q $LATDEN | awk '/^TMIN /{print $2}')
  T=$(( ((tmin + 1 + SEGQ - 1) / SEGQ) * SEGQ - 1 ))
  echo "$m $M $s $Q $tmin $T" >> $OUT/targets.txt; [ $T -gt $TMAX ] && TMAX=$T
done
NSEG=$(( (TMAX + 1) / SEGQ )); stamp "targets: $(tr '\n' ';' < $OUT/targets.txt) TMAX=$TMAX NSEG=$NSEG"
FREE=$(df -g $OUT | awk 'NR==2{print $4}'); KEEP_WIT=${KEEP_WIT:-$([ $FREE -ge 60 ] && echo 1 || echo 0)}
# ---- Stage W ----
cat > $OUT/seg.sh <<SEG
#!/bin/bash
set -euo pipefail
s=\$1; [ -f $OUT/seg/\$s.done ] && exit 0
$R/src/apwit $AI $TMAX $QB $SEGQ $OUT/wit \$s \$((s + 1)) $FAST > $OUT/logs/prod_\$s.log 2> $OUT/logs/prod_\$s.err
$R/verifier/wverify wit $AI $TMAX $QB $SEGQ $OUT/wit $OUT/ap \$s \$((s + 1)) > $OUT/logs/ver_\$s.log 2> $OUT/logs/ver_\$s.err
shasum -a 256 $OUT/wit/wit_\$(printf %06d \$s).bin > $OUT/logs/witsha_\$s.txt
[ "$KEEP_WIT" = 1 ] || rm -f $OUT/wit/wit_\$(printf %06d \$s).bin
touch $OUT/seg/\$s.done
SEG
chmod +x $OUT/seg.sh
stamp "stage W start (J=$J, KEEP_WIT=$KEEP_WIT)"
seq 0 $((NSEG - 1)) | xargs -P $J -n 1 $OUT/seg.sh
[ $(ls $OUT/seg | wc -l) -eq $NSEG ] || { stamp "stage W incomplete"; exit 3; }
stamp "stage W done"
# ---- Stage A ----
while read m M s Q tmin T; do
  if [ ! -s $OUT/msl_m$m.txt ]; then stamp "stage A m=$m T=$T start"
    /usr/bin/time -l $R/src/arbcore msl $AI $m $Q $s $T $SEGQ $OUT/ap $W $OUT/units_m$m $LATDEN > $OUT/msl_m$m.tmp 2> $OUT/logs/msl_m$m.err
    mv $OUT/msl_m$m.tmp $OUT/msl_m$m.txt; stamp "stage A m=$m done"; fi
done < $OUT/targets.txt
# ---- Stage C ----
python3 $R/p3plan/p3_check.py $OUT $SEGQ $LATDEN $ZERO_SYMBOL | tee $OUT/P3_CHECK.txt
stamp "ALL DONE"
