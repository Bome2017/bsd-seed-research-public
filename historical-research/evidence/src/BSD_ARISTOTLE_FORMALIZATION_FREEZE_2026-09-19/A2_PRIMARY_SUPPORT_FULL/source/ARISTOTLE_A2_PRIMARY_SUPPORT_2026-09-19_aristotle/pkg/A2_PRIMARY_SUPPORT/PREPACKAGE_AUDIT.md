# PREPACKAGE_AUDIT — A2 (hostile, done before tarring; 2026-09-19)

1. **Targets reconstructed from the Codex sources**:
   - B3 (primary assembly);
   - WC §1 (the J_E characterisation and its generator);
   - A3 plus WC §4 "Descent to Z" (content);
   - §B (Lemma B);
   - §H (order consequence and countermodel).
   Each Lean statement matches the prose. The only form changes are the valuation model of Lemma B, and the square-order
   input of §H as an explicit hypothesis.
2. **Hidden J_E ≠ 0: none.** J2 characterises when J ≠ 0. L7 derives J ≠ 0 only from an explicit primitive-content comparison
   hypothesis, which is the missing arithmetic input (NOT_PART_OF_THIS_TASK).
3. **Hidden FIN: none.** H2 carries `[Finite G]` explicitly (a statement under FIN), and its conclusion is only 9t², optimal by
   CM4. Nothing else assumes finiteness.
4. **"Each primary part finite" vs "finitely many nonzero": separated.** P5 is the exact conjunction; CM1 and CM1′ show that
   neither part suffices alone.
5. **Finite and formal enough for Aristotle.**
   - Pure group theory and elementary number theory; everything compiles against mathlib v4.28.0.
   - Every target was checked true on paper, including edge cases: n = 0, z = 0, m = 0, k = 0, non-primes via `P ⊆ primes`,
     ZMod 0 / ZMod 1.
6. **Simplifications.**
   - Lemma B uses the valuation model, which is exact because d_p Z_p = p^{v_p} Z_p.
   - Codex's pairing-decorated torsion example is stretch S3; the simpler CM1 does the separation.
7. **Counterexamples to stronger false statements**: CM1, CM1′, CM2, CM3, CM4 (required) and S2 (the cyclic-target trap).

## Issues discovered while packaging
- **D5 — the square-order consequence needs a cyclic pairing target.**
  - The tempting abstract statement "nondegenerate alternating pairing ⇒ square order" is FALSE for non-cyclic targets
    (S2: cross product on (ZMod 2)³, order 8).
  - Codex's Lemma H is correct because the Cassels–Tate pairing is ℚ/ℤ-valued. S1 therefore uses target ZMod N.
- **D6 — Lemma B clause (4)** (inverting all nonzero integers in ∏ Z_p) is equivalent but not separately formalized.

## Statements deliberately not formalized here
- **Codex's FORMULA-side B1, B2 and B4** (spacing, polynomial separation, common certificate): not in this split.
- **The WC implication and the group-ring algebra:** package A1.
- **Genuine ℤ_[p]-valued Lemma B:** replaced by the exact valuation model.
- **The rank-two contraction.**

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced.
