import WitnessContent.Targets

/-!
Independent target-integrity audit (custodian, 2026-09-19). Not part of the proof sources.
For every target `WitnessContent.X` it checks that the DECLARED type is syntactically the frozen
constant `WitnessContent.Spec.<Name>` (no wrapper, no defeq detour), re-checks it with an `example`,
and lists every constant in the `WitnessContent.Spec` namespace (must be exactly the frozen 20).
-/

open Lean Elab Command in
elab "#assert_target_type " n:ident " : " s:ident : command => do
  let env ← getEnv
  let some ci := env.find? n.getId | throwError "MISSING target {n.getId}"
  let expected := mkConst s.getId
  if ci.type == expected then
    logInfo m!"OK  {n.getId} : {s.getId}  (declared type is exactly the frozen constant)"
  else
    throwError "MISMATCH {n.getId}: declared type {ci.type}"

open Lean Elab Command in
elab "#list_spec_constants" : command => do
  let env ← getEnv
  let names := env.constants.toList.filterMap fun (nm, _) =>
    if (`WitnessContent.Spec).isPrefixOf nm && !nm.isInternal then some nm else none
  let sorted := names.toArray.qsort (fun a b => a.toString < b.toString)
  logInfo m!"WitnessContent.Spec constants ({sorted.size}): {sorted.toList}"

#assert_target_type WitnessContent.lemmaA_comm : WitnessContent.Spec.LemmaA_comm
#assert_target_type WitnessContent.gr_killed_by_exponent : WitnessContent.Spec.Gr_killed_by_exponent
#assert_target_type WitnessContent.depth_spec : WitnessContent.Spec.Depth_spec
#assert_target_type WitnessContent.zero_infinitely_divisible : WitnessContent.Spec.Zero_infinitely_divisible
#assert_target_type WitnessContent.hInf_lt_top_iff : WitnessContent.Spec.HInf_lt_top_iff
#assert_target_type WitnessContent.hInf_le_iff : WitnessContent.Spec.HInf_le_iff
#assert_target_type WitnessContent.JE_bounds : WitnessContent.Spec.JE_bounds
#assert_target_type WitnessContent.WC_abstract : WitnessContent.Spec.WC_abstract
#assert_target_type WitnessContent.CM_uniform_denominator : WitnessContent.Spec.CM_uniform_denominator
#assert_target_type WitnessContent.CM_nonzero_everywhere : WitnessContent.Spec.CM_nonzero_everywhere
#assert_target_type WitnessContent.WC_abstract_nonvacuous : WitnessContent.Spec.WC_abstract_nonvacuous
#assert_target_type WitnessContent.gr_p_primary : WitnessContent.Spec.Gr_p_primary
#assert_target_type WitnessContent.bridge_517 : WitnessContent.Spec.Bridge_517
#assert_target_type WitnessContent.cls2_zero_iff : WitnessContent.Spec.Cls2_zero_iff
#assert_target_type WitnessContent.WC_groupRing : WitnessContent.Spec.WC_groupRing
#assert_target_type WitnessContent.padicInt_units : WitnessContent.Spec.PadicInt_units
#assert_target_type WitnessContent.units_exponent : WitnessContent.Spec.Units_exponent
#assert_target_type WitnessContent.lemmaA_general : WitnessContent.Spec.LemmaA_general
#assert_target_type WitnessContent.gr_finite_Z : WitnessContent.Spec.Gr_finite_Z
#assert_target_type WitnessContent.gr_rational_trivial : WitnessContent.Spec.Gr_rational_trivial

-- kernel re-check through fully qualified names
example : WitnessContent.Spec.WC_abstract := WitnessContent.WC_abstract
example : WitnessContent.Spec.WC_groupRing := WitnessContent.WC_groupRing
example : WitnessContent.Spec.CM_uniform_denominator := WitnessContent.CM_uniform_denominator
example : WitnessContent.Spec.CM_nonzero_everywhere := WitnessContent.CM_nonzero_everywhere
example : WitnessContent.Spec.WC_abstract_nonvacuous := WitnessContent.WC_abstract_nonvacuous

#list_spec_constants
