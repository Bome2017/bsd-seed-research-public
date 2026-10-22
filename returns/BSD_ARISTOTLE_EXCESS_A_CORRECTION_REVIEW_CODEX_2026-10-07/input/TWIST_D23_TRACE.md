# Trace of the D = −23 twist records (L′(E^{(−23)},1), ord_{s=1} = 1)

Paths are relative to `project/` after `python3 prepare_reference.py`.
The exact re-checks below come from `checks/d23_trace_check.py` (Python standard library only;
output in `checks/d23_trace_check.out.json`). That script recomputes **no** L-series sum.
I ran no new L-value computation and no remote job.

Abbreviations:
- CERT = `reading_set/BSD_SEED_ARISTOTLE_2026-10-05/working_set/repo/evidence/src/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21`
- W3 = `current_overlay/BSD_CURRENT_OVERLAY_2026-10-06/current_lab/work/returns/BSD_ARISTOTLE_W3_P17_P19_RETURN_2026-10-06`

## 1. The two calculations in the record, by date

| Date | What | Where | Claimed grade |
|---|---|---|---|
| 2026-09-21 | Arb ball sum to T = 3,456,106,495 plus a written tail bound: **39.512236 ≤ L′ ≤ 40.182321** | CERT/RESULT.md (sha256 66354605…19a8), CERT/PROOF.md (e45c4f9a…3ad2) | "TWIST_D23_NONZERO_CERTIFIED"; compendium status PROVED_COMPUTER_ASSISTED; reviews were same-family/metadata only (CERT/COMPLETION_REVIEW.json: `formal_proof: false`, `second_full_numerical_implementation: false`) |
| 2026-09-21 | Exact recheck of the endpoint arithmetic, and coverage of the primes served (5 ≤ p ≤ 160) | `…/_work/bridge_repair_assessment_2026-09-21/D23_COVERAGE_REVIEW.md`; `…/BSD_TWIST_D23_CERTIFICATE_2026-09-21/CERTIFICATE_CONFIRMED_AND_COVERAGE.md` | endpoint arithmetic only, not a second sum |
| 2026-10-06 | Floating-point sum to T = 3·23·√N ≈ 5.56·10⁹, with an independent a_q engine (Shanks–Mestre BSGS): **L′ ≈ 39.84727806412**; split-parameter functional-equation check discrepancy 6.8·10⁻¹² | W3/HEEGNER_NU_NOTE.md §3 (f3a86b23…bda2), W3/w3_p17/TWIST23_RESULTS.json (01301ee2…d49d) | its author: "floating point and is not interval-certified" |

The compendium headings for these records are at FULL_COMPENDIUM.md lines 331, 343, 520, 1039, 1075, 1099, 1172 and 16399. Both
calculations use the seed curve. The certificate's model is y² = x³ − 22735x² + 106272484x,
and the governing model is y² = x³ − x² − 66020924x − 65074271436. The two models have identical
c4 = 3169004368 and c6 = 56243184546880, so they are isomorphic over Q (exact check 4). The
conductor 23²·N = 3440186458738710936 also agrees.

## 2. What the certificate's surviving files support (exact, rechecked here)

1. **Custody.** CERT/MANIFEST.sha256 has 1,070 entries.
   - 17 are present in the archive, and all 17 match their hashes.
   - The hashes recorded inside RESULT.json for INPUT_BINDINGS.json, BUILD_BINDINGS.json, the
     engine log and the combine log all match.
   - The logs `run_T3456106495.log` and `combine_T3456106495.log` print identical results: the
     partial sum `[39.847278312318874 +/- 4.28e-16]`, the tail `[0.33504179704832… +/- 1.74e-26]`,
     the interval `[39512236, 40182321] / 1000000` and `ZERO_EXCLUDED 1`.
2. **Tail bound.** Formula (2) of `…/bridge_repair_assessment_2026-09-21/MCS_TWIST_IDEAL_REVIEW.md` §3:
   - I checked its derivation line by line. It uses |a_n| ≤ d(n)√n, the bounds
     x log x − x ≤ Σ_{n≤x} d(n) ≤ x(log x + 1), partial summation, E_1(y) ≤ e^{−y}/y, and
     log x ≤ log T + (x−T)/T.
   - Evaluated at 80 digits with c = 2π/(23√N) and T = 3,456,106,495, it gives
     B = 0.3350417970483208239547060827…. This agrees with the logged Arb ball to all printed digits.
3. **Endpoints.** 2S_T − 4.28·10⁻¹⁶ − B = 39.5122365152… ≥ 39.512236, and
   2S_T + 4.28·10⁻¹⁶ + B = 40.1823201093… ≤ 40.182321. The margin is |2S_T|/B ≈ 119.
4. **Root number.** N = 2³·3·2243·4547²·5843. Since −23 ≡ 1 (mod 8), χ_{−23}(2) = +1, and
   χ_{−23}(q) = +1 for q = 3, 2243, 4547, 5843. Since χ_{−23}(−1) = −1, we get χ_{−23}(−N) = −1.
   With the imported w(E) = +1, the formula w(E^χ) = χ(−N)w(E) for gcd(23, N) = 1 gives
   w(E^{−23}) = −1, so L(E^{−23},1) = 0.
5. **The 2026-10-06 value.** Re-derived from the shipped bucket sums (post-processing only):
   39.84727806412273, inside the certified interval. It differs from the certified partial sum
   2S_T by −2.48·10⁻⁷. That is the expected size of the true tail beyond T (cT ≈ 11.7), and far
   inside B.

## 3. What cannot be checked from the supplied archive

- **The finite sum 2S_T itself.** Absent from the archive:
  - `twist.c` (12,686 bytes; bound sha256 4eef4e08…a623);
  - `retained_arbcore.c` (34,328 bytes; bound sha256 56a43aac…7fd7);
  - the binary `twist`;
  - all 1,030 atomic work units under `run_T3456106495/` (the manifest lists 1,031 entries there);
  - `supervise.py`, `integrate_completion.py` and `CHECKPOINTS.jsonl`;
  - the benchmark and timing logs.

  `full_record_index/FILE_INVENTORY.jsonl.gz` and `BULK_BINARY_RECEIPTS.jsonl.gz` list the two
  source files at those sizes on the original host (for example
  `/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21/twist.c`), without
  hashes. CERT/review_completion.py cannot run here, because it reads those absent files.
- **The coefficient input.** CERT/INPUT_BINDINGS.json binds 206 segments of the C11 a_p corpus by
  absolute host paths (`/Users/bsm/…/active_full_bsd/p11/run/ap/ap_*.bin`). None of these files
  is in the archive. The binding itself records `witness_replay: false` and custody
  `REUSED_SEALED_P7_CERTIFICATE`. So the certificate inherits the corpus grade rather than
  re-witnessing it.
- **The Taylor-model E_1 error analysis** is described in CERT/DESIGN.md. Its implementation is in
  the absent `twist.c`.

## 4. Consequence for this return

- ord_{s=1} L(E^{−23},s) = 1 follows from the two facts "interval excludes 0" and "w = −1".
- The second fact is rechecked exactly here, given the imported w(E) = +1.
- The first fact rests on the 2026-09-21 computer-assisted certificate. That certificate's
  arithmetic core is not replayable from the supplied files.
- An independent floating-point calculation, with independently generated coefficients, agrees
  to 2.5·10⁻⁷. That is consistent with the certificate's claimed value, but it is not a proof.

Gross–Zagier–Kolyvagin then gives rank E^{−23}(Q) = 1 and Sha(E^{−23}/Q) finite. Hence
s⁻ = dim Sel_p(E^{−23}/Q) = 1 for every odd p not dividing #Sha(E^{−23}/Q)·#E^{−23}(Q)_tors.
That is a cofinite set, but no explicit bound is known because #Sha(E^{−23}/Q) has not been computed.

If the reviewer can match the host files against the BUILD_BINDINGS hashes and the unit hashes
in CERT/RESULT.json, CERT/review_completion.py is the record's own replay entry point.
