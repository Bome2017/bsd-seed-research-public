# RESUME — C13 run

Target: C13 = [T^2] L_13(E,T) mod 13. Nonzero => Sha[13^inf] = 0. Zero => inconclusive, STOP.
Cutoffs verified: m=169 T=55,046,045,695 (3281 seg); m=13 T=4,026,531,839 (240 seg). 2333 reused + 948 new.
Preflight done (PREFLIGHT.json, 0 failures). Stage W+A launched via run_p3.sh in background; log run/logs/pipeline.log
and run/logs/timeline.log. Restart: the pipeline is per-segment restartable; rerun the same command.
STILL TO WRITE while it runs: the C13 downstream functional (9 * sum binom(j(b),2) S_b over the 66 folded symbols,
weights predeclared in the gate's P13_EVALUATION_GATE.json) and the byte-sealing step.

## SUPERSEDED 2026-09-22
C13 = 2 (omega1) / 1 (full real period), NONZERO. This file's "STILL TO WRITE" items were completed elsewhere:
see `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p13/` (NORMALIZATION.md, DOWNSTREAM.json,
COMPLETION_REVIEW.json, CERTIFICATE_BINDINGS.json) and `audits/P13_PRIMARY_THEOREM.md`.
Do NOT restart this pipeline. There is no successor. See SUPERSEDED_BY_NORMALIZATION.md for what this folder got wrong.
