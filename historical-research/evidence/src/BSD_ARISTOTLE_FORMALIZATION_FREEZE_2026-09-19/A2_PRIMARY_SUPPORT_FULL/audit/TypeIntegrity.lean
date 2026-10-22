import PrimarySupport.Targets

/-! Independent target-integrity audit (custodian, 2026-09-19). Not part of the proof sources.
Checks that each target's DECLARED type is syntactically the frozen constant
`PrimarySupport.Spec.<Name>`, re-checks the boundary-sensitive targets through the kernel, and lists
every constant in the `PrimarySupport.Spec` namespace (must be exactly the frozen 28). -/

open Lean Elab Command in
elab "#assert_target_type " n:ident " : " s:ident : command => do
  let env ← getEnv
  let some ci := env.find? n.getId | throwError "MISSING target {n.getId}"
  if ci.type == mkConst s.getId then
    logInfo m!"OK  {n.getId} : {s.getId}  (declared type is exactly the frozen constant)"
  else throwError "MISMATCH {n.getId}: declared type {ci.type}"

open Lean Elab Command in
elab "#list_spec_constants" : command => do
  let env ← getEnv
  let names := env.constants.toList.filterMap fun (nm, _) =>
    if (`PrimarySupport.Spec).isPrefixOf nm && !nm.isInternal then some nm else none
  let sorted := names.toArray.qsort (fun a b => a.toString < b.toString)
  logInfo m!"PrimarySupport.Spec constants ({sorted.size}): {sorted.toList}"

#assert_target_type PrimarySupport.primary_zero_of_torsionfree : PrimarySupport.Spec.Primary_zero_of_torsionfree
#assert_target_type PrimarySupport.torsion_decomposition : PrimarySupport.Spec.Torsion_decomposition
#assert_target_type PrimarySupport.assembly : PrimarySupport.Spec.Assembly
#assert_target_type PrimarySupport.assembly_WC_shape : PrimarySupport.Spec.Assembly_WC_shape
#assert_target_type PrimarySupport.JOf_ideal : PrimarySupport.Spec.JOf_ideal
#assert_target_type PrimarySupport.JOf_ne_zero_iff : PrimarySupport.Spec.JOf_ne_zero_iff
#assert_target_type PrimarySupport.positive_depth_divides : PrimarySupport.Spec.Positive_depth_divides
#assert_target_type PrimarySupport.content_dvd_iff : PrimarySupport.Spec.Content_dvd_iff
#assert_target_type PrimarySupport.content_padic : PrimarySupport.Spec.Content_padic
#assert_target_type PrimarySupport.CM_each_local_finite : PrimarySupport.Spec.CM_each_local_finite
#assert_target_type PrimarySupport.CM_finite_support : PrimarySupport.Spec.CM_finite_support
#assert_target_type PrimarySupport.CM_nonzero_everywhere : PrimarySupport.Spec.CM_nonzero_everywhere
#assert_target_type PrimarySupport.CM_profinite_perfectness : PrimarySupport.Spec.CM_profinite_perfectness
#assert_target_type PrimarySupport.finite_iff_local_and_support : PrimarySupport.Spec.Finite_iff_local_and_support
#assert_target_type PrimarySupport.JOf_generator : PrimarySupport.Spec.JOf_generator
#assert_target_type PrimarySupport.content_basic : PrimarySupport.Spec.Content_basic
#assert_target_type PrimarySupport.content_unimodular : PrimarySupport.Spec.Content_unimodular
#assert_target_type PrimarySupport.exists_primitive : PrimarySupport.Spec.Exists_primitive
#assert_target_type PrimarySupport.content_mod_pk : PrimarySupport.Spec.Content_mod_pk
#assert_target_type PrimarySupport.content_bounds_J : PrimarySupport.Spec.Content_bounds_J
#assert_target_type PrimarySupport.lemmaB_valuation : PrimarySupport.Spec.LemmaB_valuation
#assert_target_type PrimarySupport.lemmaB_cokernel : PrimarySupport.Spec.LemmaB_cokernel
#assert_target_type PrimarySupport.card_eq_prod_primary : PrimarySupport.Spec.Card_eq_prod_primary
#assert_target_type PrimarySupport.order_nine_t_sq : PrimarySupport.Spec.Order_nine_t_sq
#assert_target_type PrimarySupport.CM_order_441 : PrimarySupport.Spec.CM_order_441
#assert_target_type PrimarySupport.alternating_square : PrimarySupport.Spec.Alternating_square
#assert_target_type PrimarySupport.CM_noncyclic_target : PrimarySupport.Spec.CM_noncyclic_target
#assert_target_type PrimarySupport.CM_codex_torsion_example : PrimarySupport.Spec.CM_codex_torsion_example

-- kernel re-checks through fully qualified names (boundary-sensitive targets)
example : PrimarySupport.Spec.Assembly_WC_shape := PrimarySupport.assembly_WC_shape
example : PrimarySupport.Spec.JOf_ne_zero_iff := PrimarySupport.JOf_ne_zero_iff
example : PrimarySupport.Spec.CM_each_local_finite := PrimarySupport.CM_each_local_finite
example : PrimarySupport.Spec.CM_finite_support := PrimarySupport.CM_finite_support
example : PrimarySupport.Spec.CM_nonzero_everywhere := PrimarySupport.CM_nonzero_everywhere
example : PrimarySupport.Spec.CM_profinite_perfectness := PrimarySupport.CM_profinite_perfectness
example : PrimarySupport.Spec.Finite_iff_local_and_support := PrimarySupport.finite_iff_local_and_support
example : PrimarySupport.Spec.Content_bounds_J := PrimarySupport.content_bounds_J
example : PrimarySupport.Spec.Order_nine_t_sq := PrimarySupport.order_nine_t_sq
example : PrimarySupport.Spec.CM_order_441 := PrimarySupport.CM_order_441
example : PrimarySupport.Spec.Alternating_square := PrimarySupport.alternating_square
example : PrimarySupport.Spec.CM_noncyclic_target := PrimarySupport.CM_noncyclic_target

#list_spec_constants
