#!/bin/bash
# final validation of the frozen S5 build (hashes in ../FINAL_BUILD_HASHES.txt): small suite, R4d, R5 (2243 scale)
cd /Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline/tests
echo "FINAL start $(date '+%F %T'); build:"; cat ../FINAL_BUILD_HASHES.txt; shasum -a 256 ../acc2243v2 ../acc2243v2_shim ../stream_seg.sh
bash run_small.sh 2>&1 | grep -v "^  File\|^    \|^ *~"
bash run_r4d.sh 2>&1
bash run_r5_2243.sh 2>&1
echo "FINAL end $(date '+%F %T')"; echo FINAL_DONE
