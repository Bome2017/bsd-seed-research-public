# Aristotle derived-Gross runs over ℚ(√−7): canonical return (2026-10-06)

**Status.** The user submitted the run. Two independent runs and one regrade all return **`PRECISE_OBSTRUCTION`**. With the pairing attached to the theta element's own group, the degree-two Gross-point identity over ℚ(√−7) is degenerate (0 = 0), and no constant m_E is ever fixed. This does **not** prove that a rank-two anchor cannot exist.

**Task.** `../BSD_ARISTOTLE_DERIVED_GROSS_SUBMISSION_2026-10-06/DELTA_TASK_DERIVED_GROSS.md`, run on the canonical packet `BSD_SEED_FRONTIER_2026-10-06` (revision 2).

**`run_74e483e4/`** (archive cb9ad0a0):
- `DERIVED_GROSS_RESULT.md`: the full return, with routes A, B and C.
  - Route A: the canonical anticyclotomic pairing on E(ℚ) is identically zero for odd p.
  - Route B: G2's cyclotomic pairing carried over needs two new theorems and covers split ℓ only.
  - Route C: Bertolini–Darmon derived heights are rebuilt for each p.
- `DerivedGross/Parity.lean`, `DerivedGross/Threshold.lean` and `AXIOMS.txt`.
- `lakefile.toml.returned` (it adds a `DerivedGross` library) and `ARISTOTLE_SUMMARY.md`.

**`runs_523a4561_1d81f21f/`** (archive 0cd74d26):
- Run 523a4561 is an independent second run of the same task. Its `DERIVED_GROSS_RESULT.md` is a separate document. It reaches the same obstruction and names the first missing arrow: a theorem computing Θ⁽²⁾_ℓ from E(K)⁺ = E(ℚ), with one constant at every level.
- Run 1d81f21f is a regrade under a tightened threshold:
  - `THRESHOLD_REGRADE.md` gives the regrade; the status stays `PRECISE_OBSTRUCTION` and is not `IDENTITY_ONLY_UP_TO_P_UNIT`.
  - `DELTA_TASK_DERIVED_GROSS_TIGHTENED.md`, `SUBMISSION_PROMPT_TIGHTENED.txt` and `SUBMIT_COMMAND_TIGHTENED.txt` carry the four-interface admission threshold and the unit-ambiguity status. Use them for any future submission.
- `RequestProject/DerivedGross/Obstruction.lean` and `Threshold.lean`, plus `ARISTOTLE_SUMMARY.md` covering both runs.

**`CLAUDE_CHECK.md`:** integrity, an independent read-only recompile, and a claim check.

**Excluded.** Aristotle's citation banner in each archive's `README.md` is left out of this folder. The original archives are kept unchanged under `../archives/`.

FIN, ORDER9 and Q36 are unchanged.
