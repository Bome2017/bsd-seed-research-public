# 05 — Next handoff (Lane 4 → coordinator / Lanes 1–3)

## Closed by this lane (ship these as theorems/defects; do not re-derive)

| ID | Statement | Where | Status |
|---|---|---|---|
| L4-T1 | Receptacle A_r^† := I_r^†⊗_Z J_r (H9R8/H9R12) has T_p of Z_p-rank \|G_r\|·2g, whereas BCPV's M^† = M⊗_{Z_p[G_r]}Z_p[G_r]^† has rank 2g. The H9R9 line "NO TYPE MISMATCH AFTER CONTRACTION" is refuted for that object. | 03 §1 | PROVED (MRS Thm 2.1, 2.2(iii); BCPV Def 4.6) |
| L4-T2 | On G_r-invariants, the frozen τ^geom = s_r⊗ϖ_* equals p^3·ϖ_* in M-coordinates; DR22 L2.8 has no constant. | 03 §1 | PROVED |
| L4-T3 | Twisted descent: for σ ∈ G_{Q(μ_p)}, σ∘Φ̄^mod_r = <m_σ>^{1/2}_{(1)}<n_σ>_{(1)}∘Φ̄^mod_r∘R(<n_σ>); the p-part auxiliary twists cancel exactly; the tame part does not. On the g-branch it is ε_g^{(t)}(n_σ). | 03 §2 | PROVED from Hida p.15 conjugation law + BCPV (4.1)–(4.4), L4.2(ii) + H9R16-A/B balance |
| L4-T4 | BCPV (4.9) with factor 1/p makes (4.8) commute only up to p^2; the consistent constant is 1/p^3. | 03 §3 | PROVED (arithmetic; independent re-check requested) |
| L4-T5 | Literal Cor_{F_{r+1}/F_r} on one vertical against descent+p_{r+1,r} on the other differs by p per level. | 03 §4 | PROVED |
| L4-T6 | Kummer injectivity survives p-completion, ⊗Q_p and fixed-base descent; coefficients must enter via Hom, not ⊗. | 03 §6 | PROVED |

## Open, in dependency order

1. **Lane 1 (C1)**: literal BCPV W normalization. It must confirm W^σ = <z>W (sign only matters for exponents) and give δ_r. Also
   (a) the model identification (A,P) ↔ Hida's (E, μ_{Np^r} ↪ E) and its effect on ϖ_1 ↔ π and U'_p ↔ U*(p); (b) common-level
   W_{Np^r} (in Δ^ord) versus native W_{N_gp^r} (in A_r) under the push-down N → N_g.
2. **Lane 2 (C2)**: adopt the retyped receptacle P^♮_r (04 §1) and the typed relation (T♮_r) (04 §3), NOT the frozen dagger-only
   square. The smallest missing lemma is (★_r) (04 §4) together with its p-power constant.
3. **Lane 3 (literature)**: look for (★_r) or its étale shadow ("modified Poincaré pairings are compatible with degeneracy maps"),
   which BCPV assert in words below (1.7) without a numbered statement; candidates [KLZ17 §7], [Oht99 §2.2], [BSV22 Prop 3.2–Rem 3.3].
   Also re-check the BCPV (4.9) constant against [DR22, L2.8] and the published BCPV version, if any.
4. (K_r) finite operator-level Kummer realization: formal, write it out.

## Do-not-redo / do-not-use

* Do not use A_r^† := I_r^†⊗_Z J_r as the Kummer receptacle, and do not use s_r⊗ϖ_{1,*} as the transition on it.
* Do not write any vertical map from BCPV (4.9) literally; use DR22 L2.8.
* Do not put a cyclotomic corestriction on one side of the square and descent/group-ring projection on the other.
* Do not assume a dagger-only receptacle over Q(μ_p) contains the A_r-modified point when ε_g^{(t)} ≠ 1; that is the actual
  Castella–Hsieh case (η_{K/Q}).
* Do not apply ϖ_{1,*} uniformly to factor 3 after A_r-transport (03 §7).
* Do not build τ^MW from Hida's w-twisted π^r_s while τ^et is BCPV's untwisted ϖ_{1,*} without writing both W-conjugations (03 §5).

## Downstream risks noticed, NOT asserted (out of C's scope; for the owner of the weight-one gates)

* BCPV require k_∘ = 0 for f and g (§1.1.4 fn 2) and ε_g = ε_g^{(t)} (§1.1.5). Castella–Hsieh's g-family lies in
  S^o(C, ω^{-1}η_{K/Q}, ·), which has a p-part ω^{-1} in its character. Whether the Castella–Hsieh weight-one point lies on a
  BCPV-admissible component depends on the two papers' Λ-adic character conventions, which this lane did not reconcile.
  Check before weight-one specialization; H9R15 is not reopened by this remark.
* Castella–Hsieh's third family is h = θ_{χ^{-1}}; BCPV's is g^c = g⊗ε_g^{-1}. They must be identified with conventions before any
  coefficient specialization.

## Custody

Lane directory: /Users/bsm/H9R16C_LANE4_HOSTILE_OBSTRUCTION_2026-09-15 (sources/ holds the PDFs and text layers; _work/ holds the
page-verified notes 01–06). Nothing was sent or published. The independence of this lane was preserved: no other lane's directory
contents were read.
