# DEPENDENCY_DAG — A1

```
IMPORTED_ARITHMETIC_THEOREM (hypotheses only, never proved here)
  H11 Ota Thm 5.17 (group-ring form)   H5 Ota Thm 1.5   H3/H12 Selmer corank facts (rank 2)   H2 Sha torsion
NOT_PART_OF_THIS_TASK
  H6 antecedent: A ≠ 0 ∧ A ∈ J_E        H7 finiteness of the S0-primary groups (hypothesis of conclusion (3))
FORMAL_ASSUMPTION
  H1 bounded exponent (abstract)   H8 2 ∈ S0   H9 G_S finite abelian   H10 prime-to-p units (Z_p)

PROVED_IN_PACKAGE (targets)
  T1 lemmaA_comm ──► T2 gr_killed_by_exponent ──► T3 gr_p_primary ◄── (H9, H10; T10 for ℤ_[p], T11 for (ZMod S)ˣ)
  T4 bridge_517 (+ T4b cls2_zero_iff)
  T5 depth_spec, T5b zero_infinitely_divisible ──► T6 hInf_lt_top_iff, T6b hInf_le_iff ──► T6c JE_bounds
  T7 WC_abstract  ◄── T6, T6b, T6c + internal primary-assembly lemma + H1, H2, H3, H4, H5, H6 (+ H7 for (3))
  T8 WC_groupRing ◄── T7 + T3 (discharges H1) + T4 (turns H11 into H4, using H8, H12) + H2, H3, H5, H6 (+ H7)
  T9a CM_uniform_denominator (independent)  ──► T9b CM_nonzero_everywhere
  T12 WC_abstract_nonvacuous (independent)
  STRETCH: S1 lemmaA_general (generalises T1);  S2 gr_finite_Z (uses T2 + Noetherianity);  S3 gr_rational_trivial (uses T2)
```

**Where arithmetic enters.** Only through H2, H3, H5, H6, H7, H11 and H12, all explicit hypotheses of T7 and T8. No target
derives any of them.

**Proof architecture of T7** (Codex WC §2):
1. **Conclusion (1).** From A ≠ 0 and T6c, h_p ≤ v_p(A) < ∞. By T6 there is a nonzero witness t(p,S). If Sha[p^∞] were
   infinite, H3 would give r p ≥ 3, and then H4 would give t(p,S) = 0, a contradiction.
2. **Conclusion (2).** If p ∤ A, then h_p = 0 (T6c). By T6b (using H1) some witness has ¬PDvd p 1. H5 then gives Sha[p] = 0,
   and every p-primary element x = 0 follows by induction on k in p^k • x = 0.
3. **Conclusion (3).**
   - By H2, every x ∈ Sha is a finite sum of elements of primary parts: for n•x = 0, write 1 = Σ u_q·(n / q^{v_q(n)}).
   - Only primes in S0 ∪ primeFactors(A) can contribute, by (2).
   - Their primary parts are finite, by (1) and H7.
   - So Sha is the image of a finite product of finite sets, hence finite.
