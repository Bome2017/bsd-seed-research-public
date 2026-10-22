/-
Run013 — `Support.lean`

The support lemma of `src/selmer/SUPPORT_AND_GLOBAL.md` §1, proved from scratch:

If `p` is a prime not dividing `b`, and the square-class representative `D` has
`v_p(D) = 1`, then the covering `C_D : n^2 = D u^4 + a u^2 v^2 + (b/D) v^4` has no
`ℚ_p`-point.

Consequently an everywhere locally soluble class is supported on the primes dividing
`b`, together with the sign.
-/
import RequestProject.Run013.PadicTools

namespace Run013

open PadicInt

variable {p : ℕ} [Fact p.Prime]

lemma padicInt_not_dvd_of_int {m : ℤ} (h : ¬ (p : ℤ) ∣ m) : ¬ (p : ℤ_[p]) ∣ (m : ℤ_[p]) := by
  rw [← PadicInt.norm_lt_one_iff_dvd, PadicInt.norm_int_lt_one_iff_dvd]
  exact h

/-- **Support lemma.**  With `p ∤ b` and `v_p(D) = 1` the covering has no `ℚ_p`-point. -/
theorem support_lemma (a b D D₁ : ℤ) (hb : ¬ (p : ℤ) ∣ b)
    (hD : D = (p : ℤ) * D₁) (hD₁ : ¬ (p : ℤ) ∣ D₁) :
    ¬ Cov ℚ_[p] ((a : ℤ) : ℚ_[p]) ((b : ℤ) : ℚ_[p]) ((D : ℤ) : ℚ_[p]) := by
  intro hcov
  have hp0 : (p : ℤ_[p]) ≠ 0 := (PadicInt.prime_p (p := p)).ne_zero
  have hD₁' : ¬ (p : ℤ_[p]) ∣ ((D₁ : ℤ) : ℤ_[p]) := padicInt_not_dvd_of_int hD₁
  have hb' : ¬ (p : ℤ_[p]) ∣ ((b : ℤ) : ℤ_[p]) := padicInt_not_dvd_of_int hb
  have hDne : D ≠ 0 := by
    rintro rfl
    refine hD₁ ⟨0, ?_⟩
    have hp' : (p : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr (Nat.Prime.ne_zero (Fact.out (p := p.Prime)))
    have := hD.symm
    rw [mul_eq_zero] at this
    rcases this with h | h
    · exact absurd h hp'
    · simpa using h
  have hD0 : ((D : ℤ) : ℚ_[p]) ≠ 0 := Int.cast_ne_zero.mpr hDne
  rw [cov_iff_covM hD0] at hcov
  have hcov' : CovM ℚ_[p] (((a : ℤ) : ℤ_[p]) : ℚ_[p]) (((b : ℤ) : ℤ_[p]) : ℚ_[p])
      (((D : ℤ) : ℤ_[p]) : ℚ_[p]) := by
    simpa using hcov
  obtain ⟨U, V, M, hUV, hM⟩ := covM_integral ((a : ℤ) : ℤ_[p]) ((b : ℤ) : ℤ_[p])
    ((D : ℤ) : ℤ_[p]) hcov'
  set A : ℤ_[p] := ((a : ℤ) : ℤ_[p])
  set B : ℤ_[p] := ((b : ℤ) : ℤ_[p])
  set E : ℤ_[p] := ((D₁ : ℤ) : ℤ_[p])
  have hDsplit : ((D : ℤ) : ℤ_[p]) = (p : ℤ_[p]) * E := by
    rw [hD]; push_cast; ring
  rw [hDsplit] at hM
  by_cases hV : (p : ℤ_[p]) ∣ V
  · -- `p ∣ V`, hence `U = 1` and the right-hand side has valuation exactly 3
    obtain ⟨V₁, rfl⟩ := hV
    have hU1 : U = 1 := by
      rcases hUV with h | h
      · exact h
      · exact absurd (⟨⟨(p : ℤ_[p]), V₁, h, by rw [mul_comm]; exact h⟩, rfl⟩ : IsUnit ((p : ℤ_[p]))) (PadicInt.prime_p (p := p)).not_unit
    subst hU1
    have hw : M ^ 2 = (p : ℤ_[p]) ^ (2 * 1 + 1) *
        (E ^ 3 + A * (p : ℤ_[p]) * E ^ 2 * V₁ ^ 2 + B * (p : ℤ_[p]) ^ 2 * E * V₁ ^ 4) := by
      rw [hM]; ring
    refine not_sq_odd_val _ ?_ 1 M hw
    intro hdvd
    refine hD₁' ?_
    have h3 : (p : ℤ_[p]) ∣ E ^ 3 := by
      have : E ^ 3 = (E ^ 3 + A * (p : ℤ_[p]) * E ^ 2 * V₁ ^ 2 + B * (p : ℤ_[p]) ^ 2 * E * V₁ ^ 4)
          - (p : ℤ_[p]) * (A * E ^ 2 * V₁ ^ 2 + B * (p : ℤ_[p]) * E * V₁ ^ 4) := by ring
      rw [this]
      exact dvd_sub hdvd ⟨_, rfl⟩
    exact (PadicInt.prime_p (p := p)).dvd_of_dvd_pow h3
  · -- `V` is a unit and the right-hand side has valuation exactly 1
    have hw : M ^ 2 = (p : ℤ_[p]) ^ (2 * 0 + 1) *
        ((p : ℤ_[p]) ^ 2 * E ^ 3 * U ^ 4 + A * (p : ℤ_[p]) * E ^ 2 * U ^ 2 * V ^ 2
          + B * E * V ^ 4) := by
      rw [hM]; ring
    refine not_sq_odd_val _ ?_ 0 M hw
    intro hdvd
    have h3 : (p : ℤ_[p]) ∣ B * E * V ^ 4 := by
      have : B * E * V ^ 4 = ((p : ℤ_[p]) ^ 2 * E ^ 3 * U ^ 4
          + A * (p : ℤ_[p]) * E ^ 2 * U ^ 2 * V ^ 2 + B * E * V ^ 4)
          - (p : ℤ_[p]) * ((p : ℤ_[p]) * E ^ 3 * U ^ 4 + A * E ^ 2 * U ^ 2 * V ^ 2) := by ring
      rw [this]
      exact dvd_sub hdvd ⟨_, rfl⟩
    rcases (PadicInt.prime_p (p := p)).dvd_mul.mp h3 with h4 | h4
    · rcases (PadicInt.prime_p (p := p)).dvd_mul.mp h4 with h5 | h5
      · exact hb' h5
      · exact hD₁' h5
    · exact hV ((PadicInt.prime_p (p := p)).dvd_of_dvd_pow h4)

/-- **Support reduction.**  If a squarefree integer `D` is everywhere locally soluble for the
covering attached to `(a, b)`, then every prime dividing `D` divides `b`.

This is the structural statement that reduces the descent to finitely many square classes;
no finite list is postulated. -/
theorem support_reduction (a b D : ℤ) (hDsf : Squarefree D)
    (hloc : ∀ (r : ℕ) [Fact r.Prime],
      Cov ℚ_[r] ((a : ℤ) : ℚ_[r]) ((b : ℤ) : ℚ_[r]) ((D : ℤ) : ℚ_[r])) :
    ∀ r : ℕ, r.Prime → (r : ℤ) ∣ D → (r : ℤ) ∣ b := by
  intro r hr hrD
  haveI : Fact r.Prime := ⟨hr⟩
  by_contra hb
  obtain ⟨D₁, hD₁⟩ := hrD
  have hrD₁ : ¬ (r : ℤ) ∣ D₁ := by
    intro ⟨D₂, hD₂⟩
    have : (r : ℤ) * (r : ℤ) ∣ D := ⟨D₂, by rw [hD₁, hD₂]; ring⟩
    have hu := hDsf _ this
    rw [Int.isUnit_iff] at hu
    have := hr.two_le
    omega
  exact support_lemma a b D D₁ hb hD₁ hrD₁ (hloc r)

end Run013
