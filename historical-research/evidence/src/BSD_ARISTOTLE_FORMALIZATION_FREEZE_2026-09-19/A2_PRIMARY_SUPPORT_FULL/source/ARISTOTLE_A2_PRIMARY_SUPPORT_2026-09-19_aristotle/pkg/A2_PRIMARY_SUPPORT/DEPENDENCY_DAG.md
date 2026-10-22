# DEPENDENCY_DAG — A2

```
P2 torsion_decomposition ──► P3 assembly ──► P4 assembly_WC_shape
            │                      └──────► P5 finite_iff_local_and_support (⇐ direction)
P1 primary_zero_of_torsionfree (independent; used where WC (2) turns Sha[p] = 0 into Sha[p^∞] = 0)
CM1, CM1′ (countermodels to the two halves of P5)

J1 JOf_ideal;  J2 JOf_ne_zero_iff ◄── J4 positive_depth_divides;  J3 JOf_generator ◄── J2
CM2 CM_nonzero_everywhere (J = {0} although every local witness is nonzero)

L1 content_dvd_iff ──► L5 content_padic;  L2 content_basic;  L4 exists_primitive ◄── L1, L2
L3 content_unimodular ◄── L1;  L6 content_mod_pk ◄── L1;  L7 content_bounds_J ◄── L5, J2 (construct A)

B1 lemmaB_valuation, B2 lemmaB_cokernel ──► CM3 CM_profinite_perfectness

H0 card_eq_prod_primary ──► H2 order_nine_t_sq;  CM4 CM_order_441 (H2's hypotheses hold, order 441)
STRETCH: S1 alternating_square (would discharge H2's square hypothesis for the abstract pairing); S2 trap; S3 Codex example
```

**Role in WC.**
- P3/P4 is exactly step (3) of Theorem WC.
- J1–J4 is exactly the "finite prime support from a fixed nonzero integer" step.
- L1–L7 formalize the sufficient "descent to ℤ with a primitive comparison" route to J_E ≠ 0, *without* supplying the
  comparison, which remains open.
- H0/H2/CM4 formalize "FIN does not determine the order".
