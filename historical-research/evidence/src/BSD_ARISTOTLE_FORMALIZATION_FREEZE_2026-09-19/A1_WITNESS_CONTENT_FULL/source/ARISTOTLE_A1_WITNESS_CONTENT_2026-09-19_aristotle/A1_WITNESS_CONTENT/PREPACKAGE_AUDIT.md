# PREPACKAGE_AUDIT — A1 (hostile, done before tarring; 2026-09-19)

1. **Target reconstructed from Codex's proof** (WITNESS_CONTENT_THEOREM §1–§2). T7 has exactly the conclusions (1), (2), (3)
   of Theorem WC, with S0, P, the S-family, depth, h_p and J_E as in §1. Three deliberate formal differences:
   - Ota 5.17 enters T7 in *witness form*. The printed group-ring form is used in T8, and the bridge T4 proves that it
     implies the witness form.
   - "M(p,S) finite p-primary" is used only through "killed by a power of p" (bounded exponent), which is what makes depth
     well defined. T3 proves bounded exponent for I²/I³ over any ring in which prime-to-p integers are units, and T10 shows
     that ℤ_[p] is such a ring.
   - The admissible family is an abstract index type `W p`.
2. **Hidden use of J_E ≠ 0: none.** The antecedent is only the explicit hypothesis `A ≠ 0 ∧ A ∈ JE …` (tag
   NOT_PART_OF_THIS_TASK). No definition presupposes it.
3. **Hidden use of FIN: none.** Finiteness of Sha[p^∞] (p ∈ P), vanishing for p ∤ A, and global finiteness are all
   *conclusions*; the last is conditional on the S0 hypothesis. The only finiteness-flavoured premise is the Selmer fact
   "infinite ⇒ corank ≥ 3" (IMPORTED).
4. **Finite support vs local finiteness: kept apart.** They are separate conclusions (1), (2), (3), and the regression
   targets T9a and T9b refute "nonzero at every p ⇒ finite support".
5. **Finite and formal enough for Aristotle.**
   - No elliptic-curve object appears.
   - All statements compile against mathlib v4.28.0.
   - Every target was checked true on paper, including edge cases (e = 0, a = 0, p = 0/1, empty W p, the junk branches of
     `depth` and `cls2`).
   - The non-vacuity target T12 guards against contradictory hypotheses.
6. **Simplifications (each documented; none changes a claim).**
   - Lemma A is required for commutative G; Codex's general-G version is stretch S1.
   - Bounded exponent replaces finiteness.
   - `W p`, `Rp p` and `G p S` are abstract, with instantiation targets T10 and T11.
7. **Counterexamples to stronger false statements.** Included as Lean targets: T9a (uniform denominators), T9b (nonzero at
   every prime ⇏ J_E ≠ 0), and T12 (non-vacuity).

## Issues discovered while packaging (recorded, not resolved)
- **D1 — S-class of Ota's Theorem 6.4.**
  - The body's Theorem 6.4 is stated for "S as in Theorem 6.1": cyclic E(F_ℓ)[p′] for EVERY prime p′ not invertible in R.
  - Codex's witness family (ℓ ≡ 1 mod p, E(F_ℓ)[p] cyclic) matches the introduction's **Theorem 1.5**, which Ota calls a
    special case of 6.4. This package imports Theorem 1.5 as printed.
  - This is a provenance nuance for the *arithmetic meaning* of J_E, not a gap in the formal implication, because `W p` is
    abstract. Under the stricter class, J_E can only shrink.
- **D2 — normalisation.** Ota's §2 θ̃ uses ½θ on the "+" quotient; Theorems 1.5 and 6.4 use θ in I^r/I^(r+1). At odd p no
  depth changes.
- **D3 — base change** from R ⊂ Q to Z_p (FORMAL_ASSUMPTION F1). Standard; not formalized.
- **D4 — p-integrality of θ_S** at p ∈ P (IMPORTED; the seed's denominators are powers of 2).

## Statements deliberately not formalized here
- **LINE ⇒ WC:** not needed (user instruction).
- **Codex's rank-two contraction** (FORMALIZABLE_GAPS A2): not in this split.
- **Integral lattice content** (A3): moved to package A2.
- **Finiteness of M(p,S):** replaced by bounded exponent. Finiteness over ℤ is stretch S2.
- **Everything arithmetic:** entered as hypotheses.

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced.
