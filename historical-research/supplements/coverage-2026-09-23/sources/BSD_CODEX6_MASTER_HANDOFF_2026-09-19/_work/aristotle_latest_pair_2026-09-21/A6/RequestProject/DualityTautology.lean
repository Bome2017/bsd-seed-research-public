import Mathlib

/-!
# The global-duality Euler characteristic for `E[n]` is the product formula

This file machine-checks the combinatorial core of the following statement, proved in full in
`ARISTOTLE_A_RETURN.md` (Theorem A):

> For an elliptic curve `E/ℚ` and `n ≥ 1`, the Greenberg–Wiles global Euler-characteristic
> formula, applied to the self-dual Galois module `M = E[n]` with the Kummer local conditions
> `L_v = im(E(ℚ_v)/nE(ℚ_v) → H¹(ℚ_v, E[n]))`, degenerates to the identity `1 = 1`.  Concretely,
> the left-hand side `#Sel_L(M) / #Sel_{L^⊥}(M^∨)` equals `1` because `M ≅ M^∨` and each `L_v`
> is its own annihilator, while the right-hand side is `∏_v (#L_v / #H⁰(ℚ_v, M))`, and the local
> index is exactly `|n|_v⁻¹`.  The formula is therefore *equivalent to the product formula for
> `n`* and carries no arithmetic information about `#Sel_n(E)`.

The arithmetic inputs (self-duality via the Weil pairing; maximal isotropy of the local Kummer
image under Tate duality; `#(E(ℚ_v)/nE(ℚ_v)) = #E(ℚ_v)[n] · |n|_v⁻¹`) are classical and are cited,
not reproved, in the written argument.  What is verified here is the resulting numerical
bookkeeping — which is where the claim "global duality gives a quantitative bound" is refuted.
-/

namespace SeedBSD

open Finset

/-- **Product formula packaging.**  For `n ≥ 1`, the archimedean local index `1/n` times the
product of the finite local indices `|n|_p⁻¹ = p^{v_p(n)}` is `1`. -/
theorem local_index_product_one (n : ℕ) (hn : 0 < n) :
    (1 / (n : ℚ)) * ∏ p ∈ n.primeFactors, (p : ℚ) ^ (n.factorization p) = 1 := by
  have hnat : ∏ p ∈ n.primeFactors, p ^ (n.factorization p) = n := by
    have h := Nat.factorization_prod_pow_eq_self hn.ne'
    rwa [Finsupp.prod, Nat.support_factorization] at h
  have hcast : ∏ p ∈ n.primeFactors, (p : ℚ) ^ (n.factorization p) = (n : ℚ) := by
    calc ∏ p ∈ n.primeFactors, (p : ℚ) ^ (n.factorization p)
        = ((∏ p ∈ n.primeFactors, p ^ (n.factorization p) : ℕ) : ℚ) := by push_cast; ring
      _ = (n : ℚ) := by rw [hnat]
  rw [hcast]
  field_simp

/-- **Theorem A, verified core.**  Suppose given, for the module `M = E[n]`:

* archimedean data `Hinf = #H⁰(ℝ, M)` and `Linf = #L_∞`, satisfying `Linf = Hinf / n`;
* for each prime `p ∣ n`, data `H0 p = #H⁰(ℚ_p, M)` and `L p = #L_p` satisfying the local
  Kummer index formula `L p = H0 p · p^{v_p(n)}`;
* at every place off `n · ∞` the local index is `1` (so those factors are omitted).

Then the Greenberg–Wiles right-hand side `∏_v (#L_v / #H⁰(ℚ_v, M))` equals `1`.  Since the
left-hand side is `#Sel_L(M)/#Sel_{L^⊥}(M^∨) = 1` by self-duality, the formula is vacuous. -/
theorem greenberg_wiles_rhs_eq_one
    (n : ℕ) (hn : 0 < n) (H0 L : ℕ → ℚ) (Hinf Linf : ℚ)
    (hH0 : ∀ p ∈ n.primeFactors, H0 p ≠ 0) (hHinf : Hinf ≠ 0)
    (hlocal : ∀ p ∈ n.primeFactors, L p = H0 p * (p : ℚ) ^ (n.factorization p))
    (hinf : Linf = Hinf / n) :
    (Linf / Hinf) * ∏ p ∈ n.primeFactors, (L p / H0 p) = 1 := by
  have hprod : ∏ p ∈ n.primeFactors, (L p / H0 p)
      = ∏ p ∈ n.primeFactors, (p : ℚ) ^ (n.factorization p) := by
    refine Finset.prod_congr rfl ?_
    intro p hp
    rw [hlocal p hp, mul_comm, mul_div_assoc, div_self (hH0 p hp), mul_one]
  have hLinf : Linf / Hinf = 1 / (n : ℚ) := by
    rw [hinf]; field_simp
  rw [hprod, hLinf]
  exact local_index_product_one n hn

end SeedBSD
