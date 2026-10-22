# TASK — ARISTOTLE_A1_WITNESS_CONTENT

> **WARNING.** Formalizing WC proves only the implication from the stated witness-content antecedent.
> It does not establish that the antecedent is easier than FIN or that FIN has been reduced.

## Objective (exact)
Replace every `sorry` in `WitnessContent/Targets.lean` by a complete proof.
- Each theorem keeps its **exact name** and its **exact type** `Spec.<Name>`, as defined in the frozen
  `WitnessContent/Spec.lean` and `WitnessContent/Defs.lean`.
- The mathematical content is the purely algebraic part of Codex's Theorem WC:
  - bounded witness content / bounded p-divisibility (the antecedent, as a hypothesis),
  - plus the exact Ota inputs (as hypotheses),
  - ⇒ finiteness of each good primary part, vanishing of the good primary parts at primes not dividing A,
    and global finiteness given finiteness at the exceptional set.
- The package also covers the finite group-ring algebra behind it and the regression countermodels.

## Acceptance levels
- **A1_FULL.** Every CORE and FULL target is proved. This means all purely algebraic implications of WC are machine-checked,
  with the arithmetic antecedent isolated as a hypothesis.
- **A1_CORE.** Every CORE target is proved: Lemma A (commutative case), depth and J_E lemmas, the abstract WC theorem
  (the finite-support deduction), and the three regression / non-vacuity checks.
  - The remaining FULL targets are the group-ring glue: T3, T4 (with T4b), T8, T10 and T11.
- **Failure.** Report the **first exact unformalized statement**: the first CORE-then-FULL target in `THEOREM_TARGETS.md` order
  that is not clean, together with the smallest sub-lemma you could not prove, stated in Lean.
- STRETCH targets (S1–S3) are optional and never affect the level.

## Rules
1. **You may invent intermediate lemmas.** Put them in new files under `WitnessContent/` and import them from `Targets.lean`.
2. **Seek a complete formal proof**, not a translation of the prose.
3. **Keep the arithmetic antecedent and the imported arithmetic theorems as explicit hypotheses.**
   - They are hypotheses of the frozen statements; never try to discharge them.
   - In particular, never try to prove `A ∈ J_E`, `J_E ≠ 0`, Ota's theorems, Selmer facts, or torsion of Sha.
4. **Do not strengthen assumptions.**
   - Do not edit `Defs.lean`, `Spec.lean`, `Acceptance.lean`, `lakefile.toml`, `lean-toolchain` or `scripts/level.py`
     (their SHA-256 values are in `scripts/FROZEN.sha256`).
   - Do not add hypotheses to a target.
   - If you believe a target is false or mis-stated, STOP. Record the counterexample or the exact issue in `STATE.json`, and
     do not "fix" the statement.
5. **Harmless abstraction is allowed** if it makes a proof easier, but you must also prove that your abstraction implies
   the packaged target (the frozen `Spec` statement is what gets checked).
6. **Test suspicious statements against the included countermodels** before investing in them. `CM_uniform_denominator` and
   `CM_nonzero_everywhere` show that "a nonzero witness at every prime ⇒ finite support / J_E ≠ 0" is FALSE. No proof may
   rely on it.
7. **No `sorry`, `admit` or new `axiom`** in any accepted theorem.
   - Temporary admits during development must be eliminated.
   - If they cannot be eliminated, the affected target is reported as FAILED (it will show `sorryAx` in `Acceptance.lean`).
8. **Keep `STATE.json` and `RESUME.md` updated** as you go: per-target status, level reached, first unformalized statement,
   and notes.
9. **Report the exact theorem names that compile clean** (the `scripts/acceptance.sh` output).
10. **Run a clean build before returning**: `bash scripts/acceptance.sh`, which removes `.lake/build`, rebuilds, and probes axioms.
11. **Make no claim that FIN, Sha finiteness, or any BSD statement is proved.** The deliverable is conditional algebra.

## Environment
- Lean `leanprover/lean4:v4.28.0`, mathlib tag `v4.28.0` (rev `8f9d9cff6bd728b17a24e163c9402775d9e6a365`). This is the same pin
  as earlier Aristotle packages of this project.
- If your environment cannot use this pin, stop and report it rather than silently porting the frozen files.

## Out of scope (NOT_PART_OF_THIS_TASK)
- Anything about elliptic curves, modular symbols, Selmer groups, Kato/Ota Euler systems, or p-adic L-functions.
- The antecedent J_E ≠ 0, and any "uniform integral comparison".
- LINE and "LINE ⇒ WC".
- FORMULA-side lemmas: rational reconstruction, polynomial separation, the common certificate.
- Codex's rank-two contraction lemma (FORMALIZABLE_GAPS A2).
- Integral lattice content (formalized in the sibling package A2).
