# RESUME — DEFINITE_FIELD_GATE, 2026-09-22

## Why this folder exists
Backward seam trace found that the definite-theta branch never instantiated its quadratic field K. It says "choose a
fixed definite imaginary quadratic K" and all later IntegralAncestor / NormCoherence work assumed "the fixed definite
K" without filling the premise. D = -23 is NOT that field (all bad primes split => indefinite, rank E(K) = 3).

## Files
- `STAGE8_D7_CERTIFIED.md` — READ THIS FIRST. THE D=-7 CERTIFICATE IS OBTAINED.
                       L(E^-7,1) in [9.054319, 9.054421], zero excluded, margin 1.79e5 => analytic rank 0
                       => (GZK) rank E^-7(Q) = 0 AND Sha(E^-7/Q) finite => r^- = 0 AND d^- = 0.
                       Artifact: ~/BSD_TWIST_D7_CERTIFICATE_2026-09-22/ (13 files sealed).
                       DEFINITE_TWIST_RANK0 flips to CERTIFIED. (r+,r-) = (2,0) established.
                       Stage-7 enumeration reduces to its first row. Remaining input to A2a: [c_2] != 0.
- `STAGE7_A2A_ROUTE_LIVE.md` — minus-side obligation now discharged by stage 8. Stage 6 was TOO PESSIMISTIC. BD's derived heights run on the PRO-p
                       SELMER group S (which CONTAINS T_p Sha), not on Mordell-Weil - so sigma >= 2*max(s^+,s^-)
                       constrains the divisible part. d^+ = 0 comes FREE. A2a route is LIVE, not a wall.
                       *** THE HOLD ON THE D = -7 RUN IS WITHDRAWN - it is back on the critical path. ***
- `STAGE7_TAU_ENUMERATION.txt` — the configuration table showing exactly what the certificate kills.
- `STAGE6_A2_SPLIT.md` — sec 4 superseded by stage 7. BD Cor 3 PROMOTED TO PROVED (definite, good ordinary - the Annals 2005
                       Thm 1 setup is N^- odd, i.e. ours). Two stage-5 defects corrected: the kernel EQUALITY was
                       unearned (and the stage-5 check used a random, generically-full-rank A, hiding it); and
                       "m=4 independent of certifying r-=0" is WITHDRAWN (r- >= 4 gives ord >= 8, unexcluded).
                       A2 split into A2a/A2b. A2a = Sha(E/K)[p^inf] FINITE = the project's recurring wall.
- `STAGE6_CORRECTED_CHECK.txt` — degenerate-A kernel table and the r- tabulation.
- `STAGE5_A0_RESOLVED.md` — sec 2, 4, 6 corrected by stage 6. A0 RESOLVED = THETA_ORDER_2_FULL_ORDER_4, checked not assumed.
                           The "max-1" formula found in search is the INDEFINITE case; ours is definite so no -1.
                           Mechanism re-derived independently (block-antidiagonal height pairing => 2*max).
                           c_2 confirmed AT LINE LEVEL from BRANCH_THETA.md as the I^2/I^3 coeff of the stabilized
                           Gross-point theta = square-root object. A1/A2 rewritten at m=4; A3 (supersingular) new.
- `STAGE5_ORDER_CHECK.txt` — the pairing-rank verification table.
- `STAGE4_INTERFACE_A_SETUP.md` — sec 4 (A0) now resolved by stage 5. Two corrections accepted (Remark 1.4 cited for the wrong reason;
                           H^0 hypothesis at N^+ was omitted). H^0 SETTLED - costs zero primes. Divisibility test
                           logic checked: it needs TWO control inputs, not one. And the square-root normalization
                           gives a HARD PARITY CONSTRAINT: ord_T L_p = 2*ord_T calL_p is ALWAYS EVEN.
- `STAGE3_BLV_CORRECTION.md` — sec 4-5 corrected by stage 4. WITHDRAWS the stage-2 coverage verdict. BLV (arXiv 2306.17784,
                           Math. Ann. 395, 2026) covers split AND inert, ordinary AND supersingular, NON-CM.
                           Fixed-K coverage REOPENED. But the rank-2 leading term is NOT in BLV, and BLV's own
                           Remark 1.4 sets the trivial character apart - that is the first unproved theorem.
- `STAGE3_HYPOTHESIS_SIZES.txt` — anomalous-prime data and the (Ram) repair.
- `GATE_STAGE2_AUDIT.md` — SUPERSEDED IN PART (sec 2-3). Conditions 4 & 5 audited at source. h(-7)=1 caveat RETIRED.
                           BLOCKER FOUND and it is not D: the invoked theorem requires p SPLIT in K, density 1/2,
                           so any FIXED K leaves an INFINITE inert gap => no FIN. Same covering wall as TASK.md Q2.
- `STAGE2_COVERAGE.txt`  — raw coverage numbers and the (Ram) verification.
- `GATE_STAGE1.md`     — the gate report. Stage 1 = congruence + root number. Read this first.
- `SEARCH_OUTPUT.txt`  — raw enumeration of admissible D per N^- branch.
- `STAGE1_DETAIL.txt`  — raw root numbers, class numbers, corpus headroom.

## Settled in stage 1
- N^- must be an odd-size subset of {3, 2243, 5843}. (2 has v=3, 4547 has v=2 => neither can be in N^-.)
  Derived from the conductor, not taken on trust from the Aristotle record.
- Admissible D per branch (first, smallest):
    N^- = {3}                -> D = -79, -319, -1255, ...
    N^- = {2243}             -> D = -119, -311, -551, ...
    N^- = {5843}             -> D = -167, -215, -287, ...
    N^- = {3,2243,5843}      -> D = -7, -103, -271, ...
- CONTROL: D = -23 admissible for NO definite N^-. Seam confirmed.
- ROOT NUMBER IS AUTOMATIC: chi_D(N) = (-1)^{|N^-|}, so |N^-| odd => w(E^D) = +1 for EVERY admissible D.
  So root number does not narrow the list; the user's "only test root-number +1 candidates" staging collapses.
- Best candidate D = -7: |D|*sqrt(N) = 5.6e8, 98x corpus headroom, full three-prime N^-.
  CAVEAT: h(-7) = 1, so Pic(O_K) trivial and the conductor-1 Gross point set is a single point. Check before adopting.
  Fallback on the same branch: D = -103 (h = 5).
- Corpus caps |D| around 500 (D = -271 already only 2.5x headroom).

## Settled in stage 2 (source audit)
- h(-7)=1 is NOT an obstruction. No class-number hypothesis; Gross points live on O_n = Z + p^n O_K whose class
  numbers grow; interpolation is stated from n >= max{1,s}. CAVEAT RETIRED. D = -7 stays the lead on cost.
- (Ram) VERIFIED for all p>=5: v_l(Delta) = 2,1,2 at l = 3,2243,5843, so rho-bar is ramified at every l|N.
- (Im) holds for all but finitely many p (Serre, non-CM). Finite exception - fine.
- [WITHDRAWN in stage 3 - true of Chan-Ho Kim's theorem only, not of the branch]
  BLOCKER: the theorem requires **p SPLIT in K**. Density 1/2. For D=-7 over 5<p<200000: 8970 split / 9008 inert.
  ANY fixed K leaves an infinite inert set => NO FIN. This is not a defect of D=-7; it holds for every K.
  It is the TASK.md Q2 covering wall arriving through a different door (r fields leave density 2^-r > 0).
- Dominant gap is now INERT-IN-K (density 1/2), not supersingular (density 0).
- Scope: inert-prime theories DO exist (Kobayashi-Ota, BHKO Thm 1.3(b)) but in the CM setting. phi_E is non-CM.
  UNSUPPLIED, not proved impossible.   <-- FALSE AS OF 2026. See stage 3: BLV and BBL supply the non-CM case.

## Settled in stage 3 (BLV source audit)
- BLV Hyp 1.1: p>=5, p ∤ N, p ∤ h_K, p ∤ disc(K), rho-bar SURJECTIVE, N^- squarefree, anomalous condition.
  p SPLIT OR INERT; ordinary OR supersingular. Thm A: (L_p^eps) subset (Char^eps), EQUALITY except one case.
  Def 1.3 exceptional = supersingular AND inert AND eps = +. One divisibility there only.
- Surjectivity FORCES non-CM => BLV is built for our kind of curve. (Burungale-He program is CM-only; inverted.)
- p ∤ h_K is VACUOUS for D = -7 since h(-7)=1. The class-number-one property is an ASSET for BLV, not a defect.
  Stage 1 read it backwards. D = -7 strengthens as the lead.
- ANSWER TO Q3: the rank-2 leading term is NOT in BLV. No derived heights, no I^2/I^3, no vanishing-L trivial
  character. BLV Remark 1.4: "The presence of a local zero in the exceptional case prevents us to treat the trivial
  character on the same ground as the other characters." OUR PROBLEM IS EXACTLY THERE (ord L(E/K,s)=2 => L(E/K,1)=0).
  => BLV_RANK2_LEADING_TERM is the FIRST UNPROVED THEOREM, not the coverage issue.
  [STAGE 4: verdict stands, but the REASON is corrected. Remark 1.4 is about the EXCEPTIONAL local zero only;
   BLV say n=0 IS accessible in the non-exceptional setting. The correct reason is simply that no higher-order
   augmentation / derived leading-term formula is stated.]
- REPAIR 1: "a_p != +-1 expected finite" WITHDRAWN. Lang-Trotter predicts INFINITELY many (density 0); unproved
  both ways. Measured: NO prime 5 <= p < 30000 has a_p = +-1 for this curve. Hypothesis is case-dependent:
  split p needs only a_p != 1, so a_p = -1 at a split prime is permitted.
- REPAIR 2b (stage 4): BLV Hyp 1.1 ALSO requires H^0(G_{Q_q}, E[p]) = 0 for q | N^+. For D=-7, N^+ = 2^3*4547^2.
  SETTLED: both places additive with j integral => formal group pro-q, E_0/E_1 = (F_q,+) a q-group, and c_q <= 4 for
  every additive Kodaira type. So E(Q_q)[p] = 0 for ALL p >= 5. ZERO primes excluded. (No PARI on host; the c_q <= 4
  bound holds for every additive type so the exact Kodaira type is not needed.)
- REPAIR 2: (Ram) completed. j integral at 2 and 4547 => potentially GOOD there => inertia order e | 24 =>
  p >= 5 gives p ∤ 24 => rho-bar ramified. Now covers ALL l | N, not just the multiplicative ones.
- FLAGGED NOT CONFIRMED: in the exceptional case (L_p) subset (Char) means Char | L_p, which BOUNDS Selmer ABOVE -
  plausibly the direction we want, so the exceptional case may cost sharpness not applicability. Check at source.

## NOT settled
- rank E^D(Q) = 0 for any candidate. NO LONGER THE BLOCKING ITEM - see above.
- Normalization conventions of H1 (shape matches; conventions unaudited; moot for the tail).
- FINITE_LAYER_NONVANISHING - still the open main term.

## Stage 2 feasibility (NOT run)
- L(E^D,1) uses the exp weight, NOT the E_1 weight the D=-23 derivative needed => strictly cheaper than a run that
  already succeeded on this host at ~1 GB.
- Stage W corpus is D-INDEPENDENT and already paid (T = 5.5046e10). chi_D is a table.
- DO NOT pick a cutoff in advance. Adequacy is undetermined until the truncated interval exists (D=-23 lesson).
- Table-free traversal ONLY. Dense path is 4*T bytes = 26 GiB at T=7e9 on a 16 GiB host.

## Hard constraints still in force
- Master handoff ~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/ read-only; untouched.
- No novelty claim, no FIN/BSD claim. Do not run p = 17. No email without explicit permission.
- Nothing certified here. No engine launched.

## [STAGE 8: DONE. Certificate obtained, see STAGE8_D7_CERTIFIED.md]
## RECOMMENDATION [REVERSED IN STAGE 7]: RUN L(E^-7,1). The hold is WITHDRAWN.
tau-structure forces d^+ = 0 for free, but leaves d^- in {0,1,2}. ONLY the certificate removes those rows:
L(E^-7,1) != 0 => GZK at analytic rank 0 => rank E^-7(Q) = 0 AND #Sha(E^-7/Q) < inf => r^- = 0 AND d^- = 0.
Nothing else in the route supplies d^- = 0. Cost unchanged from stage 1: exp weight (not E_1), |D|*sqrt(N) = 5.65e8,
98x corpus headroom, stage W already paid. Cutoff FROM the computed interval, never in advance. Table-free only.
[superseded] The blocker is the rank-2 leading-term arrow, NOT coverage. DO NOT vary K yet.

## THE LIVE TEST (stage 4) - interface A, and A0 comes first
BLV Thm A gives F_p | L_p (Euler-system direction, bounds the algebraic side ABOVE). If the witness gives
ord_T L_p = m with unit normalized leading coefficient, and control forces ord_T F_p >= m, then both leading
coefficients are units. Logic checked and sound. BUT it needs TWO control inputs:
   A1 [STAGE 7: DISSOLVED AT ORDINARY p]. BLV's exceptional case is supersingular+inert+eps=+, so at ordinary p
      Theorem A gives EQUALITY (L_p) = (Char_p). Hence [c_2] != 0 => sigma = 4 with unit leading coeff, directly.
      What remains of A1 is MODULE IDENTIFICATION: is BLV's Char_p(f) the characteristic ideal of the SAME X_inf
      (same local conditions) that BD's derived-height theorem applies to?
   A1 (stage-5 wording): does the BLV/BD characteristic object satisfy ord_I F_p >= 4 under (r+,r-) = (2,0)?
   A2 [SPLIT IN STAGE 6 into A2a + A2b - see above]
   A2 (stage-5 wording): if the normalized I^4/I^5 coefficient is a unit, does Sha(E/K)[p^inf] = 0 follow?
      CRITICAL: with r- = 0 the anticyclotomic height pairing is IDENTICALLY ZERO and |r+ - r-| = 2 > 1, so the
      STANDARD regulator vanishes. The leading term carries a DERIVED regulator (hp^(k)). Source-confirmed.
      Must be in A2's wording, not discovered mid-audit.
   A3 (NEW): the supersingular analogue. BD Cor 3 is good-ordinary; the tail needs ALL p. No established
      augmentation order on the signed side. Do NOT transplant m=4 there.
A0 IS RESOLVED (stage 5): THETA_ORDER_2_FULL_ORDER_4. ord_I calL_p >= 2, ord_I L_p >= 4. Reading 2 RETIRED.
   Driver is the rank DISTRIBUTION (r+,r-) = (2,0), not generic "rank two": ord = 2*max(r+,r-), and the extra
   vanishing over the complex order (= r+ + r- = 2) is |r+ - r-| = 2.
   ROBUSTNESS [CORRECTED IN STAGE 6]: m = 4 holds iff r- <= 2. w(E^-7)=+1 gives only r- in {0,2,4,...} and
   r- = 4 would give ord_I L_p >= 8. The correct claim is "independent of DISTINGUISHING r- = 0 from r- = 2",
   NOT "independent of certifying r- = 0". r- >= 4 is unexcluded by anything in the project record.
   REVERSAL (holds): proving [c_2] != 0 forces 2*max(2,r-) <= 4, hence r- <= 2, for free at ordinary p.
   [superseded detail] BLV set L_p = calL_p * calL_p^iota. iota sends T -> -T/(1+T), preserves I, preserves ord.
   => ord_T L_p = 2 * ord_T calL_p, ALWAYS EVEN. And leading coeff of L_p = +-(leading coeff of calL_p)^2.
   (a) ORDER IS AMBIGUOUS AND THE READINGS ARE MUTUALLY EXCLUSIVE: BRANCH_THETA manipulates theta_n = the
       square-root side. If c_2 is the I^2/I^3 coefficient of calL_p then m = 4, NOT 2. If instead rank two pins
       ord_T L_p = 2 then ord_T calL_p = 1 and the witness belongs in I/I^2 of theta. Parity is a hard check:
       ord_T L_p can never be odd.
   (b) THE UNIT CONDITION IS ROBUST: unit leading coeff transfers between calL_p and L_p either way.
       So A0 must be resolved to know WHICH m to prove, but not to know that the unit property carries.

## NOT VERIFIED (do not record as proved)
- [RESOLVED IN STAGE 6] BD Corollary 3 is now source-backed: Annals 2005 Thm 1 assumes N^- squarefree with an ODD
  number of prime factors (the DEFINITE case, ours); with delta^± = 0 at good ordinary p, Cor 3 gives
  ord_I L_p >= 2*max(r+,r-). PROMOTED TO PROVED.
- [STAGE 8: rank E^{-7}(Q) = 0 is now CERTIFIED. Line below is historical.]
- rank E^{-7}(Q) = 0 still uncertified. Affects the order (r- <= 2), A2's regulator, AND (stage 7) A2a's minus side.
- MW-RANK PARITY FROM THE SIGN IS WITHDRAWN (stage 7): w(E^-7) = +1 gives ANALYTIC rank even, NOT Mordell-Weil rank
  even. Earlier files (stage 1 sec3, stage 6 sec3) used it for algebraic rank. That needs a parity theorem with its
  own hypotheses, not installed here. Harmless for the route (GZK gives rank 0 from L != 0) but do not reuse.
- BD Thms 2.7 / 2.18 / 2.23 and Remark 2.21 NOT read at source; characterization accepted as given.
- The whole A2a route is CONDITIONAL ON [c_2] != 0. A2a is not eliminated, it is REDUCED to
  [c_2] != 0 + the D=-7 certificate + module identification.
- KERNEL DIMENSION: only the INEQUALITY dim ker >= |r+ - r-| is justified. Equality needs A of maximal rank.

## [STAGE 7: THE HEADING BELOW IS SUPERSEDED - A2a IS A LIVE ROUTE, NOT A WALL]
## A2 IS SPLIT, AND A2a IS THE WALL
BD Derived p-adic heights Thm 2.23: leading coeff ~ [Sha[p^inf] / Div Sha[p^inf]] x R_der.
So a unit leading coefficient gives Sha[p^inf] = Div Sha[p^inf], i.e. (Q_p/Z_p)^d - NOT Sha = 0.
  A2a control/eliminate the divisible part   <- LOAD-BEARING
  A2b control v_p(R_der)
DEMONSTRATION that A2a does not follow: X_inf ~ (+)_i Lambda/(f_i); control gives corank Sel(K) = #{i : T|f_i}
  = 2 + d, and ord_I F_p = sum ord_T f_i. Four factors each with ord_T = 1 and unit leading coeff give
  ord_I F_p = 4, unit normalized coefficient, AND d = 2. So corank Sha = 2 is CONSISTENT with everything A1 gives.
A2a == "Sha(E/K)[p^inf] is finite". At analytic rank 2 there is no known source. This is exactly what Keller named
  (rank 1: finiteness comes from the finite Heegner index; no rank-2 analogue) and the project has recorded
  "wall = Sha finiteness" before (H9R19).
PROMPT REQUIREMENT: A2a must be named load-bearing and explicitly forbidden as an assumption. "Without assuming FIN"
  is NOT sufficient - A2a is weaker than FIN and can be assumed without appearing to assume FIN.
LEAD (not a claim): ord_I L_p = 4 < inf gives L_p != 0, so BLV Thm A's F_p | L_p forces F_p != 0, i.e. X_inf is
  Lambda-torsion. Whether Lambda-torsion + control gives d = 0 is the thing to check; the module computation above
  shows it does NOT follow from order + unit coefficient alone.

## Interface B (moot unless A closes)
a_p = +-1 ordinary primes: conjecturally infinite (Lang-Trotter), unproved both ways, none below 30000 here.

[Private-correspondence paragraph omitted from public export; no mathematical certification is inferred from correspondence.]