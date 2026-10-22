import PrimarySupport.Defs

/-!
# A2 — helper lemmas: content of vectors in the finite free lattice `ℤ^n`

Supporting material for the packaged targets L1–L6 (and, via `Descent.lean`, L7).  Everything here
is elementary commutative algebra over `ℤ`; nothing mentions elliptic curves.
-/

namespace PrimarySupport

/-- The content divides every coordinate. -/
lemma content_dvd_coord {n : ℕ} (z : Fin n → ℤ) (i : Fin n) : content z ∣ z i :=
  Finset.gcd_dvd (Finset.mem_univ i)

/-- Dividing the content is the same as dividing every coordinate. -/
lemma dvd_content_iff {n : ℕ} (z : Fin n → ℤ) (m : ℤ) : m ∣ content z ↔ ∀ i, m ∣ z i := by
  rw [content, Finset.dvd_gcd_iff]
  exact ⟨fun h i => h i (Finset.mem_univ i), fun h i _ => h i⟩

/-- L2 (first half). The content is nonnegative. -/
lemma content_nonneg {n : ℕ} (z : Fin n → ℤ) : 0 ≤ content z := by
  have h : |content z| = content z := by rw [Int.abs_eq_normalize]; exact Finset.normalize_gcd
  exact h ▸ abs_nonneg _

/-- L2 (second half). The content vanishes exactly at the zero vector. -/
lemma content_eq_zero_iff {n : ℕ} (z : Fin n → ℤ) : content z = 0 ↔ z = 0 := by
  rw [content, Finset.gcd_eq_zero_iff]
  exact ⟨fun h => funext fun i => h i (Finset.mem_univ i), fun h i _ => by simp [h]⟩

lemma content_ne_zero {n : ℕ} {z : Fin n → ℤ} (hz : z ≠ 0) : content z ≠ 0 :=
  fun h => hz ((content_eq_zero_iff z).1 h)

/-- L1. `z ∈ m·ℤ^n` iff `m` divides the content. -/
lemma content_dvd_iff_mem_smul {n : ℕ} (z : Fin n → ℤ) (m : ℤ) :
    (∃ y : Fin n → ℤ, z = m • y) ↔ m ∣ content z := by
  constructor
  · rintro ⟨y, rfl⟩
    exact (dvd_content_iff _ _).2 fun i => ⟨y i, rfl⟩
  · intro hm
    refine ⟨fun i => z i / m, funext fun i => ?_⟩
    have hi : m ∣ z i := (dvd_content_iff z m).1 hm i
    simp [Int.mul_ediv_cancel' hi]

/-- Content of a nonnegative scalar multiple. -/
lemma content_smul {n : ℕ} (c : ℤ) (hc : 0 ≤ c) (z : Fin n → ℤ) :
    content (c • z) = c * content z := by
  have h : content (c • z) = normalize c * content z := Finset.gcd_mul_left
  rwa [Int.normalize_of_nonneg hc] at h

/-- The content can only grow under an integral linear map. -/
lemma content_dvd_mulVec {n : ℕ} (M : Matrix (Fin n) (Fin n) ℤ) (z : Fin n → ℤ) :
    content z ∣ content (M.mulVec z) := by
  refine (dvd_content_iff _ _).2 fun i => ?_
  rw [Matrix.mulVec, dotProduct]
  exact Finset.dvd_sum fun j _ => Dvd.dvd.mul_left (content_dvd_coord z j) _

/-- L3. The content is invariant under a unimodular change of basis. -/
lemma content_mulVec_of_isUnit_det {n : ℕ} (U : Matrix (Fin n) (Fin n) ℤ) (hU : IsUnit U.det)
    (z : Fin n → ℤ) : content (U.mulVec z) = content z := by
  refine Int.dvd_antisymm (content_nonneg _) (content_nonneg _) ?_ (content_dvd_mulVec U z)
  have h : U⁻¹.mulVec (U.mulVec z) = z := by
    rw [Matrix.mulVec_mulVec, Matrix.nonsing_inv_mul U hU, Matrix.one_mulVec]
  calc content (U.mulVec z) ∣ content (U⁻¹.mulVec (U.mulVec z)) := content_dvd_mulVec _ _
    _ = content z := by rw [h]

/-- L4. A nonzero vector is its content times a primitive vector. -/
lemma exists_primitive_factor {n : ℕ} (z : Fin n → ℤ) (hz : z ≠ 0) :
    ∃ z₀ : Fin n → ℤ, content z₀ = 1 ∧ z = content z • z₀ := by
  have hc : content z ≠ 0 := content_ne_zero hz
  obtain ⟨y, hy⟩ := (content_dvd_iff_mem_smul z (content z)).2 dvd_rfl
  refine ⟨y, ?_, hy⟩
  have h1 : content z = content z * content y := by
    conv_lhs => rw [hy]
    exact content_smul (content z) (content_nonneg z) y
  have h2 : content z * 1 = content z * content y := by rw [mul_one]; exact h1
  exact (mul_left_cancel₀ hc h2).symm

/-- L5. `p`-adic form of L1 for a nonzero vector. -/
lemma content_padic_dvd_iff {n : ℕ} (z : Fin n → ℤ) (p j : ℕ) (hp : p.Prime) (hz : z ≠ 0) :
    ((∃ y : Fin n → ℤ, z = ((p : ℤ) ^ j) • y) ↔ j ≤ padicValInt p (content z)) := by
  haveI : Fact p.Prime := ⟨hp⟩
  rw [content_dvd_iff_mem_smul, padicValInt_dvd_iff]
  simp [content_ne_zero hz]

/-- Coordinatewise `ZMod (p^k)` form: the class of `a` is divisible by `p^j` in `ZMod (p^k)` iff
`p^(min j k)` divides `a` in `ℤ`.  The truncation case `j > k` is included. -/
lemma zmod_pow_smul_iff (p k j : ℕ) (hp : p.Prime) (a : ℤ) :
    (∃ w : ZMod (p ^ k), ((a : ZMod (p ^ k))) = (p ^ j : ℕ) • w) ↔ (p : ℤ) ^ (min j k) ∣ a := by
  have hp0 : p ≠ 0 := hp.pos.ne'
  haveI : NeZero (p ^ k) := ⟨pow_ne_zero _ hp0⟩
  constructor
  · rintro ⟨w, hw⟩
    obtain ⟨b, rfl⟩ := ZMod.intCast_surjective (n := p ^ k) w
    have h0 : (((a - (p : ℤ) ^ j * b : ℤ)) : ZMod (p ^ k)) = 0 := by
      push_cast
      rw [hw]
      ring
    rw [ZMod.intCast_zmod_eq_zero_iff_dvd] at h0
    have h1 : ((p : ℤ)) ^ (min j k) ∣ ((p ^ k : ℕ) : ℤ) := by
      push_cast
      exact pow_dvd_pow _ (min_le_right _ _)
    have h2 : ((p : ℤ)) ^ (min j k) ∣ (p : ℤ) ^ j * b :=
      Dvd.dvd.mul_right (pow_dvd_pow _ (min_le_left _ _)) _
    have h3 := dvd_add (h1.trans h0) h2
    simpa using h3
  · rintro ⟨c, rfl⟩
    rcases le_or_gt j k with hjk | hjk
    · refine ⟨(c : ZMod (p ^ k)), ?_⟩
      rw [min_eq_left hjk]
      push_cast
      rw [nsmul_eq_mul]
      push_cast
      ring
    · refine ⟨0, ?_⟩
      rw [min_eq_right hjk.le, smul_zero]
      push_cast
      rw [show ((p : ZMod (p ^ k))) ^ k = ((p ^ k : ℕ) : ZMod (p ^ k)) by push_cast; ring,
        ZMod.natCast_self, zero_mul]

/-- L6. Finite version over `ZMod (p^k)`. -/
lemma content_mod_pk_iff {n : ℕ} (z : Fin n → ℤ) (p j k : ℕ) (hp : p.Prime) :
    ((∃ y : Fin n → ZMod (p ^ k), reduceMod (p ^ k) z = (p ^ j) • y) ↔
      ((p : ℤ) ^ (min j k)) ∣ content z) := by
  rw [dvd_content_iff]
  constructor
  · rintro ⟨y, hy⟩ i
    refine (zmod_pow_smul_iff p k j hp (z i)).1 ⟨y i, ?_⟩
    have := congrFun hy i
    simpa [reduceMod] using this
  · intro h
    choose w hw using fun i => (zmod_pow_smul_iff p k j hp (z i)).2 (h i)
    exact ⟨w, funext fun i => by simpa [reduceMod] using hw i⟩

end PrimarySupport
