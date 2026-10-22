#!/usr/bin/env python3
"""v0.2.6 transition check (the Kurihara position, B.20-B.22): reconstruct the v0.2.5 K2 tree exactly, run ITS checker
unchanged, then check the v0.2.6 delta.

  python3 tools/verify_v026_transition.py                         the check (prints V026_TRANSITION_PASS)
  python3 tools/verify_v026_transition.py --with-prev-controls    also run the K2 negative controls in the reconstruction
  python3 tools/verify_v026_transition.py --negative-controls     corrupt throwaway copies; every corruption must FAIL

1. Copy this tree, restore every path in the record's `base_copies` (the 4344c6a bytes kept under review/history/v0.2.5k2/),
   remove every path in `added_paths`; the reconstructed file set must EQUAL the preserved 4344c6a manifest.
2. Run the reconstructed tree's tools/verify_patch_release.py (the K2 checker, byte-identical). It reconstructs the route-K
   tree in turn, and so on back. It must pass.
3. Check the v0.2.6 delta by exact rows, exact lists and set equality with uniqueness. The changed and added files must be
   exactly the sets fixed HERE. The semantic bounds are also fixed here (not in the record): B.20's coverage (every good
   p >= 5; no exclusion of 19, 59, 487; no restriction to ordinary primes; nothing claimed at p <= 3 or at a bad prime),
   its version caveat and ordinary-coverage explanation, "mod-p unit", B.21's identity and scope sentence, B.22's strict
   "< 4", actual conductor and sufficiency only, the verbatim review label, the governing files (own files copied, 29
   third-party files bound by hash only), and outward scans (no "only/all that remains", no "no method exists", no
   assertion that FIN, finite support or a uniform bound has been proved; the K2 scans are kept).
Standard library only; this repository is never written.
"""
import hashlib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
REC_PATH = 'review/V026_APPLIED.json'
PRIOR_RECORDS = ('review/V025_BANK_APPLIED.json', 'review/V025K_ROUTEK_APPLIED.json', 'review/V025K2_APPLIED.json')
LABEL = ('Derived by Codex (OpenAI). Independent review by ChatGPT Pro (OpenAI): ACCEPT_AT_IMPORT_GRADE. The source statements '
         'were checked by Claude Opus 5.5 and Claude Fable 5.1 (Anthropic); the \u0394-component bridge by Claude Fable 5.1; the Part B '
         'deductions by Claude Opus 5.5. The author-hosted CLW revision is byte-identical across three independent downloads '
         '(sha256 0686fa41\u2026d036fb98); arXiv v1 is a different file. Not a human review; not formalized.')
REVIEW = ('MODEL_CROSS_FAMILY at the statement and deduction level: derived by Codex (OpenAI); independent review by ChatGPT Pro '
          '(OpenAI); source statements, the Delta-component bridge and the Part B deductions checked by Claude models (Anthropic); '
          'not a human review; not formalized')
PROV = ('derived by Codex (OpenAI) and independently reviewed by ChatGPT Pro (OpenAI), with source and deduction checks by '
        'Claude models (Anthropic); not a human review; not formalized')
TARGET = ('Find one finite set S containing {2,3,2243,4547,5843} and an independent argument that, for every p outside S, either a '
          'two-prime mod-p unit Kurihara witness exists or dim_{F_p} Sel_p(E/Q) \u2264 3. Under B.21 these two conditions are equivalent '
          'to each other and to Sha[p^\u221e]=0. A faithful value of the full BH-normalized element of a real cyclic degree-p field at its '
          'actual conductor prime to pN, with depth strictly below four, is another sufficient condition. No converse from Sha vanishing '
          'to existence of that character value is claimed. Fields, conductors and estimates may depend on p.')
SENTENCE = ('This is an identity, not an upper bound. The abstract dual module X = Z_p\u00b2 \u2295 (Z/p)\u00b2 needs four generators, with '
            'Fitt\u2082(X)=(p\u00b2), Fitt\u2083(X)=(p), and Fitt\u2084(X)=Z_p. It is compatible with M_\u221e=0 and first unit index four. This is a '
            'module countermodel to an inference from primitivity alone, not a claim about the seed at an uncomputed prime.')
CLW_SHA = '0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98'
NEW_IDS = ['B.20', 'B.21', 'B.22']
REVISED_IDS = ['O.1', 'O.2']
GRADES = ['PROVED_WRITTEN', 'IMPORTED_PREPRINT']
_S = 'evidence/src/'
SYN, RC = 'BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/', 'BSD_UNIFORM_SYNTHESIS_REVIEW_CHECK_CODEX_2026-09-30/'
PRO = RC + 'input/BSD_UNIFORM_SYNTHESIS_INDEPENDENT_REVIEW_2026-09-30/'
TI = 'BSD_SEED_V026_BANK_TASK_2026-09-30/inputs/'
SINGLES = [_S + x for x in ('BSD_BUILD_MAP/UNIFORM_STEP_REDUCTION_SHEET_2026-09-29.md', 'BSD_RUN_NOW_RETURNS_CHECK_CLAUDE_2026-09-29/REPORT.md',
                            TI + 'V026_SCOPE.md', TI + 'CODEX_THREE_BRIEFS_REVIEW_REPORT.md', TI + 'CLAUDE_ADDENDUM_25.md', TI + 'CLAUDE_ADDENDUM_28.md',
                            'BSD_SEED_V026_BANK_RETURN_OPUS_2026-09-30/checks/seed_local_facts.gp',
                            'BSD_SEED_V026_BANK_RETURN_OPUS_2026-09-30/checks/seed_local_facts.log')]
DEPTH_REQUIRED = [_S + SYN + 'DEPTH_TARGET.md', _S + PRO + 'PART_B_DEPTH.md', _S + PRO + 'RETURN.md', _S + TI + 'CLAUDE_ADDENDUM_28.md']
TEXT_EDIT_FILES = {'paper/sections/09_reductions.tex', 'paper/sections/11_remaining.tex', 'paper/refs.bib', 'paper/release_id.tex',
                   'README.md', 'tools/verify_patch_release.py'}
DERIVED_CHANGED = {'claims/spec/common.py', 'claims/spec/part2_bridges.py', 'claims/spec/part4_open.py', 'claims/claims.json',
                   'claims/CLAIM_INDEX.md', 'review/SYNTHESIS_CHECK_BRIEF.md', 'evidence/PROVENANCE.tsv', 'tools/extra_evidence.txt',
                   'paper/seed_bsd.pdf', 'paper/seed_bsd.bbl', 'MANIFEST.sha256', 'SOURCE_SNAPSHOT.json'}
NEW_FILES = {REC_PATH, 'tools/verify_v026_transition.py', 'RECHECK_V0_2_6.md', 'review/V026_EVIDENCE_ADDITIONS.json',
             'review/V026_EVIDENCE_TRANSITION.json'}
ALLOW_FILES = set(PRIOR_RECORDS) | {REC_PATH, 'tools/verify_v025k_transition.py', 'tools/verify_v025k2_transition.py', 'tools/verify_v026_transition.py'}
ALLOW_PREFIXES = ('review/history/', 'evidence/src/')
E1 = re.compile(r'12\.5 ?\(4\)')
OLD81 = re.compile(r'give only[^.;]{0,40}81')
OLD_K_LABEL_TAIL = 'all Anthropic models, not cross-family'
LABEL_SCOPE = ('claims/', 'paper/', 'README.md', 'review/SYNTHESIS_CHECK_BRIEF.md')
REMAINS = re.compile(r'\b(only remains|all that remains|only what remains)\b', re.I)
NOMETHOD = re.compile(r'\bno (known )?(method|mechanism)s? (exists?|is known|is available|can)\b|\bthere (is|are) no (known )?(method|mechanism)s?\b'
                      r'|\bno one has an? (method|mechanism)\b|\bno method whatsoever\b', re.I)
FIN_SUBJ = re.compile(r'\bFIN\b|finiteness of (the )?(\$\\Sha\$|Sha)(?!\s*\$?\[)|\bSha(\(E/Q\))? is finite\b|finite (prime )?support'
                      r'|\buniform (upper |torsion )?bound\b', re.I)
FIN_VERB = re.compile(r'\b(is|are|was|were|has|have|had)\s+(now\s+)?(been\s+)?(proved|proven|established|shown|settled)\b'
                      r'|\bnow (proved|proven|established|shown|settled)\b'
                      r'|\b(proves?|establish(es)?|settles?)\s+(that\s+)?(FIN\b|finite|the uniform|a uniform|finiteness)', re.I)
FIN_NEG = re.compile(r"\b(not|no|nor|neither|never|would|could|if|unless|open|conditional|none|without|needs?|suffices?|sufficient|"
                     r"target|equivalent|whether|question|until|remains?|only if|given)\b", re.I)
PROCESS_MARKERS = ['Fable', 'Opus', ' lane', 'Lane ', 'RUN_NOW', 'coordinator', 'addendum', 'Addendum', 'DRAFT', 'draft banner', 'session',
                   'only remains', 'all that remains', 'only what remains', 'ACCEPT_AT', 'CONFIRMED_WITH', 'PASS_AT', 'BANKED', 'BLOCKED',
                   'SOURCE_UPDATE', 'Pro-6']
PAPER_HEADERS = {'B.20': '\\cid{B.20}; written application of preprint theorems; ' + PROV + ']\\label{thm:kurexist}',
                 'B.21': '\\cid{B.21}; written deduction from preprint theorems; ' + PROV + ']\\label{thm:rp}',
                 'B.22': '\\cid{B.22}; written deduction from a preprint theorem; conditional; ' + PROV + ']\\label{thm:depth}'}
PAPER_FRONTIER = ['current known frontier for the uniform step', 'one finite set $S$ containing $\\{2,3,2243,4547,5843\\}$',
                  'either a two-prime mod-$p$ unit Kurihara witness exists or $\\dim_{\\F_p}\\Sel_p(E/\\Q)\\le3$',
                  'these two conditions are equivalent to each other and to $\\Sha[p^\\infty]=0$',
                  'at its actual conductor prime to $pN$, with depth strictly below four, is another sufficient condition',
                  'No converse from $\\Sha$ vanishing to existence of that character value is claimed.',
                  'Fields, conductors and estimates may depend on $p$.', 'No applicable theorem was located in the screened sources.']
PAPER_B20 = ['not on arXiv on 30 September 2026', 'listed only version~1, the squarefree-level version',
             'a later version could change the hypotheses of Theorem~A', 'Theorem~B of Castella--Sano as printed',
             '$a_{19}=4$, $a_{59}=-4$, $a_{487}=-28$', '$2242=2\\cdot19\\cdot59$, $5844=12\\cdot487$', 'create no extra exception']
CAVEAT = ['author-hosted', 'not on arXiv as of 2026-09-30', 'arXiv 2608.29470 lists only v1', 'squarefree-level version',
          'checked live on 2026-09-30', CLW_SHA, 'a later version could change the hypotheses of Theorem A']
ORDINARY = ['Castella-Sano Theorem B as printed', 'p > 3, (sur) and p not dividing c_phi', '[Wan15, BCS25]', 'a_19 = 4, a_59 = -4, a_487 = -28',
            'ellap', '2242 = 2*19*59, 5844 = 12*487', 'no extra exception', 'supersingular primes come from the CLW revision',
            'requires squarefree N']


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
    """Paths under the K2 scans (every file except the historical allowlist)."""
    return not (rel in ALLOW_FILES or rel.startswith(ALLOW_PREFIXES))


def outward_text(rel):
    """The public text scanned for wording: README, SHARING, the manuscript, and the hand-written claims documents."""
    return (rel in ('README.md', 'SHARING.md', 'claims/CONTRADICTIONS.md', 'claims/CROSS_CONNECTIONS.md', 'coverage/COVERAGE.md')
            or (rel.startswith('paper/') and rel.endswith(('.tex', '.bib'))))


def b20_coverage(stmt):
    """None if the statement covers exactly the good primes p >= 5 (19, 59, 487 not excluded; no ordinary-only restriction;
    nothing claimed at p <= 3 or at a bad prime); otherwise the reason."""
    s = ' '.join(stmt.split())
    if not re.search(r'\bevery (good (prime )?p ?>= ?5\b|prime p ?>= ?5 of good reduction\b)', s):
        return 'no universal quantifier over the good primes p >= 5'
    if re.search(r'(?<![Nn]on)(?<![Nn]on-)\bordinary\b', s):
        return 'restricted to (or phrased through) ordinary primes'
    if re.search(r'\bp ?>= ?[0-4]\b|\ball primes\b|\bevery prime\b(?! p ?>= ?5)', s):
        return 'a quantifier that reaches p <= 3'
    if re.search(r'\b(19|59|487)\b', s.replace('including the supersingular primes and 19, 59 and 487', '')):
        return '19, 59 or 487 mentioned outside the inclusion clause'
    for sent in re.split(r'(?<=\.)\s+', s):
        if re.search(r'\b(2243|4547|5843)\b|p ?<= ?3\b|\bp ?= ?[23]\b', sent) and not re.search(r'\bnot covered\b|\bexcluded\b', sent):
            return 'a bad prime or p <= 3 outside a not-covered sentence'
    return None


def scan(paths, claims):
    """Outward scans. K2 scans (12.5(4) wording, the old <= 81 phrase, the old route-K label) over every non-allowlisted
    file; wording scans (remains, no method, FIN proved) over the public text and the non-withdrawn claims."""
    out = {k: [] for k in ('e1', 'old81', 'oldlabel', 'remains', 'nomethod', 'finproved')}
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
            public.append((f"claims:{c['id']}", '\n'.join([c['title'], c['statement']] + c['qualifications'] + c['imports'])))
    for rel, text in public:
        for n, line in enumerate(text.splitlines(), 1):
            where = f'{rel}:{n}'
            if REMAINS.search(line):
                out['remains'].append(where)
            if NOMETHOD.search(line):
                out['nomethod'].append(where)
            for sent in re.split(r'(?<=[.;])\s+', line):
                if FIN_SUBJ.search(sent) and FIN_VERB.search(sent) and not FIN_NEG.search(sent):
                    out['finproved'].append(where)
    return out


def check_new_claims(ccl, REC):
    for i in NEW_IDS:
        c = ccl[i]
        require(c['grades'] == GRADES and c['kind'] == ('CONDITIONAL' if i == 'B.22' else 'THEOREM'),
                f'v0.2.6: {i} has kind {"CONDITIONAL" if i == "B.22" else "THEOREM"} and grades PROVED_WRITTEN, IMPORTED_PREPRINT only')
        require(c['verification'].get('review_label') == LABEL, f'v0.2.6: {i} carries the exact review label in verification.review_label')
        require(c['verification'].get('review') == REVIEW and not any(k.startswith('formal') or k == 'grade_label' for k in c['verification']),
                f'v0.2.6: {i} review level is MODEL_CROSS_FAMILY at the statement and deduction level; no human review, not formalized')
    b20, b21, b22 = ccl['B.20'], ccl['B.21'], ccl['B.22']
    why = b20_coverage(b20['statement'])
    require(why is None, 'v0.2.6: B.20 covers every good p >= 5 and nothing else' + (f' ({why})' if why else ''))
    require('mod-p unit' in b20['statement'] and 'mod-p unit' in b20['title'] and 'M_infinity(delta) = 0' in b20['statement']
            and not re.search(r'nonzero p-adic|p-adically nonzero|p-adic nonzero', b20['statement'] + b20['title']),
            'v0.2.6: B.20 asserts a mod-p unit witness (not merely a nonzero p-adic one) and M_infinity = 0')
    require(any(all(k in q for k in CAVEAT) for q in b20['qualifications']), 'v0.2.6: B.20 carries the pinned CLW author-revision caveat')
    require(any(all(k in q for k in ORDINARY) for q in b20['qualifications']), 'v0.2.6: B.20 carries the separate ordinary-coverage explanation (Castella-Sano Theorem B)')
    require(any(CLW_SHA in x and 'author-hosted revision dated 2026-09-21' in x and 'Theorem A' in x for x in b20['imports']),
            'v0.2.6: B.20 imports the pinned CLW revision, Theorem A')
    s21 = b21['statement']
    require(all(k in s21 for k in ('r_p := min{nu(n) : delta_n is nonzero mod p}', 'mod-p unit', 'r_p = dim_{F_p} Sel_p(E/Q)', 'even and >= 2',
                                   'r_p = 2 if and only if Sha(E/Q)[p^infinity] = 0', 'no finiteness of Sha is assumed'))
            and not re.search(r'nonzero p-adic|p-adically nonzero', s21), 'v0.2.6: B.21 states the unit-length identity and its equivalence')
    require(b21['qualifications'][0] == SENTENCE and 'only its Sha-independent clauses' in b21['imports'][0],
            'v0.2.6: B.21 carries the mandatory scope sentence and only the Sha-independent clauses of Kim Thm 1.8')
    s22 = ' '.join(b22['statement'].split())
    require('v_{zeta_p - 1}(chi(theta_K^MT)) < 4' in s22 and not re.search(r'<= ?4|\u2264 ?4|=< ?4', s22),
            'v0.2.6: B.22 uses the strict inequality < 4')
    require('whose actual conductor m is prime to pN' in s22 and 'at its actual conductor m' in s22
            and not re.search(r'multiple of|divisible by|any conductor|enlarged|some conductor|auxiliary modulus', s22),
            'v0.2.6: B.22 is stated at the actual conductor (no silent change of conductor)')
    require(any('norm relations of Bullach-Honnor Proposition 2.4, with their Euler factors retained' in q for q in b22['qualifications']),
            'v0.2.6: B.22 records that another conductor needs the norm relations with their Euler factors')
    require(not re.search(r'if and only if|\biff\b|equivalen|necessary|only if|<=>|\u27fa', s22)
            and s22.rstrip().endswith('then Sha(E/Q)[p^infinity] = 0.')
            and any(q.startswith('Sufficient only: no converse from Sha(E/Q)[p^infinity] = 0') for q in b22['qualifications']),
            'v0.2.6: B.22 is a sufficient criterion only (no converse or equivalence claimed)')
    require(any(q.startswith('The inequality is strict. A bound <= 4 is insufficient') for q in b22['qualifications']),
            'v0.2.6: B.22 records why "<= 4" is insufficient')
    ev = {i: {e['path'] for e in ccl[i]['evidence']} for i in NEW_IDS}
    rel = set(REC['released_governing'])
    require(set(DEPTH_REQUIRED) <= ev['B.21'] and set(DEPTH_REQUIRED) <= ev['B.22'] and rel - set(DEPTH_REQUIRED[:2]) <= ev['B.20']
            and set(SINGLES) <= ev['B.20'] and ev['B.20'] | ev['B.21'] | ev['B.22'] == rel,
            'v0.2.6: B.20-B.22 cite exactly the released governing files, with the required ones per claim')
    o1 = ccl['O.1']['qualifications']
    require(any(q == 'Current known frontier for the uniform step (B.20-B.22): ' + TARGET + ' No applicable theorem was located in the screened '
                'sources. Together with finiteness of the primary components at the primes of S, this target would give FIN.' for q in o1)
            and ccl['O.1']['kind'] == ccl['O.2']['kind'] == 'OPEN' and ccl['O.1']['grades'] == ccl['O.2']['grades'] == [],
            'v0.2.6: O.1 states the exact open target (verbatim); O.1 and O.2 stay OPEN with no grade')


def check_governing(REC):
    """Own files of the three governing folders released byte-identical (per their released manifests); the 29 third-party
    files bound by hash only and absent; the single governing files released."""
    want_tp, own = set(), set()
    for folder, is_tp in ((SYN, lambda n: n.startswith('sources/')), (RC, lambda n: n.startswith('CLW2_fresh')),
                          (PRO, lambda n: n.startswith('source_checks/') and n.endswith('.png'))):
        man = {n: h for h, n in (l.split('  ', 1) for l in (R / _S / folder / 'MANIFEST.sha256').read_text().splitlines())}
        for n, h in man.items():
            if is_tp(n):
                want_tp.add((folder, n, h))
            elif not n.startswith('input/'):
                own.add((folder, n, h))
    got_tp = {(x['folder'], x['name'], x['sha256']) for x in REC['governing_files']['third_party_hash_only']}
    require(len(REC['governing_files']['third_party_hash_only']) == len(got_tp) == len(want_tp) == 29 and got_tp == want_tp
            and not any((R / _S / f / n).exists() for f, n, _ in want_tp),
            'v0.2.6: the 29 third-party files are bound by hash exactly as the released manifests list them, and are not copied')
    require(all((R / _S / f / n).is_file() and sha(R / _S / f / n) == h for f, n, h in own)
            and {_S + f + n for f, n, _ in own} | {_S + f + 'MANIFEST.sha256' for f in (SYN, RC, PRO)} | set(SINGLES) == set(REC['released_governing']),
            'v0.2.6: every own file of the synthesis, the review and its return check is released byte-identical; the released governing set is exact')


def main():
    REC = json.loads((R / REC_PATH).read_text())
    HR = REC['history_root']
    bc, added = REC['base_copies'], REC['added_paths']
    require(len(added) == len(set(added)), 'v0.2.6: each added path is declared once')
    added = set(added); changed = set(bc)
    require(not (set(PRIOR_RECORDS) & (changed | added)), 'v0.2.6: the v0.2.5, route-K and K2 records are unchanged')
    prev = manifest_rows(R / REC['prev_manifest']['path'])
    require(all(x['path'] == f'{HR}/{p}' and sha(R / x['path']) == x['sha256'] for p, x in bc.items()), 'v0.2.6: preserved 4344c6a base copies intact')
    require(sha(R / REC['prev_manifest']['path']) == REC['prev_manifest']['sha256'], 'v0.2.6: preserved 4344c6a manifest bound')
    require(not (added & set(prev)) and changed - {'MANIFEST.sha256'} <= set(prev), 'v0.2.6: added paths are new; changed paths existed at 4344c6a')
    require(changed <= TEXT_EDIT_FILES | DERIVED_CHANGED and set(REC['text_edits']) == TEXT_EDIT_FILES,
            'v0.2.6: the changed files are within the set fixed by this checker, and the declared text edits cover exactly its text files')
    decl = json.loads((R / 'review/V026_EVIDENCE_ADDITIONS.json').read_text())
    dpaths = [a['release_path'] for a in decl['additions']]
    want_added = NEW_FILES | set(dpaths) | {f'{HR}/{p}' for p in bc} | {f'{HR}/evidence/{n}' for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}
    require(added == want_added, 'v0.2.6: the added files are exactly the new records, the declared evidence and the history copies')
    cur = manifest_rows(R / 'MANIFEST.sha256')
    require(set(cur) == (set(prev) | added) - {'MANIFEST.sha256'}, 'v0.2.6: the file set is exactly the 4344c6a set plus the declared additions')
    cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    cols = cp[0].split('\t')
    prov = [dict(zip(cols, x.split('\t'))) for x in cp[1:] if x]
    rl = (R / 'evidence/REDACTIONS.tsv').read_text().split('\n')
    red = {r['release_path']: r for r in (dict(zip(rl[0].split('\t'), x.split('\t'))) for x in rl[1:] if x)}
    ppaths = [r['release_path'] for r in prov]
    srcfiles = {p.relative_to(R).as_posix() for p in (R / 'evidence/src').rglob('*') if p.is_file() or p.is_symlink()}
    require(len(ppaths) == len(set(ppaths)), 'v0.2.6: no provenance path occurs twice (whole table)')
    require(set(ppaths) == srcfiles, 'v0.2.6: provenance rows and evidence/src files correspond one to one (whole table)')
    require(all(sha(R / r['release_path']) == r['sha256'] for r in prov), 'v0.2.6: every provenance row matches its file hash (whole table)')
    require(all((r['release_path'] in red and red[r['release_path']]['released_sha256'] == r['sha256']
                 and red[r['release_path']]['original_sha256'] == r['original_sha256'])
                or (r['release_path'] not in red and r['bytes'] == str((R / r['release_path']).stat().st_size)) for r in prov)
            and set(red) <= set(ppaths), 'v0.2.6: sizes agree with the files, except the declared redactions (whole table)')
    tmp = Path(tempfile.mkdtemp(prefix='v026_reconstruct_'))
    try:
        T = tmp / 'repo'
        shutil.copytree(R, T, ignore=shutil.ignore_patterns('.git'), symlinks=True)
        for p, x in bc.items():
            (T / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(R / x['path'], T / p)
        for p in added:
            (T / p).unlink()
        tfiles = {q.relative_to(T).as_posix() for q in T.rglob('*') if q.is_file() or q.is_symlink()}
        require({q for q in tfiles if not ignored(q)} == set(prev), 'v0.2.6: the reconstructed file set equals the 4344c6a manifest (set equality)')
        require(all(sha(T / q) == h for q, h in prev.items()), 'v0.2.6: every reconstructed file has its 4344c6a hash')
        require(sha(T / 'tools/verify_patch_release.py') == REC['prev_checker_sha256'], 'v0.2.6: reconstructed checker is the K2 checker, byte-identical')
        r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_patch_release.py')], capture_output=True, text=True, cwd=T)
        old_ok = r.returncode == 0 and 'V025K2_TRANSITION_PASS' in r.stdout and 'PATCH_RECHECK_PASS' in r.stdout
        if not old_ok:
            print(r.stdout[-1500:] + r.stderr[-1500:])
        require(old_ok, 'v0.2.6: the K2 checker passes on the reconstructed 4344c6a tree (it reconstructs every earlier tree)')
        if '--with-prev-controls' in sys.argv:
            r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_v025k2_transition.py'), '--negative-controls'], capture_output=True, text=True, cwd=T)
            print('\n'.join(l for l in r.stdout.splitlines() if ' exit=' in l))
            require(r.returncode == 0 and 'NEGATIVE_CONTROLS_PASS' in r.stdout, 'v0.2.6: the K2 negative controls pass on the reconstructed 4344c6a tree')
        bdoc = json.loads((T / 'claims/claims.json').read_text()); cdoc = json.loads((R / 'claims/claims.json').read_text())
        bcl = {c['id']: c for c in bdoc['claims']}; ccl = {c['id']: c for c in cdoc['claims']}
        border = [c['id'] for c in bdoc['claims']]; k = border.index('B.19') + 1
        require([c['id'] for c in cdoc['claims']] == border[:k] + NEW_IDS + border[k:] == REC['claim_order']
                and len(REC['claim_order']) == len(set(REC['claim_order'])), 'v0.2.6: the 4344c6a claims in order, with B.20-B.22 inserted after B.19, each once')
        require({k: v for k, v in bdoc.items() if k != 'claims'} == {k: v for k, v in cdoc.items() if k != 'claims'}, 'v0.2.6: claims.json header unchanged')
        delta = REC['claim_delta']
        require(set(delta) == set(REVISED_IDS) and all(set(delta[i]) <= {'qualifications', 'evidence'} for i in delta),
                'v0.2.6: the revised claims are exactly O.1 and O.2, and only their qualifications and evidence change')
        ok = True
        for i in bcl:
            if i not in delta:
                ok &= ccl[i] == bcl[i]; continue
            exp = dict(bcl[i])
            for f, x in delta[i].items():
                ok &= bcl[i].get(f) == x['before']; exp[f] = x['after']
            ok &= ccl[i] == exp
        require(ok, 'v0.2.6: every 4344c6a claim equals its 4344c6a value plus exactly the declared field changes')
        require(all(REC['new_claims'][i] == ccl[i] for i in NEW_IDS) and set(REC['new_claims']) == set(NEW_IDS), 'v0.2.6: the new claims equal the recorded ones')
        found = scan(set(cur) | {'MANIFEST.sha256'}, cdoc['claims'])
        for key, msg in (('remains', 'no outward text says "only/all that remains"'), ('nomethod', 'no outward text claims that no method exists'),
                         ('finproved', 'no outward text asserts that FIN, finite support or a uniform bound has been proved'),
                         ('old81', 'no outward line assigns <= 81 to the actual regulator (K2)'),
                         ('e1', 'every outward 12.5(4) line says that its final length inequality is printed for V (K2)'),
                         ('oldlabel', 'the old route-K label stays out of the claims, paper, README and brief (K2)')):
            require(not found[key], 'v0.2.6: ' + msg + (f' {found[key][:4]}' if found[key] else ''))
        check_new_claims(ccl, REC)
        check_governing(REC)
        p09 = (R / 'paper/sections/09_reductions.tex').read_text(); p11 = (R / 'paper/sections/11_remaining.tex').read_text()
        require(all(h in p09 for h in PAPER_HEADERS.values()) and all(k in p09 for k in PAPER_B20),
                'v0.2.6: the manuscript records B.20-B.22 with their grades, the provenance clause, the version caveat and the ordinary coverage')
        m = re.search(r'\\cid\{B\.22\}.*?\\end\{researchrecord\}', p09, re.S)
        require(m and '\\bigr)<4' in m.group(0) and not re.search(r'\\le(q)?\s*4|\\leqslant', m.group(0)) and 'actual conductor $m$' in m.group(0),
                'v0.2.6: the manuscript states B.22 with the strict inequality at the actual conductor')
        require(all(k in p11 for k in PAPER_FRONTIER), 'v0.2.6: §11 states the exact open target, no converse, and the screened-sources wording')
        readme = (R / 'README.md').read_text()
        require('**Current known frontier (the uniform step).** ' + TARGET in readme and PROV in readme and 'mod-p unit Kurihara witness' in readme,
                'v0.2.6: the README states the exact open target and the provenance clause')
        require(LABEL in (R / 'RECHECK_V0_2_6.md').read_text() and TARGET in (R / 'RECHECK_V0_2_6.md').read_text() and REC['review_label'] == LABEL,
                'v0.2.6: the recheck note and the record carry the exact review label')
        for p, edits in REC['text_edits'].items():
            s = (T / p).read_text()
            for e in edits:
                require(s.count(e['old']) == 1, f'v0.2.6: edit anchor occurs exactly once in the 4344c6a {p}')
                if p.startswith('paper/') or p == 'README.md':
                    new = e['new'].replace(PROV, '').replace(TARGET, '')
                    require(all(new.count(mk) <= e['old'].count(mk) for mk in PROCESS_MARKERS), f'v0.2.6: no internal process marker added to {p}')
                s = s.replace(e['old'], e['new'])
            require((R / p).read_text() == s, f'v0.2.6: {p} equals the 4344c6a file plus exactly the declared edits')
        ex_old, ex_new = (T / 'tools/extra_evidence.txt').read_text(), (R / 'tools/extra_evidence.txt').read_text()
        require(ex_new == ex_old + REC['extra_evidence_append'], 'v0.2.6: tools/extra_evidence.txt is the 4344c6a file plus exactly the declared appended text')
        bp = (T / 'evidence/PROVENANCE.tsv').read_text().split('\n')
        require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'v0.2.6: every 4344c6a provenance row preserved byte for byte, in order')
        tlog = json.loads((R / REC['evidence']['transition_log']['path']).read_text())
        want = {a['release_path']: a for a in decl['additions']}
        appended_lines = [l for l in REC['extra_evidence_append'].splitlines() if l and not l.startswith('#')]
        require(len(dpaths) == len(set(dpaths)) and len(tlog['appended']) == len(set(tlog['appended'])) and set(tlog['appended']) == set(dpaths)
                and len(appended_lines) == len(set(appended_lines)) and set(appended_lines) == {a['original_path'] for a in decl['additions']},
                'v0.2.6: the declaration, the logged append list and the appended source list name the same files, each exactly once')
        require(set(dpaths) == set(REC['released_governing']) and all(a['disposition'] == 'admitted_unmasked' for a in decl['additions']),
                'v0.2.6: the declared additions are exactly the released governing files, each admitted unmasked')
        expect = ['\t'.join([p, want[p]['original_path'], want[p]['sha256'], str(want[p]['bytes']), 'extra', '', '', '', want[p]['sha256']]) for p in tlog['appended']]
        require(cp[len(bp) - 1:-1] == expect, 'v0.2.6: the appended provenance rows are exactly one row per declared addition, in logged order, with exact content')
        require(all((R / 'evidence' / n).read_bytes() == (T / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')),
                'v0.2.6: exclusion and redaction tables unchanged')
        require(all(sha(R / a) == want[a]['sha256'] for a in want), 'v0.2.6: declared evidence files present with their hashes')
        rsc = json.loads((R / REC['evidence']['retained_source_changes']['path']).read_text())['retained_source_changes']
        bprov = {x.split('\t')[0]: x.split('\t') for x in bp[1:] if x}
        require(len({x['release_path'] for x in rsc}) == len(rsc) and all(x['release_path'] in bprov and bprov[x['release_path']][2] == x['released_sha256']
                                                                          and sha(R / x['release_path']) == x['released_sha256'] for x in rsc),
                'v0.2.6: each retained source change is a 4344c6a row, declared once, whose released bytes are unchanged')
        require(sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in tlog.get('retained_source_changes', []))
                == sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in rsc), 'v0.2.6: the transition log retained exactly the declared source changes')
        require(tlog['baseline_tables'] == {n: {'path': f'{HR}/evidence/{n}', 'sha256': sha(T / 'evidence' / n)} for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')},
                'v0.2.6: the transition started from the 4344c6a tables')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ev = REC['evidence']
    require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'transition_log', 'retained_source_changes')),
            'v0.2.6: evidence declaration, retained-change declaration and transition log bound')
    require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}, 'v0.2.6: transition log matches the current tables')
    t = subprocess.run([sys.executable, '-B', str(R / 'tools/build_evidence_transition.py'), '--self-test'], capture_output=True, text=True)
    require(t.returncode == 0 and 'SELF_TEST_PASS' in t.stdout and [l.split()[-1] for l in t.stdout.splitlines()[:-1]] == ['rejected'] * 19,
            'v0.2.6: the evidence transition tool rejects all 19 of its self-test corruptions')
    gov = [g for item in REC['governing_files'].values() for g in item]
    require(all(sha(R / g['release_path']) == g['sha256'] for g in gov if g.get('release_path')), 'v0.2.6: every released governing file matches its bound sha256')
    bound = set(REC['current_bindings'])
    require(bound == (changed | added) - {'MANIFEST.sha256', REC_PATH} and all(sha(R / p) == h for p, h in REC['current_bindings'].items()),
            'v0.2.6: every changed or added file (except the manifest and this record) bound to its bytes')
    for gen in ('build_index.py', 'build_brief.py'):
        g = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
        require(g.returncode == 0, 'v0.2.6: generated output current: ' + gen)
    for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
        require(not ((changed | added) & set(json.loads((R / 'review' / name).read_text())['files'])), 'v0.2.6: no edited path among the non-redirectable ' + name)
    print('V026_TRANSITION_PASS: the 4344c6a tree reconstructed and its checker passes; the v0.2.6 delta is exactly the declared one')


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
    """Change declared new text in rel (the declared edit is rebound too), as a maximal adversary would."""
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    e = next(e for e in d['text_edits'][rel] if old in e['new'])
    e['new'] = e['new'].replace(old, new, 1); rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    p = t / rel; s = p.read_text(); assert s.count(old) >= 1; p.write_text(s.replace(old, new, 1))


P2, P4, CM = 'claims/spec/part2_bridges.py', 'claims/spec/part4_open.py', 'claims/spec/common.py'
def m_le4_spec(t):
    _spec_edit(t, P2, 'If v_{zeta_p - 1}(chi(theta_K^MT)) < 4 for the full', 'If v_{zeta_p - 1}(chi(theta_K^MT)) <= 4 for the full'); _rebind_all(t)
def m_le4_paper(t):
    _text_rebound(t, 'paper/sections/09_reductions.tex', '\\bigr)<4,', '\\bigr)\\le4,'); _rebind_all(t)
def m_b20_excl19(t):
    _spec_edit(t, P2, 'including the supersingular primes and 19, 59 and 487, M_infinity', 'including the supersingular primes, other than 19, M_infinity'); _rebind_all(t)
def m_b20_ordinary(t):
    _spec_edit(t, P2, "'For every prime p >= 5 of good reduction for E, including", "'For every prime p >= 5 of good ordinary reduction for E, including"); _rebind_all(t)
def m_b20_p3(t):
    _spec_edit(t, P2, "'For every prime p >= 5 of good reduction for E, including", "'For every prime p >= 3 of good reduction for E, including"); _rebind_all(t)
def m_b20_bad(t):
    _spec_edit(t, P2, 'The bad primes 2243, 4547 and 5843 and the primes p <= 3 are not covered.', 'The bad prime 2243 is covered as well.'); _rebind_all(t)
def m_b20_universal_only(t):   # POSITIVE: the universal phrase alone, without listing 19, 59, 487
    _spec_edit(t, P2, "'For every prime p >= 5 of good reduction for E, including the supersingular primes and 19, 59 and 487, M_infinity(delta) = 0. '",
               "'For every good p >= 5, M_infinity(delta) = 0. '"); _rebind_all(t)
def m_no_caveat(t):
    _spec_edit(t, P2, "'by sha256 ' + V26.CLW_SHA + '; a later version could change the hypotheses of Theorem A.',", "'by sha256 ' + V26.CLW_SHA + '.',"); _rebind_all(t)
def m_no_ordinary(t):
    _spec_edit(t, P2, "'Theorem B requires squarefree N.',", "'Theorem B is not needed.',"); _rebind_all(t)
def m_label_altered(t):
    _spec_edit(t, P2, "verification={'review': V26.REVIEW, 'review_label': V26.LABEL},\n          qualifications=[V26.SENTENCE,",
               "verification={'review': V26.REVIEW, 'review_label': V26.LABEL.replace('Fable 5.1;', 'Fable 5.1,')},\n          qualifications=[V26.SENTENCE,"); _rebind_all(t)
def m_label_missing(t):
    _spec_edit(t, P2, "verification={'review': V26.REVIEW, 'review_label': V26.LABEL},\n          qualifications=['The inequality is strict.",
               "verification={'review': V26.REVIEW},\n          qualifications=['The inequality is strict."); _rebind_all(t)
def m_fin_proved(t):
    _text_rebound(t, 'paper/sections/11_remaining.tex', 'this target would give FIN.', 'this target would give FIN. This revision proves FIN.'); _rebind_all(t)
def m_bound_proved(t):
    _text_rebound(t, 'README.md', ' No applicable theorem was located in the screened sources.\n', ' A uniform upper bound has now been established.\n'); _rebind_all(t)
def m_conditional_ok(t):       # POSITIVE: a conditional implication and a stated open target stay acceptable
    _text_rebound(t, 'README.md', ' No applicable theorem was located in the screened sources.\n',
                  ' No applicable theorem was located in the screened sources. If the target is proved, FIN follows given finiteness at the primes of S.\n'); _rebind_all(t)
def m_no_method(t):
    _text_rebound(t, 'paper/sections/11_remaining.tex', 'No applicable theorem was located in the screened sources.', 'No method exists for this step.'); _rebind_all(t)
def m_remains(t):
    _text_rebound(t, 'paper/sections/11_remaining.tex', 'The current known frontier for the uniform step is the following target.',
                  'All that remains is the following target.'); _rebind_all(t)
def m_drop_governing(t):       # PART_B_DEPTH.md dropped everywhere (file, row, declaration, log, source list, spec, record), all rebound
    rel = _S + PRO + 'PART_B_DEPTH.md'
    _spec_edit(t, CM, "            E(V26.PRO + 'PART_B_DEPTH.md', 'independent review (ChatGPT Pro): Part B, sections B1-B7'),\n", '')
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
def m_nonzero_padic(t):
    _spec_edit(t, P2, "'Hence some squarefree Kato conductor n, which may depend on p, gives a mod-p unit Kurihara witness: delta_n is nonzero mod p. '",
               "'Hence some squarefree Kato conductor n, which may depend on p, gives a nonzero p-adic Kurihara witness: delta_n is nonzero. '"); _rebind_all(t)
def m_conductor(t):
    _spec_edit(t, P2, 'let K/Q be a real cyclic extension of degree p whose actual conductor m is prime to pN (m may be ',
               'let K/Q be a real cyclic extension of degree p, take any conductor m that is a multiple of its conductor and prime to pN (m may be '); _rebind_all(t)
def m_converse_spec(t):
    _spec_edit(t, P2, "'Omega^+ = 2*omega_1), then Sha(E/Q)[p^infinity] = 0.',", "'Omega^+ = 2*omega_1), if and only if Sha(E/Q)[p^infinity] = 0.',"); _rebind_all(t)
def m_converse_paper(t):
    _text_rebound(t, 'paper/sections/11_remaining.tex', 'with depth strictly below four, is another sufficient condition', 'with depth strictly below four, is an equivalent condition'); _rebind_all(t)
def m_omit_appended(t):
    p, L = _prov(t); del L[_n_old(t) + 3]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_dup_appended(t):
    p, L = _prov(t); k = _n_old(t); L[k + 5] = L[k + 4]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_history_byte(t):
    p = t / 'review/history/v0.2.5k2/README.md'; b = bytearray(p.read_bytes()); b[10] ^= 1; p.write_bytes(bytes(b))
def m_paper_edit(t):
    p = t / 'paper/sections/09_reductions.tex'; s = p.read_text(); assert 'no such value has been computed.' in s
    p.write_text(s.replace('no such value has been computed.', 'no such value has yet been computed.', 1)); _rebind_all(t)
def m_other_file_rebound(t):   # an undeclared edit to a file outside the fixed changed set, with a history copy and every binding forged
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
            ('positive_b20_universal_phrase_without_19_59_487', m_b20_universal_only, ''),
            ('positive_conditional_fin_implication_in_readme', m_conditional_ok, ''),
            ('1a_le4_in_spec_rebound', m_le4_spec, 'B.22 uses the strict inequality < 4'),
            ('1b_le4_in_paper_rebound', m_le4_paper, 'the manuscript states B.22 with the strict inequality'),
            ('2a_b20_excludes_19_rebound', m_b20_excl19, 'B.20 covers every good p >= 5 and nothing else'),
            ('2b_b20_ordinary_only_rebound', m_b20_ordinary, 'B.20 covers every good p >= 5 and nothing else'),
            ('2c_b20_reaches_p3_rebound', m_b20_p3, 'B.20 covers every good p >= 5 and nothing else'),
            ('2d_b20_claims_bad_prime_rebound', m_b20_bad, 'B.20 covers every good p >= 5 and nothing else'),
            ('3a_b20_without_clw_caveat_rebound', m_no_caveat, 'B.20 carries the pinned CLW author-revision caveat'),
            ('3b_b20_without_ordinary_coverage_rebound', m_no_ordinary, 'B.20 carries the separate ordinary-coverage explanation'),
            ('4a_review_label_altered_rebound', m_label_altered, 'B.21 carries the exact review label'),
            ('4b_review_label_missing_rebound', m_label_missing, 'B.22 carries the exact review label'),
            ('5a_fin_proved_asserted_in_paper_rebound', m_fin_proved, 'no outward text asserts that FIN'),
            ('5b_uniform_bound_asserted_in_readme_rebound', m_bound_proved, 'no outward text asserts that FIN'),
            ('6_no_method_exists_wording_rebound', m_no_method, 'no outward text claims that no method exists'),
            ('6b_all_that_remains_wording_rebound', m_remains, 'no outward text says "only/all that remains"'),
            ('7a_governing_file_dropped_rebound_all', m_drop_governing, 'B.20-B.22 cite exactly the released governing files'),
            ('7b_hash_only_binding_dropped_rebound', m_drop_hashonly, 'the 29 third-party files are bound by hash'),
            ('8_mod_p_unit_weakened_to_nonzero_p_adic_rebound', m_nonzero_padic, 'B.20 asserts a mod-p unit witness'),
            ('9_conductor_changed_untracked_rebound', m_conductor, 'B.22 is stated at the actual conductor'),
            ('10a_b22_converse_in_spec_rebound', m_converse_spec, 'B.22 is a sufficient criterion only'),
            ('10b_b22_equivalence_in_paper_rebound', m_converse_paper, '§11 states the exact open target'),
            ('a_appended_row_omitted_rebound_all', m_omit_appended, 'provenance rows and evidence/src files correspond one to one'),
            ('b_duplicate_rebinds_omitted_appended_row', m_dup_appended, 'no provenance path occurs twice'),
            ('c_historical_copy_byte_altered', m_history_byte, 'preserved 4344c6a base copies intact'),
            ('d_undeclared_paper_edit_rebound', m_paper_edit, '09_reductions.tex equals the 4344c6a file plus exactly the declared edits'),
            ('e_undeclared_edit_outside_fixed_set_rebound_all', m_other_file_rebound, 'the changed files are within the set fixed by this checker'),
            ('f_undeclared_evidence_file', m_undeclared_file, 'the file set is exactly the 4344c6a set plus the declared additions')]


def negative_controls():
    res = {}
    for name, mut, want in CONTROLS:
        tmp = Path(tempfile.mkdtemp(prefix='v026_negctl_'))
        try:
            t = tmp / 'repo'; shutil.copytree(R, t, ignore=shutil.ignore_patterns('.git'), symlinks=True)
            if mut:
                mut(t)
            r = subprocess.run([sys.executable, '-B', str(t / 'tools/verify_v026_transition.py')], capture_output=True, text=True, cwd=t)
            first = next((l for l in (r.stdout + r.stderr).splitlines() if l.startswith('FAIL')), '')
            positive = name.startswith('positive')
            ok = (r.returncode == 0 and 'V026_TRANSITION_PASS' in r.stdout) if positive else (r.returncode != 0 and want in first)
            res[name] = {'exit': r.returncode, 'as_expected': ok, 'first_fail': first}
            print(f"{name:52s} exit={r.returncode} {'OK' if ok else 'UNEXPECTED'}  {first[:120]}", flush=True)
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
