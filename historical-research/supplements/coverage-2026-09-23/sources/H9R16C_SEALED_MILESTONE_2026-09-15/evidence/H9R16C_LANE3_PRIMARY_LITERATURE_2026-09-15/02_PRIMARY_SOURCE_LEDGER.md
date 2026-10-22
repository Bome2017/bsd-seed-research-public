# 02 — Primary source ledger (Lane 3)

Classification vocabulary, per the lane prompt: **PRINTED** · **NOT_PRINTED** · **FALSE** ·
**TYPE_MISMATCH** · **NEW_THEOREM_REQUIRED**. `HYP` records whether the source's hypotheses match
the H9R16-C setting: YES / PARTIAL / NO.

Statements below are paraphrased in my own words, with formulas. The PDFs are in
`_work/sources/` (hashes in 06), and line references are to the pdftotext `.txt` files beside
them. Numbering was checked **only** in the versions listed.

---

## A. Search-target matrix (the eight items the lane prompt names)

| # | Target | Exact printed items | HYP vs H9R16-C | Class |
|---|---|---|---|---|
| 1 | w-twisted degeneracy maps | **HidaC §6** (p.15–16): w_r over Q[μ_{Np^r}]; w_r^σ = ⟨z⟩w_r = w_r⟨z^{-1}⟩; π^{sr} := w_r π_{s,r,*} w_s over Q, Hecke-equivariant (T(n) for (n,Np)=1, U(q) for q\|Np). **HidaL §5 end** (p.25–26): the same. **Cais Prop 2.3.6**: ρw_{r+1} = w_rσ, σw_{r+1} = ⟨p⟩_N w_r ρ, w_r^2 = ⟨−p^r⟩_N⟨−N⟩ (local, over Q_p). **BCPV Lemma 4.10 proof** asserts "Atkin–Lehner interchanges ϖ_{1,*}, ϖ_{2,*}" with no formula. | PARTIAL: Hida fixes the base k and uses the μ-model, Cais is local, BCPV prints no formula. | PRINTED (Hida, Cais); NOT_PRINTED (BCPV) |
| 2 | starred / unstarred Hecke algebras | **Ohta (1.5.4)**: τ_r intertwines T(n)↔T*(n) and T(q,q)↔T*(q,q) *on modular forms*. **Ohta (4.2.4)**: w_r^σ = w_r T(a,a) = T*(a,a) w_r on GJ_r. **Cais Prop 2.3.24**: w_r T = T* w_r. **HidaC §5**: i : Ĵ_∞^ord ≅ J̃_∞^{co-ord} with i∘T(n) = T*(n)∘i. **BCPV (1.8)–(1.9)** cite Ohta (1.5.4) for W intertwining U'_p, U_p. | PARTIAL: each source has its own normalization, and BCPV's U'_p ↔ U*(p) dictionary is not printed. | PRINTED per source; cross-source dictionary NOT_PRINTED |
| 3 | Kummer commuting with degeneracy | **HidaC §6**, the display before Lemma 6.2: the Kummer diagram for D̂_s^ord(κ)⊗Z/p^m → H^1(D_s[p^m]^ord) is compatible with π^r_s (quotient towers, fixed k), giving (6.3) and Lemma 6.2. **HidaL §6**, the display before Lemma 6.1: the same for B_s. **How Lemma 2.2.4 proof**: Kum_s(α_* x_{c,s+1}) = α_* Kum_{s+1}(x_{c,s+1}), on the fixed-base twisted H^0. **Ohta (3.3.4)–(3.3.6)**: *geometric* Kummer (over F̄), trace ↔ Hom(f_*,Z_p) and pullback ↔ Hom(f^*,Z_p). | PARTIAL: all used as formal naturality for a morphism over a fixed base; none for an MRS twist or Weil-restricted tower. | PRINTED (as used); MRS/Weil-restriction version NOT_PRINTED |
| 4 | Tate modules of twists | **MRS Thm 2.2(iii)**: T_ℓ(I⊗_O V) ≅ I⊗_O T_ℓ(V), γ acting as γ^{-1}⊗γ, functorial in I and V. **How (9)**: lim(Ta^ord_p(J_s)⊗ζ_s) = Ta^ord with G_Q twisted by Θ^{-1}, mapping to T^†. **Cais Prop 5.4.15**: a p-divisible group over Q_p twisted by ⟨χ⟩⟨a⟩_N. | YES for MRS at finite level (finite Galois image); NO for a Λ-adic dagger (infinite image). | PRINTED |
| 5 | norm / corestriction under Weil restriction | **MRS Prop 4.1**: O[G]⊗_O V ≅ Res^L_k V; (4.1) (Res V)(A) = V(A⊗L). **MRS Rem 5.11 (5.2)**: N_{L/F} factors through R_{L/F,V} : Res^L_k V ↠ Res^F_k V, induced by Z[G] ↠ Z[Gal(F/k)]. **How (7)**: Cor_{H_{cp^s}/H_c} applied to H^0 of twisted points. No consulted source states Kummer ∘ (Weil-restriction norm) = corestriction ∘ Kummer under Shapiro. | PARTIAL: MRS covers varieties and points only; the Galois-direction part of s_r only (see T2 in 01). | Varieties PRINTED; Kummer/Shapiro compatibility NOT_PRINTED in consulted sources |
| 6 | projective ordinary MW towers | **HidaC** Lemma 5.1, Lemma 5.2, Thm 5.3 (fppf control), Lemma 6.2, (6.4), Prop 6.4 (subvariety pro-limit = 0), Thm 9.2 (control with error term), Thm 10.1 (number field, under finite Sel(A_{P_0})^ord). **HidaL** Thm 1.1 = Thm 6.6 (ind-limit, dual), Prop 6.4 = (1.1). | NO for the cyclotomic/MRS tower (fixed k only); YES for J_r over the fixed K_0. | PRINTED (fixed-k standard tower only) |
| 7 | group-ring coefficient change | **DR22 Lemma 2.8**: p_{r+1,r} ∘ κ_{r+1}(σ)(γ_{r+1}) = κ_r(σ)(γ_r) for γ compatible under (ϖ_1^3)_*. **BCPV (4.8)–(4.9), Rem 4.5, Cor 4.11, Def 4.12**. **MRS Cor 1.7(ii)** (lattice maps induce K_0-morphisms). **Cais Prop 5.2.4 proof**: the modified pairing at level r of pushed-forward classes equals a sum over δ ∈ Δ_r/Δ_{r+1} of the level-(r+1) modified pairing with one more U^*. | PARTIAL: étale and de Rham classes only; uncontracted (DR22/BCPV) or de Rham local (Cais). | PRINTED (cohomological); point-level NOT_PRINTED |
| 8 | functoriality after twisting | **MRS Prop 1.6, Cor 1.7, Thm 1.8, Cor 1.9, Thm 2.2** (functorial in I and V). **How §2.2**: the twisted Kummer map is h_{2,s}- and G_Q-equivariant. | YES at finite level. | PRINTED |

---

## B. Per-source ledger

### B1. HidaC — Hida, *Control of Λ-adic Mordell–Weil groups* (JHC70 preprint, dated Feb 22, 2016)
Published as PROMS 188 (2016) 253–294; the published version was **not** consulted.

- **Intro.** X_r is the moduli of (E, μ_{Np^r} ↪ E) with ∞ Q-rational. Ĵ_∞(k) := lim_r Ĵ_r(k) over "Albanese functoriality twisted by the Weil involutions", for a fixed number field k. The main exact sequence (1.1) is Theorem 9.2.
- **Lemma 2.1** (from [H15, L2.2]). For X an extension of an abelian variety over k by a finite étale group of prime-to-p order: lim X̂(k)/p^n ↪ lim H^1(X[p^n]), and 0 → X̂(k) → H^1(T_pX) → T_pH^1(X) → 0. *HYP:* fixed k, finite S — YES for any abelian variety over K_0.
- **(5.1)–(5.2), Lemma 5.1.** π^* : J_r(k) → J_s^r(k) is a U(p)-isomorphism; π_* is a U*(p)-isomorphism. Ordinary ≅ via π^*; co-ordinary ≅ via π_*.
- **Lemma 5.2, Thm 5.3.** Control of fppf sheaves under diamond operators. **Rem 5.4**: part (b) is not an isomorphism on T-points.
- **§6 (p.15–16).** w_r is defined from the fixed coherent generator ζ, over Q[μ_{Np^r}]; T*(n)w_r = w_r T(n) [MFM 4.6]; w_r^σ = ⟨z⟩w_r = w_r⟨z^{-1}⟩ [MW86 p.237, MW84 2.5.6]; π^{sr} := w_r∘π_{s,r,*}∘w_s is defined over Q and Hecke-equivariant; w_r^2 = 1; {J_s, π_{s,r,*}} and {J_s, π^{sr}} are isomorphic projective systems.
- **Lemma 6.1** (Galois continuity). **(6.1)–(6.3)**: w-twisted Cartier duality [H14 §4] and the Kummer diagram give D̂_s^ord ≅ D̂_r^ord. **Lemma 6.2.**
- **(6.4)** π^{sr}∘π^*_{r,s} = p^{s−r}U(p^{s−r}). **Cor 6.3.** **Prop 6.4**: lim_s Ĉ_s(κ)^ord = 0 for subvariety towers over number fields.
- **§7 Lemma 7.1, Cor 7.2, Prop 7.3** (branch/abelian factors under (A); used by H9R12–13, not by C).
- **Lemma 8.1** (8.2); **Lemma 8.2**: lim_s H^1(A_r[p^s]^ord) = H^1(T_pA_r^ord).
- **Thm 9.2; Thm 10.1.** For k a finite extension of Q, a single P_0 ∈ Ω_T with finite Sel_k(A_{P_0})^ord gives, for almost all P ∈ Ω_T ∩ Spec(I), an exact control sequence with finite error. *HYP:* fixed k, principal arithmetic P, good reduction over Z_p[μ_{p^∞}] — NO for a Weil-restricted or cyclotomic tower.
- **§11.** Norm maps relative to k_s/k_r appear only in the local l = p error-term analysis (W_s = Z_p[μ_{p^s}]); Hida flags this as problematic for projective limits.

### B2. HidaL — Hida, *Limit Mordell–Weil groups and their p-adic closure* (author preprint LMWM.pdf)
Published Doc. Math. Extra Vol. Merkurjev (2015) 221–264; the published version was **not** consulted.

- **Intro.** Thm 1.1 = Thm 6.6 (exactness up to finite error of the Z_p-dual control sequence for the **ind**-limit J̌_∞(k)^ord_T); (1.3)–(1.4) U(p^{s−r}) level lowering; Prop 6.4 = (1.1).
- **Lemma 2.3** (0 → Â(κ)⊗Q_p/Z_p → H^1(A[p^∞]) → H^1(Â) → 0). **§5 (A)/(B), Prop 5.1** (P1)–(P3).
- **§5 end (p.25–26).** The same w_r, the same w_r^σ formula, the same Q-rational Hecke-equivariant π^{sr}; A_s^* = w_s(A_s) because T(n)w_s = w_sT*(n) [MFM Thm 4.5.5].
- **§6.** (6.1)–(6.3); w-twisted Cartier duality [H14a §4] (x|T(n), y) = (x, y|T(n)); (6.4)–(6.5) Kummer diagram; **Lemma 6.1**; **Thm 6.6**; **Thm 7.1, Cor 7.2**.

### B3. Ohta — Compositio 115 (1999) 241–301 (user-supplied copy)

- **(1.1.2)** canonical models with i∞ Q-rational. **(1.1.5)** GES_p(N), ES_p(N) as trace limits. **(1.1.6)** e*.
- **(1.2.4)** trace ↔ corestriction; Lemmas (1.2.7), (1.2.10), Cor (1.2.11), (1.2.12).
- **(1.5.3)–(1.5.4).** τ_r intertwines T(n)↔T*(n) and T(q,q)↔T*(q,q) on M_k(Γ_r) and S_k(Γ_r). *This is the equation BCPV cite.* It concerns the slash action on modular forms: no Galois action, no Jacobian, no level transition.
- **Thm-Def (1.5.7).**
- **(2.2.1)–(2.2.3).** τ_r-twisted trace-compatible systems of forms, with an explicit isomorphism involving T*(p)^{±r}. This is the modular-forms prototype of BCPV's W^{-1}(U')^r normalization. The exact exponents/signs are garbled by pdftotext; re-read from the PDF image before any use.
- **(3.3.1)–(3.3.6).** Kummer theory on generalized Jacobians over F̄; trace ↔ Hom(f_*,Z_p) (3.3.4); pullback ↔ Hom(f^*,Z_p) (3.3.5)–(3.3.6).
- **(4.2.4)** w_r^σ = w_r T(a,a) = T*(a,a) w_r for ζ^σ = ζ^a. **(4.2.5)** Q_r over Q. **(4.3.10)** Galois action on cusps. **(4.4.15)–(4.4.16).**
- **§5.1, proof of (5.1.5).** The twisted pairing {,} of [O2] (4.1.17), with adjoints [O2] (4.2.8). [O2] = Ohta 1995 (Crelle 463) — **not consulted**.

### B4. DR22 — Darmon–Rotger, arXiv:2207.01314v1 (4 Jul 2022; only version on arXiv)
Published Astérisque 434 (2022); the published version was **not** consulted.

- **(1.14)–(1.16)** tower and U_p^*. **(1.17)–(1.19)** geometric Shapiro. **Lemma 2.1, Lemma 2.2** (2.7)–(2.8), **Rem 2.3** (2.9).
- **Lemma 2.4** (Chow-level distribution relations): (ϖ_1^3)_* = p^3, (ϖ_2^3)_* = U_p^{⊗3}, Σ = (ϖ_1^3)^*.
- **Lemma 2.5** (θ_q). **(2.17)** Λ(G_r)-hermitian pairing. **Lemma 2.6** (descent to Q(ζ_1) via excision). **Lemma 2.8** (p_{r+1,r} compatibility; θ_q-cycles, no W, no e^*). **Def 2.9, (2.27), Lemma 2.10.**
- **Citation note.** BCPV Lemma 4.10 cites "[DR22], Lemma 2.5" (second statement) for (ϖ_2)_*-type behaviour, which is **Lemma 2.4** in arXiv v1. BCPV's proof of Lemma 4.2 cites Lemma 2.5 for θ_q-annihilation, consistent with v1. The offset is either a BCPV slip or published-version renumbering. Not a mathematical issue: **CITATION_OFFSET_UNRESOLVED**.

### B5. BCPV — arXiv:2409.08645v1 (13 Sep 2024; "to appear" in the EMS Congress Reports volume *Arithmetic of L-functions*)

- **PRINTED.** §1.1.4–1.1.10 ((1.2)–(1.14)); §2.2 (2.9), Lemma 2.1; §4.1 Lemma 4.1; §4.2 (4.1)–(4.11), Lemma 4.2, Def 4.3, Rem 4.4, Rem 4.5, Def 4.6, Lemma 4.7, Def 4.8, Rem 4.9, Lemma 4.10, Cor 4.11, Def 4.12–4.14; §4.2.5 Lemma 4.15, Rem 4.16, Def 4.17, Lemma 4.18; §4.3 Lemma 4.19, (4.12)–(4.16); §5.2.1; Prop 6.2, Cor 6.3, Rem 6.4 (6.9, local); Prop 6.5; Thm 7.3.
- **NOT_PRINTED in BCPV.**
  - (i) any definition of W_{N_h p^r} or W_{Np^r};
  - (ii) the Galois-twist formula for W, used implicitly in Lemma 4.2(ii);
  - (iii) the W/degeneracy interchange formula, used in the proof of Lemma 4.10;
  - (iv) a proof that (1.4) interpolates (1.7), imported from [KLZ17 §7];
  - (v) the relation between W_{Np^r} (common tame level, (4.4)) and W_{N_h p^r} (native, (1.6)) under the Def 4.13 pushforward;
  - (vi) any unspecialized finite-level transition of *contracted* (trace) classes — (4.14) is stated only at (κ,λ) ∈ A_r^{(2)};
  - (vii) any point-valued tower.

### B6. How — Howard, arXiv:1202.6358 (Invent. Math. 167 (2007) 91–128)

- **Def 2.1.3** (Θ, T^†); **Prop 2.1.2**; the pairing Ta^ord × Ta^ord → Λ(1)⊗Θ^2 [26 §1.6.10; 28 §4]; **(3)** T^†×T^† → R(1).
- **Lemma 2.2.1, Cor 2.2.2** (CM moduli, point-level Galois law (5)); **(6)**, **(7)** (fixed-base twisted point module via corestriction); the twisted Kummer map (unnumbered display, "both h_{2,s} and G_Q equivariant"); **(8)**, **(9)**; **Def 2.2.3** (lim U_p^{-s}).
- **Lemma 2.2.4**: α_*(X_{c,s+1}) = U_p·X_{c,s}. *Proof order:* a point-level divisor identity (11)–(12), then corestriction, then Kummer naturality.
- **Prop 2.3.1** (corestriction relations). **Lemma 2.3.3**: W_N acts on T as wΘ(−N), w = ±1.
- *HYP vs C:* **PARTIAL**. Same architecture — twisted fixed-base point module, corestriction, twisted Kummer map, plain Albanese α_* with U_p-normalization. But the points are Heegner points on one Jacobian, the twist Θ acts through diamonds of that one tower, and the point-level transition comes from CM theory. BCPV Rem 4.9 and Rem 4.16 themselves point to this analogy.

### B7. MRS — arXiv:math/0609066v2 (J. Algebra 314 (2007))

- **Def 1.1, Rem 1.2, Lemma 1.3, Thm 1.4, Ex 1.5(ii),(iv), Prop 1.6, Cor 1.7, Thm 1.8, Cor 1.9, Cor 1.10, Thm 2.1, Thm 2.2, Lemma 2.3, Lemma 2.4, Cor 2.5, Prop 2.6, Def 3.1, Lemma 3.2–3.5, Prop 4.1, (4.1), (4.2), Prop 4.2, Thm 4.5, Def 5.1, Thm 5.2, Thm 5.5, Thm 5.8, Rem 5.11 (5.2).**
- *HYP:* I ∈ FMod_O(k) needs a finite Galois image (discrete topology), and O commutative acting on V over k. YES for I_r^† = Z[G_r] at finite r with O = Z; NO for Z_p[[G_∞]]^†.
- **Absent:** any Kummer, Galois-cohomology or Shapiro statement.

### B8. Cais — arXiv:1209.0046
- **Rem 2.3.5; Prop 2.3.6; Def 2.3.23; Prop 2.3.24; (5.2.9); Prop 5.2.4 and its proof; Prop 5.4.9; Lemma 5.4.10; Prop 5.4.12; Lemma 5.4.13; Prop 5.4.15.**
- *HYP:* local over Q_p for §2–5.2, with the Katz–Mazur model and Cais's own w_r. Global over Q only in §5.4 (quotients B_r, maps W_r). **PARTIAL.**

### B9. Downloaded but not relied on
- Longo–Vigni, arXiv:0903.2797: only headings and §5.4 (critical characters) scanned; no item relied upon.
- Hida, MWCT slides (UCLA): grep-scanned; no item relied upon.

### B10. Web / abstract level only (no mathematical item relied upon)
- arXiv abstract pages: 2409.08645 (authors, version), 2207.01314 (v1 only), 1503.02888 (KLZ17; v1–v6; CJM 5 (2017) 1–122).
- Search results only: BSV22 (Astérisque 434, pp. 77–174; the uni-due.de PDF), Castella arXiv:2312.01481, Darmon–Rotger arXiv:2207.01310.
- **Search negative.** No title or abstract found that claims a Λ-adic, big or pro-family of Chow–Heegner points or a norm-compatible diagonal-cycle point tower. This is a title/abstract-level negative, **not** a proof of absence.

---

## C. Addendum: sources downloaded after the second approval (KLZ17, BSV22)

In §B10, KLZ17 and BSV22 were web/abstract-only when that section was written; both are now consulted in full (hashes in 06).
The search-target matrix §A gains these entries:
row 1 (w-twisted degeneracy): KLZ17 Prop 10.1.1 proof; BSV22 Lemma 6.1 proof; BSV22 §4.3 (92).
row 2 (starred/unstarred): KLZ17 Def 2.4.3; BSV22 (65)–(68), (114).
row 7 (group ring): KLZ17 Thm 7.2.3(v) (Λ-adic pairing, statement only).

### B11. KLZ17 — Kings–Loeffler–Zerbes, *Rankin–Eisenstein classes and explicit reciprocity laws*, arXiv:1503.02888 v6 (21 Nov 2023; includes §13 "Correction (November 2023)")
Published CJM 5 (2017) 1–122.

- **Def 2.4.1–2.4.3, Lemma 2.4.4, Prop 2.4.5.** Degeneracy maps, primed Hecke operators as correspondences, and the level-change identities (pr_2)_*U'_p = p^{k+1}(pr_1)_* and (pr_1)_*U'_p = T'_p(pr_1)_* − [[p,0],[0,p^{-1}]]^*(pr_2)_*.
- **Notation 2.5.1, Def 2.5.2 and relations, Rem 2.5.3, Def 2.5.4.** W_Q as a matrix class and as a moduli automorphism over Z[1/N, ζ_Q]. Relations: W_Q^2, diamond conjugation, W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'}, and the Atkin–Li comparison. **No Galois-twist formula printed.**
- **Rem 2.6.1.** Galois behaviour of forms in the point model; W_N interchanges rationality structures.
- **Thm 4.5.1** ((1) the inverse limit over (pr_1)_*; (2) moment maps = Ohta's twisting), **Rem 4.5.2–4.5.3.**
- **Prop 7.2.1** (Ohta: tower, inverse-diamond Λ_D-structure, Galois and T'_n commute, tame W_Q only, perfect control), **Rem 7.2.2.**
- **Thm 7.2.3** (Ohta [Oht00]: F^±, (v) the canonical perfect Λ_D-pairing). **Proof:** Oht00 Cor 1.3.8, 2.3.6, plus the model dictionary (twist by 1+k+ε_N).
- **Def 7.2.5, Thm 7.2.8** (Wiles), **§7.3, Prop 7.3.1**, **§7.4** (M' via W_{Np^r}^{-1}), **Rem 7.4.1** (τ_r = W_{Np^r}^{-1} up to sign), **Lemma 7.4.2** (= Oht99 Thm 2.2.3, 2.4.5), **§7.5–7.7.**
- **Prop 10.1.1** (λ_N(f); the identities W_{Np}pr_1^* = pr_2^*W_N and W_{Np}pr_2^* = p^k pr_1^*W_N in its proof; "the duality pairing involves the same factor W_{Np^r}^{-1}∘(U'_p)^r"). **Prop 10.1.2** (Λ-adic W_N).
- *HYP vs C:* **PARTIAL.** These are cohomological (étale/de Rham) and Λ-adic statements. No finite-level statement of the modified-pairing compatibility with degeneracy maps is numbered anywhere in KLZ17; KLZ17 defers to [Oht00] (Ohta 2000, Math. Ann. 318), which was **not consulted**. No points.

### B12. BSV22 — Bertolini–Seveso–Venerucci, *Reciprocity laws for balanced diagonal classes*, author PDF Ast-BSV1.pdf (CreationDate 22 Feb 2021)
Published Astérisque 434 (2022) 77–174; the published version was **not** consulted.

- **§2.2 (8); §2.3.1** (diamonds; w_p over Z[1/N, μ_p]; dual w'_p; w_Q).
- **§3 Prop 3.2 → Remarks 3.3** ((44)–(46): s_i, V_{N,r}, κ_{N,r}). **CITATION_TARGET_MISMATCH:** BCPV §1.1.9 and fn. 7 point here for W and the (1.6)–(1.9) comparison, but this version of the passage contains no Atkin–Lehner operator. It does contain the S_i ≅ L_i(−i) identification, which parallels BCPV (1.8)'s TSym/Sym^∨ step.
- **§4.1.2 (65)–(68):** U_p w_p = w_p U'_p ⟨p⟩_N and U_p w_{Np} = w_{Np} U'_p (and the dual forms). Equivariance: w_p is G_Q-equivariant, w_{Np} is G_{Q(μ_N)}-equivariant.
- **§4.3 (85), (91)–(92).** **§5 (114).** **Lemma 6.1 proof** (w_N pr_p^* = ⟨(p,1)⟩ pr_p^* w_N; w_N pr_1^* = pr_1^* w_N). **§7.2** pairing [x,y]_ξ = ⟨x, w_{Np}^{-1}y⟩. **§8.1, §8.2 (157)**, Thm 8.1, Cor 8.2.
- *HYP vs C:* **PARTIAL.** Fixed level Np, weight interpolation, twisted-class descent from Q(μ_p) to Q at level Γ_1(N)∩Γ_0(p). No p-power tower, no points.
