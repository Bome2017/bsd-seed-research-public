#!/bin/bash
# Full independent replay of the seed analytic-rank certificate in a FRESH directory:
#   producer (apwit) -> independent verifier (wverify wit) -> wverify an (a_n Merkle root) -> arbcore l2 -> compare with the certificate.
# usage: certificate/replay_seed_l2.sh <fresh-outdir> [J processes] [W threads]     (binaries from ./build.sh)
set -euo pipefail
R=$(cd "$(dirname "$0")/.." && pwd); P=${P:-$HOME/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4}
export DYLD_LIBRARY_PATH=$P/Odarwin-x86_64
D=${1:?usage: replay_seed_l2.sh <fresh-outdir> [J] [W]}; J=${2:-4}; W=${3:-4}
[ -e "$D" ] && { echo "REFUSED: $D exists (use a fresh directory)"; exit 2; }
mkdir -p $D/wit $D/ap
AI="0 -22735 0 106272484 0"; N=6503188012738584; T=150000000; QB=4096; SEGQ=16777216
printf '#!/bin/sh\n%s/src/apwit %s %s %s %s %s/wit $1 $(($1 + 1)) fast > %s/prod_$1.log\n' "$R" "$AI" $T $QB $SEGQ "$D" "$D" > $D/prod.sh
printf '#!/bin/sh\n%s/verifier/wverify wit %s %s %s %s %s/wit %s/ap $1 $(($1 + 1)) > %s/ver_$1.log\n' "$R" "$AI" $T $QB $SEGQ "$D" "$D" "$D" > $D/ver.sh
chmod +x $D/prod.sh $D/ver.sh
seq 0 8 | xargs -P $J -n 1 $D/prod.sh
seq 0 8 | xargs -P $J -n 1 $D/ver.sh
$R/verifier/wverify an $AI $T $SEGQ $D/ap > $D/an.log
$R/src/arbcore l2 $AI $N $T $SEGQ $D/ap $W $D/l2_units > $D/l2.txt
fail=0; chk() { if [ "$2" = "$3" ]; then echo "PASS $1"; else echo "FAIL $1: got '$2' want '$3'"; fail=1; fi; }
chk "verifier segments" "$(cat $D/ver_*.log | grep -c '^SEG ')" 9
chk "a_q verified" "$(cat $D/ver_*.log | awk '{s += $8} END {print s}')" 8444396
chk "a_q segment root" "$(cat $D/ver_*.log | sort -k2n | awk '{print $NF}' | xxd -r -p | shasum -a 256 | cut -d' ' -f1)" 916155fe549e9323e8cdc63ecdbc8c190b6cfe9c9c2e6f7554c6a6214d4617f6
chk "wverify an root" "$(awk '{print $2}' $D/an.log)" 8c0b71ccac2dd538d043ea34f4d4bbbf41459c72f7444371f43f7c58ded8cc94
chk "arbcore a_n root" "$(awk '/^AN_MERKLE/{print $2}' $D/l2.txt)" 8c0b71ccac2dd538d043ea34f4d4bbbf41459c72f7444371f43f7c58ded8cc94
chk "witness file root (producer determinism; not needed for soundness)" "$(for s in 0 1 2 3 4 5 6 7 8; do shasum -a 256 $D/wit/wit_00000$s.bin | cut -d' ' -f1; done | xxd -r -p | shasum -a 256 | cut -d' ' -f1)" 47f1cb431fdf9e56427ce2aaab881bd61ee7e33f34ba8e16561cc63992b49ecd
chk "L2HALF_DUMP (exact ball)" "$(grep '^L2HALF_DUMP' $D/l2.txt | cut -d' ' -f2-)" "8fbdc2e36e453517571bc5e5f9400837 -7a 17625463 -24"
chk "L2HALF_INTERVAL" "$(grep '^L2HALF_INTERVAL' $D/l2.txt | cut -d' ' -f2-)" "[35929604, 35941023] / 1000000"
chk "ZERO_EXCLUDED" "$(awk '/^ZERO_EXCLUDED/{print $2}' $D/l2.txt)" 1
[ $fail = 0 ] && echo REPLAY_PASS || { echo REPLAY_FAIL; exit 1; }
