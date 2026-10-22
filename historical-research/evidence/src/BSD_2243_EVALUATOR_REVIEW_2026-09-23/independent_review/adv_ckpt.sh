#!/bin/bash
# adversarial checkpoint tests on COPIES of the reviewer's own m = 27 run (merge only; cheap)
set -uo pipefail
R=/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/independent_review
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
B="$R/acc_review"; TP="python3 $R/tools/tamper.py"
CUR=(0 -22735 0 106272484 0)
OUTF="$R/adv_ckpt_results.txt"; : > "$OUTF"
fresh() { rm -rf "$R/adv/$1"; mkdir -p "$R/adv/$1"; cp -p "$R"/m27/ckpt_g*.bin "$R/adv/$1/"; }
domerge() {  # case  m  T  [Q sign]  -> runs merge with (m, T, Q, sign) on adv/case
  local c=$1 m=$2 t=$3 q=${4:-2167729337579528} s=${5:-1}
  "$B" merge "${CUR[@]}" "$m" "$q" "$s" "$t" 16777216 "$AP" "$R/adv/$c" 1024 > "$R/adv/$c.out" 2>&1; local ec=$?
  { echo "=== $c  (merge m=$m T=$t Q=$q sign=$s)  exit=$ec"
    grep -E 'FATAL|^MERGE|^FINGERPRINT|^COUNT|^CHUNK_DIGEST|^XB_PLUS_DETERMINED' "$R/adv/$c.out" | sed 's/^/    /'
    grep -E '^XB (1|2) ' "$R/adv/$c.out" | sed 's/^/    /'; } >> "$OUTF"
}
W1="ckpt_g001_w01.bin"; W0="ckpt_g001_w00.bin"
# A0 control: untouched copy
fresh A0_control; domerge A0_control 27 4831838207
# A1 flip one byte in the array, trailer NOT fixed
fresh A1_flip_nofix; $TP flip "$R/adv/A1_flip_nofix/$W1" 27 5 3; domerge A1_flip_nofix 27 4831838207
# A2 flip low byte (bits 24..31) of entry 5, trailer recomputed
fresh A2_flip_low_rehash; $TP flip "$R/adv/A2_flip_low_rehash/$W1" 27 5 3 rehash; domerge A2_flip_low_rehash 27 4831838207
# A3 flip high byte (bits 64..71) of entry 5, trailer recomputed  -> fingerprint blind
fresh A3_flip_high_rehash; $TP flip "$R/adv/A3_flip_high_rehash/$W1" 27 5 8 rehash; domerge A3_flip_high_rehash 27 4831838207
# A3b flip bit 96 (byte 12) of entry 5, trailer recomputed -> class sum changes by 1.0
fresh A3b_flip_bit96_rehash; $TP flip "$R/adv/A3b_flip_bit96_rehash/$W1" 27 5 12 rehash; domerge A3b_flip_bit96_rehash 27 4831838207
# A3c add n*2^64 units to S_0 (n = round(Omega+/2 * 2^32)), trailer recomputed -> every plus symbol shifted by +1, still "identified"
fresh A3c_shift_plus_by_1; $TP add "$R/adv/A3c_shift_plus_by_1/$W1" 27 0 1110972999840677023210012672 rehash; domerge A3c_shift_plus_by_1 27 4831838207
# A4 delete one U record line (unit 8), fix trailer only (NREC unchanged)
fresh A4_delU_rehash; $TP delU "$R/adv/A4_delU_rehash/$W1" 8 rehash; domerge A4_delU_rehash 27 4831838207
# A5 delete one U record line (unit 8), decrement NREC, fix trailer
fresh A5_delU_fixnrec_rehash; $TP delU "$R/adv/A5_delU_fixnrec_rehash/$W1" 8 fixnrec rehash; domerge A5_delU_fixnrec_rehash 27 4831838207
# A6 duplicate a checkpoint under a new name that matches the ckpt_g*.bin filter
fresh A6_dup_ckpt; cp -p "$R/adv/A6_dup_ckpt/$W0" "$R/adv/A6_dup_ckpt/ckpt_g002_w00_tcopy.bin"; domerge A6_dup_ckpt 27 4831838207
# A6b duplicate under a name the filter ignores (.tmp) -> ignored
fresh A6b_dup_tmp; cp -p "$R/adv/A6b_dup_tmp/$W0" "$R/adv/A6b_dup_tmp/ckpt_g002_w00.bin.tmp"; domerge A6b_dup_tmp 27 4831838207
# A6c one checkpoint removed -> coverage
fresh A6c_missing_ckpt; rm "$R/adv/A6c_missing_ckpt/$W0"; domerge A6c_missing_ckpt 27 4831838207
# A6d truncated checkpoint (kill -9 without tmp+rename would look like this)
fresh A6d_truncated; head -c 20000 "$R/adv/A6d_truncated/$W1" > "$R/adv/A6d_truncated/x" && mv "$R/adv/A6d_truncated/x" "$R/adv/A6d_truncated/$W1"; domerge A6d_truncated 27 4831838207
# A7 merge with a different m / T / Q / sign on the same checkpoints
fresh A7_m81; domerge A7_m81 81 4831838207
fresh A7_T; domerge A7_T 27 4831838206
fresh A7_Q; domerge A7_Q 27 4831838207 2167729337579529 1
fresh A7_sign; domerge A7_sign 27 4831838207 2167729337579528 -1
# A8 move a U record (unit 8) from w01 to w00 (arrays untouched), both re-hashed -> global identities unchanged
fresh A8_move_record
python3 - "$R/adv/A8_move_record" <<'PY'
import sys, re, hashlib
d = sys.argv[1]; M = 27
def rd(fn): b = open(fn,'rb').read(); return b[:-70]
def wr(fn, body): open(fn,'wb').write(body + b'\nEND ' + hashlib.sha256(body).hexdigest().encode() + b'\n')
a = rd(d+'/ckpt_g001_w01.bin'); i = a.index(b'\nU 8 fp ')+1; j = a.index(b'\n', i)+1; line = a[i:j]; a = a[:i]+a[j:]
m = re.search(rb'\nNREC (\d+)\n', a); a = a[:m.start()] + b'\nNREC %d\n' % (int(m.group(1))-1) + a[m.end():]
b = rd(d+'/ckpt_g001_w00.bin'); k = b.index(b'\nERR ')+1; b = b[:k]+line+b[k:]
m = re.search(rb'\nNREC (\d+)\n', b); b = b[:m.start()] + b'\nNREC %d\n' % (int(m.group(1))+1) + b[m.end():]
wr(d+'/ckpt_g001_w01.bin', a); wr(d+'/ckpt_g001_w00.bin', b)
PY
domerge A8_move_record 27 4831838207
# A9 checkpoint of a different UNIT_TERMS pooled in (PARAMS text edited, re-hashed)
fresh A9_params_UT; python3 - "$R/adv/A9_params_UT/$W1" <<'PY'
import sys, hashlib
fn = sys.argv[1]; b = open(fn,'rb').read()[:-70]; b = b.replace(b'UT=500000000', b'UT=400000000', 1)
open(fn,'wb').write(b + b'\nEND ' + hashlib.sha256(b).hexdigest().encode() + b'\n')
PY
domerge A9_params_UT 27 4831838207
# A10 ACC_SELECT given at merge for a full run
fresh A10_select_at_merge; ACC_SELECT=L0 "$B" merge "${CUR[@]}" 27 2167729337579528 1 4831838207 16777216 "$AP" "$R/adv/A10_select_at_merge" 1024 > "$R/adv/A10_select_at_merge.out" 2>&1
echo "=== A10_select_at_merge exit=$?" >> "$OUTF"; grep FATAL "$R/adv/A10_select_at_merge.out" | sed 's/^/    /' >> "$OUTF"
# A11 run mode on the finished directory copy with a different UNIT_TERMS (must refuse before any work)
fresh A11_run_other_UT; "$B" run "${CUR[@]}" 27 2167729337579528 1 4831838207 16777216 "$AP" 1 "$R/adv/A11_run_other_UT" 400000000 40 > "$R/adv/A11_run_other_UT.out" 2>&1
echo "=== A11_run_other_UT (run, UNIT_TERMS 4e8 into a 5e8 directory) exit=$?" >> "$OUTF"; grep -E 'FATAL|^RUN' "$R/adv/A11_run_other_UT.out" | sed 's/^/    /' >> "$OUTF"
# A12 run mode on the finished directory copy with the same parameters: nothing left to do, no new checkpoint
fresh A12_run_complete; "$B" run "${CUR[@]}" 27 2167729337579528 1 4831838207 16777216 "$AP" 1 "$R/adv/A12_run_complete" 500000000 40 > "$R/adv/A12_run_complete.out" 2>&1
echo "=== A12_run_complete (rerun on a complete directory) exit=$?  files: $(ls "$R/adv/A12_run_complete" | tr '\n' ' ')" >> "$OUTF"; grep -E 'FATAL|^RUN' "$R/adv/A12_run_complete.out" | sed 's/^/    /' >> "$OUTF"
domerge A12_run_complete 27 4831838207
echo done
