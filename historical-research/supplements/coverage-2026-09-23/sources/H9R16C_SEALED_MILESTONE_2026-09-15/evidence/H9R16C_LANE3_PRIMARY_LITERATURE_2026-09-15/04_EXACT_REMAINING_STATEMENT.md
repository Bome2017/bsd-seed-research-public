# 04 — Exact remaining statement (the literature delta for H9R16-C), revision v2

## Change log

- **v1** (this session). The first unprinted statement was E: étale compatibility of BCPV's modified
  pairing across one level step, with an unknown central unit c_r.
- **v2** (after operator input; every claim checked against the local KLZ17 v6 and BSV22 PDFs; see
  03 §6). E is **PRINTED BY REFERENCE** in KLZ17's convention:
  - KLZ17 Thm 7.2.3(v): a canonical perfect Λ_D-pairing on H^1_ord,par(Np^∞) before specialization
    (proof = Oht00 Cor 1.3.8, 2.3.6);
  - the proof of Prop 10.1.1: cohomological factor W_{Np^r}^{-1}∘(U'_p)^r, forms factor
    U_p^r∘W_{Np^r}^{-1};
  - Rem 7.4.1: Ohta's τ_r = W_{Np^r}^{-1} up to signs; Lemma 7.4.2;
  - reduction to level r by the perfect control of Prop 7.2.1(4).

  So c_r = 1 up to sign in KLZ17's normalization. The exact finite-level group-ring packaging and the
  sign are in Oht00, which lane 3 did not consult.

  **Scope correction.** BSV22 (109) is weight specialization at fixed level Γ_1(N)∩Γ_0(p) for integer
  weights k ∈ U_f^cl. It does not cover p-power level or wild characters.

  The first unprinted statement therefore moves to **E′** (packaging of the contraction) together
  with **D4**.

## Settled inputs (printed or printed by reference)

| # | Input | Source |
|---|---|---|
| P1 | E: tower compatibility of the modified pairing, KLZ17 convention | KLZ17 Thm 7.2.3(v), Prop 7.2.1(4), proof of Prop 10.1.1, Rem 7.4.1, Lemma 7.4.2 (→ Oht00) |
| P2 | uncontracted étale transition with dagger | BCPV Cor 4.11(ii), Def 4.12; DR22 Lemma 2.8 |
| P3 | Chow-level ordinary transition | BCPV Lemma 4.10 (= DR22 Lemma 2.4 in arXiv v1) |
| P4 | Kummer naturality, MRS twists, Weil restriction / Shapiro / norms | formal, 03 §2 F1–F4 (not printed in consulted sources) |
| P5 | a K_0-rational τ_r^MW := s_r ⊗ Alb(ϖ_1) in the point model, U'_p-normalized on p-completed ordinary parts | KLZ17 Def 2.4.1, Prop 7.2.1(2); BSV22 §4.3; HidaC §5; MRS Cor 1.7(ii); 03 D2 |
| P6 | Kummer injection on p-completed points | HidaC Lemma 2.1 |

## Statement E′ — first exact unprinted statement: packaging of the modified contraction

**Setting.**
- Point model X_s := X_1(Np^s). The auxiliary g-factors are pushed to native level N_g p^s as in
  BCPV Def 4.13; hazard T7 applies to the tame level.
- G_s ⊂ ((Z/p^s)^×)^3 is the p-Sylow subgroup; Z_p[G_s]^† and Δ^ét_s are as in BCPV Def 4.6 and
  Def 4.8. BCPV (4.1) gives the diamond action on cycles, (4.3) and (4.5) the Galois action.
- On the auxiliary factors, use the modified pairing at level s in KLZ17/Ohta form. Its values lie in
  Λ_D/I_{0,s}, the group ring of p-part diamonds, with Λ_D acting through inverse diamonds (KLZ17
  Prop 7.2.1(1)). It is ∗-hermitian in the sense of DR22 (2.17): ⟨⟨λa,b⟩⟩ = λ^*⟨⟨a,b⟩⟩ and
  ⟨⟨a,λb⟩⟩ = λ⟨⟨a,b⟩⟩. It is Galois-equivariant only as a group-ring-valued pairing (BCPV (1.6),
  values in Z_p[Δ_{N_g p^s}]).
- Compose with the g ⊗ g^c trace (BCPV (1.10)–(1.11)) and with the balanced Hecke-orbit carrier of
  H9R16-A/B, A_s = W_{N_g p^s}^{-1}(U'_p)^s.
- Call the result Contr^mod_s, applied to the dagger-packaged triple classes.

**E′(a) — the target twist.** Contr^mod_s(Δ^ét_s) is a class in H^1(K_0, T_s^{tr,†}), whose
coefficient Galois module is the one induced from ⟨χ⟩_s^{-1/2} on factor 1. Concretely: the diamond
directions of G_s on factors 2 and 3, and the Z_p[Δ_{N_g p^s}]-valued Galois twist of the pairing,
combine through the ∗-hermitian rules to leave exactly the factor-1 dagger. This requires nothing
beyond a projection Z_p[G_s]^† ↠ Z_p[G_s^{(1)}]^† onto factor-1 diamond coefficients that is
equivariant for G_{K_0}.

**E′(b) — the level step.** On U'_p-normalized classes,

    (ϖ_{1,*} ⊗ p^{(1)}_{s+1,s}) ∘ Contr^mod_{s+1}  =  u_s · Contr^mod_s ∘ (ϖ_{1,*}^{⊗3} ⊗ p_{s+1,s}),

for an explicit **central** unit u_s. Its expected shape: a U'_p power on factor 1 (cancelled by the
(U'_p{}^{⊗3})^{-r} of BCPV Def 4.12), nebentype values of tame diamonds on the g-branch (compare
BCPV (4.13), λ_{Np^r}(g_λ)^{-1}), and at most a sign (KLZ17 Rem 7.4.1).

**Ingredients, each printed.** DR22 (2.17) and Lemma 2.8 — the hermitian group-ring pairing and its
compatibility for uncontracted classes. BCPV (4.1), (4.7)–(4.9), Def 4.6, Cor 4.11. KLZ17
Prop 7.2.1(1),(4) and Thm 7.2.3(v). The proof of Cais Prop 5.2.4, which shows the diamond sum over
Δ_r/Δ_{r+1} appearing exactly when both slots are pushed forward.

**Status: NOT_PRINTED.** No consulted source contracts a dagger-packaged triple class by the
modified pairing at unspecialized finite level. The statement is expected to be formal from the
ingredients above; lane 2 should write it.

## Statement D4 — unprinted, formal

For the A_s-twisted balanced finite points of H9R16-A/B, unspecialized:

    Kum(P_s^{tr,†}) = Contr^mod_s(packaged cl_1 Δ_s^ord)   in H^1(K_0, T_s^{tr,†}).

Printed nearby: BCPV Lemma 4.18 (after specialization only) and the Hecke-equivariance of cl_1 used
in the proof of Cor 4.11. **Status: NOT_PRINTED** — formal from étale Abel–Jacobi functoriality for
algebraic correspondences (compare H9R10).

## How C then closes (literature architecture; not a proof)

- E′(b) + P2 + P1 ⇒ τ_r^et(Contr^mod_{r+1} Δ^ét_{r+1}) = u_r · Contr^mod_r Δ^ét_r.
- D4 ⇒ τ_r^et(Kum P_{r+1}^{tr,†}) = u_r · Kum P_r^{tr,†}.
- F4 ⇒ Kum(τ_r^MW P_{r+1}^{tr,†}) = τ_r^et Kum(P_{r+1}^{tr,†}).
- Absorbing u_r into C_POINT_NORMALIZATION and applying Kummer injectivity (P6) gives
  τ_r^MW P_{r+1}^{tr,†} = P_r^{tr,†}.

## Normalization transport (bookkeeping, not a theorem)

- **N1.** Is BCPV's W_{N_h p^r} equal to KLZ17 Def 2.5.4's W_Q with Q = N_h p^r? BCPV never define
  W. The identification is plausible because they rely on KLZ17 §7. Check BCPV's companion [BCS]
  §2.1 (not consulted).
- **N2.** Sign: Ohta's τ_r = W^{-1} up to signs (KLZ17 Rem 7.4.1).
- **N3.** Tame level: W_{Np^r} (BCPV (4.4), common level) vs W_{N_g p^r} (A_r, native level) under
  the Def 4.13 pushforward. Use KLZ17 W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'} and the identities in the proof of
  BSV22 Lemma 6.1.
- **N4.** Hazard T9: if Hida's π^{sr} is used on the point side, insert the levelwise w_s Galois
  twist. The recommended choice is τ^MW = s_r ⊗ Alb(ϖ_1).
- **N5.** The operator-relayed "(Np^r)^{2−k}" factor from an unnamed exposition is **NOT VERIFIED**
  and is not used.

## What would make E′ false (a TYPE_MISMATCH, not a gap)

E′(a) fails if the ∗-hermitian cancellation on factors 2 and 3, combined with the pairing's
Z_p[Δ_{N_g p^s}] Galois twist, leaves a Galois character on factor 1 that is not the image of
⟨χ⟩_s^{-1/2} — for instance, an extra full ⟨χ⟩^{±1} coming from W. Then the contracted classes would
not lie in H^1(K_0, T_s^{tr,†}) as the prompt types that group. No consulted source decides this.
It is the NEXT_SMALLEST_TEST in 00.
