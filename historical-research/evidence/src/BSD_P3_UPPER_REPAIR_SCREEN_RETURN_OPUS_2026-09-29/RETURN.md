# RETURN — Lane R23: source screen for the p = 3 upper half (2026-09-29)
**Worker:** Fable 5.1, not Opus as TASK.md planned. This session also wrote B1. The user confirmed at 14:19:
"its fine do it as fable". So this return is not independent of B1.

## STATUS
- **Route 3: REDUCED**, to one named statement, MS-R3 (below). There is also a scoped SOURCE_FOUND for the
  finiteness half.
  - Finiteness of Sha[3^∞]: Kato 2004 Thm 18.4. It is a rational statement.
  - Integral bound: Ochiai 2006 Thm 3, specialized at f. It is gated by MS-R3.
- **Route 2: NO_SOURCE_FOR_THESE** (scoped; the reading list is below).
- **K-R3: PASS** for both of the strongest candidates. In each, p = 3 is allowed and nonsplit multiplicative p
  is allowed.
  - Kato 18.4: yes / yes.
  - Ochiai 2006: p ≥ 3 is stated (Oc l.248). The weight-2 point f lies in X_arith (Def 2.1).
  - Kim–Nakamura (arXiv:1808.07726) fails: it assumes additive reduction.
- **K-R2.**
  - Ohta [Crelle 463, 1995] needs p > 3. This is a secondary report (Wake Rem 1.8); Ohta's text is paywalled
    and was not read.
  - A p = 3 extension exists: Wake, arXiv:1303.0406v3, Cor 1.7, which needs only Np > 4.

## Route 3(a): finiteness (SOURCE_FOUND; SRC_Kato2004.md §A)
- **Kato Thm 18.4** (Ka l.8707–8723) covers any α with ord_p α < k−1 (18.1). This includes p ∥ N with
  α = a_p. It carries no image hypothesis and no p ∤ N, and it allows every p.
- **Statement.** Take E not a Tate curve at p, and T = T_pE. Then
  corank Sel(T) ≤ ord_{s=1} L_{p-adic,α}(E).
  Here Sel is the usual p^∞-Selmer group (Ka 14.1).
- **Seed check.** α = a₃ = −1 (nonsplit), so 3 is not a Tate-curve prime. E is non-CM.
- **How it enters the upper half.**
  - The certificate gives ord_T L₃ ≤ 2, from a₂ ≠ 0 with a_{4,2} = 15480.
  - Orders do not depend on the normalization.
  - So corank Sel₃^∞(E/Q) ≤ 2 = rank.
  - Hence Sha[3^∞] is finite, with no input from SU, Skinner, Jones or any main conjecture.
  - This replaces Skinner's equality in R1 §2.2 (2.4) for the finiteness step only. It gives no bound ≤ 9.
- **UNCHECKED.** Kato's ord_{s=1} is identified with SW's ord_T L₃(E,T). Both are the bounded interpolant
  with α = −1, so this is standard, but it was checked only by reading.

## Route 3(b): the integral inclusion at f itself (REDUCED; SRC_Ochiai2006.md)
- **Chain, as printed.** Ochiai Thm 3(ii) (Oc l.553–567) gives, over H^n.o_F,
  length(Sel_T^∨)_l ≤ ord_l L^Ki_p + ord_l P_τ^m,
  at every height-one prime l, including those containing p.
- **Specialization.** Take P_τ a unit and specialize as in the proof of Cor 7.5, steps (12)–(14)
  (Oc l.2684–2709). Kitagawa's p-adic period C_{p,I,b} is a unit "by Kitagawa's construction".
- **Result at every I ∈ X_arith(≥0), including I = f.**
  - The inclusion (L^MTT_p(T_I)) ⊆ Ch(Sel_I^∨) holds integrally.
  - Its complex period Ω_{∞,I} is built from the q-expansion f_I and an O-basis of H¹_{B,c} ∩ V^± (Def 6.6).
  - At f, that is the canonical-period type, which S.3 already compares with the Néron period through GV
    and R2 (3.8).
  - So B1's MS-B1 does not arise on this route.
- **Checked for the seed.**
  - (Ir) holds.
  - τ ∈ I₂₂₄₃ gives P_τ a unit, since ρ̄(τ) ≠ 1.
  - −I lies in GL₂(F₃), which supplies τ′.
  - Rem 7.6's local condition at v ≠ 3 holds:
    - v₂(j) = 4 and v₄₅₄₇(j) = 0, so reduction is potentially good there;
    - 2243 and 5843 divide N exactly once;
    - this was a tiny PARI check, and Rem 7.6 is only a remark.
- **(MS-R3), the named missing statement.** The component H^ord_F of Hida's ordinary Hecke algebra through f
  (tame level M = N/3, p = 3) is isomorphic to O[[X]]. This is Ochiai's Thm 2/3 hypothesis
  H^n.o_F ≅ O[[X₁,X₂]].
- **One-way sufficient conditions** (standard: Hida control plus Nakayama; UNCHECKED as written deductions):
  - H^ord_F/P₂H^ord_F = Z₃, i.e. f is the only weight-2 point on its component;
  - for that, it suffices that R2's A = T_m is Z₃, i.e. η_f(N) is a 3-adic unit.
- **Why MS-R3 is sharper than MS-B1.** It is one weight-2 Hecke-algebra property, not a p-adic Hodge
  comparison at infinitely many weights.
- **It cannot be tested locally.** The level is about 6.5·10¹⁵. There is no claim about its truth, and
  A ≠ Z₃ would not refute it.

## How route 3 would close the upper half (one-way; UNAUDITED)
- **If MS-R3 holds,** the chain gives L₃(E,T) ∈ Ch(f) integrally, in the Néron/ω₁ normalization up to
  3-adic units, through the comparison S.3 already uses.
- **B1's upper-half steps would then apply:** ord_T Ch = 2, Jones Thm 3.1 (forward), and the height
  certificate. Together they give #Sha[3^∞] ≤ 9.
- **Not audited here.** The Ch ⊆ (L) direction is not used. Separately UNCHECKED:
  - Ochiai's Sel_I at I = f is identified with the classical Sel_{3^∞}(E/Q_∞).

## Route 2: NO_SOURCE_FOR_THESE (scoped; SRC_Wake2014_OhtaES.md)
- **What Wake gives.** Wake Cor 1.7 (the Λ-adic Eichler–Shimura isomorphism, over Z_p, Np > 4) and Thm 1.1
  (h_r ≅ D(H¹(Ȳ_r)^ord)) are statements for the weight-2 tower X₁(Mp^r).
- **What MS-B1 needs, which is in no text read:**
  - integral weight-k control at p = 3 (Wake attributes Hida's control to p ≥ 5);
  - compatibility of the specialized comparison with Kato's (17.5.1) at weight k_m.
- No argument was attempted.
- The route-3(b) chain does not pass through MS-B1.

## What was read (one SRC file each)
| Source | Parts read | Where it fails for the seed |
|---|---|---|
| Kato 2004 | §§12.4–12.8, 13.1–13.5, 13.14, 14.1, 16.1–16.6, 17.1–17.13, 18.1–18.11 | 17.4 needs p ∤ N; 18.4 is rational |
| Ochiai 2006 | §2; Def 2.1; §6 (periods, Thm 6.7, Prop 6.9); §7 (Conj 7.4, Cor 7.5 and its proof) | MS-R3 (regularity) |
| Kim–Nakamura | §1 | additive reduction only |
| Wake | §1 | weight-2 tower only |
| Skinner 2016 | §§2–3, from the byte-identical input copy | no multiplicative-p Kato-direction statement except Thm A via SU |

**NOT READ** (no claim either way):
- Ohta (paywalled);
- Cais;
- Kitagawa 1994;
- Ochiai 2003 and 2005;
- Fukaya–Kato;
- Emerton–Pollack–Weston;
- Pollack–Weston;
- Fouquet;
- Delbourgo;
- Venerucci;
- Büyükboduk;
- arXiv:1706.01571 (Euler systems over normal deformation rings; a possible weakening of MS-R3).

## Grades (kept separate)
- **THEOREM (printed, read at source):**
  - Kato Thm 18.4 and 17.4;
  - Ochiai Thm 2, Thm 3, Def 2.1, Thm 6.7, Prop 6.9 and Cor 7.5 (statements);
  - Wake Cor 1.5, Cor 1.7 and Thm 1.1–1.2.
- **REMARK grade:**
  - Ochiai Rem 7.6;
  - Ochiai's "C_{p,I,b} is known to be a p-adic unit" (in the proof of Cor 7.5);
  - Wake Rem 1.6, 1.8 and 1.11.
- **PREPRINT copies read:** Wake arXiv v3; Kim–Nakamura arXiv v2.
- **UNCHECKED:**
  - MS-R3 and its sufficient conditions;
  - my one-sided reading of the proof of Cor 7.5;
  - [Kit94], [Och03] and [Och05] at p = 3;
  - Ochiai's Sel_I versus the classical Selmer group;
  - Kato's ord_{s=1} versus SW's ord_T;
  - Ohta's p > 3 (secondary).
- **CONJECTURE:** none asserted.
- No record was edited. S.3's grade and wording are untouched.
- R1, R2 (3.1)–(3.9) and lane 1's SU items were not reopened.

## Files
- NOTES.md, RESUME.md, STATE.json.
- SRC_Kato2004.md, SRC_Ochiai2006.md, SRC_KimNakamura2019.md, SRC_Wake2014_OhtaES.md, SRC_Skinner2016.md.
- sources/: PDFs, pdftotext output and SOURCES.sha256.
- MANIFEST.sha256.
- Computation: one PARI call (j-valuations and local data), under a second. No pushes and no messages.
  Nothing was written outside this folder.

FIN, ORDER9 and Q36 are unchanged.
