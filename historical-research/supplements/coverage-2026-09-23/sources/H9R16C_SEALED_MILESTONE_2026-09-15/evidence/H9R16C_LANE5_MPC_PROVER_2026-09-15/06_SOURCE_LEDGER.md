# 06 — Source ledger (what was used, for what, and what was NOT used)

Files: `sources/` (hashes in 08). Line numbers refer to the TeX sources in `sources/tex/` (BCPV.tex, DR22.tex,
KLZ17.tex) or to the pdftotext layers.

## Used, load-bearing

| ref | statement used | where | role |
|---|---|---|---|
| BCPV (1.6) `eqn_2023_09_29_1444` (BCPV.tex 512–518) | modified pairing `x⊗y ↦ ⟨x, W_{N_hp^r}^{-1}(U'_p)^r y⟩ ∈ Z_p[Δ_{N_hp^r}]⊗χ^{k+1}` | 01 §5, 03 Cor | defines `A_r`, group-ring target |
| BCPV (1.8)–(1.9) `eqn_2023_11_06_1518/1525` (BCPV.tex 538–545) | `W^{-1}(U'_p)^r : e'_ordH^1 ≅ e_ordH^1`, inverse `U_p^{-r}W`; `e'_ord = lim (U'_p)^{n!}` | 01 §4–5 | conventions |
| BCPV §4.2 (BCPV.tex 1206–1213) | `ϖ_1(A,P) = (A,pP)`; `X_1(Np^r)` point model | 01 §2 | convention |
| BCPV (4.4) `eqn_2023_11_08_1351` (1247–1250) | `Δ_r^ord = (e'_ord W_{Np^r})^{⊗3}Δ_r` | 05 | D4 objects |
| BCPV Lemma 4.10 + proof (1409–1419) | `ϖ_{1,*}^{⊗3}Δ^ord_{r+1} = U'^{⊗3}_pΔ^ord_r`; "W interchanges `ϖ_{1,*}`, `ϖ_{2,*}`, intertwines `U_p`, `U'_p`" | 03 Lemma W (cohomological form), 05 | printed form of Lemma W's consequence |
| BCPV Cor 4.11 (1421–1432) | same on `Δ^ét[a,b,c]`, `Δ^ét[[a,b,c]]`, `Δ^ét_r` | 05 | D4 tower |
| BCPV (4.7) `eqn_2023_11_10_1126`, Rem 4.5(i) (1319–1348) | group-ring packaging `Δ^ét[[a,b,c]] = Σ_G Δ^ét[g·(a,b,c)]g`, `G`/`G^{-1}` | 05 | packaging |
| BCPV Def 4.6 (1366–1370) | `Z_p[G_r]^†`, `M^† = M ⊗_{Z_p[G_r]} Z_p[G_r]^†` (type B) | 05 | receptacle |
| BCPV Lemma 4.7 + proof (1371–1400) | descent of `Δ^ét[[a,b,c]]` to `Q(μ_p)` via inflation–restriction; `σ_m` action | 05 | descent |
| BCPV §6, Prop 6.2, Rem 6.4 `remark_2023_11_22_0818` (1760–1815) | specialized comparison `P_r^∘ = Π_{Z,*}Δ^∘`, Cartesian square after `log_BK` | 05 §5 | the printed (specialized, local) D4 |
| DR22 §1.3 (DR22.tex 1150–1200) | `ϖ_1: τ↦τ`, `ϖ_2: τ↦pτ`, `ϖ_i = π_i∘μ`, `μ` cyclic Galois of degree `p`; `U_p^* := π_{1*}π_2^*`; compatibility with `ϖ_{1*}` | 01 §2–4, 02 §2(c) | conventions |
| DR22 (eqn:galois-pushforward) + Lemma 2.4 `lemma:compat-cycles-proj` (2095–2160) | `j^*j_*(Δ) = Σ_{σ∈G}σΔ` for Galois `j`; `(ϖ_2^3)_*Δ_{r+1} = U_p^{⊗3}Δ_r`; distribution relation | 02 §3 (relation), 05 | invariant transition |
| DR22 (2.17)-type pairing (eqn:pairing-LambdaG, 2250–2285) + Lemma 2.8 `lemma:compatibility-bis` (2472–2500) | `⟨⟨a,b⟩⟩_r = Σ_{σ∈G_r}⟨a^σ,b⟩⟨d⟩`, `*`-hermitian, Galois-invariant; `p_{r+1,r}⟨⟨κ_{r+1},γ_{r+1}⟩⟩ = ⟨⟨κ_r,γ_r⟩⟩` with NO constant | 03 Cor, 05 | the group-ring transition (prompt's mandate) |
| KLZ17 Def 2.4.1–2.4.4 (KLZ17.tex 541–592) | `pr_1, pr_2`, `T'_ℓ/U'_ℓ = pr_*Φ^*hpr^*`, `T_ℓ` = transposes, "T_ℓ match q-expansions" | 01 §4, 02 §1 | conventions |
| KLZ17 Lemma 2.4.4 (`lemma:isogeny`) | `⟨φP,φQ⟩_{E'} = ⟨P,Q⟩_E^{deg φ}` | 03 Lemma W | Weil pairing |
| KLZ17 Prop 2.4.5 (`prop:pridentity1`) | `(pr_2)_*U'_p = p^{k+1}(pr_1)_*` | 02 §2(b), 08 check (ii) | reproduced by the framework |
| KLZ17 Def 2.5.2, relations, Rem 2.5.3, Def 2.5.4 (609–660) | `W_Q` matrix class, `W_Q^2`, conjugation by diamonds, `W_{QQ'}`; moduli `W_Q(E,P_{N/Q},P_Q) = (E/⟨P_Q⟩, ·, P'_Q)` with `⟨P_Q,P'_Q⟩ = ζ_Q` | 01 §5, 03 Lemma W | definition of `W` |
| KLZ17 §10.1 proof (3031–3038) | `W_{Np}∘pr_1^* = pr_2^*∘W_N`, `W_{Np}∘pr_2^* = p^k pr_1^*∘W_N` | 03 (corroboration of Lemma W, tame step, weight k+2) | corroboration |
| Hida LMWM (6.6) (Hida_LMWM.txt 2361) | `π^r_s∘π^*_{r,s} = p^{s−r}U(p^{s−r})` | 02 §0, 04 §2 | shows where `p`-powers live |
| BSV22 (68) (BSV22 txt 2305) | `w_{Np}U_p = U'_p w_{Np}` (no tame diamond), `w_pU_p = U'_p w_p ⟨p⟩_N` | 04 §2, 08 (vi-c) | corroboration |
| Ohta 1999 (4.2.4) (txt 3116) | `w_r^σ = w_r∘T(a;a) = T^*(a;a)∘w_r` | 01 §5, 05 §3 | Galois law of `W` |
| Silverman AEC III.8.1(e), III.8.2 | `e_{mm'}(x,y) = e_m(m'x,y)`; `e(φx,y) = e(x,φ̂y)` | 03 Lemma W | standard, not in packet |

## Consulted, not load-bearing

| ref | note |
|---|---|
| KLZ17 Prop 7.2.1, Thm 7.2.3(v) (2223–2300) | Λ-adic control and perfect `Λ_D`-pairing (proof = Ohta II Cor 1.3.8, 2.3.6). Used for NOTHING in the proof (mandatory check 5); 03 Corollary is its finite-level content, derived independently. |
| KLZ17 §7.4 Rem/Lemma 7.4.2 (2373–2395), Cor 10.3.4 | forms-side `U_p^r∘W_{Np^r}^{-1}`; Ohta's `τ_r = W^{-1}` up to sign. Weight-2 sign is fixed by `W^2 = id`. |
| BCPV Rem 4.5(ii) (4.8)–(4.9) (1330–1348) | the `1/p` transition. PROHIBITED by the prompt; not used. (Lane 2/4: should be `1/p^3`; consistent with 02 §4.) |
| BCPV Lemma 5.? `lemma_second_reduction`, (6.?) `eqn_2024_02_08_1848` (1542–1580, 1717–1730) | specialized pairing `a_p(g)^r λ_{N_gp^r}(g)^{-1}⟨,⟩_r`; "compatibility of the Poincaré duality pairing with degeneracy maps" is invoked in words. |
| Ohta 1999 (1.5.4), (3.3.4), (4.3.10), (5.1.5) | Hecke-algebra isomorphism via `τ_r`; trace/Poincaré compatibility; Galois action on `Z_p[C_r]`. |
| BSV22 Prop 3.2–Rem 3.3, (109), (114) | fixed level `Np`, integer weights (Lane 3's scope correction confirmed: no p-power level statement). |
| Cais 1209.0046 | not opened (Lane 3's Prop 2.3.6 reference recorded only). |

## Not available (mandatory check 6)

* **Ohta 2000, Math. Ann. 318 ("Ohta II"), Cor 1.3.8, 2.3.6**: not on disk, not consulted. Not needed for MPC or
  for 03 Corollary. The ONLY place where it would have been used is as an *alternative printed source* for the
  finite-level group-ring pairing compatibility, which is now derived. So there is no finite-control step left
  unverified in this lane's claims. (What Ohta II would additionally give — perfectness of the Λ-adic pairing on the
  parabolic ordinary part — is not a claim of this lane.)
* Nekovář 2000 / Jannsen 1990 (functoriality of the étale Abel–Jacobi map under correspondences): standard, not in
  packet; cited in 05 with the exact statement needed.
* H9R16-A/B text (definition of the packaged point `P_r^{tr,†}`): not in the packet, by design. 05 defines the point
  from BCPV's objects and flags the identification for the referee.
