#!/usr/bin/env bash
# Acceptance check for this package. Run from the package root:  bash scripts/acceptance.sh
set -u
LIB="PrimarySupport"
echo "== 1. frozen files (statements, definitions, probe, toolchain pin)"
shasum -a 256 -c scripts/FROZEN.sha256 || { echo "RESULT: FROZEN_FILES_CHANGED"; exit 2; }
echo "== 2. clean build of this package (mathlib itself is not rebuilt)"
rm -rf .lake/build
lake build > build.log 2>&1; tail -3 build.log
grep -q "Build completed successfully" build.log || { echo "RESULT: BUILD_FAILED"; exit 3; }
echo "== 3. informational: sorry / admit / axiom tokens in non-frozen Lean files (step 4 is authoritative)"
grep -rnE "\bsorry\b|\badmit\b|^[[:space:]]*axiom[[:space:]]" --include='*.lean' "$LIB" | grep -vE "^$LIB/(Defs|Spec|Acceptance)\.lean:" || echo "(none)"
echo "== 4. axioms of every target"
lake env lean "$LIB/Acceptance.lean" > axioms.log 2>&1; cat axioms.log
echo "== 5. level"
python3 scripts/level.py axioms.log
