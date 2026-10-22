# 08 — Program status freeze after H9R19 (operator, 2026-09-15) — ROUTE SUPERSESSION

```
H9R16C_POINT_TOWER = SEALED
H_PI = PROVED

H9R18_WEIGHTED_BIG_TRACE =
    PROVED_CONDITIONAL_FOR_THE_BCPV_DIAGONAL_CLASS

H9R19_WEIGHTED_RECIPROCITY =
    PROVED_BY_RECONSTRUCTION
    CONDITIONAL_ON_TF_W-CRIS_AND_EXACT_SCALAR_SEAMS

BCPV_AD_Tg_TRACE_ROUTE_TO_LIVE_CH_CLASS =
    CLOSED / WRONG_REFINED_BRANCH

BCPV_DIAGONAL_WEIGHT_ONE_SPECIALIZATION =
    SAME_ROOT_CLASS
    = kappa_{alpha,beta^{-1}}
    = 0

LIVE_CH_TARGET =
    kappa_{alpha,alpha^{-1}}
    = kappa(f,g_alpha,g_beta)

FIRST_PROGRAMMATIC_OPEN_STATEMENT =
    RETARGET_THE_GEOMETRIC_CONSTRUCTION_FROM_THE_BCPV
    SAME-BRANCH_DIAGONAL_TO_THE_ACTUAL_CH_CONJUGATE-BRANCH
    TRIPLE (f,g,h)

W-CRIS =
    REAL_BUT_SECONDARY_COMPLETION_TASK
```

Superseded route:   H9 point geometry -> (f,g,g^c) -> ad(g) trace -> L_p^g          [lands on the zero same-root specialization]
Prospective route:  H9 point geometry -> (f,g,h) conjugate-branch class -> kappa_{alpha,alpha^{-1}} -> CH f-dominant Coleman map -> Theta_{f/K}

H9R20 (next Pro-6 problem): can the sealed construction be retargeted from the literal diagonal lambda -> (lambda,lambda) on
(f,g,g^c) to the conjugate-branch graph lambda -> (lambda, iota_CM(lambda)) on (f,g,h) without losing the point-valued realization?
Fable's assignment: source-audit the exact Hida-weight-space involution relating the g and h branches and determine whether
the H9R16 modified pairing survives along its graph.  -> see 09_BRANCH_INVOLUTION_AUDIT.md.
Internal-only caution: DR22 indexing/convention seams ([bc,ac,ab] vs [a,b,c]; one-orbit factor 2) affect exact normalization,
not the gate-B branch obstruction.

## Supersession of one line above (operator, after 09)
"RETARGET_THE_GEOMETRIC_CONSTRUCTION" was too broad. Precise form:
    CYCLE/COHOMOLOGY TOWER RETARGETS TO (f,g,h)   [change of Hecke projection only; CH p.21]
    H9R16 POINT TOWER DOES NOT                    [modified pairing is a same-sheet self-pairing; zero across sheets]
Map: line I = actual point tower, zero target | line III = live target, generically non-Selmer/non-Kummer |
     line IV = live target + possible Selmer route; the p_frak-singular component is the kill gate (Q1), then Q2, Q3.

## H9R20 freeze (operator, 2026-09-16)
```
H9R20_Q1_LINE_IV_SINGULAR = PROVED_IDENTICALLY_ZERO
H9R20_Q2_PRINTED_LAW      = PROVED
    BSV_THEOREM_A_f_DOMINANT + BSV_PROP_7_3 + CH_THM_4_1
LINE_IV_LOCAL_STATUS      = STRICT_SELMER_CONDITION_PROVED
LINE_IV_FAMILY_STATUS     = SELMER_FAMILY_PROVED / POINT_FAMILY_NOT_PROVED
H9R20_Q3                  = OPEN
CH_COR_5_1_SHORTCUT       = UNAVAILABLE (needs V_p Sha(E/Q) = 0)
REMAINING_STATEMENT       = q_Sha(kappa_{alpha,alpha^{-1}}) = 0
NEXT                      = H9R21 cross-sheet Kummer realization gate (Pro 6); Fable source audit = file 12
```

## H9R21 freeze (operator, 2026-09-16) — narrowed after Pro 6 / Fable reconciliation
```
H9R21_MODULAR_TOWER_AUDIT           = NEGATIVE: NO PRINTED CROSS-SHEET GEOMETRIC CONTRACTION;
                                      H9R16 SAME-SHEET POINT MECHANISM DOES NOT EXTEND
H9R21_TARGET_ARTIN_COEFFICIENT_MAP  = EXISTS IN BROADER MOTIVIC CATEGORY [Pro-6 result; awaiting H9R22 construction audit]
H9R21_CLASS_LEVEL_AJ_COMPARISON     = OPEN
KUMMER_REALIZATION                  = UNDECIDED
SHA_FINITE                          = REQUIRED BY PRINTED CH ROUTE; NOT LOGICALLY REQUIRED IF TARGET (TC) CONSTRUCTION EXISTS
FIRST_EXACT_OPEN_STATEMENT          = TARGET CROSS-SHEET CHOW–ABEL–JACOBI COMPARISON (TC): c_{0,*}(AJ(D_0) - z_0) = 0
NEXT                                = nothing launched; Pro 6 H9R22 target construction. Decisive checks on return: D_0 actually
                                      constructed (not only the coefficient map); construction outside the tower; exact (TC) proved;
                                      if mod-p^n, denominators bounded independently of n; K_g-linearity step (12 sec 6) refuted or avoided.
```

## H9R22 freeze (operator, 2026-09-16) and H9R23 source audit result (file 13)
```
H9R22_TARGET_ARTIN_CORRESPONDENCE  = EXPLICITLY_CONSTRUCTED
H9R22_TARGET_CHOW_AJ               = SOURCE_CONSTRUCTION_MISSING
H9R22_MODULAR_TOWER_SHEET_EXCHANGE = BLOCKED / NOT_REALIZED
H9R22_FINITE_CONGRUENCE_ROUTE      = COEFFICIENT_APPROXIMATION_PROVED; CHOW/KUMMER_CONGRUENCE OPEN
KUMMER_REALIZATION                 = UNDECIDED
SHA_FINITE_NEEDED                  = NO IF THE FINITE_CONGRUENCE ROUTE CLOSES
FIRST_EXACT_OPEN_STATEMENT         = UNIFORM CLASSICAL-APPROXIMATION CHOW/KUMMER CONGRUENCE THEOREM (H9R23)

H9R23_SOURCE_AUDIT (13)            = BLOCKED_AT_FIRST_OPERATION: the only Hecke-compatible algebraic contraction (polarization) kills
                                     the cross-newform approximants identically; the needed contraction is the chi^{-2} CM-twist
                                     correspondence M(g^o_{l_n}) -> M(h^o_{l_n}) over F = K_chi, algebraic at weight 2 only, a Tate-conjecture
                                     instance at the approximating weights l_n >= p. Integrality of everything else is controlled
                                     (eps_{r_n} avoidable via TSym). CORRECTION to 12: correspondences between different factors DO exist over F.
```

## H9R23 correction (operator, 2026-09-16; recorded in 13 sec 5 and 14 Correction)
```
H9R23_FIRST_FAILING_OPERATION      = RE-IDENTIFIED: the live contraction of the moving constituent Ind Psi^{1-c} (CH (4.4)) is not
                                     G_F-equivariant at any classical weight (defect (a/b-1, 0, 0, b/a-1), zero only at weight one).
                                     Every available algebraic contraction — polarization (13 sec 2(a)), chi^{-2} CM-twist composite
                                     (13 sec 2(d)), C_n-transported CM polarization (14) — hits the fixed constituent Ind chi^2, on which
                                     the CH class is zero (Lemma 4.5(1)). No algebraic correspondence over any number field induces the
                                     mod-p^n live functional (13 sec 5(iv)); lifting obstruction beta_n(sigma) = (rho_n(sigma)^{-1}-1)/p^n.
C_n_STATUS                         = NECESSARY, NOT SUFFICIENT. "Only missing piece" (14) withdrawn.
CHOW_LEVEL_REQUIRED                = NO (withdrawn): an algebraic representative of a homological correspondence suffices, D = Gamma_* Delta.
OPERATIVE_STATEMENT (verbatim)     = "The CM model exists; its modular-source comparison is unconstructed. But that comparison alone is
                                     not sufficient: polarization on the model contracts the complementary finite-character constituent.
                                     The live contraction must be matched explicitly after reduction, rather than inferred from the
                                     model's existence."
NEW_H9R_NUMBER                     = NONE; NO NEW LAUNCHES (operator).
```

## CONGRUENCE-LINKING GATE (operator spec 2026-09-16; file 19) — KILLED at step 2
```
TAME_HECKE_CONGRUENCE_ORDER = p^n (both approximants = theta_chi mod p^n away from p)
CONGRUENCE_MODULE          = killed by p^{d_0}, d_0 = v_p(alpha - beta) fixed; = 0 under p-distinguishedness
LIVE_FUNCTIONAL_MATCH      = NO
FIRST_DEFECT               = a_p(g_{l_n}) = alpha, a_p(h_{l_n}) = beta mod p^n: at p the approximants are the two different stabilizations
                             of theta_chi; T_p (level C) / U_p (ordinary part) bound the gluing depth by p^{d_0} uniformly in n.
```

## DERIVED-POINT GATE (operator architecture 2026-09-16; file 20) — KILLED at gate 1
```
GATE_1 (2-dim base containing C) = NO: sealed object is a T'_inf(N_g)-module with g/h collapsed at the carrier (01 sec 6) and a
                                   weight-2 Jacobian receptacle on the f-side; E-specialization itself is a sealed NON-CLAIM (05 l.41).
RIVERO_PREMISE                   = Prop 3.6 vanishing on C needs f split multiplicative (l.127-130): factor 1 - alpha_f^{-1}; nonzero for our E.
GATE_2                           = NOT RUN
```

## TERMINAL EQUIVALENCE for the live endpoint (2026-09-16; Castella, "Nonvanishing of generalised Kato classes and Iwasawa main
## conjectures", Theorem A, archived as lane file 22, l.88-102; Theorem 5.2.3 l.861-866)
Castella Thm A (E good ordinary at p > 3; E[p] absolutely irreducible; a prime q || N with E[p] ramified at q if q = +-1 mod p; p > 5 or
big image; w = +1, L(E,1) = 0): (1) kappa_p(E) != 0 => dim Sel(Q,V_pE) = 2; (2) if dim Sel = 2, kappa_p(E) != 0 iff loc_p != 0 on Sel,
and then kappa_p(E) spans ker(loc_p). Remark (2): kappa_p(E) = lambda (log_p(Q) P - log_p(P) Q) for ANY basis (P,Q) of Sel — a Selmer basis.
Corollary (two lines, no new input). Assume Thm A's hypotheses and kappa_p(E) != 0. Let M = Kum(E(Q) (x) Q_p) subset Sel, r = rank E(Q).
  r = 2: M = Sel (both 2-dimensional), so kappa_p(E) in M; and Sha(E/Q)[p^inf] is finite.
  r <= 1: loc_p is injective on M (a non-torsion rational point has nonzero formal-group logarithm), so M cap ker(loc_p) = 0 and
          kappa_p(E) = spanning vector of ker(loc_p) is NOT in M.
  Hence   q_Sha(kappa_{alpha,alpha^{-1}}) = 0   <=>   rank E(Q) = 2   <=>   Sha(E/Q)[p^inf] finite   (given dim Sel = 2).
Consequences.
  (a) The STRICT_LINE_POINT_CONSTRUCTION (a P in E(Q) (x) L with Kum(P) != 0, loc_p Kum(P) = 0) exists iff rank >= 2; constructing it IS
      constructing a second independent rational point. There is no cheaper form of the endpoint.
  (b) Every route killed in this lane (H9R17/18 same-sheet trace; line IV Q3; H9R21 cross-sheet; H9R23 approximants; CM model; congruence
      linking; derived point) failed at the step "p-adic or cohomological object -> rational point"; that step is (a).
  (c) No printed theorem proves Sha[p^inf] finite for any elliptic curve of rank >= 2. DR16 Conj 3.12 / BSV22a Conj 3.4 state the
      point-valuedness as conjecture; CH sec 5.7 assumes Sha finite; Castella's Remark (2) uses a SELMER basis.
  (d) Per-curve instances are decidable by descent: Sel_p(E/Q) of F_p-dimension 2 = rank forces Sha[p] = 0, hence Sha[p^inf] = 0, hence
      (Thm A(2)) kappa_p(E) != 0 and Kummer. This yields examples only, not the program's statement.
```
LIVE_ENDPOINT                     = q_Sha(kappa_{alpha,alpha^{-1}}) = 0
TERMINAL_EQUIVALENCE              = <=> rank E(Q) = 2 <=> Sha(E/Q)[p^inf] finite   (under Castella Thm A + kappa != 0)
ROUTE_WITH_PRINTED_INPUTS         = NONE
LANE_STATUS                       = CLOSED AT THE RANK-2 SHA-FINITENESS BOUNDARY (no new H9R number)
H9R16_C_BOUNDARY (must survive)   = one-direction same-sheet point tower in its Jacobian receptacle; g/h collapsed at the carrier;
                                    E(Q)-valued specialization NOT PROVED (sealed non-claim 05 l.41); not a two-variable E(Q)-valued family
```

## BRAUER-SPLITTING PROPOSAL (operator, 2026-09-16; file 23) — criterion verified, construction not startable
```
SPLITTING_CRITERION / EXTRACTION / WEAKER_PRECISION = VERIFIED (independent of CK numbering)
SOURCE_OF_u_sigma  = NONE (excision data -> target only via Hecke-module specialization + non-cycle contraction; neither acts on Div^0(E))
MOD_pN_DESCENT     = FAILS (H^1(G, Div^0/p^n) != 0)
EQUIVALENT_TO      = rank 2 / Sha[p^inf] finite (terminal block)
DISPOSITION        = RETAIN (16) AS CHECKER; NOT A CONSTRUCTION; lane status unchanged (CLOSED at the rank-2 Sha-finiteness boundary)
```

## WAY-FORWARD ASSESSMENT (2026-09-16, closing)
```
ROUTE_WITH_PRINTED_INPUTS   = NONE (terminal block; 23 sec D; Pro 6's plectic / mock-plectic / CM checks all negative)
NAME_OF_THE_WALL            = rank-2 converse to Gross–Zagier–Kolyvagin: Sel corank 2 => Mordell–Weil rank 2 (= Sha[p^inf] finite).
                              Known machinery produces points only from FIRST derivatives (Heegner, Chow–Heegner, p-adic GZ); every
                              rank-2 statement in print (DR16 Conj 3.12, Darmon–Fornea Conj 3.13, BSV22a Conj 3.4, CH sec 5.7, CM
                              second-derivative criteria) either assumes rank 2 / Sha finite or stops at Selmer corank.
EXECUTABLE_OUTPUTS          = (i) per-curve instances by p-descent (Sel_p of dim 2 => Sha[p]=0 => kappa Kummer): examples only;
                              (ii) the closed audits and the terminal equivalence as a handoff of closed statements. Nothing else.
RECOMMENDATION              = no further agent spend on this endpoint without a proposal that names its second point or its
                              second-derivative-to-point mechanism; kill at that question first.
```

## Correction to the terminal block, clause (c) (2026-09-16, whole-map audit 14 in ~/BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15)
"No printed theorem proves Sha[p^inf] finite for any elliptic curve of rank >= 2" is too strong as written. CH sec 6 (l.1462-1476) asserts,
citing Bertolini–Darmon [BD95, BD05, Cor. 3], that for their tabulated rank-2 instances (389a1 p=11 K=Q(sqrt-2); 433a1 11 -7; 446c1 7 -3;
563a1 5 -1; 643a1 5 -1; 571b1 5 -1; 1913a1 7 -3; 2027a1 13 -1; 1621a1 11 -2) exact-order-2 vanishing of Theta_{E/K} at T = 0 implies
Sha(E/K)[p^inf] finite, and then Cor B gives kappa_{alpha,alpha^{-1}} != 0 spanning Sel_str inside the 2-dimensional Selmer group. With rank 2
known, M = S and kappa is Kummer for those instances: an instance-level printed route, through a per-curve p-adic computation (Brandt
modules). Corrected clause: no printed UNIFORM theorem; the instance criterion exists and is p-adic-analytic. BD05 Cor 3 not verified here.
The uniform conclusion (LANE CLOSED at the rank-2 Sha-finiteness boundary; no route with printed inputs) is unchanged.

## ARITHMETIC GATE AUDIT (Pro note relayed by operator, 2026-09-16; audit = file 26; source = file 25) — read-only; no new H9R number; nothing built
```
PRO_NOTE_VERDICT              = CONFIRMED, secs 1-7 (Castella Thm A verbatim at 22 l.88-102). Most of it restates this ledger: terminal block,
                                clause (d), Castella Remark (2), gate 19.
NEW_AND_ADOPTED               = support-rank test (note Cor 3.2) as G-SUPPORT; auxiliary-class proportionality (note sec 4) as G-AUX;
                                finite theta-coefficient lemma (note sec 7); analytic rank is only >= 2 under Castella's hypotheses
SUPERSESSION (label only)     = WAY-FORWARD "NAME_OF_THE_WALL = rank-2 converse to Gross–Zagier–Kolyvagin" is a misnomer. Corrected:
                                SELMER-CORANK-2 SHA FINITENESS: dim Sel(Q,V_pE) = 2 => rank E(Q) = 2 (<=> Sha(E/Q)[p^inf] finite); purely
                                algebraic. Castella–Hsieh's own names (arXiv l.185-189): Cor B = rank-2 analogue of Skinner's converse,
                                Cor C = rank-2 analogue of Kolyvagin. The wall is neither.
CHAT_SLIPS_WITHDRAWN          = "no unconditional method for any family" (unsupported; never in this ledger); "v_2(alpha - beta)" (19 and
                                this ledger use v_p)
DESCENDED_OUTPUT_IN_E(Q)(x)Q_p = NOT DEFINED (sealed non-claim, milestone 05 l.41)
SUPPORT_RANK_TEST             = NO INPUT on the sealed tower; same-root branch output = 0; no new strict-localization obstruction recorded
KAPPA_AT_INSTANCE_LEVEL       = DOWNSTREAM. Every printed kappa != 0 criterion consumes or implies dim Sel <= 2 (CH Thm A; Cor B; sec 6 and
                                published Thm B, where exact theta order 2 gives dim Sel <= 2 through 2rho >= sum i e_i with odd layers zero;
                                Castella Thm A(2)). That bound plus two independent points gives W = S without kappa.
KAPPA_FREE_CERTIFICATE        = PRINTED: Stein–Wuthrich Thm 6.1 with Kato's Thm 7.3/7.4: two independent points + ord_T L_p <= 2 =>
                                Sha(E/Q)(p) finite. SW Thm 1.1: Sha(E/Q)[p] = 0 for 1,534,422 pairs, rank >= 2, conductor <= 30000, 5 <= p < 1000.
EXECUTABLE_OUTPUTS (amended)  = (i) p-descent; (ii) cyclotomic Iwasawa (SW); (iii) anticyclotomic theta order (CH sec 6). All instance-level,
                                all kappa-free.
ADMISSION_GATE                = G-DATUM, G-MECH, G-REUSE, G-SUPPORT, G-AUX, G-CYC, G-TEST (26 sec 3); replaces the chat-only
                                "say where the second point comes from"; the WAY-FORWARD recommendation stays compatible
QUANTIFIER_CHOICE             = UNIVERSAL target retained; NEW_ARITHMETIC_SOURCE_SELECTED = NONE ADMISSIBLE; BUILD = NONE.
                                BENCHMARK and NARROWER FAMILY are excluded by name under the operator's $1M-only rule 3. BENCHMARK adds no
                                arithmetic. FAMILY, if overridden, needs a NEW uniform Selmer bound; first failure test = a positive-dimensional
                                constant-E[p] family with two independent sections; NOT RUN; NOT A CANDIDATE.
LANE_STATUS                   = UNCHANGED: CLOSED AT THE RANK-2 (SELMER-CORANK-2) SHA-FINITENESS BOUNDARY
```

## COEFFICIENT GATE + SCOPE CORRECTIONS (Pro response relayed by operator, 2026-09-16; check = file 31; source = file 28) — read-only; nothing built
```
COEFFICIENT_LEMMA             = CONFIRMED: for E/Q non-CM, log_p is injective on (E(Q)/tors) (x) (Q̄ ∩ Q_p) — Fuchs–Pham arXiv:1412.1248v2
                                Thm 2.2 (page images checked: statements over Q̄), resting on the p-adic analytic subgroup theorem
                                (their Thm 1.1 = arXiv:1502.00768 Thm 2.2, published 2015)
H9_CONSEQUENCE                = no nonzero strict class is a finite algebraic-over-Q coefficient vector in a rational Mordell–Weil basis,
                                even up to a common p-adic scalar; log_p(Q)/log_p(P) transcendental. NOT closed under p-adic limits; does
                                NOT cover p-adic coefficient fields (e.g. L of CH l.702, residue fields F_g of Hida families)
ANNOTATION_TO_TERMINAL_(a)    = the STRICT_LINE_POINT_CONSTRUCTION needs a p-adic coefficient field L; with L algebraic over Q it never exists
SCOPE_CORRECTIONS             = file 31 SC1-SC6 ACCEPTED (status words; certificate redundancy scoped to inspected criteria, no cost claim;
                                file 26 closing sentence replaced; wall label scoped to Castella Thm A hypotheses + kappa != 0; SW dating;
                                admission gate)
ADMISSION_GATE                = G-DATUM, G-MECH, G-REUSE, G-SUPPORT, G-AUX, G-WSHA, G-COEFF, G-TEST
STATUS_WORDS (supersede every "LANE CLOSED" / "LANE_STATUS = CLOSED" line of this ledger):
    CURRENT_H9_CONSTRUCTION      = STOPPED AT ITS RECORDED BOUNDARY
    UNIFORM_H9_ARITHMETIC_TARGET = OPEN
    NEW_ADMITTED_MECHANISM       = NONE IDENTIFIED
BUILD                         = NONE; H41 untouched; no sealed statement changes
```

## NEW-MECHANISM KILL GATES A, B, C (operator order 2026-09-16; file 32; sources 33-35) — kill-first; nothing built
```
GATE_A (Castella–Do relaxed/strict machinery -> V_p Sha)  = KILLED. arXiv:2303.06751v2 bounds (ord,ord)/(rel,str) Selmer groups (Thms A-C,
                                                            6.6.1); no Sha, Chow or Mordell–Weil comparison anywhere in the text; in
                                                            the H9 regime V_p Sha = 0 is equivalent to kappa in W, so an exact
                                                            comparison would prove the H9 target
GATE_B (rank-two Kolyvagin/Stark systems)                  = KILLED. Rubin–Mazur Thm 10: kappa_n in |Sel(T*,n)| wedge^r Sel(T,n) —
                                                            Selmer outputs only; every positive-core-rank structure for T_pE has a dual
                                                            strict at p containing kappa != 0, so the p-adic bottom datum is ZERO in the
                                                            H9 regime (same argument: Kato's bottom class vanishes); derived data reach
                                                            L-values only via Burns–Kurihara–Sano's conjecture
GATE_C (families, universality relaxed)                    = p = 2 ALREADY PROVED: Zywina arXiv:2502.01957 (2025) — infinitely many curves
                                                            with E(Q) = Z/2 x Z^2 and Sha[2] = 0 (2-isogeny descent + Tao–Ziegler);
                                                            mechanism needs rational 2-torsion and integral singular fibres, so it cannot
                                                            run at p > 3 with E[p] irreducible. p >= 5: NOT STARTABLE (no uniform
                                                            mechanism; e.g. rational-5-torsion family has discriminant t^5(t^2-11t-1))
SURVIVING_MECHANISM                                        = NONE
CURRENT_H9_CONSTRUCTION                                    = STOPPED AT ITS RECORDED BOUNDARY
UNIFORM_H9_ARITHMETIC_TARGET                               = OPEN; PARKED until a genuinely new arithmetic idea
WRITE_UP                                                   = NOT STARTED (needs operator decision under the standing no-manuscript rule)
```

## ABC REVIEW CORRECTIONS + KURIHARA GATE (Pro review 2026-09-17; audit ~/BSD_ABC_REVIEW_2026-09-17/00_REPORT.md sha256 7478087bfaad5624679da399d50c9e5c00c34408d7cc9948f632180e4c2afce5)
```
A_DIRECT_PRINTED_APPLICATION        = NOT_APPLICABLE (Castella–Do 6.5.1/6.7.1 hypotheses fail at j = 0, L(f/K,1) = 0)
A_UNIVERSAL_IMPOSSIBILITY_CLAIM     = WITHDRAWN (file 32 A4 overreached)
B_NONZERO_UNDERIVED_BOTTOM_ROUTE    = OBSTRUCTED (Mazur–Rubin 2016 Thm 13.4(viii): kappa_1 != 0 iff dual Selmer finite)
B_ZERO_BOTTOM_IMPLIES_NONPRIMITIVE  = FALSE — WITHDRAWN (Cor 13.1(iii), Thm 13.4(vii))
B_EXACT_H9_ARITHMETIC_REALIZATION   = NOT ESTABLISHED
BKS_DESCRIPTION                     = CORRECTED (regulators explicit in Def 4.10 / Prop 4.14; circular only via Hypothesis 2.2(iii))
C_RANK2_AND_SHA2                    = EXISTING THEOREM (Zywina 2025)
C1_FAMILY (m=491 mod 840, n=0 mod 420, m,A,B prime) = AUDITED PASS: infinite, rank 2, good ordinary at 5, image GL_2(F_5), 5 ∤ Tam
PROPOSITION_K (proved from Kim Thm 1.8(1)-(3), Cor 1.6; Castella–Sano Thm B; Castella Thm A)
                                    = on C1 at p=5: two-prime Kurihara witness <=> kappa_5 != 0 <=> Sha[5^inf] finite;
                                      witness valuation <= C <=> #Sha[5^inf] <= 5^C
MECHANISMS                          = M1 congruence transport KILLED (mod-5 rep ramified at each member's own m, A, B);
                                      M2 rank-2 Mazur–Tate/GPR NOT ADMISSIBLE (needs finite Sha); M3 Kim Thm 1.10 NO INDEX CONTROL
RESOURCES                           = smallest member m=3011, n=420; conductor 10^24.1-10^25.9; modular symbols infeasible; nothing launched
C_UNIFORM_SHA5_BOUND                = OPEN (UNKNOWN): needs a non-tautological mechanism for finite (or 5^C-bounded) Sha[5^inf] on an
                                      explicit infinite subfamily of C1
CURRENT_H9_CONSTRUCTION             = STOPPED AT ITS RECORDED BOUNDARY (unchanged)
UNIFORM_H9_ARITHMETIC_TARGET        = OPEN (unchanged)
```

## C1 CLASS-GROUP GATE (Pro note 2026-09-17; audit ~/BSD_ABC_REVIEW_2026-09-17/C1_CLASSGROUP_AUDIT/00_AUDIT.md sha256 b92e9f6753d863ddd901d4d0192050b827dd3aa60d1921817c45d7086a3050b0)
```
CG  (dim Sel_5 <= 3 + c_chi, c_chi = dim Cl(L)[5]^{sigma=2}, L = Q(nonzero 5-torsion point), degree 24)  = VERIFIED on C1
CG0 (c_chi = 0 => Sha[5^inf] = 0)                                                                         = VERIFIED on C1
NONVACUITY (does some C1 member have c_chi = 0?)                                                          = UNKNOWN
LEMMA_R (proved): 1 <= d_str <= c'' <= 3 + c_chi, c'' = dual-point-field eigenspace (L'' = Q(E[5]^dual point), d -> d)
                                                                                                          = reflected condition c''=0 VACUOUS on C1
FAMILY_INPUT                                                                                              = NOT TRIGGERED; none known
COMPUTATION                                                                                               = class group at |disc| >= 10^285.7 infeasible; not launched
C_UNIFORM_SHA5_BOUND                                                                                      = OPEN (unchanged)
```

## C1 REFLECTION + UNIT/CLASS CRITERIA GATE (Pro note 2026-09-17; audit ~/BSD_ABC_REVIEW_2026-09-17/C1_REFLECTION_UNIT_AUDIT/00_AUDIT.md sha256 4694f979fdf5b78ad8309afe4bac89b96964b57dd0a9722532be75fa02f9244f)
```
R_EXACT (b = dim Cl(Ld)[5]^theta* = 3 + c - r5)   = VERIFIED on C1 (2I acts by 4 on H^1_ur(mu_5) vs 2 on theta; prime-to-5 descent; orientation)
DUAL_IDENTITY (new)                               = c = 3 + b - r5d; r5 + r5d = 6
CERTIFICATE_ROWS                                  = b<=2 | c=0 | c<=1 & t5>=2 | c<=2 & t5=3  => Sha[5^inf]=0; r5 <= c+2;
                                                    t5 may be replaced by r5 (virtual units suffice)
CALIBRATION_389a1 (outside C1; GRH class groups)  = c=0, r5=t5=2, b=1, r5d=4 exactly as predicted; not new (Stein–Wuthrich Thm 12.3)
UNIT_HALF                                         = RESTRICTED_ANSATZ_OBSTRUCTION: O(X~)^* = Q^* on the generic C1 surface (no uniform integral
                                                    unit or relative-Pell formula, vertical poles allowed); horizontal-pole ansatz NOT excluded
CLASS_HALF                                        = UNKNOWN; first missing: whole-component bound c<=1 (or b<=2) on an explicit infinite subfamily
C1_WITNESS                                        = NONE; per-member computation infeasible (log10|disc L| >= 285.7, calibrated ~2e17 x 389a1 cost)
CLASSGROUP_AUDIT_S4                               = CORRECTED ("PARI not installed" was false; verdict unchanged)
C_UNIFORM_SHA5_BOUND                              = OPEN (unchanged)
CURRENT_H9_CONSTRUCTION                           = STOPPED AT ITS RECORDED BOUNDARY (unchanged)
UNIFORM_H9_ARITHMETIC_TARGET                      = OPEN (unchanged)
```

## C1 GENERIC RADICAL SATURATION GATE (Pro note 2026-09-17; audit ~/BSD_ABC_REVIEW_2026-09-17/C1_GENERIC_RADICAL_AUDIT/00_AUDIT.md sha256 42cc1ff3b82c5f8e51321da1cd0cc07bc970958daedaba2c61547269333ab86d)
```
POINT_COVER_MODEL           = VERIFIED independently: C: W^2 = 5*F2*G4*D, deg 18, disc -2^70*3^16*5^88, genus 8, t = N/D of degree 12;
                              x_T = d*s^2 is a psi_5 root at five specializations, so Q(s,W) = Q(t)(T) (not a j-match)
FROBENIUS_AT_7              = VERIFIED twice (hyperellcharpoly; brute force to 7^4): #J_C(F_7) = 6253200 = 2^4*3^4*5^2*193, v_5 = 2
                              => dim J_C(Q)[5] <= 2, no GRH
SECTIONS_MOD_5              = VERIFIED: rows (1,4) at p=23 and (1,2) at p=47 on t=1, determinant 3 mod 5
GENERIC_RADICAL_SATURATION  = VERIFIED: R_C^chi = <j(delta P1), j(delta P2)>, dim 2; J_C(Q)[5^inf] = (Z/5)^2; same on the normalized
                              (m,n)-plane; rational S-units on the bad fibres have zero chi-part
NEW_COROLLARY (this audit)  = any chi-eigen function with divisor supported over the bad fibres lies in <alpha1,alpha2>; closes item N1
                              (horizontal poles) of the reflection/unit audit
CERTIFICATE_EFFECT          = the generic source gives r5 >= 1, never 2; it certifies only when c = 0, i.e. no gain over CG0.
                              NOT recorded as r5(E) <= 1
ADMISSION_TEST              = ARITHMETIC_INPUT_NOT_IDENTIFIED (A no mechanism; B no bound: L_0 has signature (2,2), not totally real,
                              so Brumer/Rubin-Stark does not apply; C the natural cover is a thin set with no infinitude input)
C1_SHA                      = NO RESULT; class half still UNKNOWN
C_UNIFORM_SHA5_BOUND        = OPEN (unchanged)
CURRENT_H9_CONSTRUCTION     = STOPPED AT ITS RECORDED BOUNDARY (unchanged)
UNIFORM_H9_ARITHMETIC_TARGET= OPEN (unchanged)
```

## C1 CORRECTIONS: LOCAL IMAGE AND STARK SCOPE (Pro REVIEW.md 2026-09-17; audit §8 of ~/BSD_ABC_REVIEW_2026-09-17/C1_GENERIC_RADICAL_AUDIT/00_AUDIT.md sha256 cac6a4f3812991c671d8fc9359cdd4de8c61f01a0b3dff3057445d1520f0733f)
```
GENERIC_LOCAL_IMAGE   = CORRECTED: dim = 1 when v5(n) = 1, and 0 when v5(n) >= 2 (log P1 = -2n/m, log P2 = 3n/m mod 5^(h+1), valuation
                        exactly h). Verified on the C1 members (3011,420) [h=1, residues 10 mod 25] and (5531,2100) [h=2, residues 50 mod
                        125, m,A,B prime]. My earlier unqualified "the generic source gives r5 >= 1" is WITHDRAWN; "never 2" stands.
EPSILON               = pinned to 1 only on the slice v5(n) = 1; unknown in {0,1} when v5(n) >= 2
STARK_SCOPE           = CORRECTED: Dasgupta-Kakde needs a CM abelian extension of a totally real base (still inapplicable), but
                        Burns-Sakamoto-Sano IV (arXiv:1903.09509) Thm 3.3 is over ARBITRARY number fields and applies here with r = 3
                        (F0 signature (2,2); one real and both complex places split completely; chi not a power of omega, so L ⊄ F0(mu5)).
                        It gives im(kappa_1) = Fitt^0(A_chi) unconditionally, with A_chi = (Cl(L) ⊗ Z5)^chi — but no evaluated element;
                        the explicit Rubin-Stark system in Cor 3.6 assumes the Rubin-Stark conjecture.
GATE_B_TARGET         = SHARPENED: c <= 1 <=> Fitt_1(A_chi) = Z5; an annihilator bounds exponents, not the number of summands
CITATION_FIX          = arXiv:2112.12949 is conditional on standard L-function conjectures; my earlier citation implied unconditional
ADMISSION_TEST        = ARITHMETIC_INPUT_NOT_IDENTIFIED (unchanged)
C1_SHA                = no result (unchanged); C_UNIFORM_SHA5_BOUND = OPEN (unchanged)
```

## C1 DUAL-COMPONENT WITNESS TARGET (Pro CLAUDE_EXECUTION_TARGET.md 2026-09-17; audit §9 of ~/BSD_ABC_REVIEW_2026-09-17/C1_GENERIC_RADICAL_AUDIT/00_AUDIT.md sha256 9cad8dd68b7b3defb1f6ea3a86aefdb03cf045bae4cbb5c9d475c06cb69f769c)
```
DUAL_TARGET           = ACCEPTED: Fitt_2(A_dual) = Z5 <=> b <= 2 => d5 = 2 => Sha[5^inf] = 0, independent of epsilon; dual-side Stark
                        rank r = 3 verified (Gal(Ld/F0) cyclic quartic; one real + two complex places of F0 split completely in Ld;
                        theta* not a power of omega, so Ld is not inside F0(mu5))
WITNESS               = NOT CONSTRUCTED
NEW                   = the BDSS rank/splitting mismatch (r_F0 = 4 vs character rank 3) is REMOVABLE by a quadratic totally imaginary base
                        change: over such F0' the rank is 6 = #S_inf(F0') and the Fitting conclusion descends, since degree 2 is prime to 5.
                        The obstruction is therefore EVALUATION, not applicability. Do not spend a cycle "fixing the signature".
ADMISSION_TEST        = ARITHMETIC_INPUT_NOT_IDENTIFIED
MISSING_DATUM         = an unconditional computable evaluation of a rank-3 Stark component at a two-prime index for (F0, theta*), i.e. an
                        unconditional Rubin-Stark case over a base that is not Q / imaginary quadratic / CM over totally real. Structure
                        theorems (BSS III 3.6(iii)(a), BSS IV 3.3, BDSS 3.8) give containments but no number; a direct finite-level
                        evaluation needs S-units of a field containing Ld (log10|disc| >= 285.7 at the smallest member)
C1_SHA                = no result (unchanged); C_UNIFORM_SHA5_BOUND = OPEN (unchanged); GENERIC_RADICAL_SATURATION_VERIFIED retained
```

(ledger note: the §9 audit hash above was recorded before a one-line repair of a shell-mangled script reference in its §9.4 table; the corrected file has sha256 b397d2d4e9046d9bbd62037ac217e0c76431c6622fe42994098986b946c068db. No content other than that filename changed.)

## C1 ONE-SIDED CERTIFICATE + CORRECTIONS (Pro REVIEW_AND_CERTIFICATE.md / CLAUDE_HANDOFF.md 2026-09-17; audit §10 of ~/BSD_ABC_REVIEW_2026-09-17/C1_GENERIC_RADICAL_AUDIT/00_AUDIT.md sha256 755555e25e6c56b8ec239f8a7d1314032b1293e4935d7b4a6d24765ffd159425)
```
ONE_SIDED_CERTIFICATE = ACCEPTED as a method: installed PARI doc says bnfcertify(bnf,1) "only certify that the class group is a quotient
                        of the one computed in bnf (much simpler in general)". If the computed invariant factors have at most two divisible
                        by 5 and flag-1 certification returns 1, then dim Cl(Ld)/5 <= 2, so b <= 2 and Sha[5^inf] = 0. No character matrix
                        and no certified unit group needed; my earlier costing assumed the wrong (full) contract.
CORRECTIONS_ACCEPTED  = (i) Fitting direct sums obey the convolution formula, not "multiplicativity" (descent still holds);
                        (ii) the totally imaginary base change needs b + b_- <= 2 upstairs, i.e. it is strictly stronger than b <= 2;
                        (iii) "equivalently an unconditional case of Rubin-Stark" WITHDRAWN (neither implication was proved);
                        (iv) a unit-valued component is required, not merely a nonzero evaluation;
                        (v) "Kato/Beilinson-Flach/Heegner are all empty in rank two" WITHDRAWN — Kim Cor 1.5 (checked in the local source)
                            gives kappa^Kato NON-TRIVIAL for good ordinary p >= 5 with surjective image, exactly C1's hypotheses; the real
                            stop is that its derived data needs modular symbols at conductor 10^24-10^26, and by Proposition K a two-prime
                            Kurihara witness is EQUIVALENT to Sha[5^inf] finite, so it is an unevaluable certificate, not an input;
                        (vi) no rank-six-to-rank-three descent by exterior norm.
STILL_MISSING         = unconditional generator coverage for Cl(Ld)/5 (quotient route and component-only route alike), or a unit-valued
                        evaluated system component. Calibration of the gap: GRH factor-base bound 12 log^2|D| is 2.1e5 at 389a1 size and
                        5.2e6 at the smallest C1 member, while the elementary unconditional (Minkowski) bounds are 10^20.5 and 10^134.6.
PROPOSED (not run)    = measure bnfcertify(bnf,1) on the already-built 389a1 dual field, capped at 300 CPU-s/1 GiB/one process; needs
                        authorization, as it is a calibration computation.
ADMISSION_TEST        = ARITHMETIC_INPUT_NOT_IDENTIFIED (unchanged); C1_SHA = no result; C_UNIFORM_SHA5_BOUND = OPEN (unchanged)
```

## C1 CERTIFICATION PREFLIGHT: INSTALLED PARI (Pro CLAUDE_PREFLIGHT.md 2026-09-17; audit §11 of ~/BSD_ABC_REVIEW_2026-09-17/C1_GENERIC_RADICAL_AUDIT/00_AUDIT.md sha256 16ec852ba1c2d7b454bc4687672f76c6d620561bb78843f107eedfa525a363de)
```
SOURCE_MATCH        = PARI 2.17.4 matched locally (source tree in the H41 lane + the binary built from it; buch3.c sha256 4fd4c139...,
                      buch2.c sha256 904ced80...). The 2.17.3 sage-env binary used for earlier calibrations has no local source.
INSTALLED_BEHAVIOUR = confirms Pro's 2.17.2 reading: zimmertbound selects minkowski_bound when N > 20; bnfcertify0 runs
                      bnftestprimes(bnf,B) ("PHASE 1 [CLASS GROUP]", a loop over ALL rational primes <= B) and only then executes
                      `if (flag) return 1`. Flag 1 therefore skips PHASE 2 (units/relations) only; the generation phase is unchanged.
BOUNDS (exact)      = degree 24, signature (4,10): 389a1 dual field B = 2.98e20 (about 6.3e18 primes to test); smallest C1 member
                      B >= 3.81e134. Reproduces BOUND_RECEIPT.json digit for digit; the receipt's 286-digit integer equals
                      3^16*m^16*A^18*B^16; the archived 389a1 output it cites is my own file (sha256 98668b33...).
SELF-CORRECTION     = my §10 Minkowski figures (20.4744871 / 134.5812371) came from a 6-digit rounded log10|D|; exact values are
                      20.4744889159 / 134.5810079019.
CALIBRATION         = WITHDRAWN. Running bnfcertify(.,1) on the 389a1 dual BNF would only time out inside phase 1. Recorded as the stock
                      implementation being outside the practical budget, NOT as impossibility of the arithmetic certificate.
COVERAGE REQUIREMENT= keep it weak: 5 does not divide [Cl(Ld):H] (equivalently H + 5G = G), or e_chi((G/H)/5(G/H)) = 0 for the
                      component-only version. Neither is an algorithm.
ADMISSION_TEST      = ARITHMETIC_INPUT_NOT_IDENTIFIED (unchanged); C1_SHA = no result; C_UNIFORM_SHA5_BOUND = OPEN (unchanged)
```

## C1 CENTRAL-INVOLUTION ADDENDUM — ACCEPTED AND INTEGRATED (Pro ACCEPTED_REVIEW_NOTE.md sha256 15bdb09768778dfd85f48efa0f972c8f2a244a6ea1dc2cb64795b7ad55db8aaf; my review ~/BSD_C1_CENTRAL_INVOLUTION_REVIEW_2026-09-17/00_REVIEW.md sha256 ede658084e5c40e77e6c1c8e27a76cb9f44eab8aa6754bd4acf7e013f99df8ae)
```
CENTRAL_ODD_TARGET_HAS_NO_LOWER_DEGREE_NORM_CHANNEL = ACCEPTED. Every subgroup of GL_2(F_5) of index < 24 contains -I (verified here
                      exhaustively against the full 76-subgroup lattice of SL_2(F_5), in addition to the theoretical proof: odd-order
                      subgroups of SL_2 have order 1, 3 or 5, and the determinant quotient has order <= 4). The target is -I-odd and every
                      smaller permutation module is -I-even, so BOTH Hom spaces vanish over any coefficient ring with 2 invertible. Hence
                      no relation N_H = sum a_i N_{J_i} b_i over Q, Q_5, Z_5 or F_5 — the "clear a denominator divisible by 5" escape is
                      closed — and the same holds for auxiliary fields of absolute degree < 24, by the direct compositum argument
                      (T_out z = T_out, z T_in = T_in) rather than by contraposing Etienne's implication.
REPAIRS RECORDED    = (i) the old N_H -> id_P cancellation is unavailable (pi iota = 20 id_P = 0 mod 5); the central proof replaces it;
                      (ii) covector labels [2^k] with beta -> 3 beta run OPPOSITE to successive right-translation orbit labels, so the
                      eigenvector coefficients lambda^k and lambda^(-k) each belong to their own convention; the executable and every
                      finite verdict are unchanged.
SCOPE               = this is a vanishing-channel statement, NOT a bound on the target component, which is nonzero (b >= 1).
NOT EXCLUDED        = arithmetic elements or ideal relations specific to D; non-splitting inequalities; fields of absolute degree >= 24;
                      genuinely different twisted-coefficient constructions; direct one-sided or component-only coverage; evaluated
                      Euler/Stark/Iwasawa inputs. Degree is not an operation count.
UNCHANGED           = GENERIC_RADICAL_SATURATION_VERIFIED; SPECIALIZATION_ARITHMETIC_OPEN; ARITHMETIC_INPUT_NOT_IDENTIFIED; C1 definition;
                      C1_SHA = no result. The earlier uncorrected denominator/outside-field escape list is NOT merged.
```

## C1 THREE ACCEPTED RESULTS — INTEGRATED (operator/Pro acceptance 2026-09-17)
```
ALL_ODD_RESIDUAL_IMAGE_VERIFIED   (review ~/BSD_C1_RESIDUAL_IMAGE_REVIEW_2026-09-17/00_REVIEW.md sha256 676d0f840781e002498c7f35c833239f6eca0004c32bd594debbcd23b281863a)
  For every m,n with m, A=m+16n^2, B=m+25n^2 prime and = 11 mod 24 (Zywina Thm 1.2's hypotheses, confirmed in the local source), the
  mod-ell image of y^2=x^3-5Ax^2+4ABx is GL_2(F_ell) for every odd ell. Local proof at A (good model over Q_A^nr(A^{1/4}), T^2=-I,
  det T=1, Frobenius inverts T since A=3 mod 4, so no stable line) + Tate transvection at m (at B if ell=m) + prime-field lemma;
  ell=A by Mazur's prime-isogeny bound (A>=2315>163). Each mod-ell image separately; NOTHING adelic. Imported, not re-derived: Mazur
  (read via Banwait Thm 1.2 / Michaud-Jacobs), Tate uniformization, Serre-Tate. C1's mod-7 conditions were sufficient, not necessary.

FIXED_PRIME_SUBFAMILY_INFINITE_VERIFIED   (per-member review ~/BSD_C1_FIXED_PRIME_REVIEW_2026-09-17/00_REVIEW.md sha256 a57744154f0cf97015225edd6f3b780bd23fd24c3b6e7c2ddc63693f53731eca;
                                           Fable adjudication ~/BSD_C1_TZ_MOD8_ADJUDICATION_2026-09-17/00_FABLE_ADJUDICATION.md sha256 f4e837212555ccdb41b9bf1c531373252a2698b684c63f7049c08a1895743552)
  F_fix: m = 15292691, n = 2171820 (mod Q = 4200*71*181), m,A,B prime; a subfamily of the UNCHANGED C1, with v5(n)=1 throughout.
  Per member: both 71 and 181 reduce every member to y^2=x^3-85x^2+1768x; localization matrix of P1,P2 = [[1,2],[1,3]], det 1 mod 5;
  so [P1],[P2] is a basis of the actual E(Q)/5E(Q) (5-saturation, not integral index one); Sel_5 = W + K with
  K = ker(loc_71, loc_181) = Sha(E/Q)[5] via an explicit projection; the relaxed structure F_rel has primal Sel_5 and dual Sha[5],
  core rank 2. Certified member (m,n) = (447086291, 2171820).
  Infinitude: by FABLE'S LEMMA A, a DERIVED fixed-congruence lemma proved from the printed Tao-Ziegler argument
  (arXiv:1603.07817 = Forum Math. Pi 6 (2018) e1) — NOT a theorem stated verbatim in the paper. Proof keeps the printed squarefree
  primorial W unchanged, expands the class indicator into additive characters of the non-squarefree part q' (q'=20 here), pushes the
  periodic weight through the printed generalized von Neumann theorem on a non-distinguished node, and treats the lone degenerate
  term by Siegel-Walfisz for modulus q'W (the only input outside the paper). The author's original W -> lcm(Q,W) route is SUPERSEDED,
  not certified. Distinct pairs give distinct curves by Zywina Lemma 4.1 (j-denominator 3^2*m*(m+25n^2)^2; checked in local source).

MR_RESIDUAL_EQUIVALENCE_VERIFIED   (~/BSD_C1_FIXED_PRIME_REVIEW_2026-09-17/01_MR_EQUIVALENCE.md sha256 7d079c1118bd4aa4f84107889d3a4916c2493e983c02dd410021fbaa4d18af05)
  Mazur-Rubin (H.1)-(H.6) hold for T=E[5], R=F_5, F_rel (core rank 2); SS_2 is free of rank one over F_5, so every nonzero Stark
  system is primitive, and omega = delta(P1)^delta(P2) extends to a Stark system with epsilon_1 = omega  <=>  Sha(E/Q)[5] = 0.
  LANE CLOSED AS A MECHANISM: "construct compatible epsilon_n extending omega" is the target itself (same shape as Proposition K).
  Residual level and this F_rel only; no statement about Z_5-level systems, other Selmer structures, or whether Sha[5] vanishes.

UNCHANGED: C1 definition; no Sha bound; no class-group bound; ARITHMETIC_INPUT_NOT_IDENTIFIED; SPECIALIZATION_ARITHMETIC_OPEN.
```

## C1 FIXED-PRIME CLASS-GROUP BRIDGE — MERGED (operator/Pro acceptance 2026-09-17; ~/BSD_C1_STRICT_CLASSGROUP_BRIDGE_2026-09-17/00_BRIDGE.md sha256 e1892af7f594dc9ed1a816ffa4031266e13a084e07d3409c7785275fc00833ca)
```
EXACT_BRIDGE_ONLY_NO_BOUND   (a structural theorem, preserved so it is not rediscovered)
  On F_fix the rational points localize at 5 as (2,2) (v5(n) = 1), so the minors (loc_5, loc_71) and (loc_5, loc_181) are 2 and 4, and
  Sha(E/Q)[5] = ker(loc_5, loc_ell) for ell = 71 or 181. That kernel is strict at 5, so it embeds into the dual of the ELL-SPLIT QUOTIENT
  (Cl(D)/<primes of D above ell> (x) F_5)^{theta*}, of dimension
      b_ell = 3 + c - r_{5,ell} = b - rho_ell      (exact; rho_ell = rank of localization above ell on the unramified theta-radicals).
  At ell = 71, 181 Frobenius acts on E[5] as a transvection; the unramified local chi-space is 2-dimensional and the Kummer line injects.
  Certified rho_ell >= 1 (the rational strict class delta(P1) - delta(P2) is non-split at both primes: it is Lemma R's forced class)
  and r_{5,ell} >= 2 REPRODUCE dim Sha[5] <= min(b - 1, 1 + c) — no improvement. Conditional only: rho_ell = 2 would let b <= 3 suffice.
  K_{71,181} itself is not strict at 5, so its correct Kummer dual is a RAY class group at 5 with the Kummer-line condition, not Cl(D)/<S>.
  No degree-24 computation proposed.
```

## PERMANENTLY CLOSED AS A MECHANISM (2026-09-17)
```
EXTEND_OMEGA_TO_A_RESIDUAL_STARK_SYSTEM = CLOSED. omega = delta(P1)^delta(P2) extends to a Stark system for (E[5], F_rel) with
  epsilon_1 = omega  <=>  Sha(E/Q)[5] = 0 (MR_RESIDUAL_EQUIVALENCE_VERIFIED). Constructing the compatible epsilon_n IS the target, not a
  step toward it — the same shape as the two-prime Kurihara equivalence (Proposition K). Do not reopen; do not rediscover the explicit
  wedge with unit local determinant as progress. Scope: residual level and this F_rel; nothing is claimed about Z_5-level systems,
  other Selmer structures, or whether Sha[5] vanishes.
NEXT (speculative branch, handoff prepared, not launched by this record): fixed-E[5] family, Gate G (geometry) then Gate S (Selmer
  transport); ~/FABLE_FIXED_E5_FAMILY_HANDOFF_2026-09-17/00_FABLE_TASK.md.
```

## FIXED-E[5] FAMILY, GATE G — MERGED WITH OPERATOR WORDING (2026-09-17; Fable report ~/FABLE_FIXED_E5_GATE_G_2026-09-17/00_GATE_G_REPORT.md sha256 b04ecdb2ccadf41112ed922ea5e50add2f9a6d640d4ef8e0dc5cad1aa2ae9be6)
```
FIXED_E5_GATE_G = OPERATIONALLY_OBSTRUCTED; NONEXISTENCE_OPEN
  Fable returned "G_OBSTRUCTED" under the handoff's stop rule. It is recorded here as an OPERATIONAL obstruction, NOT a nonexistence theorem;
  the report's own section 3.5 names the unresolved statement. Gate S was not entered and nothing about it is claimed.

PROVED (accepted):
  - the fixed-E0[5] universal surface (Rubin-Silverberg Thm 5.1, instantiated for 389a1: twelve I5 fibres, nothing else) is geometrically
    Shioda's S(5): chi = 5, p_g = 4, kappa = 1, rho = h^{1,1} = 50, MW = (Z/5)^2, geometric rank 0;
  - every base change ramified only over cusps (every moduli-theoretic base change, congruence or not) still has rank 0;
  - rank budget (Lemma A): for phi: C -> X_E(5) of degree n and genus g, rank E(Qbar(C)) <= R_free(phi), the ramification over non-cusps,
    with equality iff rho(S_C) = h^{1,1}(S_C) = 50n + 2g;
  - a Gate G solution with C(Q) infinite reduces to Q-rational non-torsion multisections of geometric genus <= 1 on the twisted S(5)
    (Lemma B), and such multisections are rigid, with very general base changes of rank 0 since S(5) is not uniruled (Lemma C(i),(ii));
  - the level-5 K3 analogy was the wrong surface: arXiv:1705.03527's R_{5,5} is the rational Gamma_1(5) surface (chi = 1); double covers of
    the chi = 5 fixed-E[5] surface are never K3. Hindry-Salgado's rank jumps need a unirational surface or a pencil of rational curves,
    impossible for kappa = 1.
NOT MERGED: any wording equivalent to "such a base change does not exist".
OPEN (report section 3.5): whether S(5)^{rho_E0} carries a Q-rational non-torsion multisection of geometric genus 0 or 1.
  Operator-supplied context, not independently checked here: Ulmer (arXiv:1407.7845) — a very general elliptic surface of height >= 3 has
  no rational multisections beyond the zero section and fibre components, special surfaces left open; a 2026 manuscripta paper — still open
  in general whether a fibration over a genus <= 1 base admits a genus <= 1 multisection with non-torsion differences; the classical 25
  three-sections of S(5) from 2-torsion are Bring curves of genus 4, so they cannot serve Gate G.
OPTIONAL BOUNDED CONTINUATION (not launched): degree-2 twists u^2 = D(t), deg D <= 4, of the 389a1 Rubin-Silverberg family — R_free = 2,
  so rank <= 2 and rank 2 means reaching the Hodge bound; constrain section classes with NS = U + A4^12 (5-torsion overlattice), Shioda
  heights and the I0* fibres of the twist before solving coordinates. Kill-first; a bounded ansatz failure is not a negative theorem.
NO SHORTCUT: no average-5-Selmer theorem applies to this thin rank-two family (Bhargava-Ho marked points: 2- and 3-Selmer only;
  Bhargava-Shankar 5-Selmer: large families) — operator check.
```

## PROJECT BOUNDARY (2026-09-17)
```
FIXED_PRIME_SUBFAMILY_INFINITE_VERIFIED
MR_RESIDUAL_EQUIVALENCE_VERIFIED
STRICT_CLASSGROUP_BRIDGE = EXACT_BRIDGE_ONLY_NO_BOUND
FIXED_E5_GATE_G = OPERATIONALLY_OBSTRUCTED   (NONEXISTENCE_OPEN)
SPECIALIZATION_ARITHMETIC_INPUT = NOT_IDENTIFIED
(also retained: ALL_ODD_RESIDUAL_IMAGE_VERIFIED; CENTRAL_ODD_TARGET_HAS_NO_LOWER_DEGREE_NORM_CHANNEL; GENERIC_RADICAL_SATURATION_VERIFIED;
 C1 unchanged; no Sha bound; H9 construction stopped; H41 frozen)
```

## FIXED-E[5] FAMILY, DEGREE-2 TWIST ATTACK — MERGED (2026-09-17; report ~/FIXED_E5_DEGREE2_TWIST_ATTACK_2026-09-17/00_REPORT.md sha256 8e9e51cab4306aa705000b0460e316c3852ab2687ac3e0c5a7622a72fe154951)
```
FIXED_E5_GENUS0_DEGREE2 = CLOSED_NEGATIVE
FIXED_E5_GENUS1         = OPEN_BUT_REDUCED
FIXED_E5_GATE_G         = OPERATIONALLY_OBSTRUCTED; NONEXISTENCE_OPEN   (unchanged; parked; no escalation to base-change degree > 2)
Task return (FIXED_E5_DEGREE2_TWIST_ATTACK_001): UNKNOWN_NO_WITNESS — no witness, and the full degree-two class (genus 0 and 1) is not
  excluded; the genus-0 half is closed by a theorem. Operator review accepted the Kummer step and the scoping of the genus-1 bound.

PROVED (genus 0): the cusp polynomial g (deg 12) of the 389a1 Rubin-Silverberg family is irreducible over Q (computed), so G_Q is
  transitive on the 12 I5 cusps and no D in Q[t] of degree <= 11 is branched at a cusp. For every squarefree D in Q[t] with deg D in {1,2}:
  rank E^D(Q(t)) <= 1, hence rank E(Q(t,sqrt D)) <= 1.
  Mechanism: MW(E^D over Qbar(t))/5 -> (+)_cusps Phi_v (x) F5 is injective. Over Qbar((s)), good-reduction and identity-component points are
  5-divisible; at the two branch points inertia acts by -1, so H^1(K_v, E^D[5]) = E[5]/(-2)E[5] = 0; globally
  H^1(pi_1(P^1 - {t1,t2}) = Zhat(1), E[5] (x) chi_D) = 0. Independently, the NS discriminant-length count is tight
  (rank L^perp = 12 = l_5(disc L)). Invariant component vectors span <= 1 dimension (one cusp orbit).
  A rank-1 twist (not evaluated) needs split multiplicative reduction at the cusp orbit: -2a(v0)b(v0)D(v0) in Q(v0)^{x2}.
REDUCED (genus 1, deg D in {3,4}; not a negative theorem): rank E^D(Q(t)) <= 1 + dim Hom_{G_Q}(J_C[5], E0[5]) <= 2, where C: u^2 = D(t).
  Rank 2 needs: J_C[5] = E0[5] as G_Q-modules (J_C 5-congruent to 389a1, symplectically or anti-symplectically); split twisted cusp fibres;
  a Q-rational section through the identity component at all 12 cusps (height >= 10); and a second section meeting components +-k at all
  cusps. These conditions do not empty the class (e.g. C = 389a1, D = 4t^3+4t^2-8t+1). Phase 0 gives no finite height range, so no
  coefficient search was run. Deciding it is a Noether-Lefschetz question.
Compute: < 1 CPU-s. No number fields, class groups or modular symbols.
```

## SMALL-SEED FIXED-PRIME FAMILY (2243,12) — MERGED WITH OPERATOR WORDING (2026-09-17; report ~/BSD_SMALL_SEED_FIXED_PRIME_2026-09-17/00_REPORT.md sha256 f03992d00b07e7d6afe1bec82663bfc33715bab218944565fa34146d48a443a3)
```
SMALL_SEED_FIXED_PRIME_FAMILY_VERIFIED  (author-side deduction, independently checked)
  Seed (m,n) = (2243,12): m, A = 4547, B = 5843 prime, all = 11 mod 24 (Zywina Thm 1.2: E(Q) = Z/2 x Z^2, P1 = (A,6nA),
  P2 = (36n^2, 12n(m-2n^2))); N = 2^3*3*m*A^2*B = 6503188012738584, Tamagawa product 16, root number +1; a5 = -2, #E(F5) = 8
  (good ordinary, non-anomalous, E(Q5)[5] = 0); psi_5 irreducible + Tate transvection at m => image GL_2(F_5).
  Fixed transvection primes 31, 181: rows (1,1), (1,0); R = [[1,1],[1,0]], det -1 => E(Q)/5E(Q) = <P1,P2> and
  Sha(E/Q)[5] = ker(loc31, loc181).
  Infinite: Fable's Lemma A / Cor A' with q = Q = 673320 = 2^3*3*5*31*181, additive variable m = 2243 mod Q, n = Qy + 12
  (admissibility checked); on this family the reductions at 5, 31, 181 and hence R are frozen. Second member (158905763,673332) checked.
  5-ADIC CORRECTION: fixing the mod-31 and mod-181 rows does NOT freeze loc5; loc5 needs mod-25 data as well
  (seed: loc5 = (0,2), P1 in 5E(Q5); member (158905763,673332): (4,1)). Use Q' = lcm(Q,25) = 3366600 when loc5 must be fixed.
  The C1 formula log P1 = -2n/m, log P2 = 3n/m mod 5^(h+1) holds for h = v5(n) >= 1 only (at h = 0 it predicts (2,2)).
  MINIMALITY (operator wording): smallest NON-ANOMALOUS parent-family seed by conductor/discriminant scale among the seeds checked —
  exhaustive for conductor <= 6503188012738584 (any exponent at 2; all 15 prime triples tested have exponent 3) and for retained
  scale log10(3^16 m^16 A^18 B^16) < 190. Smaller m-values exist, e.g. (11,24), but all eight lower-conductor / lower-scale seeds
  ((659,12),(947,12),(1187,12),(1499,12),(1787,12),(1907,12),(11,24),(11,36)) are anomalous at 5 (#E(F5) = 10).
FIELDS_BUILT: point field L and dual field Ld, degree 24, signature (4,10), Aut order 4 (sigma: T -> 2T; tau on Ld);
  Delta_L = Delta_Ld = 2^32 * 3^16 * 5^23 * m^16 * A^18 * B^16  (exact: order maximal by prime support + Neron-Ogg-Shafarevich),
  log10|Delta_L| = log10|Delta_Ld| = 213.06170177...  (operator reproduced independently). Retained prime-to-2-and-5 scale 187.35;
  the 2- and 5-parts add 25.71 digits. Polynomials in ~/BSD_SMALL_SEED_FIXED_PRIME_2026-09-17/runs/fields_2243_12.gp.
PROVISIONAL_CLASS_ARITHMETIC_EXCEEDS_CAP: one probe, PARI 2.17.4 bnfinit(L), GRH-rigorous defaults, 900 s / 1 thread / 4 GiB:
  GRH generation bound LIMC2 = 419775 (effective Bach constant 1.744 log^2|D|); the 4 GiB stack overflowed after factor-base
  construction and before any relation was recorded. c, b NOT obtained. Stock-implementation cost, not an impossibility statement.
```

## C1_PROJECTED_CHI_RELATIONS_001 — MERGED WITH OPERATOR WORDING (2026-09-17; report ~/BSD_PROJECTED_CHI_RELATIONS_2026-09-17/00_REPORT.md sha256 a67aac2a44119e7e1445273bbd0075b40acc8875bc7a5a00ad68c79d65f8d8a3, erratum section governs)
```
PROJECTED_RELATIONS_INSUFFICIENT   (seed (2243,12), dual field Ld; GRH-conditional reconnaissance only — no claim about b or Sha)
PROJECTED_RELATION_METHOD_PARKED_FOR_2243_12
  Reduction verified: C4-orbits with nontrivial stabilizer have zero chi-projection (tau^2 acts by chi(tau^2) = -1); one generator per
  free orbit; row = sum_k v_{tau^k P}(alpha) 2^k mod 5 (retained convention T_tau[a] = [tau a], chi(tau) = 2, distinct from chi^-1 = 3);
  b <= N - rank. "chi and chi^-1 dimensions agree" is FALSE in general (389a1 calibration: dims 1 and 0).
  GRH factor base: 419775 was computed for L and transfers to Ld — L, Ld are Gassmann-equivalent (vectors vs covectors of GL2(F5)),
  zeta_L = zeta_Ld, PARI 2.17.4 GRHchk sees only (N, R1, log|D|, residue-degree patterns); 0 mismatches over all 35373 primes <= B.
  N = 8918 free orbits, streamed in 6.8 CPU-s, RSS 17 MB (the 4 GiB storage wall is gone).
  Relations: 396962 exact candidates (a - b*theta: 384534; skew-reduced ideal elements: 12428), 0 fully 419775-smooth; rank 0 of the
  8916 needed for b <= 2. Smallest sampled smoothness targets 10^45.7 (ideal family, N(alpha)/N(P)) and 10^52.4 (a - b*theta, N(alpha));
  best residual non-smooth cofactors 10^31.0 and 10^28.3 respectively. Dickman u about 8.1 and 9.3 at those targets.
  Operational stop only: do not repeat these naive relation families on nearby or larger members without a new reason. NOT a theorem
  that direct class-group computation fails elsewhere in the infinite family; not a complexity lower bound.
```

## PARTIAL_FULL_5_DESCENT_GATE_001 — MERGED WITH NARROWED WORDING (2026-09-18; report ~/BSD_PARTIAL_5_DESCENT_GATE_2026-09-17/00_REPORT.md sha256 26c27ff8cda4a50ebb6fef48fc91fafd06523396b7f2d80f7e59153fa818b966, erratum section governs)
```
NO_LINEAR_KUMMER/PERMUTATION/RESOLVENT_DESCENT_BELOW_DEGREE_24   (seed (2243,12); NOT "no partial descent of any kind")
  Fisher 2013 §6 (source read): full 5-descent embeds H^1(Q,E[5]) into the sigma_2-eigenspace of L*/L*^5, L = Q(T) of degree 24; with
  Tamagawa numbers prime to 5, Sel_5 lies in L({p|5},5). For (2243,12): dim L(S,5)^(2) = 3 + c, so dim Sel_5 <= 2 needs only an upper
  bound on one faithful 5-primary component (c = 0, or b <= 2), not the full class group or units. Fisher calls class groups and units
  the main obstruction.
  GAP on GL2(F5): 13 of 48 subgroup classes avoid -I, minimal index 24; exactly 4 of index 24 (C5:C4, the point fields of
  E[5] (x) det^j; Gassmann pairs {0,1} = {L, Ld} and {2,3}). Over every base of degree < 24 each composition factor of E[5] is -I-odd,
  cut out in degree >= 24.
  PROVED: G_Q-linear descent maps induced by E[5] -> Ind_{H'}^G(W') with [G:H'] < 24 and -I trivial on W' (Kummer mu_5, permutation,
  resolvent modules) are zero; -I-odd coefficient modules over number fields need degree >= 24. This closes the Siksek-Stoll /
  intermediate-cover class (a Selmer-SET obstruction, not a Selmer-group bound).
  NOT CLAIMED: local restrictions (loc31, loc181) and cup products with fixed explicit classes via the Weil pairing (-I-even target
  H^2(mu_5)) give nonzero functionals on H^1(Q,E[5]); Poitou-Tate/Cassels-Tate constructions and non-descent methods are not excluded.
  Magma's n = 5 implementation claim: operator-supplied (handbook HTTP 401 here).
```

## STEIN_WUTHRICH_P5_GATE_001 — MERGED WITH SIX-SYMBOL ADDENDUM (2026-09-18; report ~/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/00_REPORT.md sha256 3a966cf9d6b3e67689b2e5d14111a6939c6f4415ef36c42278c5e8c8b1633137)
```
SW_REGULATOR_DONE_LP_FEASIBLE   (seed (2243,12), p = 5)
  SW Alg. 11.1 and Kato Thm 7.3 apply (good ordinary at 5, rho-bar_5 = GL2(F5)). Index lemma: Reg_5(<P1,P2>) = I^2 Reg_5(E(Q)), 5 not | I.
  Reg_5(<P1,P2>) = 5^2 + 2*5^4 + 3*5^5 + ... + O(5^26), ord 2, nondegenerate (PARI = SW normalization, 446d1 reproduced).
  ord_5 Reg_gamma = 0 and epsilon_5, Tamagawa (16), torsion are 5-units, so b_5 = ord_5 L_5*(E,0); ord_T L_5 >= 2 automatically.
  a_2 mod 5 is the T^2 coefficient of P_2 (SW Prop 3.5, c = 0). SIX-SYMBOL FORM (operator; independently re-derived):
    a_2 = 3([2/25]+ + [3/25]+ + [4/25]+ + [11/25]+) + 4([9/25]+ + [12/25]+)  (mod 5);  the [b/5]+ terms cancel (sum C(j,2) = 10);
    alpha = 13 (mod 25).
  If a_2 is not 0 (mod 5): ord_T L_5 = 2, v_5(L_5*) = 0, b_5 = 0, Sha(E/Q)[5^inf] = 0 (Kato + SW Thm 6.1 only; no p-adic BSD).
  If a_2 = 0 (mod 5): stop; no Sha[5] != 0 claim until the Skinner-Urban converse is checked against its original hypotheses.
  NORMALIZATION: 5 does not divide c0 (Mazur; Abbes-Ullmo: c0 = 2^a 4547^b), so the mod-5 bit is normalization-independent.
  IDENTIFICATION CAVEAT: recovering exact symbol values from numerics needs a denominator bound, and c0's size at 2 and 4547 is not
    bounded by any published theorem (Edixhoven's bound is unpublished; Cesnavicius-Neururer-Saha give c | deg(phi)). The streaming run
    therefore reports the explicit Manin threshold it certifies. Wuthrich Thm 12 cost with certified truncation (Lemmas 4-5):
    T about 1.07e10 (eps 1e-6) to 1.29e10 (eps 1e-9).
```

## STEIN_WUTHRICH_P5_LP_RUN_001 — MERGED WITH OPERATOR CORRECTION 4547 ∤ c0 (2026-09-18; run report ~/BSD_SW_LP5_STREAMING_2026-09-18/00_REPORT.md sha256 226d1d1671777979eb26b97352b4d73819a1c986fd54c0e3c84165087aeba601, addendum governs; run MANIFEST sha256 2708836834d57d562d1935578e9b1fc5bb4618dadf2433a48f95a59b4f739578; check report ~/BSD_MANIN_4547_EDIXHOVEN_CHECK_2026-09-18/00_REPORT.md sha256 b075b1bae5036b655b5ba175fe4b23ca03dcb6412db9d56e2653716b24c369ce)
```
A2_EQUIV_2_MOD_5_CONDITIONAL_ON_V2_C0_LE_17   (seed (2243,12), p = 5; certified streaming computation)
  a_2(L_5) = 2 (mod 5) in our normalisation (nonzero in every 5-unit normalisation), PROVIDED v_2(c0) <= 17.
  Computation: Wuthrich 2018 Sec. 4 on the unitary cusps b/25; certified truncation (Deligne + Berkane-Bordelles-Ramare divisor bound):
    T1 = 7682510690 and T2 = 9134686292, certified symbol error 2.5e-4 and 2.5e-6; 4.17e8 primes a_q by a certified BSGS counter
    (0 fallbacks; 417382 in-run PARI spot checks, 0 mismatches). Validation: 37a1, 389a1, 446d1, 234446a1 (all 20 [b/25]+ = eclib =
    Wuthrich's own implementation; his printed [1/27]+ = 1 for 234446a1 is a slip, true value 0).
  [b/25]+ for b = 1..24, 5 not | b: -54 16 90 -52 | -76 16 76 -52 | -54 90 90 -54 | -52 76 16 -76 | -52 90 16 -54 (identical at T1, T2).
  Six-symbol value 3(16+90-52-54) + 4(-52+90) = 152; direct weighted accumulator 152.000000000006; full 20-symbol P_2 with the unit
    root: T^2 coefficient = 2 (mod 5) (algebraic check of the reduction on the same rounded values); L(E,1)-check 2.9e-14.
  IDENTIFICATION: b/25 ~ 0 under Gamma0(N) and L(E,1) = 0, so c_E lambda(b/25) lies in the rectangular Lambda_E and c_E x_b is in Z,
    with c_E = u c0, u in {1,2}. Certified whenever c_E <= 399575, i.e. c0 <= 199787 without knowing which curve is optimal.
  4547 DOES NOT DIVIDE c0 (operator correction, verified): Edixhoven [Edi91, Thm 3] as stated in Cesnavicius-Neururer-Saha
    (arXiv 1911.09446v3 Sec. 1) and Cesnavicius (arXiv 1703.02951 Sec. 1.2): for the optimal quotient and p >= 11, if E_Qp does not
    have potentially ORDINARY reduction of Kodaira type II/III/IV then ord_p(c) = 0. Both curves of the class: type III at 4547,
    v(j) = 0, j = 1728 (mod 4547), 4547 = 3 (mod 4), hence potentially good SUPERSINGULAR. Primary source (Texel volume) not read.
    With Mazur (p | c0 => p^2 | 4N): c0 = 2^a, and c0 <= 199787 <=> a <= 17 (a <= 18 suffices if the seed is the strong Weil curve).
  CONSEQUENCE (Kato + SW Thm 6.1 upper-bound direction only; no p-adic BSD; no Skinner-Urban):
    IF v_2(c0) <= 17 THEN ord_T L_5(E,T) = 2, v_5(L_5*) = 0, b_5 = 0, Sha(E/Q)[5^inf] = 0.
  STATUS: SMALL_SEED_2243_12_SHA5 = ZERO_CONDITIONAL_ON_V2_C0_LE_17. The only remaining obstruction is 2^18 | c0.
    Published 2-adic results do not close it: CNS Thm 1.2 gives only v_2(c0) <= v_2(deg phi) here (N has primes = 3 mod 4) and deg phi
    is not computable at this conductor; Raynaud's 4 | c => 4 | N is vacuous (8 | N); Edixhoven's E-independent bounds at 2 are
    unpublished (ARS 2006; CNS fn. 3). Manin's conjecture (c0 = 1) implies the condition; it is not assumed.
  REJECTED: unconditional upgrade via Wuthrich 2018 Prop. 1. The proof's last line misplaces c0; the correct form is
    2 #E(Q)_tors c_E [r]+ / c_inf(E) in Z (11a3: c_E = 5, [0]+ = 1/25). The printed unitary statement also fails for curves other
    than the strong Weil curve.
  RESOURCES: 12 threads, 1.7 GB, about 5.9 CPU-h; wall 33.4 min EXCEEDED the 30-min authorization by 3.4 min.
```

## MANIN_2_PRIMARY_GATE_2243_12 — MERGED WITH OPERATOR EDITORIAL CORRECTION (2026-09-18; report ~/BSD_MANIN_2_PRIMARY_GATE_2243_12_2026-09-18/00_REPORT.md sha256 54aa940cbb45fae58a8efd205e784469abc111eb552d69a52030ad856d7bac30, §6 and §8 govern; pre-merge sha256 0a1f03296873adc8a77609d87502cfea27e39db462386104803370a594068a56; prior ledger sha256 d6446744012ae70c3aa44ce1bfecec31a278f198ef1ed54d51190a7faf6093d2)
```
MANIN_2_PRIMARY_GATE_2243_12 — V2_C0_LE_8_DERIVED  (strong Weil curve of the (2243,12) class; referee PASS_WITH_CORRECTIONS;
  operator review (lane 1) independently reconstructed Steps A and B: ACCEPTED)
  DERIVED lemma (not a verbatim theorem; Pasten 2017 Sec. 10 method, sharpened by CNS and made explicit): every optimal E/Q with
  v_2(N) = 3 and some prime = 3 (mod 4) dividing N has v_2(c0) <= 8.
  Step A: X_0(N)_Z(2) has rational singularities (CNS 6.12(c); 3 | N), so H = H^0(X_0(N),Omega) = H^0(Neron J_0(N),Omega^1)
    (CNS 6.2) and omega_f in H is primitive (CNS 5.15). pi pi^v = [deg phi] with T_l (l not | N) self-adjoint and strong
    multiplicity one gives v_2(deg phi) >= v_2(c0) + kappa. deg phi | congruence exponent (ARS12 Thm 3.6(a); operator's review
    read the original) gives v_2(deg phi) <= e' + kappa, where e' = 2-exponent of S_2(Gamma0(N),Z_(2))/H. So v_2(c0) <= e'.
  Step B: the regular model X_{Gamma0(N) cap Gamma1(5)} has four reduced fibre components (a,b), a+b = 3, at 2 (KM 13.4.7 and
    13.5.6 via CNS 5.9; e(a,b) = phi(2^min(a,b)) = 1), all through each of the mu/12 supersingular points (ker F^3). Adjunction +
    genus/cusp counts give pole order K <= 9 - 12c'/mu < 9, so e' <= 8. (K <= 4 if the components are smooth; not used.)
  Sanity (referee, not used in the proof): exact e' = 0, 2, 3, 3 at N = 24, 56, 88, 152; Step A inequalities hold on 56a1, 56b1,
    88a1, 152a1, 152b1.
  Secondary-source dependencies retained: Katz-Mazur (via CNS), Liu 9.1.37, Deuring mass formula, Conrad BDP17 App. B.
  Editorial correction (operator): "No computation was run" -> "No computation is used in the proof; the referee ran independent
    numerical sanity checks."
CONSEQUENCE (with 4547 not | c0): c0 = 2^a, a <= 8; c_E | 2c0 (c_psi | deg psi, CNS Cor 7.3 proof), so c_E <= 512 < 3999 (T1)
  and < 399575 (T2). All 20 [b/25]+ are the recovered integers, a_2(L_5) = 2 (mod 5) unconditionally, and
STATUS: SMALL_SEED_2243_12_SHA5 = PROVED_ZERO   (via the derived v_2(c0) <= 8 lemma)
  ord_T L_5(E,T) = 2, v_5(L_5*) = 0, b_5 = 0, Sha(E/Q)[5^inf] = 0 for the seed (2243,12).
  Uses Kato + Stein-Wuthrich Thm 6.1 (upper-bound direction) only; no Manin conjecture, no p-adic BSD, no Skinner-Urban.
  Supersedes the STATUS line of STEIN_WUTHRICH_P5_LP_RUN_001 (ZERO_CONDITIONAL_ON_V2_C0_LE_17).
NON-CLAIMS: not full BSD for the seed; no l-primary statement for l other than 2 (Zywina: Sha[2] = 0) and 5; analytic rank = 2 is
  not certified (only >= 2: L(E,1) = 0 by Kato/Kolyvagin with rank 2, and root number +1); nothing about other family members.
```
