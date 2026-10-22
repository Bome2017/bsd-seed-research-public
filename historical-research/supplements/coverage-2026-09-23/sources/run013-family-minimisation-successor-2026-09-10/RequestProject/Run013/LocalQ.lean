/-
Run013 — `LocalQ.lean`

The exact local exclusions at the moving prime `q` in the dual (`hat phi_q`) orientation,
following `src/local_q/LOCAL_Q.md` and `evidence/DESCENT_DERIVATION.md` Lemma 4.4.

Under
  `(2/q) = -1`   (i.e. `2` is not a square mod `q`, which holds for `q ≡ 5 mod 8`) and
  `(-31/q) = -1` (i.e. `-31` is not a square mod `q`, which follows from `(q/31) = -1`
                  by reciprocity since `q ≡ 1 mod 4`),
the square classes `2`, `q`, `2q` all fail to be `ℚ_q`-soluble on
  `C^{(hat phi)}_{q,d} : n^2 = d u^4 - 15 q u^2 v^2 + (64 q^2 / d) v^4`.
-/
import RequestProject.Run013.PadicTools

namespace Run013

open PadicInt

lemma isSquare_of_sq_eq {F : Type*} [Field F] {c r s : F} (hs : s ≠ 0) (h : r ^ 2 = c * s ^ 2) :
    IsSquare c := ⟨r / s, by field_simp; linear_combination -h⟩

variable {q : ℕ} [Fact q.Prime]

lemma toZMod_eq_zero_iff (x : ℤ_[q]) : PadicInt.toZMod x = 0 ↔ (q : ℤ_[q]) ∣ x := by
  rw [← RingHom.mem_ker, PadicInt.ker_toZMod, PadicInt.maximalIdeal_eq_span_p,
    Ideal.mem_span_singleton]

/-- Integral normalisation for the dual covering over `ℚ_q`. -/
lemma dual_covM_int (D : ℤ) (hD : D ≠ 0)
    (h : Cov ℚ_[q] ((-15 * q : ℤ) : ℚ_[q]) ((64 * q ^ 2 : ℤ) : ℚ_[q]) ((D : ℤ) : ℚ_[q])) :
    ∃ U V M : ℤ_[q], (U = 1 ∨ V = 1) ∧
      M ^ 2 = ((D : ℤ) : ℤ_[q]) ^ 3 * U ^ 4
        + ((-15 * q : ℤ) : ℤ_[q]) * ((D : ℤ) : ℤ_[q]) ^ 2 * U ^ 2 * V ^ 2
        + ((64 * q ^ 2 : ℤ) : ℤ_[q]) * ((D : ℤ) : ℤ_[q]) * V ^ 4 := by
  have hD0 : ((D : ℤ) : ℚ_[q]) ≠ 0 := Int.cast_ne_zero.mpr hD
  rw [cov_iff_covM hD0] at h
  have h' : CovM ℚ_[q] ((((-15 * q : ℤ)) : ℤ_[q]) : ℚ_[q]) ((((64 * q ^ 2 : ℤ)) : ℤ_[q]) : ℚ_[q])
      ((((D : ℤ)) : ℤ_[q]) : ℚ_[q]) := by simpa using h
  exact covM_integral _ _ _ h'

lemma q_cast_ne_two (hq2 : q ≠ 2) : (2 : ZMod q) ≠ 0 := by
  have hp : q.Prime := Fact.out
  intro h
  have hdvd : q ∣ 2 := (ZMod.natCast_eq_zero_iff 2 q).mp (by exact_mod_cast h)
  exact hq2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp hdvd)

lemma q_cast_eight_ne_zero (hq2 : q ≠ 2) : (8 : ZMod q) ≠ 0 := by
  have hp : q.Prime := Fact.out
  intro h
  have hdvd : q ∣ 8 := (ZMod.natCast_eq_zero_iff 8 q).mp (by exact_mod_cast h)
  have := (Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp
    (hp.dvd_of_dvd_pow (n := 3) (by simpa using hdvd))
  exact hq2 this

/-- Exclusion of the class `d = 2` at `q`. -/
theorem localq_dual_two (hq2 : q ≠ 2) (hns : ¬ IsSquare (2 : ZMod q)) :
    ¬ Cov ℚ_[q] ((-15 * q : ℤ) : ℚ_[q]) ((64 * q ^ 2 : ℤ) : ℚ_[q]) ((2 : ℤ) : ℚ_[q]) := by
  intro h
  obtain ⟨U, V, M, hUV, hM⟩ := dual_covM_int (2 : ℤ) (by norm_num) h
  have hq0 : PadicInt.toZMod ((q : ℕ) : ℤ_[q]) = 0 := by
    simp
  by_cases hU : (q : ℤ_[q]) ∣ U
  · -- then `V = 1`
    obtain ⟨U₁, rfl⟩ := hU
    have hV1 : V = 1 := by
      rcases hUV with hh | hh
      · exact absurd (⟨⟨(q : ℤ_[q]), U₁, hh, by rw [mul_comm]; exact hh⟩, rfl⟩ :
          IsUnit ((q : ℤ_[q]))) (PadicInt.prime_p (p := q)).not_unit
      · exact hh
    subst hV1
    -- `M^2 = q^2 * W`
    have hW : M ^ 2 = (q : ℤ_[q]) ^ 2 *
        (8 * (q : ℤ_[q]) ^ 2 * U₁ ^ 4 - 60 * (q : ℤ_[q]) * U₁ ^ 2 + 128) := by
      rw [hM]; push_cast; ring
    have hqM : (q : ℤ_[q]) ∣ M := by
      refine (PadicInt.prime_p (p := q)).dvd_of_dvd_pow (n := 2) ?_
      exact ⟨(q : ℤ_[q]) * (8 * (q : ℤ_[q]) ^ 2 * U₁ ^ 4 - 60 * (q : ℤ_[q]) * U₁ ^ 2 + 128),
        by rw [hW]; ring⟩
    obtain ⟨M₁, rfl⟩ := hqM
    have hq0' : (q : ℤ_[q]) ≠ 0 := (PadicInt.prime_p (p := q)).ne_zero
    have hM₁ : M₁ ^ 2 = 8 * (q : ℤ_[q]) ^ 2 * U₁ ^ 4 - 60 * (q : ℤ_[q]) * U₁ ^ 2 + 128 := by
      have h2 : (q : ℤ_[q]) ^ 2 * M₁ ^ 2 = (q : ℤ_[q]) ^ 2 *
          (8 * (q : ℤ_[q]) ^ 2 * U₁ ^ 4 - 60 * (q : ℤ_[q]) * U₁ ^ 2 + 128) := by
        rw [← hW]; ring
      exact mul_left_cancel₀ (pow_ne_zero 2 hq0') h2
    have hf := congrArg (PadicInt.toZMod (p := q)) hM₁
    simp only [map_mul, map_pow, map_add, map_sub, map_ofNat, hq0] at hf
    refine hns (isSquare_of_sq_eq (c := (2 : ZMod q)) (r := PadicInt.toZMod M₁) (s := 8)
      (q_cast_eight_ne_zero hq2) ?_)
    rw [hf]; ring
  · -- `U` is a unit at `q`
    have hUne : PadicInt.toZMod U ≠ 0 := fun hz => hU ((toZMod_eq_zero_iff U).mp hz)
    have hM' : M ^ 2 = 8 * U ^ 4
        - 60 * (q : ℤ_[q]) * U ^ 2 * V ^ 2 + 128 * (q : ℤ_[q]) ^ 2 * V ^ 4 := by
      rw [hM]; push_cast; ring
    have hf := congrArg (PadicInt.toZMod (p := q)) hM'
    simp only [map_mul, map_pow, map_add, map_sub, map_ofNat, map_natCast,
      ZMod.natCast_self, zero_mul, mul_zero, sub_zero] at hf
    refine hns (isSquare_of_sq_eq (c := (2 : ZMod q)) (r := PadicInt.toZMod M)
      (s := 2 * (PadicInt.toZMod U) ^ 2) (by
        exact mul_ne_zero (q_cast_ne_two hq2) (pow_ne_zero 2 hUne)) ?_)
    rw [hf]; ring

/-- Exclusion of the class `d = q` at `q`. -/
theorem localq_dual_q (hns : ¬ IsSquare ((-31 : ℤ) : ZMod q)) :
    ¬ Cov ℚ_[q] ((-15 * q : ℤ) : ℚ_[q]) ((64 * q ^ 2 : ℤ) : ℚ_[q]) (((q : ℕ) : ℤ) : ℚ_[q]) := by
  intro h
  have hqne : ((q : ℕ) : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr (Nat.Prime.ne_zero (Fact.out))
  obtain ⟨U, V, M, hUV, hM⟩ := dual_covM_int ((q : ℕ) : ℤ) hqne h
  have hW : M ^ 2 = (q : ℤ_[q]) ^ (2 * 1 + 1) * (U ^ 4 - 15 * U ^ 2 * V ^ 2 + 64 * V ^ 4) := by
    rw [hM]; push_cast; ring
  refine not_sq_odd_val _ ?_ 1 M hW
  intro hdvd
  have hf : (PadicInt.toZMod U) ^ 4 - 15 * (PadicInt.toZMod U) ^ 2 * (PadicInt.toZMod V) ^ 2
      + 64 * (PadicInt.toZMod V) ^ 4 = 0 := by
    have := (toZMod_eq_zero_iff _).mpr hdvd
    simpa only [map_add, map_sub, map_mul, map_pow, map_ofNat] using this
  set a : ZMod q := PadicInt.toZMod U with hadef
  set b : ZMod q := PadicInt.toZMod V with hbdef
  by_cases hb : b = 0
  · -- then `U` is a unit and the form reduces to `a^4`
    have hU1 : U = 1 := by
      rcases hUV with hh | hh
      · exact hh
      · exfalso
        rw [hbdef, hh] at hb
        simp at hb
    have ha : a = 1 := by rw [hadef, hU1]; simp
    rw [hb, ha] at hf
    simp at hf
  · refine hns (isSquare_of_sq_eq (c := ((-31 : ℤ) : ZMod q)) (r := 2 * a ^ 2 - 15 * b ^ 2)
      (s := b ^ 2) (pow_ne_zero 2 hb) ?_)
    push_cast
    linear_combination (4 : ZMod q) * hf

/-- Exclusion of the class `d = 2q` at `q`. -/
theorem localq_dual_twoq (hq2 : q ≠ 2) (hns : ¬ IsSquare ((-31 : ℤ) : ZMod q)) :
    ¬ Cov ℚ_[q] ((-15 * q : ℤ) : ℚ_[q]) ((64 * q ^ 2 : ℤ) : ℚ_[q]) ((2 * (q : ℕ) : ℤ) : ℚ_[q]) := by
  intro h
  have hqne : (2 * (q : ℕ) : ℤ) ≠ 0 := by
    have := Nat.Prime.ne_zero (Fact.out (p := q.Prime))
    simpa using this
  obtain ⟨U, V, M, hUV, hM⟩ := dual_covM_int (2 * (q : ℕ) : ℤ) hqne h
  have hW : M ^ 2 = (q : ℤ_[q]) ^ (2 * 1 + 1) *
      (4 * (2 * U ^ 4 - 15 * U ^ 2 * V ^ 2 + 32 * V ^ 4)) := by
    rw [hM]; push_cast; ring
  refine not_sq_odd_val _ ?_ 1 M hW
  intro hdvd
  have hfz : (4 : ZMod q) * (2 * (PadicInt.toZMod U) ^ 4
      - 15 * (PadicInt.toZMod U) ^ 2 * (PadicInt.toZMod V) ^ 2
      + 32 * (PadicInt.toZMod V) ^ 4) = 0 := by
    have := (toZMod_eq_zero_iff _).mpr hdvd
    simpa only [map_add, map_sub, map_mul, map_pow, map_ofNat] using this
  have h4 : (4 : ZMod q) ≠ 0 := by
    intro hc
    exact q_cast_eight_ne_zero hq2 (by rw [show (8 : ZMod q) = 2 * 4 by ring, hc]; ring)
  have hf : 2 * (PadicInt.toZMod U) ^ 4
      - 15 * (PadicInt.toZMod U) ^ 2 * (PadicInt.toZMod V) ^ 2
      + 32 * (PadicInt.toZMod V) ^ 4 = 0 := by
    rcases mul_eq_zero.mp hfz with hc | hc
    · exact absurd hc h4
    · exact hc
  set a : ZMod q := PadicInt.toZMod U with hadef
  set b : ZMod q := PadicInt.toZMod V with hbdef
  by_cases hb : b = 0
  · have hU1 : U = 1 := by
      rcases hUV with hh | hh
      · exact hh
      · exfalso
        rw [hbdef, hh] at hb
        simp at hb
    have ha : a = 1 := by rw [hadef, hU1]; simp
    rw [hb, ha] at hf
    simp only [one_pow, mul_one] at hf
    norm_num at hf
    exact q_cast_ne_two hq2 (by linear_combination hf)
  · refine hns (isSquare_of_sq_eq (c := ((-31 : ℤ) : ZMod q)) (r := 4 * a ^ 2 - 15 * b ^ 2)
      (s := b ^ 2) (pow_ne_zero 2 hb) ?_)
    push_cast
    linear_combination (8 : ZMod q) * hf

end Run013
