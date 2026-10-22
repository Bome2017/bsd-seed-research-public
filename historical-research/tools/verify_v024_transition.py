#!/usr/bin/env python3
"""v0.2.4 transition check: reconstruct v0.2.3 exactly, run ITS checker unchanged, then check the v0.2.4 delta.

1. Copy this tree to a temporary directory, restore every path in the record's `base_copies` (v0.2.3 bytes kept under
   review/history/v0.2.3/), and remove every path in `added_paths`. Every file of the preserved v0.2.3 MANIFEST must be
   present with its v0.2.3 hash.
2. Run the reconstructed tree's own tools/verify_patch_release.py (the v0.2.3 checker, byte-identical). It must pass,
   including its A4 transition checks and every earlier binding. Nothing old is re-pointed or weakened.
3. Check that the current tree differs from v0.2.3 exactly as declared: the file set, claim fields before/after,
   exact-once text edits, evidence rows appended, generated outputs current, and every new byte bound.
Whole-table provenance invariants (added after the 2026-09-25 audit, finding F1) do not depend on any rebindable hash:
each provenance path occurs once, rows and evidence/src files correspond one to one, every row matches its file's
hash, and sizes agree except for the declared redactions. The appended rows must be exactly one row per declared
addition, in the logged order, with the exact expected content.
Prints V024_TRANSITION_PASS on success. Standard library only; this repository is never written.
"""
import hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
REC_PATH = 'review/V024_PERIMETER_APPLIED.json'
REC = json.loads((R / REC_PATH).read_text())
HR = REC['history_root']


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit('FAIL: ' + message)
    print('PASS: ' + message)


def manifest_rows(path):
    rows = {}
    for line in Path(path).read_text().splitlines():
        h, rel = line.split('  ', 1)
        rows[rel] = h
    return rows


bc, added = REC['base_copies'], set(REC['added_paths'])
changed = set(bc)
v023 = manifest_rows(R / REC['v023_manifest']['path'])

# ---- 0. the record's bindings of the preserved copies, and the file set ----
require(all(x['path'] == f'{HR}/{p}' and sha(R / x['path']) == x['sha256'] for p, x in bc.items()), 'v0.2.4: preserved v0.2.3 base copies intact')
require(sha(R / REC['v023_manifest']['path']) == REC['v023_manifest']['sha256'], 'v0.2.4: preserved v0.2.3 manifest bound')
require(not (added & set(v023)) and changed - {'MANIFEST.sha256'} <= set(v023), 'v0.2.4: added paths are new; changed paths existed in v0.2.3')
cur = manifest_rows(R / 'MANIFEST.sha256')
require(set(cur) == (set(v023) | added) - {'MANIFEST.sha256'}, 'v0.2.4: the file set is exactly v0.2.3 plus the declared additions')

# ---- 0b. whole-table provenance invariants (independent of every rebindable hash) ----
cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
cols = cp[0].split('\t')
prov = [dict(zip(cols, x.split('\t'))) for x in cp[1:] if x]
rl = (R / 'evidence/REDACTIONS.tsv').read_text().split('\n')
red = {r['release_path']: r for r in (dict(zip(rl[0].split('\t'), x.split('\t'))) for x in rl[1:] if x)}
ppaths = [r['release_path'] for r in prov]
srcfiles = {p.relative_to(R).as_posix() for p in (R / 'evidence/src').rglob('*') if p.is_file() or p.is_symlink()}
require(len(ppaths) == len(set(ppaths)), 'v0.2.4: no provenance path occurs twice (whole table)')
require(set(ppaths) == srcfiles, 'v0.2.4: provenance rows and evidence/src files correspond one to one (whole table)')
require(all(sha(R / r['release_path']) == r['sha256'] for r in prov), 'v0.2.4: every provenance row matches its file hash (whole table)')
require(all((r['release_path'] in red and red[r['release_path']]['released_sha256'] == r['sha256']
             and red[r['release_path']]['original_sha256'] == r['original_sha256'])
            or (r['release_path'] not in red and r['bytes'] == str((R / r['release_path']).stat().st_size)) for r in prov)
        and set(red) <= set(ppaths), 'v0.2.4: sizes agree with the files, except the declared redactions (whole table)')

tmp = Path(tempfile.mkdtemp(prefix='v023_reconstruct_'))
try:
    # ---- 1. reconstruct v0.2.3 ----
    T = tmp / 'repo'
    shutil.copytree(R, T, ignore=shutil.ignore_patterns('.git'), symlinks=True)
    for p, x in bc.items():
        (T / p).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(R / x['path'], T / p)
    for p in added:
        (T / p).unlink()
    require(all((T / q).is_file() and sha(T / q) == h for q, h in v023.items()), 'v0.2.4: the reconstruction has every v0.2.3 file with its v0.2.3 hash')
    require(not any((T / p).exists() for p in added), 'v0.2.4: no v0.2.4 addition remains in the reconstruction')
    # ---- 2. the v0.2.3 checker, unchanged, on the reconstruction ----
    require(sha(T / 'tools/verify_patch_release.py') == REC['v023_checker_sha256'], 'v0.2.4: reconstructed checker is the v0.2.3 checker, byte-identical')
    r = subprocess.run([sys.executable, '-B', str(T / 'tools/verify_patch_release.py')], capture_output=True, text=True, cwd=T)
    old_ok = r.returncode == 0 and 'A4_TRANSITION_PASS' in r.stdout and 'PATCH_RECHECK_PASS' in r.stdout
    if not old_ok:
        print(r.stdout[-1500:] + r.stderr[-1500:])
    require(old_ok, 'v0.2.4: the v0.2.3 checker passes on the reconstructed v0.2.3 tree (A4 and every earlier binding)')
    # ---- 3. the v0.2.4 delta against the v0.2.3 view ----
    bdoc = json.loads((T / 'claims/claims.json').read_text()); cdoc = json.loads((R / 'claims/claims.json').read_text())
    bcl = {c['id']: c for c in bdoc['claims']}; ccl = {c['id']: c for c in cdoc['claims']}
    delta = REC['claim_delta']
    require(list(bcl) == list(ccl) and {k: v for k, v in bdoc.items() if k != 'claims'} == {k: v for k, v in cdoc.items() if k != 'claims'},
            'v0.2.4: same claims, same order')
    ok = True
    for i in ccl:
        if i not in delta:
            ok &= ccl[i] == bcl[i]
            continue
        exp = dict(bcl[i])
        for f, x in delta[i].items():
            ok &= bcl[i].get(f) == x['before']
            exp[f] = x['after']
        ok &= ccl[i] == exp
    require(ok, 'v0.2.4: claims.json equals v0.2.3 plus exactly the declared field changes (' + ', '.join(delta) + ')')
    for p, edits in REC['text_edits'].items():
        s = (T / p).read_text()
        for e in edits:
            require(s.count(e['old']) == 1, f'v0.2.4: edit anchor occurs exactly once in v0.2.3 {p}')
            s = s.replace(e['old'], e['new'])
        require((R / p).read_text() == s, f'v0.2.4: {p} equals v0.2.3 plus exactly the declared edits')
    bp = (T / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'v0.2.4: every v0.2.3 provenance row preserved byte for byte, in order')
    decl = json.loads((R / REC['evidence']['declared']['path']).read_text())
    tlog0 = json.loads((R / REC['evidence']['transition_log']['path']).read_text())
    dpaths = [a['release_path'] for a in decl['additions']]
    want = {a['release_path']: a for a in decl['additions']}
    require(len(dpaths) == len(set(dpaths)) and len(tlog0['appended']) == len(set(tlog0['appended'])) and set(tlog0['appended']) == set(dpaths),
            'v0.2.4: the declaration and the logged append list name the same paths, each exactly once')
    require(all(a['disposition'] == 'admitted_unmasked' for a in decl['additions']), 'v0.2.4: every declared addition is admitted unmasked')
    expect = ['\t'.join([p, want[p]['original_path'], want[p]['sha256'], str(want[p]['bytes']), 'extra', '', '', '', want[p]['sha256']])
              for p in tlog0['appended']]
    require(cp[len(bp) - 1:-1] == expect, 'v0.2.4: the appended provenance rows are exactly one row per declared addition, in logged order, with exact content')
    require({p for p in added if p.startswith('evidence/')} == set(dpaths), 'v0.2.4: the added evidence files are exactly the declared additions')
    require(all((R / 'evidence' / n).read_bytes() == (T / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')),
            'v0.2.4: exclusion and redaction tables unchanged')
    require(all(sha(R / a) == want[a]['sha256'] for a in want), 'v0.2.4: declared evidence files present with their hashes')
finally:
    shutil.rmtree(tmp, ignore_errors=True)

ev = REC['evidence']
require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'transition_log')), 'v0.2.4: evidence declaration and transition log bound')
tlog = json.loads((R / ev['transition_log']['path']).read_text())
require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}, 'v0.2.4: transition log matches the current tables')
bound = set(REC['current_bindings'])
require(bound == (changed | added) - {'MANIFEST.sha256', REC_PATH} and all(sha(R / p) == h for p, h in REC['current_bindings'].items()),
        'v0.2.4: every changed or added file (except the manifest and this record) bound to its v0.2.4 bytes')
for gen in ('build_index.py', 'build_brief.py'):
    g = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
    require(g.returncode == 0, 'v0.2.4: generated output current: ' + gen)
for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
    require(not ((changed | added) & set(json.loads((R / 'review' / name).read_text())['files'])), 'v0.2.4: no edited path among the non-redirectable ' + name)
print('V024_TRANSITION_PASS: v0.2.3 reconstructed and its checker passes; the v0.2.4 delta is exactly the declared one')
