#!/bin/bash
# restart / crash / shard / tag / lock tests on a selection (W <= 2; the m=81 run holds 3 threads)
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
B="$R/acc_review"; CUR=(0 -22735 0 106272484 0); P=(27 2167729337579528 1 4831838207 16777216 "$AP")
export ACC_SELECT="L50-69,S200-229"
OUTF="$R/adv_restart_results.txt"; : > "$OUTF"; D="$R/adv/rs"; rm -rf "$D"; mkdir -p "$D"
log() { echo "$*" >> "$OUTF"; }
mrg() { "$B" merge "${CUR[@]}" "${P[@]}" "$1" 1024 > "$1.merge" 2>&1; local ec=$?; log "  merge $(basename $1) exit=$ec"; grep -E 'FATAL|^MERGE|^FINGERPRINT|^COUNT_SELECTION|^CHUNK_DIGEST|^PARTIAL' "$1.merge" | sed 's/^/    /' >> "$OUTF"; }
# R1 reference (W=1) + concurrent second run in the same directory (flock)
( /usr/bin/time -p "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/ref" 500000000 5 > "$D/ref.out" 2>&1 ) &
sleep 1; "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/ref" 500000000 5 > "$D/ref_second.out" 2>&1; log "R1b second concurrent run in the same dir: exit=$? $(grep FATAL $D/ref_second.out)"
wait; log "R1 reference run: $(grep -E '^RUN|^user' $D/ref.out | tr '\n' ' ')"; mrg "$D/ref"
# R2 simulated crash after 13 units (checkpoint every 5 units, W=2), then restart
"$B" run "${CUR[@]}" "${P[@]}" 2 "$D/crash" 500000000 5 13 > "$D/crash1.out" 2>&1; log "R2 crash run exit=$? $(grep -E 'SIMULATED|^RUN units' $D/crash1.out | tr '\n' ' ') files: $(ls $D/crash | tr '\n' ' ')"
"$B" run "${CUR[@]}" "${P[@]}" 2 "$D/crash" 500000000 5 > "$D/crash2.out" 2>&1; log "R2 restart exit=$? $(grep -E '^RUN units' $D/crash2.out) files: $(ls $D/crash | tr '\n' ' ')"; mrg "$D/crash"
# R3 crash before the first checkpoint (CKPT_UNITS=40, die after 2 units), restart: which generation?
"$B" run "${CUR[@]}" "${P[@]}" 1 "$D/crash0" 500000000 40 2 > "$D/crash0_1.out" 2>&1; log "R3 crash-before-ckpt exit=$? $(grep -E 'SIMULATED|^RUN units' $D/crash0_1.out | tr '\n' ' ') files: $(ls $D/crash0 | tr '\n' ' ')"
"$B" run "${CUR[@]}" "${P[@]}" 1 "$D/crash0" 500000000 40 > "$D/crash0_2.out" 2>&1; log "R3 restart exit=$? $(grep -E '^RUN units' $D/crash0_2.out)"; mrg "$D/crash0"
# R4 shards 0/2 (tag A) and 1/2 (tag B) in separate dirs, pooled
ACC_SHARD=0/2 ACC_TAG=A "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/shA" 500000000 5 > "$D/shA.out" 2>&1; log "R4 shard 0/2 tag A exit=$?"
ACC_SHARD=1/2 ACC_TAG=B "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/shB" 500000000 5 > "$D/shB.out" 2>&1; log "R4 shard 1/2 tag B exit=$?"
mkdir -p "$D/pool"; cp -p "$D"/shA/ckpt_*.bin "$D"/shB/ckpt_*.bin "$D/pool/"; log "  pool: $(ls $D/pool | tr '\n' ' ')"; mrg "$D/pool"
mrg "$D/shA"
# R5 duplicate shard 0/2 under tag C pooled with A and B
ACC_SHARD=0/2 ACC_TAG=C "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/shC" 500000000 5 > "$D/shC.out" 2>&1; log "R5 duplicate shard 0/2 tag C exit=$?"
mkdir -p "$D/pooldup"; cp -p "$D"/shA/ckpt_*.bin "$D"/shB/ckpt_*.bin "$D"/shC/ckpt_*.bin "$D/pooldup/"; mrg "$D/pooldup"
# R6 untagged shards pooled by copy (name collision: second copy overwrites the first)
ACC_SHARD=0/2 "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/shU0" 500000000 5 > /dev/null 2>&1; ACC_SHARD=1/2 "$B" run "${CUR[@]}" "${P[@]}" 1 "$D/shU1" 500000000 5 > /dev/null 2>&1
mkdir -p "$D/poolU"; cp -p "$D"/shU0/ckpt_*.bin "$D/poolU/"; cp -p "$D"/shU1/ckpt_*.bin "$D/poolU/"; log "R6 untagged pool: $(ls $D/poolU | tr '\n' ' ')"; mrg "$D/poolU"
# R7 tampered counts in a selection (re-hashed): an L record cnt+1, then an S record cnt+1
mkdir -p "$D/cntL" "$D/cntS"; cp -p "$D"/ref/ckpt_*.bin "$D/cntL/"; cp -p "$D"/ref/ckpt_*.bin "$D/cntS/"
python3 - "$D/cntL/ckpt_g001_w00.bin" "$D/cntS/ckpt_g001_w00.bin" <<'PY'
import sys, re, hashlib
def edit(fn, pick):
    b = open(fn,'rb').read()[:-70]
    recs = list(re.finditer(rb'\nU (\d+) fp ([0-9a-f]+) nterm (\d+) cnt (\d+) ', b)); r = pick(recs)
    new = b[:r.start(4)] + str(int(r.group(4)) + 1).encode() + b[r.end(4):]
    open(fn,'wb').write(new + b'\nEND ' + hashlib.sha256(new).hexdigest().encode() + b'\n'); print(fn, 'unit', int(r.group(1)))
edit(sys.argv[1], lambda rs: min(rs, key=lambda r: int(r.group(1))))   # smallest u = an L sub-unit
edit(sys.argv[2], lambda rs: max(rs, key=lambda r: int(r.group(1))))   # largest u = an S block
PY
log "R7a L-unit cnt+1 (selection)"; mrg "$D/cntL"; log "R7b S-block cnt+1 (selection)"; mrg "$D/cntS"
echo done
