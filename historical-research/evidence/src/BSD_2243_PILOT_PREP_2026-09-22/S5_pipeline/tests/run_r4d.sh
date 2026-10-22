#!/bin/bash
# R4d: restart FROM PARTIAL CHECKPOINTS (m = 27 selection). CKPT_UNITS = 1 so every finished unit is checkpointed; crash
# after 40 units; the restart must report already-done units > 0 in > 0 checkpoints, skip them, and reproduce the digest.
# A second crash in the restarted generation, then a third generation, exercises checkpoints of several generations.
set -u
P5=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline; AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
D=$P5/tests/small; cd $D; rm -rf r4d r4d_ref
C27=(0 -22735 0 106272484 0 27 2167729337579528 1 4831838207 16777216 $AP)
SELD="L0,L1-40,S0-199"
dig() { grep '^CHUNK_DIGEST' "$1" | awk '{print $2}'; }
ACC_SELECT=$SELD $P5/acc2243v2 run "${C27[@]}" 6 r4d_ref 500000000 50 > r4d_ref.txt 2>&1
ACC_SELECT=$SELD $P5/acc2243v2 run "${C27[@]}" 6 r4d 500000000 1 40 > r4d_1.txt 2>&1; echo "R4d gen1 exit $?"
ACC_SELECT=$SELD $P5/acc2243v2 run "${C27[@]}" 3 r4d 500000000 1 90 > r4d_2.txt 2>&1; echo "R4d gen2 exit $?: $(grep '^RUN units' r4d_2.txt)"
ACC_SELECT=$SELD $P5/acc2243v2 run "${C27[@]}" 5 r4d 500000000 1 > r4d_3.txt 2>&1; echo "R4d gen3 exit $?: $(grep '^RUN units' r4d_3.txt)"
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C27[@]}" r4d_ref 1024 > r4d_ref_merge.txt 2>&1
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C27[@]}" r4d 1024 > r4d_merge.txt 2>&1
g2=$(grep '^RUN units' r4d_2.txt | sed 's/.*already done \([0-9]*\) in \([0-9]*\) checkpoints.*/\1 \2/'); g3=$(grep '^RUN units' r4d_3.txt | sed 's/.*already done \([0-9]*\) in \([0-9]*\) checkpoints.*/\1 \2/')
set -- $g2 $g3
if [ "$1" -gt 0 ] && [ "$2" -gt 0 ] && [ "$3" -gt "$1" ] && [ -n "$(dig r4d_ref_merge.txt)" ] && [ "$(dig r4d_ref_merge.txt)" = "$(dig r4d_merge.txt)" ]; then
  echo "R4d PASS restart from partial checkpoints (gen2 resumed $1 units from $2 ckpts; gen3 resumed $3 units from $4 ckpts; $(ls r4d/ckpt_*.bin | wc -l | tr -d ' ') ckpt files, 3 generations) digest == reference $(dig r4d_merge.txt)"
else echo "R4d FAIL ($g2 / $g3)"; fi
