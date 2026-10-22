# 00 — Verdict (Lane 5: fresh H9R16-C finite modified-pairing prover, 2026-09-15)

## Result

**MPC_r is PROVED, with `d_r = 1` and `ν_{r+1} = N_{r+1,r} = Σ_{d ≡ 1 (mod N p^r)} ⟨d⟩`**, as an identity of algebraic
correspondences on `X_1(N p^{r+1})`, hence on all of `H^1` (Betti, étale `Z_p(1)`, de Rham), integrally, for every
tame level `N` prime to `p` and every `r ≥ 1`:

    ϖ_1^* ∘ W_{Np^r}^{-1}(U'_p)^r ∘ ϖ_{1,*}  =  W_{Np^{r+1}}^{-1}(U'_p)^{r+1} ∘ N_{r+1,r},

equivalently `⟨ϖ_{1,*}y, A_rϖ_{1,*}z⟩_r = ⟨y, A_{r+1}N_{r+1,r}z⟩_{r+1}`. Restriction to `e'_ord H^1` is BCPV's setting; nothing
about ordinarity is used. Conventions: BCPV/DR22/KLZ17 (`ϖ_1(A,P) = (A,pP)`, `U'_p = π_{1*}π_2^*`, KLZ17's moduli `W`
with a compatible system of roots of unity `ζ_{Np^{s+1}}^p = ζ_{Np^s}`).

The proof (02, 03) is four lines from three cycle identities, each proved twice (double cosets and moduli):

1. `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` (DR22 §1.3, re-derived);
2. Lemma W: `W_{Np^s}∘ϖ_1 = ϖ_2∘W_{Np^{s+1}}` and `W_{Np^s}∘ϖ_2 = ϖ_1∘W_{Np^{s+1}}` **exactly** (no diamond) with compatible `ζ`'s;
3. **the norm-element identity** `ϖ_2^*∘ϖ_{1,*} = U'_p∘N_{r+1,r}` — the fibre of `ϖ_2` over `ϖ_1(y)` is the `U'_p`-orbit of
   the `K_r`-orbit of `y`; this is the Galois pushforward `μ^*μ_*` of DR22 (proof of Lemma 2.8) on one factor.

Then `ϖ_1^*W_rU'^rϖ_{1,*} = ϖ_1^*W_rϖ_{1,*}U'^r = W_{r+1}ϖ_2^*ϖ_{1,*}U'^r = W_{r+1}U'N U'^r = A_{r+1}N`.

**Why no `p`-power:** the `p`-powers of Hida (6.6) `π^r_sπ^*_{r,s} = p^{s−r}U(p^{s−r})` and KLZ17 Prop 2.4.5 `(pr_2)_*U'_p = p(pr_1)_*`
arise in push-then-pull composites `ϖ_{i,*}ϖ_j^*`; MPC contains the pull-after-push composite `ϖ_2^*ϖ_{1,*}`, which is a
sum over a coset space and yields the *element* `N_{r+1,r}` (whose image under `Z_p[Δ_{r+1}] → Z_p[Δ_r]` is `p`), not a scalar.

**Independent numerical confirmation** (`_verify/msym_check.py`, `msym_check_np.py`; logs in `_verify/`): every operator
was implemented directly from its definition as matrices acting on weight-2 modular symbols (Manin symbols for
`Γ_1(L)`, full relative homology `H_1(X_1(L), cusps)`), and MPC_r together with all auxiliary identities was checked
exactly modulo two primes (`1000003`, `999983`) for `(N_g, p, r)` = (5,3,1), (2,3,2), (7,2,1), (3,2,2), (4,5,1), (1,7,1)
and (1,5,2) (levels 25→125, `dim MS(125) = 1201`, both primes, `rank(LHS) = rank(RHS) = 43`), with `rank(LHS) = rank(RHS)` (`= dim MS(M)` whenever `r = 1`), and the
alternatives `d_r ∈ {p^{±1}, p^{±2}, −1}` excluded. KLZ17 Prop 2.4.5 and BSV22 (68) are reproduced by the same code.

## The other mandatory checks

* `N_{r+1,r}` derived from the coset/moduli structure (02 §3), not imported. Lane 2's *expected* value (derived there
  under a "group-ring-pairing hypothesis") coincides with it; here the hypothesis is a theorem (03 Corollary).
* `d_r` computed: `1`. Every candidate factor and its absent mechanism is tabulated in 04 §2.
* `P3_REAPPEARS = NO`: the type-A `p^3` (= `|ker(G_{r+1}→G_r)|` for the triple group; BCPV (4.9)'s defective constant)
  is the scalar shadow of the product of three per-factor norm elements; on the type-B object each factor carries the
  element `N_{r+1,r}` (order-`p` kernel) and no scalar (04 §2, 05 §3–4).
* Tracking: native `N_g` vs common `N` (04 §3: MPC holds at both; the transport `pr^t_1∘W_{Np^s} = W_{N_gp^s}∘pr^t_2` is a change
  of tame degeneracy map, no scalar, no diamond); `W_{Np^r}` vs `W_{N_gp^r}` (same); diamonds (only through `N`); tame
  nebentype and `g^c` (never enter MPC; enter the descent of the packaged point, Lanes 2/4, used in 05); `U'_p` vs `U(p)`
  (01 §4, 02 §1 — BCPV's `U'_p` = DR22's `U_p^*` = KLZ17's `U'_p`; adjoint of the classical `U_p`); the Lane-1 `α_r`
  bridge, `⟨u_r⟩`, `⟨c_r⟩` (not needed: no Hida-model object is used anywhere).
* KLZ17 Thm 7.2.3(v) used for nothing; its finite-level content is 03 Corollary (`π(⟨⟨x,y⟩⟩_{r+1}) = ⟨⟨ϖ_*x,ϖ_*y⟩⟩_r`, constant 1).
* Ohta II unavailable and not needed: no finite-control step of this lane's claims remains unverified (06 §"Not available").
* DR22 Lemma 2.8 is the transition used (its `μ^*μ_* = Σ_K⟨d⟩`); BCPV (4.9) is not used.
* No density, no H9R15 localization, no weight-one specialization, no big Kummer trace.

## D4

Written and proved in 05 for the point `P_r[[a,b,c]] := Σ_g Π_{A_r,*}Δ^ord_r[g·(a,b,c)] ⊗ g` built from BCPV's own cycle
`Δ^ord_r` and the correspondence `Π_{A_r} = X_{14} × Γ_{A_r}` (BCPV §7.2's `Π_Z` with the diagonal replaced by the graph of
`A_r`): `Kum(P_r[[a,b,c]]) = Contr^{A_r}_*(Δ^ét_r[[a,b,c]])`, over `Q(μ_{Np^r})` and, after Lanes 2/4's twisted descent, over
`Q(μ_p)` on the type-B, tame-twisted carrier. Formal from one standard input: functoriality of the étale Abel–Jacobi map
under algebraic correspondences (Jannsen LNM 1400 §9 / Nekovář 2000 §1; exact numbering to be pinned by the referee, R1),
plus the cycle-class/operator dictionary BCPV themselves use in Prop 6.2. D4 + MPC + BCPV Cor 4.11 give the typed
integral point tower with `δ♮_r = 1` (05 §4). The identification of this `P_r[[a,b,c]]` with H9R16-A/B's `P_r^{tr,†}` is
not made here (definition not in the packet; R2).

## Files

00 this · 01 objects/types · 02 norm element · 03 MPC proof · 04 `d_r` · 05 D4 · 06 source ledger · 07 handoff ·
08 hashes · `sources/` · `_verify/` (script, numpy variant, logs).

LANE = 5 — fresh H9R16-C finite modified-pairing prover (MPC_r(N_{r+1,r}))
STATUS = STOP_A — MPC_PROVED with d_r = 1 explicitly controlled; D4 PROVED (formal, one standard input to pin); H9R16-C's operator-level gap (Lane 2 MPC_r(ν), Lane 4 (★_r)) CLOSED
PROVED = L5-T1 Lemma W (exact interchange, no diamond, compatible ζ); L5-T2 ϖ_2^*ϖ_{1,*} = U'_p N_{r+1,r}; L5-T3 MPC_r with d_r = 1 on all of H^1; L5-T4 group-ring form π(⟨⟨x,y⟩⟩_{r+1}) = ⟨⟨ϖ_*x,ϖ_*y⟩⟩_r; L5-T5 tame transport pr^t_1∘W_{Np^s} = W_{N_gp^s}∘pr^t_2; L5-D4 Kum(P_r[[a,b,c]]) = Contr^{A_r}_*(Δ^ét_r[[a,b,c]]) (given (AJ-corr)); all numerically confirmed in 7 cases × 2 primes except D4 (not numerical)
REFUTED = "a power of p (cf. Hida (6.4)) may survive in the modified-pairing/degeneracy compatibility" (Lane 4 §4 hazard): no — the p-powers live in ϖ_{i,*}ϖ_j^*, not in ϖ_2^*ϖ_{1,*}; "BCPV (4.9)'s 1/p is the transition constant": not used, not needed (DR22 L2.8 has none; the per-factor kernel enters as the element N_{r+1,r})
FIRST_EXACT_UNPROVED_STATEMENT = none inside this lane's target. Outside it (for the referee): (R1) the numbered citation for AJ-functoriality under correspondences; (R2) definitional identification P_r^{tr,†} (H9R16-A/B) = P_r[[a,b,c]] (05 §2), including which tame push-down (forgetful vs quotient) H9R16-A/B used at the common→native step (04 §3)
TYPE_CHECK = PASS: all operators are correspondences on X_1(Np^{r+1}) over Q(μ_{Np^{r+1}}); W^{-1} = W (weight 2); N_{r+1,r} central; pairing form ⇔ operator form by the projection formula; type-B packaging is Z_p[G_r]-linear in the contraction; restriction H^1(K_0,·) → H^1(F',·) injective
NEW_ASSUMPTIONS = compatible roots of unity ζ_{s+1}^p = ζ_s (BCPV/KLZ17 convention; an incompatible choice changes d_r by a central Q-rational diamond, harmless per Lanes 1/2/4); standard Weil-pairing identities (Silverman III.8.1(e), III.8.2); (AJ-corr) for D4 only
COUNTEREXAMPLE_OR_OBSTRUCTION = none. Searched: p-powers, diamond units, signs, tame diamonds ⟨p⟩_N, ⟨u_r⟩/⟨c_r⟩, pseudo-eigenvalues, U-exponent mismatch, (p−1)-factors, cusps (04 §2)
NEXT_SMALLEST_TEST = referee items R1–R3 (07); optional: exact-Q rerun of _verify (10-line change) and a case with N_g ∤ N (common vs native) exercising 04 §3 numerically
ARISTOTLE_READY = NO (general-r theorem needs moduli of curves / double cosets, not in a formal library; per-case certificates exist as the _verify computation)
STOP_ROUTE = YES

FINAL BLOCK
MPC_STATUS = MPC_PROVED
NORM_ELEMENT = N_{r+1,r} = Σ_{d ∈ ker((Z/Np^{r+1})^× → (Z/Np^r)^×)} ⟨d⟩  (order-p kernel; = μ^*μ_* for DR22's Galois cover μ; image p under p_{r+1,r})
d_r = 1  (exactly; integral; all of H^1)
P3_REAPPEARS = NO
COMMON_TO_NATIVE_LEVEL_CORRECTION = none in MPC (holds at each tame level with its own W); transport is pr^t_1∘W_{Np^s} = W_{N_gp^s}∘pr^t_2 (change of tame degeneracy map, no scalar, no diamond) with ζ_{Np^s}^t = ζ_{N_gp^s}
D4_STATUS = PROVED_FORMAL (given AJ-functoriality under correspondences, citation to pin) on the type-B tame-twisted carrier for the BCPV-built point; identification with H9R16-A/B's P_r^{tr,†} left to the referee
FIRST_EXACT_UNPROVED_STATEMENT = none in-lane; referee items R1 (citation), R2 (definitional identification), R3 (tame push-down convention)
ARISTOTLE_READY = NO
STOP_ROUTE = YES
