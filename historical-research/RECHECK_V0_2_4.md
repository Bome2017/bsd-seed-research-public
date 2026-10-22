# v0.2.4 (local, unreleased): the perimeter is closed

This revision preserves v0.2.3 (local commit `8ed37c5`, itself built on v0.2.2 `2a726213`). It adds two things and one
statement.

1. **An exact descent certificate for the rank and `Sha[2]`**, replacing the preprint import under the rank, basis and 2-primary
   results.
   - A 2-isogeny descent is local at {2, 3, 2243, 4547, 5843, ∞}, with no class groups: `106272484 = 2²·4547·5843`,
     `22735² − 4·106272484 = 3²·2243·4547`.
   - It is computed independently by PARI 2.17.3 `ellrank` (unconditional; `[2,2,0]` for E and E′) and by eclib 20250627
     `mwrank` (`Rank = 2`, 2-Selmer rank 3, `#III(E/Q)[2] = 1`).
   - Explicit images give `#α(E(ℚ))·#α′(E′(ℚ)) = 16 = 2^(r+2)`.
   - Index one: eclib saturation at a proven bound.
   - Claims R.1, R.4 and S.2 are now graded EXACT_COMPUTATION, and S.P follows. Zywina's family theorem (arXiv:2502.01957)
     is corroboration only.
   - Evidence: `evidence/src/BSD_PERIMETER_Q36_2026-09-25/descent/`, replayed by `verify_descent.sh` in about 4 s.
2. **The A5 formal check at p = 3.** The deduction of `Sha[3^∞] ≅ (ℤ/3)²` (claim S.3) is Lean-checked: A5_FULL, 23/23
   targets, STRETCH clean, standard axioms only, one proof run replayed from a fresh copy.
   - The hypotheses follow the governing order of inference: Skinner Thm A; control finiteness first; the independent
     height certificate; Jones Thm 3.1 forward; SW Prop. 3.5; the Cassels–Tate pairing.
   - New Remark 4.7 (`rem:a5lean`). S.3 gains LEAN_CHECKED.
3. **The statement of the frontier.** §11 now says four things.
   - The three obligations (FIN, ORDER9, Q36) together are equivalent to full BSD for E (Theorem `thm:endpoint`, claim
     R.7). The group obligation is finiteness *and* order nine; FIN does not imply ORDER9.
   - Every other statement is settled at its stated grade, so these endpoint obligations form the current known
     frontier. B.8 and O.4 stay OPEN in the index as a regime and a proposed mechanism, not further endpoint obligations.
   - Under the retained prime-by-prime strategy, FIN and ORDER9 need every good prime p ≥ 17 and the bad primes 2243, 4547
     and 5843; a proof need not use that strategy.
   - For Q36, rationality with denominator at most 174 would suffice (Q.1); Q.2 and Q.3 are other sufficient routes; none
     of these antecedents is proved.

   The wording follows the project rule to say "current known frontier", not "only what remains".
4. **README corrections.** The status table no longer cites the preprint rank theorem for R.1. The 2-primary row names
   the exact computation and the Lean-checked deductions. The v0.2.2 editorial paragraph no longer reads as if it described
   this revision.

**Evidence.**
- 16 files are appended, byte-identical to their originals, by `tools/build_evidence_transition.py`.
- All 3,373 v0.2.3 provenance rows, 36,076 exclusions and 6 redactions are preserved byte for byte.
- The retained reviewed differences (122 and 7) are listed in `review/V024_EVIDENCE_TRANSITION.json`.

**Bindings.** The transition record is `review/V024_PERIMETER_APPLIED.json`. `tools/verify_patch_release.py` now
delegates to `tools/verify_v024_transition.py`, which:
- rebuilds the exact v0.2.3 tree from the copies preserved under `review/history/v0.2.3/`, and proves it equal to the
  v0.2.3 manifest;
- runs the unmodified v0.2.3 checker inside it (every earlier binding and the A4 transition);
- then checks the v0.2.4 delta: the file set, claim fields before and after, exact-once text edits, the evidence rows,
  generated outputs, and new bytes bound.

From the bundle root run:

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
shasum -a 256 -c MANIFEST.sha256
```

**Not changed.** Theorem statements, certificates, `tools/verify_release.py`, `paper/seed_bsd.tex` (its title-page date
and tag remain those of v0.2.2), the Makefile, and the Lean sources of earlier packages.

**Audit repairs (2026-09-25, after the independent audit of `9eeebf9`).**
- **F1.** `tools/verify_v024_transition.py` no longer accepts an omitted provenance row replaced by a duplicate. It now
  checks whole-table invariants that do not depend on any rebindable hash:
  - each provenance path occurs once;
  - rows and `evidence/src` files correspond one to one;
  - every row matches its file's hash;
  - sizes agree, except for the declared redactions.

  It also requires the appended rows to be exactly one row per declared addition, in the logged order, with exact
  content. Four negative controls use a maximal rebinding adversary that recomputes every table, record and manifest
  hash:
  - the auditor's duplicate-row counterexample;
  - the same corruption among the v0.2.3 rows;
  - changed metadata on an appended row;
  - an undeclared README edit.

  Each must fail at the named check. The historical v0.2.3 checker is unchanged.
- **F2.** The preprint statement in §11 now names the upgraded claims and keeps B.9 and B.13's explicit preprint
  dependencies.
- **F3.** The frontier wording distinguishes the endpoint from necessary proof steps (see item 3).
- **Recheck notes (K2).** Two inherited sentences in §10 are narrowed:
  - the prime-by-prime ladder moves the threshold only when climbed in order;
  - the bad-prime core-hours are cost-model estimates, not necessary workloads.

  The claim index is unchanged. X.14's literal wording still begins "Each further prime moves only the conditional
  threshold"; its parenthetical ladder (2601 → 3249 → 4761 → 7569 …) suggests consecutive primes, but does not state the
  out-of-order qualification. Aligning X.14's wording is left for a future controlled index update. X.16 already calls
  its figures modeled.

**Open.** FIN, ORDER9 and Q36 remain open. No new computation or research branch is authorized by this revision.
