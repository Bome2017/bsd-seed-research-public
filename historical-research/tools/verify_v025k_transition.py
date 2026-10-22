#!/usr/bin/env python3
"""Route-K transition check (a follow-on commit to v0.2.5): reconstruct the v0.2.5 bank tree exactly, run ITS checker
unchanged, then check the route-K delta.

  python3 tools/verify_v025k_transition.py                        the check (prints V025K_TRANSITION_PASS)
  python3 tools/verify_v025k_transition.py --with-v025-controls   also run the v0.2.5 negative controls in the reconstruction
  python3 tools/verify_v025k_transition.py --negative-controls    corrupt throwaway copies; every control must FAIL

1. Copy this tree, restore every path in the record's `base_copies` (the bank bytes kept under review/history/v0.2.5/),
   remove every path in `added_paths`. The reconstructed file set must EQUAL the preserved v0.2.5 manifest.
2. Run the reconstructed tree's tools/verify_patch_release.py (the v0.2.5 checker, byte-identical). It reconstructs
   v0.2.4 in turn, and so on back to v0.2.3. It must pass.
3. Check the route-K delta by exact rows, exact lists and set equality with uniqueness (never count plus membership):
   claim order, field changes, the new claim, text edits, appended evidence rows, retained rows, bound bytes. Then:
   - route K's record is complete: S.3K cites, and the release contains, the derivation D1-D8, the errata, the
     cross-model reading and BOTH second readers' returns and T-files;
   - bounds fixed here, not in the record: S.3K carries its exact grade label; S.3's statement and grades are unchanged
     and its primary support is route K with Skinner as the second route; S.17-47 cites Ota's print;
   - the citation scan: every line of every manifest file that cites Kato 12.5(4) must say that it is printed for V,
     except in the declared allowlist of historical records (E1_ALLOW below);
   - no internal process marker is added to the manuscript or README (the exact grade label is exempt).
Standard library only; this repository is never written.
"""
import hashlib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
REC_PATH = 'review/V025K_ROUTEK_APPLIED.json'
LABEL = ('written derivation; three model readers (one cross-model: Fable 5.1; two independent fresh sessions: Opus 5.5); '
         'all Anthropic models, not cross-family; no human review')
NEW_IDS = ['S.3K']
REVISED_IDS = ['S.3', 'S.17-47']
_S = 'evidence/src/'
_R25, _FCK = _S + 'BSD_P3_MS_R24_COLEMAN_RETURN_OPUS_2026-09-29/', _S + 'BSD_P3_MS_R24_COLEMAN_CHECK_FABLE_2026-09-29/'
_SRA, _SRB = _S + 'BSD_R25_SECOND_READER_RETURN_OPUS_2026-09-29/', _S + 'BSD_R25_SECOND_READER_RETURN_OPUS_B_2026-09-29/'
ROUTEK_REQUIRED = ([_R25 + d for d in ('D1_CONSTRUCTION.md', 'D2_INTEGRALITY.md', 'D3_KILL_TESTS_A_B.md', 'D4_KILL_TEST_C.md',
                                       'D5_MS_R24.md', 'D6_O2_POITOU_TATE.md', 'D7_O4_NORMALISATION.md', 'D8_ASSEMBLY.md', 'RETURN.md')]
                   + [_S + 'BSD_SEED_V025_BANK_ROUTEK_TASK_2026-09-29/inputs/R25_ERRATA_2026-09-29.md', _FCK + 'CHECK.md',
                      _SRA + 'RETURN.md', _SRB + 'RETURN.md']
                   + [_SRA + t for t in ('T1_D5_STEP2_3_INTERPOLATION.md', 'T2_D5_STEP1_COLEMAN_ISO.md', 'T3_D6_O2.md',
                                         'T4_D8_ASSEMBLY_JONES.md', 'T5_D1_D2_BY_HAND.md')]
                   + [_SRB + t for t in ('T1_D5_STEPS2-3_INTERPOLATION.md', 'T2_D5_STEP1_COL_ISO.md', 'T3_D6_O2.md',
                                         'T4_D8_ASSEMBLY_JONES.md', 'T5_D1_D2_BY_HAND.md')])
E1_ALLOW_FILES = {'review/V025_BANK_APPLIED.json', REC_PATH, 'tools/verify_v025k_transition.py'}
E1_ALLOW_PREFIXES = ('review/history/', 'evidence/src/')
E1_PATTERN = re.compile(r'12\.5 ?\(4\)')
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
    name = rel.rsplit('/', 1)[-1]
    return (rel == 'MANIFEST.sha256' or '__pycache__' in rel.split('/') or name.endswith('.pyc') or name == '.DS_Store'
            or (rel.startswith('paper/') and rel.count('/') == 1
                and name.endswith(('.aux', '.log', '.fls', '.fdb_latexmk', '.out', '.toc', '.blg', '.synctex.gz'))))


def e1_offenders(root, paths):
    bad = []
    for rel in sorted(paths):
        if rel in E1_ALLOW_FILES or rel.startswith(E1_ALLOW_PREFIXES):
            continue
        try:
            text = (root / rel).read_text()
        except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if E1_PATTERN.search(line) and 'printed for V' not in line:
                bad.append(f'{rel}:{n}')
    return bad


def check_claims(ccl, bcl):
    k = ccl['S.3K']
    ev = {e['path'] for e in k['evidence']}
    require(set(ROUTEK_REQUIRED) <= ev and all((R / p).is_file() for p in ROUTEK_REQUIRED),
            'v0.2.5K: S.3K cites, and the release contains, every required route-K record (D1-D8, errata, the three readers)')
    stmt, other = k['statement'], json.dumps([k['imports'], k['qualifications'], k['verification'], k['normalization']], ensure_ascii=False)
    ok = (k['kind'] == 'THEOREM' and set(k['grades']) <= {'PROVED_WRITTEN', 'IMPORTED_PUBLISHED', 'PROVED_COMPUTER_ASSISTED'}
          and 'PROVED_WRITTEN' in k['grades'] and k['verification'].get('grade_label') == LABEL and k['qualifications'][0] == 'Grade: ' + LABEL + '.'
          and '#Sha(E/Q)[3^infinity] <= 9' in stmt and 'no Skinner, Skinner-Urban or GRH' in stmt and '13.4(3) via 13.14' in stmt
          and '13.4(3) via 13.14' in other and 'gamma-normalized det<,>_gamma' in other and 'only <= 81' in other
          and 'not cross-family' in k['verification'].get('review', '') and 'no human review' in k['verification'].get('review', ''))
    require(ok, 'v0.2.5K: S.3K within its bound (exact grade label, statement, 13.4(3) via 13.14, regulator normalization)')
    s3, b3 = ccl['S.3'], bcl['S.3']
    ok = all(s3[f] == b3[f] for f in ('title', 'statement', 'kind', 'grades')) and 'S.3K' in s3['depends_on']
    ok &= s3['verification'].get('primary_support') == 'route K (S.3K): ' + LABEL
    ok &= all(x in s3['verification'].get('second_route', '') for x in ('Skinner 2016 Theorem A', 'MS-13.4.1(ii)', 'MS-B1'))
    ok &= 'route K is the primary support' in json.dumps(s3['qualifications'])
    require(ok, "v0.2.5K: S.3's statement and grades unchanged; primary support route K; Skinner the second route with MS-13.4.1(ii) and MS-B1")
    q = json.dumps(ccl['S.17-47'], ensure_ascii=False)
    ok = ('Amer. J. Math. 140 (2018) 495-542' in json.dumps(ccl['S.17-47']['qualifications']) and 'not re-checked against the print' in q
          and ccl['S.17-47']['grades'] == bcl['S.17-47']['grades'] and 'lane 2' not in q)
    require(ok, "v0.2.5K: S.17-47 cites Ota's print, keeps its grades and carries no internal marker")
    bad = [c['id'] for c in ccl.values() if any(s in json.dumps(c, ensure_ascii=False) for s in ('only remains', 'all that remains', 'only what remains'))
           or c['verification'].get('review', '').startswith('HUMAN')]
    require(not bad, 'v0.2.5K: no claim says "only/all that remains" or claims human review')


def main():
    REC = json.loads((R / REC_PATH).read_text())
    HR = REC['history_root']
    bc, added = REC['base_copies'], REC['added_paths']
    require(len(added) == len(set(added)), 'v0.2.5K: each added path is declared once')
    added = set(added); changed = set(bc)
    require('review/V025_BANK_APPLIED.json' not in changed | added, 'v0.2.5K: the v0.2.5 record of declared edits is unchanged')
    v025 = manifest_rows(R / REC['v025_manifest']['path'])
    require(all(x['path'] == f'{HR}/{p}' and sha(R / x['path']) == x['sha256'] for p, x in bc.items()), 'v0.2.5K: preserved v0.2.5 base copies intact')
    require(sha(R / REC['v025_manifest']['path']) == REC['v025_manifest']['sha256'], 'v0.2.5K: preserved v0.2.5 manifest bound')
    require(not (added & set(v025)) and changed - {'MANIFEST.sha256'} <= set(v025), 'v0.2.5K: added paths are new; changed paths existed in v0.2.5')
    cur = manifest_rows(R / 'MANIFEST.sha256')
    require(set(cur) == (set(v025) | added) - {'MANIFEST.sha256'}, 'v0.2.5K: the file set is exactly v0.2.5 plus the declared additions')
    # whole-table provenance invariants
    cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    cols = cp[0].split('\t')
    prov = [dict(zip(cols, x.split('\t'))) for x in cp[1:] if x]
    rl = (R / 'evidence/REDACTIONS.tsv').read_text().split('\n')
    red = {r['release_path']: r for r in (dict(zip(rl[0].split('\t'), x.split('\t'))) for x in rl[1:] if x)}
    ppaths = [r['release_path'] for r in prov]
    srcfiles = {p.relative_to(R).as_posix() for p in (R / 'evidence/src').rglob('*') if p.is_file() or p.is_symlink()}
    require(len(ppaths) == len(set(ppaths)), 'v0.2.5K: no provenance path occurs twice (whole table)')
    require(set(ppaths) == srcfiles, 'v0.2.5K: provenance rows and evidence/src files correspond one to one (whole table)')
    require(all(sha(R / r['release_path']) == r['sha256'] for r in prov), 'v0.2.5K: every provenance row matches its file hash (whole table)')
    require(all((r['release_path'] in red and red[r['release_path']]['released_sha256'] == r['sha256']
                 and red[r['release_path']]['original_sha256'] == r['original_sha256'])
                or (r['release_path'] not in red and r['bytes'] == str((R / r['release_path']).stat().st_size)) for r in prov)
            and set(red) <= set(ppaths), 'v0.2.5K: sizes agree with the files, except the declared redactions (whole table)')
    tmp = Path(tempfile.mkdtemp(prefix='v025_reconstruct_'))
    try:
        T = tmp / 'repo'
        shutil.copytree(R, T, ignore=shutil.ignore_patterns('.git'), symlinks=True)
        for p, x in bc.items():
            (T / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(R / x['path'], T / p)
        for p in added:
            (T / p).unlink()
        tfiles = {q.relative_to(T).as_posix() for q in T.rglob('*') if q.is_file() or q.is_symlink()}
        require({q for q in tfiles if not ignored(q)} == set(v025), 'v0.2.5K: the reconstructed file set equals the v0.2.5 manifest (set equality)')
        require(all(sha(T / q) == h for q, h in v025.items()), 'v0.2.5K: every reconstructed file has its v0.2.5 hash')
        require(sha(T / 'tools/verify_patch_release.py') == REC['v025_checker_sha256'], 'v0.2.5K: reconstructed checker is the v0.2.5 checker, byte-identical')
        r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_patch_release.py')], capture_output=True, text=True, cwd=T)
        old_ok = r.returncode == 0 and 'V025_TRANSITION_PASS' in r.stdout and 'PATCH_RECHECK_PASS' in r.stdout
        if not old_ok:
            print(r.stdout[-1500:] + r.stderr[-1500:])
        require(old_ok, 'v0.2.5K: the v0.2.5 checker passes on the reconstructed v0.2.5 tree (it reconstructs v0.2.4 and runs every earlier check)')
        if '--with-v025-controls' in sys.argv:
            r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_v025_transition.py'), '--negative-controls'], capture_output=True, text=True, cwd=T)
            print('\n'.join(l for l in r.stdout.splitlines() if ' exit=' in l))
            require(r.returncode == 0 and 'NEGATIVE_CONTROLS_PASS' in r.stdout, 'v0.2.5K: the v0.2.5 negative controls pass on the reconstructed v0.2.5 tree')
        # ---- the route-K delta ----
        bdoc = json.loads((T / 'claims/claims.json').read_text()); cdoc = json.loads((R / 'claims/claims.json').read_text())
        bcl = {c['id']: c for c in bdoc['claims']}; ccl = {c['id']: c for c in cdoc['claims']}
        cids = [c['id'] for c in cdoc['claims']]; order = REC['claim_order']
        require(len(cids) == len(set(cids)) and cids == order and len(order) == len(set(order)), 'v0.2.5K: the claim ids are exactly the declared order, each once')
        require(set(order) == set(bcl) | set(NEW_IDS) and set(REC['new_claims']) == set(NEW_IDS) and not (set(NEW_IDS) & set(bcl)),
                'v0.2.5K: the claims are exactly the v0.2.5 claims plus S.3K (set equality)')
        require([i for i in cids if i in bcl] == list(bcl), 'v0.2.5K: the v0.2.5 claims keep their relative order')
        require({k: v for k, v in bdoc.items() if k != 'claims'} == {k: v for k, v in cdoc.items() if k != 'claims'}, 'v0.2.5K: claims.json header unchanged')
        delta = REC['claim_delta']
        require(set(delta) == set(REVISED_IDS), 'v0.2.5K: the revised claims are exactly S.3 and S.17-47')
        ok = True
        for i in bcl:
            if i not in delta:
                ok &= ccl[i] == bcl[i]; continue
            exp = dict(bcl[i])
            for f, x in delta[i].items():
                ok &= bcl[i].get(f) == x['before']; exp[f] = x['after']
            ok &= ccl[i] == exp
        require(ok, 'v0.2.5K: every v0.2.5 claim equals v0.2.5 plus exactly the declared field changes')
        require(all(ccl[i] == REC['new_claims'][i] for i in NEW_IDS), 'v0.2.5K: S.3K equals its declared value exactly')
        bad = e1_offenders(R, set(cur) | {'MANIFEST.sha256'})
        require(not bad, 'v0.2.5K: no line cites Kato 12.5(4) as the integral step outside the declared historical allowlist' + (f' {bad[:4]}' if bad else ''))
        check_claims(ccl, bcl)
        for p, edits in REC['text_edits'].items():
            s = (T / p).read_text()
            for e in edits:
                require(s.count(e['old']) == 1, f'v0.2.5K: edit anchor occurs exactly once in v0.2.5 {p}')
                if p.startswith('paper/') or p == 'README.md':
                    new = e['new'].replace(LABEL, '')
                    require(all(new.count(m) <= e['old'].count(m) for m in PROCESS_MARKERS), f'v0.2.5K: no internal process marker added to {p}')
                s = s.replace(e['old'], e['new'])
            require((R / p).read_text() == s, f'v0.2.5K: {p} equals v0.2.5 plus exactly the declared edits')
        require('\\cid{S.3K}; ' + LABEL in (R / 'paper/sections/04_primary.tex').read_text(), 'v0.2.5K: the manuscript states route K with its exact grade label')
        ex_old, ex_new = (T / 'tools/extra_evidence.txt').read_text(), (R / 'tools/extra_evidence.txt').read_text()
        require(ex_new == ex_old + REC['extra_evidence_append'], 'v0.2.5K: tools/extra_evidence.txt is v0.2.5 plus exactly the declared appended text')
        bp = (T / 'evidence/PROVENANCE.tsv').read_text().split('\n')
        require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'v0.2.5K: every v0.2.5 provenance row preserved byte for byte, in order')
        decl = json.loads((R / REC['evidence']['declared']['path']).read_text())
        tlog = json.loads((R / REC['evidence']['transition_log']['path']).read_text())
        dpaths = [a['release_path'] for a in decl['additions']]; want = {a['release_path']: a for a in decl['additions']}
        appended_lines = [l for l in REC['extra_evidence_append'].splitlines() if l and not l.startswith('#')]
        require(len(dpaths) == len(set(dpaths)) and len(tlog['appended']) == len(set(tlog['appended'])) and set(tlog['appended']) == set(dpaths)
                and len(appended_lines) == len(set(appended_lines)) and set(appended_lines) == {a['original_path'] for a in decl['additions']},
                'v0.2.5K: the declaration, the logged append list and the appended source list name the same files, each exactly once')
        require(all(a['disposition'] == 'admitted_unmasked' for a in decl['additions']), 'v0.2.5K: every declared addition is admitted unmasked')
        expect = ['\t'.join([p, want[p]['original_path'], want[p]['sha256'], str(want[p]['bytes']), 'extra', '', '', '', want[p]['sha256']]) for p in tlog['appended']]
        require(cp[len(bp) - 1:-1] == expect, 'v0.2.5K: the appended provenance rows are exactly one row per declared addition, in logged order, with exact content')
        require({p for p in added if p.startswith('evidence/')} == set(dpaths), 'v0.2.5K: the added evidence files are exactly the declared additions')
        require(all((R / 'evidence' / n).read_bytes() == (T / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')),
                'v0.2.5K: exclusion and redaction tables unchanged')
        require(all(sha(R / a) == want[a]['sha256'] for a in want), 'v0.2.5K: declared evidence files present with their hashes')
        rsc = json.loads((R / REC['evidence']['retained_source_changes']['path']).read_text())['retained_source_changes']
        bprov = {x.split('\t')[0]: x.split('\t') for x in bp[1:] if x}
        require(len({x['release_path'] for x in rsc}) == len(rsc) and all(x['release_path'] in bprov and bprov[x['release_path']][2] == x['released_sha256']
                                                                          and sha(R / x['release_path']) == x['released_sha256'] for x in rsc),
                'v0.2.5K: each retained source change is a v0.2.5 row, declared once, whose released bytes are unchanged')
        require(sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in tlog.get('retained_source_changes', []))
                == sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in rsc), 'v0.2.5K: the transition log retained exactly the declared source changes')
        require(tlog['baseline_tables'] == {n: {'path': f'{HR}/evidence/{n}', 'sha256': sha(T / 'evidence' / n)} for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')},
                'v0.2.5K: the transition started from the v0.2.5 tables')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ev = REC['evidence']
    require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'transition_log', 'retained_source_changes')),
            'v0.2.5K: evidence declaration, retained-change declaration and transition log bound')
    require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}, 'v0.2.5K: transition log matches the current tables')
    t = subprocess.run([sys.executable, '-B', str(R / 'tools/build_evidence_transition.py'), '--self-test'], capture_output=True, text=True)
    require(t.returncode == 0 and 'SELF_TEST_PASS' in t.stdout and [l.split()[-1] for l in t.stdout.splitlines()[:-1]] == ['rejected'] * 19,
            'v0.2.5K: the evidence transition tool rejects all 19 of its self-test corruptions')
    gov = [g for item in REC['governing_files'].values() for g in item]
    require(all(sha(R / g['release_path']) == g['sha256'] for g in gov if g.get('release_path')), 'v0.2.5K: every released governing file matches its bound sha256')
    bound = set(REC['current_bindings'])
    require(bound == (changed | added) - {'MANIFEST.sha256', REC_PATH} and all(sha(R / p) == h for p, h in REC['current_bindings'].items()),
            'v0.2.5K: every changed or added file (except the manifest and this record) bound to its bytes')
    for gen in ('build_index.py', 'build_brief.py'):
        g = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
        require(g.returncode == 0, 'v0.2.5K: generated output current: ' + gen)
    for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
        require(not ((changed | added) & set(json.loads((R / 'review' / name).read_text())['files'])), 'v0.2.5K: no edited path among the non-redirectable ' + name)
    print('V025K_TRANSITION_PASS: the v0.2.5 bank tree reconstructed and its checker passes; the route-K delta is exactly the declared one')


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
    d['new_claims'] = {i: cl[i] for i in d['new_claims'] if i in cl}
    base = {c['id']: c for c in json.loads((t / d['history_root'] / 'claims/claims.json').read_text())['claims']}
    d['claim_delta'] = {i: {f: {'before': base[i].get(f), 'after': cl[i][f]} for f in cl[i] if cl[i][f] != base[i].get(f)} for i in d['claim_delta']}
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


def m_label_removed(t):      # K-BK3: the route-K row with its grade label removed
    _spec_edit(t, 'claims/spec/part1_core.py', "          verification={'grade_label': VK.LABEL,\n", "          verification={\n")
    _spec_edit(t, 'claims/spec/part1_core.py', "qualifications=['Grade: ' + VK.LABEL + '.',", "qualifications=['Grade: written derivation.',"); _rebind_all(t)
def m_e1_spec(t):            # K-BK3: 12.5(4) cited again as the integral step (claims spec, regenerated)
    _spec_edit(t, 'claims/spec/part1_core.py', "with Kato 13.4(3) via 13.14 (the integral inequality at every height-one prime; '",
               "with Kato 2004 12.5(4), which holds for T_3E (the integral inequality at every height-one prime; '"); _rebind_all(t)
def m_e1_paper(t):           # K-BK3: the same in the manuscript, through a rebound declared edit
    old, new = "combined with Kato's Theorem~13.4(3) via 13.14", "combined with Kato's \\cite[12.5(4)]{kato}, which holds for $T_3E$,"
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    e = next(e for e in d['text_edits']['paper/sections/04_primary.tex'] if 'Theorem~13.4(3) via 13.14 (the integral' in e['new'])
    e['new'] = e['new'].replace("with Kato's Theorem~13.4(3) via 13.14", "with Kato's \\cite[12.5(4)]{kato}, which holds for $T_3E$,")
    rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    p = t / 'paper/sections/04_primary.tex'; s = p.read_text(); assert s.count("with Kato's Theorem~13.4(3) via 13.14") == 1
    p.write_text(s.replace("with Kato's Theorem~13.4(3) via 13.14", "with Kato's \\cite[12.5(4)]{kato}, which holds for $T_3E$,")); _rebind_all(t)
def m_drop_reader(t):        # K-BK3: a reader's return dropped everywhere (file, row, declaration, log, source list, spec), all rebound
    rel = _SRB + 'RETURN.md'
    _spec_edit(t, 'claims/spec/common.py', "E(b + 'RETURN.md', 'second reader B: PASS_WITH_CORRECTIONS'), ", "")
    (t / rel).unlink()
    p, L = _prov(t); p.write_text('\n'.join(x for x in L if not x.startswith(rel + '\t')))
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    dp = t / d['evidence']['declared']['path']; dj = json.loads(dp.read_text()); src = next(a['original_path'] for a in dj['additions'] if a['release_path'] == rel)
    dj['additions'] = [a for a in dj['additions'] if a['release_path'] != rel]; dp.write_text(json.dumps(dj, indent=1, ensure_ascii=False) + '\n')
    tl = t / d['evidence']['transition_log']['path']; tj = json.loads(tl.read_text()); tj['appended'] = [a for a in tj['appended'] if a != rel]
    tl.write_text(json.dumps(tj, indent=1, ensure_ascii=False) + '\n')
    d['extra_evidence_append'] = d['extra_evidence_append'].replace(src + '\n', '')
    ex = t / 'tools/extra_evidence.txt'; ex.write_text(ex.read_text().replace(src + '\n', ''))
    d['added_paths'] = [a for a in d['added_paths'] if a != rel]
    for item in d['governing_files'].values():
        item[:] = [g for g in item if g.get('release_path') != rel]
    rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n'); _rebind_all(t)
def m_omit_appended(t):
    p, L = _prov(t); del L[_n_old(t) + 3]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_dup_appended(t):
    p, L = _prov(t); k = _n_old(t); L[k + 5] = L[k + 4]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_history_byte(t):
    p = t / 'review/history/v0.2.5/README.md'; b = bytearray(p.read_bytes()); b[10] ^= 1; p.write_bytes(bytes(b))
def m_s3_statement(t):       # S.3's statement changed (frozen by the scope)
    _spec_edit(t, 'claims/spec/part1_core.py', "'Sha(E/Q)[3^infinity] is isomorphic to (Z/3Z)^2. The certified", "'Sha(E/Q)[3^infinity] is isomorphic to (Z/3Z)^2 unconditionally. The certified"); _rebind_all(t)
def m_ota_print(t):          # F2 undone: the print citation removed
    _spec_edit(t, 'claims/spec/part1_core.py', "\"K. Ota, 'Kato's Euler system and the Mazur-Tate refined conjecture of BSD type', Amer. J. Math. 140 (2018) 495-542; \"\n",
               "\"K. Ota; \"\n"); _rebind_all(t)
def m_paper_edit(t):
    p = t / 'paper/sections/04_primary.tex'; s = p.read_text(); assert 'with no input from Skinner' in s
    p.write_text(s.replace('with no input from Skinner', 'with no input at all from Skinner', 1)); _rebind_all(t)
def m_undeclared_file(t):
    (t / 'evidence/src/UNDECLARED.txt').write_text('x\n')
    m = t / 'MANIFEST.sha256'; m.write_text(m.read_text() + hashlib.sha256(b'x\n').hexdigest() + '  evidence/src/UNDECLARED.txt\n')


CONTROLS = [('positive_control_unmodified', None, ''),
            ('K1_route_K_label_removed_rebound', m_label_removed, 'S.3K within its bound'),
            ('K2a_integral_12_5_4_citation_in_spec_rebound', m_e1_spec, 'no line cites Kato 12.5(4) as the integral step'),
            ('K2b_integral_12_5_4_citation_in_paper_rebound', m_e1_paper, 'no line cites Kato 12.5(4) as the integral step'),
            ('K3_reader_return_dropped_rebound_all', m_drop_reader, 'S.3K cites, and the release contains, every required route-K record'),
            ('a_appended_row_omitted_rebound_all', m_omit_appended, 'provenance rows and evidence/src files correspond one to one'),
            ('b_duplicate_rebinds_omitted_appended_row', m_dup_appended, 'no provenance path occurs twice'),
            ('c_historical_copy_byte_altered', m_history_byte, 'preserved v0.2.5 base copies intact'),
            ('d_S3_statement_changed_rebound', m_s3_statement, "S.3's statement and grades unchanged"),
            ('e_ota_print_citation_removed_rebound', m_ota_print, "S.17-47 cites Ota's print"),
            ('f_undeclared_paper_edit_rebound', m_paper_edit, '04_primary.tex equals v0.2.5 plus exactly the declared edits'),
            ('g_undeclared_evidence_file', m_undeclared_file, 'the file set is exactly v0.2.5 plus the declared additions')]


def negative_controls():
    res = {}
    for name, mut, want in CONTROLS:
        tmp = Path(tempfile.mkdtemp(prefix='v025k_negctl_'))
        try:
            t = tmp / 'repo'; shutil.copytree(R, t, ignore=shutil.ignore_patterns('.git'), symlinks=True)
            if mut:
                mut(t)
            r = subprocess.run([sys.executable, '-B', str(t / 'tools/verify_v025k_transition.py')], capture_output=True, text=True, cwd=t)
            first = next((l for l in (r.stdout + r.stderr).splitlines() if l.startswith('FAIL')), '')
            ok = (r.returncode == 0 and 'V025K_TRANSITION_PASS' in r.stdout) if not mut else (r.returncode != 0 and want in first)
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
