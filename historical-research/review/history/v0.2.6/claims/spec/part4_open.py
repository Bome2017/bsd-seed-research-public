"""Part 4: open obligations, historical family results (other curves), and the withdrawn/superseded register."""
from .common import claim, E, M, V26

D = 'Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/'

CLAIMS = [
    # ------------------------------------------------------------------ O: open obligations
    claim('O.1', 'FIN', 'Sha(E/Q) is finite.', 'OPEN', [], origin='BSD obligation', section='11',
          evidence=[E(M + 'MASTER_BSD_DAG.md', 'sections 1, 3, 7'), E(V26.TI + 'V026_SCOPE.md', 'item 4: the current known frontier for the uniform step')],
          qualifications=['Equivalently (S.K): every primary component finite and Sha[p] = 0 for almost all p.',
                          'Remaining regimes: good ordinary p >= 53; good supersingular p >= 53 (infinitely many, by Elkies; 131, 167, 281, ...); the bad primes 2243, 4547, 5843. The primes p <= 47 are settled (S.P, S.17-47).',
                          'Current known frontier for the uniform step (B.20-B.22): ' + V26.TARGET + ' No applicable theorem was located in the screened sources. Together with finiteness of the primary components at the primes of S, this target would give FIN.'],
          role='necessary', label='open:fin'),
    claim('O.2', 'ORDER9', 'If Sha(E/Q) is finite, its order is 9.', 'OPEN', [], origin='BSD obligation', section='11',
          evidence=[E(M + 'MASTER_BSD_DAG.md', 'section 3')], depends_on=['S.FIN', 'S.U'],
          qualifications=['FIN alone permits 9t^2 with every prime factor of t at least 53 (S.FIN); a proof that #Sha < 25,281 given FIN, or the uniform '
           'bound (U), would suffice.',
           'Any nonzero bad-prime component would contribute at least 2243^2 to the order.',
           'The uniform bound #Sha[n]<2601 for every n is equivalent to FIN together with ORDER9, not to the '
           'conditional assertion ORDER9 alone.'],
          role='necessary', label='open:order9'),
    claim('O.3', 'Q36', 'q = L\'\'(E,1)/(2*Omega_E*Reg) = 36.', 'OPEN', [], origin='BSD obligation', section='11',
          evidence=[E(M + 'MASTER_BSD_DAG.md', 'section 4')], depends_on=['R.6', 'Q.1', 'Q.2', 'Q.3'],
          qualifications=['No p-adic-to-real comparison is currently available; this is narrower than "p-adic work cannot supply FORMULA".',
                          'Even q = 36 leaves ORDER9 to prove.'], role='necessary', label='open:q36'),
    claim('O.4', 'The prime-uniform integral witness (frontier question)',
          'Is some currently p-adic sufficient witness (c_2(p), M_2(p), I_3(p), C_p, ...) the specialization of a single integral, '
          'prime-independent object whose nonvanishing or defect is controlled by one fixed integer? A positive answer with the '
          'supersingular and bad-prime regimes covered would give finite prime support.',
          'OPEN', [], origin='research question', section='11',
          evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'status set: PRIME_UNIFORM_INTEGRAL_WITNESS = OPEN')],
          qualifications=['In analytic rank one the answer is the Heegner index (conductor-one object); for this curve the corresponding rank-one quantity over Q(sqrt(-23)) is infinite because rank E(K) = 3.'],
          post_master='New formulation since the master record.', label='open:uniform'),

    # ------------------------------------------------------------------ H: other curves (context only)
    claim('H.1', 'Run013: a qualified full-BSD twist family of 62a1',
          'Conventional 2-isogeny descent for twists of 62a1 by primes q = 5 mod 8 with (q/31) = -1 gives algebraic rank zero and '
          'trivial 2-primary Sha (relative natural density 1/8); a qualified full-BSD assembly uses Zhai and Banwait-Huang.',
          'HISTORICAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='earlier project result (other curves)', section='A',
          evidence=[E('run013-62a1-bsd2-2026-08-22/PROOF.md', 'proof ledger'), E('run013-family-minimisation-successor-2026-09-10/PROPOSITIONS_A_B.md', 'minimization')],
          qualifications=['Rank-zero chains consume L(E,1) != 0 and do not transfer to this rank-two seed.'], label='hist:run013'),
    claim('H.2', 'The 66b1 family',
          'The parallel qualified assembly for primes q = 5 mod 8, (q/3) = -1, (q/11) = 1.',
          'HISTORICAL', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='earlier project result (other curves)', section='A',
          evidence=[E(D + '66B1_CONVENTIONAL_FREEZE_001/THEOREM_STATEMENT.md', 'statement'),
                    E(D + '66B1_CONVENTIONAL_FREEZE_001/LITERATURE_DEPENDENT_STRONG_BSD_COROLLARY.md', 'qualified assembly')], label='hist:66b1'),
    claim('H.3', 'H41 mod-4 successor',
          'Integral character coordinates obtained before the component-group quotient close the retained positive/negative H41 '
          'twist-family arguments at their qualified tier (conventional proof with model reviews).',
          'HISTORICAL', ['PROVED_WRITTEN'], origin='earlier project result (other curves)', section='A',
          evidence=[E(D + 'H41_MOD4_SUCCESSOR_ADDENDUM_018/ADDENDUM.md', 'addendum'), E('H41_MOD4_SUCCESSOR_PROOF_2026-09-16/PROOF.md', 'proof')], label='hist:h41'),
    claim('H.4', 'Gate-R: Lean point-group bridge for E_{r,q}',
          'For E_{r,q}: y^2 = x^3 + (1-2r)qx^2 + r^2q^2x, r = +-2^m, m >= 3, under the frozen Params/H41 hypotheses, the Lean '
          'chain P01/P03/P04 reaches E_{r,q}(Q)/2E_{r,q}(Q) = Z/2, Gate-R proves rank zero, and the finiteness freeze proves '
          'E_{r,q}(Q) finite (finiteness of the rational-point group, not of Sha).',
          'HISTORICAL', ['LEAN_CHECKED'], origin='earlier project result (other curves)', section='A',
          evidence=[E(D + 'GATE_R_FINITENESS_FORMALIZATION_FREEZE_001/STATUS.md', 'finiteness freeze'),
                    E(D + 'GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001/STATUS.md', 'rank assembly')],
          qualifications=['Recorded Lean builds; no fresh rebuild in this release (build artifacts were reclaimed).'], label='hist:gater'),
    claim('H.5', 'H9R16-C geometric milestone',
          'The compatible Hom-valued Jacobian point tower with integral finite-level compatibility constant one, at its recorded '
          'model-audit tier; explicit nonclaims exclude descent to E(Q), non-torsion, and the arithmetic application.',
          'HISTORICAL', ['PROVED_WRITTEN'], origin='earlier project result', section='A',
          evidence=[E('H9R16C_SEALED_MILESTONE_2026-09-15/00_MILESTONE.md', 'milestone'), E('H9R16C_SEALED_MILESTONE_2026-09-15/05_NON_CLAIMS.md', 'nonclaims')],
          label='hist:h9'),

    # ------------------------------------------------------------------ W: withdrawn or superseded (do not resurrect)
    claim('W.1', 'WITHDRAWN: "C_1 != 0 is forced by the unit specialization at p = 13"',
          'Over Q(sqrt(-23)), I_3 = F_13 requires Sha(E/Q)[13] = 0 and Sha(E^{-23}/Q)[13] = 0; only the seed\'s part is supplied. '
          'There is no certified unit specialization at 13, and C_1 != 0 is not established.',
          'WITHDRAWN', [], origin='correction', section='B',
          evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/CORRECTION_2026-09-22_I3_AT_13.md', 'correction'),
                    E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'the withdrawn wording (lines 111-112) is preserved unedited')], label='w:i3'),
    claim('W.2', 'WITHDRAWN: the arrow-orientation rule ("must map out of Selmer, not into it")',
          'Admissible control of the quotient may use a bounded source surjecting onto it, a bounded target receiving it '
          'injectively, bounded kernel and cokernel, an annihilator, an exact sequence, or an equivalent assertion. The defect of '
          'the killed automorphic routes was absence of coverage, not direction.',
          'WITHDRAWN', [], origin='correction', section='B', evidence=[E('BSD_FRONTIER_FREEZE_2026-09-22/FRONTIER.md', 'section 4')],
          label='w:arrow'),
    claim('W.3', 'SUPERSEDED: C13 = 7 or 8',
          'The returned values used lattice numerators and omitted alpha^-2; both correct to C13 = 2 mod 13 (omega1).',
          'WITHDRAWN', [], origin='normalization reconciliation', section='B',
          evidence=[E('BSD_SEED_P13_RUN_2026-09-21/SUPERSEDED_BY_NORMALIZATION.md', 'explanation'),
                    E(M + '_work/active_full_bsd/p13/NORMALIZATION.md', 'resolution')], label='w:c13'),
    claim('W.4', 'CORRECTED: exact theta order, "A_2 = 0 equivalently", and "rho_p = 4 suffices"',
          'The lower order calL_p in I^2 is unconditional, but exact order holds only given the c_2 unit. A_2 = 0 is sufficient, '
          'not equivalent, for v_p(R_der) >= 0. rho_p = 4 alone does not make c_2(p) a unit: the leading coefficient is '
          '#(Sha/Div Sha)(E/K)[p^infinity]*R_der.',
          'WITHDRAWN', [], origin='corrections', section='B',
          evidence=[E('BSD_TWIST_SHA_SUPPORT_2026-09-22/ORDINARY_LANE_FREEZE.md', 'final paragraph'),
                    E('BSD_C2_WITNESS_2026-09-22/REV2_RETURN_INDEPENDENT_CHECK.md', 'rho_p correction')], label='w:theta'),
    claim('W.5', 'CORRECTED: "cbar_2 = -c_{p-3}" and "5843 obstructs the twist Sha support"',
          'The correct relation is cbar_2 = c_{p-3}/2 (given M_1 = 0). 5843 is not an obstruction to the fixed-twist support '
          '(the 5843 exceptional-zero question for E^{-7} is disputed and off the critical path).',
          'WITHDRAWN', [], origin='errata', section='B',
          evidence=[E('BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_ERRATUM_2026-09-22.md', 'erratum'),
                    E('BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_2026-09-22.md', 'grading, item 3')], label='w:c2'),
    claim('W.6', 'SUPERSEDED: older 2243/5843 cost figures and the "compute only" framing',
          'The architect figures of about 2e4 / 1e5 CPU-hours are superseded by measured-rate estimates of about 1.2e5 / 6.3e5; the '
          'bad-prime routes also carry mathematical inputs (D1-D7) and evaluator requirement D8, now partly discharged.',
          'WITHDRAWN', [], origin='feasibility check', section='B',
          evidence=[E('BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/REPORT.md', 'measured rates')], label='w:cost'),
    claim('W.7', 'WITHDRAWN: "v2.3 isolates crashed and restarted runs"',
          'The evaluator reuses a stream-directory generation after a crash before the first checkpoint (reproduced). No false '
          'arithmetic result was shown; the isolation claim fails.',
          'WITHDRAWN', [], origin='cross-family review', section='B',
          evidence=[E('BSD_2243_ACC_CODEX_CHECK_2026-09-23/REVIEW.md', 'finding'), E('BSD_2243_EVALUATOR_REVIEW_2026-09-23/FIX_PROPOSAL_GENERATION_RESERVATION.md', 'proposed fix')],
          label='w:f4'),
    claim('W.8', 'Earlier register',
          'Older corrections (normalization and formalization bookkeeping, R2 closure claims, DM, thresholds, and others) are in '
          'the master\'s frozen DO_NOT_RESURRECT register and the supersession table of MASTER_BSD_DAG.md section 6.',
          'WITHDRAWN', [], origin='master record', section='B',
          evidence=[E(M + 'DO_NOT_RESURRECT.md', 'frozen register'), E(M + 'MASTER_BSD_DAG.md', 'section 6')], label='w:older'),
]
