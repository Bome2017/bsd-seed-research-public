#!/bin/bash
set -euo pipefail
export R=/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19
export OUT=/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p7/run
export P3_AUTHORIZED=yes TARGETS="49:1:1 7:1:1" LATDEN=1024 J=12 W=12 KEEP_WIT=1
exec "$R/p3plan/run_p3.sh"
