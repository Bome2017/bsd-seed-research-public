import PrimarySupport.Spec
import PrimarySupport.Content
import PrimarySupport.Depth
import PrimarySupport.Descent
import PrimarySupport.LemmaB
import PrimarySupport.Primary
import PrimarySupport.Countermodels
import PrimarySupport.Order
import PrimarySupport.Pairing
import PrimarySupport.CodexExample
import PrimarySupport.Symplectic

/-!
# A2 — targets (Aristotle: replace every `sorry`)

Each theorem must keep its exact name and its exact type `Spec.<Name>`. Add helper lemmas freely
(preferably in new files under `PrimarySupport/`), but do not edit `Defs.lean` or `Spec.lean`.
Final acceptance: no `sorry`/`admit`/new `axiom`; `#print axioms` of every accepted target shows only
`propext`, `Classical.choice`, `Quot.sound` (see `Acceptance.lean`).
-/

namespace PrimarySupport

/-! ### Required for A2_CORE -/
theorem primary_zero_of_torsionfree : Spec.Primary_zero_of_torsionfree :=
  fun _ _ p _ hfree => primaryPart_eq_bot_of_torsionfree p hfree

theorem torsion_decomposition : Spec.Torsion_decomposition :=
  fun _ _ htor x => torsion_decomposition_aux htor x

theorem assembly : Spec.Assembly := fun _ _ T htor hbot hfin => finite_of_primary T htor hbot hfin

theorem assembly_WC_shape : Spec.Assembly_WC_shape := fun _ _ S0 A htor hA hbot hfin hS0 =>
  finite_of_primary_WC_shape S0 A htor hA hbot hfin hS0

theorem JOf_ideal : Spec.JOf_ideal := fun P h hP =>
  ⟨zero_mem_JOf P h, fun _ _ ha hb => add_mem_JOf hP ha hb, fun c _ ha => mul_mem_JOf hP c ha⟩

theorem JOf_ne_zero_iff : Spec.JOf_ne_zero_iff := fun _ _ hP => exists_ne_zero_mem_JOf_iff hP

theorem positive_depth_divides : Spec.Positive_depth_divides := by
  intro P h A hP hA0 hA
  obtain ⟨htop, hfin⟩ := (exists_ne_zero_mem_JOf_iff hP).1 ⟨A, hA, hA0⟩
  exact ⟨fun p hp => dvd_of_mem_posSupport hP hA hA0 hp, hfin, htop⟩

theorem content_dvd_iff : Spec.Content_dvd_iff := fun _ z m => content_dvd_iff_mem_smul z m

theorem content_padic : Spec.Content_padic := fun _ z p j hp hz => content_padic_dvd_iff z p j hp hz

theorem CM_each_local_finite : Spec.CM_each_local_finite :=
  ⟨dsum_isTorsion, fun _ hp => dsum_primary_finite hp, dsum_support_infinite, dsum_not_finite⟩

theorem CM_finite_support : Spec.CM_finite_support :=
  ⟨finsupp_zmod2_isTorsion, finsupp_zmod2_support_finite, finsupp_zmod2_not_finite⟩

theorem CM_nonzero_everywhere : Spec.CM_nonzero_everywhere :=
  ⟨fun _ hp => zmod_p_sq_ne_zero hp, JOf_const_two⟩

theorem CM_profinite_perfectness : Spec.CM_profinite_perfectness := by
  refine ⟨?_, ?_, ?_⟩
  · intro p
    haveI : NeZero ((p : ℕ) ^ (if (p : ℕ) = 2 ∨ (p : ℕ) = 5 then 0 else 2)) :=
      ⟨pow_ne_zero _ p.2.pos.ne'⟩
    infer_instance
  · exact not_finite_pi_of_infinite_support (v := cm3v) cm3_support_infinite
  · intro A hA
    by_contra hA0
    exact (Set.not_infinite.mpr ((exists_int_dvd_iff_finite_support cm3v).1 ⟨A, hA0, hA⟩))
      cm3_support_infinite

/-! ### Additionally required for A2_FULL -/
theorem finite_iff_local_and_support : Spec.Finite_iff_local_and_support :=
  fun _ _ htor => finite_iff_local_and_support_aux htor

theorem JOf_generator : Spec.JOf_generator := fun _ _ hP htop hfin => JOf_eq_multiples hP htop hfin

theorem content_basic : Spec.Content_basic := fun _ z => ⟨content_nonneg z, content_eq_zero_iff z⟩

theorem content_unimodular : Spec.Content_unimodular := fun _ U hU z =>
  content_mulVec_of_isUnit_det U hU z

theorem exists_primitive : Spec.Exists_primitive := fun _ z hz => exists_primitive_factor z hz

theorem content_mod_pk : Spec.Content_mod_pk := fun _ z p j k hp => content_mod_pk_iff z p j k hp

theorem content_bounds_J : Spec.Content_bounds_J := fun _ _ B _ z hP hz hout hin =>
  exists_ne_zero_mem_JOf_of_content_bound B z hP hz hout hin

theorem lemmaB_valuation : Spec.LemmaB_valuation := exists_int_dvd_iff_finite_support

theorem lemmaB_cokernel : Spec.LemmaB_cokernel := finite_pi_iff_finite_support

theorem card_eq_prod_primary : Spec.Card_eq_prod_primary := fun _ _ _ => card_eq_prod_primary_aux

theorem order_nine_t_sq : Spec.Order_nine_t_sq := fun _ _ _ h2 h3 h5 hsq =>
  order_nine_t_sq_aux h2 h3 h5 hsq

theorem CM_order_441 : Spec.CM_order_441 := by
  refine ⟨primaryPart_G441_other Nat.prime_two (by norm_num) (by norm_num),
    primaryPart_G441_three, primaryPart_G441_other (by norm_num) (by norm_num) (by norm_num),
    ?_, by simp⟩
  intro p hp _
  by_cases h3 : p = 3
  · subst h3; rw [primaryPart_G441_three]; exact ⟨3, by norm_num⟩
  by_cases h7 : p = 7
  · subst h7; rw [primaryPart_G441_seven]; exact ⟨7, by norm_num⟩
  · rw [primaryPart_G441_other hp h3 h7]; exact ⟨1, by norm_num⟩

/-! ### Stretch (optional) -/
theorem alternating_square : Spec.Alternating_square := fun G _ _ N β halt hnd =>
  Symp.isSquare_card G N β halt hnd
theorem CM_noncyclic_target : Spec.CM_noncyclic_target :=
  ⟨crossHom, crossZ2_self, crossZ2_nondegenerate, by simpa using not_isSquare_eight⟩
theorem CM_codex_torsion_example : Spec.CM_codex_torsion_example :=
  ⟨cg_isTorsion, cg_primary_eq_bot Nat.prime_two (Or.inl rfl),
    cg_primary_eq_bot (by norm_num) (Or.inr rfl), cg_card_primary_three,
    fun p hp => ⟨cg_primary_finite hp, cg_primary_isSquare hp⟩,
    cg_support_infinite, cg_not_finite⟩

end PrimarySupport
