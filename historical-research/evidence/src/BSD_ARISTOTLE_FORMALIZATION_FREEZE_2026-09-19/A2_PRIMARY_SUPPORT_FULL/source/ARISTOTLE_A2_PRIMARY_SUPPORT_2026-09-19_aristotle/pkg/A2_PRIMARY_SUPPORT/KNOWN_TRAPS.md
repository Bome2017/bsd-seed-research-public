# KNOWN_TRAPS — A2

1. **"Every primary part finite ⇒ finite" is FALSE** (CM1: ⨁_p ZMod p). You also need finite support.
2. **"Finite support ⇒ finite" is FALSE** (CM1′: ℕ →₀ ZMod 2). You also need every primary part finite. P5 states the exact
   conjunction.
3. **"A nonzero local witness at every prime ⇒ finite prime support" is FALSE** (CM2: depth 2 at every p gives J = {0}).
4. **"Perfect complex over ∏ Z_p with finite local defects ⇒ finite global defect / bounded content" is FALSE** (CM3, Lemma B).
   The distinction between a perfect ℤ-complex and a perfect profinite complex carries the whole argument (Codex FIN_ATTACK §C).
5. **"FIN ⇒ #Sha = 9" is FALSE.** Under the stated hypotheses the order is 9t² with gcd(t, 30) = 1 (H2), and t = 7 occurs (CM4).
6. **Square order needs a CYCLIC pairing target.** A nondegenerate alternating pairing into a non-cyclic group does not force
   square order (S2: cross product on (ZMod 2)³, order 8). Cassels–Tate is ℚ/ℤ-valued.
7. **padicValInt junk.** For non-primes and for 0 its values are junk. Every J- and content-target assumes primes and handles
   0 via `vInf` / `z ≠ 0`.
8. **Content conventions.** `Finset.gcd` over ℤ is normalized (≥ 0), and gcd(∅) = 0. For n = 0 the only vector is 0.
9. **ZMod edge cases.** ZMod 0 = ℤ is infinite; ZMod 1 is trivial. In L6, k = 0 makes both sides trivially true. In B2, v p = 0
   gives the trivial factor ZMod 1.
10. **Do not strengthen H2 to #G = 9, and do not drop `[Finite G]`.** H2 is a statement under FIN.
11. **Do not assume or prove J_E ≠ 0** for any concrete depth function, and do not construct the "primitive comparison" of L7.
12. **A compiled support/assembly theory is not FIN.** Formalizing WC proves only the implication from the stated
    witness-content antecedent. It does not establish that the antecedent is easier than FIN or that FIN has been reduced.
