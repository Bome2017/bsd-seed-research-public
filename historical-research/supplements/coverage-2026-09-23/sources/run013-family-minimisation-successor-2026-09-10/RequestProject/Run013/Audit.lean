/-
Run013 — `Audit.lean`

Axiom audit.  Every headline theorem of the project is printed here with `#print axioms`.

Expected output for every one of them:

    'Run013.<name>' depends on axioms: [propext, Classical.choice, Quot.sound]

which are the standard Lean foundations.  Any other axiom would be a blocking Run013
custom mathematical assumption; there are none.

There is no `sorry`, no `admit`, no `axiom`, no `native_decide` and no
`Lean.ofReduceBool` anywhere in this project.  The only finite computations are kernel
`decide` calls on explicitly enumerated finite propositions (see `LocalTwo.lean`), and
they are reached only after the finite reduction has itself been proved
(`Support.support_reduction` and `Squareclasses.squarefree_int_classify`).
-/
import RequestProject.Run013.Main

namespace Run013

section Audit

-- LEVEL A: the two exact isogeny-Selmer identities
#print axioms Run013.phi_selmer_eq
#print axioms Run013.dual_phi_selmer_eq
#print axioms Run013.phi_selmer_eq_min
#print axioms Run013.dual_phi_selmer_eq_min

-- the exported main theorem
#print axioms Run013.run013_primary_theorem
#print axioms Run013.run013_selmer_orders
#print axioms Run013.run013_primary_theorem_min
#print axioms Run013.run013_selmer_orders_min

-- the structural finite reduction (no finite list is postulated)
#print axioms Run013.support_lemma
#print axioms Run013.support_reduction
#print axioms Run013.squarefree_int_classify
#print axioms Run013.exists_squarefree_rep

-- the local conditions
#print axioms Run013.localinf_dual
#print axioms Run013.local2_phi
#print axioms Run013.local31_dual
#print axioms Run013.localq_dual_two
#print axioms Run013.localq_dual_q
#print axioms Run013.localq_dual_twoq

-- the bridge between coverings and the genuine Kummer image
#print axioms Run013.cov_iff_inKummer
#print axioms Run013.mem_selmerSet_iff

-- models, isogeny, orientation
#print axioms Run013.model_62a1
#print axioms Run013.EqCurve_Δ
#print axioms Run013.EqPrimeCurve_Δ
#print axioms Run013.phi_maps_to
#print axioms Run013.dual_phi_maps_to
#print axioms Run013.dual_comp_phi_eq_double
#print axioms Run013.phi_coeffs
#print axioms Run013.dual_coeffs
#print axioms Run013.phi_selmer_eq_torsion_image
#print axioms Run013.phi_selmer_eq_torsion_image_min

-- LEVEL B
#print axioms Run013.phi_selmer_ncard
#print axioms Run013.dual_phi_selmer_ncard
#print axioms Run013.phi_selmer_ncard_min
#print axioms Run013.dual_phi_selmer_ncard_min
#print axioms Run013.card_middle_of_exact
#print axioms Run013.subsingleton_of_exact
#print axioms Run013.eq_one_of_two_primary

-- LEVEL C
#print axioms Run013.cq_component_root_iff
#print axioms Run013.no_rational_four_torsion
#print axioms Run013.descent_differential_is_half_neron
#print axioms Run013.tamagawa_product_valuation
#print axioms Run013.sha_analytic_two_valuation

end Audit

end Run013
