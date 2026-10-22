"""Part 2: per-prime sufficient criteria, conditional bridges, equivalences and reductions."""
from .common import claim, E, M

P = 'BSD_2243_PILOT_PREP_2026-09-22/'
EV = 'BSD_2243_EVALUATOR_REVIEW_2026-09-23/'
D5 = 'BSD_2243_D5_INDEPENDENT_2026-09-23/'
CX = 'BSD_2243_ACC_CODEX_CHECK_2026-09-23/'
TS = 'BSD_TWIST_SHA_SUPPORT_2026-09-22/'

CLAIMS = [
    claim('B.1', 'Cyclotomic depth-two criterion at good ordinary primes',
          'Let p >= 5 be a prime of good ordinary reduction. If C_p := [T^2]L_p(E,T) is a p-adic unit, then '
          'Sha(E/Q)[p^infinity] = 0. For this curve every hypothesis other than the unit coefficient is automatic: the '
          'residual image is full (A.3), p does not divide #E(F_p) (A.1), the Tamagawa and torsion factors are p-units, and '
          'epsilon_p = (1 - alpha^-1)^2 is a unit because a_p is even and |a_p| <= 2*sqrt(p). C_p mod p is a finite weighted '
          'sum of depth-two modular symbols [b/p^2]^+ (SW Prop. 3.5). This is the argument of S.5, S.7, S.11, S.13.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='application of published theorems (the method of S.7)', section='7',
          evidence=[E(M + 'audits/P7_PRIMARY_THEOREM.md', 'sections 2-3: the argument'),
                    E('BSD_LANE2_SEED_TO_FAMILY_2026-09-18/LANE2_REPORT.md', 'the one-bit form'),
                    E(M + 'FIN_FRONTIER.md', 'section 4, good-ordinary row')],
          depends_on=['A.1', 'A.3', 'A.4', 'R.1'],
          imports=['Kato divisibility (SW Thm 7.3)', 'SW Thm 6.1, good ordinary equality clause (Schneider, Perrin-Riou)', 'SW Prop. 3.5; SW section 4.1'],
          qualifications=['Sufficient, not necessary: C_p = 0 mod p proves nothing.',
                          'At p = 17 the normalized 17-adic regulator has valuation one, so the depth-two coefficient cannot be a unit; a depth-three computation would be needed (recorded in D_primes/01_GATES.md section 2). The user has not authorized p = 17.'],
          role='sufficient witness at each good ordinary prime', label='thm:cyclo'),
    claim('B.2', 'Criterion SS at good supersingular primes',
          'Let p >= 5 be a good supersingular prime (a_p = 0) and r = rank E(Q) = 2 <= p - 1. If the X^r coefficient of the '
          'depth-one Mazur-Tate element theta_1 is nonzero mod p (a finite weighted sum of the symbols [a/p^2]^+), then '
          'Sha(E/Q)[p^infinity] = 0.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='application of published theorems (hostile-audited)', section='7',
          evidence=[E('BSD_SEED_2243_12_CRITERION_SS_HOSTILE_GATE_2026-09-19/CRITERION_SS_HOSTILE_GATE.md', 'verdict CRITERION_SS_VALID_WITH_CORRECTIONS'),
                    E(M + 'FIN_FRONTIER.md', 'section 4, supersingular row: costs')],
          depends_on=['A.3', 'R.4'],
          imports=['Pollack, Duke 2003, Prop. 6.18 (read only through Kim-Kurihara Prop. 1.11 and Pollack-Rubin (10)-(12))',
                   'Kobayashi, Invent. 2003 (read only through restatements)', 'B.D. Kim 2013, Thm 1.1 (via Kitajima-Otsuki)'],
          qualifications=['Four primary texts were read only through restatements (a provenance caveat).',
                          'Not computed for this curve. Estimated 270 and 460 CPU-hours at p = 23 and 29 (cutoffs 1.76e11 and 2.83e11).'],
          verification={'review': 'MODEL_SAME_FAMILY (hostile gate)'}, role='sufficient witness at each good supersingular prime',
          label='thm:ss'),
    claim('B.3', 'Anticyclotomic forward bridge at good ordinary primes (K = Q(sqrt(-7)))',
          'For every prime p >= 5 with p not dividing 7N and E ordinary at p: if c_2(p) is a p-adic unit, then '
          'Sha(E/Q)[p^infinity] = 0. Here c_2(p) is the I^2/I^3 coefficient of the stabilized Gross-point square-root theta '
          'element of Bertolini-Longo-Venerucci over K = Q(sqrt(-7)) (quaternion algebra ramified at 3, 2243, 5843). '
          'Proof skeleton: unit c_2 gives exact augmentation order (the lower order calL_p in I^2 is unconditional, by '
          'Bertolini-Darmon Cor. 3 and K.2); BLV equality gives sigma = 4; Bertolini-Darmon derived heights with s^- = 0 give '
          'Div Sha(E/K)[p^infinity] = 0; the exponent bound v_p(#Sha(E/K)[p^infinity]) <= 2c; then the odd-p decomposition '
          'Sha(E/K)[p^infinity] = A + B with B = Sha(E^{-7}/Q)[p^infinity] finite and Cassels-Tate on B forces A = 0.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED', 'PROVED_COMPUTER_ASSISTED'], origin='new deduction combining published theorems', section='7',
          evidence=[E(TS + 'ORDINARY_LANE_FREEZE.md', 'canonical statement and replay status'),
                    E(TS + 'CASSELS_TATE_SHORTCUT.md', 'the Cassels-Tate step'),
                    E(TS + 'FREEZE_MANIFEST.sha256', 'freeze seal'),
                    E('BSD_ARISTOTLE_ORDINARY_BRIDGE_2026-09-22/returned/GRADING.md', 'grading of the two external audits'),
                    E('BSD_DEFINITE_FIELD_GATE_2026-09-22/STAGE7_A2A_ROUTE_LIVE.md', 'the tau-equivariant route')],
          depends_on=['K.2', 'A.3', 'R.4'],
          imports=['Bertolini-Longo-Venerucci, arXiv:2306.17784 (Math. Ann. 395, 2026), Thm A (statement, Hyp. 1.1, Def. 1.3 read at source)',
                   'Bertolini-Darmon, Annals 2005, Cor. 3 (read at source)',
                   'Bertolini-Darmon, Derived p-adic heights, Thms 2.18, 2.23, Lemma 3.1 (read by two external audits only)'],
          verification={'review': 'two external model audits (both caught that BD Lemma 3.1 sits in a chapter assuming Sha finite and re-derived it without)',
                        'replayed_by_project': 'the A_2 <= c step and the Cassels-Tate classification; NOT replayed: the BLV-BD module identification, BD 2.18(5)/2.23/Lemma 3.1, the odd-p descent'},
          qualifications=['c_2(p) is a different object at each p; the uniform statement is the open frontier.',
                          'Excludes p | 7N and supersingular p.',
                          'An alternative proof at ordinary p via the A3 argument (B.4) is recorded but not substituted in the records.'],
          post_master='New since the master record (frozen 2026-09-22).', role='sufficient witness at each good ordinary p >= 5, p not dividing 7N', label='thm:ordbridge'),
    claim('B.4', 'Anticyclotomic forward bridge at good supersingular primes (A3)',
          ('For every good supersingular prime p >= 5 with p not dividing 7N: M_2(p) != 0 implies '
           "Sha(E/Q)[p^infinity] = 0, where M_i(p) = sum_{j=0}^{p-1} j^i psibar(gamma^j P_1) and P_1 is BLV's "
           'traced conductor-p^2 Gross point. Moreover M_0 = M_1 = 0 unconditionally and bbar_2 = M_2/2, so '
           'ord_T(F^- mod p) = 2 iff M_2(p) != 0. When F^- mod p is nonzero put d=ord_T(F^- mod p), which implies '
           'mu=0 and lambda=d; finite lambda alone does not imply mu=0. Route: BLV Thm 7.1 equality at an '
           'infinite-order character gives no finite submodule; a tau-equivariant freeing-set Poitou-Tate '
           'argument gives rank X^+ = rank X^- = d; d = 2 with rank E(Q) = 2 gives Sha = 0.'),
          'CONDITIONAL', ['PROVED_WRITTEN', 'LEAN_CHECKED', 'IMPORTED_PUBLISHED'], origin='new deduction combining published theorems', section='7',
          evidence=[E('BSD_SUPERSINGULAR_SIGNED_BRIDGE_2026-09-22/SIGNED_MINIMAL_LAMBDA_BRIDGE.md', 'the written proof'),
                    E('BSD_SUPERSINGULAR_SIGNED_BRIDGE_REVIEW_2026-09-22/REVIEW.md', 'source-checked review, verdict PASS'),
                    E('BSD_A3_LEAN_CORE_2026-09-22/A3Core.lean', 'Lean 4 algebraic core (capstone A3_bridge_core)'),
                    E('BSD_A3_LEAN_CORE_2026-09-22/build6.log', 'clean build log'),
                    E('BSD_A3_LEAN_CORE_2026-09-22/REPORT.md', 'hypothesis ledger'),
                    E(TS + 'SUPERSINGULAR_LANE_FREEZE_ADDENDUM_2026-09-22.md', 'promotion record'),
                    E(TS + 'SUPERSINGULAR_LANE_FREEZE_ADDENDUM_ERRATUM_2026-09-22.md', 'wording erratum: sufficient route, not obligation')],
          depends_on=['A.3', 'R.4'],
          imports=['Bertolini-Longo-Venerucci arXiv:2306.17784v2: Thms 5.2, 7.1, 7.3; Props 5.3, 5.9, 5.10, 5.13, 5.15; section 4.3 (checked at source)',
                   'inside BLV: Fouquet-Wan, BSTW, CCSS, Iovita-Pollack, Burungale-Kobayashi-Ota (published; not read by the project)'],
          verification={'lean': 'Lean 4.32.2, Mathlib 905b9581 (v4.32.2): 0 errors, 0 warnings, axioms propext/Classical.choice/Quot.sound only; replay: cd ~/proximity-prize && lake env lean A3Core.lean',
                        'lean_scope': 'the algebraic core of sections 2-4; the arithmetic inputs (I1)-(I4) and structural inputs (S1)-(S4) are hypotheses; modeling steps (M1), (M2) are not formalized',
                        'review': 'MODEL_SAME_FAMILY (source-checked; algebra re-derived)',
                        'release_replay': 'tools/verify_release.py --lean rebuilt A3Core.lean on 2026-09-23 with output identical to build6.log (PASS)'},
          qualifications=['M_2(p) != 0 is open at every prime; no prime is gained by the bridge.', 'Not refereed.'],
          post_master='New since the master record (promoted 2026-09-22 after the Lean replay).',
          role='sufficient witness at each good supersingular p >= 5, p not dividing 7N', label='thm:a3'),
    claim('B.5', 'One forward architecture for every good prime p >= 5, p not dividing 7N',
          'For every good prime p >= 5 with p not dividing 7N: M_2(p) != 0 implies Sha(E/Q)[p^infinity] = 0. At ordinary p, '
          'given M_1 = 0, cbar_2 = c_{p-3}/2 = -M_2/2, where c_i are the Lagrange coefficients of j -> psibar(gamma^j P_1) on F_p.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'LEAN_CHECKED', 'IMPORTED_PUBLISHED'], origin='combination of B.3 and B.4', section='7',
          evidence=[E(TS + 'SUPERSINGULAR_LANE_FREEZE_ADDENDUM_2026-09-22.md', 'section 2'),
                    E('BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_ERRATUM_2026-09-22.md', 'the c_2 / c_{p-3} relation (erratum)'),
                    E('BSD_C2_WITNESS_2026-09-22/REV2_RETURN_INDEPENDENT_CHECK.md', 'independent check of the Lagrange-coefficient formula (p <= 53)')],
          depends_on=['B.3', 'B.4'],
          qualifications=['M2_NONVANISHING is open at every prime (quantifier level zero).',
                          'Excluded primes: 2, 3, 7 and the bad primes 2243, 4547, 5843 (2, 3, 5, 7, 11, 13 are settled by S.P).',
                          'Evaluating M_2(p) requires the quaternionic eigenform on a definite Shimura set of mass about 5.4e14 (builder estimate); no evaluation method is known at any prime.'],
          post_master='New since the master record.', role='sufficient witness', label='thm:unified'),
    claim('B.6', 'The split multiplicative prime 2243: a sufficient certificate, not computed',
          'Let p = 2243 (split multiplicative, alpha = a_p = +1). For b in (Z/p^2)^x let l(b) be congruent to -(b^{p-1} - 1)/p mod p, '
          'and let K = 1024 * sum over b mod +-1 of bal_p(2*C(l(b),3)) * [b/p^2]^+ (SW normalization, plus period omega1). '
          'If K is not congruent to 0 mod 2243, then Sha(E/Q)[2243^infinity] = 0, given mathematical inputs D1-D7: '
          'D1 Skinner Thm A hypotheses (verified); D2 char(X_Gr) = T*char(X_cl) at split p (DISCHARGED at source level: '
          'Skinner 2016 section 3.2 plus a written matching of Selmer local conditions); D3 period comparison (as published); '
          'D4 finiteness first (elementary control argument); D5 nondegenerate split height (CERTIFIED 2026-09-23: '
          'det H = 2181*2243^2 + O(2243^3), Reg_gamma = 2181 mod 2243, by an independent computation); D6 Jones 1989 Thm 3.1, '
          'forward direction (read; hypothesis log_p q_E != 0 holds since l_gamma = 1799 mod 2243); D7 SW Prop. 3.5 and the '
          'lattice (A.4). D8 is a certificate-production requirement, not a hypothesis on the mathematically defined K. K = 0 mod 2243 establishes nothing.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED', 'PROVED_COMPUTER_ASSISTED'], origin='application of published theorems; new independent height certificate', section='8',
          evidence=[E(P + 'S1_RESULTS.md', 'sign, split height and dependency checks'),
                    E(P + 'REPORT.md', 'pilot preparation report: formula, costs'),
                    E(EV + 'dependencies/D2_D5_RECONCILIATION.md', 'D2 discharged; D5 necessary at the retained grade (before the certificate)'),
                    E(D5 + 'PROOF.md', 'the D5 certificate'),
                    E(D5 + 'RESULT.md', 'D5 result'),
                    E(D5 + 'certify_d5.py', 'standard-library certificate program'),
                    E(D5 + 'verify_d5.py', 'separate verifier'),
                    E(D5 + 'VERIFICATION.json', 'verification record'),
                    E(CX + 'MATHEMATICAL_CHECK.md', 'cross-family check of D2/D5 framing and normalization'),
                    E(CX + 'LOCAL_L_INVARIANT.json', 'q_E mod 2243^3 and l_gamma = 1799, a second computation'),
                    E('BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/REPORT.md', 'feasibility and exact certificate consequence')],
          depends_on=['A.3', 'A.4', 'R.1'],
          imports=['Skinner 2016 Thm A and section 3.2 (read at source)', 'Jones 1989 Thm 3.1, split clause, forward direction (read at source)',
                   'Stein-Wuthrich section 4.2 (Werner-corrected split height), section 4.4, Prop. 3.5 (read at source)'],
          normalization=('SW normalization with the plus period omega1 (the full real period 2*omega1 differs by a unit at '
           '2243); ell_gamma = log_p(q_E)/(ord_p(q_E)*log_p(1+p)), congruent to 1799 mod 2243 because '
           'ord_p(q_E)=1.'),
          verification={'D5': 'standard-library exact arithmetic; no PARI/Sage height function; separate division-free verifier; matches PARI residue only after the fact',
                        'engine': 'v2.3 accumulator: arithmetic replays PASS (m = 27, 81); restart isolation FAIL (defect F4, generation reuse after a crash before the first checkpoint); fix proposed, not applied'},
          qualifications=['The coefficient K has NOT been computed. Cost: cutoff T_run = 3.912e13, about 110,623 local '
           'core-hours; modeled cloud scenarios $1,368-$8,059 (central $2,162), not quotes.',
           "The route uses only Jones's forward theorem with finiteness (D4) and independent nondegeneracy (D5); no converse is imported.",
           'Skinner Theorem A is a shared published import. The project has not independently reconstructed its '
           'internal SU normalization; this is not an identified defect in the published theorem.',
           'All stated theorem dependencies retain their source-reading grades. The scalar is uncomputed, and the '
           'existing engine is not authorized for production until its recorded restart defect is repaired.'],
          post_master='Changed since the master record: master section 3 lists "no completed certificates; split case also needs its stated nonzero L-invariant input". The L-invariant input is now supplied (l_gamma = 1799, two computations), D2 is discharged, and D5 is certified. The coefficient itself remains uncomputed.',
          role='sufficient witness for the 2243-primary component', label='thm:2243'),
    claim('B.7', 'The nonsplit multiplicative prime 5843: a sufficient certificate, not computed',
          'At p = 5843 (I2, nonsplit, a_p = -1, c = 2) a single depth-two coefficient mod p is a sufficient certificate via '
          'Skinner Thm A and the nonsplit Jones formula, as at p = 3. Cutoff T_min = 1.687e14; measured-rate estimate about '
          '6.3e5 CPU-hours.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='application of published theorems', section='8',
          evidence=[E('BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/REPORT.md', 'feasibility report')],
          depends_on=['A.3', 'A.4'],
          qualifications=['Not computed; held by the user. The R2-type period-comparison question may recur at p | N.'],
          role='sufficient witness for the 5843-primary component', label='thm:5843'),
    claim('B.8', 'The additive prime 4547: only a semi-decision, and the route is blocked',
          ('At 4547 (type III, potentially supersingular, U_p-eigenvalue 0), the retained records do not supply a '
           "cyclotomic p-adic L-function/main-conjecture/control chain in the required form. They do record Kim's "
           'two-prime Kurihara sufficient witness; existence is not established here. The smallest recorded '
           'admissible pair has product about 8.1e15, infeasible for the costed direct evaluator. This is a '
           'project boundary, not nonexistence of all possible local theories or algorithms.'),
          'OPEN', ['PROVED_WRITTEN'], origin='source audit', section='8',
          evidence=[E(M + 'FIN_FRONTIER.md', 'section 4, 4547 row'), E(M + 'MASTER_BSD_DAG.md', 'section 3 table')],
          qualifications=['Both the unevaluated sufficient witness and its retained import grades remain. No impossibility '
           'theorem for this prime is claimed.'],
          label='prop:4547'),
    claim('B.9', 'Ordinary-tail equivalence O1',
          'Let S0 = {2, 3, 5, 2243, 4547, 5843}. For every good ordinary prime p outside S0: h_p = 0 if and only if '
          'Sha(E/Q)[p^infinity] = 0, where h_p is the witness depth of Ota\'s theta elements over admissible auxiliary pairs.',
          'EQUIVALENCE', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT', 'IMPORTED_PUBLISHED'], origin='new deduction from published and preprint sources', section='9',
          evidence=[E('BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md', 'Theorem O1 and its limits'),
                    E('BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/EXACT_WC_ANTECEDENT.md', 'definition of h_p')],
          depends_on=['A.3', 'A.4', 'R.4'],
          imports=['Castella-Sano arXiv:2601.14504v1, Thm B (preprint)', 'C.-H. Kim arXiv:2203.12159v6, Thm 1.10', 'Ota, Thms 5.17 and 6.4'],
          qualifications=['Uniform primitive witnesses on the ordinary tail are exactly uniform vanishing there: an equivalence, not a reduction.',
                          'No positive-depth or supersingular converse, and no global statement J_E != 0 iff FIN.'],
          label='thm:o1'),
    claim('B.10', 'Division-field reduction',
          'For p >= 7 outside {19, 59, 487, 2243, 4547, 5843}, let C_p = Hom_{GL_2(F_p)}(Cl(Q(E[p]))/p, E[p]). Then '
          'Sha(E/Q)[p] = 0 if and only if dim C_p <= 2; and dim C_p >= 1 always.',
          'EQUIVALENCE', ['PROVED_WRITTEN'], origin='new written reduction', section='9',
          evidence=[E('BSD_CODEX6_DIVISION_FIELD_HORIZONTAL_2026-09-19/DIVISION_FIELD_REDUCTION_THEOREM.md', 'the theorem'),
                    E('BSD_CODEX6_DIVISION_FIELD_HORIZONTAL_2026-09-19/LOCAL_CONDUCTOR_AND_MODULES.md', 'local modules')],
          depends_on=['A.3', 'R.1'],
          qualifications=['The excluded set bounds only the applicability of the simplified reduction, not the Sha primes.',
                          'The global upper bound on C_p is open and equivalent to the desired vanishing.'],
          label='thm:divfield'),
    claim('B.11', 'LINE and witness content (conditional algebra)',
          'LINE postulates one rational scalar a/b with b*delta_n = a*rho_n at all required auxiliary pairs and primes; the '
          'conditional theorem gives finite primary groups at the covered good primes and vanishing away from the numerator '
          'support. Witness content weakens this to a nonzero integer A in J_E. The finite algebra of both conditional '
          'implications is formalized in Lean (A1/A2 freeze).',
          'CONDITIONAL', ['PROVED_WRITTEN', 'LEAN_CHECKED'], origin='new conditional theorems', section='9',
          evidence=[E('BSD_SEED_2243_12_LINE_HOSTILE_AUDIT_2026-09-19/LINE_HOSTILE_AUDIT.md', 'hostile audit'),
                    E('BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md', 'witness-content theorem and countermodels'),
                    E('BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/FORMALIZATION_BOUNDARY.md', 'what A1/A2 do and do not formalize'),
                    E('BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/FREEZE_INDEX.md', 'frozen archives A1 baa04352..., A2 fd55eab3...')],
          qualifications=['The arithmetic antecedents (the cross-prime scalar; A != 0) are unproved.',
                          'The determinant-line version that needed finiteness to define its comparison is withdrawn as an unconditional equivalent.'],
          label='thm:line'),
    claim('B.12', 'Local structure of the Selmer groups at settled primes',
          'At p in {2, 3, 5, 7, 11} the rational p-adic Selmer group is Q_p*delta(P1) + Q_p*delta(P2); at p = 5, 7, 11, '
          'Sel_{p^n}(E/Q) = (Z/p^n)^2 for all n, and the kernel of localization at p is the line spanned by '
          'log_p(P2)*delta(P1) - log_p(P1)*delta(P2). At 11, with S = {infinity, 2, 3, 11, 2243, 4547, 5843}, the kernel of '
          'loc_S on Sel_11 is F_11*delta_11(2P1 - P2) (exact local coordinates lambda_11(P1) = 1, lambda_11(P2) = 2).',
          'THEOREM', ['PROVED_WRITTEN', 'EXACT_COMPUTATION'], origin='standard deduction plus an exact computation', section='9',
          evidence=[E(M + '_work/bridge_repair_assessment_2026-09-21/ASSESSMENT.md', 'short proof'),
                    E(M + '_work/bridge_repair_assessment_2026-09-21/C11_LOCALIZATION_JOIN.md', 'the mod-11 computation')],
          depends_on=['S.P', 'R.1'],
          qualifications=['Kummer membership only; it does not construct any proposed class. The same argument applies at 13 given S.13 (routine; not separately recorded).'],
          label='prop:localsel'),
    claim('B.13', 'Heegner-Stark Fitting identities over Q(sqrt(-23))',
          'For good ordinary p >= 5, p not in {19, 59, 487}, p not dividing #E(F_p), a written source composition (BCK Thm A, '
          'Kataoka-Sano Prop. 5.12, the Macias Castillo-Sano determinant comparison) gives the base-layer Heegner Stark-system basis '
          'and classical Selmer Fitting identities at every depth over a suitable imaginary quadratic field. With K = Q(sqrt(-23)) '
          '(K.1): Fitt^i(Sha(E/K)[p^n]^*) = I_{i+3}(eps^Hg_{n,0}), valid at p = 13, 31, 41, 47, 71, 73, 101, 127, 139, 151 among p <= 160.',
          'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT', 'IMPORTED_PUBLISHED'], origin='new source composition', section='9',
          evidence=[E(M + '_work/bridge_repair_assessment_2026-09-21/MCS_NONSQUAREFREE_JOIN.md', 'the composition'),
                    E(M + '_work/bridge_repair_assessment_2026-09-21/MCS_DERIVED_HEIGHT_GATE.md', 'the derived-height correction'),
                    E(M + '_work/bridge_repair_assessment_2026-09-21/D23_COVERAGE_REVIEW.md', 'applicability through 160'),
                    E('BSD_TWIST_D23_CERTIFICATE_2026-09-21/SCOPE_AT_13.md', 'the 13-primary scope over K')],
          depends_on=['K.1'],
          qualifications=['The arithmetic ideals are unevaluated. The Heegner Lambda-index does not determine I_3 (explicit counterexample).',
                          'I_3 = F_13 would need Sha(E^{-23}/Q)[13] = 0 as well as the seed\'s 13-part; the twist part is not supplied (see W.1).'],
          label='thm:mcs'),
    claim('B.14', 'An effective constant from any fixed integral model (Lean)',
          'For a matrix-presented model: if the k x k minors of a fixed integer matrix A specialize so that I_3(p) = F_p iff some '
          'minor is nonzero mod p, and one unit specialization exists, then C_1 := |gcd of the k x k minors| is nonzero, and '
          'I_3(p) != F_p implies p | C_1.',
          'CONDITIONAL', ['LEAN_CHECKED'], origin='new formal lemma', section='9',
          evidence=[E('BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22/review_2026-09-22/SYNTHESIS_AB.md', 'record of the returned Lean lemmas'),
                    E('BSD_FRONTIER_FREEZE_2026-09-22/CORRECTION_2026-09-22_I3_AT_13.md', 'the premise at 13 is not established')],
          qualifications=['No integral model is constructed, and no unit specialization is established (the claimed one at 13 is withdrawn, W.1).'],
          post_master='New since the master record.', label='lem:minors'),
    claim('B.15', 'The ordinary stabilization correction is invisible in the witness quotient',
          'For p >= 5 the norm element N = sum_{i<p}(1+t)^i lies in p*Lambda + I^3, so the alpha-stabilization correction in the '
          'ordinary theta measure does not affect the degree-two witness mod (p, I^3). Norm coherence of the stabilized elements '
          'holds conditionally on an explicit three-term relation H1 (source audit pending).',
          'CONDITIONAL', ['PROVED_WRITTEN'], origin='new (elementary for the invisibility; conditional for coherence)', section='9',
          evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'section 1, theta branch')],
          qualifications=['Conditional algebra; the ancestor object is still p-dependent.'], post_master='New since the master record.',
          label='prop:invis'),
]
