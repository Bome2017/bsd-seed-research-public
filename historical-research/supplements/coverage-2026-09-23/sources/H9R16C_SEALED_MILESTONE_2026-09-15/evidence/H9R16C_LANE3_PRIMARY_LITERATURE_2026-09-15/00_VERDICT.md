# 00 — Verdict. Lane 3: is there an existing theorem implying H9R16-C?

Date: 2026-09-15 · Lane directory: `~/H9R16C_LANE3_PRIMARY_LITERATURE_2026-09-15` · Revision v2
(incorporates the operator's mid-lane input, checked against the local copies).

## Bottom line

1. **EXISTING_THEOREM_CLOSES_C = NO.** No consulted primary source states H9R16-C. None proves a
   theorem whose hypotheses cover a fixed-base dagger/MRS point/Kummer transition square for
   contracted Chow–Heegner points.

2. **The square itself is formal** once τ_r^et is the Tate-module map of a K_0-rational point
   transition. This uses Kummer naturality, MRS twists and Weil restriction/Shapiro (03 §2, F1–F4) —
   standard facts, but not printed in the consulted sources. Such a transition exists in BCPV's point
   model: τ_r^MW := s_r ⊗ Alb(ϖ_1), U'_p-normalized on p-completed ordinary parts.

3. **The étale pairing step is settled by reference.** Compatibility of the modified pairing
   ⟨x, W_{Np^r}^{-1}(U'_p)^r y⟩ along the tower is **PRINTED BY REFERENCE** in KLZ17's convention:
   Thm 7.2.3(v), the proof of Prop 10.1.1, Rem 7.4.1 and Lemma 7.4.2, via Ohta 2000 (not consulted).
   The operator supplied this mid-lane; lane 3 checked it in KLZ17 v6 and BSV22.
   **Scope correction:** BSV22 (109) is integer-weight specialization at the fixed level
   Γ_1(N)∩Γ_0(p). It does not reach p-power levels.

4. **What no consulted source prints** (04 v2):
   - **E′** — the dagger / group-ring packaging of the A_r-modified contraction: its target twist
     E′(a), and its level step with an explicit central unit E′(b);
   - **D4** — the unspecialized finite-level Abel–Jacobi identity
     Kum(P_r^{tr,†}) = Contr^mod_r(packaged cl_1 Δ_r^ord);
   - normalization transport N1–N4 (BCPV never define W).

   E′ and D4 both look formal from printed ingredients, but neither is printed.

5. **Nearest theorems, ranked.**
   1. Howard 2007 §2.2 (Lemma 2.2.4, twisted Kummer map, fixed-base corestricted twisted points):
      the same architecture, but its point-level transition comes from CM moduli.
   2. Hida, HidaC §5–6 / HidaL §5–6: Q-rational, Hecke-equivariant (w-twisted) Jacobian towers over a
      fixed k, with Kummer diagrams.
   3. MRS Thm 1.4, 2.2(iii), Cor 1.7(ii), Prop 4.1, Rem 5.11: the receptacle.
   4. BCPV Lemma 4.10, Cor 4.11, Def 4.12 and DR22 Lemma 2.4, 2.6, 2.8: Chow and étale transitions.
   5. KLZ17 Thm 7.2.3(v) and Prop 10.1.1, and Cais Prop 5.2.4: the twisted pairing across levels.

6. **No FALSE statement and no genuinely incompatible normalization was found.** Hazards recorded
   (01 §9 and §12, 03 §4):
   - **T9:** Hida's w-twisted π^{sr} vs BCPV's untwisted ϖ_{1,*}/U'_p tower — a TYPE_MISMATCH unless
     the levelwise w_s Galois twist is inserted;
   - **T2:** s_r is not a corestriction;
   - **T6:** old-form subvariety towers have zero integral pro-limit (HidaC Prop 6.4);
   - **T7:** BCPV use two different tame levels;
   - **T1/T8:** two moduli models, and five printed W conventions.

   Citation defects in BCPV:
   - Lemma 4.10 cites DR22 "Lemma 2.5", which is Lemma 2.4 in arXiv v1;
   - (1.8)–(1.9) cite Ohta (1.5.4), which is an identity about modular forms only;
   - the BSV22 passage cited in §1.1.9 and fn. 7 contains no Atkin–Lehner operator in the version
     consulted.

## Classification summary (the lane prompt's vocabulary)

- **NOT_PRINTED:** F1–F3; E′; D4; BCPV's definition of W, its Galois twist, and its degeneracy
  interchange; any point-valued Chow–Heegner tower.
- **FALSE as citation:** Hida's Mordell–Weil control theorems applied to the MRS/cyclotomic tower;
  BSV22 (109) read as a p-power-level statement; "MRS prints a Kummer or Shapiro statement".
- **TYPE_MISMATCH (hazards):** T9; E′(a) remains unchecked.
- **NEW_THEOREM_REQUIRED:** none identified at lane-3 level. E is printed by reference; E′ and D4 are
  expected to be formal.

## Files

| File | Contents |
|---|---|
| 01_TYPES_AND_OBJECTS.md | objects per source; placement of the square's objects; hazards T1–T9 |
| 02_PRIMARY_SOURCE_LEDGER.md | search-target matrix; per-source item ledger with hypothesis match |
| 03_DERIVATION_OR_OBSTRUCTION.md | nearest theorems; formal lemmas F1–F4; delta D1–D5; hazards; verification of the operator input (§6) |
| 04_EXACT_REMAINING_STATEMENT.md | v2: E settled by reference; E′ and D4 with types; normalization transport N1–N5 |
| 05_NEXT_HANDOFF.md | handoff to the coordinator and lanes 1, 2, 4; unconsulted sources |
| 06_FILES_CONSULTED.sha256 | SHA-256 of every source PDF and local file read |

LANE = 3 — primary-literature search for an existing theorem implying H9R16-C
STATUS = EXISTING_THEOREM_CLOSES_C = NO; NEAREST_THEOREMS_IDENTIFIED; ETALE_PAIRING_TOWER_COMPATIBILITY = PRINTED_BY_REFERENCE (KLZ17 Thm 7.2.3(v) + Prop 10.1.1 proof + Rem 7.4.1, via Oht00; operator-supplied, lane-3-verified); C_SQUARE = FORMAL_FOR_T_p(τ^MW) (03 F1–F4); DELTA = E′ + D4 (unprinted, expected formal) + normalization transport N1–N4
PROVED = source-verified: KLZ17 Thm 7.2.3(v) (perfect Λ_D-pairing on H^1_ord,par(Np^∞) before specialization); KLZ17 Rem 7.4.1, Lemma 7.4.2 and Prop 10.1.1 proof (W_{Np^r}^{-1}(U'_p)^r on cohomology, U_p^r W_{Np^r}^{-1} on forms, τ_r = W^{-1} up to sign); BSV22 (103), (104), (109), (114) at fixed level Np; BCPV L4.10 and Cor 4.11 (Chow and étale transitions); DR22 L2.4, L2.8; HidaC §6 (Q-rational Hecke-equivariant π^{sr}, w_r^σ = ⟨z⟩w_r) and Lemma 2.1 (Kummer injection); MRS Thm 1.4, 2.2(iii), Cor 1.7(ii), Prop 4.1, Rem 5.11. Lane-3 formal (not printed): F1–F4 — Kummer naturality for K_0-morphisms of finite-level MRS twists and Shapiro/norm compatibility, so the square commutes for τ_r^et := T_p(τ_r^MW)
REFUTED = as claims or citations: "BCPV define W or print its Galois twist / degeneracy interchange" (NOT_PRINTED); "[Oht99] (1.5.4) is an étale/Jacobian/Galois statement" (forms only; the Galois formula is Ohta (4.2.4)); "[DR22] Lemma 2.5 is the distribution relation" (it is Lemma 2.4 in arXiv v1); "BCPV's cited BSV22 passage contains W" (not in the consulted version); "Hida's Mordell–Weil control theorems apply to the MRS/cyclotomic point tower" (their hypotheses fix k); "BSV22 (109) gives p-power-level compatibility" (fixed level Np, integer weights); "MRS prints a Kummer or Shapiro statement" (none)
FIRST_EXACT_UNPROVED_STATEMENT = E′ + D4 (04 v2). At unspecialized finite level r, the A_r-modified contraction of the Z_p[G_r]^†-packaged class Δ^ét_r on factors 2,3 (KLZ17/Ohta pairing with ∗-hermitian group-ring values as in DR22 (2.17), g⊗g^c trace, balanced Hecke-orbit carrier) (a) lands in H^1(K_0, T_r^{tr,†}) with exactly the factor-1 dagger induced from ⟨χ⟩_r^{-1/2}, and (b) satisfies (ϖ_{1,*}⊗p^{(1)}_{r+1,r}) ∘ Contr^mod_{r+1} = u_r · Contr^mod_r ∘ (ϖ_{1,*}^{⊗3}⊗p_{r+1,r}) on U'_p-normalized classes for an explicit central unit u_r; and (D4) Kum(P_r^{tr,†}) = Contr^mod_r(packaged cl_1 Δ_r^ord). Not printed in any consulted source
TYPE_CHECK = PASS_AT_FINITE_LEVEL_WITH_HAZARDS — receptacle, Kummer map, Tate module and lattice maps are well-typed (MRS finite Galois image, O = Z, Hida p-completion); hazards T1 model mismatch, T2 s_r ≠ corestriction, T3 no Λ-adic MRS twist, T4 U'_p^{-1} only on completions, T5 Hida control fixes k, T6 subvariety pro-limit 0, T7 two tame levels, T8 five W conventions, T9 w-twisted vs untwisted transition; E′(a) target twist unchecked
NEW_ASSUMPTIONS = NONE
COUNTEREXAMPLE_OR_OBSTRUCTION = NONE_FOUND; hazards only: T9 is a TYPE_MISMATCH if Hida's π^{sr} (or any w-conjugated transition) is paired with BCPV's τ^et without the levelwise w_s Galois twist; E′(a) would be a TYPE_MISMATCH if the pairing's Z_p[Δ_{N_g p^r}] twist and the G_r-dagger do not combine to T_r^{tr,†} (unchecked)
NEXT_SMALLEST_TEST = r = 1→2 with N_g fixed: compute the Galois action on Contr^mod_r(Δ^ét_r[[a,b,c]]) from BCPV (4.1), (4.3), (4.5), Def 4.6 and the pairing's hermitian/Galois rules (DR22 (2.17); BCPV (1.6) Z_p[Δ]-values; KLZ17 Prop 7.2.1(1) inverse diamonds), and compare it with T_r^{tr,†} (E′(a)); then check the p_{2,1} level step (E′(b)) using KLZ17 Thm 7.2.3(v) reduced by Prop 7.2.1(4)
ARISTOTLE_READY = NO
STOP_ROUTE = NO
