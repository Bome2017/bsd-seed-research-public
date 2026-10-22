import WitnessContent.Depth

/-!
# A1 — regression countermodels and the non-vacuity check

* T9a `CM_uniform_denominator`: the witnesses `p² ∈ ZMod (p³)` are nonzero at every prime, yet the
  witness ideal is `{0}`: a uniform (indeed absent) denominator in the source does not bound the
  content of the image.
* T9b `CM_nonzero_everywhere`: hence "a nonzero witness at every prime ⇒ a nonzero element of
  `J_E`" is FALSE.
* T12 `WC_abstract_nonvacuous`: the hypotheses of T7 are jointly satisfiable.
-/

namespace WitnessContent

section Countermodel

/-- The countermodel witness at `p` is the class of `p²` in `ZMod (p³)`. -/
lemma cm_witness_eq (p : ℕ) :
    (zmultiplesHom (ZMod (p ^ 3)) ((p : ZMod (p ^ 3)) ^ 2)) 1 = ((p ^ 2 : ℕ) : ZMod (p ^ 3)) := by
  simp

lemma cm_kill (p : ℕ) (x : ZMod (p ^ 3)) : p ^ 3 • x = 0 := by
  rw [nsmul_eq_mul, ZMod.natCast_self, zero_mul]

lemma cm_ne_zero {p : ℕ} (hp : p.Prime) : ((p ^ 2 : ℕ) : ZMod (p ^ 3)) ≠ 0 := by
  rw [Ne, ZMod.natCast_eq_zero_iff]
  intro hdvd
  have hle := Nat.le_of_dvd (pow_pos hp.pos 2) hdvd
  have h2 := hp.two_le
  have : p ^ 2 < p ^ 3 := by
    exact Nat.pow_lt_pow_right (by omega) (by omega)
  omega

lemma cm_depth {p : ℕ} (hp : p.Prime) : depth p ((p ^ 2 : ℕ) : ZMod (p ^ 3)) = 2 := by
  obtain ⟨-, -, hlt⟩ := depth_spec_aux (cm_kill p) (cm_ne_zero hp)
  have hdvd : PDvd p 2 (((p ^ 2 : ℕ) : ZMod (p ^ 3))) := ⟨1, by simp [nsmul_eq_mul]⟩
  have hge := le_depth (cm_kill p) (cm_ne_zero hp) hdvd
  omega

lemma cm_hInf {p : ℕ} (hp : p.Prime) :
    hInf (W := fun _ => Unit) (M := fun p _ => ZMod (p ^ 3))
      (fun p _ => ((p ^ 2 : ℕ) : ZMod (p ^ 3))) p = ((2 : ℕ) : ℕ∞) := by
  rw [hInf, iInf_unique, iInf_pos (cm_ne_zero hp), cm_depth hp]

/-- Every nonzero integer is prime to some prime. -/
lemma exists_prime_not_dvd {a : ℤ} (ha : a ≠ 0) : ∃ p : ℕ, p.Prime ∧ ¬ (p : ℤ) ∣ a := by
  obtain ⟨p, hple, hp⟩ := Nat.exists_infinite_primes (a.natAbs + 1)
  refine ⟨p, hp, fun hdvd => ?_⟩
  have hdvd' : p ∣ a.natAbs := by
    have h : (p : ℤ) ∣ (a.natAbs : ℤ) := (Int.dvd_natAbs).2 hdvd
    exact_mod_cast h
  have hpos : 0 < a.natAbs := Int.natAbs_pos.2 ha
  have := Nat.le_of_dvd hpos hdvd'
  omega

/-- The witness ideal of the countermodel is `{0}`, although every witness is nonzero. -/
lemma cm_JE :
    JE (W := fun _ => Unit) (M := fun p _ => ZMod (p ^ 3))
      (fun p _ => ((p ^ 2 : ℕ) : ZMod (p ^ 3))) {p | p.Prime} = {0} := by
  ext a
  simp only [JE, Set.mem_setOf_eq, Set.mem_singleton_iff]
  constructor
  · intro h
    by_contra hane
    obtain ⟨p, hp, hnd⟩ := exists_prime_not_dvd hane
    have hle := h p hp
    rw [cm_hInf hp, vInf, if_neg hane, padicValInt.eq_zero_of_not_dvd hnd] at hle
    have : (2 : ℕ) ≤ (0 : ℕ) := by exact_mod_cast hle
    omega
  · rintro rfl
    intro p _
    simp [vInf]

/-- T9a. -/
theorem CM_uniform_denominator_proof : Spec.CM_uniform_denominator := by
  constructor
  · intro p hp
    rw [cm_witness_eq]
    exact cm_ne_zero hp
  · have hfun : (fun (p : ℕ) (_ : Unit) => (zmultiplesHom (ZMod (p ^ 3))
        ((p : ZMod (p ^ 3)) ^ 2)) 1) = fun (p : ℕ) (_ : Unit) => ((p ^ 2 : ℕ) : ZMod (p ^ 3)) := by
      funext p _
      exact cm_witness_eq p
    rw [hfun]
    exact cm_JE

/-- T9b: the false shortcut "nonzero witness everywhere ⇒ finite prime support" is refuted. -/
theorem CM_nonzero_everywhere_proof : Spec.CM_nonzero_everywhere := by
  intro h
  have hfin : ∀ p : ℕ, p.Prime → ∀ _S : Unit, Finite (ZMod (p ^ 3)) := by
    intro p hp _
    haveI : NeZero (p ^ 3) := ⟨pow_ne_zero _ hp.ne_zero⟩
    infer_instance
  have hexp : ∀ p : ℕ, p.Prime → ∀ _S : Unit, ∃ a : ℕ, ∀ x : ZMod (p ^ 3), p ^ a • x = 0 :=
    fun p _ _ => ⟨3, cm_kill p⟩
  have hnz : ∀ p : ℕ, p.Prime → ∃ _S : Unit, ((p ^ 2 : ℕ) : ZMod (p ^ 3)) ≠ 0 :=
    fun p hp => ⟨(), cm_ne_zero hp⟩
  obtain ⟨A, hA, hAJ⟩ := h (fun _ => Unit) (fun p _ => ZMod (p ^ 3))
    (fun p _ => ((p ^ 2 : ℕ) : ZMod (p ^ 3))) hfin hexp hnz
  rw [cm_JE] at hAJ
  exact hA hAJ

end Countermodel

section NonVacuous

/-- T12: the hypotheses of T7 are jointly satisfiable, with `1 ∈ J_E` and a nonzero witness at
every good prime. -/
theorem WC_abstract_nonvacuous_proof : Spec.WC_abstract_nonvacuous := by
  classical
  refine ⟨∅, PUnit, inferInstance, fun _ => Unit, fun p _ => ZMod p, fun _ _ => inferInstance,
    fun p _ => (1 : ZMod p), fun _ => 2, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro p _ _
    refine ⟨1, fun x => ?_⟩
    rw [pow_one, nsmul_eq_mul, ZMod.natCast_self, zero_mul]
  · intro x
    exact ⟨1, one_pos, Subsingleton.elim _ _⟩
  · intro p _ hinf
    exact absurd (Set.toFinite _) hinf
  · intro p _ _ h
    norm_num at h
  · intro p _ _ _ x _
    exact Subsingleton.elim _ _
  · intro p hp
    have hp' : p.Prime := hp.1
    haveI : Fact p.Prime := ⟨hp'⟩
    have hne : (1 : ZMod p) ≠ 0 := one_ne_zero
    have hkill : ∀ x : ZMod p, p ^ 1 • x = 0 := by
      intro x
      rw [pow_one, nsmul_eq_mul, ZMod.natCast_self, zero_mul]
    obtain ⟨-, -, hlt⟩ := depth_spec_aux hkill hne
    have hdepth : depth p (1 : ZMod p) = 0 := by omega
    have : hInf (W := fun _ => Unit) (M := fun p _ => ZMod p) (fun p _ => (1 : ZMod p)) p
        = ((0 : ℕ) : ℕ∞) := by
      rw [hInf, iInf_unique, iInf_pos hne, hdepth]
    rw [this, vInf, if_neg (by norm_num : (1 : ℤ) ≠ 0)]
    simp
  · intro p hp
    haveI : Fact p.Prime := ⟨hp.1⟩
    exact ⟨(), one_ne_zero⟩

end NonVacuous

end WitnessContent
