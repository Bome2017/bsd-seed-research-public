# LANE 1 SYNTHESIS: H9 calibration at the seed (2243,12), p = 5

Date: 2026-09-18. Scope: L1A-L1D only. Lanes 2-5 are not synthesized here.
Inputs: L1A/L1B structured returns (`resume_args.pre_stop.json`, key `cached`), L1C/L1D returns (the task text), every
`L1*/00_REPORT.md` and `L1*/VERIFY/00_VERIFY.md`. The synthesis ran two new computations, each under 1 CPU-s:
`00_LANE1_SYNTHESIS/runs/k119.gp` (splitting patterns of candidate K) and `runs/kod2.gp` (reduction at 2).
Under the H9 terminal equivalence, everything below is a CALIBRATION, not a mechanism. Sha[5^inf] = 0 (CERT N11) is an input
and never an output.

## OPERATOR REVIEW (2026-09-18). This section governs.

**Verdict.** Keep and freeze as `LANE1_H9 = CALIBRATION_COMPLETE; CURRENT_SEALED_BRANCH_MISSES_TARGET`, with Castella explicit-instance completion gated by R1–R3 (§3a). The value is structural calibration, not new BSD closure.

**What it establishes.** The H9 target at the seed is explicit: Sel_str(Q,V₅E) = Q₅(P₁ − tP₂) with v₅(t) = 1 and a reproducible 5-adic fingerprint. NC5 is a real negative structural result: the current sealed CH-branch tower output does not hit that line. It does not make H9 impossible. It does mean a future route must be genuinely different. The design question becomes: *what operation changes branch, support or eigenspace so that the known target line can appear?* Future H9 work should not try to prove that the existing same-root/CH branch equals the target.

**What it does not do.**
- It gives no new proof of Sha[5^∞] = 0; that is an input.
- The Kurihara, MR, Kato and class-group checkers are positive controls on this seed, not a general mechanism.
- If Lane 3 finds that full BSD needs some input X, Lane 1 does not automatically supply X.

**Conditions for merging the §4 block:**
1. The calibration wording is corrected. DONE in §4, operator's sentence.
2. The manifest `00_LANE1_SYNTHESIS.MANIFEST.sha256` is generated. PENDING: shell commands are blocked in the coordinator's conversation.
3. The Nekovář claim stays marked PENDING G3, not final. DONE in §4 and §6 (D1).

**Gate order changed to G2 → G3 → G1.**
- If the non-squarefree-N⁺ seam fails, a certified L(E^{−79},1) does not finish the Castella gate, so G2 goes first.
- G1 then starts with a timing prefix. It is certified only if G2 and the χ-existence chain survive and the measured cost is reasonable.

## TOP LINE

1. At p = 5 the seed meets every hypothesis of Castella Thm A that is printed in the statement (L1A C1, confirmed). With
   dim Sel(Q,V_5E) = 2 (N1+N11) and loc_5 != 0 (L1A C3, PROVED), Thm A(2) says: kappa_5(E) != 0, and it spans the strict line
   Q_5*(P1 - t*P2) with t = log_5P1/log_5P2, v_5(t) = 1. This holds for every admissible (K,chi). The status is CONDITIONAL on
   two things: (a) an admissible (K,chi) exists, and (b) Castella's Assumption (A) is sufficient at the non-squarefree N+
   (the transitive seam).
2. NEW IN THIS SYNTHESIS (CERTIFIED_COMPUTATION, `runs/k119_output.txt`): explicit K meet Choice 5.2.1(1)-(2) with 5 split:
   - D = -79 (h = 5): q = 3 is inert; 2, 5, 2243, 4547 and 5843 split; w(E^K) = +1.
   - D = -119 (h = 10): q = 2243 is inert; 2, 3, 5, 4547 and 5843 split; w(E^K) = +1.
   With an explicit K, the literature caveat on the EXISTENCE of K disappears: BFH90 as printed does not give "q inert", and a
   Friedberg-Hoffstein-type theorem would be needed (L1A verifier). What remains for K is one finite computation,
   L(E^K,1) != 0. The existence of chi still rests on Vatsal / CH18 Thm D.
3. Castella-Hsieh Cor B (L1B, verifier-corrected). The CH chain has no failing printed hypothesis. The verifier also closes the
   author's non-computational gap (the vanishing of Sel(K,V_5E(x)chi^2)) with Nekovar 2012 CJM Thm A. What remains:
   L(E^K,1) != 0 (finite; the estimate for K = Q(sqrt-271) is about 16 CPU-h) and the BLV/BD05 substitution caveats.
4. The sealed H9R16-C tower (L1C) instantiates at the seed but does not reach E(Q)(x)Q_5. The first open statement is A1.3;
   the first BLOCKED operation is A1.4 (collapsed carrier). Wherever a value is defined, it is 0, never the strict line. New
   result NC5 (PROVED_DERIVED, first refereed by the L1C verifier): on CH's branch, the E-projected values are eta_K-eigen, so
   their E(Q)-component is 0 at every finite level. This says a component vanishes. It does not say the route is impossible.
5. Checkers (L1D). Every Selmer-side checker is an instance-level PASS: Prop K transferred, the Kurihara witness at 5611, MR at
   (31,181), LI5, and the exact relative class-group form. No class-group bound follows. Theorem NB shows that every c >= 0 is
   consistent with the recorded relation system Sigma plus Sha = 0.
6. What the calibration pins: the target line of H9 at the seed is explicit, including its 5-adic fingerprint
   c_k = -t mod 5^k. Any future H9 output at the seed must equal this line. The calibration gives no new information about
   Sha (G-WSHA fails).

## 1. Lane table

| lane | worker verdict | verifier | what is now known |
|---|---|---|---|
| L1A Castella Thm A | CALIBRATION_INSTANCE_VERIFIED_SCOPED | PASS_WITH_CORRECTIONS (4 corrections: line numbers; first open statement re-aimed; CH l.93-94; unaudited Thm 4.1.1 and BSV22b Cor 8.2 seam) | kappa_5 != 0 spans ker loc_5 = Q_5(P1 - tP2) for every admissible (K,chi). CONDITIONAL on the existence of (K,chi) and on seam 1; lambda cannot be checked from cyclotomic data |
| L1B CH Cor B | CONDITIONAL(L(E^K,1) != 0 at -271 AND S7) | PASS_WITH_CORRECTIONS (verifier REFUTED the OPEN status of C7 via Nekovar 2012) | no printed CH hypothesis fails. BD05 has no squarefree hypothesis (only 5 ∤ deg phi_E is uncertified); PW11 is NOT_APPLICABLE; CH15 is NOT_APPLICABLE at p = 5. Remaining: L(E^K,1) != 0 and the substitution caveats |
| L1C sealed tower | CALIBRATION_COMPLETE / NO_IDENTIFICATION; NOT_ADMITTED (G-MECH) | PASS_WITH_CORRECTIONS (C6 and C7 wording; step-5 simplification) | the seal instantiates with no content about E. A2.3 and A3.2 are BLOCKED. NC5: the eta_K component vanishes on CH's branch |
| L1D checkers | CHECKERS_CALIBRATED: Selmer side ALL PASS; class-group side UNDETERMINED | PASS_WITH_CORRECTIONS (5 corrections: ledger line numbers, headline scope, cosmetic) | Prop K, the Kurihara witness n = 5611, MR (31,181), LI5 and the exact form hold. The class-group region is unbounded in c (NB) |

## 2. PROMOTED CLAIMS (verifier CONFIRMED, or CONFIRMED_WITH_CORRECTIONS with the correction applied)

L1A:
- A-C0 PROVED: the lane target is a corollary of N11 + Thm A. It is equivalent to no open ledger item.
- A-C1 CERTIFIED_COMPUTATION: the Thm A hypotheses hold at p = 5 (a5 = -2; image GL2(F5); q in {3, 2243, 5843}, all ≡ 3 mod 5
  and ramified; w = +1; L(E,1) = 0; p-distinguished). Correction applied: Thm 2.3.2 is at CAS l.330-334, Cor 5.1.3 at l.820,
  (2.1)/(2.4) at l.368, (3.2) at l.515, and Assumption (A) at l.755-758.
- A-C2 PROVED_DERIVED: dim Sel(Q,V_5E) = 2.
- A-C3 PROVED: log_5 P != 0 for every non-torsion P, so loc_5 != 0.
- A-C4 CONDITIONAL: kappa_5(E) != 0 spans Q_5(log_5(P2)P1 - log_5(P1)P2). Corrected condition: (i) an admissible K exists
  (3 inert; {2,5,2243,4547,5843} split; L(E^K,1) != 0), for which BFH90 as printed is not enough; and (ii) seam 1, including
  Thm 4.1.1 and BSV22b Cor 8.2.
  Synthesis update: (i) reduces to L(E^K,1) != 0 at the explicit D = -79 (see §3a).
- A-C5 CONDITIONAL (same K/chi caveat, plus CH l.93-94 on chi): CH Cor B also applies.
- A-C6 CERTIFIED_COMPUTATION (four routes, to O(5^22)): v_5(log P1) = 2, v_5(log P2) = 1, t/5 ≡ 1 mod 5, loc_5 ≡ (0,2) mod 5,
  P1 ∈ 5E(Q_5).
- A-C7 and A-C8 VERIFIED_FROM_SOURCE: the lambda formula exists only in CH; its inputs are anticyclotomic, and no printed
  formula links them to a2 ≡ 2.
- A-C9 OPEN: whether Castella's class equals CH's class.

L1B:
- B-C1 VERIFIED_FROM_SOURCE: no squarefree-N, semistability or Heegner hypothesis in CH Thm A, Cor B or Cor 5.1; only N^- must
  be squarefree.
- B-C2 PROVED: rhobar_5 = GL2(F5), ramified at 3, 2243, 5843, 4547 and 2; a5 = -2; p-distinguished. Correction applied: E has
  potentially good reduction at 2 (v2(j) = 4). Ramification at 2 follows from Serre-Tate, not from a Tate-curve twist. The
  synthesis re-checked this (`runs/kod2_output.txt`): PARI Kodaira code -5 = I1*, v2(j) = 4, v2(Delta) = 8. The label I1* and
  "potentially good" are both correct.
- B-C3 VERIFIED_FROM_SOURCE: CH18 Thm A and Hsi19 put no condition on N^+.
- B-C4 corrected: PW11 is NOT_APPLICABLE (squarefree level N). BD05 Thm 1 is CONDITIONAL(on 5 ∤ deg phi_E, Assumption 6.3);
  it is not NOT_APPLICABLE.
- B-C5 VERIFIED_FROM_SOURCE with caveats: BLV Hyp 1.1 holds for (E, Q(sqrt-271), 5). Residual caveats: BLV l.375-376 says
  "p > 5" while its hypothesis lists say p >= 5, and the match between BLV's theta element and CH's was not verified.
- B-C6 NOT_APPLICABLE(at CH15 (CR+)(1), p = 5).
- B-C8 CERTIFIED_COMPUTATION: 151 admissible D with |D| <= 20000; -271 is the first with 5 ∤ h; ellrank(E^K) = [0,0] for the
  first six. Correction: under the BD05 route, -79 is admissible if 5 ∤ deg phi_E.
- B-C9 PROVED_DERIVED: a chi exists with L(E/K,chi^2,1) != 0 (existence only).
- B-C10 and B-C11: CONDITIONAL(on L(E^K,1) != 0 and L(E/K,chi^2,1) != 0 [existential], and on the BLV/BD05 substitution).
  kappa_{alpha,alpha^-1} lies on the strict line and generates Sel_str. (The S7 condition is removed only if the verifier's C7
  finding is accepted; see §6.)
- B-C12 BLOCKED(at cap): certifying L(E^K,1) at -271 is estimated at about 16 CPU-h. This is an estimate, not a measurement.

L1C:
- C-C1 PROVED_DERIVED: the seal depends on E only through N_E and carries no arithmetic content about E.
- C-C2 CERTIFIED_COMPUTATION + VERIFIED_FROM_SOURCE: the BCPV/H9R17 frame fails at H-2.3 (N not squarefree), H-3.3 (w = +1)
  and (H-omega).
- C-C3 CERTIFIED_COMPUTATION: fingerprint c_k = -t mod 5^k = 0, 20, 70, 195, 820, 13320, 75820, 388320, 1169570, 3122695,
  42185195, 188669570.
- C-C4 VERIFIED_FROM_SOURCE: A1.3 is OPEN (sealed non-claim); A1.4 is BLOCKED (collapsed carrier).
- C-C5 PROVED_DERIVED, refereed by the L1C verifier: NC5, the eta_K-eigen vanishing of the E(Q)-component on CH's branch.
- C-C6 BLOCKED(at A2.3), with the correction: at the seed the Mordell-Weil control is replaced by an etale identification
  (Psi, K_0 -> Q descent, Selmer condition, specialization). None of these is supplied, and the bypass is
  NOT_APPLICABLE(at (H-omega)).
- C-C7 BLOCKED(at A3.2), with the correction: "value 0 = kappa_{alpha,beta^-1}" is VERIFIED_FROM_SOURCE +
  CONDITIONAL(on an admissible (K,chi)).
- C-C8 CONDITIONAL(existence of (K,chi)): H6 and H7 of file 11 are met at the seed.
- C-C9 and C-C10 PROVED_DERIVED: NC1-NC5; the gate audit (G-MECH is the first to fail; G-SUPPORT, G-WSHA, G-REUSE and G-COEFF
  also fail).

L1D:
- C0 through C14 are all CONFIRMED, as stated in the worker return, with these corrections applied:
  - the custody hashes are at ledger l.283/l.295;
  - Theorem NB is about the relation system Sigma, not about Cl(L);
  - §2.5 relies on Kim's sum convention I_n (KIM l.186).
- The key promoted items:
  - C2 Prop K transfer (part (e) CONDITIONAL on Choice 5.2.1);
  - C3 witness n = 5611;
  - C4: 278 witnesses and 47 forced zeros below 3000, smallest witness 4681, first forced zero 58001;
  - C5 Kato primitivity, ord kappa^(1) = 1;
  - C6 MR (31,181) PASS; (71,181) NOT_APPLICABLE(at (H.6));
  - C7 LI5 PROVED;
  - C8 region;
  - C9 NB;
  - C10 exact form;
  - C11 erratum E1;
  - C13 OPEN;
  - C14 CONDITIONAL.

NOT promoted: B-C7 (the author's OPEN status). The verifier REFUTED it by citing Nekovar 2012 CJM Thm A (see §6). No other
claim was refuted.

## 3. THE H9 CALIBRATION MAP at the seed, p = 5

### 3a. What Castella Thm A and CH give, and under which remaining conditions

Castella Thm A(2) (CAS l.98-101):

    kappa_5(E) = lambda * (P1 - t*P2),  lambda ∈ Q_5^x,

for every (K,chi) as in Choice 5.2.1 (CAS l.839-846). Remaining conditions:
- R1 (finite computation): L(E^K,1) != 0 for ONE explicit admissible K. This synthesis certifies admissible splitting
  patterns and root numbers for two candidates (`runs/k119_output.txt`):
  - D = -79: q = 3; N^- = 3; sqrt(N_K) = 6.37e9.
  - D = -119: q = 2243; sqrt(N_K) = 9.60e9.
  A certified nonzero value at either one replaces the existence argument that needs Friedberg-Hoffstein.
  Unmeasured scaling estimate: about 0.83x and 1.25x of the N7 series length, i.e. roughly 5-7 CPU-h. This is not a
  measurement.
- R2 (existence, printed): some chi of l-power conductor with L(E/K,chi,1) != 0 and chi|G_Kp != 1. This comes from Vat03 /
  CH18 Thm D, via L1B C9's argument. That argument was made for -271; it transfers verbatim to any K where 5 splits, but this
  was not re-refereed for -79/-119.
- R3 (seam 1, literature): Assumption (A) is sufficient for Thm 4.2.1 at N+ = 2^3*2243*4547^2*5843 (or N+ = N/2243 for
  D = -119). This needs BD05 (CONDITIONAL on 5 ∤ deg phi_E), PW11 (NOT_APPLICABLE), KPW17, SU14/Wan15, Thm 4.1.1 and
  BSV22b Cor 8.2 (not audited).

CH Cor B (CH l.182-184) at K = Q(sqrt-271), with N^- = 3*2243*5843: kappa_{alpha,alpha^-1} != 0 and generates Sel_str
= Q_5(P1 - tP2). Remaining conditions:
- R1' L(E^{-271},1) != 0 (about 16 CPU-h estimated);
- R3' the BLV Thm A substitution (the p > 5 textual inconsistency; the theta match is unverified) or BD05 (5 ∤ deg phi_E);
- the S7 vanishing, closed by Nekovar 2012 per the verifier (not re-refereed).

The CH route could also run at -79 via BD05, but only if 5 ∤ deg phi_E. The value of lambda cannot be checked at the seed
(A-C8).

### 3b. The strict line

    Sel_str(Q,V_5E) = ker(loc_5) = Q_5*(log_5(P2)*P1 - log_5(P1)*P2) = Q_5*(P1 - t*P2)

where:
- log_5 P1 = 2*5^2 + 3*5^4 + ... (v = 2);
- log_5 P2 = 2*5 + 5^2 + 4*5^3 + ... (v = 1);
- t = 5 + 2*5^2 + 3*5^3 + 3*5^4 + 2*5^8 + 3*5^9 + 5^11 + 4*5^13 + ... (v_5(t) = 1, t/5 ≡ 1 mod 5).

Normalized loc_5 ≡ (0,2) mod 5, so the strict Selmer group mod 5 is <P1>. The integral fingerprint is c_k = -t mod 5^k
(list in §2, C-C3). Status: CERTIFIED_COMPUTATION, by at least five independent implementations across L1A, L1B, L1C and
the verifiers.

### 3c. Where the sealed H9R16-C chain fails (SEAL-05 l.41)

A1 is localization at p_g:
- A1.1 and A1.2 are fine.
- A1.3 is the FIRST OPEN STATEMENT: Q_inf is non-torsion after localization at p_CH (sealed non-claim, SEAL-05 l.58-60).
- A1.4 is the FIRST BLOCKED operation: the collapsed carrier B^bal ≅ R has no h-direction, so the pair is the same-root pair
  (g, g^c) (LEDGER l.47-48).

A2 is Mordell-Weil descent. It is BLOCKED at A2.3: there is no Lambda-adic Mordell-Weil control or descent map to
(E(Q)(x)Q_5)(x)R_g. The etale bypass is NOT_APPLICABLE(at (H-omega)) for CH's g.

A3 is lambda_g-specialization. It is BLOCKED at A3.2: there is no weight-one specialization lemma. Even if A1-A3.2 were
supplied, the value at p_CH would be kappa_{alpha,beta^-1} = 0 (CH l.159, CONDITIONAL on (K,chi)).

NC5 (PROVED_DERIVED, refereed once): a Galois-compatible map from CH-branch values to E(Q)(x)Q_5 is zero on them. A
non-equivariant or untwisting identification is NOT excluded.

### 3d. Retained checkers at the instance level, and reverse constraints

Instance-level PASS, each an equivalent reformulation of Sha[5] = 0, not independent evidence:
- Prop K transferred, with a two-prime unit Kurihara witness at n = 4681 (the smallest) or 5611 = 31*181;
  delta^(1)_5611 != 0 <=> Sha[5] = 0;
- Kato primitivity, ord kappa^(1) = 1;
- MR residual Stark at (31,181);
- LI5;
- the bridge kernels and the fixed-prime identity.

The Kummer leg of Prop K(e) is CONDITIONAL on Choice 5.2.1. That is the same R1-R3 as in 3a.

Reverse constraints (PROVED_DERIVED/PROVED; unconditional at the seed, Sha is not needed):
- r5 >= 1 and b >= 1;
- 1 <= r5 <= min(6, 2+c);
- max(1, c-3) <= b <= c+2;
- max(0, 4-c) <= r5d <= 5;
- at l = 31 and 181: r_{5,l} >= 2, rho_l >= 1, b_l <= min(b-1, 1+c).

Theorem NB: no upper bound on c, b, b_l or b_S follows from Sigma + Sha = 0.

Exact relative form: Sha[5] = 0 <=> w(H^1(Q,E[5])) ∩ B_ur^theta = <w delta P1>. c = dim Cl(L)[5]^chi is OPEN.

### 3e. What the calibration pins

Under the terminal equivalence (Castella Thm A with kappa != 0: kappa Kummer <=> rank 2 <=> Sha[5^inf] finite), every item
above is deduced FROM N1 + N11. It is a calibration, not a mechanism.

What it pins:
1. The exact target that any H9-type construction must hit at the seed: the line Q_5(P1 - tP2), with fingerprint c_k.
2. The support rank of that target is 2 (NC2).
3. The sealed tower's CH-branch output misses it by a vanishing eta_K component (NC5).
4. The class-group side is not forced by Sha = 0 beyond the relative form.

What it does not pin: lambda, c, analytic rank = 2, or anything outside p = 5 and the seed.

## 4. PROPOSED ledger block (NOT MERGED; awaiting operator acceptance; do not copy into the ledger without review)

```
## SEED_2243_12_LANE1_H9_CALIBRATION — ACCEPTED BY OPERATOR, MERGE PENDING MANIFEST (2026-09-18; synthesis ~/SEED_2243_12_MECHANISM_LANES_2026-09-18/00_LANE1_SYNTHESIS.md; manifest 00_LANE1_SYNTHESIS.MANIFEST.sha256)
LANE1_H9 = CALIBRATION_COMPLETE; CURRENT_SEALED_BRANCH_MISSES_TARGET
  (4 lanes, each hostile-verified PASS_WITH_CORRECTIONS; Castella explicit-instance completion gated by R1-R3)
  CALIBRATION, NOT MECHANISM: identification of the H9 terminal target uses the proved seed arithmetic N1 + N11. Auxiliary
    splitting computations and the NC5 tower-vanishing result are independent structural results, but neither supplies a new
    route to Sha[5^inf] = 0. G-WSHA fails.
  H9 CONSEQUENCE: known strict line != current CH-branch tower output (NC5: that output has zero E(Q)-component at every finite
    level). Do not try to prove that the existing same-root/CH branch equals the target. Surviving H9 work must name an operation
    that changes branch, support or eigenspace so that the known line can appear (untwisting, a different branch, a
    non-equivariant identification, or a different specialization mechanism).
  STRICT LINE (CERTIFIED_COMPUTATION, >= 5 implementations): Sel_str(Q,V_5E) = Q_5(P1 - tP2), t = log_5P1/log_5P2,
    v_5(log P1) = 2, v_5(log P2) = 1, v_5(t) = 1, loc_5 = (0,2) mod 5; fingerprint -t mod 5^6 = 13320.
  CASTELLA THM A (L1A): all printed hypotheses hold at p = 5 (q in {3,2243,5843}); kappa_5(E) spans the strict line
    CONDITIONAL on (R1) L(E^K,1) != 0 for one admissible K [explicit candidates D = -79 (q=3), D = -119 (q=2243), splitting and
    w(E^K) = +1 certified; L-value not computed], (R2) chi existence via Vat03/CH18 Thm D, (R3) seam 1: Assumption (A) at
    non-squarefree N+ (BD05 needs 5 not | deg phi_E; PW11 NOT_APPLICABLE; KPW17, SU14/Wan15, Thm 4.1.1, BSV22b Cor 8.2 unaudited).
    Printed BFH90 does not give "q inert" (verifier); explicit K bypasses the existence citation.
  CASTELLA-HSIEH COR B (L1B): no printed hypothesis fails at K = Q(sqrt-271); remaining: L(E^{-271},1) != 0 (~16 CPU-h est.,
    BLOCKED at cap) and the BLV Thm A / BD05 substitution. Sel(K,V_5E(x)chi^2) = 0: author OPEN; verifier cites Nekovar 2012
    CJM Thm A; PENDING G3 re-referee, not treated as final. CH15 Thm 1 NOT_APPLICABLE at (CR+)(1), p = 5.
  SEALED TOWER (L1C): NOT_ADMITTED, first failing gate G-MECH. First open A1.3; first BLOCKED A1.4; A2.3, A3.2 BLOCKED.
    NC5 (PROVED_DERIVED, one referee): CH-branch E-projected values are eta_K-eigen; E(Q)-component 0 at every finite level.
    Component vanishing only; no impossibility claim.
  CHECKERS (L1D): Selmer side instance-level PASS (Prop K transfer, Kurihara witness 5611 and 4681, MR (31,181), LI5 PROVED,
    Kato primitivity). Class-group side: unconditional region r5 >= 1, b >= 1, max(1,c-3) <= b <= c+2; Theorem NB: no upper
    bound on c from the recorded relations + Sha = 0. c = dim Cl(L)[5]^chi OPEN.
  NON-CLAIMS: no mechanism; lambda not computed; no L(E^K,1) or L(E/K,chi,1) certified; no explicit chi; Castella's class = CH's
    class OPEN; analytic rank 2 not certified; nothing for p != 5 or other family members; no seal defect claimed; H9 not claimed
    impossible.
  GATE ORDER (operator): G2 seam-1 audit -> G3 Nekovar re-referee -> G1 L(E^{-79},1) != 0 (timing prefix first; certify only if
    G2 and the chi-existence chain survive and the measured cost is reasonable).
```

## 5. Next Lane-1 gates

The operator re-ordered these to **G2 → G3 → G1**; see OPERATOR REVIEW. The list below is the synthesis agent's original ranking.

1. **G1: L(E^K,1) != 0 at D = -79** (q = 3, 5 split). This single value discharges R1 for Castella and supplies an explicit K.
   - Cheapest first test: a low-precision run of the N7 streaming code on the twisted minus-symbol series at D = -79. First
     measure CPU time on a short prefix, then extrapolate (no full run).
   - Exclusion: if L(E^{-79},1) = 0 (certified), switch to D = -119, then -311. A zero here says nothing against Castella.
   - Resources: roughly 5 CPU-h total (unmeasured scaling from N7's 5.645 CPU-h). This exceeds the 45 CPU-min cap and needs
     operator authorization. The prefix timing needs about 5 CPU-min.
2. **G2: seam 1 audit (R3), literature only.**
   - Target: whether Thm 4.2.1's inputs (BD05 Assumption 6, KPW17, SU14/Wan15, Thm 4.1.1, BSV22b Cor 8.2) hold at the
     non-squarefree N+.
   - Cheapest first test: read BD05 Assumption 6.3 and check whether any printed bound gives 5 ∤ deg phi_E (e.g. congruence
     primes vs. 5 ∤ product of Tamagawa numbers, with rhobar surjective). A clean "5 ∤ deg phi" would also admit -79 on the
     CH route.
   - Exclusion: some primary requires squarefree N+ and has no substitute. Record NOT_APPLICABLE at that hypothesis, not
     "impossible".
   - Resources: 0 CPU; about 1-2 h of reading.
3. **G3: re-referee of the L1B verifier's Nekovar 2012 finding (B-C7).**
   - Cheapest first test: re-read Nekovar CJM 64 Thm A (l.241-256) and 0.12 (l.362-380) in
     `L1B_CH_COR_B/VERIFY/sources/Nekovar2012_CJM.txt`. Check (A1)-(A3), the Bloch-Kato vs CH Selmer identification, and the
     case of ring-class chi of l-power conductor with l split.
   - Exclusion: a hypothesis excludes this chi or p = 5. Then S7 reverts to OPEN.
   - Resources: 0 CPU; about 30 min.
4. **G4 (optional, falsifiable): modular-symbol delta_n mod 5** at n = 4681, 5611 (predicted nonzero) and 58001 (predicted
   zero).
   - Cheapest first test: n = 4681 only.
   - Exclusion: a mismatch refutes the L1D transfer.
   - Resources: level 6.5e15 modular symbols are probably infeasible under the cap. Estimate the cost before launching.

## 6. Open author/verifier disagreements

- D1 (L1B C7): the author says OPEN, with no printed source for Sel(K,V_5E(x)chi^2) = 0 at p = 5. The verifier says REFUTED:
  Nekovar 2012 CJM Thm A applies, which gives VERIFIED_FROM_SOURCE. It has not been re-refereed; see gate G3.
- D2 (L1B C4): the author says BD05 is NOT_APPLICABLE (squarefree N). The verifier says BD05 has no squarefree hypothesis and
  is CONDITIONAL(on 5 ∤ deg phi_E). The correction is applied in §2, but the author has not acknowledged it.
- D3 (L1A first open statement): the author asks whether BFH90 allows "5 split". The verifier says that is not an issue: BFH90
  does not give "q inert", so a Friedberg-Hoffstein-type theorem is needed (UNVERIFIABLE_IN_CAP). The synthesis bypasses the
  issue with the explicit D = -79/-119, but R1 stays open.
- D4 (L1C C6/C7 wording): "W = S makes A2.3 unnecessary" and the "value 0" status line. These are wording corrections,
  applied in §2.
- D5 (L1C, verifier observation, not a lane claim): NC5 generalizes to any finite-order tame eps_g^(t). This sharpens the OPEN
  typing question between H17 08 §2.2 and REF2-C7 §1.
- D6 (L1D headline): the phrase "Sha = 0 implies nothing new on the class-group side" is scoped to Sigma, per the verifier.
- D7 (L1B C5): BLV l.375-376 says "p > 5" while its hypothesis lists say p >= 5, and the match between BLV's theta element and
  CH's is unverified. Nobody has resolved either.
- Cross-lane data note (not a disagreement): L1C's "first CH discriminants -119, -311, ..." use the Castella pattern with
  q = 2243. L1B's list (-79, -119, -271, ...) uses the CH pattern with any odd N^-. These are consistent (`runs/k119_output.txt`).

## 7. Other-lane outputs left by the stopped duplicate run (UNVERIFIED; listed only, not evaluated)

- Complete lane directories: L2A_REGULATOR_CONGRUENCE, L2B_A2_EQUIVALENCE (has VERIFY/), L2D_LITERATURE_NOVELTY (has VERIFY/),
  L5A_TRANSFER_FINITE, L5B_TRANSFER_ARITHMETIC.
- Partial directories: L2C_DAG_UNIFORMITY, L3A_ANALYTIC_RANK, L3C_ELL_PRIMARY, L4A_MANIN_HOSTILE_RECON (src/ only),
  L4B_CERTIFICATE_AUDIT, L4C_FORMALIZATION.
- Cached structured returns in resume_args.pre_stop.json: L2A, L2B, L2D, L5A, L5B.
