import WitnessContent.Spec

/-!
# A1 — depth, `h_p` and `J_E` helpers

Helper lemmas for the targets T5 (`depth_spec`), T5b (`zero_infinitely_divisible`),
T6 (`hInf_lt_top_iff`), T6b (`hInf_le_iff`) and T6c (`JE_bounds`).
-/

namespace WitnessContent

section PDvd

variable {M : Type*} [AddCommGroup M]

lemma pdvd_zero (p j : ℕ) : PDvd p j (0 : M) := ⟨0, by simp⟩

lemma pdvd_zero_elt (p j : ℕ) (t : M) (ht : t = 0) : PDvd p j t := ht ▸ pdvd_zero p j

/-- `{j | PDvd p j t}` is downward closed. -/
lemma pdvd_of_le {p j k : ℕ} {t : M} (hjk : j ≤ k) (h : PDvd p k t) : PDvd p j t := by
  obtain ⟨y, hy⟩ := h
  refine ⟨p ^ (k - j) • y, ?_⟩
  rw [smul_smul, ← pow_add]
  rwa [Nat.add_sub_cancel' hjk]

lemma pdvd_zero_index (p : ℕ) (t : M) : PDvd p 0 t := ⟨t, by simp⟩

/-- In a module killed by `p ^ a`, no nonzero element is divisible by `p ^ a`. -/
lemma not_pdvd_of_exponent {p a : ℕ} {t : M} (hkill : ∀ x : M, p ^ a • x = 0) (ht : t ≠ 0) :
    ¬ PDvd p a t := by
  rintro ⟨y, hy⟩
  exact ht (by rw [← hy, hkill y])

lemma depth_bddAbove {p a : ℕ} {t : M} (hkill : ∀ x : M, p ^ a • x = 0) (ht : t ≠ 0) :
    BddAbove {j : ℕ | PDvd p j t} := by
  refine ⟨a, fun j hj => ?_⟩
  by_contra hlt
  push_neg at hlt
  exact not_pdvd_of_exponent hkill ht (pdvd_of_le (le_of_lt hlt) hj)

/-- T5: on a nonzero element of a module of bounded `p`-power exponent, the depth is attained,
maximal, and bounded by the exponent. -/
lemma depth_spec_aux {p a : ℕ} (hkill : ∀ x : M, p ^ a • x = 0) {t : M} (ht : t ≠ 0) :
    PDvd p (depth p t) t ∧ ¬ PDvd p (depth p t + 1) t ∧ depth p t < a := by
  have hne : {j : ℕ | PDvd p j t}.Nonempty := ⟨0, pdvd_zero_index p t⟩
  have hbdd := depth_bddAbove hkill ht
  have hmem : depth p t ∈ {j : ℕ | PDvd p j t} := Nat.sSup_mem hne hbdd
  refine ⟨hmem, ?_, ?_⟩
  · intro hsucc
    have : depth p t + 1 ≤ depth p t := le_csSup hbdd hsucc
    omega
  · by_contra hge
    push_neg at hge
    exact not_pdvd_of_exponent hkill ht (pdvd_of_le hge hmem)

/-- The depth bounds divisibility: if `t` is `p ^ j`-divisible then `j ≤ depth p t`. -/
lemma le_depth {p a j : ℕ} (hkill : ∀ x : M, p ^ a • x = 0) {t : M} (ht : t ≠ 0)
    (h : PDvd p j t) : j ≤ depth p t :=
  le_csSup (depth_bddAbove hkill ht) h

end PDvd

section HInf

variable {W : ℕ → Type*} {Mod : (p : ℕ) → W p → Type*} [∀ p S, AddCommGroup (Mod p S)]

lemma hInf_le_of_ne_zero (t : ∀ p S, Mod p S) (p : ℕ) (S : W p) (hS : t p S ≠ 0) :
    hInf t p ≤ (depth p (t p S) : ℕ∞) := by
  refine le_trans (iInf_le _ S) ?_
  exact le_of_eq (by rw [iInf_pos hS])

/-- T6. -/
lemma hInf_lt_top_iff_aux (t : ∀ p S, Mod p S) (p : ℕ) :
    hInf t p < ⊤ ↔ ∃ S, t p S ≠ 0 := by
  constructor
  · intro h
    by_contra hall
    push_neg at hall
    have : hInf t p = ⊤ := by
      refine le_antisymm le_top ?_
      refine le_iInf fun S => ?_
      refine le_iInf fun hS => ?_
      exact absurd (hall S) hS
    rw [this] at h
    exact lt_irrefl _ h
  · rintro ⟨S, hS⟩
    exact lt_of_le_of_lt (hInf_le_of_ne_zero t p S hS) (by exact ENat.coe_lt_top _)

/-- In `ℕ∞`, an infimum is `≤ d` exactly when some term is. -/
lemma iInf_le_nat_iff {ι : Type*} (f : ι → ℕ∞) (d : ℕ) :
    (⨅ i, f i) ≤ (d : ℕ∞) ↔ ∃ i, f i ≤ (d : ℕ∞) := by
  constructor
  · intro h
    by_contra hall
    push_neg at hall
    have : ((d : ℕ∞) + 1) ≤ ⨅ i, f i :=
      le_iInf fun i => Order.add_one_le_of_lt (hall i)
    have h2 : ((d : ℕ∞) + 1) ≤ (d : ℕ∞) := le_trans this h
    have h3 : ((d + 1 : ℕ) : ℕ∞) ≤ ((d : ℕ) : ℕ∞) := by push_cast; exact h2
    have h4 : d + 1 ≤ d := by exact_mod_cast h3
    omega
  · rintro ⟨i, hi⟩
    exact le_trans (iInf_le f i) hi

/-- T6b. -/
lemma hInf_le_iff_aux (t : ∀ p S, Mod p S) (p : ℕ) (_hp : p.Prime)
    (hexp : ∀ S, ∃ a : ℕ, ∀ x : Mod p S, p ^ a • x = 0) (d : ℕ) :
    hInf t p ≤ (d : ℕ∞) ↔ ∃ S, ¬ PDvd p (d + 1) (t p S) := by
  constructor
  · intro h
    rw [hInf, iInf_le_nat_iff] at h
    obtain ⟨S, hS⟩ := h
    by_cases hz : t p S = 0
    · rw [iInf_neg (by simpa using hz)] at hS
      exact absurd hS (by simp)
    · rw [iInf_pos hz] at hS
      have hdle : depth p (t p S) ≤ d := by exact_mod_cast hS
      obtain ⟨a, ha⟩ := hexp S
      obtain ⟨-, hnot, -⟩ := depth_spec_aux ha hz
      refine ⟨S, fun hdvd => hnot ?_⟩
      exact pdvd_of_le (by omega) hdvd
  · rintro ⟨S, hS⟩
    have hz : t p S ≠ 0 := fun h => hS (pdvd_zero_elt p (d + 1) _ h)
    obtain ⟨a, ha⟩ := hexp S
    obtain ⟨hmem, -, -⟩ := depth_spec_aux ha hz
    have hdle : depth p (t p S) ≤ d := by
      by_contra hgt
      push_neg at hgt
      exact hS (pdvd_of_le hgt hmem)
    refine le_trans (hInf_le_of_ne_zero t p S hz) ?_
    exact_mod_cast hdle

/-- T6c. -/
lemma JE_bounds_aux (t : ∀ p S, Mod p S) (P : Set ℕ) (A : ℤ) (hA : A ≠ 0) (hAJ : A ∈ JE t P) :
    (∀ p ∈ P, hInf t p ≤ (padicValInt p A : ℕ)) ∧
      (∀ p ∈ P, p.Prime → ¬ (p : ℤ) ∣ A → hInf t p = 0) := by
  constructor
  · intro p hp
    have := hAJ p hp
    rwa [vInf, if_neg hA] at this
  · intro p hp _hpp hdvd
    have h1 := hAJ p hp
    rw [vInf, if_neg hA, padicValInt.eq_zero_of_not_dvd hdvd] at h1
    simpa using h1

end HInf

end WitnessContent
