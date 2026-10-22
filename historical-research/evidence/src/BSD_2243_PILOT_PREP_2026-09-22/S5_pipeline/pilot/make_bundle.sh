#!/bin/bash
# make_bundle.sh -- assemble pilot_bundle_2243.tar.gz from the FROZEN local build and the local reference results.
# Run only after tests/run_final.sh has printed FINAL_DONE with every check passing. No network access; nothing is sent.
set -euo pipefail
P=/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22; P5=$P/S5_pipeline; T=$P5/tests; OUTD=$P5/pilot/bundle; B=$OUTD/pilot_bundle_2243
grep -q FINAL_DONE $T/final_driver.log || { echo "final validation not finished"; exit 1; }
if grep -qE '(^| )FAIL( |$)' $T/final_driver.log; then echo "final validation has failures: no bundle"; exit 1; fi
rm -rf $OUTD; mkdir -p $B/src/compat/CommonCrypto $B/scripts $B/reference/T2 $B/third_party $B/logs
cp $P5/acc2243v2.c $B/src/; cp $P5/compat/CommonCrypto/CommonDigest.h $B/src/compat/CommonCrypto/
cp /Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/verifier/wverify.c $B/src/
cp /Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/producer_variant/apwit.c /Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/producer_variant/fastap.c $B/src/
cp $P5/stream_seg.sh $P5/pilot/bootstrap.sh $P5/pilot/pilot_run.sh $T/compare_dft.py $B/scripts/
cp /Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4.tar.gz $B/third_party/
cp -R $P/S2_prototype/T2/run_m27 $P/S2_prototype/T2/run_m81 $P/S2_prototype/T2/merge_m27.txt $P/S2_prototype/T2/merge_m81.txt $B/reference/T2/
rm -f $B/reference/T2/run_m27/run.lock $B/reference/T2/run_m81/run.lock
mkdir -p $B/reference/v23; cp $T/small/r1_acc2243v2_m27.txt $B/reference/v23/merge_m27.txt; cp $T/small/r1_acc2243v2_m81.txt $B/reference/v23/merge_m81.txt; cp $T/small/r2_m81.txt $B/reference/v23/merge_m81_dft.txt
dig() { grep '^CHUNK_DIGEST' "$1" | awk '{print $2}'; }
SEL5=$(grep '^SEL5=' $T/run_r5_2243.sh | sed 's/^SEL5="\(.*\)"$/\1/')
{ echo "m27_digest $(dig $T/small/r3_merge.txt)"; echo "m81_digest $(dig $T/small/r1_acc2243v2_m81.txt)"
  echo "r5_digest $(dig $T/r5/A_merge.txt)"; echo "r5_selection $SEL5"; } > $B/reference/expected.txt
( cd /Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap && for f in ap_*.bin; do s=${f#ap_}; s=${s%.bin}; echo "$((10#$s)) $(shasum -a 256 $f | cut -d' ' -f1)"; done ) > $B/reference/certified_ap_sha256.txt
( for f in $P/S3_bench/ap/ap_*.bin $P/S3_bench/conc/ap/ap_*.bin; do s=$(basename $f .bin); s=${s#ap_}; echo "$((10#$s)) $(shasum -a 256 $f | cut -d' ' -f1)"; done ) | sort -u > $B/reference/local_ap_sha256_2243.txt
# provenance: bundled sources against the sealed / frozen originals
{ echo "bundled sources vs originals (sha256 must match)"
  shasum -a 256 $B/src/wverify.c /Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/verifier/wverify.c
  echo "sealed manifest entries:"; grep -E '\./(verifier/wverify|src/apwit)\.c$' /Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/MANIFEST.sha256
  grep -E 'producer_variant/fastap\.c$' /Users/bsm/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/MANIFEST.sha256
  shasum -a 256 $B/src/apwit.c /Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/apwit.c $B/src/fastap.c $B/src/acc2243v2.c $B/src/compat/CommonCrypto/CommonDigest.h
  cat $P5/FINAL_BUILD_HASHES.txt; shasum -a 256 $B/third_party/pari-2.17.4.tar.gz; } > $B/reference/PROVENANCE.txt
wc -l $B/reference/*.txt; cat $B/reference/expected.txt
( cd $OUTD && COPYFILE_DISABLE=1 tar czf pilot_bundle_2243.tar.gz pilot_bundle_2243 && shasum -a 256 pilot_bundle_2243.tar.gz | tee pilot_bundle_2243.tar.gz.sha256 && ls -la pilot_bundle_2243.tar.gz )
