# LANE 2 — SEED → FAMILY: final report and proposed ledger block (coordinator, 2026-09-18 ~16:10 PDT)

**Status.** FINAL for Lane 2's mandate. The completeness critic's findings are applied. NOTHING IS MERGED; the operator merges.

**Merge only from §4 below.** The author files still carry refereed-out statements (critic M-1), so do not copy from `*_return.md`, U §9 or the sub-lane reports.

**Sources.**
- Sub-lane reports: `R_REGULATOR/`, `C_CALIBRATION/`, `U_UNIFORMITY/`, `B_A2_MECHANISM/`.
- Returns and verdicts: `results/`.
- Referee reports: `V_VERIFY/`.
- Critic: `X_CRITIC/00_CRITIC.md`.
- Machine state: `STATE.json`, `RESUME.md`.

## 0. The question and the answer

The operator's question: is the seed's 5-adic success isolated? Can v₅(Reg_γ) and a₂(L₅) mod 5 be controlled by a finite congruence condition on the fixed-congruence family F_fix?

**Answer.**
- **Regulator half: YES.** It is controlled by n mod 25 alone, with K = 2 minimal: Reg_γ is a 5-adic unit ⇔ n ≢ 22 (mod 25). On n ≡ 22 (mod 25), ord₅ Reg₅ ≥ 4. Both classes are infinite. Two independent proofs agree (R, and Lane 1's L2A), confirmed by 1242 canonical members and by Sage.
- **a₂ half: only in the degenerate direction.** On n ≡ 22 (mod 25), a₂ ≡ 0 (mod 25) is forced, which carries no Sha information. On n ≢ 22 (mod 25), a₂ ≢ 0 (mod 5) is *equivalent* to Sha[5^∞] = 0 (Kato plus the Skinner–Urban preprint), so controlling it would prove the target. No mechanism for it was found.
- **"One computation becomes infinitely many curves" is NOT achieved.** Every member other than the seed has conductor ≥ 8.884·10³³ and needs its own a₂.
- **Verdict.** Every node of the seed's certificate transports to F_fix except the per-curve modular-symbol bit (N7/N9). That is where the seed is isolated.

## 1. Referee outcomes

| referee | target | verdict |
|---|---|---|
| V_R_PROOF | R: regulator theorem | CONFIRMED_WITH_CORRECTIONS. Katz congruence is E₂E₄ ≡ E₆, i.e. E₂(E,ω) ≡ −c₆/c₄ (mod 5); labels become DERIVED; the R1 narrative is fixed. |
| V_NUM | numerics of R and C | CONFIRMED. 25 members by four routes (4 new); 142/142 failing members have ord 4. |
| V_PARI | PARI defect; seed canonical Reg | CONFIRMED_WITH_CORRECTIONS. There is also a u ≠ 1 scaling error; C's u ≠ 1 formula is wrong; PARI 2.17.3 has the same defect. |
| V_U | U: transport and Skinner–Urban | CONFIRMED_WITH_CORRECTIONS. Δ′ exponent is 2¹⁰; the CPU-h figure is an estimate; INTEG is DERIVED. Recovered from its on-disk report after the session limit. |
| V_B | B: a₂ mechanism | CONFIRMED_WITH_CORRECTIONS. Canonical ord on n ≡ 22 is 4; a₂ ≡ 0 holds mod 25; verdict relabelled. |
| X critic | completeness | Complete as refereed; corrections outstanding in author files; the block in §4 uses only refereed claims. |

**What the referees refuted:**
- C's u ≠ 1 back-map formula;
- R's value congruence "E₂ ≡ E₆" (its conclusion survives with E₂E₄ ≡ E₆);
- every raw-model "ord 3" value (the canonical value is 4);
- unrestricted "PARI is model-robust mod 5³" wording, which holds for u = 1 only.

Nothing central was refuted.

## 2. The PARI defect

| aspect | finding |
|---|---|
| Affected functions | `ellpadicheight` and `ellpadicregulator`, in PARI 2.17.3 and 2.17.4 |
| Cause | `ellpadic.c` l.740–745, `a = (a + r*b)/u; b = u*b;`, which maps back in the inverse direction |
| u = 1 error | canonical − 2r·log(P)², bilinearly −2r·l_i·l_j (V_PARI, entrywise to O(5²⁷)) |
| u ≠ 1 error | an additional scaling error; the result is wrong already at the 5² digit of Reg₅ |
| Fix | `b = b/u^2; a = a - r*b;`, in that order |
| Workaround | run PARI on the reduced minimal model, or use Sage's `padic_height` |

**Robustness is for u = 1 only.** Under translation-only model changes, "ord₅ Reg₅ = 2 vs ≥ 3" and Reg₅/25 mod 5 are unaffected; digits from 5³ up are not. Every Lane 2 number used a u = 1 model.

**Independent confirmations:**
- Lane 1 (bsm-b5, ADDENDUM_001; its "robust mod 5³" wording also needs "for u = 1");
- Lane 4 (bsm-e3), with Sage's own `padic_height` (`~/BSD_SEED_2243_12_LANE4_AUDIT_FORMAL_2026-09-18/numerics/L4_reg5_NOTE.md`).

Lane 4 writes the offset as −r·log P·log Q in `ellpadiclog` units. That is a factor-2 convention difference and not load-bearing.

**Minimal reproduction** on 37a1: `V_VERIFY/V_PARI.md` §8 and `V_VERIFY/runs_V_PARI/t7_repro.gp`. **NOT filed; nobody contacted.**

## 3. Cross-lane consistency

- **Lane 1** (a blind duplicate run):
  - L2A's mod-25 table is identical to R's. Its four "ord 3" rows are raw-model artifacts; canonically they are 4.
  - L2B's Skinner–Urban reading agrees with U's. Both read the SAME preprint, so this is not independent evidence about the published text. L2B's 10²⁴ conductor bound is superseded by 8.884·10³³.
  - L2D: the family target is novel as far as it swept, and rank-2 Sha finiteness over Q is open.
- **Lane 3:** Sha_an = 9 (certified numerics; their audit is pending).
  - 5-adic BSD then predicts a₂^SW ≡ ε·Reg_γ·#Sha·∏c/#tors² ≡ 1·1·9·4 ≡ 1 (mod 5), which matches the observed value.
  - So critic item M-4 is resolved as a *consistency check*, and the canonical Reg_γ ≡ 1 (mod 5) is corroborated.
  - It does not affect Sha[5^∞] = 0, since 5 ∤ 9.

## 4. PROPOSED LEDGER BLOCK — NOT MERGED

This is the critic's refereed-only draft (`X_CRITIC/00_CRITIC.md` §4), adopted verbatim except for the two coordinator amendments marked [coord].

```
LANE2_SEED_TO_FAMILY (2026-09-18) — NOT MERGED. Refereed material only (V_R_PROOF, V_NUM, V_PARI, V_B, V_U; corrections applied).
SETTING  F_fix = {(m,n): m == 2243, n == 12 (mod Q = 673320 = 2^3*3*5*31*181); m, A = m+16n^2, B = m+25n^2 prime}; n is NORMALISED by
  n == 12 (mod Q), i.e. n = Qy + 12. E = E_{m,n}: y^2 = x^3 - 5A x^2 + 4AB x; P1 = (A, 6nA), P2 = (36n^2, 12n(m - 2n^2)).
  Heights: Stein-Wuthrich (4.1) canonical 5-adic height; Reg_gamma = Reg5 / log5(6)^2.
(D) PARI DEFECT  [DERIVED from ellpadic.c l.740-745 + VERIFIED_NUMERIC; C, R, V_NUM, V_PARI; Lane 1 and Lane 4 (Sage) independently]
  PARI 2.17.3 AND 2.17.4 ellpadicheight / ellpadicregulator on a model x = x_min + r (u = 1) return canonical - 2r*log_E(P)^2
  (bilinearly -2r log P_i log P_j); on F_fix r = (5A-1)/3, u = 1. For u != 1 there is an additional scaling error; the result is
  wrong already at the 5^2 digit of Reg5 (correct back-map a = a' - r b'/u^2, b = b'/u^2). Workaround: PARI on the reduced minimal
  model, or Sage padic_height. Robustness: for u = 1 changes only, ord5 Reg5 = 2 vs >= 3 and Reg5/25 mod 5 are unaffected; digits
  from 5^3 are not. Minimal reproduction prepared (37a1), NOT filed.
(S) SEED CANONICAL REGULATOR  [VERIFIED_NUMERIC; C, R; independently V_NUM (O(5^27)), V_PARI (O(5^32)), Sage, Lane 4]
  Reg5(<P1,P2>) = 5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 4*5^6 + 4*5^8 + 4*5^9 + 5^10 + 5^11 + 4*5^12 + ... + O(5^27);
  Reg5/25 == 16, Reg_gamma == 21 (mod 25). The expansion recorded in the SW gate / charter / N5 (5^2 + 2*5^4 + ...) is the raw-model
  output, correct only mod 5^3. ord5 Reg5 = 2 is unaffected; N5 and N11 stand. (Replacing the N5 digits is an operator decision.)
(R1) REG_CONGRUENCE  [DERIVED: SW (4.1) + Mazur-Tate sigma_5 in Z_5[[t]] (MT91, read via SW) + exact algebra (R Lemmas 2-5) + finite
  class evaluation; independent second proof Lane 1 L2A; numerics C 1233 + V_NUM 9 new, Sage]
  For every (m,n) in F_fix: Reg5(<P1,P2>) == -(n+3)^2 (mod 5^3); with c = (n+3)/5 mod 5, (h_ij/5) == [[3c-2,2c+1],[2c+1,c+2]] (mod 5).
  Hence ord5 Reg5 = 2 <=> n != 22 (mod 25) <=> y != 3 (mod 5), and then Reg_gamma == -c^2 (mod 5) is a unit. K = 2 minimal; m irrelevant.
  Same ord for E(Q) [DERIVED via N2; rank 2 from Zywina Thm 1.2, arXiv v1]. The law does NOT lift to mod 5^4 (fails in 325/625 classes).
(R2) FAILING CLASS  [DERIVED: (R1) inputs + Katz/Serre q-expansion principle: E2*E4 == E6 (mod 5), i.e. E2(E,w) == -c6/c4 (mod 5);
  on F_fix c6 == 0, so s2 == 0 (mod 5)]
  n == 22 (mod 25) ==> ord5 Reg5 >= 4, ord5 Reg_gamma >= 2 (also for E(Q)). "= 4 exactly": VERIFIED_NUMERIC on 142 certified members;
  on the whole class OPEN (needs s2 mod 25; a route is suggested in X_CRITIC F-17, unrefereed).
(R3) INFINITUDE  [DERIVED via Fable's Lemma A (derived, non-verbatim; not re-audited), modulus 5Q = 3366600]
  Each class n == 2, 7, 12, 17, 22 (mod 25) of F_fix is infinite.
(I) INTEGRALITY  [DERIVED: SW (4.1) + MT91 via SW]
  E/Q good ordinary at odd p, p not dividing #E~(F_p)*prod c_v ==> canonical p-adic heights in pZ_p, Reg_gamma in Z_p. On F_fix: Reg_gamma in Z_5.
(N0) UNIFORM LOCAL DATA on the Zywina family  [PROVED: symbolic Tate + finite 2-adic sweep; V_U re-derived]
  N = 2^3*3*m*A^2*B; types 2: I1* (2), 3: I2 (2), m: I1 (1), A: III (2), B: I2 (2); prod c_v = 16; minimal model. On F_fix a5 = -2,
  #E(F5) = 8, alpha == 13 (mod 25); torsion Z/2. Root number +1 [DERIVED]. 5 does not divide c_E [DERIVED]. N >= 8.884e33 for every
  non-seed member [VERIFIED_NUMERIC]; the 6.9e9 CPU-h figure is an ESTIMATE for the seed's streaming method, not a lower bound.
(F) SIX-SYMBOL FORMULA uniform on F_fix [DERIVED]: a2(E) == 3([2/25]+ + [3/25]+ + [4/25]+ + [11/25]+) + 4([9/25]+ + [12/25]+) (mod 5),
  with E's own plus symbols (values per member).
(K) KATO DIRECTION  [DERIVED: Kato (SW Thm 7.3) + SW Thm 6.1 + (I) + Zywina rank 2]
  For every member: a2(L5) != 0 (mod 5) ==> ord_T L5 = 2, Sha(E/Q)[5^inf] = 0 AND ord5 Reg_gamma = 0 (no regulator hypothesis).
(Z) FORCED ZERO  [DERIVED: (K) machinery + (I) + (R2)]  a2 in Reg_gamma*Z_5; on F_fix cap {n == 22 (mod 25)}: a2(L5) == 0 (mod 25).
  Congruence control of a2 in the degenerate direction only; NO Sha information.
(SU) CONVERSE  [DERIVED from Skinner-Urban Thm 3.6.9 in the AUTHORS' PREPRINT (Dec 2012); hypotheses (good ordinary at 5,
  rho-bar_5 irreducible, q = m || N with rho-bar ramified, (dist)) checked on every member by U, V_U and Lane 1 L2B (same document).
  Published Invent. Math. 195 text NOT read. Whether this discharges charter 3.11 = OPERATOR DECISION.]
  On F_fix cap {n != 22 (mod 25)}: Sha(E/Q)[5^inf] = 0 <=> a2 != 0 (mod 5). With k = ord5 Reg_gamma: [Sha = 0 and nondegenerate]
  <=> [a2 != 0 and ord5 a2 = k]; on n == 22 the Sha test needs plus symbols of depth >= 4 ([b/625]+).
(V) MECHANISM VERDICT  [TARGET_RENAMED_NO_MECHANISM, conditional on (SU)'s provenance]
  A class where a2 != 0 (mod 5) on every member must have 25 | modulus and avoid n == 22 (mod 25); there, a2-control is equivalent
  to Sha(E/Q)[5] = 0 on the class. Checked (B survey, V_B, Lane 1 L2D): transport needs a common residual representation (M1); the
  rest are TARGET_RENAMED, PER-CURVE, charter-closed, or density/parity. NOT FOUND in the sources checked (not an impossibility).
FIRST_UNAVAILABLE_INPUT  dim_F5 Sel5(E/Q) = 2 (equivalently Sha(E/Q)[5] = 0 = ker(loc31, loc181) on Sel5) for every member of an admissible
  class containing (2243,12), with 25 | modulus and inside {n != 22 (mod 25)} — the Lane 2 target itself.
VERDICT [coord]  REGULATOR_TRANSPORTS; A2_BIT_ISOLATED: every certificate node transports to F_fix except the per-curve bit (N7/N9).
CONSISTENCY [coord]  seed p-adic BSD value: predicted eps*Reg_gamma*#Sha*prod c/#tors^2 == 4*#Sha (mod 5), observed a2^SW == 1; consistent
  with Lane 3's certified Sha_an = 9 (their audit pending). Not load-bearing for any Lane 2 claim.
NON_CLAIMS  No Sha(E/Q)[5^inf] = 0 for any member other than the seed. No a2 value for any non-seed member except the forced zero (Z).
  No density or probability statements. Nothing about models with u != 1 beyond (D). (K)+(SU) is SW's method plus SU, not new in kind.
```

## 5. Open items and operator decisions

**Operator decisions needed:**
1. **Charter §3.11 / critic M-2.** Does reading the Skinner–Urban authors' preprint (Thm 3.6.9) discharge the converse check? The cheapest upgrade is a verbatim quotation of the published Invent. Math. 195 theorem.
2. **PARI upstream report (M-7).** The reproduction and patch are ready. Filing is outward-facing, so it waits for the operator.
3. **Certificate N5 digits.** The certificate session decides; Lane 1's ADDENDUM_001 exists. Its "robust mod 5³" wording should say "for u = 1 model changes".

**Provenance that is read by nobody (M-3):**
- MT91 (load-bearing for R1, R2 and I);
- the Katz/Serre q-expansion principle (load-bearing for R2);
- Perrin-Riou/Schneider behind SW Thm 6.1, and Kato Thm 17.4;
- Vatsal, Edixhoven, Monsky/Dokchitser parity;
- Kundu–Ray (web summary only).

Read at least MT91 and Katz before any outward use.

**Other open items:**
- **Novelty (M-8).** No semantic check exists for REG_CONGRUENCE, and one is needed before any outward statement.
- **R-EXACT4 (M-6).** Low priority, and it changes no Sha statement. The route is the weight-2 Kummer congruence mod 25 for E₂. A sanity test passed on 4160 of 4160 curves (critic F-17). It needs one R-type agent plus a mod-625 enumeration; not launched.

## 6. Process record

**Duplicate-writer incident.**
- 11:02: SendMessage to the workflow agents forked a copy of each.
- 11:05: the workflow was stopped, and the copies became the sole owners.
- Files the originals wrote after the fork are quarantined or marked do-not-cite in each sub-lane directory.
- Other sessions were warned, and memory was corrected. Lane 4 later showed that stopping only the fork by its id is the cheaper fix.

**Session limit.**
- About 11:36–15:40. V_U was stopped at its return step; its report was already complete, so the verdict was recovered from disk.
- Nothing was lost. `STATE.json` and `RESUME.md` were refreshed every 10 minutes and after every event.

**Compute:** all Lane 2 work totals under about 15 CPU-minutes. At most 2 heavy processes ran at once.
