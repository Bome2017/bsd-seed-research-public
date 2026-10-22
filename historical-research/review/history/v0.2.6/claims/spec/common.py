"""Shared vocabulary for the claim specification (the single source for claims/CLAIM_INDEX.md and claims/claims.json).

Edit the spec files in this folder, then run `python3 tools/build_index.py`. The generated files must not be edited.
"""

M = 'BSD_CODEX6_MASTER_HANDOFF_2026-09-19/'          # canonical master record (read-only original)


def E(path, role=''):
    """An evidence item: a path relative to the research home (it is released under evidence/src/)."""
    return {'path': 'evidence/src/' + path, 'role': role}


# Evidence grades: what supports a statement. A claim may carry several.
GRADES = {
    'IMPORTED_PUBLISHED': 'A published theorem, applied. The source-check level is stated per import.',
    'IMPORTED_PREPRINT': 'A theorem from a preprint (not refereed), applied.',
    'PROVED_WRITTEN': 'A written proof or deduction in the project records (possibly combining imported theorems).',
    'PROVED_COMPUTER_ASSISTED': 'A certificate with rigorous error control (Arb balls, directed rounding, or exact arithmetic), with a stated trust base.',
    'EXACT_COMPUTATION': 'A finite exact computation (integers or rationals), replayable in seconds or minutes.',
    'LEAN_CHECKED': 'Machine-checked in Lean 4 from explicit hypotheses; the hypotheses are listed and are not themselves formalized unless stated.',
    'NUMERICAL_EVIDENCE': 'Floating-point or heuristic evidence; never used as a proof input.',
}

# Logical kinds: what sort of statement it is.
KINDS = {
    'FACT': 'Exact data about the curve.',
    'THEOREM': 'Unconditional, relative to the listed imports and trust base.',
    'CONDITIONAL': 'An implication whose antecedent is not established; the antecedent is a sufficient witness, never an obligation.',
    'EQUIVALENCE': 'A reformulation proved equivalent to an open statement; it earns no difficulty reduction by itself.',
    'OBSTRUCTION': 'A stopped route; see stop_kind and scope.',
    'OPEN': 'An open obligation of full BSD for this curve.',
    'HISTORICAL': 'A completed result about other curves or families, retained for context; it does not transfer to this curve.',
    'WITHDRAWN': 'An assertion that was made in the records and is withdrawn or superseded; listed to prevent resurrection.',
}

# Kinds of stop; they must not be conflated.
STOP_KINDS = {
    'PROVED_OBSTRUCTION': 'A theorem shows the route cannot succeed within an explicitly delimited class; nothing is claimed outside that class.',
    'EQUIVALENT_REFORMULATION': 'The route target is proved equivalent to the open problem; absent an independent proof method this gives no demonstrated difficulty reduction. It is not an impossibility.',
    'DEFECTIVE_SOURCE': 'The imported mechanism is false (counterexample recorded).',
    'UNAFFORDABLE': 'A known implementation exists, but its measured or modeled cost exceeds what has been authorized; not a mathematical stop.',
    'UNSUCCESSFUL_ATTEMPT': 'An attempt that found nothing; no impossibility is claimed.',
    'PROCEDURAL': 'Stopped by a stopping rule or decision (archived), not refuted.',
}

# Review levels: who has checked it.
REVIEWS = {
    'NONE': 'No review beyond the author.',
    'MODEL_SAME_FAMILY': 'A fresh-context review by a model of the same family as the author.',
    'MODEL_CROSS_FAMILY': 'A review by a model of a different family.',
    'HUMAN': 'Independent human review (none recorded for any claim).',
}


def claim(id, title, statement, kind, grades, *, origin, section, evidence, imports=(), depends_on=(),
          normalization='', verification=None, qualifications=(), master_ref='', post_master='', stop_kind='',
          scope='', role='', label=''):
    assert kind in KINDS, kind
    for g in grades:
        assert g in GRADES, g
    if kind == 'OBSTRUCTION':
        assert stop_kind in STOP_KINDS, (id, stop_kind)
    return dict(id=id, title=title, statement=statement, kind=kind, grades=list(grades), origin=origin,
                section=section, evidence=list(evidence), imports=list(imports), depends_on=list(depends_on),
                normalization=normalization, verification=verification or {}, qualifications=list(qualifications),
                master_ref=master_ref, post_master=post_master, stop_kind=stop_kind, scope=scope, role=role, label=label)


class V25:
    """Governing records of the v0.2.5 bank (paths relative to the research home; each is released under evidence/src/)."""
    RC = 'BSD_RECORD_RECONCILIATION_CODEX_2026-09-29/'
    DRAFT, LEDGER, P13R, RCREP = RC + 'V025_CLAIM_UPDATE_DRAFT.md', RC + 'SOURCE_LEDGER.json', RC + 'P13_BINDING_RECONCILIATION.json', RC + 'REPORT.md'
    TA = 'BSD_LINE_TA_COMPATIBILITY_REVIEW_2026-09-24/INPUT_TA_TB_RESOLUTION.md'
    K288 = 'BSD_K288_UNIFORMITY_AUDIT_CODEX_2026-09-27/AUDIT.md'
    SP = 'BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/'
    SPEC, CHECKER = SP + 'SINGLETON_SPEC_v1_audited.md', SP + 'checker/singleton_check.py'
    PRO_OTA = 'BSD_BUILD_MAP/pro6/SINGLETON_AUDIT_REPORT_PRO.md'
    AUD1729 = 'BSD_CERT_17_29_AUDIT_RETURN_FABLE_2026-09-29/'
    BATCHC = 'BSD_BATCH_C_AUDIT_CODEX_2026-09-27/REVIEW.md'
    PROF = 'BSD_PRO_FOLLOWUP_LEAN_BATCH_C_AUDIT_CODEX_2026-09-27/AUDIT.md'
    G2P = 'BSD_BUILD_MAP/pro6/G1G2_REVIEW_2026-09-26/BSD_GLOBAL_G1G2_REVIEW_2026-09-26/G2_PROOF.md'
    G2A = 'BSD_G2_INDEPENDENT_AUDIT_CODEX_2026-09-26/REPORT.md'
    KATO = 'BSD_BUILD_MAP/reviews/pro_kato_followup_2026-09-27/BSD_KATO_FOLLOWUP_REVIEW_2026-09-27/REVIEW.md'
    BHC = 'BSD_BAD_PRIME_SINGLETON_RETURN_CHECK_CODEX_2026-09-27/'
    BHI = BHC + 'input/BSD_BAD_PRIME_SINGLETON_AUDIT_2026-09-27/'
    COST = 'BSD_BAD_PRIME_COST_SCREEN_AUDIT_CODEX_2026-09-27/REVIEW.md'
    L1 = 'BSD_P3_SEAMS_RETURN_FABLE_2026-09-29/'
    B1 = 'BSD_P3_UPPER_HALF_RETURN_FABLE_2026-09-29/'
    R24 = 'BSD_P3_UPPER_INTEGRAL_SCREEN_RETURN_FABLE_2026-09-29/'
    B2 = 'BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29/'
    R23 = 'BSD_P3_UPPER_REPAIR_SCREEN_RETURN_OPUS_2026-09-29/'
    CCR = 'BSD_SEED_V025_BANK_TASK_2026-09-29/inputs/CLAUDE_CHECK_REPORT.md'
    FRC = 'BSD_SEED_V025_BANK_TASK_2026-09-29/inputs/FABLE_RETURN_CHECKS.md'
    CED = 'BSD_BUILD_MAP/V025_CANDIDATE_EDITS_2026-09-29.md'
    TW = 'BSD_BUILD_MAP/V025_CANDIDATE_THEOREM_W_2026-09-29.md'
    UA = 'BSD_UNIFORMITY_ATTEMPTS_CHECK_CODEX_2026-09-29/'
    WF = 'BSD_W_ELL_INDEPENDENCE_RETURN_FABLE_2026-09-29/'
    TC = 'BSD_TAME_CONSTANT_NORM_RETURN_OPUS_2026-09-29/'
    SF = 'BSD_SHA_FACTOR_CALIBRATION_RETURN_FABLE_2026-09-29/'
    # (p, auxiliary l, run folder, frozen package, result record) for the singleton certificates at 17 <= p <= 47
    RUNS = [(17, 103, 'l103', 'FROZEN_RUN_PACKAGE_l103', 'RESULT_P17.md'),
            (19, 191, 'p19_l191_v2', 'FROZEN_RUN_PACKAGE_p19_l191_v2', 'RESULT_P19.md'),
            (23, 47, 'p23_l47', 'FROZEN_RUN_PACKAGE_p23_l47', 'RESULT_P23.md'),
            (29, 233, 'p29_l233_v2', 'FROZEN_RUN_PACKAGE_p29_l233_v2', 'RESULT_P29_L233.md'),
            (31, 311, 'p31_l311', 'FROZEN_RUN_PACKAGE_p31_l311', 'RESULT_P31.md'),
            (37, 149, 'p37_l149', 'FROZEN_RUN_PACKAGE_p37_l149', 'RESULT_P37.md'),
            (41, 83, 'p41_l83', 'FROZEN_RUN_PACKAGE_p41_l83', 'RESULT_P41.md'),
            (43, 173, 'p43_l173', 'FROZEN_RUN_PACKAGE_p43_l173', 'RESULT_P43.md'),
            (47, 283, 'p47_l283', 'FROZEN_RUN_PACKAGE_p47_l283', 'RESULT_P47.md')]
    DOWNSTREAM = {19, 23, 29}          # runs whose folder also holds DOWNSTREAM_RECOMPUTE_MAIN.json


class VK:
    """Governing records of the route-K follow-on (paths relative to the research home; released under evidence/src/)."""
    LABEL = ('written derivation; three Anthropic model readers (one cross-model: Fable 5.1; two independent fresh sessions: '
             'Opus 5.5) and one cross-family source reading (Codex, OpenAI) of D5/D6/D8 with the errata E1–E7, passing at the '
             'retained arithmetic-input and imported-theorem grades; not a full certificate replay; no human review')
    CODEX = 'BSD_ASTRA_CATCHUP_RETURN_2026-09-30/'
    CODEX_FILES = ['RETURN.md', 'MANIFEST.sha256', 'ITEM1_ROUTE_K.md', 'ITEM1_PRECOMPARISON.md', 'K_ASTRA_1.md', 'ITEM3_RELEASE_WORDING.md',
                   'RECORD_REPAIRS.md', 'INTEGRITY_AND_SCOPE.md', 'ITEM2_UNIFORM_STEP.md', 'ITEM4_CATCHUP_AND_CONTRADICTIONS.md', 'RESUME.md',
                   'SOURCE_BINDINGS.tsv', 'checks/normalization.gp', 'checks/normalization.log']
    R25 = 'BSD_P3_MS_R24_COLEMAN_RETURN_OPUS_2026-09-29/'
    ERRATA = 'BSD_SEED_V025_BANK_ROUTEK_TASK_2026-09-29/inputs/R25_ERRATA_2026-09-29.md'
    FCK = 'BSD_P3_MS_R24_COLEMAN_CHECK_FABLE_2026-09-29/'
    SRA = 'BSD_R25_SECOND_READER_RETURN_OPUS_2026-09-29/'
    SRB = 'BSD_R25_SECOND_READER_RETURN_OPUS_B_2026-09-29/'
    BANKCHECK = 'BSD_SEED_V025_BANK_CHECK_FABLE_2026-09-29/CHECK.md'
    D = ['D1_CONSTRUCTION.md', 'D2_INTEGRALITY.md', 'D3_KILL_TESTS_A_B.md', 'D4_KILL_TEST_C.md', 'D5_MS_R24.md',
         'D6_O2_POITOU_TATE.md', 'D7_O4_NORMALISATION.md', 'D8_ASSEMBLY.md']
    TA = ['T1_D5_STEP2_3_INTERPOLATION.md', 'T2_D5_STEP1_COLEMAN_ISO.md', 'T3_D6_O2.md', 'T4_D8_ASSEMBLY_JONES.md', 'T5_D1_D2_BY_HAND.md']
    TB = ['T1_D5_STEPS2-3_INTERPOLATION.md', 'T2_D5_STEP1_COL_ISO.md', 'T3_D6_O2.md', 'T4_D8_ASSEMBLY_JONES.md', 'T5_D1_D2_BY_HAND.md']


class V26:
    """Governing records of the v0.2.6 bank: the Kurihara position (paths relative to the research home; released under
    evidence/src/). LABEL, TARGET and SENTENCE are verbatim from the governing scope inputs/V026_SCOPE.md."""
    LABEL = 'Derived by Codex (OpenAI). Independent review by ChatGPT Pro (OpenAI): ACCEPT_AT_IMPORT_GRADE. The source statements were checked by Claude Opus 5.5 and Claude Fable 5.1 (Anthropic); the Δ-component bridge by Claude Fable 5.1; the Part B deductions by Claude Opus 5.5. The author-hosted CLW revision is byte-identical across three independent downloads (sha256 0686fa41…d036fb98); arXiv v1 is a different file. Not a human review; not formalized.'
    PROVENANCE = ('derived by Codex (OpenAI) and independently reviewed by ChatGPT Pro (OpenAI), with source and deduction checks by '
                  'Claude models (Anthropic); not a human review; not formalized')
    REVIEW = ('MODEL_CROSS_FAMILY at the statement and deduction level: derived by Codex (OpenAI); independent review by ChatGPT Pro '
              '(OpenAI); source statements, the Delta-component bridge and the Part B deductions checked by Claude models (Anthropic); '
              'not a human review; not formalized')
    TARGET = 'Find one finite set S containing {2,3,2243,4547,5843} and an independent argument that, for every p outside S, either a two-prime mod-p unit Kurihara witness exists or dim_{F_p} Sel_p(E/Q) ≤ 3. Under B.21 these two conditions are equivalent to each other and to Sha[p^∞]=0. A faithful value of the full BH-normalized element of a real cyclic degree-p field at its actual conductor prime to pN, with depth strictly below four, is another sufficient condition. No converse from Sha vanishing to existence of that character value is claimed. Fields, conductors and estimates may depend on p.'
    SENTENCE = 'This is an identity, not an upper bound. The abstract dual module X = Z_p² ⊕ (Z/p)² needs four generators, with Fitt₂(X)=(p²), Fitt₃(X)=(p), and Fitt₄(X)=Z_p. It is compatible with M_∞=0 and first unit index four. This is a module countermodel to an inference from primitivity alone, not a claim about the seed at an uncomputed prime.'
    CLW_SHA = '0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98'
    MODEL_Q = ('The deep theorems are imported from preprints and not reproved; the retained seed inputs were not replayed by the '
               'reviews. The review label records model reviews at their stated scopes; repeated byte-identical downloads verify source '
               'identity, not independent proofs.')
    SYN = 'BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/'
    RC = 'BSD_UNIFORM_SYNTHESIS_REVIEW_CHECK_CODEX_2026-09-30/'
    PRO = RC + 'input/BSD_UNIFORM_SYNTHESIS_INDEPENDENT_REVIEW_2026-09-30/'
    SHEET = 'BSD_BUILD_MAP/UNIFORM_STEP_REDUCTION_SHEET_2026-09-29.md'
    CCR = 'BSD_RUN_NOW_RETURNS_CHECK_CLAUDE_2026-09-29/REPORT.md'
    TI = 'BSD_SEED_V026_BANK_TASK_2026-09-30/inputs/'
    LOCAL = 'BSD_SEED_V026_BANK_RETURN_OPUS_2026-09-30/checks/'


def v26_coverage_evidence():
    """B.20: the synthesis and its application, the independent review (Part A and its source audit), the return check with its
    fresh download, the source-statement and Delta-bridge check, the Claude checks, the scope and its checks, and the local
    re-derivation of a_19, a_59, a_487. Third-party page renders, paper copies and text extractions are bound by hash in the
    release record, not copied."""
    s, r, p = V26.SYN, V26.RC, V26.PRO
    out = [E(s + f, 'uniform synthesis (Codex): ' + role) for f, role in (
        ('REPORT.md', 'verdicts and scope'), ('NEW_INPUT_APPLICATION.md', 'the application of CLW and Castella-Sano to the seed'),
        ('SOURCE_REGISTER.md', 'sources and anchors'), ('SOURCE_BINDINGS.json', 'source URLs and hashes (the pinned CLW revision)'),
        ('LOCAL_BINDINGS.json', 'hashes of the local records read'), ('SEED_LOCAL_CHECK.json', 'v_2243(Delta) = 1 and c4 mod 2243'),
        ('check_arithmetic.py', 'the local arithmetic check'), ('CHECKS.json', 'check summary'), ('NEXT_TASK.md', 'the review request'),
        ('STATE.json', 'state'), ('RESUME.md', 'resume notes'), ('MANIFEST.sha256', 'synthesis manifest'))]
    out += [E(p + f, 'independent review (ChatGPT Pro): ' + role) for f, role in (
        ('RETURN.md', 'ACCEPT_AT_IMPORT_GRADE'), ('PART_A_COVERAGE.md', 'Part A: the coverage audit A1-A5'),
        ('SOURCE_AUDIT.md', 'source and custody audit'), ('SOURCE_BINDINGS.json', 'source hashes'), ('INPUT_INTEGRITY.json', 'input integrity'),
        ('INPUT_NEXT_TASK.md', 'the review request as received'), ('CHECKS.json', 'check summary'), ('NOTES.md', 'notes'),
        ('STATE.json', 'state'), ('RESUME.md', 'resume notes'), ('MANIFEST.sha256', 'review manifest'),
        ('source_checks/anchors.json', 'text anchors of the source statements'))]
    out += [E(r + f, 'return check of the review (Codex): ' + role) for f, role in (
        ('REPORT.md', 'ACCEPT_REVIEW_AT_STATED_GRADE; live source hash match'), ('FRESH_SOURCE.json', 'fresh download of the CLW revision: headers and sha256'),
        ('STATE.json', 'state'), ('MANIFEST.sha256', 'return-check manifest'))]
    out += [E(V26.SHEET, 'section 9: the source-statement and Delta-component bridge check (Fable); section 9a: the pinned-source comparison'),
            E(V26.CCR, 'Claude check report: addendum 25 (source statements) and addendum 28 (source fetch, Part B deductions)'),
            E(V26.TI + 'CLAUDE_ADDENDUM_25.md', 'addendum 25, as supplied with the task'), E(V26.TI + 'CLAUDE_ADDENDUM_28.md', 'addendum 28, as supplied with the task'),
            E(V26.TI + 'V026_SCOPE.md', 'the governing scope (claims, labels, IN and OUT)'),
            E(V26.TI + 'CODEX_THREE_BRIEFS_REVIEW_REPORT.md', 'check of the scope: CONFIRMED_WITH_CORRECTIONS'),
            E(V26.LOCAL + 'seed_local_facts.gp', 'PARI re-derivation of a_19, a_59, a_487 and the local data'),
            E(V26.LOCAL + 'seed_local_facts.log', 'its output: a_19 = 4, a_59 = -4, a_487 = -28')]
    return out


def v26_depth_evidence():
    """B.21 and B.22: the depth target, the independent review's Part B, and the Part B check."""
    return [E(V26.SYN + 'DEPTH_TARGET.md', 'uniform synthesis (Codex): the minimal unit length and the character-depth test'),
            E(V26.PRO + 'PART_B_DEPTH.md', 'independent review (ChatGPT Pro): Part B, sections B1-B7'),
            E(V26.PRO + 'RETURN.md', 'independent review (ChatGPT Pro): ACCEPT_AT_IMPORT_GRADE'),
            E(V26.CCR, 'Claude check report: addendum 28 (Part B deductions checked)'),
            E(V26.TI + 'CLAUDE_ADDENDUM_28.md', 'addendum 28, as supplied with the task'),
            E(V26.TI + 'V026_SCOPE.md', 'the governing scope'),
            E(V26.TI + 'CODEX_THREE_BRIEFS_REVIEW_REPORT.md', 'check of the scope: CONFIRMED_WITH_CORRECTIONS')]


def codex_evidence():
    """The cross-family source reading of route K (Codex, OpenAI): its own files. Its source_checks/ (third-party page images
    and a text extraction) are bound by hash in the release record, not copied."""
    return [E(VK.CODEX + f, 'cross-family source reading of route K: ' + f) for f in VK.CODEX_FILES]


def routek_evidence():
    """Evidence for route K: the derivation D1-D8 and its checks, the errata, the cross-model check and both second readers."""
    r, f, a, b = VK.R25, VK.FCK, VK.SRA, VK.SRB
    out = [E(r + 'RETURN.md', 'route K: status, inputs and grades'), E(r + 'MANIFEST.sha256', 'derivation manifest')]
    out += [E(r + d, 'route K derivation, ' + d.split('_')[0]) for d in VK.D]
    out += [E(r + 'checks/' + c, 'route K check') for c in ('coleman_family.gp', 'coleman_family.log', 'kr25c.sage', 'kr25c.log',
                                                           'cands.txt', 'seed_sign_check.log')]
    out += [E(VK.ERRATA, 'errata E1-E7 from the three readings'),
            E(f + 'CHECK.md', 'cross-model reading (Fable 5.1), including section 7'), E(f + 'MANIFEST.sha256', 'check manifest'),
            E(f + 'checks/coleman_family_replay.log', 'identical replay of the Coleman-family check'),
            E(f + 'checks/rank1_check.sage', 'rank-1 calibration of the regulator convention'), E(f + 'checks/rank1_check.log', 'its output, 23/23'),
            E(a + 'RETURN.md', 'second reader A: PASS_WITH_CORRECTIONS'), E(a + 'MANIFEST.sha256', 'reader A manifest')]
    out += [E(a + t, 'reader A, ' + t.split('_')[0]) for t in VK.TA]
    out += [E(a + 'checks/reg.gp', 'reader A: 3-adic regulator recomputation'), E(a + 'checks/reg.log', 'its output: v_3(Reg_PARI) = 2'),
            E(b + 'RETURN.md', 'second reader B: PASS_WITH_CORRECTIONS'), E(b + 'MANIFEST.sha256', 'reader B manifest')]
    out += [E(b + t, 'reader B, ' + t.split('_')[0]) for t in VK.TB]
    out += [E(V25.R24 + 'SRC_Elkies_rho3.md', 'rho_3 surjective onto GL_2(Z_3): Elkies criterion'),
            E(V25.R24 + 'checks_elkies_rho3.gp', 'its computation'), E(V25.R24 + 'SRC_Kobayashi2006.md', 'Kobayashi 2006 at source')]
    return out


def singleton_run_evidence():
    """Evidence items for every singleton run: result, frozen-checker report, run manifest, symbol output, freeze records."""
    out = []
    for p, l, run, pkg, result in V25.RUNS:
        r, f = V25.SP + 'seed_runs/' + run + '/', V25.SP + pkg + '/'
        out += [E(r + result, f'p = {p}, l = {l}: result record'), E(r + 'SINGLETON_REPORT.json', f'p = {p}: frozen acceptance checker output (NONZERO)'),
                E(r + 'RUN_MANIFEST.json', f'p = {p}: run manifest'), E(r + 'msl.txt', f'p = {p}: certified symbol intervals at l = {l}')]
        if p in V25.DOWNSTREAM:
            out.append(E(r + 'DOWNSTREAM_RECOMPUTE_MAIN.json', f'p = {p}: downstream recomputation'))
        out += [E(f + 'FREEZE_MANIFEST.json', f'p = {p}: frozen run package manifest'), E(f + 'PREREGISTRATION.md', f'p = {p}: preregistration')]
    return out
