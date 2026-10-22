import WitnessContent.Spec
import WitnessContent.GroupRing
import WitnessContent.Depth
import WitnessContent.Primary
import WitnessContent.WC
import WitnessContent.Countermodels
import WitnessContent.Instances
import WitnessContent.Stretch

/-!
# A1 — targets

Each theorem keeps its exact name and its exact type `Spec.<Name>`. The proofs live in the
helper files imported above; `Defs.lean`, `Spec.lean` and `Acceptance.lean` are untouched.
-/

namespace WitnessContent

/-! ### Required for A1_CORE -/
theorem lemmaA_comm : Spec.LemmaA_comm :=
  fun _R _ _G _ e he r hr x hx => nsmul_augIdeal_pow e he r hr x hx

theorem gr_killed_by_exponent : Spec.Gr_killed_by_exponent :=
  fun _R _ _G _ e he r hr y => gr_nsmul_exponent_eq_zero e he r hr y

theorem depth_spec : Spec.Depth_spec :=
  fun _M _ _p _a _hp hkill _t ht => depth_spec_aux hkill ht

theorem zero_infinitely_divisible : Spec.Zero_infinitely_divisible :=
  fun _M _ p j => pdvd_zero p j

theorem hInf_lt_top_iff : Spec.HInf_lt_top_iff :=
  fun _W _M _ t p => hInf_lt_top_iff_aux t p

theorem hInf_le_iff : Spec.HInf_le_iff :=
  fun _W _M _ t p hp hexp d => hInf_le_iff_aux t p hp hexp d

theorem JE_bounds : Spec.JE_bounds :=
  fun _W _M _ t P A hA hAJ => JE_bounds_aux t P A hA hAJ

theorem WC_abstract : Spec.WC_abstract := WC_abstract_proof

theorem CM_uniform_denominator : Spec.CM_uniform_denominator := CM_uniform_denominator_proof

theorem CM_nonzero_everywhere : Spec.CM_nonzero_everywhere := CM_nonzero_everywhere_proof

theorem WC_abstract_nonvacuous : Spec.WC_abstract_nonvacuous := WC_abstract_nonvacuous_proof

/-! ### Additionally required for A1_FULL -/
theorem gr_p_primary : Spec.Gr_p_primary :=
  fun _R _ _G _ p e hp he0 he hu r hr y =>
    gr_pow_factorization_smul_eq_zero p e hp he0 he hu r hr y

theorem bridge_517 : Spec.Bridge_517 :=
  fun _R _ _G _ θ r p hr hp hθ => bridge_517_aux θ r p hr hp hθ

theorem cls2_zero_iff : Spec.Cls2_zero_iff :=
  fun _R _ _G _ θ hθ => cls2_eq_zero_iff θ hθ

theorem WC_groupRing : Spec.WC_groupRing := WC_groupRing_proof

theorem padicInt_units : Spec.PadicInt_units := padicInt_units_proof

theorem units_exponent : Spec.Units_exponent := units_exponent_proof

/-! ### Stretch (optional) -/
theorem lemmaA_general : Spec.LemmaA_general := lemmaA_general_proof

theorem gr_finite_Z : Spec.Gr_finite_Z := gr_finite_Z_proof

theorem gr_rational_trivial : Spec.Gr_rational_trivial := gr_rational_trivial_proof

end WitnessContent
