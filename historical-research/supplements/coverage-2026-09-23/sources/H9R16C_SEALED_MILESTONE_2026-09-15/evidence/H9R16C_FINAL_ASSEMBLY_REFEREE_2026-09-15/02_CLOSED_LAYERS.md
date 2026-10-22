# 02 — Closed layers, frozen definitions, recorded pressure points, source anchors

Every statement below is copied from the named file. Where a statement is an INPUT (§A), the charter forbids
re-proving it; where it is a CLOSED TYPING RESULT (§B), it was proved by an earlier lane and should be used, not
re-derived (re-deriving a weaker form wastes the run and invites false scope claims).

## §A. Inputs (charter: do not revisit)

**A1 = L5-T3 (MPC_r, d_r = 1).** Lane 5 `03` Theorem; `00` l.6–14. For any tame level M with p ∤ M, r ≥ 1, KLZ17
moduli W with compatible roots ζ_{Mp^{s+1}}^p = ζ_{Mp^s}, A_s := W_{Mp^s}^{-1}(U'_p)^s, on all of H^1(X_1(Mp^{r+1}))
(Betti / étale any twist / de Rham), integrally, no ordinarity used:

    ϖ_1^* ∘ A_r ∘ ϖ_{1,*}  =  A_{r+1} ∘ N_{r+1,r};     ⟨ϖ_{1,*}y, A_r ϖ_{1,*}z⟩_r = ⟨y, A_{r+1} N_{r+1,r} z⟩_{r+1}.

Conventions (Lane 5 `01`): ϖ_1(A,P) = (A,pP) (τ↦τ); ϖ_2(A,P) = (A/⟨Np^sP⟩, P mod) (τ↦pτ); U'_p = π_{1*}π_2^* =
DR22 U_p^* = KLZ17 U'_p, the Poincaré adjoint of classical U_p; W_s^2 = id in weight 2, so W^{-1} = W, W^* = W_*.
With an incompatible ζ-system d_r becomes a central Q-rational diamond ⟨c⟩^{±1} (Lane 5 `03` obstruction list).

**A2 = L5-T2 (norm element).** Lane 5 `02` §3, two proofs. On H^1(X_{r+1}), as correspondences:

    ϖ_2^* ∘ ϖ_{1,*} = U'_p ∘ N_{r+1,r} = N_{r+1,r} ∘ U'_p,     N_{r+1,r} := Σ_{d ∈ K_r} ⟨d⟩,  K_r = {d ≡ 1 mod Mp^r} (order p).

N is central, inversion-invariant, N^2 = pN, and its image under Z_p[(Z/Mp^{r+1})^×] → Z_p[(Z/Mp^r)^×] is p·1.
p-powers live only in push-then-pull composites: ϖ_{2,*}ϖ_1^* = p·U_p, ϖ_{1,*}ϖ_2^* = p·U'_p, ϖ_{2,*}U'_p = p·ϖ_{1,*}.
Also ϖ_{1,*}U'_p = U'_pϖ_{1,*} (cycle identity; DR22 §1.3), while ϖ_1^*U'_p ≠ U'_pϖ_1^*.

**A3 = L5-T1 (Lemma W).** Lane 5 `03`. ϖ_1∘W_{s+1} = W_s∘ϖ_2 and ϖ_2∘W_{s+1} = W_s∘ϖ_1 exactly (compatible ζ, no
diamond). On H^1: ϖ_1^*W_r = W_{r+1}ϖ_2^*, ϖ_2^*W_r = W_{r+1}ϖ_1^*, W_rϖ_{1,*} = ϖ_{2,*}W_{r+1}, W_rϖ_{2,*} = ϖ_{1,*}W_{r+1}.

**A4 = L5-T4 (group-ring form, constant 1).** Lane 5 `03` Corollary. Δ_s := (Z/Mp^s)^×, π: Z_p[Δ_{r+1}] → Z_p[Δ_r],
⟨⟨x,y⟩⟩_s := Σ_{σ∈Δ_s} ⟨x, A_s⟨σ⟩y⟩_s [σ^{-1}]. Then π(⟨⟨x,y⟩⟩_{r+1}) = ⟨⟨ϖ_{1,*}x, ϖ_{1,*}y⟩⟩_r.

**A5 = L5-T5 (tame transport; the tool for item 3).** Lane 5 `04` §3. t := N/N_g; pr^t_1(A,P) = (A,tP) (forgetful);
pr^t_2(A,P) = (A/⟨N_gp^sP⟩, P mod). With ζ_{Np^s}^t = ζ_{N_gp^s}:

    pr^t_1 ∘ W_{Np^s} = W_{N_gp^s} ∘ pr^t_2,     pr^t_2 ∘ W_{Np^s} = W_{N_gp^s} ∘ pr^t_1     (no scalar, no diamond),

hence pr^t_{1,*} W_{Np^s} = W_{N_gp^s} pr^t_{2,*} on H^1. Proof = Lemma W's proof with p → t. **Not exercised by
`_verify/msym_check.py`** (that checker has no tame-level case); checking it numerically is in scope.

**A6 = L5-D4 scalar (charter: SCALAR_D4 = PROVED_FORMAL).** Lane 5 `05` §3. With (AJ-corr) (étale Abel–Jacobi
functoriality under algebraic correspondences; Jannsen LNM 1400 §9 / Nekovář 2000 §1; numbered statement unpinned = R1):
for every d ∈ G̃_r and every Hecke pair (t_2, t_3),

    Kum( Π_{Γ,*} Δ_r^ord[d] ) = Contr^{Γ}_*( K ∘ cl_1(Δ_r^ord[d]) )   in H^1(F'_r, S(1)),   Γ = Γ_{t_2}^t ∘ Γ_A ∘ Γ_{t_3},

Π_Γ := X_{14} × Γ, Contr^Γ(y_1⊗y_2⊗y_3) = ⟨y_2, [Γ]_* y_3⟩·y_1, K = Künneth projection, F'_r = Q(μ_{Np^r}).
**Orientation caveat (Lane 5 `07` item 5):** the wrong orientation of Γ_A replaces ⟨y_2, A y_3⟩ by ⟨y_2, A^t y_3⟩,
A^t = (U_p)^r W; this must be matched against H9R16-A/B's Φ^mod (§C).

## §B. Closed typing results from earlier lanes (use; do not re-derive)

**B1 (Lane 2 `_parts/03_1`, Lemma F, Lemma T, extensions 1–4, Consequence C-F).** For abelian varieties over a number
field and φ ∈ Hom_F(A,B)⊗Z_p: Kum_B∘φ = H^1(F,T_pφ)∘Kum_A; Kum injective on Â(F); res_{L/F} injective on H^1(F,T_pA);
Tate faithfulness; the same with idempotent cuts, carrier coefficients x ∈ Hom_{Z_p}(B, Â(F)) (Kum(x)(b) := Kum(x(b)),
natural in pre-composition by any Z_p-linear β: B' → B), MRS twists, and change of group ring.

**B2 (twisted descent of the contracted point; two equivalent forms).** Both use W^σ = ⟨z⟩∘W, which BCPV's printed
σ_mΔ^ord[e] = Δ^ord[m^{-1}e] forces (Lane 2 `_parts/03_2` §03.2.1), and H9R16-A/B balance.
- Lane 2 (G2), `_parts/03_2` §03.2.2: for σ ∈ G_{K_0}, σ(ζ_{N_gp^r}) = ζ^z, z = (z_p, z_N):
  σΦ_r^mod(t_2 ⊗ t_3) = ⟨c_r(σ)^{1/2}⟩_{(1)} Φ_r^mod(t_2 ⊗ ⟨z_N(σ)⟩^{-1} t_3). p-part of the dagger lands on factor 1;
  the carrier is twisted by ⟨ε_N⟩^{-1} on factor 3 (ε_g^{-1} on g-isotypic parts = the g^c twist of BCPV (1.7)).
- Lane 4 L4-T3, `03` §2: σ∘Φ̄^mod_r = ⟨m_σ⟩^{1/2}_{(1)} ⟨n_σ⟩_{(1)} ∘ Φ̄^mod_r ∘ R(⟨n_σ⟩); p-part auxiliary twists cancel
  exactly (⟨m⟩^{1/2}·⟨m⟩^{1/2}·⟨m⟩^{-1} = 1), the tame part survives.
- Reconciliation (Lane 2 `05` §"Cross-lane"): the tame diagonal diamond fixes Δ_r^ord, so Φ = ⟨n⟩_{(1)}∘Φ∘(1⊗⟨n⟩^2)
  and the two formulas agree.
- Level caveat carried by both: W_{N_gp^r} on factor 3 of a cycle at common level N needs either N_gp^r ∥ Np^r or a
  prior push-down to native level; only the tame factor depends on this.

**B3 (type A vs type B).** Lane 2 `_parts/03_3` §03.3.2–03.3.3; Lane 4 `03` §1, L4-T1, L4-T2.
- Type B: A_r^† = O_r(c^{1/2}) ⊗_{O_r} V_r, O_r = Z[G_r] by Q-rational diamonds; T_p = T_pV_r ⊗_{Z_p[G_r]} Z_p[G_r]^† (BCPV's module).
- Type A: Z[G_r](c^{1/2}) ⊗_Z V_r; T_p has Z_p-rank |G_r| = p^{3(r−1)} times larger. μ_r: g⊗v ↦ ⟨g⟩v is K_0-rational, surjective.
- On G_r-invariants of type A (norm image {Σ_g g⊗g^{-1}m} ≅ M), the frozen s_r⊗ϖ_* equals p^3·ϖ_* in M-coordinates,
  because ker(G_{r+1}→G_r) ≅ (Z/p)^3 acts trivially after ϖ_*; DR22 Lemma 2.8 has no constant.
- Type B has no corestriction: σ(ϖ_{1,*}x) = c_r(σ)^{1/2}ϖ_{1,*}x (pr_r∘c_{r+1}^{1/2} = c_r^{1/2}).
- After contraction the dagger group is the factor-1 cyclic quotient (order p^{r−1}), not G_r (Lane 4 `03` §1).
- MRS lattice sign: character c_r^{+1/2} realizes BCPV's ⟨χ⟩^{-1/2} (MRS Lemma 1.3 inverse convention; Lane 2 §03.3.1).
- Albanese μ-model diamonds flip ⟨χ⟩^{-1/2} to ⟨χ⟩^{+1/2}; use point-model diamonds (Lane 1 `04` R3).

**B4 (BCPV (4.9) constant).** Lane 4 L4-T4; Lane 2 §03.3.3; successor audit rerun. Printed 1/p; commutativity of (4.8)
forces p^{-3}. Recorded, not used (charter).

**B5 (Lane 4 `04` §1–§3: the retyped receptacle and relation).** n_σ := χ_cyc(σ) mod N, m_σ := ⟨χ_cyc(σ)⟩ ∈ 1+pZ_p.
    M_r := Hom_{Z_p}(B^bal_r, Ĵ^{(1)}_r(F'_r)^{ord}),   (σ⋆Φ)(b) := ⟨m_σ⟩^{-1/2}_{(1)} ⟨n_σ⟩^{-1}_{(1)} · σ( Φ( R(⟨n_σ⟩)^{-1} b ) ),
    P^♮_r := M_r^{Gal(F'_r/K_0), ⋆},   T^♮_r := Hom_{Z_p}(B^bal_r, T_pJ^{(1),ord}_r) with the same ⋆,
    Kum^♮_r : P^♮_r → H^1(K_0, T^♮_r)  (injective, L3);  L1: ⋆-compatible K_0-homomorphisms map P^♮_{r+1} → P^♮_r.
    (T♮_r)  ϖ^{(1)}_{1,*} ∘ (U'_p)^{-(r+1)} ∘ Φ̄^mod_{r+1} = δ♮_r · (U'_p)^{-r} ∘ Φ̄^mod_r ∘ res^bal_{r+1,r}
            in Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord});   Lane 5 `05` §4 claims δ♮_r = 1 with N_{r+1,r} on the carrier.
The operator's 𝒫_r^♮ (charter §1) is this P^♮_r.

**B6 (Lane 2 `_parts/03_4`: the square and the typed relation).**
- τ_r^MW : P_{r+1}^{tr,†} → Hom_{Z_p}(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0), x ↦ ϖ_{1,*}∘x; (SQ) Kum∘τ_r^MW = τ_r^et∘Kum, formal.
- No arrow P_{r+1} → P_r exists (Hom contravariant in the carrier; B_{r+1} ↠ B_r); π_r^*: P_r ↪ Hom(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0).
- Q_r := (U'_p)^{-r}_{(1)} ∘ Φ_r^mod ∘ (U'_p)^{-2r}_{carrier}  (Lane 2 `01` T3).
- (E_ν) derivation from MPC_r(ν) + BCPV Cor 4.11(i), then Kum(τ(Q_{r+1})∘(1⊗ν) − π^*Q_r) = 0 ⇒ τ_r^MW(Q_{r+1})∘(1⊗ν_{r+1}) = π_r^*Q_r.
- Inputs that lane did not prove: (K_r) finite modified point/Kummer realization (= D4, now A6);
  H_π: ring maps π_r : e'𝕋'_{r+1}⊗Z_p → e'𝕋'_r⊗Z_p with ϖ_{1,*}t = π_r(t)ϖ_{1,*} ("standard Hida theory; not re-proved").

**B7 (Lane 1).** W^BCPV_{Np^r} = ⟨c_r⟩^{-1}α_r^{-1}w_rα_r; α_r^{-1}π^{r+1}_rα_{r+1} = ⟨u_r⟩^{-1}ϖ_{1,*}; under α: U'_p ↔ U(p),
e'_ord ↔ e. Not needed on BCPV's point model. H9R12's U'_p ↔ U^*(p) is the ι-dictionary (Galois-twisted): TYPE_MISMATCH.

**B8 (Lane 3).** KLZ17 Thm 7.2.3(v) is Λ-adic only (not a finite-level statement). E′(a) (target twist of the
contracted class), E′(b) (level step) and D4 are NOT_PRINTED. BSV22 (109) is fixed level Np. BCPV never define W.

## §C. Frozen H9R16-A/B definitions (the objects items 1–3 must match)

Operator text, `~/.claude/paste-cache/a81606aed099d4e9.txt` l.161–215 (H9R16-A/B block) and l.229–300 (H9R16-C block):
- A_r = W_{N_gp^r}^{-1}(U'_p)^r (native level N_g).
- Raw Rosati/transpose ρ_r : (T'_r)^op → T_r with T'_ℓ ↦ T_ℓ (ℓ ∤ Np), U'_p ↦ U_p, ⟨d⟩ ↦ ⟨d⟩^{-1}, e'_ord ↦ e_ord;
  plain balance Φ_r^P(t_2u', t_3) = Φ_r^P(t_2, ρ_r(u')t_3); ρ_r(u')A_r = A_r u'; ι_r(u') := A_r^{-1}ρ_r(u')A_r = u'.
- **Φ_r^mod(t_2,t_3) := Π_{Z,*}((1 ⊗ t_2 ⊗ A_r t_3) Δ_r^ord)**, "with action order interpreted in BCPV's correspondence
  convention"; balance Φ_r^mod(t_2u', t_3) = Φ_r^mod(t_2, u't_3). Π_Z := X_{14} × Z, Z = X_{23} the plain diagonal.
- Carrier: Z_p-module quotient by (t_2u')⊗t_3 − t_2⊗u't_3 after A_r transport. "g^c is the dual/nebentype-twisted
  third factor. Do not identify the two raw geometric Hecke actions naively."
- The checkpoint NEVER defines P_r^{tr,†} or T_r^{tr,†} (Lane 4 `01` §7). The tame push-down inside Φ^mod is not
  stated in the frozen formula (Lane 4 `01` §6 reads it "factorwise as in BCPV Def 4.13").
- Lane 5's version (`05` §2): P_r[d] := Π_{A,*}Δ_r^ord[d], Π_A := X_{14} × Γ_A;
  P_r[[a,b,c]] := Σ_{g∈G_r} P_r[g·(a,b,c)] ⊗ g ∈ J(F') ⊗ Z_p[G_r];  Φ^mod_r(t_2⊗t_3) := Π_{(t_2⊗At_3),*}Δ with Γ = Γ_{t_2}^t∘Γ_A∘Γ_{t_3}.
- Same text, second local copy: `~/BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15/_work/RECOVERED_H5_H9_CHECKPOINT_FULL_TEXT.txt`
  l.1124–1290. That file is a drift-evidence extract (the successor audit forbids using it as a repair source).
- **Authoritative copy: the operator's Google Drive checkpoint (current through H9R16-C).** If a verdict turns on a
  wording difference between these local copies and the Drive checkpoint, say so explicitly.

## §D. Recorded pressure points (facts from the lane files, listed so they are traced, not conclusions)

- P1 Packaging identification. BCPV identify packaged and unpackaged classes by `G`: ψ = Σψ_g g ↦ ψ_e, with inverse
  `G^{-1}`: φ ↦ Σ_g φ(g^{-1}•)g (BCPV.tex l.1331–1332; Remark l.1334–1336). Lane 2's μ_r and Lane 4's invariant
  computation (B3) show that a multiplication-type identification produces p^3 per level.
- P2 The post-contraction dagger group is factor 1 only (B3); BCPV's Z_p[G_r]^† uses the DIAGONAL map (l.1362–1366).
- P3 A_r is defined only over Q(μ_{N_gp^r}); Contr^{A_r} is ⋆-equivariant, not plainly G_{K_0}-equivariant (B2, B5).
- P4 Levels. Δ^ord uses W_{Np^r} at common level (l.1247). A_r uses W_{N_gp^r} at native level. BCPV's push-downs to
  native level are the forgetful ϖ_{1,*} on each factor (Def `definition_big_diagonal_Hida_families`, l.1448–1459;
  `pr_h` in (4.16), l.1480–1487). L5-T5 converts forgetful-after-W_{Np^r} into W_{N_gp^r}-after-quotient.
- P5 Orientation of Γ_A / transpose (A6 caveat) versus ρ_r in §C.
- P6 Carrier maps: H_π (B6); the balance relation must be preserved by 1⊗N_{r+1,r} (N central) and by π_r.
- P7 Normalizations. Q_r uses (U'_p)^{-r} on factor 1 and (U'_p)^{-2r} on the carrier (B6). BCPV use
  (U'^{⊗3}_p)^{-r} (l.1438), a_p(f)^{-r}a_p(g)^{-2r} (Lemma l.1490), and the specialized trace pairing
  a_p(g)^r λ_{N_gp^r}^{-1}⟨,⟩_r (l.1561) with a_p(f)^{-r}a_p(g)^{-r}λ^{-1} (l.1567). These matter for stating G_BIG_KUMMER_TRACE.
- P8 N_{r+1,r} is an element of the finite group ring, not a scalar. Any inverse-limit module must say how it is
  absorbed (compare A4, where the group-ring form has constant 1).

## §E. Source anchors (local)

**BCPV TeX** `~/H9R16C_LANE5_MPC_PROVER_2026-09-15/sources/tex/BCPV.tex` (arXiv 2409.08645v1). Cite by label and line:

| item | label | line |
|---|---|---|
| (1.6) modified pairing | `eqn_2023_09_29_1444` | 514 |
| (1.8), (1.9) | `eqn_2023_11_06_1518`, `_1525` | 539, 544 |
| §4.2 big diagonal cycles; ϖ_1 | — | 1195 |
| (4.1) diamonds on Δ_r[d] | `eqn_2023_11_01_1241` | 1218 |
| (4.2), (4.3) Galois on Δ_r | `eqn_2023_11_01_1242`, `_12417` | 1222, 1227 |
| (4.4) Δ^ord := (e'W_{Np^r})^{⊗3}Δ | `eqn_2023_11_08_1351` | 1247 |
| Lemma: σ_mΔ^ord[d] = Δ^ord[m^{-1}d] | `DR_Lemma_2_5`, `eqn_2023_11_11_1700` | 1253, 1257 |
| Δ^ét[d] := cl_1(Δ^ord[d]); Künneth K | `eqn_2023_11_08_1512` | 1307 |
| (4.7) packaged class Δ^ét[[a,b,c]] | `eqn_2023_11_10_1126` | 1317 |
| G, G^{-1} formulas | — | 1331–1332 |
| Remark (i) chain; (ii) diagram (4.8) | `remark_2023_11_13_1509`, `eqn_2023_11_13_1224` | 1334, 1342 |
| (4.9) PROHIBITED | `defn_3rd_vertical_map` | 1351 |
| Def: Z_p[G_r]^†, M^† (diagonal) | `defn_Gal_twisted_general` | 1362 |
| Lemma: descent of Δ^ét[[a,b,c]] to Q(μ_p) | `lemma_Gal_action_on_bold_Delta` | 1371 |
| Def: Δ^ét_r := p^3/(p−1)^3 Σ Δ^ét_r[[bc,ac,ab]] | `definition_2023_11_11_1723` | 1397 |
| Lemma: ϖ_{1,*}^{⊗3}Δ^ord_{r+1} = U'^{⊗3}_pΔ^ord_r | `DR_lemma_2_5_dual` | 1412 |
| Cor: same for Δ^ét[a,b,c], Δ^ét[[a,b,c]], Δ^ét_r | `cor_DR_lemma_2_5_dual` | 1422 |
| Def: Δ^ét_∞ := {(U'^{⊗3}_p)^{-r}Δ^ét_r} | `definition_big_Heegner_main` | 1438 |
| Def: Δ^ét(f,g,h), forgetful tame push-downs | `definition_big_diagonal_Hida_families` | 1448 |
| Def: Δ^ét(f⊗ad(g)) | `defn_2023_11_15_1209` | 1463 |
| (4.15), (4.16) specializations; pr_h = forgetful ϖ_{1,*} | `eqn_2023_11_15_1243`, `_1557` | 1474, 1480 |
| Lemma: res Δ^ét(f⊗ad g)|_{(κ,λ)} = a_p(f)^{-r}a_p(g)^{-2r}Δ^ét_r(κ,λ) | `lemma_2023_11_14_1442` | 1490 |
| trace pairing a_p(g)^rλ^{-1}⟨,⟩_r; Δ^tr relation | `eqn_2024_02_08_1848`, `_1858` | 1561, 1567 |
| Prop 6.2; Rem 6.4 (specialized D4 shadow) | `prop_main_comparison_Sec5`, `remark_2023_11_22_0818` | 1765, 1802 |

**DR22 TeX** `…/sources/tex/DR22.tex`: `eqn:def-varpi-12` 1157; `eqn:galois-pushforward` 2104;
`lemma:compat-cycles-proj` 2116; `eqn:pairing-LambdaG` 2275; `lemma:compatibility-bis` (Lemma 2.8) 2473.
**KLZ17 TeX** `…/sources/tex/KLZ17.tex`: `lemma:isogeny` 585; `prop:pridentity1` 595; Atkin–Lehner subsection 609
(Def 2.5.2–2.5.4 follow); `prop:controlthm` 2225; `thm:ordinaryfiltration` 2254.
**MRS** `~/H9R16C_LANE4_HOSTILE_OBSTRUCTION_2026-09-15/sources/MRS_twisting_math0609066.{pdf,txt}` and Lane 2 `sources/mrs.pdf`.
**Castella–Hsieh** Lane 4 `sources/CastellaHsieh_1809.09066.{pdf,txt}`. **Hida** Lane 4 `sources/` (Control; LMWM).
**PDF text layers** for BCPV, DR22, KLZ17, BSV22, Hida, Ohta 1999, Cais: Lane 5 `sources/*.txt`.
**Checker** Lane 5 `_verify/msym_check.py` (Manin symbols for Γ_1(L); every operator from its definition; F_ℓ with
ℓ ∈ {1000003, 999983}); `python3 msym_check.py 5,3,1` reproduces the first case.

## §F. Custody of the §C text copies at charter time

```
a81606aed099d4e9cea5abd72b7d489f3b390e0d479aa74fb47290e95a5117a4  /Users/bsm/.claude/paste-cache/a81606aed099d4e9.txt
a25e24c257da4472e51792a22b47b4efd3ace4edcf39cb1fa36820dd9d5d88e9  /Users/bsm/BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15/_work/RECOVERED_H5_H9_CHECKPOINT_FULL_TEXT.txt
b25d6e4724d74129383ba37426f37983c9044e33c1ac9df3aa48a929647c12e3  /Users/bsm/H9R16C_LANE5_MPC_PROVER_2026-09-15/sources/tex/BCPV.tex
855031bb0954db994a3080bb7484ee0caadac0166d674a98183a824ccdfba1e6  /Users/bsm/H9R16C_LANE5_MPC_PROVER_2026-09-15/sources/tex/DR22.tex
dd2da210365a9cbd0a5948e0777375d6d71befcab1b8e2931f3ae5745ed0a815  /Users/bsm/H9R16C_LANE5_MPC_PROVER_2026-09-15/sources/tex/KLZ17.tex
f99115c142844abb116402f9d9b32e704c67597d17df21074c39930ac374c3e8  /Users/bsm/H9R16C_LANE5_MPC_PROVER_2026-09-15/_verify/msym_check.py
```
