#!/usr/bin/env python3
"""K2 transition check (the cross-family reading of route K): reconstruct the route-K tree exactly, run ITS checker
unchanged, then check the K2 delta.

  python3 tools/verify_v025k2_transition.py                         the check (prints V025K2_TRANSITION_PASS)
  python3 tools/verify_v025k2_transition.py --with-prev-controls    also run the route-K negative controls in the reconstruction
  python3 tools/verify_v025k2_transition.py --negative-controls     corrupt throwaway copies; every control must FAIL

1. Copy this tree, restore every path in the record's `base_copies` (the route-K bytes kept under review/history/v0.2.5k/),
   remove every path in `added_paths`; the reconstructed file set must EQUAL the preserved route-K manifest.
2. Run the reconstructed tree's tools/verify_patch_release.py (the route-K checker, byte-identical). It reconstructs the
   v0.2.5 bank tree in turn, and so on back. It must pass.
3. Check the K2 delta by exact rows, exact lists and set equality with uniqueness, then the bounds fixed HERE (not in the
   record): the new S.3K label (with its cross-family clause), S.3's primary support, the regulator relation
   v_3(#Sha[3^inf]) <= 4 - v_3(Reg_3), the 12.5(4) wording, the kappa-shift dictionary, and the Codex evidence (its own files
   copied; its third-party source_checks/ bound by hash only, matching the released Codex manifest). Outward scans: no
   old "<= 81" sentence, no bare 12.5(4) wording, no old label, no added process marker.
Standard library only; this repository is never written.
"""
import hashlib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
REC_PATH = 'review/V025K2_APPLIED.json'
PRIOR_RECORDS = ('review/V025_BANK_APPLIED.json', 'review/V025K_ROUTEK_APPLIED.json')
LABEL = ('written derivation; three Anthropic model readers (one cross-model: Fable 5.1; two independent fresh sessions: '
         'Opus 5.5) and one cross-family source reading (Codex, OpenAI) of D5/D6/D8 with the errata E1–E7, passing at the '
         'retained arithmetic-input and imported-theorem grades; not a full certificate replay; no human review')
LABEL_TEX = LABEL.replace('–', '--')
OLD_LABEL_TAIL = 'all Anthropic models, not cross-family'
REVISED_IDS = ['S.3', 'S.3K']
_S = 'evidence/src/'
_CODEX = _S + 'BSD_ASTRA_CATCHUP_RETURN_2026-09-30/'
CODEX_REQUIRED = [_CODEX + f for f in ('RETURN.md', 'MANIFEST.sha256', 'ITEM1_ROUTE_K.md', 'ITEM1_PRECOMPARISON.md', 'K_ASTRA_1.md',
                                       'ITEM3_RELEASE_WORDING.md', 'RECORD_REPAIRS.md', 'INTEGRITY_AND_SCOPE.md', 'ITEM2_UNIFORM_STEP.md',
                                       'ITEM4_CATCHUP_AND_CONTRADICTIONS.md', 'RESUME.md', 'SOURCE_BINDINGS.tsv',
                                       'checks/normalization.gp', 'checks/normalization.log')]
_R25, _FCK = _S + 'BSD_P3_MS_R24_COLEMAN_RETURN_OPUS_2026-09-29/', _S + 'BSD_P3_MS_R24_COLEMAN_CHECK_FABLE_2026-09-29/'
_SRA, _SRB = _S + 'BSD_R25_SECOND_READER_RETURN_OPUS_2026-09-29/', _S + 'BSD_R25_SECOND_READER_RETURN_OPUS_B_2026-09-29/'
ROUTEK_REQUIRED = ([_R25 + d for d in ('D5_MS_R24.md', 'D6_O2_POITOU_TATE.md', 'D8_ASSEMBLY.md', 'RETURN.md')]
                   + [_FCK + 'CHECK.md', _SRA + 'RETURN.md', _SRB + 'RETURN.md',
                      _S + 'BSD_SEED_V025_BANK_ROUTEK_TASK_2026-09-29/inputs/R25_ERRATA_2026-09-29.md'])
ALLOW_FILES = set(PRIOR_RECORDS) | {REC_PATH, 'tools/verify_v025k_transition.py', 'tools/verify_v025k2_transition.py'}
ALLOW_PREFIXES = ('review/history/', 'evidence/src/')
E1 = re.compile(r'12\.5 ?\(4\)')
OLD81 = re.compile(r'give only[^.;]{0,40}81')
LABEL_SCOPE = ('claims/', 'paper/', 'README.md', 'review/SYNTHESIS_CHECK_BRIEF.md')
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


def scan(paths):
    """Outward text scans; returns (bad 12.5(4) lines, old <= 81 lines, old-label lines)."""
    e1, o81, lab = [], [], []
    for rel in sorted(paths):
        if rel in ALLOW_FILES or rel.startswith(ALLOW_PREFIXES):
            continue
        try:
            text = (R / rel).read_text()
        except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if E1.search(line) and 'final length inequality of 12.5(4)' not in line:
                e1.append(f'{rel}:{n}')
            if OLD81.search(line):
                o81.append(f'{rel}:{n}')
            if rel.startswith(LABEL_SCOPE) and OLD_LABEL_TAIL in line:
                lab.append(f'{rel}:{n}')
    return e1, o81, lab


def check_claims(ccl, bcl, REC):
    k, bk = ccl['S.3K'], bcl['S.3K']
    ev = {e['path'] for e in k['evidence']}
    require(set(CODEX_REQUIRED) | set(ROUTEK_REQUIRED) <= ev and all((R / p).is_file() for p in CODEX_REQUIRED + ROUTEK_REQUIRED),
            'v0.2.5K2: S.3K cites, and the release contains, the Codex reading and the route-K records')
    imp = json.dumps(k['imports'], ensure_ascii=False)
    ok = (k['statement'] == bk['statement'] and k['kind'] == bk['kind'] and k['grades'] == bk['grades']
          and k['verification'].get('grade_label') == LABEL and k['qualifications'][0] == 'Grade: ' + LABEL + '.'
          and k['verification'].get('review', '').startswith('MODEL_CROSS_FAMILY:') and 'Codex (OpenAI)' in k['verification']['review']
          and 'not a full certificate replay' in k['verification']['review'] and 'no human review' in k['verification']['review']
          and '4 - v_3(Reg_3)' in imp and 'whose actual valuation 2 gives <= 9' in imp and 'only a gamma-free valuation of 0 would give <= 81' in imp
          and 'the final length inequality of 12.5(4) is printed for V' in imp and 'integral containment Z(f,T) in H^1(T) is retained (and used)' in imp)
    require(ok, 'v0.2.5K2: S.3K within its K2 bound (statement and grades unchanged; exact label with the cross-family clause; regulator relation; 12.5(4) wording)')
    s3, b3 = ccl['S.3'], bcl['S.3']
    require(all(s3[f] == b3[f] for f in ('title', 'statement', 'kind', 'grades')) and s3['verification'].get('primary_support') == 'route K (S.3K): ' + LABEL,
            "v0.2.5K2: S.3's statement and grades unchanged; its primary support carries the new label")
    bad = [c['id'] for c in ccl.values() if any(s in json.dumps(c, ensure_ascii=False) for s in ('only remains', 'all that remains', 'only what remains'))
           or c['verification'].get('review', '').startswith('HUMAN') or ('LEAN_CHECKED' in c['grades'] and 'LEAN_CHECKED' not in bcl[c['id']]['grades'])]
    require(not bad, 'v0.2.5K2: no claim says "only/all that remains", claims human review, or gains LEAN_CHECKED')
    tp = REC['governing_files']['codex_third_party_hash_only']
    cm = {rel: h for h, rel in (l.split('  ', 1) for l in (R / (_CODEX + 'MANIFEST.sha256')).read_text().splitlines())}
    require(len(tp) == 12 and all(x['name'].startswith('source_checks/') and cm.get(x['name']) == x['sha256']
                                  and not (R / _CODEX / x['name']).exists() for x in tp)
            and {n for n in cm if n.startswith('source_checks/')} == {x['name'] for x in tp},
            "v0.2.5K2: Codex's 12 third-party source_checks files are bound by hash (matching its released manifest) and not copied")


def main():
    REC = json.loads((R / REC_PATH).read_text())
    HR = REC['history_root']
    bc, added = REC['base_copies'], REC['added_paths']
    require(len(added) == len(set(added)), 'v0.2.5K2: each added path is declared once')
    added = set(added); changed = set(bc)
    require(not (set(PRIOR_RECORDS) & (changed | added)), 'v0.2.5K2: the v0.2.5 and route-K records are unchanged')
    prev = manifest_rows(R / REC['prev_manifest']['path'])
    require(all(x['path'] == f'{HR}/{p}' and sha(R / x['path']) == x['sha256'] for p, x in bc.items()), 'v0.2.5K2: preserved route-K base copies intact')
    require(sha(R / REC['prev_manifest']['path']) == REC['prev_manifest']['sha256'], 'v0.2.5K2: preserved route-K manifest bound')
    require(not (added & set(prev)) and changed - {'MANIFEST.sha256'} <= set(prev), 'v0.2.5K2: added paths are new; changed paths existed at route K')
    cur = manifest_rows(R / 'MANIFEST.sha256')
    require(set(cur) == (set(prev) | added) - {'MANIFEST.sha256'}, 'v0.2.5K2: the file set is exactly the route-K set plus the declared additions')
    cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    cols = cp[0].split('\t')
    prov = [dict(zip(cols, x.split('\t'))) for x in cp[1:] if x]
    rl = (R / 'evidence/REDACTIONS.tsv').read_text().split('\n')
    red = {r['release_path']: r for r in (dict(zip(rl[0].split('\t'), x.split('\t'))) for x in rl[1:] if x)}
    ppaths = [r['release_path'] for r in prov]
    srcfiles = {p.relative_to(R).as_posix() for p in (R / 'evidence/src').rglob('*') if p.is_file() or p.is_symlink()}
    require(len(ppaths) == len(set(ppaths)), 'v0.2.5K2: no provenance path occurs twice (whole table)')
    require(set(ppaths) == srcfiles, 'v0.2.5K2: provenance rows and evidence/src files correspond one to one (whole table)')
    require(all(sha(R / r['release_path']) == r['sha256'] for r in prov), 'v0.2.5K2: every provenance row matches its file hash (whole table)')
    require(all((r['release_path'] in red and red[r['release_path']]['released_sha256'] == r['sha256']
                 and red[r['release_path']]['original_sha256'] == r['original_sha256'])
                or (r['release_path'] not in red and r['bytes'] == str((R / r['release_path']).stat().st_size)) for r in prov)
            and set(red) <= set(ppaths), 'v0.2.5K2: sizes agree with the files, except the declared redactions (whole table)')
    tmp = Path(tempfile.mkdtemp(prefix='v025k_reconstruct_'))
    try:
        T = tmp / 'repo'
        shutil.copytree(R, T, ignore=shutil.ignore_patterns('.git'), symlinks=True)
        for p, x in bc.items():
            (T / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(R / x['path'], T / p)
        for p in added:
            (T / p).unlink()
        tfiles = {q.relative_to(T).as_posix() for q in T.rglob('*') if q.is_file() or q.is_symlink()}
        require({q for q in tfiles if not ignored(q)} == set(prev), 'v0.2.5K2: the reconstructed file set equals the route-K manifest (set equality)')
        require(all(sha(T / q) == h for q, h in prev.items()), 'v0.2.5K2: every reconstructed file has its route-K hash')
        require(sha(T / 'tools/verify_patch_release.py') == REC['prev_checker_sha256'], 'v0.2.5K2: reconstructed checker is the route-K checker, byte-identical')
        r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_patch_release.py')], capture_output=True, text=True, cwd=T)
        old_ok = r.returncode == 0 and 'V025K_TRANSITION_PASS' in r.stdout and 'PATCH_RECHECK_PASS' in r.stdout
        if not old_ok:
            print(r.stdout[-1500:] + r.stderr[-1500:])
        require(old_ok, 'v0.2.5K2: the route-K checker passes on the reconstructed route-K tree (it reconstructs every earlier tree)')
        if '--with-prev-controls' in sys.argv:
            r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_v025k_transition.py'), '--negative-controls'], capture_output=True, text=True, cwd=T)
            print('\n'.join(l for l in r.stdout.splitlines() if ' exit=' in l))
            require(r.returncode == 0 and 'NEGATIVE_CONTROLS_PASS' in r.stdout, 'v0.2.5K2: the route-K negative controls pass on the reconstructed route-K tree')
        bdoc = json.loads((T / 'claims/claims.json').read_text()); cdoc = json.loads((R / 'claims/claims.json').read_text())
        bcl = {c['id']: c for c in bdoc['claims']}; ccl = {c['id']: c for c in cdoc['claims']}
        require([c['id'] for c in cdoc['claims']] == [c['id'] for c in bdoc['claims']] == REC['claim_order']
                and len(REC['claim_order']) == len(set(REC['claim_order'])), 'v0.2.5K2: the same claims in the same order, each once')
        require({k: v for k, v in bdoc.items() if k != 'claims'} == {k: v for k, v in cdoc.items() if k != 'claims'}, 'v0.2.5K2: claims.json header unchanged')
        delta = REC['claim_delta']
        require(set(delta) == set(REVISED_IDS), 'v0.2.5K2: the revised claims are exactly S.3 and S.3K')
        ok = True
        for i in bcl:
            if i not in delta:
                ok &= ccl[i] == bcl[i]; continue
            exp = dict(bcl[i])
            for f, x in delta[i].items():
                ok &= bcl[i].get(f) == x['before']; exp[f] = x['after']
            ok &= ccl[i] == exp
        require(ok, 'v0.2.5K2: every route-K claim equals its route-K value plus exactly the declared field changes')
        e1, o81, lab = scan(set(cur) | {'MANIFEST.sha256'})
        require(not o81, 'v0.2.5K2: no outward line assigns <= 81 to the actual regulator' + (f' {o81[:4]}' if o81 else ''))
        require(not e1, 'v0.2.5K2: every outward 12.5(4) line says that its final length inequality is printed for V' + (f' {e1[:4]}' if e1 else ''))
        require(not lab, 'v0.2.5K2: the old route-K label is gone from the claims, paper, README and brief' + (f' {lab[:4]}' if lab else ''))
        check_claims(ccl, bcl, REC)
        pap = (R / 'paper/sections/04_primary.tex').read_text()
        require('\\cid{S.3K}; ' + LABEL_TEX in pap and '4-\\ord_3\\Reg_3' in pap and 'shifted by the cyclotomic character $\\kappa$' in pap
                and 'not related to it by an involution' in pap, 'v0.2.5K2: the manuscript carries the new label, the regulator relation and the kappa-shift dictionary')
        require('one cross-family source reading (Codex, OpenAI)' in (R / 'README.md').read_text(), 'v0.2.5K2: the README states the cross-family reading')
        for p, edits in REC['text_edits'].items():
            s = (T / p).read_text()
            for e in edits:
                require(s.count(e['old']) == 1, f'v0.2.5K2: edit anchor occurs exactly once in the route-K {p}')
                if p.startswith('paper/') or p == 'README.md':
                    new = e['new'].replace(LABEL_TEX, '')
                    require(all(new.count(m) <= e['old'].count(m) for m in PROCESS_MARKERS), f'v0.2.5K2: no internal process marker added to {p}')
                s = s.replace(e['old'], e['new'])
            require((R / p).read_text() == s, f'v0.2.5K2: {p} equals the route-K file plus exactly the declared edits')
        ex_old, ex_new = (T / 'tools/extra_evidence.txt').read_text(), (R / 'tools/extra_evidence.txt').read_text()
        require(ex_new == ex_old + REC['extra_evidence_append'], 'v0.2.5K2: tools/extra_evidence.txt is the route-K file plus exactly the declared appended text')
        bp = (T / 'evidence/PROVENANCE.tsv').read_text().split('\n')
        require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'v0.2.5K2: every route-K provenance row preserved byte for byte, in order')
        decl = json.loads((R / REC['evidence']['declared']['path']).read_text())
        tlog = json.loads((R / REC['evidence']['transition_log']['path']).read_text())
        dpaths = [a['release_path'] for a in decl['additions']]; want = {a['release_path']: a for a in decl['additions']}
        appended_lines = [l for l in REC['extra_evidence_append'].splitlines() if l and not l.startswith('#')]
        require(len(dpaths) == len(set(dpaths)) and len(tlog['appended']) == len(set(tlog['appended'])) and set(tlog['appended']) == set(dpaths)
                and len(appended_lines) == len(set(appended_lines)) and set(appended_lines) == {a['original_path'] for a in decl['additions']},
                'v0.2.5K2: the declaration, the logged append list and the appended source list name the same files, each exactly once')
        require(all(a['disposition'] == 'admitted_unmasked' for a in decl['additions']), 'v0.2.5K2: every declared addition is admitted unmasked')
        expect = ['\t'.join([p, want[p]['original_path'], want[p]['sha256'], str(want[p]['bytes']), 'extra', '', '', '', want[p]['sha256']]) for p in tlog['appended']]
        require(cp[len(bp) - 1:-1] == expect, 'v0.2.5K2: the appended provenance rows are exactly one row per declared addition, in logged order, with exact content')
        require({p for p in added if p.startswith('evidence/')} == set(dpaths), 'v0.2.5K2: the added evidence files are exactly the declared additions')
        require(all((R / 'evidence' / n).read_bytes() == (T / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')),
                'v0.2.5K2: exclusion and redaction tables unchanged')
        require(all(sha(R / a) == want[a]['sha256'] for a in want), 'v0.2.5K2: declared evidence files present with their hashes')
        rsc = json.loads((R / REC['evidence']['retained_source_changes']['path']).read_text())['retained_source_changes']
        bprov = {x.split('\t')[0]: x.split('\t') for x in bp[1:] if x}
        require(len({x['release_path'] for x in rsc}) == len(rsc) and all(x['release_path'] in bprov and bprov[x['release_path']][2] == x['released_sha256']
                                                                          and sha(R / x['release_path']) == x['released_sha256'] for x in rsc),
                'v0.2.5K2: each retained source change is a route-K row, declared once, whose released bytes are unchanged')
        require(sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in tlog.get('retained_source_changes', []))
                == sorted((x['release_path'], x['released_sha256'], x['live_sha256']) for x in rsc), 'v0.2.5K2: the transition log retained exactly the declared source changes')
        require(tlog['baseline_tables'] == {n: {'path': f'{HR}/evidence/{n}', 'sha256': sha(T / 'evidence' / n)} for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')},
                'v0.2.5K2: the transition started from the route-K tables')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ev = REC['evidence']
    require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'transition_log', 'retained_source_changes')),
            'v0.2.5K2: evidence declaration, retained-change declaration and transition log bound')
    require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}, 'v0.2.5K2: transition log matches the current tables')
    t = subprocess.run([sys.executable, '-B', str(R / 'tools/build_evidence_transition.py'), '--self-test'], capture_output=True, text=True)
    require(t.returncode == 0 and 'SELF_TEST_PASS' in t.stdout and [l.split()[-1] for l in t.stdout.splitlines()[:-1]] == ['rejected'] * 19,
            'v0.2.5K2: the evidence transition tool rejects all 19 of its self-test corruptions')
    gov = [g for item in REC['governing_files'].values() for g in item]
    require(all(sha(R / g['release_path']) == g['sha256'] for g in gov if g.get('release_path')), 'v0.2.5K2: every released governing file matches its bound sha256')
    bound = set(REC['current_bindings'])
    require(bound == (changed | added) - {'MANIFEST.sha256', REC_PATH} and all(sha(R / p) == h for p, h in REC['current_bindings'].items()),
            'v0.2.5K2: every changed or added file (except the manifest and this record) bound to its bytes')
    for gen in ('build_index.py', 'build_brief.py'):
        g = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
        require(g.returncode == 0, 'v0.2.5K2: generated output current: ' + gen)
    for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
        require(not ((changed | added) & set(json.loads((R / 'review' / name).read_text())['files'])), 'v0.2.5K2: no edited path among the non-redirectable ' + name)
    print('V025K2_TRANSITION_PASS: the route-K tree reconstructed and its checker passes; the K2 delta is exactly the declared one')


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


def _paper_rebound(t, old, new):
    rp = t / REC_PATH; d = json.loads(rp.read_text())
    e = next(e for e in d['text_edits']['paper/sections/04_primary.tex'] if old in e['new'])
    e['new'] = e['new'].replace(old, new); rp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    p = t / 'paper/sections/04_primary.tex'; s = p.read_text(); assert s.count(old) == 1; p.write_text(s.replace(old, new))


def m_old81_paper(t):        # K2: the old "<= 81" sentence restored in the manuscript, through a rebound declared edit
    _paper_rebound(t, 'If only valuation $0$ for the $\\gamma$-free determinant had been established, the resulting bound would be $81$ rather than $9$.',
                   'For the $\\gamma$-free determinant, whose valuation is $2$, the chain would give only $\\#\\Sha[3^\\infty]\\le81$.'); _rebind_all(t)
def m_old81_spec(t):         # K2: the old "<= 81" phrase restored in S.3K's imports (spec, regenerated)
    _spec_edit(t, 'claims/spec/part1_core.py', 'whose actual valuation 2 gives <= 9; only a gamma-free valuation of 0 would give <= 81',
               'the gamma-free determinant would give only <= 81'); _rebind_all(t)
def m_label_no_crossfamily(t):  # K2: the S.3K label without its cross-family clause
    _spec_edit(t, 'claims/spec/common.py', " and one cross-family source reading (Codex, OpenAI) of D5/D6/D8 with the errata E1–E7, passing at the '\n"
               "             'retained arithmetic-input and imported-theorem grades", "'\n             '"); _rebind_all(t)
def m_drop_codex(t):         # K2: a Codex evidence file dropped everywhere (file, row, declaration, log, source list, spec), all rebound
    rel = _CODEX + 'ITEM1_ROUTE_K.md'
    _spec_edit(t, 'claims/spec/common.py', "['RETURN.md', 'MANIFEST.sha256', 'ITEM1_ROUTE_K.md', ", "['RETURN.md', 'MANIFEST.sha256', ")
    _spec_edit(t, 'claims/spec/part1_core.py', "                    E(VK.CODEX + 'ITEM1_ROUTE_K.md', 'cross-family source reading of route K')],\n", "                    ],\n")
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
def m_bare_1254(t):          # the shorter 12.5(4) wording restored in the spec
    _spec_edit(t, 'claims/spec/part1_core.py', 'the final length inequality of 12.5(4) is printed for V; its integral containment Z(f,T) in H^1(T) is retained (and used)',
               '12.5(4) is printed for V and is not the integral step'); _rebind_all(t)
def m_lean_upgrade(t):       # an upgrade to formalized: LEAN_CHECKED added to S.3K
    _spec_edit(t, 'claims/spec/part1_core.py', "'THEOREM', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED', 'PROVED_COMPUTER_ASSISTED'],\n          origin='written derivation applying",
               "'THEOREM', ['PROVED_WRITTEN', 'IMPORTED_PUBLISHED', 'PROVED_COMPUTER_ASSISTED', 'LEAN_CHECKED'],\n          origin='written derivation applying"); _rebind_all(t)
def m_omit_appended(t):
    p, L = _prov(t); del L[_n_old(t) + 3]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_dup_appended(t):
    p, L = _prov(t); k = _n_old(t); L[k + 5] = L[k + 4]; p.write_text('\n'.join(L)); _rebind_all(t)
def m_history_byte(t):
    p = t / 'review/history/v0.2.5k/README.md'; b = bytearray(p.read_bytes()); b[10] ^= 1; p.write_bytes(bytes(b))
def m_paper_edit(t):
    p = t / 'paper/sections/04_primary.tex'; s = p.read_text(); assert 'with no input from Skinner' in s
    p.write_text(s.replace('with no input from Skinner', 'with no input at all from Skinner', 1)); _rebind_all(t)
def m_undeclared_file(t):
    (t / 'evidence/src/UNDECLARED.txt').write_text('x\n')
    m = t / 'MANIFEST.sha256'; m.write_text(m.read_text() + hashlib.sha256(b'x\n').hexdigest() + '  evidence/src/UNDECLARED.txt\n')


CONTROLS = [('positive_control_unmodified', None, ''),
            ('K2_1a_old_81_sentence_restored_in_paper_rebound', m_old81_paper, 'no outward line assigns <= 81 to the actual regulator'),
            ('K2_1b_old_81_phrase_restored_in_spec_rebound', m_old81_spec, 'no outward line assigns <= 81 to the actual regulator'),
            ('K2_2_label_without_cross_family_clause_rebound', m_label_no_crossfamily, 'S.3K within its K2 bound'),
            ('K2_3_codex_evidence_file_dropped_rebound_all', m_drop_codex, 'S.3K cites, and the release contains, the Codex reading'),
            ('K2_4_bare_12_5_4_wording_restored_rebound', m_bare_1254, 'every outward 12.5(4) line says that its final length inequality is printed for V'),
            ('K2_5_S3K_upgraded_to_lean_checked_rebound', m_lean_upgrade, 'S.3K within its K2 bound'),
            ('a_appended_row_omitted_rebound_all', m_omit_appended, 'provenance rows and evidence/src files correspond one to one'),
            ('b_duplicate_rebinds_omitted_appended_row', m_dup_appended, 'no provenance path occurs twice'),
            ('c_historical_copy_byte_altered', m_history_byte, 'preserved route-K base copies intact'),
            ('d_undeclared_paper_edit_rebound', m_paper_edit, '04_primary.tex equals the route-K file plus exactly the declared edits'),
            ('e_undeclared_evidence_file', m_undeclared_file, 'the file set is exactly the route-K set plus the declared additions')]


def negative_controls():
    res = {}
    for name, mut, want in CONTROLS:
        tmp = Path(tempfile.mkdtemp(prefix='v025k2_negctl_'))
        try:
            t = tmp / 'repo'; shutil.copytree(R, t, ignore=shutil.ignore_patterns('.git'), symlinks=True)
            if mut:
                mut(t)
            r = subprocess.run([sys.executable, '-B', str(t / 'tools/verify_v025k2_transition.py')], capture_output=True, text=True, cwd=t)
            first = next((l for l in (r.stdout + r.stderr).splitlines() if l.startswith('FAIL')), '')
            ok = (r.returncode == 0 and 'V025K2_TRANSITION_PASS' in r.stdout) if not mut else (r.returncode != 0 and want in first)
            res[name] = {'exit': r.returncode, 'as_expected': ok, 'first_fail': first}
            print(f"{name:50s} exit={r.returncode} {'OK' if ok else 'UNEXPECTED'}  {first[:110]}", flush=True)
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
