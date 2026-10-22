#!/bin/bash
# F-i: the setup-time table (segment 0 -> a_p, p <= RT) is not bound into checkpoints; a shard with a divergent segment 0 pools silently
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
B="$R/acc_review"; CUR=(0 -22735 0 106272484 0); P=(27 2167729337579528 1 4831838207 16777216)
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap; BAD="$R/adv/apdir_bad0"
export ACC_SELECT="L50-69,S200-229"; D="$R/adv/rs"; OUTF="$R/adv_setup_table_results.txt"; : > "$OUTF"
rm -rf "$D/shD" "$D/poolAD"
ACC_SHARD=1/2 ACC_TAG=D "$B" run "${CUR[@]}" "${P[@]}" "$BAD" 1 "$D/shD" 500000000 5 > "$D/shD.out" 2>&1; echo "shard 1/2 tag D with corrupted segment 0 (a_5+2): run exit=$?" >> "$OUTF"
mkdir -p "$D/poolAD"; cp -p "$D"/shA/ckpt_*.bin "$D"/shD/ckpt_*.bin "$D/poolAD/"
"$B" merge "${CUR[@]}" "${P[@]}" "$AP" "$D/poolAD" 1024 > "$D/poolAD.merge" 2>&1; echo "merge pool A (good) + D (bad segment 0), good apdir at merge: exit=$?" >> "$OUTF"
grep -E 'FATAL|^MERGE|^FINGERPRINT|^COUNT_SELECTION|^AP_SEGROOT|^CHUNK_DIGEST' "$D/poolAD.merge" | sed 's/^/    /' >> "$OUTF"
echo "reference (all good) merge of the same selection:" >> "$OUTF"; grep -E '^AP_SEGROOT|^CHUNK_DIGEST' "$D/pool.merge" | sed 's/^/    /' >> "$OUTF"
# full-run count identity catches an S-block cnt change (m27 copy, re-hashed)
rm -rf "$R/adv/A13_full_Scnt"; mkdir -p "$R/adv/A13_full_Scnt"; cp -p "$R"/m27/ckpt_g*.bin "$R/adv/A13_full_Scnt/"
python3 - "$R/adv/A13_full_Scnt/ckpt_g001_w00.bin" <<'PY'
import sys, re, hashlib
fn = sys.argv[1]; b = open(fn,'rb').read()[:-70]
r = max(re.finditer(rb'\nU (\d+) fp ([0-9a-f]+) nterm (\d+) cnt (\d+) ', b), key=lambda r: int(r.group(1)))
new = b[:r.start(4)] + str(int(r.group(4)) + 1).encode() + b[r.end(4):]
open(fn,'wb').write(new + b'\nEND ' + hashlib.sha256(new).hexdigest().encode() + b'\n'); print('S unit', r.group(1).decode())
PY
unset ACC_SELECT
"$B" merge "${CUR[@]}" "${P[@]}" "$AP" "$R/adv/A13_full_Scnt" 1024 > "$R/adv/A13_full_Scnt.out" 2>&1; echo "full run, S-block cnt+1 (re-hashed): merge exit=$?" >> "$OUTF"
grep -E 'FATAL|^COUNT' "$R/adv/A13_full_Scnt.out" | sed 's/^/    /' >> "$OUTF"
echo done
