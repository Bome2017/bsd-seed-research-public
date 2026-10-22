# STATUS: PASS_WITH_CORRECTIONS

Lane R25-SR, hostile second reader (Claude Opus 5.5, fresh session), 2026-09-29. Target: R25 (route K, nonsplit p = 3).
No step of R25 was found false, and no uncancelled power of 3. Two citation/provenance errors were found; neither
changes the bound. R25's "modulo" inputs (O1: the 3-adic image (12.5.2); O5: the height certificate; S.3's a_{4,2};
B2) are carried as INPUTS. O5 is corroborated by an independent PARI value (SECONDARY). FABLE_CHECK was opened only
after T1–T5 were written.

## Corrections (each with its fix)
- C1 (T1; provenance). R25 INPUT 4 / D7 item 1 inherit the χ ↔ χ^{-1} convention "from Kobayashi's printed split
  identity". Kobayashi's text writes L(E,χ,1) in two places (l.301–305, l.321–322) where Kato 12.5(1) and SW/MTT as printed
  give L(E,χ^{-1},1); the two slips cancel. FIX: source Col(loc z_γ)(χ) = α^{-(n+1)} τ(χ) L(E,χ^{-1},1)/Ω_+ directly from
  Ka 12.5(1) and SW §3.2 (T1 §4). Same identification on both sides; no involution. Kato's L_{p-adic} is evaluated at κχ.
- C2 (T3(b); citation, and a misquote in the first reader's check). The printed Ka 12.5(4) (p.222) states its length
  inequality for V_{F_λ}(f) and Z(f), which is empty at 𝔭 = (3). FIX: cite Ka Thm 13.4(3) (p.226, stated for the lattice T at
  every height-one prime, bounding H²(T)_0 = H²(T) here) via 13.14 (p.234: "The inequality in Thm. 12.5 (4) follows from
  Thm. 13.4 (3)"), as Kato does in 17.13. Its hypothesis (σ with Coker(1 - σ) free of rank 1) needs the 3-adic image
  input O1; ρ̄_3 = GL_2(F_3) alone does not give it.
- Minor (not R25's): SEED_DATA_v2's "Kato 18.4 gives Sha[3^∞] finite" is correct (Ka 18.4, p.281: α ≠ 1); finiteness also
  follows inside route K from ord_T f_E ≤ ord_T L_3 = 2 = rank.

## Kill tests (KILL_TESTS.md): K-SR1 PASS (L_0 = 3/2; 16.2(ii) value 2L(E,1)/Ω_+), K-SR2 PASS (n = 1: both characters give
α^{-2}τ(χ), not α^{-2}τ(χ^{-1}); also n = 2), K-SR3 PASS (≤ 27 routes: stray Euler factor at 5843 — excluded by T3(c);
v_3(Reg_γ) = -1 — excluded at SECONDARY grade by PARI, harmless anyway by squareness. The dangerous ≤ 81 route, a
(log_3 κ(γ))^2 mismatch, is excluded: v_3(det<,>_3) = 2).

## Verdicts: T1 PASS (C1) · T2 PASS · T3 PASS_WITH_CORRECTIONS (C2) · T4 PASS · T5 PASS

## Steps re-derived here (DERIVED unless marked)
1. Kobayashi rearrangement for any norm-compatible c; Λ-linearity of Col (T1).
2. D1.1(c) Gauss-sum identity with α^{-(n+1)} at α = -1: by hand and exact PARI, n = 1, 2 (T1, checks/ksr.log).
3. Character values of Col(loc z_γ) from Ka 12.5(1)+6.2; Birch's lemma for SW's measure; the trivial character exactly,
   sign included (log c_0 = +3/2); Weierstrass-preparation argument for "finitely many zeros" (T1).
4. D5 Step 1 (a)–(e): H^0/H^2 vanishing, freeness, perfect pairing, Kummer surjectivity, Z_3[Γ_n]-freeness (Herbrand
   quotient + Serre IX), generator via norm, log: Ê(3Z_3) ≅ 3Z_3 (T2).
5. D6: (a1), (a2) at every finite level (sharper than 17.9), (a3); Kato's twist bookkeeping T = T_pE(-1) (17.5);
   length inequality at every height-one prime incl. (3) from 13.4(3); (12.5.1) excluded; Σ-imprimitive sequence and
   the exact local term H^1_Iw(Q_5843,T) whose omission would create 1 + 5843^{-1} (T3).
6. D8 steps 4–8 against Jones (printed pp.1, 2, 3, 5, 6, 13, 16, 17, 18): (log_p κ(γ))^{-r}, e = 0, classical Selmer,
   standing hypotheses, m_l prime to 3, order of inference (finiteness before Jones) (T4).
7. D1.1(a),(b), D2.1–D2.3 by hand; Dwork integrality replayed numerically (T5, checks/dwork.gp).

## THEOREM / DERIVED / SECONDARY
THEOREM (read on rendered pages): Ka 6.2, 8.2, 12.2, 12.4, 12.5(1),(3),(4), 13.4, 13.14, 14.9.3, 16.2, 16.3, 17.3–17.5, 17.10,
17.13, 18.4; Kob §3 l.195–329; SW §3 l.285–521; Jones pp.1–18 (author copy). DERIVED: T1–T5 as listed.
SECONDARY: Tate local duality/Euler characteristic, Serre Local Fields IX, BK Prop 3.8; PARI's p-adic height
implementation at nonsplit p (checks/reg.log); the 3-adic image input O1; S.3's a_{4,2}; B2.

## Limits kept: ≤ 2 processes (1 used at a time), tiny PARI only (< 1 CPU-min), no subagents, pushes, messages or paid
compute; writes only in this folder. Files: MANIFEST.sha256.

FIN, ORDER9 and Q36 are unchanged.
