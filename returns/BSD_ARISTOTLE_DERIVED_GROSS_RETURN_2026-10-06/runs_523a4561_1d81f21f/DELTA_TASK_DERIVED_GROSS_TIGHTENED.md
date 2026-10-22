# Delta task: a derived Gross identity over K = ℚ(√−7) (2026-10-06)

This project contains the canonical packet `BSD_SEED_FRONTIER_2026-10-06` (revision 2). Read `CURRENT_FRONTIER.md` first. **This file governs the run.** Every rule in the root `TASK.md` "Do not" list applies here.

## A correction to carry forward

**K = ℚ(√−7) is the definite case.**
- E^{−7} has analytic and algebraic rank 0. L(E^{−7},1) ∈ [9.054319, 9.054421] is certified (record K.2), and Ш(E^{−7}/ℚ) is finite.
- So ε(E/K) = +1, and rank E(K) = rank E(ℚ) = 2 with (r⁺, r⁻) = (2, 0).
- Hence ord_{s=1} L(E/K,s) = 2, and

  **L″(E/K,1) = L″(E,1)·L(E^{−7},1).**

The fixed nonzero twist factor here is the central value L(E^{−7},1), a rational multiple of its period. It is not a derivative. The formula L‴(E/K,1) = 3·L″(E,1)·L′(E^K,1) from the previous run (`2_CLOSED_LANES/RANK2_ANCHOR_RESULT.md`) belongs to the indefinite (Heegner) case, for example K = ℚ(√−23).

## The one question

Can the degree-two augmentation coefficient of the definite Gross-point (Mazur–Tate-type) theta element for E over K = ℚ(√−7) be related, by a proved algebraic identity, to det(⟨P_i, P_j⟩)_{i,j=1,2}? The pairing is a specified Mazur–Tate / tame height pairing on E(K)^+ = E(ℚ) = ⟨P₁, P₂⟩. The identity must have a normalization constant m_E ∈ ℚ^× that:
- is independent of p and of the auxiliary conductor;
- does not involve FIN, #Ш, any Selmer length, Q36 or the BSD quotient.

**Best case for the endpoint.** A Ш-free identity, combined with the record's per-prime definite detector (below), would give finite support of Ш at the primes the detector covers. That has the right cross-prime shape for the uniform step.

## Record facts for ℚ(√−7) (do not re-derive)

- **Definite-field gate (09-22).**
  - N⁻ must be an odd-size subset of {3, 2243, 5843}. For ℚ(√−7), N⁻ = {3, 2243, 5843}.
  - 2 (with v = 3) and 4547 (with v = 2) split.
  - The class number h(−7) = 1, so the conductor-1 Gross set is a single point.
  - The root-number condition holds automatically.
- **Per-prime definite detector** (record B.3 / M₂; conditional, written grade): for good ordinary p ≥ 5 with p ∤ 7N, a nonzero depth-two coefficient c₂(p) (M₂(p)) of the anticyclotomic object over ℚ(√−7) gives Ш[p^∞] = 0. It uses:
  - the Bertolini–Longo–Venerucci anticyclotomic main conjecture (Math. Ann. 2026): (L_p^ε) ⊆ (Char^ε), with equality except in the supersingular, inert, ε = + case;
  - Bertolini–Darmon derived heights.
- **M₂ cannot be computed.** It is open at every prime, and the Gross-point mass is about 5.4·10¹⁴.
- **BLV Remark 1.4** excludes the trivial character in the exceptional case. That is exactly where ord L(E/K,s) = 2 places this problem.
- **U22 (09-28/29, paused).** A GU(2,2) Klingen–Eisenstein family over ℚ(√−7), aimed at C₂ = u·det(h) with u independent of Ш.
  - Stage 1 (an exact identity) was built.
  - Codex audit verdict: OBSTRUCTION_NOT_ESTABLISHED, meaning an incomplete mechanism, not a kill.
  - First missing comparison: an explicitly normalized map from the automorphic extension to G2's secondary height.
  - Do not re-run U22's links without a new input; you may use its findings.
- **A known obstacle** (`3_LIVE_QUESTION/ADMISSION.md` §1). At every finite level, the I²/I³ class of a finite group ring lies in a finite group, so it has no ℚ-valued realization. A rational m_E can therefore come only from an identity that holds at every level with one constant. State any identity in that form.
- **Prior run (recorded; do not redo).** `2_CLOSED_LANES/RANK2_ANCHOR_RESULT.md`, R1–R5. Its R4 (definite Gross points) failed at step 3 because the trivial-character formula reads 0 = 0. This task asks the narrower degree-two question that R4 did not pursue.

## Stop conditions

1. **Define the object first.** Name:
   - the exact theta element: the Gross points, the quaternion algebra, and the order or level structure for N = 2³·3·2243·4547²·5843 (not squarefree);
   - the character family and the group ring;
   - the augmentation ideal I.

   Say which element, θ or θ·θ*, has its first nonzero coefficient in I²/I³, and why. Cite the printed theorem that makes it interpolate L(E/K,χ,1) at this level (Gross; Waldspurger; Yuan–Zhang–Zhang; Cai–Shu–Tian; or BLV's setup). Specify the height pairing on E(ℚ) and its normalization.
2. **No analytic hand-waving.** Derive the degree-two coefficient from Gross-point distribution relations or from a printed theorem.
3. **No Ш in the constant.** If the comparison constant contains #Ш, a Selmer length, Q36 or the BSD quotient, return `CIRCULAR_CONSTANT` and stop.
4. **No per-p rebuilding.** The target is one rational or integral object attached to the fixed seed and K = ℚ(√−7).
5. **No large computation.** Do not attempt the Brandt module or the Gross-point data at conductor ≈ 6.5·10¹⁵. This run is theoretical only.
6. **Admission.** The identity Θ^{(2)} = m_E·det(H(P_i, P_j)) in I²/I³ is necessary but **not sufficient**. See the tightened threshold below.

## Admission threshold for `DERIVED_GROSS_IDENTITY` (tightened 2026-10-07; governs grading)

`DERIVED_GROSS_IDENTITY` requires the **whole compatibility square**, not only its top row:

```
  Θ^{(2)}     =  m_E · det h(P₁,P₂)            (characteristic zero, every level, one m_E)
     ↓ φ_{p,ℓ}           ↓ φ_{p,ℓ}
  C₂(p,ℓ)     =  m_E · (a_ℓ − 2)·R_{p,ℓ}   (mod p)
```

for every relevant p outside **one explicit, fixed, finite exceptional set S**, with the vertical maps normalized independently of p and ℓ. All four interfaces must be present:

1. **A characteristic-zero degree-two identity**, holding at every level with one constant (the finite-level I²/I³ class alone has no ℚ-valued realization; `3_LIVE_QUESTION/ADMISSION.md` §1).
2. **A fixed m_E ∈ ℚ^×, Ш/FIN/Q36/BSD-free.**
   - **m_E ≠ 0 must be proved**, not conjectured. With m_E = 0 the bottom row is consistent with C₂ ≡ 0 and the detector never fires.
   - **The denominator of m_E must be explicitly controlled.** Write m_E = a/b in lowest terms and name the primes of b; they join the exceptional set.
   - A rational m_E whose numerator or denominator is itself defined using Ш, Q36 or BSD is circular even if it is independent of p. Return `CIRCULAR_CONSTANT`.
3. **Both specialization/reduction maps, with compatible normalizations.** Name the map sending Θ^{(2)} to C₂(p,ℓ) and the map sending det h to (a_ℓ − 2)·R_{p,ℓ}, and prove that they are the same map on the group where the top row holds (or differ by a factor that is **proved** to be a p-adic unit; see the next section).
4. **An explicit finite exceptional set S** such that, for p ∉ S with p ∤ b and G2's admissible ℓ (which must also satisfy whatever splitting condition the left map needs, e.g. ℓ split in K),

   Ш[p] ≠ 0 ⇒ C₂(p,ℓ) = 0 ⇒ m_E ≡ 0 (mod p) ⇒ p ∣ a = num(m_E).

   The logic of this step is formalized in `RequestProject/DerivedGross/Threshold.lean` (`finite_support_of_square`). The return must supply its hypotheses, not restate them.

Note: the bottom row says that Theorem W's scalar s_p = C₂/((a_ℓ − 2)R_{p,ℓ}) is ≡ m_E (mod p). So the full square delivers the exact Law (G1) with m = m_E (Lean `bottom_row_is_exact_law`).

## Unit ambiguity: return `IDENTITY_ONLY_UP_TO_P_UNIT` and say exactly where the unit sits

If the square is obtained only up to p-adic units, return `IDENTITY_ONLY_UP_TO_P_UNIT` (not `DERIVED_GROSS_IDENTITY`, not a failure status) and state, for every unit, **where it appears** and **what is proved about it**. Distinguish:

- **(U1) One multiplicative unit on the final congruence:** s_p = u_p·m_E with u_p ∈ ℤ_p^× proved. Then s_p ≡ 0 ⟺ m_E ≡ 0 (mod p), so pure support detection survives (Lean `single_unit_preserves_zero`). The exact residue law s_p ≡ m_E, and consistency with the eleven 288 residues, do not follow.
- **(U2) Separate units on the two vertical maps:** Θ^{(2)} ↦ u_{p,ℓ}·C₂ and det h ↦ v_{p,ℓ}·(a_ℓ − 2)R_{p,ℓ}.
  - If **both** u_{p,ℓ} and v_{p,ℓ} are proved to lie in ℤ_p^× under the normalization in which the top row holds, their quotient is a unit and support detection survives (Lean `proved_units_preserve_zero`).
  - If either is only known to be a scalar in ℤ_p or ℚ_p (not proved to be a unit), or the two maps are normalized independently so that the top row is not transported by one map, the square does **not** establish the bridge (Lean `uncontrolled_factor_no_detection`). This case is **not** `IDENTITY_ONLY_UP_TO_P_UNIT`; grade it by its first missing interface.
- **Free units with a Ш-defined constant** are the existence form of the Law, which is FIN restated (`3_LIVE_QUESTION/STATUS.md` §1). The circularity there comes from the choice of m, not from the unit. With m_E Ш-free and proved nonzero, (U1) or proved-unit (U2) still gives finite support.

## Return exactly one status

`DERIVED_GROSS_IDENTITY` (all four interfaces above) · `IDENTITY_ONLY_UP_TO_P_UNIT` (with the U1/U2 location of every unit) · `REDUCTION_TO_ONE_NEW_THEOREM` · `CIRCULAR_CONSTANT` · `NO_DEGREE2_IDENTITY` · `PRECISE_OBSTRUCTION`

## Do not (in addition to the canonical list)

- W3, OpenAI Result 002 transplants, the rank-two determinant switch, the plectic framework, the exceptional primes, or any per-prime computation.
- A literature survey without a specific candidate identity to test.
- Redoing R1–R5 of the previous run.

## Return format

As in the canonical `TASK.md`:
- one STATUS line;
- for `DERIVED_GROSS_IDENTITY` or `IDENTITY_ONLY_UP_TO_P_UNIT`: a four-row table (interfaces 1–4), each row labelled PROVED, IMPORTED or HEURISTIC, plus m_E = a/b, a proof that m_E ≠ 0, the primes of b, and the set S written out;
- for any other status: the first of interfaces 1–4 that fails;
- every claim labelled PROVED, IMPORTED or HEURISTIC;
- Lean with no `sorry`, plus `#print axioms` for every new theorem;
- end with "FIN, ORDER9 and Q36: unchanged", or a precise statement of what changed.
