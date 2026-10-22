module

public import Mathlib

/-!
# No order-`p` lift of a transvection modulo `p²` (`p ≥ 5`)

This is the group-theoretic input used in `research_return/UPPER_CONTROL.md`, §4, to prove
that `H²(Γ_p, E[p]) = 0`. It is a classical fact (Serre, *Abelian ℓ-adic representations*,
IV-23, Lemma 3) and is kernel-checked here for every prime `p ≥ 5`.

* `pow_eq_of_lift` : if `x ∈ M₂(ℤ/p²)` reduces to `u = !![1,1;0,1]` mod `p`, then
  `x ^ p = 1 + p • e₁₂`.
* `pow_ne_one_of_lift` : hence `x ^ p ≠ 1`.
* `no_section_SL2` : no monoid homomorphism `SL₂(𝔽_p) → M₂(ℤ/p²)` composes with reduction
  to the inclusion. In particular `SL₂(ℤ/p²) → SL₂(𝔽_p)` and `GL₂(ℤ/p²) → GL₂(𝔽_p)` do not
  split over `SL₂(𝔽_p)`.

The proof: write `x = 1 + N`, with `N = e₁₂ + p A`. Then `N⁴ = 0`, so
`x^p = 1 + pN + C(p,2) N² + C(p,3) N³`. Here `N²` and `N³` are multiples of `p`, and `p`
divides `C(p,2)` and `C(p,3)` when `p ≥ 5`. This is false at `p = 3`.
-/

@[expose] public section

open Matrix

namespace Seed.NoLift

variable {R : Type*} [CommRing R]

/-- Binomial expansion of `(1 + N)^n` when `N⁴ = 0`. -/
theorem one_add_pow_of_pow_four {N : Matrix (Fin 2) (Fin 2) R} (hN : N ^ 4 = 0) (n : ℕ) :
    (1 + N) ^ n = 1 + (n : Matrix (Fin 2) (Fin 2) R) * N +
      ((n.choose 2 : ℕ) : Matrix (Fin 2) (Fin 2) R) * N ^ 2 +
      ((n.choose 3 : ℕ) : Matrix (Fin 2) (Fin 2) R) * N ^ 3 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ih, Nat.choose_succ_succ' n 2, Nat.choose_succ_succ' n 1, Nat.choose_one_right]
    have h4 : N ^ 3 * N = 0 := by rw [← pow_succ]; exact hN
    push_cast
    have e2 : N * N = N ^ 2 := by rw [sq]
    have e3 : N ^ 2 * N = N ^ 3 := by rw [pow_succ N 2]
    simp only [add_mul, mul_add, mul_one, one_mul, mul_assoc, e2, e3, h4, mul_zero, add_zero]
    abel

/-- The elementary matrix `e₁₂`. -/
def e12 : Matrix (Fin 2) (Fin 2) R := !![0, 1; 0, 0]

theorem e12_mul_e12 : (e12 : Matrix (Fin 2) (Fin 2) R) * e12 = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [e12]

/-- Key algebraic identity: if `q² = 0` is a central scalar and `N = e₁₂ + q A`, then
`N⁴ = 0`, `N² = q (e₁₂ A + A e₁₂)` and `N³ = q e₁₂ A e₁₂`. -/
theorem pow_four_eq_zero (q : R) (hq : q * q = 0) (A : Matrix (Fin 2) (Fin 2) R) :
    (e12 + q • A) ^ 4 = 0 ∧ (e12 + q • A) ^ 2 = q • (e12 * A + A * e12) ∧
      (e12 + q • A) ^ 3 = q • (e12 * A * e12) := by
  have hE := (e12_mul_e12 : (e12 : Matrix (Fin 2) (Fin 2) R) * e12 = 0)
  have h2 : (e12 + q • A) ^ 2 = q • (e12 * A + A * e12) := by
    rw [sq]
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_smul, hq, zero_smul,
      add_zero, hE, zero_add, smul_add]
    abel
  have h3 : (e12 + q • A) ^ 3 = q • (e12 * A * e12) := by
    rw [pow_succ, h2]
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_smul, hq, zero_smul,
      add_zero, smul_add, mul_assoc, hE, mul_zero, smul_zero]
  refine ⟨?_, h2, h3⟩
  rw [pow_succ, h3]
  simp only [mul_add, smul_mul_assoc, mul_smul_comm, smul_smul, hq, zero_smul, add_zero,
    mul_assoc, hE, mul_zero, smul_zero]

variable {p : ℕ} [hp : Fact p.Prime]

/-- Reduction `ℤ/p² → 𝔽_p`. -/
abbrev red (p : ℕ) : ZMod (p ^ 2) →+* ZMod p :=
  ZMod.castHom (dvd_pow_self p two_ne_zero) (ZMod p)

theorem exists_mul_of_red_eq_zero (a : ZMod (p ^ 2)) (ha : red p a = 0) :
    ∃ b : ZMod (p ^ 2), a = (p : ZMod (p ^ 2)) * b := by
  have h1 : ((a.val : ℕ) : ZMod p) = 0 := by
    have := ha
    rw [← ZMod.natCast_zmod_val a] at this
    simpa using this
  rw [ZMod.natCast_eq_zero_iff] at h1
  obtain ⟨m, hm⟩ := h1
  refine ⟨(m : ZMod (p ^ 2)), ?_⟩
  rw [← ZMod.natCast_zmod_val a, hm]
  push_cast; ring

omit hp in
theorem natCast_p_sq_eq_zero : (p : ZMod (p ^ 2)) * (p : ZMod (p ^ 2)) = 0 := by
  rw [← Nat.cast_mul, ← sq, ZMod.natCast_self]

theorem natCast_p_ne_zero : (p : ZMod (p ^ 2)) ≠ 0 := by
  intro h
  rw [ZMod.natCast_eq_zero_iff] at h
  have h1 := Nat.le_of_dvd hp.out.pos h
  have h2 := hp.out.two_le
  nlinarith

/-- If `x ∈ M₂(ℤ/p²)` reduces to the transvection `!![1,1;0,1]`, and `p ≥ 5`, then
`x ^ p = 1 + p • e₁₂`. -/
theorem pow_eq_of_lift (h5 : 5 ≤ p) (x : Matrix (Fin 2) (Fin 2) (ZMod (p ^ 2)))
    (hx : x.map (red p) = !![1, 1; 0, 1]) :
    x ^ p = 1 + (p : ZMod (p ^ 2)) • e12 := by
  set q : ZMod (p ^ 2) := (p : ZMod (p ^ 2)) with hqdef
  have hq : q * q = 0 := natCast_p_sq_eq_zero
  -- write `x - 1 - e₁₂ = q • A`
  have hent : ∀ i j, ∃ b : ZMod (p ^ 2), (x - 1 - (e12 : Matrix (Fin 2) (Fin 2) (ZMod (p ^ 2)))) i j = q * b := by
    intro i j
    apply exists_mul_of_red_eq_zero
    have := congrFun (congrFun hx i) j
    fin_cases i <;> fin_cases j <;> simp_all [e12]
  choose A hA using hent
  have hxA : x = 1 + (e12 + q • Matrix.of A) := by
    ext i j
    have := hA i j
    simp only [Matrix.sub_apply] at this
    simp only [Matrix.add_apply, Matrix.smul_apply, Matrix.of_apply, smul_eq_mul]
    linear_combination this
  obtain ⟨h4, h2, h3⟩ := pow_four_eq_zero q hq (Matrix.of A)
  rw [hxA, one_add_pow_of_pow_four h4 p, h2, h3]
  have hc2 : p ∣ p.choose 2 := hp.out.dvd_choose_self (by norm_num) (by omega)
  have hc3 : p ∣ p.choose 3 := hp.out.dvd_choose_self (by norm_num) (by omega)
  obtain ⟨k2, hk2⟩ := hc2
  obtain ⟨k3, hk3⟩ := hc3
  have hcast : ∀ (n : ℕ) (M : Matrix (Fin 2) (Fin 2) (ZMod (p ^ 2))),
      ((n : ℕ) : Matrix (Fin 2) (Fin 2) (ZMod (p ^ 2))) * M = (n : ZMod (p ^ 2)) • M := by
    intro n M
    rw [← nsmul_eq_mul, Nat.cast_smul_eq_nsmul]
  rw [hcast, hcast, hcast, hk2, hk3]
  simp only [smul_add, smul_smul, Nat.cast_mul, ← hqdef]
  have hqq : ∀ m : ZMod (p ^ 2), q * m * q = 0 := by
    intro m; rw [mul_comm q m, mul_assoc, hq, mul_zero]
  simp only [hqq, hq, zero_smul, add_zero]

/-- No element of `M₂(ℤ/p²)` lifting the transvection has `x ^ p = 1`, for `p ≥ 5`. -/
theorem pow_ne_one_of_lift (h5 : 5 ≤ p) (x : Matrix (Fin 2) (Fin 2) (ZMod (p ^ 2)))
    (hx : x.map (red p) = !![1, 1; 0, 1]) : x ^ p ≠ 1 := by
  rw [pow_eq_of_lift h5 x hx]
  intro h
  have := congrFun (congrFun h 0) 1
  simp [e12] at this
  exact natCast_p_ne_zero this

/-- The transvection has order dividing `p` in `SL₂(𝔽_p)`. -/
theorem transvection_pow_p : (!![1, 1; 0, 1] : Matrix (Fin 2) (Fin 2) (ZMod p)) ^ p = 1 := by
  have key : ∀ n : ℕ, (!![1, 1; 0, 1] : Matrix (Fin 2) (Fin 2) (ZMod p)) ^ n =
      !![1, (n : ZMod p); 0, 1] := by
    intro n
    induction n with
    | zero => ext i j; fin_cases i <;> fin_cases j <;> simp
    | succ n ih =>
      rw [pow_succ, ih]
      ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]; ring
  rw [key, ZMod.natCast_self]
  ext i j; fin_cases i <;> fin_cases j <;> simp

/-- **No section over `SL₂(𝔽_p)` for `p ≥ 5`.** There is no monoid homomorphism
`s : SL₂(𝔽_p) → M₂(ℤ/p²)` whose reduction modulo `p` is the inclusion `SL₂(𝔽_p) ⊂ M₂(𝔽_p)`.
-/
theorem no_section_SL2 (h5 : 5 ≤ p) :
    ¬ ∃ s : Matrix.SpecialLinearGroup (Fin 2) (ZMod p) →* Matrix (Fin 2) (Fin 2) (ZMod (p ^ 2)),
      ∀ g, (s g).map (red p) = (g : Matrix (Fin 2) (Fin 2) (ZMod p)) := by
  rintro ⟨s, hs⟩
  let u : Matrix.SpecialLinearGroup (Fin 2) (ZMod p) :=
    ⟨!![1, 1; 0, 1], by simp [Matrix.det_fin_two]⟩
  have hu : u ^ p = 1 := by
    apply Subtype.ext
    simpa [u] using (transvection_pow_p (p := p))
  apply pow_ne_one_of_lift h5 (s u) (by simpa [u] using hs u)
  rw [← map_pow, hu, map_one]

end Seed.NoLift
