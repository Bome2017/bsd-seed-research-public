"""Part 3: stopped routes. Each carries its stop kind and its precise scope; nothing is claimed outside the scope."""
from .common import claim, E, M, V25

A = M + 'audits/'
CMP = 'BSD_2243_COMPRESSION_ATTEMPT_2026-09-23/'

CLAIMS = [
    claim('X.1', 'Integral sources do not bound prime support',
          'The maps Z -> Z_p, 1 -> p^2, are nonzero at every prime with nonunit image at every prime; the two-term complex with '
          'diagonal differential (p^2)_p over prod_p Z_p is perfect with finite nonzero defects at infinitely many primes. So '
          'source integrality, profinite perfectness, pointwise nonvanishing and pointwise finite primary groups do not imply finite support.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='elementary countermodels', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='the inference "integral/perfect source => finite support"; a fixed nonzero integer C with Sha[p] != 0 => p | C would still prove finite support',
          evidence=[E('BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md', 'countermodels'),
                    E('BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md', 'lemmas')], label='obs:support'),
    claim('X.2', 'Localization determinants of the known points do not see the quotient',
          'An invertible localization matrix on <P1,P2>/p does not show that Sel_p/(E(Q)/p) vanishes (abstractly, an isomorphism '
          'on M in 0 -> M -> M + Q -> Q -> 0 says nothing about Q). The paused seed experiment also rules out one scalar matching '
          'all raw determinants up to nonzero factors.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='elementary; paused experiment', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='raw localization determinants of the two known points; determinants coupled to independently controlled classes are outside it',
          evidence=[E('BSD_CODEX6_SEED_INVENTION_2026-09-19/INTEGER_LIFT_OBSTRUCTION.md', 'determinant obstruction'),
                    E('BSD_CODEX6_SEED_INVENTION_2026-09-19/STATE.json', 'paused, unsealed state')], label='obs:det'),
    claim('X.3', 'The Destrempes-Malinin lifting mechanism is false',
          'The implication "alpha in a prime P above p => Tr(alpha) in pZ" fails (in Q(i), 4 + i lies above 17 with trace 8). The '
          'audit also gives contradictions in the division-field setting, rules out finite universal lift sets and disproves the '
          'proposed fixed-field universal local coverage. The set {7, 13, 2243, 4547, 5843} is therefore not an established Sha-exception set.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='counterexample', section='10', stop_kind='DEFECTIVE_SOURCE',
          scope='the paper\'s stated lifting mechanism', evidence=[E('BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/PROOF_AUDIT.md', 'audit'),
                    E('BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/TRACE_AND_FIXED_FIELD_OBSTRUCTION.md', 'obstruction proofs')], label='obs:dm'),
    claim('X.4', 'Eisenstein congruences give selected subspaces only',
          'Nonclassical weight-two methods reach Hom(B_aut, F_p) -> Sel_p(E) after local checks; the image is the subspace of '
          'extensions factoring through the chosen automorphic quotient, and nothing bounds its complement. Separately, 1 + rho_E '
          'has Hodge-Tate weights {0,0,1}, irregular for classical GL(3) cohomology.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='source audit', section='10', stop_kind='UNSUCCESSFUL_ATTEMPT',
          scope='the examined Eisenstein/GL(3) constructions; not an impossibility theorem for every nonclassical upper bound',
          evidence=[E('BSD_CODEX6_FIXED_EISENSTEIN_GATE_2026-09-19/EISENSTEIN_TYPE_AND_DIRECTION_AUDIT.md', 'audit'),
                    E('BSD_CODEX6_FIXED_EISENSTEIN_GATE_2026-09-19/PRIMARY_SOURCE_AUDIT.md', 'sources')],
          qualifications=['The defect is absence of coverage, not arrow direction (see W.2).'], label='obs:eis'),
    claim('X.5', 'Finite logarithmic realizations of the Mellin period are excluded in the stated class',
          'Nonconstant polynomials in l(z) have infinite cusp-translation span; the ordinary infinitesimal Tate deformation does '
          'not give the asserted jet; the half-ray maps to a null-homotopic loop in E; finite algebraic connections, iterated '
          'integrals and finite exact corrections in class L3 cannot supply the local identity. Also J_j = (1 + (-1)^j) H_j for '
          'half-ray/full-ray moments.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='new written proofs', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='the constructions M1-M4 and the finite class L3; not an independently established scalar equality from another construction',
          evidence=[E('BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md', 'M1-M4'),
                    E('BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/EXACT_CORRECTION_OBSTRUCTION.md', 'L3'),
                    E('BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/LOWER_MOMENT_AND_ENDPOINT_GATE.md', 'moments')],
          depends_on=['Q.4'], label='obs:mellin'),
    claim('X.6', 'Both single-vertex Eisenstein completions miss the Mellin period (certified residuals)',
          'For the automorphic second-jet decomposition, the integral of alpha_f times E\'\'(z,0) over gamma equals '
          'L\'\'(E,1)/2 + Delta. The midpoint-maximal-compact completion has 0.000535614030 <= Delta_mid <= 0.000801512867; the '
          'Fricke-symmetrized endpoint completion has 0.000757821864 <= Delta_* <= 0.000841639764. Both residuals are positive, so '
          'neither completion reproduces the weighted Mellin period.',
          'OBSTRUCTION', ['PROVED_COMPUTER_ASSISTED', 'PROVED_WRITTEN'], origin='new certificates', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='the two single-vertex Fricke-symmetrized completions of the specified segment; arbitrary mixtures in the invariant span are outside it',
          evidence=[E(A + 'AUTOMORPHIC_SECOND_JET_EXPERIMENT.md', 'decomposition'),
                    E(A + 'AUTOMORPHIC_MIDDLE_ORBIT_CLASSIFICATION.md', 'orbit classification'),
                    E(A + 'MIDPOINT_DELTA_INTERVAL.md', 'midpoint certificate'),
                    E(A + 'ENDPOINT_VERTEX_COMPLETION_TEST.md', 'endpoint certificate')], label='obs:jet'),
    claim('X.7', 'Further midpoint analyses (trace, Mellin, Green kernel, secondary descent)',
          'TRACE_ZERO_BUT_I0_NOT_FORCED (the U_4547 trace sums the translated periods to zero without forcing the zeroth one); the '
          'normalized shifted-convolution family has a nonzero continuous Mellin density, excluding an ordinary Dirichlet series or '
          'Euler product (not isolated special values); PARTIAL_KERNEL_MATCH with the Berndt-Kuehn Eisenstein series (no arithmetic '
          'Green-current identification); SECONDARY_CLASS_OBSTRUCTED for the relative/holomorphic Deligne-regulator interpretation '
          'on compact X_0(N) (nonzero curvature, no smooth cusp extension).',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='new written analyses', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='each verdict is scoped in its report; none excludes singular-current theories or isolated identities',
          evidence=[E(A + 'MIDPOINT_UP_TRACE_TEST.md', 'trace'), E(A + 'MIDPOINT_GLOBAL_MELLIN_REDUCTION.md', 'Mellin'),
                    E(A + 'MIDPOINT_GREEN_KERNEL_TEST.md', 'Green kernel'), E(A + 'MIDPOINT_SECONDARY_DESCENT_TEST.md', 'descent')],
          label='obs:midpoint'),
    claim('X.8', 'Broad curvature orthogonality',
          'For every global C^1 scalar J on Y_0(N) with polynomial/logarithmic growth of J and its first derivatives at every cusp, '
          'and every holomorphic weight-two cusp differential alpha_f, the integral of alpha_f wedge dJ over Y_0(N) is 0.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='new written proof (Stokes with zero cusp flux; independent Eisenstein unfolding)', section='10',
          stop_kind='PROVED_OBSTRUCTION',
          scope='unweighted full-domain area pairings from moderate-growth scalar jets; not singular, multivalued, nonexact or boundary-flux constructions',
          evidence=[E(A + 'CURVATURE_AREA_TEST.md', 'proof')], label='thm:curv'),
    claim('X.9', 'Visibility gives no horizontal gain',
          'Varying-level visibility covers all relevant classes (Tamiozzo, Zhang) for each fixed residual prime, but: any finite '
          'stock of auxiliary primes serves only finitely many p (p | D_l = (l+1)^2 - a_l^2); p-unit functorial descent to a fixed '
          'ambient is obstructed; and for a fixed embedding, eventual fixed-ambient visibility on the ordinary tail is equivalent '
          'to eventual ordinary Sha vanishing.',
          'OBSTRUCTION', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='new written deduction', section='10', stop_kind='EQUIVALENT_REFORMULATION',
          scope='finite auxiliary stocks and functorial descent of the constructed ambients; no universal impossibility for unrelated fixed-level proofs',
          evidence=[E(A + 'fixed_visibility_2026-09-19/FIXED_VISIBILITY_AUDIT.md', 'audit and proofs')],
          imports=['Tamiozzo (public 2024 manuscript body read)', 'Zhang 2014, Hypothesis heart (published)'], label='obs:vis'),
    claim('X.10', 'Torus and vector extensions retain exactly the unknown Sha',
          ('For a number field k, an abelian variety A/k and a commutative extension 0 -> G_m^s -> G -> A -> 0, '
           'the natural map Sha^1(k,G) -> Sha(k,A) is an isomorphism; similarly for vector groups and '
           'quasi-trivial tori, and on l-primary parts for tori split by an extension of degree prime to l. The '
           "seed's extension by a split torus by the two points is anti-affine."),
          'OBSTRUCTION', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='elementary deductions from standard inputs', section='10',
          stop_kind='PROVED_OBSTRUCTION', scope='toric/vector packaging as a difficulty reduction; arithmetic volumes and mixed motives are outside it',
          evidence=[E(M + '_work/active_full_bsd/WORKING.md', 'calculation and collision check')],
          imports=['Brion, anti-affine groups, section 2.1 and Prop. 2.1', 'Milne, Class Field Theory (Brauer-Hasse-Noether etc.)'], label='obs:torus'),
    claim('X.11', 'Finite local data and first-derivative formulas do not reach the second derivative',
          'Totally positive quadratic integers can approach 36 while matching arbitrary finite local data; known first-derivative '
          'formulas vanish on this seed; L(E/K,s) = L(E,s)L(E^K,s) supplies no second-derivative comparison.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='quantitative counterexamples', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='those inferences', evidence=[E('BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/QUANTITATIVE_ALGEBRAICITY_THEOREM.md', 'counterexamples'),
                    E('BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/LEMMA_U_AND_P5_UNIT_AUDIT.md', 'unit audit')], label='obs:local'),
    claim('X.12', 'A fixed rank-three ambient model is equivalent to finite lane support',
          'Inside the finitely generated module class, a fixed rank-3 ambient base-change model over Q(sqrt(-23)) is equivalent to '
          'finite lane support (M = Z^3 + T gives dim(M/p) = 3 outside the invariant factors of T, while dim Sel(K,E[p]) = 3 + '
          'dim Sha(E/K)[p]); a bounded variant gives only #Sha[p] <= p^(B-3).',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='new elementary deduction', section='10', stop_kind='EQUIVALENT_REFORMULATION',
          scope='the fixed-ambient base-change class; not a no-go for integral Selmer complexes',
          evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'Stark branch parked'),
                    E('BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22/review_2026-09-22/BRANCH_STARK_PARKED.md', 'record')],
          post_master='New since the master record.', label='obs:stark'),
    claim('X.13', 'No unit-root stabilization at supersingular primes',
          'For p >= 5 supersingular over Q, a_p = 0, so X^2 + p has roots of valuation 1/2 and there is no unit root; the '
          'relation collapses to pr^2(theta_{n+2}) = -p*theta_n. The ordinary mechanism cannot be base-changed; A3 (B.4) uses '
          'signed objects instead.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='elementary', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='the unit-root stabilization lane', evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'supersingular constraint')],
          label='obs:ssunit'),
    claim('X.14', 'The prime-by-prime ladder: stopped at 13, resumed through 47, stopped again',
          'The ladder of fixed-prime certificates was stopped at 13, resumed through 47 with the singleton certificates of S.17-47, and '
          'stopped again on 2026-09-27. Settling the smallest unsettled prime moves only the conditional threshold (2601 at 17, then '
          '25,281 at 53 after S.17-47); a prime settled out of order does not move it, and no finite list of settled primes reaches the '
          'infinite tail or establishes finite support. Depth three at 17 was a feature of the earlier cyclotomic criterion (B.1), not a '
          'requirement of the singleton route that settled 17.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='decision record', section='10', stop_kind='PROCEDURAL',
          scope='a stopping decision; the criteria (B.1, B.2 and the singleton criterion of S.17-47) remain valid prime by prime',
          evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'prime ladder'), E(V25.BATCHC, 'the ladder through 47 and the bound 25,281'),
                    E(V25.DRAFT, 'governing claim delta (X.14)')], depends_on=['S.17-47'],
          post_master='Changed since the master record: resumed through 47 and stopped again (2026-09-27).', label='obs:ladder'),
    claim('X.15', 'No Manin/Hecke/Atkin-Lehner compression of the 2243 certificate',
          'K is congruent mod p to c_3 = [T^3] sum_j Y_j (1+T)^j, where Y_j are the column sums of the depth-two symbol matrix in '
          'Teichmueller/Fermat-quotient coordinates. U_p traces fix only row sums (hence only c_0). The Atkin-Lehner W_Q pairing '
          'x_{u_b} = -x_b (u_b = (Qb)^-1, Q = N/p) maps column j to -1989 - j and makes (1+T)^{1989/2} theta odd in '
          'W = T(1+T)^{-1/2}; it fixes c_0 = 0, c_2 = -995 c_1 and c_4 = 1247 c_3 + 511 c_1 but leaves c_3 free (exact rank 2 > 1 '
          'over F_2243). Loops need scale >= N (actual loops 10^8-10^9 times the current scale), W_p/W_N moves >= 16x, T_5 costs '
          '6.65x, aggregation 1.216x, Kolyvagin denominators about 5e11x, and the level-N or weight-2244 symbol spaces have '
          'dimension 10^15-10^16.',
          'OBSTRUCTION', ['PROVED_WRITTEN', 'EXACT_COMPUTATION'], origin='new', section='10', stop_kind='PROVED_OBSTRUCTION',
          scope='the relations examined (U_p; W_Q, W_p, W_N; Gamma_0(N) loops; T_l, U_l; Hida; Galois conjugacy; aggregation; Kolyvagin); not a lower bound for every algorithm',
          evidence=[E(CMP + 'REPORT.md', 'report'), E(CMP + '02_DERIVATION.md', 'derivation'), E(CMP + '03_WORKLOAD.md', 'workload'),
                    E(CMP + 'checks/p2243_relation_rank.py', 'exact rank computation'), E(CMP + 'checks/p2243_relation_rank.txt', 'its output'),
                    E(CMP + 'checks/check_wq_pairing.txt', 'pairing verified on certified m = 27, 81 tables'),
                    E(CMP + 'checks/cusp_orbit_scales.txt', 'exact orbit-scale checks')],
          depends_on=['B.6'], post_master='New since the master record (2026-09-23).', label='obs:compress'),
    claim('X.16', 'The bad-prime certificates are unaffordable at the authorized budget',
          'Historical route-specific models, retained: 2243: cutoff 3.912e13, about 1.1e5 local core-hours (about 1.1 years on the 20-core host); modeled cloud all-in '
          '$1,368 low / $2,162 central / $3,947 high spot / $5,762 on demand / $8,059 worst (modeled scenarios, not quotes). '
          '5843: cutoff 1.687e14, about 6.3e5 CPU-hours. The 2243 evaluator also has an open restart-isolation defect (F4). '
          'A second model, for the singleton criterion B.18 at the smallest auxiliaries (4547: l = 27,283; 5843: l = 35,059; 2243: '
          'l = 71,777; quarter-tail cutoffs 1.03e13, 1.33e13 and 2.75e13), gives about 24k, 32k and 74k local core-hours for coefficient '
          'production, verification and accumulation; merge, I/O, initialization, restart and acceptance are not priced. In the current '
          'evaluator the retained checkpoint files alone need at least 0.80, 1.34 and 5.80 TB, beyond the recorded local free space. '
          'Disposition: HOLD.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='measured rates and models', section='10', stop_kind='UNAFFORDABLE',
          scope='a budget decision, parked by the user; not a mathematical stop',
          evidence=[E('BSD_2243_PILOT_PREP_2026-09-22/REPORT.md', 'costs'), E('BSD_2243_PILOT_PREP_2026-09-22/S4_cost/S4_COST_RECONCILIATION.md', 'cost reconciliation'),
                    E('BSD_2243_EVALUATOR_REVIEW_2026-09-23/REPORT.md', 'evaluator verdicts'), E('BSD_2243_ACC_CODEX_CHECK_2026-09-23/REVIEW.md', 'cross-family review (F4)'),
                    E('BSD_2243_EVALUATOR_REVIEW_2026-09-23/REMAINING_BEFORE_PRODUCTION.md', 'what remains before production'),
                    E(V25.COST, 'audit of the singleton cost screen: reproduced models, storage bound, corrections F1-F6'),
                    E(V25.BHC + 'REVIEW.md', 'the criterion being costed'), E(V25.DRAFT, 'governing claim delta (X.16)')],
          qualifications=['Both are cost models, not intrinsic computational lower bounds: neither shows that paid computation is necessary, or that no other algorithm or certificate could be cheaper.',
                          'Modeled rates interpolate measured anchors; the dollar figures are scenarios, not quotes or spending recommendations.'],
          depends_on=['B.6', 'B.7', 'B.18'], post_master='New since the master record; the singleton cost model was added on 2026-09-27.', label='obs:cost'),
    claim('X.17', 'Procedural and unsuccessful stops',
          'RS2 cross-cusp kernel: archived by a stopping rule, with a source-qualified analytic identity; not a nonexistence '
          'result. MCS Heegner-Stark: I_3 has no evaluation method. c_2 witness: bounded attempt closed, open at every prime. '
          'Saito-Kurokawa/GSp4: the tangent inequality bounds the eigenvariety by the Selmer dimension and cannot be inverted. '
          'H9 generalized Kato classes: the comparison with the rational-point subspace is missing. The p = 5 Castella-Hsieh branch '
          'misses the calibrated strict line.',
          'OBSTRUCTION', ['PROVED_WRITTEN'], origin='records', section='10', stop_kind='UNSUCCESSFUL_ATTEMPT',
          scope='each named construction only; RS2 is procedural, not refuted',
          evidence=[E('BSD_FABLE_RS2_L3_2026-09-20/ARCHIVE_NOTE.md', 'RS2 archive note'),
                    E(M + '_work/bridge_repair_assessment_2026-09-21/MCS_RETURN_REVIEW.md', 'MCS review'),
                    E('BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_2026-09-22.md', 'c_2 grading'),
                    E('SEED_2243_12_MECHANISM_LANES_2026-09-18/00_LANE1_SYNTHESIS.md', 'Castella-Hsieh calibration')], label='obs:misc'),
]
