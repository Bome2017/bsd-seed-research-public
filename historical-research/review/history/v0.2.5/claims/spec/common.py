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
