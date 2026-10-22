# 09 — VERDICT (H9R16-C final assembly referee, 2026-09-15)

    H9R16C_CLOSED

**Inverse-limit point module created** (08 §1), with `B^bal_r ≅ R_r = e'_ord𝕋'_{N_gp^r}⊗Z_p`,
`𝒫^♮_r = Hom_{Z_p}(B^bal_r, Ĵ^{(1)}_r(F'_r)^{ord})^{Gal(F'_r/K_0),⋆}`,
`Q_r = (U'_p)^{-r}_{(1)}∘Φ̄^mod_r∘(U'_p)^{-2r}_{carrier}`, `τ_r^MW(x) = ϖ^{(1)}_{1,*}∘x`,
`π_r^*(y) = y∘res^bal_{r+1,r}`, `N_{r+1,r} = Σ_{d≡1 (N_gp^r)}⟨d⟩`:

    𝒫^♮_∞ := { (Q_r)_{r≥1} ∈ ∏_r 𝒫^♮_r : τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r}) = π_r^*(Q_r) ∀ r ≥ 1 },

a module over Hida's big ordinary Hecke algebra `𝕋'_∞(N_g) = lim_r R_r` acting through the carrier, with the
tame `ε_g^{-1}` twist inside ⋆. The system `𝒬_∞ = (Q_r)_r` built from BCPV's cycles lies in `𝒫^♮_∞`,
integrally, with constant 1.

**Next gate** `G_BIG_KUMMER_TRACE` (08 §3): prove
`Kum_∞(𝒬_∞) = (Kum^♮_r(Q_r))_r ∈ lim_r H^1(K_0,T^♮_r)` is the restriction to `K_0` of BCPV's big trace class
`Δ^tr(f⊗ad(g)) = (id⊗tr)Δ^ét(f⊗ad(g)) ∈ H^1(Q,T_f^†)`, under the branch identification of the carrier and
with the normalization dictionary of 08 §4 ((U'_p)^{-r}/(U'_p)^{-2r} vs `a_p(f)^{-r}a_p(g)^{-2r}`;
`Δ^tr_r = a_p(g)^rλ_{N_gp^r}(g)^{-1}Δ^{(P)}_r`; `Δ^ét_∞ = {(U'^{⊗3}_p)^{-r}Δ^ét_r}`), **before** weight-one
coefficient specialization.

## Status, one line per item

    ITEM1_POINT_OBJECT   = PROVED   explicit map b ↦ pd^{t_f}_*(Π_{Γ(b),*}Δ_r^ord[e]); Γ_A orientation fixed by
                                     §C (A_r on factor 3, plain diagonal Z); carrier B^bal_r; ⋆ per B5;
                                     packaging removed by BCPV's G, μ_r refused; Φ̄^mod_r ∈ 𝒫^♮_r   (03)
    ITEM2_HOM_VALUED_D4  = PROVED   evaluationwise A6 + linearity + frozen balance ⇒ Hom-valued identity over
                                     F'_r; ⋆-invariance transported through Kum; unique descent to K_0
                                     ((T_pJ)^{G_{F'_r}} = 0); E′(a) derived, (4.9) not used              (04)
    ITEM3_TAME_PUSHDOWN  = PROVED   tame push-down NOT_PRINTED in BCPV (02a §1), fixed as pr^t_1 by the
                                     inherited KLZ17 l.544–551/l.800 + DR22 l.1149–1154 index convention AND
                                     shown immaterial (either index gives the same relation and constant);
                                     A5 transports W across levels ((★): A_r pr^t_{1,*}W_{Np^r} = (U_p)^r pr^t_{2,*});
                                     chain MPC(native) + Cor 4.11 + D4_{r+1} + D4_r + normalizations gives
                                     τ_r^MW(Q_{r+1})∘(1⊗N_{r+1,r}) = π_r^*Q_r with constant 1, integrally;
                                     Kummer injectivity applied evaluationwise over F'_{r+1}              (05)
    ITEM4_RANK_FACTOR    = PROVED   no |G_r|, no p^3, no p^{±1}/p^{±2}: carrier ≅ R_r; type-B receptacle;
                                     transition is ϖ_{1,*}∘(−), not s_r⊗ϖ_*; (4.9) unused; BCPV's
                                     p^3/(p−1)^3 is level-independent; the unique p is π_r(N_{r+1,r}) = p.
                                     μ_r computed: Φ̄^mod∘(1⊗Σ⟨d_2d_3⟩^{-1}) — |G_r| or 0, hence refused   (06)
    ITEM5_TAME_TWIST     = PROVED   ε_g^{-1} preserved by ϖ^{(1)}_{1,*}, π_r/res^bal, 1⊗N_{r+1,r} (elements
                                     ≡ 1 mod N_g ⇒ trivial tame part), both tame push-downs, and the U'_p
                                     normalizations; both sides live in one ⋆-module                      (07)

    NUMERICAL (new, this referee): _verify/msym_tame_check.py (imports Lane 5's msym_check.py unmodified)
      cases (N_g,t,p,r) = (3,3,2,1), (5,3,2,1), (5,2,3,1), primes 1000003 & 999983, levels ≤ 90:
      A5 (T5-a/T5-b), pr^t_{i,*}U'_p = U'_p pr^t_{i,*}, diamond compatibility, pr^t_{i,*}ϖ_{1,*} = ϖ_{1,*}pr^t_{i,*},
      and (★). 91 checks, ALL PASS, 0 FAIL. Log: _verify/tame_check.log.

## Findings that are corrections, not defects

1. **B5 `(T♮_r)` / Lane 5 `05` §4 normalization wording** (05 §6): with the factor-1 normalization alone the
   constant is **not** 1 — the leftover is `(1⊗(U'_p)^2)` on the carrier, exactly BCPV's `a_p(g)^{-2r}`.
   With the charter's `Q_r` (Lane 2 T3, carrier normalization `(U'_p)^{-2r}`) the constant is 1.
2. **02 §D P4/§E** (confirmed by 02a): BCPV print no tame-direction definition of `ϖ_1`; the forgetful
   reading is justified by inheritance, not by their text — and the verdict is independent of it (05 §4).
3. **02 §D P1** (02a §2): the `p^3` is a type-A/`s_r⊗ϖ_*` phenomenon; for the Lane-5 packaging the
   multiplication identification gives `|G_r|`-or-`0`, computed in 06 §2, and is avoided by construction.

## Carried into the next gate (recorded, none used above)

    R1  (AJ-corr) numbered citation still unpinned in the packet — frozen as PROVED_FORMAL by the operator
    H_π ring maps π_r with ϖ_{1,*}t = π_r(t)ϖ_{1,*} — standing input of the statement itself (B6)
    TAME_PUSHDOWN_SCALAR  pr^t_1 vs pr^t_2 changes the constructed point by a tame Hecke scalar at ℓ | t;
                          must be fixed before any statement naming λ_{N_gp^r}(g) or a_p(g)^{±r}   (05 §5)
    DRIVE_CHECKPOINT = NOT_OBTAINED; the two local copies of §C agree on every load-bearing formula (10)

## Prohibitions honoured

BCPV (4.9) not used; Hida's w-twisted tower not used; no inverse-limit identification, density, H9R15
localization, f-branch extraction, weight-one specialization or big Kummer trace used to patch C (the gate is
stated at the end, as required). No Lean, no Aristotle, no messages, no publishing, no git. Lanes 1–5 and
files 00–02/02a unmodified (custody re-verified against `_work/LANE_FILES_AT_LAUNCH.sha256`).

    H9R16C_STATUS = CLOSED
    FIRST_EXACT_DEFECT = none found in R2 (packaging) or R3 (tame push-down)
