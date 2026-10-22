#!/usr/bin/env python3
"""V026-D transition check (the depth-length-Selmer comparison, B.23-B.24): reconstruct the v0.2.6 bank tree exactly, run
ITS checker unchanged, then check the V026-D delta.

  python3 tools/verify_v026d_transition.py                         the check (prints V026D_TRANSITION_PASS)
  python3 tools/verify_v026d_transition.py --with-prev-controls    also run the v0.2.6 negative controls in the reconstruction
  python3 tools/verify_v026d_transition.py --negative-controls     corrupt throwaway copies; every corruption must FAIL

1. Copy this tree, restore every path in the record's `base_copies` (the 8182b9c bytes kept under review/history/v0.2.6/),
   remove every path in `added_paths`; the reconstructed file set must EQUAL the preserved 8182b9c manifest.
2. Run the reconstructed tree's tools/verify_patch_release.py (the v0.2.6 checker, byte-identical). It reconstructs the K2
   tree in turn, and so on back. It must pass.
3. Check the V026-D delta by exact rows, exact lists and set equality with uniqueness. The changed and added files must be
   exactly the sets fixed HERE, and so are the semantic bounds: B.23 (the capped identity, the strict "< 4", the three
   scope sentences), B.24 (the antecedent, kind CONDITIONAL, the factor-2 normalization), B.22 unchanged except for its one
   qualification (cross-reference; "not evaluated at any p >= 53"), O.1's frontier text, the verbatim review label, the
   release-grade vocabulary, the governing files (own files copied; page renders by hash only; the Claude-report row kept as
   a retained source change), and outward scans (no witness, new vanishing prime, uniform bound or FIN claimed; no field
   claimed to attain depth two; the converse not attributed to B.22; no "no such value computed"; the v0.2.6 scans kept).
Standard library only; this repository is never written.
"""
import hashlib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
REC_PATH = 'review/V026D_APPLIED.json'
PRIOR_RECORDS = ('review/V025_BANK_APPLIED.json', 'review/V025K_ROUTEK_APPLIED.json', 'review/V025K2_APPLIED.json', 'review/V026_APPLIED.json')
LABEL = ('Derived by ChatGPT Pro (OpenAI). Independent check by Codex (OpenAI): ACCEPT_AT_RETAINED_AND_IMPORTED_THEOREM_GRADE. '
         'Cross-family check of D1\u2013D5 by Claude Opus 5.5 (Anthropic). No literature-novelty claim. Not a human review; not formalized.')
REVIEW = ('MODEL_CROSS_FAMILY at the deduction level: derived by ChatGPT Pro (OpenAI); independent check by Codex (OpenAI); '
          'cross-family check of D1-D5 by Claude Opus 5.5 (Anthropic); no literature-novelty claim; not a human review; not formalized')
PROV = ('derived by ChatGPT Pro (OpenAI) and independently checked by Codex (OpenAI), with a cross-family check by '
        'Claude (Anthropic); not a human review; not formalized')
SENTENCES = ['This is an equivalence between existence statements. It does not say that a preselected field, or every field, attains depth two.',
             'It supplies no witness, no new vanishing prime and no upper bound.',
             'The strict inequality < 4 and the cap p \u2212 1 are part of the statement.']
SENTENCES_TEX = ['This is an equivalence between existence statements. It does not say that a preselected field, or every field, attains depth two.',
                 'It supplies no witness, no new vanishing prime and no upper bound.',
                 'The strict inequality $<4$ and the cap $p-1$ are part of the statement.']
TARGET = ('Current known frontier for the uniform part of FIN on good primes: one finite set S \u2287 {2, 3, 2243, 4547, 5843} with '
          'dim_{F_p} Sel_p(E/Q) \u2264 3 for every p \u2209 S, or any independently proved equivalent criterion. By B.21\u2013B.23 this is '
          'equivalent, prime by prime, to a two-prime mod-p unit Kurihara witness. It is also equivalent to a faithful character value, '
          'of depth strictly below four, of the full BH element of a real cyclic degree-p field at its actual conductor prime to pN. '
          'Fields, conductors and estimates may depend on p.')
CROSSREF = 'The converse holds by B.23 (derived 2026-09-30).'
NOT_EVAL = 'It has not been evaluated at any p \u2265 53.'
README_B22 = 'not evaluated at p \u2265 53; converse: B.23'
B22_OLD_Q = ('Sufficient only: no converse from Sha(E/Q)[p^infinity] = 0 to the existence of such a character value is claimed, '
             'and no such value has been computed at any prime.')
B22_NEW_Q = ('Sufficient only: no converse from Sha(E/Q)[p^infinity] = 0 to the existence of such a character value is claimed '
             'here. ' + CROSSREF + ' ' + NOT_EVAL)
O1_OLD_PREFIX = 'Current known frontier for the uniform step (B.20-B.22): '
O1_NEW_Q = (TARGET + ' No applicable theorem was located in the screened sources. Together with finiteness of the primary components '
            'at the primes of S, this would give FIN.')
GRADES = ['PROVED_WRITTEN', 'IMPORTED_PREPRINT']
NEW_IDS = ['B.23', 'B.24']
REVISED = {'B.22': {'qualifications'}, 'O.1': {'qualifications', 'evidence'}}
_S = 'evidence/src/'
CX = 'BSD_UNIFORM_DEPTH_V2_REVIEW_CODEX_2026-09-30/'
RET = CX + 'input/BSD_UNIFORM_DEPTH_V2_RETURN_2026-09-30/'
TI = 'BSD_SEED_V026D_COMPARISON_TASK_2026-09-30/inputs/'
SINGLES = [_S + TI + n for n in ('CLAUDE_ADDENDUM_32.md', 'CLAUDE_ADDENDUM_33.md', 'SCOPE_V026D.md')]
BRIDGE_REQUIRED = [_S + RET + 'ATTEMPT_II_TWO_PRIME_WITNESS.md', _S + CX + 'REPORT.md', _S + TI + 'CLAUDE_ADDENDUM_32.md']
REPORT_ROW = ('evidence/src/BSD_RUN_NOW_RETURNS_CHECK_CLAUDE_2026-09-29/REPORT.md', 'ca86c869c1db2f4a6356bc5dcee3dc78c6a7020724dbfd1fc5a03718958f2586')
BH_BOUND = ('BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/', 'sources/BH_2511.07203v1.pdf', 'd3355b216eff780f070df45778d161d8636b4acc43f73b8c7186b1c037f52481')
TEXT_EDIT_FILES = {'paper/sections/09_reductions.tex', 'paper/sections/11_remaining.tex', 'paper/release_id.tex', 'README.md',
                   'RECHECK_V0_2_6.md', 'tools/verify_patch_release.py'}
DERIVED_CHANGED = {'claims/spec/common.py', 'claims/spec/part2_bridges.py', 'claims/spec/part4_open.py', 'claims/claims.json',
                   'claims/CLAIM_INDEX.md', 'review/SYNTHESIS_CHECK_BRIEF.md', 'evidence/PROVENANCE.tsv', 'tools/extra_evidence.txt',
                   'paper/seed_bsd.pdf', 'paper/seed_bsd.bbl', 'MANIFEST.sha256', 'SOURCE_SNAPSHOT.json'}
NEW_FILES = {REC_PATH, 'tools/verify_v026d_transition.py', 'review/V026D_EVIDENCE_ADDITIONS.json', 'review/V026D_EVIDENCE_TRANSITION.json',
             'review/V026D_RETAINED_SOURCE_CHANGES.json'}
ALLOW_FILES = set(PRIOR_RECORDS) | {REC_PATH, 'tools/verify_v025k_transition.py', 'tools/verify_v025k2_transition.py',
                                    'tools/verify_v026_transition.py', 'tools/verify_v026d_transition.py'}
ALLOW_PREFIXES = ('review/history/', 'evidence/src/')
E1 = re.compile(r'12\.5 ?\(4\)')
OLD81 = re.compile(r'give only[^.;]{0,40}81')
OLD_K_LABEL_TAIL = 'all Anthropic models, not cross-family'
LABEL_SCOPE = ('claims/', 'paper/', 'README.md', 'review/SYNTHESIS_CHECK_BRIEF.md')
REMAINS = re.compile(r'\b(only remains|all that remains|only what remains)\b', re.I)
NOMETHOD = re.compile(r'\bno (known )?(method|mechanism)s? (exists?|is known|is available|can)\b|\bthere (is|are) no (known )?(method|mechanism)s?\b'
                      r'|\bno one has an? (method|mechanism)\b|\bno method whatsoever\b', re.I)
NEG = re.compile(r"\b(not|no|nor|neither|never|would|could|if|unless|open|conditional|none|without|needs?|suffices?|sufficient|"
                 r"target|equivalent(ly)?|whether|question|until|remains?|only if|given|suppose|supposes|assume[sd]?|antecedent|conjectur\w*)\b", re.I)
FIN_SUBJ = re.compile(r'\bFIN\b|finiteness of (the )?(\$\\Sha\$|Sha)(?!\s*\$?\[)|\bSha(\(E/Q\))? is finite\b|finite (prime )?support'
                      r'|\buniform (upper |torsion )?bound\b', re.I)
FIN_VERB = re.compile(r'\b(is|are|was|were|has|have|had)\s+(now\s+)?(been\s+)?(proved|proven|established|shown|settled)\b'
                      r'|\bnow (proved|proven|established|shown|settled)\b'
                      r'|\b(proves?|establish(es)?|settles?)\s+(that\s+)?(FIN\b|finite|the uniform|a uniform|finiteness)', re.I)
WITNESS = re.compile(r'(two-prime|length-two|quadratic|depth-two)[^.;]{0,50}witness(es)?[^.;]{0,40}\b(exists?|has been (found|constructed|computed|established)'
                     r'|have been (found|constructed|computed)|is (known|found|established)|was (found|computed))\b', re.I)
VANISH = re.compile(r'(infinitely many|all but finitely many|almost all|a new)[^.;]{0,50}(\\?Sha|vanish)[^.;]{0,40}|(\\?Sha)[^.;]{0,60}(= ?0|vanish\w*)[^.;]{0,40}'
                    r'(for|at) (infinitely many|all but finitely many|almost all|every p (>=|\\ge|\u2265) ?53)|new vanishing prime[^.;]{0,30}(is|was|has been) (found|proved)', re.I)
NOVALUE = re.compile(r'no (such )?values? (has |have )?(yet )?(been )?computed|no value computed', re.I)
B22CONV = re.compile(r'B\.22[^.;]{0,40}\b(itself )?(proves|establishes|gives|supplies|contains) (the |its )?converse|converse (of|to) B\.22 (is|was) (proved|given) (by|in) B\.22', re.I)
EVERYFIELD = re.compile(r'(every|each|any|a preselected|the preselected|a given|a fixed|the chosen)( such| real cyclic)?( degree-p)?( field| K)[^.;]{0,60}attains? (depth|a depth) (two|2)', re.I)
OLD_V26_TARGET_BIT = 'No converse from Sha vanishing to existence of that character value is claimed.'
PROCESS_MARKERS = ['Fable', 'Opus', ' lane', 'Lane ', 'RUN_NOW', 'coordinator', 'addendum', 'Addendum', 'DRAFT', 'draft banner', 'session',
                   'only remains', 'all that remains', 'only what remains', 'ACCEPT_AT', 'CONFIRMED_WITH', 'PASS_AT', 'BANKED', 'BLOCKED',
                   'SOURCE_UPDATE', 'Pro-6', 'REDUCED', 'V026']
PAPER_HEADERS = {'B.23': '\\cid{B.23}; written deduction from a preprint theorem; ' + PROV + ']\\label{thm:cmp}',
                 'B.24': '\\cid{B.24}; written deduction from a preprint theorem; conditional; ' + PROV + ']\\label{thm:bridge}'}
PAPER_FRONTIER = ['Current known frontier for the uniform part of FIN on good primes: one finite set $S\\supseteq\\{2,3,2243,4547,5843\\}$ with $\\dim_{\\F_p}\\Sel_p(E/\\Q)\\le3$ for every $p\\notin S$, or any independently proved equivalent criterion.',
                  'this is equivalent, prime by prime, to a two-prime mod-$p$ unit Kurihara witness.',
                  'It is also equivalent to a faithful character value, of depth strictly below four, of the full Bullach--Honnor element of a real cyclic degree-$p$ field at its actual conductor prime to $pN$.',
                  'Fields, conductors and estimates may depend on $p$.', 'No applicable theorem was located in the screened sources.']


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit('FAIL: ' + message)
    print('PASS: ' + message)


def manifest_rows(path):
    pairs = [line.split('  ', 1) for line in Path(path).read_text().splitlines()]
    rows = {rel: h for h, rel in pairs}
    require(len(rows) == len(pairs), f'every path of {Path(path).relative_to(R)} is listed once')
    return rows


def ignored(rel):
    name = rel.rsplit('/', 1)[-1]
    return (rel == 'MANIFEST.sha256' or '__pycache__' in rel.split('/') or name.endswith('.pyc') or name == '.DS_Store'
            or (rel.startswith('paper/') and rel.count('/') == 1
                and name.endswith(('.aux', '.log', '.fls', '.fdb_latexmk', '.out', '.toc', '.blg', '.synctex.gz'))))


def k2_scope(rel):
    return not (rel in ALLOW_FILES or rel.startswith(ALLOW_PREFIXES))


def outward_text(rel):
    return (rel in ('README.md', 'SHARING.md', 'claims/CONTRADICTIONS.md', 'claims/CROSS_CONNECTIONS.md', 'coverage/COVERAGE.md')
            or (rel.startswith('paper/') and rel.endswith(('.tex', '.bib'))))


def scan(paths, claims):
    keys = ('e1', 'old81', 'oldlabel', 'remains', 'nomethod', 'finproved', 'witness', 'vanish', 'novalue', 'b22conv', 'everyfield', 'oldtarget')
    out = {k: [] for k in keys}
    public = []
    for rel in sorted(paths):
        if not k2_scope(rel):
            continue
        try:
            text = (R / rel).read_text()
        except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if E1.search(line) and 'final length inequality of 12.5(4)' not in line:
                out['e1'].append(f'{rel}:{n}')
            if OLD81.search(line):
                out['old81'].append(f'{rel}:{n}')
            if rel.startswith(LABEL_SCOPE) and OLD_K_LABEL_TAIL in line:
                out['oldlabel'].append(f'{rel}:{n}')
        if outward_text(rel):
            public.append((rel, text))
    for c in claims:
        if c['kind'] not in ('WITHDRAWN', 'HISTORICAL'):
            public.append((f"claims:{c['id']}", '\n'.join([c['title'], c['statement'], c['normalization']] + c['qualifications'] + c['imports'])))
    for rel, text in public:
        for s in SENTENCES + SENTENCES_TEX:
            text = text.replace(s, '')
        for n, line in enumerate(text.splitlines(), 1):
            where = f'{rel}:{n}'
            for key, rx in (('remains', REMAINS), ('nomethod', NOMETHOD), ('novalue', NOVALUE), ('b22conv', B22CONV), ('everyfield', EVERYFIELD)):
                if rx.search(line):
                    out[key].append(where)
            if OLD_V26_TARGET_BIT in line or 'No converse from $\\Sha$ vanishing to existence of that character value is claimed' in line:
                out['oldtarget'].append(where)
            for sent in re.split(r'(?<=[.;])\s+', line):
                if NEG.search(sent):
                    continue
                if FIN_SUBJ.search(sent) and FIN_VERB.search(sent):
                    out['finproved'].append(where)
                if WITNESS.search(sent):
                    out['witness'].append(where)
                if VANISH.search(sent):
                    out['vanish'].append(where)
    return out


def check_claims(ccl, bcl, REC):
    for i in NEW_IDS:
        c = ccl[i]
        require(c['grades'] == GRADES and c['kind'] == ('THEOREM' if i == 'B.23' else 'CONDITIONAL'),
                f'v0.2.6D: {i} has kind {"THEOREM" if i == "B.23" else "CONDITIONAL"} and grades PROVED_WRITTEN, IMPORTED_PREPRINT only')
        require(c['verification'].get('review_label') == LABEL, f'v0.2.6D: {i} carries the exact review label in verification.review_label')
        require(c['verification'].get('review') == REVIEW, f'v0.2.6D: {i} review level is MODEL_CROSS_FAMILY at the deduction level; not human, not formalized')
    b23 =' '.join(ccl['B.23']['statement'].split())
    require('min(h_p, p - 1) = min(r_p, p - 1) = min(d_p, p - 1)' in b23, 'v0.2.6D: B.23 states the identity with the cap p - 1')
    require('h_p < 4 <=> h_p = 2 <=> r_p = 2 <=> d_p <= 3 <=> Sha(E/Q)[p^infinity] = 0' in b23 and not re.search(r'h_p ?(<=|\u2264|=<) ?4', b23),
            'v0.2.6D: B.23 uses the strict inequality h_p < 4')
    require(all(k in b23 for k in ('every good prime p >= 5', 'at its actual conductor prime to pN', 'faithful character', 'h_p = +infinity is allowed',
                                   'full Bullach-Honnor-normalized', 'mod-p unit')),
            'v0.2.6D: B.23 defines h_p, r_p and d_p as the scope does (actual conductor, faithful characters, +infinity allowed)')
    require(ccl['B.23']['qualifications'][:3] == SENTENCES, 'v0.2.6D: B.23 carries the three mandatory scope sentences, verbatim')
    b24 = ' '.join(ccl['B.24']['statement'].split())
    require('suppose delta_{q_1 q_2} is a mod-p unit' in b24 and 'theta_L = delta_{q_1 q_2} * T_1 T_2 (mod p, J^3)' in b24
            and 'actual conductor q_1 q_2' in b24 and 'exact depth 2' in b24
            and any(q.startswith('The antecedent is a sufficient witness, not an established fact.') for q in ccl['B.24']['qualifications']),
            'v0.2.6D: B.24 is stated with its antecedent (a sufficient witness, not an established fact)')
    n24 = ccl['B.24']['normalization']
    require('Omega_E^+ = 2*omega_1' in n24 and 'one half of the production symbol' in n24,
            'v0.2.6D: B.24 records the total-real-period normalization and the factor 2 against the production symbol')
    b, c = bcl['B.22'], ccl['B.22']
    require(all(c[f] == b[f] for f in c if f != 'qualifications') and set(c) == set(b), "v0.2.6D: B.22's statement, kind, grades, provenance and other fields are unchanged")
    require(b['qualifications'].count(B22_OLD_Q) == 1 and c['qualifications'] == [B22_NEW_Q if q == B22_OLD_Q else q for q in b['qualifications']],
            "v0.2.6D: B.22 changes only its one qualification: the cross-reference to B.23 and 'not evaluated at any p >= 53'")
    b1, c1 = bcl['O.1'], ccl['O.1']
    old1 = [q for q in b1['qualifications'] if q.startswith(O1_OLD_PREFIX)]
    require(len(old1) == 1 and c1['qualifications'] == [O1_NEW_Q if q == old1[0] else q for q in b1['qualifications']]
            and c1['kind'] == 'OPEN' and c1['grades'] == [] and c1['statement'] == b1['statement'],
            "v0.2.6D: O.1 carries the scope's frontier text verbatim in place of the v0.2.6 wording; O.1 stays OPEN")
    ev = {i: {e['path'] for e in ccl[i]['evidence']} for i in NEW_IDS}
    rel = set(REC['released_governing'])
    require(ev['B.23'] == rel and set(BRIDGE_REQUIRED) <= ev['B.24'] <= rel,
            'v0.2.6D: B.23 cites exactly the released governing files, and B.24 cites the bridge records')


def check_governing(REC):
    want_tp, own = set(), set()
    man = {n: h for h, n in (l.split('  ', 1) for l in (R / _S / CX / 'MANIFEST.sha256').read_text().splitlines())}
    for n, h in man.items():
        (want_tp if n.startswith('sources/') else own).add((CX, n, h))
    got_tp = {(x['folder'], x['name'], x['sha256']) for x in REC['governing_files']['third_party_hash_only']}
    require(len(REC['governing_files']['third_party_hash_only']) == len(got_tp) == len(want_tp) == 3 and got_tp == want_tp
            and not any((R / _S / f / n).exists() for f, n, _ in want_tp),
            "v0.2.6D: Codex's three page renders are bound by hash exactly as its released manifest lists them, and are not copied")
    require(all((R / _S / f / n).is_file() and sha(R / _S / f / n) == h for f, n, h in own)
            and {_S + f + n for f, n, _ in own} | {_S + CX + 'MANIFEST.sha256'} | set(SINGLES) == set(REC['released_governing']),
            "v0.2.6D: every own file of Codex's review (the return included) is released byte-identical; the released governing set is exact")
    rman = {n: h for h, n in (l.split('  ', 1) for l in (R / _S / RET / 'MANIFEST.sha256').read_text().splitlines())}
    require(len(rman) == 14 and all(sha(R / _S / RET / n) == h for n, h in rman.items()), "v0.2.6D: the return's 14 files match its own manifest")
    v26 = json.loads((R / 'review/V026_APPLIED.json').read_text())
    cx_sb = json.loads((R / _S / CX / 'SOURCE_BINDINGS.json').read_text())
    require(BH_BOUND in {(x['folder'], x['name'], x['sha256']) for x in v26['governing_files']['third_party_hash_only']}
            and any(x.get('sha256') == BH_BOUND[2] and x.get('source', '').endswith(BH_BOUND[1]) for x in cx_sb)
            and REC['bh_pdf_binding'] == {'record': 'review/V026_APPLIED.json', 'folder': BH_BOUND[0], 'name': BH_BOUND[1], 'sha256': BH_BOUND[2]},
            'v0.2.6D: the Bullach-Honnor PDF named by the review is the one already bound by hash in the v0.2.6 record')


def main():
    REC = json.loads((R / REC_PATH).read_text())
    HR = REC['history_root']
    bc, added = REC['base_copies'], REC['added_paths']
    require(len(added) == len(set(added)), 'v0.2.6D: each added path is declared once')
    added = set(added); changed = set(bc)
    require(not (set(PRIOR_RECORDS) & (changed | added)), 'v0.2.6D: the v0.2.5, route-K, K2 and v0.2.6 records are unchanged')
    prev = manifest_rows(R / REC['prev_manifest']['path'])
    require(all(x['path'] == f'{HR}/{p}' and sha(R / x['path']) == x['sha256'] for p, x in bc.items()), 'v0.2.6D: preserved 8182b9c base copies intact')
    require(sha(R / REC['prev_manifest']['path']) == REC['prev_manifest']['sha256'], 'v0.2.6D: preserved 8182b9c manifest bound')
    require(not (added & set(prev)) and changed - {'MANIFEST.sha256'} <= set(prev), 'v0.2.6D: added paths are new; changed paths existed at 8182b9c')
    require(changed <= TEXT_EDIT_FILES | DERIVED_CHANGED and set(REC['text_edits']) == TEXT_EDIT_FILES,
            'v0.2.6D: the changed files are within the set fixed by this checker, and the declared text edits cover exactly its text files')
    decl = json.loads((R / 'review/V026D_EVIDENCE_ADDITIONS.json').read_text())
    dpaths = [a['release_path'] for a in decl['additions']]
    want_added = (NEW_FILES | set(dpaths) | {f'{HR}/{p}' for p in bc}
                  | {f'{HR}/evidence/{n}' for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')})
    require(added == want_added, 'v0.2.6D: the added files are exactly the new records, the declared evidence and the history copies')
    cur = manifest_rows(R / 'MANIFEST.sha256')
    require(set(cur) == (set(prev) | added) - {'MANIFEST.sha256'}, 'v0.2.6D: the file set is exactly the 8182b9c set plus the declared additions')
    cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    cols = cp[0].split('\t')
    prov = [dict(zip(cols, x.split('\t'))) for x in cp[1:] if x]
    rl = (R / 'evidence/REDACTIONS.tsv').read_text().split('\n')
    red = {r['release_path']: r for r in (dict(zip(rl[0].split('\t'), x.split('\t'))) for x in rl[1:] if x)}
    ppaths = [r['release_path'] for r in prov]
    srcfiles = {p.relative_to(R).as_posix() for p in (R / 'evidence/src').rglob('*') if p.is_file() or p.is_symlink()}
    require(len(ppaths) == len(set(ppaths)), 'v0.2.6D: no provenance path occurs twice (whole table)')
    require(set(ppaths) == srcfiles, 'v0.2.6D: provenance rows and evidence/src files correspond one to one (whole table)')
    require(all(sha(R / r['release_path']) == r['sha256'] for r in prov), 'v0.2.6D: every provenance row matches its file hash (whole table)')
    require(all((r['release_path'] in red and red[r['release_path']]['released_sha256'] == r['sha256']
                 and red[r['release_path']]['original_sha256'] == r['original_sha256'])
                or (r['release_path'] not in red and r['bytes'] == str((R / r['release_path']).stat().st_size)) for r in prov)
            and set(red) <= set(ppaths), 'v0.2.6D: sizes agree with the files, except the declared redactions (whole table)')
    tmp = Path(tempfile.mkdtemp(prefix='v026d_reconstruct_'))
    try:
        T = tmp / 'repo'
        shutil.copytree(R, T, ignore=shutil.ignore_patterns('.git'), symlinks=True)
        for p, x in bc.items():
            (T / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(R / x['path'], T / p)
        for p in added:
            (T / p).unlink()
        tfiles = {q.relative_to(T).as_posix() for q in T.rglob('*') if q.is_file() or q.is_symlink()}
        require({q for q in tfiles if not ignored(q)} == set(prev), 'v0.2.6D: the reconstructed file set equals the 8182b9c manifest (set equality)')
        require(all(sha(T / q) == h for q, h in prev.items()), 'v0.2.6D: every reconstructed file has its 8182b9c hash')
        require(sha(T / 'tools/verify_patch_release.py') == REC['prev_checker_sha256'], 'v0.2.6D: reconstructed checker is the v0.2.6 checker, byte-identical')
        r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_patch_release.py')], capture_output=True, text=True, cwd=T)
        old_ok = r.returncode == 0 and 'V026_TRANSITION_PASS' in r.stdout and 'PATCH_RECHECK_PASS' in r.stdout
        if not old_ok:
            print(r.stdout[-1500:] + r.stderr[-1500:])
        require(old_ok, 'v0.2.6D: the v0.2.6 checker passes on the reconstructed 8182b9c tree (it reconstructs every earlier tree)')
        if '--with-prev-controls' in sys.argv:
            r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_v026_transition.py'), '--negative-controls'], capture_output=True, text=True, cwd=T)
            print('\n'.join(l for l in r.stdout.splitlines() if ' exit=' in l))
            require(r.returncode == 0 and 'NEGATIVE_CONTROLS_PASS' in r.stdout, 'v0.2.6D: the v0.2.6 negative controls pass on the reconstructed 8182b9c tree')
        bdoc = json.loads((T / 'claims/claims.json').read_text()); cdoc = json.loads((R / 'claims/claims.json').read_text())
        bcl = {c['id']: c for c in bdoc['claims']}; ccl = {c['id']: c for c in cdoc['claims']}
        border = [c['id'] for c in bdoc['claims']]; k = border.index('B.22') + 1
        require([c['id'] for c in cdoc['claims']] == border[:k] + NEW_IDS + border[k:] == REC['claim_order']
                and len(REC['claim_order']) == len(set(REC['claim_order'])), 'v0.2.6D: the 8182b9c claims in order, with B.23-B.24 inserted after B.22, each once')
        require({k: v for k, v in bdoc.items() if k != 'claims'} == {k: v for k, v in cdoc.items() if k != 'claims'}, 'v0.2.6D: claims.json header unchanged')
        delta = REC['claim_delta']
        require(set(delta) == set(REVISED) and all(set(delta[i]) == REVISED[i] for i in delta),
                'v0.2.6D: the revised claims are exactly B.22 (qualifications) and O.1 (qualifications, evidence)')
        ok = True
        for i in bcl:
            if i not in delta:
                ok &= ccl[i] == bcl[i]; continue
            exp = dict(bcl[i])
            for f, x in delta[i].items():
                ok &= bcl[i].get(f) == x['before']; exp[f] = x['after']
            ok &= ccl[i] == exp
        require(ok, 'v0.2.6D: every 8182b9c claim equals its 8182b9c value plus exactly the declared field changes')
        require(all(REC['new_claims'][i] == ccl[i] for i in NEW_IDS) and set(REC['new_claims']) == set(NEW_IDS), 'v0.2.6D: the new claims equal the recorded ones')
        require((R / 'claims/LABELS.md').read_bytes() == (T / 'claims/LABELS.md').read_bytes()
                and all(set(c['grades']) <= {'IMPORTED_PUBLISHED', 'IMPORTED_PREPRINT', 'PROVED_WRITTEN', 'PROVED_COMPUTER_ASSISTED',
                                             'EXACT_COMPUTATION', 'LEAN_CHECKED', 'NUMERICAL_EVIDENCE'} for c in ccl.values()),
                'v0.2.6D: the grade vocabulary is unchanged and every grade is a release grade ("DERIVED" is prose, not a grade)')
        found = scan(set(cur) | {'MANIFEST.sha256'}, cdoc['claims'])
        for key, msg in (('remains', 'no outward text says "only/all that remains"'), ('nomethod', 'no outward text claims that no method exists'),
                         ('finproved', 'no outward text asserts that FIN, finite support or a uniform bound has been proved'),
                         ('witness', 'no outward text claims a two-prime or depth-two witness'),
                         ('vanish', 'no outward text claims a new vanishing prime or an infinite vanishing set'),
                         ('novalue', 'no outward text says that no such value has been computed (scope item 4)'),
                         ('b22conv', 'no outward text attributes the converse to B.22 itself'),
                         ('everyfield', 'no outward text says that every field or a preselected field attains depth two'),
                         ('oldtarget', 'the v0.2.6 frontier wording ("no converse ... is claimed") is replaced outward'),
                         ('old81', 'no outward line assigns <= 81 to the actual regulator (K2)'),
                         ('e1', 'every outward 12.5(4) line says that its final length inequality is printed for V (K2)'),
                         ('oldlabel', 'the old route-K label stays out of the claims, paper, README and brief (K2)')):
            require(not found[key], 'v0.2.6D: ' + msg + (f' {found[key][:4]}' if found[key] else ''))
        check_claims(ccl, bcl, REC)
        check_governing(REC)
        p09 = (R / 'paper/sections/09_reductions.tex').read_text(); p11 = (R / 'paper/sections/11_remaining.tex').read_text()
        require(all(h in p09 for h in PAPER_HEADERS.values()) and all(s in p09 for s in SENTENCES_TEX)
                and 'one half of the production symbol for this seed' in p09,
                'v0.2.6D: the manuscript records B.23-B.24 with their grades, the provenance clause, the scope sentences and the factor-2 note')
        m = re.search(r'\\cid\{B\.23\}.*?\\end\{researchrecord\}', p09, re.S)
        require(m and '\\min(h_p,p-1)=\\min(r_p,p-1)=\\min(d_p,p-1)' in m.group(0) and 'h_p<4\\iff h_p=2\\iff r_p=2\\iff d_p\\le3' in m.group(0)
                and not re.search(r'h_p\s*\\le(q)?\s*4', m.group(0)), 'v0.2.6D: the manuscript states B.23 with the cap and the strict inequality')
        m = re.search(r'\\cid\{B\.22\}.*?\\subsection\{Depth, witness length', p09, re.S)
        require(m and 'The converse holds by \\cid{B.23} (derived 2026-09-30)' in m.group(0) and 'It has not been evaluated at any $p\\ge53$.' in m.group(0),
                "v0.2.6D: the manuscript's B.22 passage cross-refers to B.23 and says 'not evaluated at any p >= 53'")
        require(all(k in p11 for k in PAPER_FRONTIER), "v0.2.6D: §11 states the scope's frontier text")
        readme = (R / 'README.md').read_text()
        require('**The uniform step.** ' + TARGET in readme and '**' + README_B22 + '**' in readme and PROV in readme,
                "v0.2.6D: the README states the scope's frontier, the corrected B.22 row and the provenance clause")
        rk = (R / 'RECHECK_V0_2_6.md').read_text()
        require(LABEL in rk and TARGET in rk and REC['review_label'] == LABEL, 'v0.2.6D: the recheck note and the record carry the exact review label')
        for p, edits in REC['text_edits'].items():
            s = (T / p).read_text()
            for e in edits:
                require(s.count(e['old']) == 1, f'v0.2.6D: edit anchor occurs exactly once in the 8182b9c {p}')
                if p.startswith('paper/') or p == 'README.md':
                    new = e['new'].replace(PROV, '').replace(TARGET, '')
                    require(all(new.count(mk) <= e['old'].count(mk) for mk in PROCESS_MARKERS), f'v0.2.6D: no internal process marker added to {p}')
                s = s.replace(e['old'], e['new'])
            require((R / p).read_text() == s, f'v0.2.6D: {p} equals the 8182b9c file plus exactly the declared edits')
        ex_old, ex_new = (T / 'tools/extra_evidence.txt').read_text(), (R / 'tools/extra_evidence.txt').read_text()
        require(ex_new == ex_old + REC['extra_evidence_append'], 'v0.2.6D: tools/extra_evidence.txt is the 8182b9c file plus exactly the declared appended text')
        bp = (T / 'evidence/PROVENANCE.tsv').read_text().split('\n')
        require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'v0.2.6D: every 8182b9c provenance row preserved byte for byte, in order')
        tlog = json.loads((R / REC['evidence']['transition_log']['path']).read_text())
        want = {a['release_path']: a for a in decl['additions']}
        appended_lines = [l for l in REC['extra_evidence_append'].splitlines() if l and not l.startswith('#')]
        require(len(dpaths) == len(set(dpaths)) and len(tlog['appended']) == len(set(tlog['appended'])) and set(tlog['appended']) == set(dpaths)
                and len(appended_lines) == len(set(appended_lines)) and set(appended_lines) == {a['original_path'] for a in decl['additions']},
                'v0.2.6D: the declaration, the logged append list and the appended source list name the same files, each exactly once')
        require(set(dpaths) == set(REC['released_governing']) and all(a['disposition'] == 'admitted_unmasked' for a in decl['additions']),
                'v0.2.6D: the declared additions are exactly the released governing files, each admitted unmasked')
        expect = ['\t'.join([p, want[p]['original_path'], want[p]['sha256'], str(want[p]['bytes']), 'extra', '', '', '', want[p]['sha256']]) for p in tlog['appended']]
        require(cp[len(bp) - 1:-1] == expect, 'v0.2.6D: the appended provenance rows are exactly one row per declared addition, in logged order, with exact content')
        require(all((R / 'evidence' / n).read_bytes() == (T / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')),
                'v0.2.6D: exclusion and redaction tables unchanged')
        require(all(sha(R / a) == want[a]['sha256'] for a in want), 'v0.2.6D: declared evidence files present with their hashes')
        rsc = json.loads((R / REC['evidence']['retained_source_changes']['path']).read_text())['retained_source_changes']
        v25 = {x['release_path'] for x in json.loads((R / 'review/V025_RETAINED_SOURCE_CHANGES.json').read_text())['retained_source_changes']}
        bprov = {x.split('\t')[0]: x.split('\t') for x in bp[1:] if x}
        require(len({x['release_path'] for x in rsc}) == len(rsc) and all(x['release_path'] in bprov and bprov[x['release_path']][2] == x['released_sha256']
                                                                          and sha(R / x['release_path']) == x['released_sha256'] for x in rsc),
                'v0.2.6D: each retained source change is an 8182b9c row, declared once, whose released bytes are unchanged')
        require(v25 | {REPORT_ROW[0]} <= {x['release_path'] for x in rsc} and any(x['release_path'] == REPORT_ROW[0] and x['released_sha256'] == REPORT_ROW[1] for x in rsc),
                "v0.2.6D: the Claude-report row (ca86c869..., a byte prefix of the live file) and the five v0.2.5 rows are retained, never refreshed")
        require(sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in tlog.get('retained_source_changes', []))
                == sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in rsc), 'v0.2.6D: the transition log retained exactly the declared source changes')
        require(tlog['baseline_tables'] == {n: {'path': f'{HR}/evidence/{n}', 'sha256': sha(T / 'evidence' / n)} for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')},
                'v0.2.6D: the transition started from the 8182b9c tables')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ev = REC['evidence']
    require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'transition_log', 'retained_source_changes')),
            'v0.2.6D: evidence declaration, retained-change declaration and transition log bound')
    require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}, 'v0.2.6D: transition log matches the current tables')
    t = subprocess.run([sys.executable, '-B', str(R / 'tools/build_evidence_transition.py'), '--self-test'], capture_output=True, text=True)
    require(t.returncode == 0 and 'SELF_TEST_PASS' in t.stdout and [l.split()[-1] for l in t.stdout.splitlines()[:-1]] == ['rejected'] * 19,
            'v0.2.6D: the evidence transition tool rejects all 19 of its self-test corruptions')
    gov = [g for item in REC['governing_files'].values() for g in item]
    require(all(sha(R / g['release_path']) == g['sha256'] for g in gov if g.get('release_path')), 'v0.2.6D: every released governing file matches its bound sha256')
    bound = set(REC['current_bindings'])
    require(bound == (changed | added) - {'MANIFEST.sha256', REC_PATH} and all(sha(R / p) == h for p, h in REC['current_bindings'].items()),
            'v0.2.6D: every changed or added file (except the manifest and this record) bound to its bytes')
    for gen in ('build_index.py', 'build_brief.py'):
        g = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
        require(g.returncode == 0, 'v0.2.6D: generated output current: ' + gen)
    for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
        require(not ((changed | added) & set(json.loads((R / 'review' / name).read_text())['files'])), 'v0.2.6D: no edited path among the non-redirectable ' + name)
    print('V026D_TRANSITION_PASS: the 8182b9c tree reconstructed and its checker passes; the V026-D delta is exactly the declared one')


# ---------------------------------------------------------------- negative controls (throwaway copies only)
def _rebind_all(t):
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    tl = t / d['evidence']['transition_log']['path']; tj = json.loads(tl.read_text())
    tj['result_tables'] = {n: sha(t / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}
    tl.write_text(json.dumps(tj, indent=1, ensure_ascii=False) + '\n')
    for k in ('declared', 'transition_log', 'retained_source_changes'):
        d['evidence'][k]['sha256'] = sha(t / d['evidence'][k]['path'])
    d['current_bindings'] = {p: sha(t / p) for p in d['current_bindings'] if (t / p).exists()}
    for item in d['governing_files'].values():
        for g in item:
            if g.get('release_path') and (t / g['release_path']).exists():
                g['sha256'] = sha(t / g['release_path'])
    cl = {c['id']: c for c in json.loads((t / 'claims/claims.json').read_text())['claims']}
    d['claim_order'] = list(cl)
    base = {c['id']: c for c in json.loads((t / d['history_root'] / 'claims/claims.json').read_text())['claims']}
    d['claim_delta'] = {i: {f: {'before': base[i].get(f), 'after': cl[i][f]} for f in cl[i] if cl[i][f] != base[i].get(f)} for i in d['claim_delta']}
    d['new_claims'] = {i: cl[i] for i in d['new_claims'] if i in cl}
    rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    m = t / 'MANIFEST.sha256'
    m.write_text(''.join(f"{sha(t / l.split('  ', 1)[1])}  {l.split('  ', 1)[1]}\n" for l in m.read_text().splitlines() if (t / l.split('  ', 1)[1]).exists()))


def _prov(t):
    p = t / 'evidence/PROVENANCE.tsv'; return p, p.read_text().split('\n')


def _n_old(t):
    d = json.loads((t / REC_PATH).read_text())
    return len((t / d['history_root'] / 'evidence/PROVENANCE.tsv').read_text().split('\n')) - 1


def _spec_edit(t, rel, old, new):
    p = t / rel; s = p.read_text(); assert s.count(old) == 1, old[:60]; p.write_text(s.replace(old, new))
    for gen in ('build_index.py', 'build_brief.py'):
        subprocess.run([sys.executable, '-B', str(t / 'tools' / gen)], capture_output=True, check=True)


def _text_rebound(t, rel, old, new):
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    e = next(e for e in d['text_edits'][rel] if old in e['new'])
    e['new'] = e['new'].replace(old, new, 1); rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    p = t / rel; s = p.read_text(); assert s.count(old) >= 1; p.write_text(s.replace(old, new, 1))


P2, P4, CM = 'claims/spec/part2_bridges.py', 'claims/spec/part4_open.py', 'claims/spec/common.py'
P09, P11 = 'paper/sections/09_reductions.tex', 'paper/sections/11_remaining.tex'
def m_le4(t):
    _spec_edit(t, P2, "'h_p < 4 <=> h_p = 2 <=>", "'h_p <= 4 <=> h_p = 2 <=>"); _rebind_all(t)
def m_cap_dropped(t):
    _spec_edit(t, P2, "'min(h_p, p - 1) = min(r_p, p - 1) = min(d_p, p - 1). Consequently", "'h_p = r_p = d_p. Consequently"); _rebind_all(t)
def m_every_field(t):
    _spec_edit(t, P2, "'The cap is needed: from degree p - 1 on,", "'In particular every field attains depth two. The cap is needed: from degree p - 1 on,"); _rebind_all(t)
def m_preselected_paper(t):
    _text_rebound(t, P09, 'the converse comes from the following bridge.', 'the converse comes from the following bridge, so a preselected field attains depth two.'); _rebind_all(t)
def m_b24_no_antecedent(t):
    _spec_edit(t, P2, "and suppose delta_{q_1 q_2} is a mod-p unit. Let '", "and delta_{q_1 q_2} is a mod-p unit. Let '"); _rebind_all(t)
def m_b24_theorem(t):
    _spec_edit(t, P2, "'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='written deduction from a preprint theorem', section='9',\n          evidence=v26d_bridge_evidence()",
               "'THEOREM', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='written deduction from a preprint theorem', section='9',\n          evidence=v26d_bridge_evidence()"); _rebind_all(t)
def m_b22_converse(t):
    _spec_edit(t, CM, "    CROSSREF = 'The converse holds by B.23 (derived 2026-09-30).'", "    CROSSREF = 'B.22 itself proves the converse.'"); _rebind_all(t)
def m_b22_statement(t):
    _spec_edit(t, P2, "(Definition 2.2, total real period '\n          'Omega^+ = 2*omega_1), then Sha(E/Q)[p^infinity] = 0.',",
               "(Definition 2.2, total real period '\n          'Omega^+ = 2*omega_1), then Sha(E/Q)[p^infinity] is finite.',"); _rebind_all(t)
def m_b22_grade(t):
    _spec_edit(t, P2, "'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='written deduction from a preprint theorem', section='9',\n          evidence=v26_depth_evidence(), depends_on=['B.21', 'A.3'],",
               "'THEOREM', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='written deduction from a preprint theorem', section='9',\n          evidence=v26_depth_evidence(), depends_on=['B.21', 'A.3'],"); _rebind_all(t)
def m_witness(t):
    _text_rebound(t, 'README.md', ' No applicable theorem was located in the screened sources.\n', ' A two-prime mod-p unit Kurihara witness has been found at every p >= 53.\n'); _rebind_all(t)
def m_vanish(t):
    _text_rebound(t, P11, 'this would give FIN.', 'this would give FIN. Hence $\\Sha(E/\\Q)[p^\\infty]=0$ for infinitely many $p$.'); _rebind_all(t)
def m_fin(t):
    _text_rebound(t, P11, 'this would give FIN.', 'this would give FIN. This revision proves FIN.'); _rebind_all(t)
def m_conditional_ok(t):       # POSITIVE: a conditional witness implication stays acceptable
    _text_rebound(t, 'README.md', ' No applicable theorem was located in the screened sources.\n',
                  ' No applicable theorem was located in the screened sources. If a two-prime unit witness exists at p, then Sha[p^∞] = 0 by B.23.\n'); _rebind_all(t)
def m_production(t):
    _spec_edit(t, P2, "normalization=(\"delta uses Castella-Sano's symbol Re(2*pi*i * integral of f)/Omega_E^+, where Omega_E^+ = 2*omega_1. That is one \"\n                         'half of the production symbol for this seed.'),",
               "normalization=('delta uses the production symbol of the release certificates.'),"); _rebind_all(t)
def m_label_altered(t):
    _spec_edit(t, CM, "Cross-family check of D1\u2013D5 by Claude Opus 5.5", "Cross-family check of D1\u2013D4 by Claude Opus 5.5"); _rebind_all(t)
def m_label_missing(t):
    _spec_edit(t, P2, "          verification={'review': V26D.REVIEW, 'review_label': V26D.LABEL,\n                        'derivations': 'D4:",
               "          verification={'review': V26D.REVIEW,\n                        'derivations': 'D4:"); _rebind_all(t)
def m_derived_grade(t):        # "DERIVED" forged into the generated claims as a grade of B.23, all rebound
    p = t / 'claims/claims.json'; d = json.loads(p.read_text())
    for c in d['claims']:
        if c['id'] == 'B.23':
            c['grades'] = ['DERIVED', 'IMPORTED_PREPRINT']
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n'); _rebind_all(t)
def m_novalue_spec(t):
    _spec_edit(t, P2, "'here. ' + V26D.CROSSREF + ' ' + V26D.NOT_EVAL,", "'here. ' + V26D.CROSSREF + ' No such value has been computed at any prime.',"); _rebind_all(t)
def m_novalue_readme(t):
    _text_rebound(t, 'README.md', '**not evaluated at p \u2265 53; converse: B.23**', '**no value computed; converse: B.23**'); _rebind_all(t)
def m_drop_governing(t):       # Codex's REPORT.md dropped everywhere (file, row, declaration, log, source list, spec, record), all rebound
    rel = _S + CX + 'REPORT.md'
    _spec_edit(t, CM, "    CX_FILES = ['REPORT.md', ", "    CX_FILES = [")
    _spec_edit(t, CM, "            E(V26D.CX + 'REPORT.md', 'independent check (Codex): checks 4 and 6, normalization'),\n", '')
    (t / rel).unlink()
    p, L = _prov(t); p.write_text('\n'.join(x for x in L if not x.startswith(rel + '\t')))
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    dp = t / d['evidence']['declared']['path']; dj = json.loads(dp.read_text()); src = next(a['original_path'] for a in dj['additions'] if a['release_path'] == rel)
    dj['additions'] = [a for a in dj['additions'] if a['release_path'] != rel]; dp.write_text(json.dumps(dj, indent=1, ensure_ascii=False) + '\n')
    tl = t / d['evidence']['transition_log']['path']; tj = json.loads(tl.read_text()); tj['appended'] = [a for a in tj['appended'] if a != rel]
    tl.write_text(json.dumps(tj, indent=1, ensure_ascii=False) + '\n')
    d['extra_evidence_append'] = d['extra_evidence_append'].replace(src + '\n', '')
    ex = t / 'tools/extra_evidence.txt'; ex.write_text(ex.read_text().replace(src + '\n', ''))
    d['added_paths'] = [a for a in d['added_paths'] if a != rel]; d['released_governing'] = [a for a in d['released_governing'] if a != rel]
    for item in d['governing_files'].values():
        item[:] = [g for g in item if g.get('release_path') != rel]
    rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n'); _rebind_all(t)
def m_drop_hashonly(t):
    rp = t / REC_PATH; d = json.loads(rp.read_text()); d['governing_files']['third_party_hash_only'].pop(0)
    rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n'); _rebind_all(t)
def m_report_refreshed(t):     # the live-file row refreshed instead of retained: the retained entry removed from the declaration, all rebound
    rp = t / REC_PATH; d = json.loads(rp.read_text()); f = t / d['evidence']['retained_source_changes']['path']; j = json.loads(f.read_text())
    j['retained_source_changes'] = [x for x in j['retained_source_changes'] if x['release_path'] != REPORT_ROW[0]]; f.write_text(json.dumps(j, indent=1) + '\n')
    tl = t / d['evidence']['transition_log']['path']; tj = json.loads(tl.read_text())
    tj['retained_source_changes'] = [x for x in tj['retained_source_changes'] if x['release_path'] != REPORT_ROW[0]]; tl.write_text(json.dumps(tj, indent=1, ensure_ascii=False) + '\n')
    _rebind_all(t)
def m_omit_appended(t):
    p, L = _prov(t); del L[_n_old(t) + 3]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_dup_appended(t):
    p, L = _prov(t); k = _n_old(t); L[k + 5] = L[k + 4]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_history_byte(t):
    p = t / 'review/history/v0.2.6/README.md'; b = bytearray(p.read_bytes()); b[10] ^= 1; p.write_bytes(bytes(b))
def m_paper_edit(t):
    p = t / P09; s = p.read_text(); assert 'no two-prime unit witness is supplied here.' in s
    p.write_text(s.replace('no two-prime unit witness is supplied here.', 'no two-prime unit witness is yet supplied here.', 1)); _rebind_all(t)
def m_other_file_rebound(t):
    rel = 'paper/sections/02_curve.tex'; d = json.loads((t / REC_PATH).read_text()); hr = d['history_root']
    (t / hr / 'paper/sections').mkdir(parents=True, exist_ok=True); shutil.copyfile(t / rel, t / hr / rel)
    s = (t / rel).read_text(); (t / rel).write_text(s.replace('the', 'THE', 1))
    d['base_copies'][rel] = {'path': f'{hr}/{rel}', 'sha256': sha(t / hr / rel)}; d['added_paths'].append(f'{hr}/{rel}')
    d['current_bindings'][rel] = ''; d['current_bindings'][f'{hr}/{rel}'] = ''
    (t / REC_PATH).write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    m = t / 'MANIFEST.sha256'; m.write_text(m.read_text() + f'{sha(t / hr / rel)}  {hr}/{rel}\n'); _rebind_all(t)
def m_undeclared_file(t):
    (t / 'evidence/src/UNDECLARED.txt').write_text('x\n')
    m = t / 'MANIFEST.sha256'; m.write_text(m.read_text() + hashlib.sha256(b'x\n').hexdigest() + '  evidence/src/UNDECLARED.txt\n')


CONTROLS = [('positive_control_unmodified', None, ''),
            ('positive_conditional_witness_implication_in_readme', m_conditional_ok, ''),
            ('1a_le4_in_b23_rebound', m_le4, 'B.23 uses the strict inequality h_p < 4'),
            ('1b_cap_p_minus_1_dropped_rebound', m_cap_dropped, 'B.23 states the identity with the cap p - 1'),
            ('2a_every_field_attains_depth_two_rebound', m_every_field, 'every field or a preselected field attains depth two'),
            ('2b_preselected_field_in_paper_rebound', m_preselected_paper, 'every field or a preselected field attains depth two'),
            ('3a_b24_without_antecedent_rebound', m_b24_no_antecedent, 'B.24 is stated with its antecedent'),
            ('3b_b24_as_theorem_rebound', m_b24_theorem, 'B.24 has kind CONDITIONAL'),
            ('4a_converse_attributed_to_b22_rebound', m_b22_converse, 'attributes the converse to B.22 itself'),
            ('4b_b22_statement_changed_rebound', m_b22_statement, 'the revised claims are exactly B.22 (qualifications)'),
            ('4c_b22_kind_changed_rebound', m_b22_grade, 'the revised claims are exactly B.22 (qualifications)'),
            ('5a_witness_claimed_in_readme_rebound', m_witness, 'no outward text claims a two-prime or depth-two witness'),
            ('5b_infinite_vanishing_claimed_in_paper_rebound', m_vanish, 'no outward text claims a new vanishing prime'),
            ('5c_fin_claimed_in_paper_rebound', m_fin, 'no outward text asserts that FIN'),
            ('6_delta_in_production_normalization_without_factor_2_rebound', m_production, 'B.24 records the total-real-period normalization and the factor 2'),
            ('7a_review_label_altered_rebound', m_label_altered, 'B.23 carries the exact review label'),
            ('7b_review_label_missing_rebound', m_label_missing, 'B.24 carries the exact review label'),
            ('8_derived_used_as_release_grade_rebound', m_derived_grade, '"DERIVED" is prose, not a grade'),
            ('9a_b22_no_such_value_computed_restored_rebound', m_novalue_spec, 'no outward text says that no such value has been computed'),
            ('9b_readme_no_value_computed_restored_rebound', m_novalue_readme, 'no outward text says that no such value has been computed'),
            ('10a_governing_file_dropped_rebound_all', m_drop_governing, 'B.23 cites exactly the released governing files'),
            ('10b_hash_only_binding_dropped_rebound', m_drop_hashonly, "Codex's three page renders are bound by hash"),
            ('10c_claude_report_row_not_retained_rebound', m_report_refreshed, 'the Claude-report row'),
            ('a_appended_row_omitted_rebound_all', m_omit_appended, 'provenance rows and evidence/src files correspond one to one'),
            ('b_duplicate_rebinds_omitted_appended_row', m_dup_appended, 'no provenance path occurs twice'),
            ('c_historical_copy_byte_altered', m_history_byte, 'preserved 8182b9c base copies intact'),
            ('d_undeclared_paper_edit_rebound', m_paper_edit, '09_reductions.tex equals the 8182b9c file plus exactly the declared edits'),
            ('e_undeclared_edit_outside_fixed_set_rebound_all', m_other_file_rebound, 'the changed files are within the set fixed by this checker'),
            ('f_undeclared_evidence_file', m_undeclared_file, 'the file set is exactly the 8182b9c set plus the declared additions')]


def negative_controls():
    res = {}
    for name, mut, want in CONTROLS:
        tmp = Path(tempfile.mkdtemp(prefix='v026d_negctl_'))
        try:
            t = tmp / 'repo'; shutil.copytree(R, t, ignore=shutil.ignore_patterns('.git'), symlinks=True)
            if mut:
                mut(t)
            r = subprocess.run([sys.executable, '-B', str(t / 'tools/verify_v026d_transition.py')], capture_output=True, text=True, cwd=t)
            first = next((l for l in (r.stdout + r.stderr).splitlines() if l.startswith('FAIL')), '')
            positive = name.startswith('positive')
            ok = (r.returncode == 0 and 'V026D_TRANSITION_PASS' in r.stdout) if positive else (r.returncode != 0 and want in first)
            res[name] = {'exit': r.returncode, 'as_expected': ok, 'first_fail': first}
            print(f"{name:62s} exit={r.returncode} {'OK' if ok else 'UNEXPECTED'}  {first[:120]}", flush=True)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    good = all(x['as_expected'] for x in res.values())
    print(json.dumps(res, indent=1, ensure_ascii=False))
    print('NEGATIVE_CONTROLS_PASS' if good else 'NEGATIVE_CONTROLS_FAIL')
    return good


if __name__ == '__main__':
    if '--negative-controls' in sys.argv:
        raise SystemExit(0 if negative_controls() else 1)
    main()
