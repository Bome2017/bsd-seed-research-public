# 00 — Operator freeze record (written before the final assembly referee was launched)

Date: 2026-09-15. Source: the operator's own review message in the coordinating session, recorded here
without editing its conclusions. The operator inspected the Lane 5 archive, read the MPC proof and the
norm-element derivation, and independently reran `_verify/msym_check.py` for (N,p,r) = (5,3,1) at both
verification primes (1000003, 999983). Every auxiliary identity and MPC passed exactly.

## Frozen now (operator verdict)

    H9R16C_MPC            = PROVED
    NORM_ELEMENT          = PROVED      N_{r+1,r} = Σ_{d ∈ ker((Z/Np^{r+1})^× → (Z/Np^r)^×)} ⟨d⟩
    d_r                   = 1
    P3_REAPPEARS          = NO   (in MPC)
    SCALAR_D4             = PROVED_FORMAL   (étale Abel–Jacobi functoriality under correspondences)
    PACKAGED_D4           = NEEDS_FINAL_BALANCED_CARRIER_IDENTIFICATION
    POINT_TOWER_RELATION  = REDUCED_TO_FORMAL_TYPED_ASSEMBLY
    H9R16C_STATUS         = ONE_PACKAGING/TYPE_ASSEMBLY_CHECK_FROM_CLOSED

Central identity accepted:  ϖ_1^* W_{Np^r}^{-1}(U'_p)^r ϖ_{1,*} = W_{Np^{r+1}}^{-1}(U'_p)^{r+1} N_{r+1,r},
via ϖ_{1,*}U'_p = U'_pϖ_{1,*},  ϖ_1^*W_r = W_{r+1}ϖ_2^*,  and the new lemma ϖ_2^*ϖ_{1,*} = U'_p N_{r+1,r}.
The pull-after-push vs push-after-pull distinction is what excludes the feared p-factor.

## What the operator does NOT yet accept (the reason for the referee)

1. **Packaged point.** Lane 5 05 §2 writes Σ_{g∈G_r} P_r[g·(a,b,c)] ⊗ g ∈ J_r(F') ⊗ Z_p[G_r] and passes
   quickly to the type-B descended object. Acceptable as intermediate packaging; NOT accepted as the final
   coefficient-retaining MRS object until the quotient/balancing map is written explicitly. Lane 4 already
   showed the post-contraction dagger group is the factor-1 quotient, not the triple G_r.
   Proposed point object:
       𝒫_r^♮ = Hom_{Z_p}(B_r^bal, Ĵ_r^{(1)}(F'_r)^ord)^⋆
   with the factor-1 dagger (+1/2 MRS lattice convention), the surviving tame g^c / ε_g^{-1} carrier twist,
   and the balanced auxiliary-Hecke module B_r^bal. Point = Φ_r^mod : B_r^bal → Ĵ_r. D4 proved
   evaluationwise on every b ∈ B_r^bal, then by linearity:  Kum(Φ̄_r^mod) = Contr^{A_r}_*(Δ_r^ét).
2. **Tower relation.** Replace Lane 5 05 §4's schematic normalized-point equation by Lane 2's typed relation
       τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r}) = π_r^* Q_r    inside  Hom(B_{r+1}^bal, Ĵ_r)^†,
   because the carrier is contravariant (B_{r+1}^bal → B_r^bal gives π_r^*: Hom(B_r^bal,−) ↪ Hom(B_{r+1}^bal,−));
   there is no naive map P_{r+1} → P_r. Kummer naturality + injectivity then give the point identity.
3. **R3 (smaller).** L5-T5 pr_1^t W_{Np^s} = W_{N_g p^s} pr_2^t (no scalar, no diamond). Remaining: which tame
   degeneracy map BCPV's branch projection actually uses, so H9R16-A/B and Lane 5 use the same push-down.
   Bookkeeping; cannot produce d_r ≠ 1.

## Instruction

Do not send MPC to another prover. Launch one fresh Opus as FINAL ASSEMBLY REFEREE, treating MPC, d_r = 1 and
scalar D4 as inputs, to decide whether they imply the correctly typed point-tower theorem (charter: 01).
If the referee passes: H9R16-C = CLOSED, and the next gate is G_BIG_KUMMER_TRACE (inverse-limit Kummer class
= BCPV's big trace class before weight-one coefficient specialization).

## Custody at launch

`_work/LANE_FILES_AT_LAUNCH.sha256` — SHA-256 of every Lane 1–5 deliverable (00–0x, _parts, _verify scripts
and logs) at the moment the referee was launched. Nothing in Lanes 1–5 is modified by this directory.
