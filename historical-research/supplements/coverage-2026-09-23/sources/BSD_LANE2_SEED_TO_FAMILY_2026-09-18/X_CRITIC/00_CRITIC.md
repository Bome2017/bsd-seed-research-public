# Lane 2 — COMPLETENESS CRITIC report (X_CRITIC), 2026-09-18

Fresh-context critic. Custody: writes only X_CRITIC/00_CRITIC.md and X_CRITIC/RESUME.md. Runs nothing heavy.
Inputs read are listed in section 0 as they are read. Findings are appended as they arise (checkpoint policy).
Nothing here is merged. The ledger block in the last section is a PROPOSAL, NOT MERGED.

## 0. Inputs read (read-only)
- 00_LANE2_CHARTER.md (all, incl. section 7), 00_CHECKPOINT_POLICY.md
- results/R_return.md, C_return.md, U_return.md, B_return.md
- results/V_B_verdict.json, V_NUM_verdict.json, V_PARI_verdict.json, V_R_PROOF_verdict.json, V_U_verdict.md
- R_REGULATOR/00_REPORT.md (all 303 lines)

## 1. Running findings (appended in order found)

F-01 (R, status wording; already raised by V_R_PROOF F2 — recorded here as UNRESOLVED IN THE AUTHOR FILES).
 R_REGULATOR/00_REPORT.md section 5 status table and R_return.md still label Lemma 1 / REG_CONGRUENCE / failing-class theorem
 "PROVED", while R's own section 2 (line 54) labels Lemma 1 DERIVED. Charter section 6: proof resting on cited published
 theorems = DERIVED. Survivable status: R-L1, R-REG, R-FAIL = DERIVED. R's section 2 heading "PROVED, modulo the two cited facts"
 and section 3 "REG_CONGRUENCE (PROVED; one cited input...)" also outrun the label rule.

F-02 (R, Lemma 1' text; V_R_PROOF F1). R_REGULATOR/00_REPORT.md line 279 still states the value congruence
 E2(E,w) == E6(E,w) = -c6 (mod 5), which is false in general (V_R_PROOF V3: holds on 912/2352 ordinary curves). The corrected
 statement E2(E,w) == -c6/c4 (mod 5) (unit constants) gives the same conclusion on F_fix because c6 == 0, c4 == 3 (mod 5).
 Critic spot-check (no computation): c4 = b2^2 - 24 b4 with b2 = -20A == 0, b4 = 8AB, AB == 1 (mod 5) => c4 == -192 == 3 (mod 5). Consistent.
 Consequence for the ledger: R-FAIL (ord >= 4) may enter only with the corrected Lemma 1' wording; the author file is not yet fixed.

F-03 (R, internal inconsistency; V_R_PROOF F3). R line 41 ("mod 25 in all cases, and not better in general", blaming the sigma term)
 contradicts R's own Lemma 1' (sigma term in 5^3 Z_5 on F_fix). The discrepancies are the raw-model PARI offset. Not load-bearing.

F-04 (R, stale cross-reference; V_R_PROOF F5). R line 166 cites C's v1 "loc5 = (0,2) occurring with ord 3"; canonical is ord 4
 (C-LOC in C_return is already canonical). Not load-bearing.

F-05 (C, uncorrected formula; V_PARI F1/F2). C_CALIBRATION/00_REPORT.md lines 61-62 and PARI_DEFECT_ellpadicheight.md still give the
 "correct back-transformation" a = u*a' - r*b'/u, b = b'/u, which V_PARI shows is wrong for u != 1 (correct: a = a' - r*b'/u^2,
 b = b'/u^2). No C number depends on it (u = 1 on F_fix). The ledger may carry the defect only in the u = 1 form, plus V_PARI's
 u != 1 correction as referee-level VERIFIED_NUMERIC (4 models), and V_NUM's finding that PARI 2.17.3 has the same defect.

F-06 (C, scope). C's "Tamagawa product 16; torsion Z/2; root number +1" per member (C line 137) is VERIFIED_NUMERIC on the 1233
 sample only; the family-wide versions are U1/U2 (symbolic Tate / Zywina + parity). Fine as stated; no outrun found.

F-07 (B, status wording NOT raised by V_B). B Lemma 2.1 is labelled PROVED (B section 2.1 heading, section 5, Return), but items
 (iii)-(vi) rest on Zywina Thm 1.2, SW Prop 7.2, Mazur's Manin-constant theorem, corrected Wuthrich Prop 1, Kato Thm 7.3 and SW Thm 6.1.
 Charter section 6 => DERIVED for (iii)-(vi); only (i) minimality/ordinarity/#E(F5) and (ii) Tamagawa types are PROVED.
 V_B's confirmed_claims repeat "Lemma 2.1 (PROVED)" without comment. Survivable label: Lemma 2.1(i)-(ii) PROVED; (iii)-(vi) DERIVED.

F-08 (B, source cited but not read). B Thm 2.3 / Prop 2.7 / Thm 2.5 use the "if and only if" of SW Thm 6.1 (Schneider / Perrin-Riou
 control theorem and leading-term formula). B section 2.4 item 2 states "the proof was not read here". All three referee chains (B, U,
 L2B) read SW's statement only. This is acceptable for DERIVED (cited published theorem) but must be carried as a provenance note:
 the primary (Perrin-Riou / Schneider) was not read by any Lane 2 agent or referee.

F-09 (B, stale values in author file; V_B F1/F2). B section 2.7 still cites C's v1 "ord 3 or 4" and b2 records "ord 3 (5), 4 (1)"
 as "identical in all 4 models"; canonical ord is 4 on all six. Cor 2.9 is stated only mod 5 conditional on [REG22] (ord >= 3), and
 Cor 2.10's worked case k = 1 never occurs on F_fix (k in {0} union [2, inf)). Author files not corrected. The ledger may carry only the
 corrected form: a2 == 0 (mod 25) on F_fix intersect {n == 22 mod 25}, DERIVED from Prop 2.7(iii) + R-FAIL (itself DERIVED, with the
 corrected Lemma 1').

F-10 (B, section 2.6 consistency flag - UNRESOLVED ACROSS LANES; routed, not Lane 2's). Under MTT p-adic BSD in SW normalization the
 seed predicts alpha2^SW == eps5 * prod c_v * #Sha * Reg_gamma / #tors^2 == 1 * 16 * #Sha * 1 / 4 == 4 #Sha (mod 5), while the observed
 alpha2^SW == 152/2 == 1 (mod 5). So either #Sha(seed) == 4 (mod 5) (with Sha[2] = 0 (Zywina) and Sha[5] = 0 (N11), #Sha is an odd square
 prime to 5 and == 4 mod 5, i.e. #Sha in {9, 49, 169, 289, ...}; #Sha = 1 is then EXCLUDED under p-adic BSD) or a sign / normalization
 convention is off by -1 somewhere in N6/N7/N9 or in the conjecture's statement. Critic arithmetic: squares mod 5 are {0,1,4}; -1 == 4,
 so the square-class test cannot see a sign error. V_B excluded the index-2 sublattice explanation. No Lane 2 agent or referee
 resolved this. It does not touch any Lane 2 bit-level claim (only the bit beta is used), but it is the one place where Lane 2
 material makes a checkable prediction about the seed's full #Sha, and it must be routed explicitly to Lanes 3/4 (classical BSD
 analytic Sha of the seed would discriminate: #Sha_an = 1 would point to a convention error, which could also affect the recorded
 value "a2 == 2" in N9 only up to sign, not the bit).

F-11 (cross-report label inconsistency for ONE lemma). The integrality lemma "p odd good ordinary, p not dividing #E~(F_p)*prod c_v
 => canonical p-adic heights in pZ_p, Reg_gamma in Z_p" was proved three times, with three labels:
   R Lemma 1 (mod-25 truncation; contains the integrality): DERIVED in R section 2, PROVED in R section 5 table / R_return;
   B Lemma 2.2: DERIVED;  U Lemma INTEG: PROVED (U section 3, U9 block "(U) PROVED (Lemma INTEG)").
 All three rest on the same cited input, Mazur-Tate integrality sigma_p in Z_p[[t]], read only through SW's sentence
 (SW l.808) and the PARI manual; the MT91 primary was read by nobody (V_U residual provenance). Survivable label: DERIVED
 (cited input MT91 via SW). V_U C3 raised this for U only; V_B did not raise it for B (B already DERIVED); V_R_PROOF raised it for R.

F-12 (U block stale against R). U's proposed block FAMILY_ONE_BIT_REDUCTION_F_FIX (U section 9) lists H_REG <=> n != +-22 (mod 25)
 as EVIDENCE and "(S) under a proof of H_REG on a congruence subfamily F_R (sub-lane R)". R-REG (refereed CONFIRMED_WITH_CORRECTIONS
 by V_R_PROOF, V_NUM) now supplies F_R = F_fix intersect {n != 22 mod 25} (DERIVED), and R-FAIL supplies ord5 Reg_gamma >= 2 on the
 complement, which by B Prop 2.7(iii) / U section 7.2(1) forces a2 == 0 (mod 25), not only mod 5. U's block was never updated and
 V_U did not merge the two. The ledger block must be re-assembled from R + U + B rather than copied from U section 9.

F-13 (U block internal labels). In U section 9 "(U) PUB: ... E(Q)/5E(Q) = <P1,P2> (frozen rows)" is not a published result: it is
 PROVED given N1 (U section 4 N2 says so). "Isogeny class {E, E/<(0,0)>}" is listed under PROVED but uses the ledger fact
 ALL_ODD_RESIDUAL_IMAGE_VERIFIED to exclude odd isogenies (DERIVED). Cosmetic, but the block is the thing that would be merged.

F-14 (U11 cost; V_U C2). U section 5 calls linear-in-sqrt(N) scaling "a lower bound on cost". It is a lower bound only for the
 Wuthrich-Thm-12 streaming method as implemented; no method-independent lower bound is proved. Ledger wording: ESTIMATE for this
 method. The conductor bound N >= 8.884e33 for every non-seed member is VERIFIED_NUMERIC (exhaustive k = 1..205 plus monotonicity).

F-15 (R vs C vs Lane 1 L2A — cross-report reconciliation; critic reading, no computation).
 - Mod-25 law: R (Jacobian doubling + own gcd lemma, k = 4,2,4) and L2A (h = h(8P)/64 via Silverman Ex. VI.6.4(e) quoted from Stange;
   primary not read) are two proofs with DIFFERENT lowest-terms mechanisms that give the SAME class table: L2A's
   H/5 = [[1+3s, 3+2s],[3+2s, 3+s]], det 4(s+1)^2, equals R's [[3c-2,2c+1],[2c+1,c+2]], det -c^2, under c = s+1 (confirmed by V_R_PROOF sec. 5).
   L2A Thm C's bad set {m==3 (5), n==+-3 (25)} meets F_fix (n==2 mod 5) exactly in n==22 (mod 25). C's 1233 canonical members agree.
   Seed: L2A H == [[10,10],[10,0]] (mod 25), Reg5 == 25 (mod 125); R: -(12+3)^2 = -225 == 25 (mod 125). Consistent.
 - DISAGREEMENT (resolved against L2A): L2A step 4/5 reports ord5 Reg5 = 3 on (4643,72), (683,228), (24923,72), (1523,372) and writes
   "members ... with n = 22 mod 25 have ord Reg_5 = 3". These are raw-model PARI 2.17.3 values; canonical ord is 4 on all four
   (V_PARI F4, V_R_PROOF V4, R-FAIL). L2A's theorem statements (">= 3") survive; its numeric sentence does not. Same artifact as C v1 and B b2.
 - Scope: L2A proves the law on the wider Zywina family (m == 3 mod 5, n == 12 mod 25), V_R_PROOF notes R's proof also runs on
   {F_Z : (m,n) == (3,2) mod 5}. R states it only on F_fix. No conflict; the ledger should state F_fix and optionally the wider scope as a remark.
 - Critic check of V_R_PROOF's scope remark: on F_Z, m == B == 11 (mod 24) forces 25n^2 == 0 (mod 24), i.e. 12 | n, so R's
   "v2(n) = 2" (Lemma 5 / F2) becomes v2(n) >= 2 there; R's Lemma 4 gcds use only n even and gcd(m,n)=1. Remark only.
 - Lane 1 L2A has NOT been corrected for the ord-3 artifact (read-only for us; operator item).

F-16 (U vs L2B on Skinner-Urban; B vs U on the equivalence direction). Critic reading:
 - U section 6.2/6.3, V_U F3/F8 and L2B section 1.1 agree on every SU hypothesis (good ordinary at 5; rho-bar_5 irreducible;
   q = m || N with rho-bar_5 ramified since v_m(Delta) = 1; (dist) automatic for p odd; integral equality from rho_5 surjective;
   no square-free / semistable / additive condition). NO DISAGREEMENT in substance. But all three readings (U, V_U, L2B) are of the
   SAME document, the authors' Dec-2012 preprint (MC.pdf). V_U's only published-text cross-check is a SECONDARY quotation
   (Dabrowski-Szymaszkiewicz arXiv:1611.07840 sec. 8.4) of the published Thm 2 (the rank-0 BSD consequence), not of the
   main-conjecture theorem. So "SU checked against its ORIGINAL hypotheses" (charter 3.11) is met for the preprint only; the
   published main-conjecture statement (Invent. Math. 195, Thm 3.29/3.33?) remains UNREAD by anyone. Whether that discharges
   3.11 is an operator decision (U says so; V_U agrees).
 - L2B Cor E writes "this closes charter item 11 for the Zywina family at p = 5" outright; U and V_U leave it to the operator.
   Wording in L2B outruns the provenance (same preprint). Lane 1 issue; recorded.
 - B vs U direction: after B's 11:15 fix, B's [SU-int] is f_E in L5*Lambda (i.e. L5 | f_E), the SU direction; Kato's is
   L5 in f_E*Lambda. U uses the full integral equality (f_E) = (L5). Both yield (Sha[5^inf] = 0 and H_REG) => a2 unit. The
   (=>) direction (a2 unit => Sha = 0 and H_REG) is Kato + SW Thm 6.1 + integrality in both. NO DISAGREEMENT after the fix.
   The pre-fix B text (fork 11:02-11:05) had the SU divisibility in Kato's direction; B's own re-check caught it (V_B confirms
   the corrected direction). Residual: B's verdict label (OPEN_WITH_NAMED_INPUT, "PENDING-U") is now stale (V_B F3).
 - L2B's cost statements use the charter's N >= 1e24 ("per-curve cost >= 1e4 x the seed's"); U's exhaustive bound N >= 8.884e33
   supersedes it (V_U). Lane 1 issue.

F-17 (R-EXACT4: a route no agent tried; CRITIC SKETCH, UNVERIFIED — not a claim). R's "first unavailable input" is s2 mod 25 as a
 class function on F_fix. Sketch: Kummer congruence for p-stabilised Eisenstein series, G2* == G22* (mod 25) since 22 == 2 mod 4*5,
 with G22* == G22 (mod 25), gives the q-expansion congruence E2 == 5*E2(q^5) + (24*B22/44)*E22 (mod 25), and E2(q^5) == E2^5 == (E6/E4)^5
 (mod 5). If this lifts through the q-expansion principle for Katz p-adic modular forms (as the mod-5 version E2*E4 == E6 does, V_R_PROOF),
 then E2(E,w) mod 25 is a rational function of (c4, c6) mod 25 with c4 a unit, hence s2 = (b2 - E2)/12 mod 25 is a class function of
 (m,n) mod 25; on F_fix c6/5 == 1 and b2 == 10 (mod 25) for every member, which would make s2 mod 25 CONSTANT (matching the observed
 s2 == 10 (mod 25) on 1233 members). R-EXACT4 would then reduce to a finite class enumeration mod 625. Status: critic sketch only;
 a small sanity test is recorded in section 1a below if run. Suggested owner: R (or Lane 4).

## 1a. Critic sanity test for F-17 (tiny; VERIFIED_NUMERIC for the listed facts only; the route itself is NOT proved)
Script V_VERIFY/runs_X_CRITIC/xc1_E2_mod25.gp, output xc1_output.txt, time xc1_time.txt; PARI 2.17.4 gp-dyn, nice 15, timeout 900,
1.4 s CPU, 9.1 MB RSS, load1 6.2 at start.
- q-expansion level (to q^40): E2 - 5*E2(q^5) - kk*E22 has all coefficients in 25Z_(5), kk = 24*B22/44 = 77683/23 (5-unit);
  E2(q^5) - (E6/E4)^5 in 5Z_(5); E22 = (57183*E4^4*E6 + 20500*E4*E6^3)/77683 exactly.
- Value level: the first (mixed-weight) form E2 == 5(E6/E4)^5 + kk*E22 (mod 25) FAILS at values (928/4160 random ordinary curves)
  — the same weight-mixing error V_R_PROOF found in R's Lemma 1'. The weight-2 form
      E2(E,w) == 5*(E6/E4)^5/E4^2 + kk*E22/E4^5   (mod 25),   E4 = c4, E6 = -c6, E2(E,w) := b2 - 12*s2 (PARI ellpadics2),
  holds on 4160/4160 short models y^2 = x^3 + a4 x + a6, |a4|,|a6| <= 40, ordinary at 5, and on 6 genuine F_fix members
  (seed; (138706163,12); (158905763,673332); (222871163,2019972); (53867843,1346628); (86187203,5386572)), each with v5(diff) = 3.
- On all 6 members: s2 == 10, E2 == 15, b2 == 10 (mod 25), c6/5 == 1 (mod 5). With c6 == 0 (mod 5) the weight-2 formula collapses to
  E2 == kk*a*(-c6)/c4 (mod 25), a function of (m,n) mod 5 only, i.e. CONSTANT on F_fix.
- Reading: R-EXACT4's "first unavailable input" (s2 mod 25 class-determined) looks AVAILABLE by the mod-p^2 Kummer congruence plus
  the q-expansion principle in weight 2 (E_{p-1}^p == 1 mod p^2). Not proved here: the lift from q-expansions to Katz values mod 25 is
  exactly the step that must be cited precisely (Katz 1973 / Serre 1973), and the finite mod-625 enumeration of R-EXACT4 was NOT run.
  Priority LOW: exact ord 4 on the failing class changes no Sha statement (it only fixes the certificate depth there at 4).

F-18 (cross-report: "model-robust" wording outruns the data; NOT raised by any referee as such). C-N5 ("a model change moves Reg5 by
 an amount of ord >= 3"), B Lemma 6.1 / B section 6 ("immune to PARI's model-dependent height offset"), U section 3.5 ("any two candidate
 canonical Gram matrices differ by c*L"; "model-robust"), R_return note 2 ("only ord5 = 2 and Reg5/25 mod 5 are reliable") and Lane 1
 ADDENDUM_001 ("only Reg5 mod 5^3 is model-independent") are all correct ONLY for u = 1 model changes. V_PARI section 6 (line 128)
 shows PARI's ellpadicregulator on a u = 7 model of the seed returns 4*5^2 + 5^3 + ..., i.e. the WRONG Reg5/25 mod 5 (4 instead of 1),
 and V_PARI line 133 says the height is wrong at its leading digit for u in {7, 2, 3, 1/7}. V_PARI classified the ADDENDUM sentence as
 COSMETIC ("refers to PARI outputs") without noticing that its own u = 7 data falsify that sentence for u != 1. No Lane 2 number is
 affected (u = 1 on every model used: V_PARI confirmed r = (5A-1)/3, u = 1). Ledger wording must say "for models differing from the
 reduced minimal model by x -> x + r (u = 1)". Operational consequence for other sessions: a non-reduced model with u != 1 gives a
 WRONG 5-adic regulator even at the 5^2 digit in PARI 2.17.3/2.17.4; always use the reduced minimal model or Sage.

F-19 (task-prompt / charter "KNOWN DEFECT" statement incomplete). The relayed defect text ("PARI 2.17.4 ... canonical - 2r*log(P)^2")
 omits (i) PARI 2.17.3 has the identical defect (V_NUM, V_PARI), so the sage-env gp is NOT a safe fallback on raw models;
 (ii) the u != 1 scaling error (V_PARI). Charter section 1's "PARI's normalization equals Stein-Wuthrich's (446d1 reproduced to O(5^7))"
 is true only on reduced models (446d1 has r = 0, so that check is blind to the defect: C, V_PARI). Charter section 1's recorded seed
 expansion (5^2 + 2*5^4 + ...) is the raw-model output, correct only mod 5^3; the canonical expansion is C-SEED. Operator items.

F-20 (V_U custody/status hygiene). V_U.md still says "Status: IN PROGRESS" at line 5 although section 3 contains the final verdict;
 V_U_RESUME.md is stale (11:33); the verdict file results/V_U_verdict.md was reconstructed by the coordinator from V_U.md section 3
 (15:5x) after the agent was cut off. Critic check: V_U.md section 3 is complete and matches V_U_verdict.md in substance. Not a defect
 in the refereeing; recorded so the merge does not cite V_U_RESUME.md.

F-21 (B's residual B-S2.6 value flag vs Lane 1 L2D). L2D records Banwait arXiv:2609.08431v1 Thms A/B (CM, vertical): c~2(p) unit <=>
 (Reg_gamma unit and X[p^inf] = 0) — the same structure as U6/B Thm 2.3+2.5, for CM curves prime by prime. Lane 2 claims no novelty
 for U6/B-T2.3; the ledger block must not present the one-bit equivalence as new in kind (it is SW's method + SU, cf. SW Thm 7.5).

F-22 (normalisation of n in the family law). R-REG's law Reg5 == -(n+3)^2 (mod 125) is NOT invariant under n -> -n (e.g. n = 12 gives 25,
 n = -12 gives -81 == 44 mod 125), although the curve and Reg5 are (P1, P2 -> -P1, -P2). It is correct for the representative n == 12 (mod Q),
 which is how R and C define F_fix (n = Qy + 12, y in Z). U writes members as n == +-12 (mod Q) and the condition as n != +-22 (mod 25),
 which is equivalent. The ledger must state the normalisation "n == 12 (mod Q)" explicitly next to the law, or state the criterion as
 y != 3 (mod 5) with n = Qy + 12, y in Z.

## 2. What is missing (ranked; each has a suggested action)

M-1 (HIGH, custody). Author files still carry the refereed defects: R (PROVED labels; Lemma 1' E2 == E6 value sentence; R1 narrative;
 stale ord-3 remark), B (b2 "ord 3" values; Cor 2.9 only mod 5 on [REG22]; Cor 2.10 worked case k = 1; verdict OPEN_WITH_NAMED_INPUT
 "PENDING-U"), C (u != 1 back-transformation), U (block section 9 predates R: H_REG law as EVIDENCE; "PUB" label on N2; 6.9e9 CPU-h as a
 bound). Action: merge ONLY from a referee-corrected block (section 4 below), or commission a one-pass errata per sub-lane. Do not
 copy U section 9 or any _return.md verbatim.

M-2 (HIGH, provenance gate for charter 3.11). The Skinner-Urban main-conjecture theorem has been read ONLY in the authors' Dec-2012
 preprint (U, V_U, L2B: same PDF, not independent). V_U's published-text check is a secondary quote of Thm 2 (rank-0 BSD), not of the
 main-conjecture theorem (published number 3.29/3.33 unverified). Every "<=" / "a2 == 0 => Sha != 0" statement (U6, U7(3), B Thm 2.5,
 the TARGET_RENAMED relabel) rests on it. Action: operator decides whether preprint reading discharges 3.11; until then label those
 items "DERIVED (SU, authors' preprint Thm 3.6.9)". Cheapest upgrade: a verbatim published-text quotation of the main-conjecture theorem
 (library copy, or a refereed paper quoting it with hypotheses).

M-3 (MEDIUM, sources cited but never read by any Lane 2 agent or referee). MT91 integrality of sigma_p (load-bearing for R-L1, R-REG,
 R-FAIL, B-L2.2, U-INTEG: read only via SW l.808 and the PARI manual); Perrin-Riou/Schneider (SW Thm 6.1: every a2 <-> Sha step);
 Kato Thm 17.4 (via SW Thm 7.3); Katz 1973 / Serre 1973 q-expansion principle (R-FAIL; V_R_PROOF asks for a precise citation);
 Vatsal Va03 (SU's N^- input); Edixhoven Edi91 (via CNS / Cesnavicius); Monsky 1996 / Dokchitsers (U2 root number); Kundu-Ray Thm 3.13
 (web-fetch summary only). Action: carry a provenance column in the ledger; read at least the MT91 and Katz statements before any outward
 use of R-REG / R-FAIL.

M-4 (MEDIUM, unresolved cross-lane flag). B section 2.6 / V_B F8: under MTT p-adic BSD the seed predicts alpha2^SW == 4*#Sha (mod 5) but
 alpha2^SW == 1 is observed, so either #Sha(seed) == 4 (mod 5) (e.g. 9, 49, ...; #Sha = 1 excluded under the conjecture) or a factor-4
 (== -1) normalisation/sign convention differs between LP5, SW and the conjecture. Nobody resolved it. Action (Lanes 3/4, not Lane 2):
 calibrate the LP5 six-symbol VALUE (not the bit) against Sage padic_lseries / p-adic BSD on a small non-anomalous rank-2 curve with
 known Sha and prod c_v / #tors^2 not == 1 (mod 5); independently, Lane 3's classical #Sha_an for the seed would discriminate. No Lane 2
 claim depends on it (only the bit beta is used; 2 and 4 are 5-units).

M-5 (MEDIUM, wording). "Model-robust" statements restricted to u = 1 (F-18); the defect statement must include PARI 2.17.3 and u != 1
 (F-19); the family law needs the n == 12 (mod Q) normalisation (F-22). Action: ledger wording; notify the certificate session (N5 digits,
 ADDENDUM_001) and Lane 1 (L2A ord-3 rows, L2B "closes item 11", L2B's 1e24 bound).

M-6 (LOW, modality not run). R-EXACT4 (ord5 Reg5 = 4 exactly on n == 22 mod 25) is OPEN with first unavailable input "s2 mod 25 class-
 determined". No agent tried the mod-p^2 Kummer congruence route; critic sanity test (section 1a) supports it (4160/4160 curves; s2 == 10
 mod 25 on 6 members). Action: an R-type agent writes the weight-2 lift with a precise q-expansion-principle citation and runs the
 mod-625 enumeration (3125 failing classes, seconds). Changes no Sha statement; fixes the certificate depth on the failing class at 4.

M-7 (LOW, external action needs the user's permission). V_PARI wrote a minimal PARI reproduction (runs_V_PARI/t7_repro.gp) and a proposed
 patch but filed nothing. Reporting upstream is an outward action: the user decides.

M-8 (LOW). No semantic novelty check exists for REG_CONGRUENCE (congruence control of 5-adic regulators on an explicit infinite rank-2
 family). Needed only if it is ever stated outward; L2D swept Sha results, not regulator laws.

M-9 (NONE REQUIRED, labelling). Lemma A (infinitude of every congruence class used) was not re-audited, per charter; every infinitude claim
 is DERIVED via a derived (non-verbatim) lemma and must be labelled so. Zywina Thm 1.2 (rank 2, Sha[2] = 0) is an arXiv v1 preprint and is
 an input to R-EQ, U4, U6 and B-T2.3 (ord_T f_E >= r needs r = 2).

## 3. Cross-report disagreements (summary; details in F-items)
X-1 PROVED vs DERIVED for the same integrality lemma (R section 5 / U INTEG PROVED; R section 2 / B DERIVED) -> DERIVED (F-01, F-11).
X-2 ord5 Reg5 on n == 22 (mod 25): "3" (C v1, B b2, L2A, raw U u6 by model 3/4/3) vs canonical 4 (R5, C canonical, V_NUM 142/142, V_PARI,
    V_R_PROOF V4/V5 Sage) -> 4 (raw-model artifact) (F-09, F-15).
X-3 C's u != 1 back-map vs V_PARI's (a = a' - r b'/u^2, b = b'/u^2) -> V_PARI (F-05).
X-4 "model-independent" (C-N5, B-L6.1, U 3.5, R note 2, ADDENDUM_001) vs V_PARI's own u = 7 data -> u = 1 only (F-18).
X-5 SU status: B "PENDING-U" / U "PASS (preprint)" / V_U "confirmed (preprint + secondary Thm 2)" / L2B "closes item 11" -> operator (F-16, M-2).
X-6 U block "H_REG <=> n != +-22: EVIDENCE" and U/B "a2 == 0 (mod 5)" vs R-REG/R-FAIL (DERIVED) and a2 == 0 (mod 25) (F-12, F-09).
X-7 B Cor 2.10 depth 3 ([b/125]+, k = 1) vs k in {0} u [2, inf) on F_fix -> depth >= 4 (V_B F2).
X-8 Charter section 1 / N5 seed digits (raw) vs C-SEED; "PARI = SW normalisation" only on reduced models (F-19).
X-9 Conductor bound 1e24 (charter, L2B) vs 8.884e33 (U, V_U) (F-14).
X-10 R section 1 R1 narrative vs R's Lemma 1' (F-03); R Lemma 1' E2 == E6 value congruence vs V_R_PROOF's 912/2352 (F-02).
X-11 B section 2.6 "Reg_gamma == 6 (mod 25) (C)" (raw) vs canonical 21 (not used by B; stale).
X-12 p-adic BSD value at the seed: predicted 4*#Sha vs observed 1 (mod 5) (F-10, M-4) — UNRESOLVED.
X-13 n sign convention: U n == +-12 (mod Q), n != +-22 (mod 25) vs R/C n == 12 (mod Q), n != 22 (mod 25); law not n -> -n invariant (F-22).

## 4. Proposed LEDGER BLOCK for Lane 2 — NOT MERGED (critic draft; only claims that survived refereeing, in their corrected form)

```
LANE2_SEED_TO_FAMILY (2026-09-18) — NOT MERGED. Drafted by X_CRITIC from refereed material only
  (referees: V_R_PROOF, V_NUM, V_PARI, V_B, V_U; all CONFIRMED or CONFIRMED_WITH_CORRECTIONS; corrections applied below).
SETTING  F_fix = {(m,n): m == 2243, n == 12 (mod Q = 673320 = 2^3*3*5*31*181); m, A = m+16n^2, B = m+25n^2 prime}; n is NORMALISED by
  n == 12 (mod Q), i.e. n = Qy + 12, y in Z. E = E_{m,n}: y^2 = x^3 - 5A x^2 + 4AB x; P1 = (A, 6nA), P2 = (36n^2, 12n(m - 2n^2)).
  Heights: Stein-Wuthrich (4.1) canonical 5-adic height; Reg_gamma = Reg5 / log5(6)^2.

(D) PARI DEFECT  [DERIVED from ellpadic.c l.740-745 + VERIFIED_NUMERIC; C, R, V_NUM, V_PARI]
  PARI 2.17.3 AND 2.17.4 ellpadicheight / ellpadicregulator on a model x = x_min + r (u = 1) return canonical - 2r*log_E(P)^2
  (bilinearly -2r log P_i log P_j); on F_fix r = (5A-1)/3, u = 1. For u != 1 there is an additional scaling error and the result is wrong
  already at the 5^2 digit of Reg5 (V_PARI: u in {7, 2, 3, 1/7}; correct back-map a = a' - r b'/u^2, b = b'/u^2). ellpadics2 transforms
  correctly under u = 1 changes (s2_raw = s2_min - r, V_NUM); its u != 1 behaviour was not tested.
  Workaround: PARI on the reduced minimal model (ellchangecurve(e, ellglobalred(e)[2])) or Sage padic_height.
  Robustness: for u = 1 model changes only, ord5 Reg5 = 2 vs >= 3 and Reg5/25 mod 5 are unaffected; digits from 5^3 are not.
(S) SEED CANONICAL REGULATOR  [VERIFIED_NUMERIC; C-SEED, R-SEED; independently V_NUM (O(5^27)), V_PARI (O(5^32)), Sage]
  Reg5(<P1,P2>) = 5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 4*5^6 + 4*5^8 + 4*5^9 + 5^10 + 5^11 + 4*5^12 + 4*5^13 + 4*5^14 + 5^15 + 3*5^16
  + 3*5^17 + 2*5^18 + 5^19 + 2*5^20 + 3*5^22 + 4*5^24 + 3*5^25 + 3*5^26 + O(5^27); Reg5/25 == 16, Reg_gamma == 21 (mod 25).
  The expansion recorded in the SW gate / charter section 1 / N5 (5^2 + 2*5^4 + ...) is the raw-model output, correct only mod 5^3.
  ord5 Reg5 = 2 and Reg5/25 == 1 (mod 5): unaffected; N5 and N11 stand. (Operator decision to replace the N5 digits.)
(R1) REG_CONGRUENCE  [DERIVED: SW (4.1) + Mazur-Tate sigma_5 in Z_5[[t]] (MT91, read via SW) + exact algebra (R Lemmas 2-5, PROVED)
  + finite class evaluation; independent second proof: Lane 1 L2A (same table); numerics C 1233 + V_NUM 9 new members, Sage]
  For every (m,n) in F_fix:  Reg5(<P1,P2>) == -(n+3)^2 (mod 5^3). With c = (n+3)/5 mod 5, (h_ij/5) == [[3c-2, 2c+1],[2c+1, c+2]] (mod 5).
  Hence ord5 Reg5 = 2 <=> n != 22 (mod 25) <=> y != 3 (mod 5), and then Reg_gamma == -c^2 (mod 5) is a 5-adic unit (value for kappa(gamma) = 6).
  Modulus 25 is minimal (K = 2); m mod 25 is irrelevant. Same ord for E(Q) [DERIVED via N2: index prime to 5; rank 2 from Zywina Thm 1.2].
  The law does NOT lift to mod 5^4 (fails in 325/625 classes mod 125) [VERIFIED_NUMERIC].
(R2) FAILING CLASS  [DERIVED: inputs of (R1) + Katz/Serre q-expansion principle in weight 2, E2*E4 == E6 (mod 5), i.e.
  E2(E,w) == -c6/c4 (mod 5) (the value congruence E2 == E6 used in R's text is FALSE in general and is replaced); on F_fix c6 == 0,
  c4 == 3 (mod 5), so s2 == 0 (mod 5) and heights are known mod 5^3]
  n == 22 (mod 25)  ==>  ord5 Reg5(<P1,P2>) >= 4, ord5 Reg_gamma >= 2 (also for E(Q)).
  ord5 Reg5 = 4 exactly: VERIFIED_NUMERIC on 142 certified members (C 133 + V_NUM 9), incl. (222871163, 2019972); on the whole class OPEN.
(R3) INFINITUDE  [DERIVED via Fable's Lemma A (a derived, non-verbatim lemma; not re-audited), modulus Q' = 5Q = 3366600, n0 = 12 + jQ]
  Each class n == 2, 7, 12, 17 (mod 25) of F_fix, and the failing class n == 22 (mod 25), is infinite.
(I) INTEGRALITY  [DERIVED: SW (4.1) + MT91 via SW; R Lemma 1, B Lemma 2.2, U Lemma INTEG]
  E/Q good ordinary at odd p with p not dividing #E~(F_p)*prod c_v  ==>  canonical p-adic heights in pZ_p, Reg_gamma in Z_p.
  On every F_fix member (#E(F5) = 8, prod c_v = 16): Reg_gamma in Z_5.
(N0) UNIFORM LOCAL DATA on the Zywina family  [PROVED: symbolic Tate at 2, 3, m, A, B + finite 2-adic sweep; V_U re-derived]
  N = 2^3*3*m*A^2*B; types 2: I1* (c=2, f=3), 3: I2 (2), m: I1 (1), A: III (2), B: I2 (2); prod c_v = 16; minimal model;
  on F_fix: E mod 5 = y^2 = x^3 - x, a5 = -2, #E(F5) = 8, alpha == 13 (mod 25), eps5 unit; torsion Z/2 [PROVED on F_fix].
  Root number +1 [DERIVED: Zywina Sha[2] = 0 + 2-parity]. Isogeny class {E, E'} [DERIVED: + ledger ALL_ODD_RESIDUAL_IMAGE_VERIFIED].
  5 does not divide c_E [DERIVED: Mazur + isogeny degree 2]. N >= 8.884e33 for every member other than the seed [VERIFIED_NUMERIC];
  the 6.9e9 CPU-h figure is an ESTIMATE for the seed's streaming method, not a lower bound.
(F) SIX-SYMBOL FORMULA uniform on F_fix  [DERIVED: SW Prop 3.5 with c = 0 (5 not dividing c_E, L(E,1) = 0 from rank 2)]
  a2(E) == 3([2/25]+ + [3/25]+ + [4/25]+ + [11/25]+) + 4([9/25]+ + [12/25]+) (mod 5), with E's OWN plus symbols; values per member (M1).
(K) KATO DIRECTION  [DERIVED: Kato (SW Thm 7.3) + SW Thm 6.1 (Schneider/Perrin-Riou, statement only) + (I) + Zywina rank 2]
  For every member: a2(L5) != 0 (mod 5)  ==>  ord_T L5 = 2, Sha(E/Q)[5^inf] = 0 AND ord5 Reg_gamma = 0 (H_REG not a hypothesis).
  a2 unit <=> (mu, lambda)(L5) = (0, 2) [PROVED, Weierstrass preparation].
(Z) FORCED ZERO  [DERIVED: Kato + SW Thm 6.1 + (I) (B Prop 2.7) + (R2)]
  a2 in Reg_gamma*Z_5 on every member. Hence on the infinite class F_fix cap {n == 22 (mod 25)}:  a2(L5) == 0 (mod 25).
  This is congruence control of a2 in the degenerate direction only; it carries NO Sha information.
(SU) CONVERSE  [DERIVED from Skinner-Urban Thm 3.6.9 as stated in the AUTHORS' PREPRINT (Dec 2012); hypotheses (good ordinary at 5,
  rho-bar_5 irreducible, q = m || N with rho-bar_5 ramified since v_m(Delta) = 1, (dist) automatic, rho_5 surjective for integrality)
  checked on every member by U, V_U and Lane 1 L2B (same document). Published Invent. Math. 195 main-conjecture text NOT read.
  Whether this discharges charter 3.11 = OPERATOR DECISION.]
  For every member: (f_E) = (L5) in Z_5[[T]]; hence a2 != 0 (mod 5) <=> [Sha(E/Q)[5^inf] = 0 AND ord5 Reg_gamma = 0];
  with k = ord5 Reg_gamma: ord5 a2 >= k always (Kato), and [Sha[5^inf] = 0 and height nondegenerate] <=> [a2 != 0 and ord5 a2 = k].
  On F_fix cap {n != 22 (mod 25)} (by (R1)): Sha(E/Q)[5^inf] = 0 <=> a2 != 0 (mod 5).
  On F_fix cap {n == 22 (mod 25)} (k >= 2): the Sha test needs a2 mod 5^(k+1), i.e. plus symbols of depth >= 4 ([b/625]+).
(V) MECHANISM VERDICT for a2 != 0 (mod 5) on a congruence class  [TARGET_RENAMED_NO_MECHANISM, conditional on (SU)'s provenance]
  Any congruence class c (containing the seed, Lemma-A admissible) with beta = 1 on F_fix cap c must have 25 | modulus and avoid
  n == 22 (mod 25); on such a class a2-control is equivalent to Sha(E/Q)[5] = 0 on the class, i.e. the Lane 2 target itself.
  Mechanisms checked (B survey a-f, V_B's own search, Lane 1 L2D): transport needs a common residual representation (M1, charter 3.1);
  the rest are TARGET_RENAMED, PER-CURVE, charter-closed, or density/parity statements: NOT FOUND in the sources checked (not an impossibility).
  Whether beta is constant on some class: OPEN.
FIRST_UNAVAILABLE_INPUT  dim_F5 Sel5(E_{m,n}/Q) = 2 (equivalently Sha(E/Q)[5] = 0, equivalently ker(loc31, loc181) = 0 on Sel5) for every
  member of an admissible class c containing (2243,12), with 25 | modulus(c) and c inside {n != 22 (mod 25)}.
EVIDENCE (not proofs)  C-J (least j = 2 on the sample), C-ORD4 (digit Reg5/5^4 mod 5 in {1,2,3} fixed by (m mod 25, n mod 125)),
  C-CONT (no precision loss, j <= 9), C-LOC (loc5 does not determine ord5 Reg5: VERIFIED_NUMERIC on explicit members), s2 == 10 (mod 25).
OPEN  R-EXACT4 (ord = 4 on the whole failing class; first input s2 mod 25 class-determined; a route is suggested in X_CRITIC F-17, unrefereed).
NON_CLAIMS  No Sha(E/Q)[5^inf] = 0 for any member other than the seed. No a2 value for any non-seed member except the forced zero (Z).
  Nothing about p-adic BSD values (B section 2.6 flag routed to Lanes 3/4). Nothing about models with u != 1 beyond (D).
  Nothing here is new in kind: (K)+(SU) is SW's method plus SU; Banwait 2026 (CM, vertical) has the same shape.
```

## 5. Critic verdict
Lane 2 is COMPLETE AS REFEREED for its mandate, with corrections outstanding in the author files. The regulator half of the mandate
succeeded (v5(Reg_gamma) is controlled by n mod 25: DERIVED, two independent proofs); the a2 half is TARGET_RENAMED on the good class and
forced zero (mod 25) on the bad class. "One computation becomes infinitely many curves" is NOT achieved: every member other than the seed
still needs its own a2, at N >= 8.9e33. The only items that could change a merged status are M-2 (SU published text) and the operator's
3.11 decision; M-4 is a cross-lane consistency flag that no Lane 2 claim depends on. Nothing was REFUTED except (i) C's u != 1 formula,
(ii) R's E2 == E6 value sentence (conclusion stands), (iii) every raw-model "ord 3" value (canonical 4), (iv) unrestricted "model-robust"
wording (u = 1 only).

## 6. Files and compute (critic)
- X_CRITIC/00_CRITIC.md (this file), X_CRITIC/RESUME.md.
- V_VERIFY/runs_X_CRITIC/xc1_E2_mod25.gp, xc1_output.txt, xc1_time.txt (sanity test for F-17; about 4.3 CPU-s over three runs, 9.3 MB RSS).
- No web use. Nothing written outside X_CRITIC/ and V_VERIFY/runs_X_CRITIC/.
