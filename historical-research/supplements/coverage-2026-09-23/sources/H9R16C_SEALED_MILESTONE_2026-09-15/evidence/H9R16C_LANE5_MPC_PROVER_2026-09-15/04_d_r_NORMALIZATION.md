# 04 — `d_r`: explicit computation and every factor that could have entered

## §1. Result

    d_r = 1     for every r ≥ 1, exactly, on all of H^1(X_{r+1}) (Betti/étale/de Rham), integrally.

No power of `p`, no diamond unit, no sign, no pseudo-eigenvalue, no Gauss sum, no root-number.

## §2. Where each candidate factor would have come from, and why it is absent

| candidate factor | mechanism that would produce it | status in MPC |
|---|---|---|
| `p^{±1}`, `p^{±2}` | a "push-then-pull" composite `ϖ_{i,*}ϖ_j^*` (Hida LMWM (6.6): `π^r_s π^*_{r,s} = p^{s−r}U(p^{s−r})`; KLZ17 Prop 2.4.5: `(pr_2)_*U'_p = p^{k+1}(pr_1)_*`) | absent: MPC contains only `ϖ_2^*ϖ_{1,*}` (pull after push), which equals `U'_p N_{r+1,r}` with the norm element in place of a scalar (02 §3). Numerically confirmed (08: checks (ii),(ii'),(ii'') show the `p` in the *other* composites; (iii),(v) show none in MPC). |
| `p^3 = |ker(G_{r+1} → G_r)|` (Lane 2/4: BCPV (4.9) prints `1/p`, should be `1/p^3`) | the group-ring *projection* normalisation of the *triple* dagger packaging (4.9) | absent: (4.9) is not used; the invariant transition DR22 Lemma 2.8 (`μ^*μ_* = Σ_{K} ⟨d⟩`, no constant) is what MPC realizes on one factor; on one factor the kernel has order `p`, and it appears as the *element* `N_{r+1,r}`, whose image under `π` is `p·1`, not as a scalar (02 §4; 03 Corollary). `P3_REAPPEARS = NO`. |
| Q-rational central diamond `⟨c⟩^{±1}` | an incompatible choice of roots of unity `ζ'_{s+1}` with `ζ'^p_{s+1} = ζ_s^c` (KLZ17 Def 2.5.2 conjugation relation) | absent with the compatible system `ζ_{s+1}^p = ζ_s` (Lemma W, 03). With an incompatible system `d_r = ⟨c⟩^{±1}`, central and harmless (Lanes 1/2/4 §"δ_r"). BCPV/KLZ17 use `ζ_m = e^{2πi/m}` (compatible). |
| tame diamond `⟨p⟩_N^{±1}` | replacing the full-level `W_{Np^s}` by the `p`-part `W_{p^s}` (BSV22 (68): `U_p w_p = w_p U'_p ⟨p⟩_N` versus `U_p w_{Np} = w_{Np} U'_p`) | absent: `A_s` uses the full-level `W_{Np^s}` (BCPV (1.6), (1.8)). Lane 1's K5 hazard, avoided. |
| tame unit `⟨u_r⟩`, `u_r ≡ p (N)` | Hida's μ-model tower with the tame-incoherent root `ζ_Nζ_{p^r}` (Lane 1 C1-c) | absent: everything is on BCPV's point model with `ϖ_1`; Hida's `π^{r+1}_r`, `w_r` are never used. |
| sign `±1` | `W^{-1}` vs `W`; Ohta's `τ_r = W^{-1}` "up to signs" (KLZ17 Rem 7.4.1) | absent in weight 2: `W_s^2 = ⟨−1⟩ = id` on `X_s`, so `W_s^{-1} = W_s`; `W^* = W_*` (03 Lemma W, cohomological form; numerically (vi-a),(vi-b)). |
| pseudo-eigenvalue `λ_{N_g p^r}(g)` | evaluating `W` on a `g`-isotypic line (BCPV (6.?) `a_p(g)^r λ^{-1} ⟨,⟩_r`) | not part of the operator identity; it appears only after specialization/projection to an eigenline and is then the *same* scalar on both sides of MPC at the appropriate level (not needed here; would enter D4-after-specialization bookkeeping, which is BCPV's Cor 6.3 territory and out of this lane). |
| `U'_p`-power mismatch `(U'_p)^{r}` vs `(U'_p)^{r+1}` | the `+1` in the exponent | accounted for exactly: the extra `U'_p` is produced by `ϖ_2^*ϖ_{1,*} = U'_p N` (02 §3). |
| `(p−1)`, `|Δ|`-type factors | Teichmüller/tame-character averaging in BCPV Def 4.9 `p^3/(p−1)^3` | not part of MPC (that is the definition of `Δ^ét_r`, applied identically at every level). |

## §3. Common level `N` versus native level `N_g` (mandatory check 4; `COMMON_TO_NATIVE_LEVEL_CORRECTION`)

MPC was proved for an arbitrary tame level `M` with `p ∤ M`: it holds at the common level `N` (with `W_{Np^s}`)
and at the native level `N_g` (with `W_{N_g p^s}`), each with its own `N_{r+1,r}` (kernel of
`(Z/Mp^{r+1})^× → (Z/Mp^r)^×`, order `p` in both cases, and the two kernels correspond under
`(Z/Np^{r+1})^× → (Z/N_gp^{r+1})^×`). The transport between the two levels, needed only for D4 (05) and not
for MPC, is the tame analogue of Lemma W. Let `t := N/N_g`, `pr^t_1 : X_1(Np^s) → X_1(N_gp^s)`, `(A,P) ↦ (A,tP)`,
and `pr^t_2 : (A,P) ↦ (A/⟨N_gp^sP⟩, P mod)`. With `ζ_{Np^s}^t = ζ_{N_gp^s}` (compatible system), the proof of Lemma W
with `p` replaced by `t` (it used only `deg φ = p` and the two Weil-pairing identities, valid for any `t`) gives

    pr^t_1 ∘ W_{Np^s} = W_{N_gp^s} ∘ pr^t_2,     pr^t_2 ∘ W_{Np^s} = W_{N_gp^s} ∘ pr^t_1     (exactly, no diamond).

Consequently `pr^t_{1,*} W_{Np^s} = W_{N_gp^s} pr^t_{2,*}` on `H^1`, i.e. pushing the `W_{Np^s}`-twisted class down by
the *forgetful* tame degeneracy map (BCPV Def 4.13's `ϖ_{1,*}` at tame level) equals the `W_{N_gp^s}`-twist of the
push-down by the *other* tame degeneracy map. So `COMMON_TO_NATIVE_LEVEL_CORRECTION = pr^t_1 ↔ pr^t_2 interchange, no
scalar and no diamond`; the correction is a *change of degeneracy map*, exactly as in the `p`-direction. (This is
Lane 1's R2 and Lane 3's N3; KLZ17's relation `W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'}` is not needed because both sides use full-level
operators.) If instead one insists on `pr^t_{1,*}` on both sides, the mismatch is the correspondence
`pr^t_{1,*}pr^{t,*}_2`-type object, not a scalar — that is a statement about BCPV's Def 4.13 construction, flagged in 07
for the referee; it does not affect MPC.

## §4. What the numerical check certifies (08, `_verify/msym_check.py`)

For `(N_g,p,r) ∈ {(5,3,1),(2,3,2),(7,2,1),(3,2,2),(4,5,1),(1,5,2),(1,7,1)}` (levels `M → pM` = 15→45, 18→54, 14→28,
12→24, 20→100, 25→125, 7→49), on the full space of weight-2 modular symbols `H_1(X_1(L), cusps; F_ℓ)` for two primes
`ℓ ∈ {1000003, 999983}`, each operator realized directly from its definition as a set of matrices acting on paths
(no use of the derivation), the identity (v) `ϖ_1^*A_rϖ_{1,*} = A_{r+1}N_{r+1,r}` holds with `rank(LHS) = rank(RHS) =
dim MS(M)` where checked, and the alternatives `d_r ∈ {p, p^{-1}, p^2, p^{-2}, −1}` are excluded whenever `RHS ≠ 0`.
The auxiliary identities (i)–(iv) and (vi) pass as well. Logs: `_verify/msym_check_all.log` (pure Python: (2,3,2),(7,2,1),(3,2,2) both primes, (4,5,1) first prime; the run was then stopped as redundant), `_verify/msym_check_np2.log` ((4,5,1), both primes, numpy variant), `_verify/msym_check_np.log` ((1,7,1) and (1,5,2), both primes, numpy variant); the first case (5,3,1) was run interactively (both primes, ALL PASS) and is reproduced by `python3 msym_check.py 5,3,1`. Ranks: (5,3,1) 17/17 = dim; (2,3,2) 15/15 (dim 19); (7,2,1) 13/13 = dim; (3,2,2) 7/7 (dim 9); (4,5,1) 25/25 = dim; (1,7,1) 5/5 = dim; (1,5,2) 43/43 (dim 51). The `r = 2` cases have rank < dim MS(M) because `ϖ_{1,*}` from level `p^3 N_g` onto `MS(N_g p^2)` composed with `A_r` need not be surjective; both sides agree exactly.
