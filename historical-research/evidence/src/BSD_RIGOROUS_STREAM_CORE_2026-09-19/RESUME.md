# RESUME (rigorous stream core)
If the session dies: read STATE.json for the phase and DESIGN.md for the spec. Artifacts are append-only under logs/.
Rebuild: see build.sh (written in P1). Never launch a p=3/p=7 run from here (P3_RUN_PLAN.md is a plan only).
2026-09-19 (after usage-limit pause): arbcore v2 built (see STATE.json). Validation outputs go to validation/; seed run to runs/seed150M/.
2026-09-19: seed certified (runs/seed150M/logs/l2.txt); p3plan/run_p3.sh tested on small curves only (never on the seed). Remaining: reports + MANIFEST.
2026-09-19 FINAL: RIGOROUS_STREAM_CORE_READY. Seed r_an = 2 certified (ANALYTIC_RANK_CERTIFICATE.md). p=3 run NOT launched (P3_RUN_PLAN.md;
run_p3.sh refuses without P3_AUTHORIZED=yes). MANIFEST.sha256 regenerated last; verify with `shasum -a 256 -c MANIFEST.sha256`.
