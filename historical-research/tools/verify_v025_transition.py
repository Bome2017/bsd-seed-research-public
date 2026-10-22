#!/usr/bin/env python3
"""v0.2.5 transition check: reconstruct v0.2.4 exactly, run ITS checker unchanged, then check the v0.2.5 delta.

  python3 tools/verify_v025_transition.py                      the check (prints V025_TRANSITION_PASS)
  python3 tools/verify_v025_transition.py --negative-controls  corrupt throwaway copies; every control must FAIL

1. Copy this tree to a temporary directory, restore every path in the record's `base_copies` (v0.2.4 bytes kept under
   review/history/v0.2.4/), and remove every path in `added_paths`. The reconstructed file set must EQUAL the preserved
   v0.2.4 MANIFEST (set equality, not membership), with every v0.2.4 hash.
2. Run the reconstructed tree's own tools/verify_patch_release.py (the v0.2.4 checker, byte-identical). It reconstructs
   v0.2.3 in turn and runs the v0.2.3 checker there. It must pass; nothing old is re-pointed or weakened.
3. Check that the current tree differs from v0.2.4 exactly as declared. Every comparison is an exact row, an exact list
   or a set equality with uniqueness; count plus membership is never used, because a duplicate could then stand in for
   an omitted row:
   - claims.json: the id order equals the declared order (each id once); every v0.2.4 claim equals its v0.2.4 value plus
     exactly the declared field changes; every new claim equals its declared value; no other claim changes;
   - text edits: each declared anchor occurs exactly once in the v0.2.4 file and the current file is v0.2.4 plus those
     edits; tools/extra_evidence.txt is v0.2.4 plus exactly the declared appended text;
   - evidence: whole-table provenance invariants; the v0.2.4 rows preserved byte for byte and in order; the appended
     rows exactly one per declared addition, in logged order, with exact content; exclusion and redaction tables
     unchanged; the retained source changes are v0.2.4 rows whose released bytes are unchanged;
   - grade and wording bounds (fixed in this file, from the bank scope): no banked claim may exceed its governing
     grade, change a frozen grade label, drop its mandatory qualifier, or use "only/all that remains" wording; the new
     manuscript and README text carries no internal process markers.
Standard library only; this repository is never written.
"""
import hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
REC_PATH = 'review/V025_BANK_APPLIED.json'

# ---------------------------------------------------------------- bounds fixed by the bank scope (not by the record)
NEW_IDS = ['S.3L', 'S.3F', 'S.17-47', 'B.18', 'B.16', 'B.17', 'B.19']
REVISED_IDS = ['S.3', 'S.P', 'S.FIN', 'B.8', 'B.11', 'X.14', 'X.16']
FROZEN = {'S.3': ('title', 'statement', 'kind', 'grades'), 'S.P': ('title', 'statement', 'kind', 'grades'),
          'B.11': ('title', 'statement', 'kind', 'grades')}
# kind; allowed grades; grades that must be present; phrases that must occur in the statement / in the other text;
# phrases that must not occur in the statement / anywhere in the claim
BOUNDS = {
    'S.3': dict(kind='THEOREM', allowed={'PROVED_COMPUTER_ASSISTED', 'IMPORTED_PUBLISHED', 'PROVED_WRITTEN', 'LEAN_CHECKED'},
                required={'PROVED_COMPUTER_ASSISTED', 'IMPORTED_PUBLISHED', 'PROVED_WRITTEN', 'LEAN_CHECKED'},
                must_other=['MS-13.4.1(ii)', 'MS-B1', 'MS-R3', 'MS-R24', 'OPEN: an upper bound #Sha[3^infinity] <= 9',
                            'still rests on Skinner Theorem A as printed', 'cross-model, same family, not cross-family audited'],
                never_any=['not an active cleanup target']),
    'S.3L': dict(kind='THEOREM', allowed={'EXACT_COMPUTATION'}, required={'EXACT_COMPUTATION'}, must_stmt=['#Sha(E/Q)[3] >= 9'],
                 never_stmt=['Sha[3^infinity]', 'finite', 'GRH'], must_other=['not cross-family', 'A lower bound only'],
                 never_imports=['Skinner', 'GRH', 'Kato']),
    'S.3F': dict(kind='THEOREM', allowed={'IMPORTED_PUBLISHED', 'PROVED_COMPUTER_ASSISTED', 'PROVED_WRITTEN'}, required={'IMPORTED_PUBLISHED'},
                 must_stmt=['Sha(E/Q)[3^infinity] is finite', 'Theorem 18.4'], never_stmt=['(Z/3)^2', '#Sha', 'isomorphic', '<= 9'],
                 must_other=['no bound on #Sha[3^infinity] follows', 'not cross-family'], never_imports=['Skinner', 'Jones']),
    'S.17-47': dict(kind='THEOREM', allowed={'PROVED_COMPUTER_ASSISTED', 'PROVED_WRITTEN', 'IMPORTED_PREPRINT'}, required={'IMPORTED_PREPRINT'},
                    must_other=['MODEL_SAME_FAMILY', 'It is not a cross-family audit', 'No independent human review',
                                'not a proof that such a scalar exists', 'do not prove FIN', 'six pre-result forecasts'],
                    never_any=['independently audited']),
    'S.FIN': dict(kind='THEOREM', allowed={'PROVED_WRITTEN'}, required={'PROVED_WRITTEN'}, must_stmt=['If Sha(E/Q) is finite', '25,281'],
                  must_other=['Conditional on FIN']),
    'B.8': dict(kind='OPEN', allowed={'PROVED_WRITTEN'}, required={'PROVED_WRITTEN'}, must_stmt=['No witness has been evaluated'],
                never_stmt=['only route', 'first concrete route']),
    'B.11': dict(kind='CONDITIONAL', allowed={'PROVED_WRITTEN', 'LEAN_CHECKED'}, required={'PROVED_WRITTEN', 'LEAN_CHECKED'},
                 must_other=['Related, not equivalent', 'conjecture grade', 'power of 2', 'says nothing about q']),
    'X.14': dict(kind='OBSTRUCTION', stop='PROCEDURAL', allowed={'PROVED_WRITTEN'}, required={'PROVED_WRITTEN'},
                 must_stmt=['stopped again', 'does not move it']),
    'X.16': dict(kind='OBSTRUCTION', stop='UNAFFORDABLE', allowed={'PROVED_WRITTEN'}, required={'PROVED_WRITTEN'},
                 must_stmt=['HOLD'], must_other=['not intrinsic computational lower bounds']),
    'B.16': dict(kind='THEOREM', allowed={'PROVED_WRITTEN', 'IMPORTED_PUBLISHED'}, required={'PROVED_WRITTEN'},
                 never_stmt=['Sha('], must_other=['proves no statement about Sha', 'G1 is ']),
    'B.17': dict(kind='THEOREM', allowed={'PROVED_WRITTEN', 'IMPORTED_PREPRINT'}, required={'IMPORTED_PREPRINT'},
                 must_other=['no unconditional prime-independent scalar', 'It does not apply at 19']),
    'B.18': dict(kind='CONDITIONAL', allowed={'PROVED_WRITTEN', 'IMPORTED_PREPRINT'}, required={'IMPORTED_PREPRINT'},
                 must_other=['no coefficient has been evaluated', 'no cross-family label is claimed']),
    'B.19': dict(kind='THEOREM', allowed={'PROVED_WRITTEN', 'IMPORTED_PREPRINT'}, required={'PROVED_WRITTEN'},
                 must_stmt=['B* = {2, 3, 19, 59, 487, 2243, 4547, 5843}'],
                 must_other=['nothing across primes', 'nothing about w != 0', 'nothing about the value 288']),
}
NEVER_ANY_CLAIM = ['only remains', 'all that remains', 'only what remains']
PROCESS_MARKERS = ['Fable', 'Opus', ' lane', 'Lane ', 'RUN_NOW', 'coordinator', 'addendum', 'DRAFT', 'draft banner', 'session',
                   'only remains', 'all that remains', 'only what remains']


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
    """Untracked build and cache files that .gitignore excludes, and the manifest itself (it does not list itself)."""
    name = rel.rsplit('/', 1)[-1]
    return (rel == 'MANIFEST.sha256' or '__pycache__' in rel.split('/') or name.endswith('.pyc') or name == '.DS_Store'
            or (rel.startswith('paper/') and rel.count('/') == 1
                and name.endswith(('.aux', '.log', '.fls', '.fdb_latexmk', '.out', '.toc', '.blg', '.synctex.gz'))))


def text_of(c, fields):
    return ' '.join(json.dumps(c.get(f), ensure_ascii=False) for f in fields)


def check_bounds(ccl, bcl):
    for i, b in BOUNDS.items():
        c = ccl[i]
        stmt = c['statement']
        other = text_of(c, ('qualifications', 'verification', 'scope', 'imports', 'post_master', 'title'))
        ok = c['kind'] == b['kind'] and set(c['grades']) <= b['allowed'] and b['required'] <= set(c['grades'])
        ok &= len(c['grades']) == len(set(c['grades'])) and c.get('stop_kind', '') == b.get('stop', c.get('stop_kind', ''))
        ok &= all(s in stmt for s in b.get('must_stmt', [])) and not any(s in stmt for s in b.get('never_stmt', []))
        ok &= all(s in other for s in b.get('must_other', []))
        ok &= not any(s in stmt + other for s in b.get('never_any', []))
        ok &= not any(s in json.dumps(c['imports']) for s in b.get('never_imports', []))
        for f in FROZEN.get(i, ()):
            ok &= c[f] == bcl[i][f]
        require(ok, f'v0.2.5: {i} within its grade and wording bound (kind, grades, mandatory qualifiers, frozen fields)')
    bad = [c['id'] for c in ccl.values() if any(s in json.dumps(c, ensure_ascii=False) for s in NEVER_ANY_CLAIM)
           or c['verification'].get('review', '').startswith('HUMAN')]
    require(not bad, 'v0.2.5: no claim says "only/all that remains" or claims human review')


def main():
    REC = json.loads((R / REC_PATH).read_text())
    HR = REC['history_root']
    bc, added = REC['base_copies'], REC['added_paths']
    require(len(added) == len(set(added)), 'v0.2.5: each added path is declared once')
    added = set(added)
    changed = set(bc)
    v024 = manifest_rows(R / REC['v024_manifest']['path'])

    # ---- 0. the record's bindings of the preserved copies, and the file set ----
    require(all(x['path'] == f'{HR}/{p}' and sha(R / x['path']) == x['sha256'] for p, x in bc.items()),
            'v0.2.5: preserved v0.2.4 base copies intact')
    require(sha(R / REC['v024_manifest']['path']) == REC['v024_manifest']['sha256'], 'v0.2.5: preserved v0.2.4 manifest bound')
    require(not (added & set(v024)) and changed - {'MANIFEST.sha256'} <= set(v024),
            'v0.2.5: added paths are new; changed paths existed in v0.2.4')
    cur = manifest_rows(R / 'MANIFEST.sha256')
    require(set(cur) == (set(v024) | added) - {'MANIFEST.sha256'}, 'v0.2.5: the file set is exactly v0.2.4 plus the declared additions')

    # ---- 0b. whole-table provenance invariants (independent of every rebindable hash) ----
    cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    cols = cp[0].split('\t')
    prov = [dict(zip(cols, x.split('\t'))) for x in cp[1:] if x]
    rl = (R / 'evidence/REDACTIONS.tsv').read_text().split('\n')
    red = {r['release_path']: r for r in (dict(zip(rl[0].split('\t'), x.split('\t'))) for x in rl[1:] if x)}
    ppaths = [r['release_path'] for r in prov]
    srcfiles = {p.relative_to(R).as_posix() for p in (R / 'evidence/src').rglob('*') if p.is_file() or p.is_symlink()}
    require(len(ppaths) == len(set(ppaths)), 'v0.2.5: no provenance path occurs twice (whole table)')
    require(set(ppaths) == srcfiles, 'v0.2.5: provenance rows and evidence/src files correspond one to one (whole table)')
    require(all(sha(R / r['release_path']) == r['sha256'] for r in prov), 'v0.2.5: every provenance row matches its file hash (whole table)')
    require(all((r['release_path'] in red and red[r['release_path']]['released_sha256'] == r['sha256']
                 and red[r['release_path']]['original_sha256'] == r['original_sha256'])
                or (r['release_path'] not in red and r['bytes'] == str((R / r['release_path']).stat().st_size)) for r in prov)
            and set(red) <= set(ppaths), 'v0.2.5: sizes agree with the files, except the declared redactions (whole table)')

    tmp = Path(tempfile.mkdtemp(prefix='v024_reconstruct_'))
    try:
        # ---- 1. reconstruct v0.2.4 ----
        T = tmp / 'repo'
        shutil.copytree(R, T, ignore=shutil.ignore_patterns('.git'), symlinks=True)
        for p, x in bc.items():
            (T / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(R / x['path'], T / p)
        for p in added:
            (T / p).unlink()
        tfiles = {q.relative_to(T).as_posix() for q in T.rglob('*') if q.is_file() or q.is_symlink()}
        tfiles = {q for q in tfiles if not ignored(q)}
        require(tfiles == set(v024), 'v0.2.5: the reconstructed file set equals the v0.2.4 manifest (set equality)')
        require(all(sha(T / q) == h for q, h in v024.items()), 'v0.2.5: every reconstructed file has its v0.2.4 hash')
        # ---- 2. the v0.2.4 checker, unchanged, on the reconstruction ----
        require(sha(T / 'tools/verify_patch_release.py') == REC['v024_checker_sha256'], 'v0.2.5: reconstructed checker is the v0.2.4 checker, byte-identical')
        r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_patch_release.py')], capture_output=True, text=True, cwd=T)
        old_ok = r.returncode == 0 and 'V024_TRANSITION_PASS' in r.stdout and 'PATCH_RECHECK_PASS' in r.stdout
        if not old_ok:
            print(r.stdout[-1500:] + r.stderr[-1500:])
        require(old_ok, 'v0.2.5: the v0.2.4 checker passes on the reconstructed v0.2.4 tree (it reconstructs v0.2.3 and runs every earlier check)')
        # ---- 3. the v0.2.5 delta against the v0.2.4 view ----
        bdoc = json.loads((T / 'claims/claims.json').read_text()); cdoc = json.loads((R / 'claims/claims.json').read_text())
        bcl = {c['id']: c for c in bdoc['claims']}; ccl = {c['id']: c for c in cdoc['claims']}
        cids = [c['id'] for c in cdoc['claims']]
        order = REC['claim_order']
        require(len(cids) == len(set(cids)) and cids == order and len(order) == len(set(order)), 'v0.2.5: the claim ids are exactly the declared order, each once')
        require(set(order) == set(bcl) | set(NEW_IDS) and set(REC['new_claims']) == set(NEW_IDS) and not (set(NEW_IDS) & set(bcl)),
                'v0.2.5: the claims are exactly the v0.2.4 claims plus the declared new claims (set equality)')
        require([i for i in cids if i in bcl] == list(bcl), 'v0.2.5: the v0.2.4 claims keep their relative order')
        require({k: v for k, v in bdoc.items() if k != 'claims'} == {k: v for k, v in cdoc.items() if k != 'claims'}, 'v0.2.5: claims.json header unchanged')
        delta = REC['claim_delta']
        require(set(delta) == set(REVISED_IDS), 'v0.2.5: the revised claims are exactly the scoped revisions (' + ', '.join(REVISED_IDS) + ')')
        ok = True
        for i in bcl:
            if i not in delta:
                ok &= ccl[i] == bcl[i]
                continue
            exp = dict(bcl[i])
            for f, x in delta[i].items():
                ok &= bcl[i].get(f) == x['before']
                exp[f] = x['after']
            ok &= ccl[i] == exp
        require(ok, 'v0.2.5: every v0.2.4 claim equals v0.2.4 plus exactly the declared field changes')
        require(all(ccl[i] == REC['new_claims'][i] for i in NEW_IDS), 'v0.2.5: every new claim equals its declared value exactly')
        check_bounds(ccl, bcl)
        for p, edits in REC['text_edits'].items():
            s = (T / p).read_text()
            for e in edits:
                require(s.count(e['old']) == 1, f'v0.2.5: edit anchor occurs exactly once in v0.2.4 {p}')
                require(all(e['new'].count(m) <= e['old'].count(m) for m in PROCESS_MARKERS) or not (p.startswith('paper/') or p == 'README.md'),
                        f'v0.2.5: no internal process marker or "only/all that remains" wording added to {p}')
                s = s.replace(e['old'], e['new'])
            require((R / p).read_text() == s, f'v0.2.5: {p} equals v0.2.4 plus exactly the declared edits')
        ex_old, ex_new = (T / 'tools/extra_evidence.txt').read_text(), (R / 'tools/extra_evidence.txt').read_text()
        require(ex_new == ex_old + REC['extra_evidence_append'], 'v0.2.5: tools/extra_evidence.txt is v0.2.4 plus exactly the declared appended text')
        # evidence rows
        bp = (T / 'evidence/PROVENANCE.tsv').read_text().split('\n')
        require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'v0.2.5: every v0.2.4 provenance row preserved byte for byte, in order')
        decl = json.loads((R / REC['evidence']['declared']['path']).read_text())
        tlog = json.loads((R / REC['evidence']['transition_log']['path']).read_text())
        dpaths = [a['release_path'] for a in decl['additions']]
        want = {a['release_path']: a for a in decl['additions']}
        appended_lines = [l.split('\n')[0] for l in REC['extra_evidence_append'].splitlines() if l and not l.startswith('#')]
        require(len(dpaths) == len(set(dpaths)) and len(tlog['appended']) == len(set(tlog['appended'])) and set(tlog['appended']) == set(dpaths)
                and len(appended_lines) == len(set(appended_lines)) and set(appended_lines) == {a['original_path'] for a in decl['additions']},
                'v0.2.5: the declaration, the logged append list and the appended source list name the same files, each exactly once')
        require(all(a['disposition'] == 'admitted_unmasked' for a in decl['additions']), 'v0.2.5: every declared addition is admitted unmasked')
        expect = ['\t'.join([p, want[p]['original_path'], want[p]['sha256'], str(want[p]['bytes']), 'extra', '', '', '', want[p]['sha256']])
                  for p in tlog['appended']]
        require(cp[len(bp) - 1:-1] == expect, 'v0.2.5: the appended provenance rows are exactly one row per declared addition, in logged order, with exact content')
        require({p for p in added if p.startswith('evidence/')} == set(dpaths), 'v0.2.5: the added evidence files are exactly the declared additions')
        require(all((R / 'evidence' / n).read_bytes() == (T / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')),
                'v0.2.5: exclusion and redaction tables unchanged')
        require(all(sha(R / a) == want[a]['sha256'] for a in want), 'v0.2.5: declared evidence files present with their hashes')
        # retained source changes: v0.2.4 rows whose released bytes stay exactly the v0.2.4 bytes
        rsc = json.loads((R / REC['evidence']['retained_source_changes']['path']).read_text())['retained_source_changes']
        bprov = {x.split('\t')[0]: x.split('\t') for x in bp[1:] if x}
        rpaths = [x['release_path'] for x in rsc]
        require(len(rpaths) == len(set(rpaths)) and all(x['release_path'] in bprov and bprov[x['release_path']][2] == x['released_sha256']
                                                         and sha(R / x['release_path']) == x['released_sha256'] and x['live_sha256'] != x['released_sha256'] for x in rsc),
                'v0.2.5: each retained source change is a v0.2.4 row, declared once, whose released bytes are unchanged')
        require(sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in tlog.get('retained_source_changes', []))
                == sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in rsc),
                'v0.2.5: the transition log retained exactly the declared source changes')
        live = [x for x in rsc if Path(x['original_path']).is_file()]
        print(f"INFO: retained source changes whose source exists on this host: {len(live)}; current source hash equals the declared one: "
              f"{sum(sha(x['original_path']) == x['live_sha256'] for x in live)}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    ev = REC['evidence']
    require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'transition_log', 'retained_source_changes')),
            'v0.2.5: evidence declaration, retained-change declaration and transition log bound')
    require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')},
            'v0.2.5: transition log matches the current tables')
    t = subprocess.run([sys.executable, '-B', str(R / 'tools/build_evidence_transition.py'), '--self-test'], capture_output=True, text=True)
    require(t.returncode == 0 and 'SELF_TEST_PASS' in t.stdout and [l.split()[-1] for l in t.stdout.splitlines()[:-1]] == ['rejected'] * 19,
            'v0.2.5: the evidence transition tool rejects all 19 of its self-test corruptions')
    gov = [g for item in REC['governing_files'].values() for g in item]
    require(all(sha(R / g['release_path']) == g['sha256'] for g in gov if g.get('release_path')),
            'v0.2.5: every released governing file matches its bound sha256')
    bound = set(REC['current_bindings'])
    require(bound == (changed | added) - {'MANIFEST.sha256', REC_PATH} and all(sha(R / p) == h for p, h in REC['current_bindings'].items()),
            'v0.2.5: every changed or added file (except the manifest and this record) bound to its v0.2.5 bytes')
    for gen in ('build_index.py', 'build_brief.py'):
        g = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
        require(g.returncode == 0, 'v0.2.5: generated output current: ' + gen)
    for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
        require(not ((changed | added) & set(json.loads((R / 'review' / name).read_text())['files'])), 'v0.2.5: no edited path among the non-redirectable ' + name)
    print('V025_TRANSITION_PASS: v0.2.4 reconstructed and its checker passes; the v0.2.5 delta is exactly the declared one')


# ---------------------------------------------------------------- negative controls (throwaway copies only)
def _rebind_all(t):
    """A maximal rebinding adversary: recompute every hash the checker could be pointed at (the transition log's tables,
    the record's evidence and current bindings, governing-file hashes, and every MANIFEST row)."""
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
    d['claim_order'] = [c['id'] for c in json.loads((t / 'claims/claims.json').read_text())['claims']]
    cl = {c['id']: c for c in json.loads((t / 'claims/claims.json').read_text())['claims']}
    d['new_claims'] = {i: cl[i] for i in d['new_claims'] if i in cl}
    base = {c['id']: c for c in json.loads((t / d['history_root'] / 'claims/claims.json').read_text())['claims']}
    d['claim_delta'] = {i: {f: {'before': base[i].get(f), 'after': cl[i][f]} for f in cl[i] if cl[i][f] != base[i].get(f)}
                        for i in d['claim_delta']}
    rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    m = t / 'MANIFEST.sha256'
    m.write_text(''.join(f"{sha(t / l.split('  ', 1)[1])}  {l.split('  ', 1)[1]}\n" for l in m.read_text().splitlines() if (t / l.split('  ', 1)[1]).exists()))


def _prov(t):
    p = t / 'evidence/PROVENANCE.tsv'; return p, p.read_text().split('\n')


def _n_old(t):
    d = json.loads((t / REC_PATH).read_text())
    return len((t / d['history_root'] / 'evidence/PROVENANCE.tsv').read_text().split('\n')) - 1   # index of the first appended row


def _spec_edit(t, part, old, new):
    p = t / 'claims/spec' / part; s = p.read_text(); assert s.count(old) == 1, old[:60]; p.write_text(s.replace(old, new))
    for gen in ('build_index.py', 'build_brief.py'):
        subprocess.run([sys.executable, '-B', str(t / 'tools' / gen)], capture_output=True, check=True)


def m_omit_appended(t):     # an appended row omitted (its file stays), every hash rebound
    p, L = _prov(t); del L[_n_old(t) + 3]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_omit_old(t):          # a v0.2.4 row omitted, every hash rebound
    p, L = _prov(t); del L[200]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_dup_appended(t):      # a duplicate rebinds an omitted appended row (row count unchanged)
    p, L = _prov(t); k = _n_old(t); L[k + 5] = L[k + 4]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_dup_old(t):           # the same in the v0.2.4 region
    p, L = _prov(t); L[100] = L[99]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_history_byte(t):      # an altered historical byte in a preserved v0.2.4 copy
    p = t / 'review/history/v0.2.4/README.md'; b = bytearray(p.read_bytes()); b[10] ^= 1; p.write_bytes(bytes(b))
def m_old_evidence_byte(t):  # an altered historical byte in a retained master copy, its provenance row rebound
    rel = 'evidence/src/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md'
    f = t / rel; b = bytearray(f.read_bytes()); b[100] ^= 1; f.write_bytes(bytes(b))
    p, L = _prov(t); i = next(k for k, x in enumerate(L) if x.startswith(rel + '\t')); c = L[i].split('\t'); c[2] = sha(f); L[i] = '\t'.join(c)
    p.write_text('\n'.join(L)); _rebind_all(t)
def m_meta_appended(t):     # hashes intact, metadata of one appended row changed
    p, L = _prov(t); k = _n_old(t) + 2; c = L[k].split('\t'); c[4] = 'master_bound'; L[k] = '\t'.join(c); p.write_text('\n'.join(L)); _rebind_all(t)
def m_claim_exceeds_S3F(t):  # finiteness claim rewritten to assert the order: text exceeds its bound
    _spec_edit(t, 'part1_core.py', "'Sha(E/Q)[3^infinity] is finite. Kato 2004", "'Sha(E/Q)[3^infinity] is isomorphic to (Z/3)^2 and finite. Kato 2004"); _rebind_all(t)
def m_claim_crossfamily(t):  # the same-family audit relabelled as cross-family
    _spec_edit(t, 'part1_core.py', 'MODEL_SAME_FAMILY) found', 'MODEL_CROSS_FAMILY) found'); _rebind_all(t)
def m_claim_bh_theorem(t):   # the conditional bad-prime criterion upgraded to an unconditional theorem
    _spec_edit(t, 'part2_bridges.py', "'CONDITIONAL', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='written corollary of a preprint theorem'",
               "'THEOREM', ['PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='written corollary of a preprint theorem'"); _rebind_all(t)
def m_claim_preprint_published(t):  # a preprint import relabelled as published
    _spec_edit(t, 'part1_core.py', "'THEOREM', ['PROVED_COMPUTER_ASSISTED', 'PROVED_WRITTEN', 'IMPORTED_PREPRINT'], origin='new computations;",
               "'THEOREM', ['PROVED_COMPUTER_ASSISTED', 'PROVED_WRITTEN', 'IMPORTED_PUBLISHED'], origin='new computations;"); _rebind_all(t)
def m_S3_grade_label(t):     # S.3's grade label changed (the scope freezes it)
    _spec_edit(t, 'part1_core.py', "'THEOREM', ['PROVED_COMPUTER_ASSISTED', 'IMPORTED_PUBLISHED', 'PROVED_WRITTEN', 'LEAN_CHECKED'],\n          origin='new computation; application of published theorems', section='4',\n          evidence=[{'path': 'evidence/src/BSD_SEED_2243_12_P3_RIGOROUS_RUN",
               "'THEOREM', ['PROVED_COMPUTER_ASSISTED', 'PROVED_WRITTEN', 'LEAN_CHECKED'],\n          origin='new computation; application of published theorems', section='4',\n          evidence=[{'path': 'evidence/src/BSD_SEED_2243_12_P3_RIGOROUS_RUN"); _rebind_all(t)
def m_frontier_wording(t):   # "all that remains" added to a revised claim
    _spec_edit(t, 'part1_core.py', "'Conditional on FIN: it neither proves FIN", "'This is all that remains. Conditional on FIN: it neither proves FIN"); _rebind_all(t)
def m_paper_edit(t):         # an undeclared manuscript edit
    p = t / 'paper/sections/11_remaining.tex'; s = p.read_text(); assert 'current known frontier of the sources read' in s
    p.write_text(s.replace('current known frontier of the sources read', 'current known frontier', 1)); _rebind_all(t)
def m_readme_marker(t):      # a process marker added to the README through a rebound declared edit
    rp = t / REC_PATH; d = json.loads(rp.read_text()); e = d['text_edits']['README.md'][0]
    e['new'] = e['new'].replace('built on version 0.2.2', 'built on version 0.2.2 by the Opus lane'); rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    p = t / 'README.md'; s = p.read_text(); p.write_text(s.replace('built on version 0.2.2', 'built on version 0.2.2 by the Opus lane', 1)); _rebind_all(t)
def m_undeclared_file(t):    # an undeclared evidence file with a manifest row
    (t / 'evidence/src/UNDECLARED.txt').write_text('x\n')
    m = t / 'MANIFEST.sha256'; m.write_text(m.read_text() + hashlib.sha256(b'x\n').hexdigest() + '  evidence/src/UNDECLARED.txt\n')


CONTROLS = [('positive_control_unmodified', None, ''),
            ('a_appended_row_omitted_rebound_all', m_omit_appended, 'provenance rows and evidence/src files correspond one to one'),
            ('b_v024_row_omitted_rebound_all', m_omit_old, 'provenance rows and evidence/src files correspond one to one'),
            ('c_duplicate_rebinds_omitted_appended_row', m_dup_appended, 'no provenance path occurs twice'),
            ('d_duplicate_rebinds_omitted_v024_row', m_dup_old, 'no provenance path occurs twice'),
            ('e_historical_copy_byte_altered', m_history_byte, 'preserved v0.2.4 base copies intact'),
            ('f_retained_master_byte_altered_rebound', m_old_evidence_byte, 'every reconstructed file has its v0.2.4 hash'),
            ('g_appended_row_metadata_changed_rebound', m_meta_appended, 'appended provenance rows are exactly'),
            ('h_claim_text_exceeds_grade_S3F', m_claim_exceeds_S3F, 'S.3F within its grade and wording bound'),
            ('i_same_family_audit_relabelled_cross_family', m_claim_crossfamily, 'S.17-47 within its grade and wording bound'),
            ('j_conditional_criterion_upgraded_to_theorem', m_claim_bh_theorem, 'B.18 within its grade and wording bound'),
            ('k_preprint_import_relabelled_published', m_claim_preprint_published, 'S.17-47 within its grade and wording bound'),
            ('l_S3_grade_label_changed', m_S3_grade_label, 'S.3 within its grade and wording bound'),
            ('m_all_that_remains_wording', m_frontier_wording, 'no claim says "only/all that remains"'),
            ('n_undeclared_paper_edit_rebound', m_paper_edit, '11_remaining.tex equals v0.2.4 plus exactly the declared edits'),
            ('o_process_marker_in_readme_rebound', m_readme_marker, 'no internal process marker'),
            ('p_undeclared_evidence_file', m_undeclared_file, 'the file set is exactly v0.2.4 plus the declared additions')]


def negative_controls():
    res = {}
    for name, mut, want in CONTROLS:
        tmp = Path(tempfile.mkdtemp(prefix='v025_negctl_'))
        try:
            t = tmp / 'repo'; shutil.copytree(R, t, ignore=shutil.ignore_patterns('.git'), symlinks=True)
            if mut:
                mut(t)
            r = subprocess.run([sys.executable, '-B', str(t / 'tools/verify_v025_transition.py')], capture_output=True, text=True, cwd=t)
            first = next((l for l in (r.stdout + r.stderr).splitlines() if l.startswith('FAIL')), '')
            ok = (r.returncode == 0 and 'V025_TRANSITION_PASS' in r.stdout) if not mut else (r.returncode != 0 and want in first)
            res[name] = {'exit': r.returncode, 'as_expected': ok, 'first_fail': first}
            print(f"{name:48s} exit={r.returncode} {'OK' if ok else 'UNEXPECTED'}  {first[:110]}", flush=True)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    good = all(x['as_expected'] for x in res.values())
    print(json.dumps(res, indent=1))
    print('NEGATIVE_CONTROLS_PASS' if good else 'NEGATIVE_CONTROLS_FAIL')
    return good


if __name__ == '__main__':
    if '--negative-controls' in sys.argv:
        raise SystemExit(0 if negative_controls() else 1)
    main()
