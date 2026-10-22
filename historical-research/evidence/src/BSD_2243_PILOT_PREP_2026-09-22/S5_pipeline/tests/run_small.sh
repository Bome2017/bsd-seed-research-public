#!/bin/bash
# S5 small-m tests (retained certified seed cases, m = 27 / 81). Nothing here is a certificate run.
#  R1  v2 merge (direct symbols) of the S2 checkpoints == S2 merge, both SHA builds
#  R2  DFT symbol path == direct path (candidates/flags identical, balls overlap)
#  R3  fresh full v2 run (shim build) == S2 merge; CHUNK_DIGEST recorded
#  R4a full coverage by two shards (tags A/B), shard B crashed + restarted, pooled merge == R3 digest
#  R4b selection: crash/restart digest identity; negative controls (wrong selection, missing, duplicated, corrupted checkpoint)
#  R4c streaming a_q (produce -> verify -> consume -> delete) == certified a_q for the same selection; fail-closed controls
set -u
P5=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline; T2=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S2_prototype/T2
AP=/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap
F=/Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22; R=/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19
export DYLD_LIBRARY_PATH=/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4/Odarwin-x86_64
D=$P5/tests/small; rm -rf $D; mkdir -p $D; cd $D
key() { grep -E '^(FINGERPRINT|COUNT |AP_SEGROOT|ROUNDING_ERR_TOTAL|TAIL_MS|S |OMEGA|XB |WEIGHTS|A_EXACT|A_MOD_P|NONZERO_ONLY)' "$1"; }
dig() { grep '^CHUNK_DIGEST' "$1" | awk '{print $2}'; }
keyx() { grep -E '^(FINGERPRINT|COUNT |AP_SEGROOT|ROUNDING_ERR_TOTAL|TAIL_MS|S |OMEGA|WEIGHTS|A_EXACT|A_MOD_P)' "$1"; }   # all but symbol radii
vs_s2() { diff <(keyx "$1") <(keyx "$2") > /dev/null && python3 $P5/tests/compare_dft.py "$1" "$2" 1.0 | grep -q '^CMP PASS'; }
expect_fatal() { local label=$1 pat=$2; shift 2; local out; out=$("$@" 2>&1); if [ $? -ne 0 ] && echo "$out" | grep -q "$pat"; then echo "NEG $label PASS (refused: $(echo "$out" | grep FATAL | head -1))"; else echo "NEG $label FAIL"; echo "$out" | tail -3; fi; }
T27=4831838207; C27=(0 -22735 0 106272484 0 27 2167729337579528 1 $T27 16777216 $AP)
C81=(0 -22735 0 106272484 0 81 2167729337579528 1 14847836159 16777216 $AP)
for B in acc2243v2 acc2243v2_shim; do
  ACC_DFT=0 $P5/$B merge "${C27[@]}" $T2/run_m27 1024 > r1_${B}_m27.txt 2>&1
  ACC_DFT=0 $P5/$B merge "${C81[@]}" $T2/run_m81 1024 3 4 2 -1 > r1_${B}_m81.txt 2>&1
  for m in 27 81; do n=$(keyx r1_${B}_m$m.txt | wc -l); if [ $n -gt 30 ] && vs_s2 $T2/merge_m$m.txt r1_${B}_m$m.txt; then echo "R1 $B m=$m PASS ($n non-symbol lines identical to S2; every symbol candidate/flag identical, balls overlap, radii <= S2)"; else echo "R1 $B m=$m FAIL"; fi; done
done
ACC_DFT=1 $P5/acc2243v2 merge "${C27[@]}" $T2/run_m27 1024 > r2_m27.txt 2>&1
ACC_DFT=1 $P5/acc2243v2 merge "${C81[@]}" $T2/run_m81 1024 3 4 2 -1 > r2_m81.txt 2>&1
echo "R2 m=27 $(python3 $P5/tests/compare_dft.py r1_acc2243v2_m27.txt r2_m27.txt)"
echo "R2 m=81 $(python3 $P5/tests/compare_dft.py r1_acc2243v2_m81.txt r2_m81.txt)"
# R3: full fresh run, shim build (portable SHA), 12 threads
{ time $P5/acc2243v2_shim run "${C27[@]}" 12 r3 500000000 40 ; } > r3_run.txt 2>&1
ACC_DFT=0 $P5/acc2243v2_shim merge "${C27[@]}" r3 1024 > r3_merge.txt 2>&1
if vs_s2 $T2/merge_m27.txt r3_merge.txt && diff <(key r1_acc2243v2_m27.txt) <(key r3_merge.txt) > /dev/null; then echo "R3 PASS fresh run == S2 (non-symbol lines, symbols) and == v2.3 merge of the S2 checkpoints byte-for-byte; digest $(dig r3_merge.txt)"; else echo "R3 FAIL"; fi
# R4a: two shards, B crashes after 15 units and restarts with other W; pooled merge
mkdir -p r4a_A r4a_B r4a_pool
ACC_SHARD=0/2 ACC_TAG=A $P5/acc2243v2 run "${C27[@]}" 6 r4a_A 500000000 7 > r4a_A.txt 2>&1
ACC_SHARD=1/2 ACC_TAG=B $P5/acc2243v2 run "${C27[@]}" 6 r4a_B 500000000 7 15 > r4a_B1.txt 2>&1; echo "R4a shard B first attempt exit $? ($(grep -c SIMULATED r4a_B1.txt) simulated crash)"
ACC_SHARD=1/2 ACC_TAG=B $P5/acc2243v2 run "${C27[@]}" 4 r4a_B 500000000 7 > r4a_B2.txt 2>&1; grep '^RUN units' r4a_B2.txt
expect_fatal "R4a-missing-shard" "units missing" $P5/acc2243v2 merge "${C27[@]}" r4a_A 1024
cp r4a_A/ckpt_*.bin r4a_B/ckpt_*.bin r4a_pool/
ACC_DFT=0 $P5/acc2243v2 merge "${C27[@]}" r4a_pool 1024 > r4a_merge.txt 2>&1
if [ "$(dig r4a_merge.txt)" = "$(dig r3_merge.txt)" ] && diff <(key r3_merge.txt) <(key r4a_merge.txt) > /dev/null; then echo "R4a PASS pooled shards (with crash/restart) digest == R3 digest $(dig r4a_merge.txt); $(ls r4a_pool | wc -l | tr -d ' ') checkpoints"; else echo "R4a FAIL"; fi
# R4b: selection
SELX="L0/0-5,L7,L100-103,L287,S0-9,S500,S1151"
ACC_SELECT=$SELX $P5/acc2243v2 run "${C27[@]}" 4 r4b_ref 500000000 5 > r4b_ref.txt 2>&1
ACC_SELECT=$SELX $P5/acc2243v2 run "${C27[@]}" 7 r4b_cr 500000000 3 9 > r4b_cr1.txt 2>&1; echo "R4b first attempt exit $?"
ACC_SELECT=$SELX $P5/acc2243v2 run "${C27[@]}" 2 r4b_cr 500000000 3 > r4b_cr2.txt 2>&1; grep '^RUN units' r4b_cr2.txt
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C27[@]}" r4b_ref 1024 > r4b_ref_merge.txt 2>&1
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C27[@]}" r4b_cr 1024 > r4b_cr_merge.txt 2>&1
grep -E '^(MERGE|COUNT_SELECTION|CHUNK_DIGEST)' r4b_ref_merge.txt
if [ -n "$(dig r4b_ref_merge.txt)" ] && [ "$(dig r4b_ref_merge.txt)" = "$(dig r4b_cr_merge.txt)" ]; then echo "R4b PASS selection digest identical after crash/restart"; else echo "R4b FAIL"; fi
expect_fatal "R4b-wrong-selection" "ACC_SELECT differs" env ACC_SELECT=L0/0-5 $P5/acc2243v2 merge "${C27[@]}" r4b_ref 1024
expect_fatal "R4b-bad-token" "selects no unit" env ACC_SELECT=S99999 $P5/acc2243v2 run "${C27[@]}" 1 r4b_bad 500000000 5
mkdir -p r4b_dup; cp r4b_ref/ckpt_*.bin r4b_dup/; f=$(ls r4b_dup/ckpt_*.bin | head -1); cp $f ${f%.bin}_tDUP.bin
expect_fatal "R4b-duplicated-ckpt" "covered twice" $P5/acc2243v2 merge "${C27[@]}" r4b_dup 1024
mkdir -p r4b_cor; cp r4b_ref/ckpt_*.bin r4b_cor/; f=$(ls r4b_cor/ckpt_*.bin | head -1); printf '\x01' | dd of=$f bs=1 seek=300 conv=notrunc 2>/dev/null
expect_fatal "R4b-corrupted-ckpt" "self-hash mismatch" $P5/acc2243v2 merge "${C27[@]}" r4b_cor 1024
mkdir -p r4b_miss; cp r4b_ref/ckpt_*.bin r4b_miss/; rm $(ls r4b_miss/ckpt_*.bin | head -1)
expect_fatal "R4b-missing-ckpt" "units missing" $P5/acc2243v2 merge "${C27[@]}" r4b_miss 1024
# R4c: streaming. apdir holds ONLY segment 0 (needed for the table); streamed segments are produced + verified on demand
SELS="L1-4,L100-101,L286-287"; mkdir -p r4c_ap; ln -sf $AP/ap_000000.bin r4c_ap/
export PRODUCER=$F/producer_variant/apwit_v VERIFIER=$R/verifier/wverify T_RUN=$T27
ACC_SELECT=$SELS $P5/acc2243v2 run "${C27[@]}" 1 r4c_ref 500000000 5 > r4c_ref.txt 2>&1
ACC_SELECT=$SELS ACC_TIMING_LOG=1 ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run 0 -22735 0 106272484 0 27 2167729337579528 1 $T27 16777216 $D/r4c_ap 8 r4c_str 500000000 1 > r4c_str.txt 2>&1
echo "R4c stream run exit $?; leftover ap/sha256 files in stream dirs: $(ls r4c_str/stream_g*_w*/ap_* 2>/dev/null | wc -l | tr -d ' ')"
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge "${C27[@]}" r4c_ref 1024 > r4c_ref_merge.txt 2>&1
ACC_NOSYMBOLS=1 $P5/acc2243v2 merge 0 -22735 0 106272484 0 27 2167729337579528 1 $T27 16777216 $D/r4c_ap r4c_str 1024 > r4c_str_merge.txt 2>&1
if [ -n "$(dig r4c_ref_merge.txt)" ] && [ "$(dig r4c_ref_merge.txt)" = "$(dig r4c_str_merge.txt)" ] && diff <(grep ^SEGHASH r4c_ref_merge.txt) <(grep ^SEGHASH r4c_str_merge.txt) > /dev/null; then echo "R4c PASS streamed a_q path digest == certified a_q path digest $(dig r4c_str_merge.txt), SEGHASH identical ($(grep -c ^SEGHASH r4c_str_merge.txt) segments)"; else echo "R4c FAIL"; fi
cat r4c_str/stream_g*_w*/stream_log.txt | awk '{print $3, $NF}' | sort -n > r4c_stream_hashes.txt; grep ^SEGHASH r4c_str_merge.txt | awk '{print $2, $3}' | sort -n > r4c_merge_hashes.txt
if [ "$(wc -l < r4c_stream_hashes.txt)" -eq 8 ] && diff r4c_stream_hashes.txt r4c_merge_hashes.txt > /dev/null; then echo "R4c PASS verifier ap_sha256 (stream log) == accumulator segment hashes (8 streamed segments)"; else echo "R4c FAIL hash cross-check ($(wc -l < r4c_stream_hashes.txt) stream lines)"; fi
# fail-closed controls: producer that fails; producer whose witness is corrupted after writing
cat > badprod_fail.sh <<'EOB'
#!/bin/bash
exit 7
EOB
cat > badprod_flip.sh <<EOB
#!/bin/bash
# real producer, then XOR one byte of a witness record (always a change); the verifier must reject the segment
$F/producer_variant/apwit_v "\$@" || exit \$?
w=\$(ls "\${9}"/wit_*.bin | head -1)
python3 -c "import sys; f=open(sys.argv[1],'r+b'); f.seek(100); b=f.read(1); f.seek(100); f.write(bytes([b[0]^0xFF])); f.close()" "\$w"
EOB
chmod +x badprod_fail.sh badprod_flip.sh; mkdir -p r4c_ap2; ln -sf $AP/ap_000000.bin r4c_ap2/
expect_fatal "R4c-producer-fails" "stream command failed" env PRODUCER=$D/badprod_fail.sh ACC_SELECT=L50 ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run 0 -22735 0 106272484 0 27 2167729337579528 1 $T27 16777216 $D/r4c_ap2 1 r4c_bad1 500000000 1
expect_fatal "R4c-witness-corrupted" "stream command failed" env PRODUCER=$D/badprod_flip.sh ACC_SELECT=L51 ACC_STREAM_CMD=$P5/stream_seg.sh $P5/acc2243v2 run 0 -22735 0 106272484 0 27 2167729337579528 1 $T27 16777216 $D/r4c_ap2 1 r4c_bad2 500000000 1
echo "R4c-witness-corrupted verifier said: $(cat r4c_bad2/stream_g001_w00/ver.time 2>/dev/null | grep FATAL | head -1)"
# tampered stored file: pre-produce segment 52 (with the verifier's .sha256 companion), then change one a_q value in place
mkdir -p r4c_ap3; ln -sf $AP/ap_000000.bin r4c_ap3/; $P5/stream_seg.sh 52 $D/r4c_pre52 && mv r4c_pre52/ap_000052.bin r4c_pre52/ap_000052.sha256 r4c_ap3/
python3 -c "import sys; f=open(sys.argv[1],'r+b'); f.seek(4000); b=f.read(4); f.seek(4000); f.write(bytes([b[0]^1])+b[1:]); f.close()" r4c_ap3/ap_000052.bin
expect_fatal "R4c-tampered-stored-ap" "differs from the file the verifier hashed" env ACC_SELECT=L52 $P5/acc2243v2 run 0 -22735 0 106272484 0 27 2167729337579528 1 $T27 16777216 $D/r4c_ap3 1 r4c_bad3 500000000 1
echo SMALL_DONE
