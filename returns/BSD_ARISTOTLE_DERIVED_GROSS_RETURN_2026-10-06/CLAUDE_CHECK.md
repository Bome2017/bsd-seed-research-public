# Independent check of the derived-Gross returns (Claude, Opus 5.5, 2026-10-06)

**Archives received**
- `cb9ad0a0-…-aristotle.tar.gz` (sha256 0fbfd81e…): run 74e483e4.
- `0cd74d26-…-aristotle.tar.gz` (sha256 a3f5d81e…): run 523a4561 (an independent second run) and run 1d81f21f (the regrade).

**Integrity**
- cb9ad0a0: every submitted file is unchanged except `lakefile.toml` (adds a `DerivedGross` library) and `README.md` (Aristotle's banner). The delta task is unchanged.
- 0cd74d26: 43 of the 48 submitted files are byte-identical. The five that differ are the ones the regrade says it changed: the delta task, the prompt, the submit command, the manifest and the README banner.

**Independent compile.** Read-only, Lean v4.28.0, Mathlib 8f9d9cff.
- `run_74e483e4/DerivedGross/Parity.lean` (46 s) and `Threshold.lean` (7 s): exit 0, no errors, no warnings. All 23 theorems use only {propext, Classical.choice, Quot.sound}.
- `runs_523a4561_1d81f21f/RequestProject/DerivedGross/Threshold.lean` (25 s, 5 theorems) and `Obstruction.lean` (7 theorems plus the lemma `add_invol_sub_mem_sq`): exit 0, no errors, no warnings. All declarations use a subset of {propext, Classical.choice, Quot.sound}; `degenerate_identity_forces_zero` uses none.
- None of these files contains `sorry`, `native_decide` or a new `axiom`.

**The mathematics checked**
- **Route A is vacuous.** This was verified by hand.
  - Complex conjugation inverts Gal(K[ℓ]/K), since ring-class fields are dihedral over ℚ, and it fixes P₁, P₂ ∈ E(ℚ). Equivariance gives 2⟨P,Q⟩ = 0 in G ⊗ ℤ_p, so the pairing vanishes for odd p.
  - So det H ∈ I³ at every level. The identity Θ⁽²⁾ = m_E·det H holds for any m exactly when Θ⁽²⁾ = 0, and no m_E is ever fixed.
  - This is the classical fact that anticyclotomic heights pair E(K)⁺ with E(K)⁻. Here E(K)⁻ = E^{−7}(ℚ) has rank 0.
- **The two runs agree on the substitute and on the gap.**
  - G2's cyclotomic pairing is the only well-typed nonzero substitute, and it transfers to degree two at split ℓ.
  - Neither a printed theorem nor a distribution relation produces the identity: distribution relations stop at degree one.
  - Every known normalization of the constant involves #Ш(E/K) or the BSD quotient. This point is labelled HEURISTIC in the returns.
- **Regrade.** It confirms the four-interface threshold. One correction it makes is accepted: for zero detection, two separately *proved* units are as good as one. What breaks detection is any factor that is not proved to be a unit.
- **Labels.** Arithmetic inputs appear in the Lean files as hypotheses. The equivariance of the pairing is IMPORTED (Mazur–Tate / Tan). The + sign of the functional equation, giving θ ∈ I² and θθ* ∈ I⁴, is HEURISTIC in 74e483e4.

**Scope.** Together with the rank-two-anchor return, the imaginary-quadratic anchors are now closed in both settings:
- Heegner (ε = −1): 0 = 0 to third order;
- definite (ε = +1): the anticyclotomic pairing vanishes on E(ℚ).

This is a scoped negative for the constructions tested. It is not an impossibility claim.

FIN, ORDER9 and Q36 are unchanged.
