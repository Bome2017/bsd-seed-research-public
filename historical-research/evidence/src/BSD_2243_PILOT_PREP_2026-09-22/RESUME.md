# RESUME — 2243 capped-pilot preparation (NO full launch, NO cloud spend)

User instruction 2026-09-22 (verbatim core): "Prepare a bounded cloud pilot for 2243 only; do not launch the full
certificate. First finish the sign, split-height, and dependency checks needed to state the exact certificate
consequence. Implement and independently validate the scalar accumulator against retained small certified cases.
Reconcile the CPU-hour estimate with the scalar-mode cutoff. Report production, verification, traversal, kernel,
interval summation, checkpointing, and storage costs separately. Include the nonzero-only stopping criterion ...
Produce a proposed cloud benchmark with a hard spending cap and resource limits. Measure the complete path at
representative heights, including the upper planned range, and test restart/recombination. Return an all-in
projected cost and its uncertainties before requesting authorization for the full run. Do not assume Aristotle
supplies a large numerical cluster, and do not substitute an unbenchmarked GPU speedup."

Finding carried in (feasibility folder): nonzero-only scalar screen needs MORE coefficients than per-symbol exact
identification (2243: 5.74e13 [W_p bound] / 4.70e13 [idealized Parseval floor] vs T_min 3.91e13). Design decision:
one chunked class-sum accumulator; derive exact symbols AND the scalar/nonzero test from it; cost both modes.

Stages: S1 math checks -> S2 accumulator + validation -> S3 local complete-path benchmark -> S4 cost model -> S5 pipeline
(streaming, restart/recombination at 2243 scale, cloud pilot bundle) -> report + authorization request (capped pilot only).
Status 2026-09-23 00:05: S1 DONE; S2 DONE (T1, T2, T3 PASS); S3 DONE (+ loaded-host S3b); S4 model DONE (1.106e5 local
core-h per-symbol; production 84%, verification 13%); S5 final build frozen (S5_pipeline/FINAL_BUILD_HASHES.txt), final
validation running: S5_pipeline/tests/run_final.sh -> tests/final_driver.log (look for FINAL_DONE; do not edit the
binaries, stream_seg.sh or tests while it runs). Remaining: S4 reconciliation doc with all-in cost + uncertainty,
pilot bundle (pilot/make_bundle.sh), AWS launcher (dry-run default), PILOT_PROPOSAL.md, CODEX_CHECK_REQUEST.md, memory.
Prices checked 2026-09-22/23: c7a.16xlarge (64 physical Genoa cores) $3.2845/h on-demand, ~$1.20/h spot; Hetzner
post-2026-06-15 CCX63 EUR 1.3678/h, AX162-1 EUR 612.30/mo + EUR 304 setup.

Update 2026-09-23 00:20: DEFECT found before spend and fixed -- v2 merge fed per-class radii (global tally) into acb_dft,
whose Bluestein/Rader steps inflate radii 7e6x at m = 2243^2 (probe/probe_full.txt): a full run would have identified no
symbol. v2.1 (merge only) feeds exact midpoints and adds 2E per symbol. Build frozen: S5_pipeline/FINAL_BUILD_HASHES.txt.
Final validation of v2.1 running (tests/final_driver.log). Docs written: S4_cost/S4_COST_RECONCILIATION.md,
S5_pipeline/pilot/PILOT_PROPOSAL.md, S5_pipeline/CODEX_CHECK_REQUEST.md. Next: when FINAL_DONE with no FAIL ->
pilot/make_bundle.sh; S5_RESULTS.md; REPORT.md; MANIFEST; memory; final message (authorization requested ONLY for the
capped pilot, not the full run).

Update 00:56: third defect fixed -- threaded system() ran serially on macOS; v2.2 uses posix_spawn. Build re-frozen
(S5_pipeline/FINAL_BUILD_HASHES.txt, v2.2). Final validation of v2.2 relaunched 00:54:49 (tests/final_driver.log).
v2.1 partial log kept (tests/final_driver_v2.1_partial.log). Docs updated to v2.2 (S5_RESULTS.md, CODEX_CHECK_REQUEST.md).

Update 01:40: two more defects fixed in v2.3 -- (4) arb_div reduced-precision radius inflation ~|x| 2^-28 on symbol
division (would eat the 4.8e-7 margin for large symbols); (5) run.lock fd inherited by stream children (restart after a
crash refused while orphans live). v2.3 frozen (FINAL_BUILD_HASHES.txt); validation relaunched 01:36:37. Tests now compare
symbols vs S2 by candidates/flags with radii <= S2 (v2.3 radii are smaller); pilot compares with LOCAL v2.3 merges
byte-for-byte (bundle reference/v23/). Remaining after FINAL_DONE: S5_RESULTS + REPORT fill-in, make_bundle, manifest,
memory project note, final message (authorization for the capped pilot only).

FINAL 02:22: preparation DONE. v2.3 validated (24 PASS / 0 FAIL). Bundle cb24d5f7... built. Documents: REPORT.md (top),
S1_RESULTS.md, S2_RESULTS.md, S4_cost/S4_COST_RECONCILIATION.md, S5_pipeline/S5_RESULTS.md, S5_pipeline/pilot/PILOT_PROPOSAL.md,
S5_pipeline/CODEX_CHECK_REQUEST.md. Nothing launched; $0 spent. Next actions belong to the user: authorize/run the capped
pilot (launch_aws.sh, dry run by default), route the Codex check, and D2/D5 before any full-run request.
