# Summary of changes for run 1d81f21f-6dbc-4aa9-a218-2d5efb80cad2
The package now uses your tightened threshold. The earlier run under the old threshold had already finished, and its return (`DERIVED_GROSS_RESULT.md`) is unchanged. Regraded against the new threshold, the status is still **PRECISE_OBSTRUCTION**, not `IDENTITY_ONLY_UP_TO_P_UNIT`.

**Package changes**
- `DELTA_TASK_DERIVED_GROSS.md` has a new "Admission threshold" section. `DERIVED_GROSS_IDENTITY` now needs the whole compatibility square and all four interfaces:
  1. a characteristic-zero degree-two identity at every level, with one constant;
  2. a fixed \(m_E = a/b\) that is Ш/FIN/Q36/BSD-free, with \(m_E \neq 0\) proved and the primes of \(b\) named;
  3. both reduction maps, with one compatible normalization;
  4. an explicit finite set \(S\) such that \(Ш[p]\neq0 \Rightarrow p \mid a\) outside \(S\) and the primes of \(b\).
- A new "Unit ambiguity" section adds `IDENTITY_ONLY_UP_TO_P_UNIT`. The return must say where every unit sits:
  - (U1) one unit on the final congruence;
  - (U2) separate units on the two vertical maps.
- The return format now requires a table of the four interfaces, or else the first interface that fails.
- `SUBMISSION_PROMPT.txt` and `SUBMIT_COMMAND.txt` carry the same threshold. `README.md` and `MANIFEST.sha256` are updated. Nothing has been submitted.

**Correction to the U1/U2 split (PROVED in Lean).** For zero/nonzero detection mod \(p\), the number of units doesn't matter. What matters is whether the total discrepancy \(v_{p,\ell}/u_{p,\ell}\) is a *proved* \(p\)-adic unit.
- If each of the two separate units is proved to be a unit, detection survives, just as with one unit (`proved_units_preserve_zero`).
- A factor that is not proved to be a unit, or two maps normalized independently, gives no detection (`uncontrolled_factor_no_detection`). The package now states the split this way.
- The existence form of the Law (free units) is FIN restated because its constant can be built from the Ш-support. With a Ш-free \(m_E\) that is proved nonzero, a result up to proved units still gives finite support. It does not give the exact Law or the 288 residues.

**Regrade (`THRESHOLD_REGRADE.md`)**
- **Canonical anticyclotomic pairing:** its determinant is identically zero on E(ℚ), so the top row of the square is degenerate.
- **G2's cyclotomic pairing (the candidate):**
  - Interface 1 fails: no derivation exists.
  - Interface 2 fails: no \(m_E\) is defined; this is HEURISTIC.
  - Interface 3 fails on its own. The right-hand map \(\det h\mapsto R_{p,\ell}\) exists, but nothing maps \(\Theta^{(2)}\) to \(C_2(p,\ell)\). The two degree-two groups are identified canonically, but the elements are not: one interpolates anticyclotomic L-values of E/K, the other Dirichlet twists of E/ℚ.
- Some unit factors are already proved harmless: \(a_\ell-2\equiv-4\), a change of generator, and the choice of prime above \(\ell\).
- Two further points (PROVED logic):
  - The bottom row is exactly Theorem W's \(s_p \equiv m_E\), i.e. the exact Law G1.
  - Read with the Ota detector, the square would not need ordinary \(p\).

**Lean (`RequestProject/DerivedGross/Threshold.lean`).** It builds with no `sorry`. Each theorem depends only on propext, Classical.choice and Quot.sound.
- `finite_support_of_square`: the four interfaces give \(Ш[p]\neq0\Rightarrow p\mid a\) outside \(S\) and the primes of \(b\), hence finite support.
- `bottom_row_is_exact_law`
- `single_unit_preserves_zero`
- `proved_units_preserve_zero`
- `uncontrolled_factor_no_detection`

These theorems prove only the logic. Every arithmetic interface enters as a hypothesis, and none of them is supplied for the seed.

FIN, ORDER9 and Q36: unchanged.

# Summary of changes for run 523a4561-aea4-4632-b1e0-dbb3c48d247e
**STATUS: PRECISE_OBSTRUCTION.** I found no proved identity relating the degree-two coefficient to a height determinant with a Ш-free constant, and I am not claiming one. The full return, with every claim labelled PROVED, IMPORTED or HEURISTIC, is in `DERIVED_GROSS_RESULT.md`. The Lean file is `RequestProject/DerivedGross/Obstruction.lean`. It builds, contains no `sorry`, and uses only the standard axioms.

**The objects (§1 of the return).**
- **Algebra and order:** B is the definite quaternion algebra ramified at {3, 2243, 5843, ∞}, with an Eichler order of level \(N^+ = 2^3\cdot 4547^2\).
- **Gross points:** the Gross set X has a primitive integer-valued Jacquet–Langlands eigenfunction f, and x₁ is the single conductor-1 point (h(−7) = 1).
- **Group and theta element:** \(G_\ell = \mathrm{Pic}(O_\ell)\) is cyclic of order \(\ell - (-7/\ell)\). The theta element is \(\theta_\ell = \sum_\sigma f(x_\ell^\sigma)\,\sigma\), and I is the augmentation ideal.
- **Interpolation (IMPORTED):** the explicit Waldspurger formula of Gross, Zhang and Cai–Shu–Tian. I did not check exact theorem numbers.

**Why θ, not θθ\*, starts in I²/I³ (the key steps are PROVED in Lean, using imported inputs).**
- **θ₁ = 0:** the formula at the trivial character, together with L(E,1) = 0, gives this.
- **θ_ℓ is in I:** the distribution relation gives aug(θ_ℓ) = (a_ℓ − 2)·θ₁ for split ℓ, and a_ℓ·θ₁ for inert ℓ. Both are 0.
- **θ_ℓ is in I² for odd p:** a general group-ring theorem shows that if 2 is invertible, θ is in I and θ\* = σ·θ, then θ is in I². This assumes the functional equation has sign +; that sign is IMPORTED/HEURISTIC.
- **Consequence:** θθ\* lies in I⁴, so its degree-two coefficient is zero.

**The obstruction (§2).**
1. **The canonical pairing gives zero (PROVED).** The pairing naturally attached to \(G_\ell\) is the anticyclotomic tame Mazur–Tate pairing. Complex conjugation turns it into its negative, so it vanishes on E(ℚ) = E(K)⁺ for every odd p, and its determinant is identically zero. This uses the pairing's standard functoriality, which is IMPORTED. An identity Θ⁽²⁾ = m_E·det(H) with this pairing is therefore either 0 = 0 or false.
2. **G2's cyclotomic pairing fits, but no identity produces it (PROVED).** For split ℓ, the degree-two pieces of the anticyclotomic and cyclotomic groups are identified canonically: the identification does not depend on the choice of prime above ℓ, because (−a)⊗(−a) = a⊗a. So the candidate Θ⁽²⁾ = m_E·det(H^cyc) is well-typed. However:
   - Distribution relations and the functional equation stop at degree one.
   - The interpolation formula has no Mordell–Weil side.
   - No printed theorem computes Θ⁽²⁾ from E(ℚ).
   - The first missing arrow is a comparison between the second derived anticyclotomic height and the cyclotomic height, with a single constant valid at every level.
3. **The constant (HEURISTIC).** Every printed or conjectural normalization of such an identity uses either #Ш(E/K) or the BSD quotient of E/K, which is q·L(E^{−7},1)/Ω′. I did not return CIRCULAR_CONSTANT because there is no proved identity whose constant could be checked; the failure comes earlier.
4. **The candidate is not a weaker reduction (PROVED bookkeeping).** Combined with G2 and the per-prime definite detector, the candidate would give Ш[p^∞] = 0 at all but finitely many good ordinary p. So it is at least as strong as the ordinary part of FIN-tail, and it says nothing at supersingular p. That is why the status is not REDUCTION_TO_ONE_NEW_THEOREM.

**Lean theorems** (output of `#print axioms` is listed in the return):
- `mem_augIdeal_sq_of_functional_eq`
- `add_invol_sub_mem_sq`
- `pairing_vanishes_on_fixed`
- `gram_det_eq_zero_of_anti`
- `sq_tmul_sign_invariant`
- `augmentation_vanishes`
- `degenerate_identity_forces_zero`
- `ordinary_bad_primes_finite_of_identity`

Each depends on at most propext, Classical.choice and Quot.sound. All arithmetic inputs appear as explicit hypotheses, and nothing in the file states anything about Ш of the seed.

FIN, ORDER9 and Q36: unchanged.