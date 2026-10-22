# Independent check of the fixed-1-motive return (Claude, Opus 5.5, 2026-10-06)


- **Package version.** It ran **revision 1** (lab d07feae). Its `DELTA_TASK_1MOTIVE.md` hash is 13dd7454…, which is the revision-1 file. Revision 2, with `NO_CANONICAL_GENERATOR` (d23a02cb…), was not used.
- **Integrity.** MANIFEST: 47 of 48 entries verify. The only mismatch is `README.md`: Aristotle's banner, and with it stripped the hash matches. New files: `ONE_MOTIVE_RESULT.md`, `ARISTOTLE_SUMMARY.md`, `RequestProject/OneMotive/Skeleton.lean`. The packet is otherwise unchanged.
- **Lean.**
  - `Skeleton.lean` compiles read-only in 43 s, exit 0, with no errors, warnings or `sorry`.
  - It uses the Lean module syntax (`module`, `public import Mathlib`), which compiles under v4.28.0.
  - All 24 declarations use exactly {propext, Classical.choice, Quot.sound}.
- **Claim audit (all checked; sound).**
  - **Step 1, Theorem 1 (PROVED).** Sel(ℚ,M_E)(n) ≅ Ш(E/ℚ)[n] for every odd n; for n = 2 it is an extension by ℤ/2. The only inputs are saturation (record) and Chebotarev. This is the same proof I sketched in the pre-check, and Pro reached it independently.
    - Correction accepted: the 1-motive's local condition at p is *rationally strict*, not Bloch–Kato.
  - **Step 2.** BSS / Sakamoto fail (Lean). This agrees with the pre-check.
  - **Step 3 (Macias Castillo–Sano, TeX source read).**
    - Hypothesis 2.11(i) and (iv) hold at odd p ∉ S.
    - The receiver's own condition fails 2.11(ii), because H⁰(ℚ_p, T_pM_E) has rank one. This is the local form of the fine-Selmer line.
    - The ordinary datum T⁻ = T_pẼ satisfies 2.11 at good ordinary non-anomalous p, with χ = 0.
    - **At supersingular p no χ = 0 datum passes**, and there are infinitely many such p.
    - The core-vertex Hypothesis 2.17 is open.
    - The Cartier dual gives the dual line. The ordinary datum of G2's 𝓜 fails 2.11(ii).
  - **Step 4.** det RΓ̃(T_pM_E) ≅ det RΓ̃(T_pE) ⊗ det RΓ̃(ℤ_p)^{⊗2}. Acyclicity ⟺ Ш[p^∞] finite ∧ det H_p ≠ 0. #H̃² = #Ш[p^∞]·p^{v_p(det H_p)}. This is the standard p-adic BSD Euler characteristic; it is PROVED modulo the identification of the connecting map δ₁ with the cyclotomic p-adic height (Nekovář, IMPORTED).
  - **Steps 5–6.** The only element intrinsic to M_E is the acyclicity trivialization. Its index carries the **wild p-adic regulator**, and it exists only under Ш[p^∞] finite plus Schneider nondegeneracy. A fixed A_M would force p-unit p-adic regulators almost everywhere. Any #Ш-free normalization is the ETNC / leading-term one (q); dividing out the tame regulator instead gives s_p, which is G1.
- **Link to today's other return.** The special value attached to the MCS line is the p-adic leading term, i.e. W3's ℓ₂ branch. The W3 return (9a3a411e) gives a concrete false alarm: at p = 17, ℓ₂ ≡ 0 because the regulator is 17-divisible, while Ш[17] = 0. So the MCS line of M_E is the record's W3 / ℓ₂ route in 1-motive form ("bridge without control"). It also has the supersingular gap.
- **Regrade under revision 2.** Under revision 2 the status is `NO_CANONICAL_GENERATOR`:
  - the framework applies as far as Hypothesis 2.11 (ordinary datum);
  - the line is computed;
  - the only intrinsic element is not proved to exist unconditionally.

  At supersingular p the status is `HYPOTHESES_FAIL`. Aristotle's `ETNC_CIRCULAR` is correct as the globalization finding. **No re-run is needed**: the substance does not depend on which revision ran.

FIN, ORDER9 and Q36 are unchanged.

## Fixed 1-motive run, revision 2: a6077c4a (received 10-06 night; sha256 1374be99…; 52 entries)

- **Package version.** Revision 2: the delta hash is d23a02cb…, and the delta contains `NO_CANONICAL_GENERATOR`.
- **Integrity.** MANIFEST: 47 of 48 entries verify. The only mismatch is the README banner; with it stripped the hash matches. New files: `RequestProject/OneMotive/{RESULT.md, Skeleton.lean}` and `ARISTOTLE_SUMMARY.md`. Nothing else changed.
- **Lean.** `Skeleton.lean` (146 lines) compiles read-only in 28 s, exit 0, with no errors or warnings and no `sorry`, `native_decide` or `axiom`. Its 5 theorems use subsets of {propext, Classical.choice, Quot.sound}; `two_torsion_div_odd` uses only propext.
- **Verdict: `NO_CANONICAL_GENERATOR`, confirmed.** It stops at step 5, as revision 2 requires. This independently replicates run 2318738a and matches my regrade of it.
- **Agreement with run 1:**
  - Theorem 1 (Sel(ℚ,M_E)(n) ≅ Ш[n] for odd n). This run uses Minkowski in place of Chebotarev; both are valid.
  - The same table of Greenberg choices for Hypothesis 2.11: four fail (ii); L gives χ = −2; T′ gives χ = 0; relaxed gives χ = 1.
  - Hypothesis 2.17 open.
  - The determinant line is E's own line.
  - #H² = #Ш[p^∞]·|Reg_p^int|⁻¹.
  - The only intrinsic element is the tautological ϑ_p.
- **New relative to run 1:**
  - The Harari–Szamuely condition is strict on the lattice quotient at every place, so it is not unramified almost everywhere and never forms a Mazur–Rubin / Nekovář structure.
  - Macias Castillo–Sano have no τ or irreducibility hypothesis; the obstruction reappears only through Hypothesis 2.17.
  - For χ = −2 there is no core vertex in 𝒩(𝒫), via the class [p] ⊗ w.
  - The Cartier dual's Selmer group contains (ℚ^×/p)², so it is infinite.
  - **§4.5:** the mod-p group of the admissible receiver is nonzero ⟺ Ш[p] ≠ 0 or p | Reg_p^int. So the admissible receiver differs from the step-1 receiver exactly at regulator-divisible primes.
  - Correction accepted: G2's torus quotient is [ℤ² → E] with e_i ↦ 16P_i, a 2-power isogeny away; T_p is the same for odd p.
- **The (f) disagreement is only apparent.**
  - Run 1: H¹_f(ℚ,V_pM_E) ≅ V_pШ holds for Bloch–Kato conditions, which are outside the framework.
  - Run 2: for the framework's conditions, H¹_F = V_pШ ⊕ ker h_p.
  - Both are right, for different local conditions.
- **Cross-check against the record at p = 17 (HEURISTIC; uses the W3 floating-point ℓ₂ and imported p-adic BSD inputs).**
  - Ш[17] = 0 and s₁₇ ≡ 288 ≡ 16 (mod 17), a unit. So ord₁₇ x_{ℚ,Σ} = 0.
  - W3 gives ℓ₂ ≡ 0, so ord₁₇ Reg₁₇^int ≥ 1.
  - Hence ord₁₇ ϑ₁₇ ≥ 1 > 0 = ord₁₇ s₁₇. The wild element and the tame scalar differ at 17, and ϑ raises a false Ш alarm there.

FIN, ORDER9 and Q36 are unchanged.

## Correction (2026-10-07, accepted from Codex, lab bb6ed896)

Both 1-motive returns, and this check, identified ℚ(M_E[p]) = ℚ(E[p], p⁻¹P₁, p⁻¹P₂) with the record's class-group receiver field L_p. **They are not the same field**: the retained receiver uses a larger field. Theorem 1, Sel(ℚ,M_E)(p) ≅ Ш[p], does not use that equality and stands. Only the displayed field identification is withdrawn.
