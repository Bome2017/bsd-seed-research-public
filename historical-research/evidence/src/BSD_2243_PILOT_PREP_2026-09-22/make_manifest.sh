#!/bin/bash
# make_manifest.sh -- SHA-256 of every file in the 2243 pilot-preparation folder (additive custody record; run last).
set -euo pipefail
cd /Users/bsm/BSD_2243_PILOT_PREP_2026-09-22
find . -type f ! -name MANIFEST.sha256 ! -name '.DS_Store' -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256 > MANIFEST.sha256
echo "files $(wc -l < MANIFEST.sha256); manifest sha256 $(shasum -a 256 MANIFEST.sha256 | cut -d' ' -f1)"
