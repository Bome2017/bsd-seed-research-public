# KNOWN_TRAPS — A1

1. **"Nonzero witness at every prime ⇒ finite prime support (J_E ≠ 0)" is FALSE.**
   - Nonzero witnesses bound nothing uniformly: h_p = 2 at every p gives J = {0}.
   - Regression: `CM_uniform_denominator`, `CM_nonzero_everywhere`.
2. **Uniform source denominators do not control image content.**
   - Integral maps n ↦ p²n from a denominator-free source already give depth 2 everywhere (Codex WC §4).
   - Any proof idea of the form "the source is integral, hence the witnesses have bounded depth" is refuted.
3. **Depth of zero.** `depth p 0 = sSup ℕ = 0` is a junk value. Zero is divisible by every p^j (`zero_infinitely_divisible`).
   `hInf` only ranges over nonzero witnesses; keep it that way in every argument.
4. **h_p = ⊤** exactly when every witness at p vanishes. A ≠ 0 in J_E forces h_p < ⊤ at every p ∈ P, which is conclusion (1).
5. **Depth 0 vs nonzero.**
   - `t ≠ 0` gives only local *finiteness* (via 5.17 + Selmer).
   - `¬ PDvd p 1 t` (t ∉ pM) gives *vanishing* Sha[p] = 0 (via Ota 1.5).
   - Do not conflate: nonzero witness, valuation zero, bounded valuation, finite Sha[p^∞], zero Sha[p^∞].
6. **Sha[p] = 0 vs Sha[p^∞] = 0.**
   - The first implies the second by induction on k in p^k • x = 0.
   - "Sha[p^∞] finite" does not imply "Sha[p] = 0".
7. **min(r, p).** Ota 5.17 gives the exponent min(r_{p^∞}, p), not r. You need p ≥ 3 (from 2 ∈ S0) to conclude
   min(r, p) ≥ 3 from r ≥ 3.
8. **cls2 junk.** `cls2 θ = 0` when θ ∉ I². Under hypothesis H11 with r ≥ 2 and p ≥ 3, θ ∈ I² always holds (T4). Never
   use the junk branch as information.
9. **Rationalising finite augmentation quotients kills them** (Lemma A: ℚ ⊗ I^r/I^(r+1) = 0 for finite G).
   - Do not try to "lift the leading term to characteristic zero" as a shortcut.
   - This does not forbid completed or derived lifts (Codex stop rule 9).
10. **Do not prove or assume the antecedent.** `A ∈ J_E`, `J_E ≠ 0`, or any "uniform integral comparison" stays a hypothesis.
11. **Do not import LINE.** WC is strictly weaker than LINE (Codex WC §3); "LINE ⇒ WC" is not a target.
12. **The S-class of Ota Thm 6.4 vs Thm 1.5.**
    - The package imports Thm 1.5, which uses the S-class ℓ ≡ 1 (mod p), E(F_ℓ)[p] cyclic. This is Codex's family.
    - If you ever instantiate W p concretely, do not silently switch to Thm 6.4's stronger class (see SOURCE_EXCERPTS).
13. **A compiled WC is not FIN.** Formalizing WC proves only the implication from the stated witness-content antecedent.
    It does not establish that the antecedent is easier than FIN or that FIN has been reduced.
14. **Noncommutative powers (S1 only).** For non-commutative G, work with ℤ-submodule powers (`augSubZ`). `Ideal` powers
    over a non-commutative ring are not what the statement uses.
15. **ℕ-smul vs ring multiplication.** `e • x` is ℕ-smul (repeated addition). In `MonoidAlgebra R G`, `e • x = (e : R[G]) * x`
    (`nsmul_eq_mul`).
