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
