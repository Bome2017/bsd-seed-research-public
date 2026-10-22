# TASK — ARISTOTLE_A2_PRIMARY_SUPPORT

> **WARNING.** Formalizing WC proves only the implication from the stated witness-content antecedent.
> It does not establish that the antecedent is easier than FIN or that FIN has been reduced.
> (This package formalizes the support infrastructure used by WC; the same caveat applies.)

## Objective (exact)
Replace every `sorry` in `PrimarySupport/Targets.lean` by a complete proof.
- Each theorem keeps its exact name and its exact type `Spec.<Name>` (frozen in `PrimarySupport/Spec.lean` and
  `PrimarySupport/Defs.lean`).

## Acceptance levels
- **A2_FULL.** Every CORE and FULL target is clean.
- **A2_CORE.** Every CORE target is clean: the primary assembly (P1–P4), the finite-support deduction (J1, J2, J4), the content
  divisibility core (L1, L5), and all four regression countermodels (CM1, CM1′, CM2, CM3).
- **Failure.** Report the first exact unformalized statement, i.e. the first non-clean CORE-then-FULL target in
  `THEOREM_TARGETS.md` order, and the smallest sub-lemma you could not prove, stated in Lean.
- STRETCH targets (S1–S3) are optional.

## Rules
1. **You may invent intermediate lemmas**, in new files under `PrimarySupport/`.
2. **Seek complete formal proofs**, not translations.
3. **Keep every arithmetic input as the explicit hypothesis it is.**
   - In H2, the square-order hypothesis stands for the Cassels–Tate pairing, and the 2-, 3- and 5-parts stand for retained
     seed data.
   - Never try to prove anything about an elliptic curve.
4. **Do not strengthen assumptions.**
   - Do not edit `Defs.lean`, `Spec.lean`, `Acceptance.lean`, `lakefile.toml`, `lean-toolchain` or `scripts/level.py`
     (hashes in `scripts/FROZEN.sha256`).
   - Do not add hypotheses to targets.
   - If a target looks false, STOP and record the counterexample in `STATE.json`.
5. **Harmless abstraction is allowed**, provided you prove that it implies the packaged target.
6. **Test suspicious statements against the countermodels** CM1, CM1′, CM2, CM3 and CM4 (and S2, S3 if attempted).
   - They exist so that you cannot "prove" a false stronger theorem.
   - Examples: "each primary part finite ⇒ finite", "finite support ⇒ finite", "nonzero at every p ⇒ finite support",
     "finite local cokernels ⇒ bounded content", "FIN-type data ⇒ #G = 9".
7. **No `sorry`, `admit` or new `axiom`** in accepted theorems. Temporary admits must be removed; otherwise the target is FAILED.
8. **Keep `STATE.json` and `RESUME.md` updated.**
9. **Report the exact names of the clean theorems.** Run `bash scripts/acceptance.sh` (a clean build) before returning.
10. **Make no claim that FIN, Sha finiteness, or #Sha = 9 is proved.**

## Environment
Lean `leanprover/lean4:v4.28.0`, mathlib `v4.28.0` (`8f9d9cff6bd728b17a24e163c9402775d9e6a365`). If you cannot use this pin,
stop and report.

## Out of scope (NOT_PART_OF_THIS_TASK)
- The WC implication itself and the group-ring / augmentation algebra (package A1).
- Elliptic curves, Selmer groups, Ota's theorems and Cassels–Tate. Their consequences enter only as hypotheses.
- J_E ≠ 0 for any curve.
- FORMULA-side lemmas: rational reconstruction, Lemma E, the common certificate B.
- Genuine p-adic integers in Lemma B: the valuation model is exact (see `MATHEMATICAL_SPEC.md` §4).
