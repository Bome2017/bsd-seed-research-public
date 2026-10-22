#!/usr/bin/env python3
"""Bounded patch/integrity checks, with exact rational outward rounding.

No historical research code is executed. Does not replay a large certificate.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, json, re, subprocess, sys

R = Path(__file__).resolve().parent.parent
editorial_path = R / 'review/EDITORIAL_PATCH_APPLIED.json'
editorial = json.loads(editorial_path.read_text()) if editorial_path.exists() else None
def prior_path(p):
    # These bindings belong to the previous review. Preserve their exact bytes.
    if editorial and p in editorial['historical_v021_files']:
        return R / editorial['historical_v021_files'][p]['path']
    return R / p
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
a4_path = R / 'review/A4_FORMAL_CHECK_APPLIED.json'
a4 = json.loads(a4_path.read_text()) if a4_path.exists() else None
A4_REDIRECT = a4['historical_bindings'] if a4 else {}
def v022_path(p):
    # v0.2.3 (A4 formal check) changed these paths. Their earlier bindings are still checked, against the preserved
    # v0.2.2 bytes; the new bytes are bound separately by the A4 transition record (checked at the end).
    return R / A4_REDIRECT[p]['path'] if p in A4_REDIRECT else R / p
BREAK_UNCHANGED = {'claims/claims.json', 'claims/CLAIM_INDEX.md', 'evidence/PROVENANCE.tsv'}
def require(ok, message):
    if not ok: raise SystemExit('FAIL: ' + message)
    print('PASS: ' + message)
def manifest(root, name):
    rows = []
    for line in (root / name).read_text().splitlines():
        h, rel = line.split('  ', 1)
        p = Path(rel)
        require(not p.is_absolute() and '..' not in p.parts, 'safe manifest path') if (p.is_absolute() or '..' in p.parts) else None
        rows.append((h, rel))
    require(len({p for _, p in rows}) == len(rows), name + ' has unique paths')
    bad = [p for h, p in rows if not (root / p).is_file() or (root / p).is_symlink() or sha(root / p) != h]
    require(not bad, str(root.relative_to(R)) + '/' + name + ': all ' + str(len(rows)) + ' hashes agree')

binding = json.loads((R / 'review/PATCH_REVIEW_BINDINGS.json').read_text())
bad = [p for p, h in binding['files'].items() if not prior_path(p).is_file() or sha(prior_path(p)) != h]
require(not bad, 'v0.2.1 patch bindings, with explicitly preserved historical files')
applied = json.loads((R / 'review/PATCH_APPLIED.json').read_text())
if a4:
    require(set(A4_REDIRECT) & set(applied['unchanged']) == BREAK_UNCHANGED, 'A4: exactly three v0.2.1 unchanged-bindings answered by v0.2.2 history')
require(all(sha(v022_path(p)) == h for p, h in applied['unchanged'].items()), 'claim index, evidence provenance and retained verifier unchanged' + (' (v0.2.2 bytes; A4 delta checked below)' if a4 else ''))
require(all(sha(prior_path(p)) == x['after'] for p, x in applied['mathematical_source_edits'].items()), 'v0.2.1 patched sources match their historical checked candidate')
hist = R / 'review/history/v0.2.0'
old = json.loads((hist / 'SECOND_REVIEW_BINDINGS.json').read_text())
new = json.loads((R / 'review/SECOND_REVIEW_BINDINGS.json').read_text())
expected = dict(old['files'])
expected['review/history/v0.2.0/SHARING.md'] = expected.pop('SHARING.md')
require(new['files'] == expected and sha(hist / 'SHARING.md') == old['files']['SHARING.md'], 'historical review redirect preserves old bytes and all other bindings')

a = R / 'review/pro6_v020'
manifest(a, 'AUDIT_FILES.sha256')
inputs = json.loads((a / 'INPUTS.json').read_text())
for arc in inputs:
    name = Path(arc['archive']).name.removesuffix('.zip')
    require(all(sha(a / 'inputs' / name / x['member']) == x['sha256'] for x in arc['members']), name + ': imported report members unchanged')

check = json.loads((a / 'checks/exact_rounding_check.json').read_text())
cert = R / 'evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/ANALYTIC_RANK_CERTIFICATE.md'
require(sha(cert) == check['source_sha256'] and check['raw_dump'] in cert.read_text(), 'exact Arb dump bound to retained certificate')
m, me, r, rexp = [int(x, 16) for x in check['raw_dump'].split()]
mid, rad = m * Fraction(2) ** me, r * Fraction(2) ** rexp
display = Fraction('35.93531375275170089')
outward = Fraction('0.00570901')
require(abs(mid - display) + rad <= outward, 'displayed enclosure rounds outward including midpoint error')
require(Fraction('35.929604') <= display - outward and display + outward <= Fraction('35.941023'), 'displayed enclosure lies inside unchanged theorem interval')
tex = (R / 'paper/sections/03_rank.tex').read_text()
require(tex.count(r'5.70901\cdot10^{-3}') == 2 and r'5.709\cdot10^{-3}' not in tex, 'both printed radii corrected')
lat = (R / 'paper/sections/F_lattice_proof.tex').read_text()
require(r'\cite[Cor.~3.7]{arsmanin}' in lat and 'Their Theorem~5.15' in lat and r'\cite[Thm.~3.6(a)]{ars}' in lat, 'distinct ARS references and CNS theorem label retained correctly')

s = R / 'supplements/coverage-2026-09-23'
result = subprocess.run([sys.executable, '-B', str(s / 'verify.py')], capture_output=True, text=True)
require(result.returncode == 0 and 'SUPPLEMENT_INTEGRITY_PASS: 681 files' in result.stdout, 'coverage supplement: 681 manifest entries, integrity only')
if editorial:
    require(all(sha(R / x['path']) == x['sha256'] for x in editorial['historical_v021_files'].values()), 'preserved v0.2.1 history files')
    if a4:
        require(set(A4_REDIRECT) & set(editorial['current_bindings']) == {'README.md', 'tools/verify_patch_release.py'}, 'A4: exactly two v0.2.2 current bindings answered by v0.2.2 history')
        require(set(A4_REDIRECT) & set(editorial['unchanged']) == BREAK_UNCHANGED, 'A4: exactly three v0.2.2 unchanged-bindings answered by v0.2.2 history')
    require(all(sha(v022_path(p)) == h for p, h in editorial['current_bindings'].items()), 'v0.2.2 editorial source and navigation bindings' + (' (v0.2.2 bytes where superseded)' if a4 else ''))
    require(all(sha(v022_path(p)) == h for p, h in editorial['unchanged'].items()), 'claim grades, original evidence provenance and Lean source unchanged' + (' (v0.2.2 bytes; A4 delta checked below)' if a4 else ''))
if a4:
    # ---- v0.2.3: the A4 formal-check transition. Every new byte is bound; every delta is exact. ----
    A, HR = a4, R / a4['history_root']
    old_maps = {'PATCH_APPLIED.unchanged': applied['unchanged']}
    if editorial:
        old_maps.update({'EDITORIAL.current_bindings': editorial['current_bindings'], 'EDITORIAL.unchanged': editorial['unchanged']})
    derived = {p for d in old_maps.values() for p in d if p in A['base_copies']}
    require(set(A4_REDIRECT) == derived, 'A4: redirect set equals the edited paths bound by earlier records')
    require(all(x['path'] == A['history_root'] + '/' + p and sha(R / x['path']) == x['sha256'] and
                all(d[p] == x['sha256'] for d in old_maps.values() if p in d) for p, x in A4_REDIRECT.items()), 'A4: exact v0.2.2 preserved bytes for every redirect')
    require(all(x['path'] == A['history_root'] + '/' + p and sha(R / x['path']) == x['sha256'] for p, x in A['base_copies'].items()), 'A4: all v0.2.2 base copies intact')
    require(set(A['current_bindings']) == set(A4_REDIRECT) and all(sha(R / p) == h for p, h in A['current_bindings'].items()), 'A4: current bindings of the redirected paths (including this checker)')
    base_doc = json.loads((HR / 'claims/claims.json').read_text()); cur_doc = json.loads((R / 'claims/claims.json').read_text())
    bc, cc = {c['id']: c for c in base_doc['claims']}, {c['id']: c for c in cur_doc['claims']}
    delta = A['claim_delta']
    require(set(delta) == {'S.5', 'S.7', 'S.11', 'S.13', 'B.1'} and list(cc) == list(bc) and
            {k: v for k, v in cur_doc.items() if k != 'claims'} == {k: v for k, v in base_doc.items() if k != 'claims'}, 'A4: same claims, same order, five declared deltas')
    def expected(b, d):
        e = dict(b)
        e['grades'] = b['grades'] + d['grades_added']; e['evidence'] = b['evidence'] + d['evidence_added']
        e['qualifications'] = b['qualifications'] + d['qualifications_added']
        e['verification'] = dict(b['verification'], **d['verification_added']); e['post_master'] = d['post_master']
        return e
    require(all(cc[i] == (expected(bc[i], delta[i]) if i in delta else bc[i]) for i in cc), 'A4: claims.json equals v0.2.2 plus exactly the declared five-claim delta')
    require(all(d['grades_added'] == ['LEAN_CHECKED'] for d in delta.values()), 'A4: the only grade added is LEAN_CHECKED')
    for gen in ('build_index.py', 'build_brief.py'):
        r = subprocess.run([sys.executable, '-B', str(R / 'tools' / gen), '--check'], capture_output=True, text=True)
        require(r.returncode == 0, 'A4: generated output current: ' + gen)
    ev = A['evidence']
    require(all(sha(R / ev[k]['path']) == ev[k]['sha256'] for k in ('declared', 'tool', 'transition_log')), 'A4: transition tool, declaration and log bound')
    decl = json.loads((R / ev['declared']['path']).read_text())
    bp = (HR / 'evidence/PROVENANCE.tsv').read_text().split('\n'); cp = (R / 'evidence/PROVENANCE.tsv').read_text().split('\n')
    require(cp[:len(bp) - 1] == bp[:-1] and cp[-1] == '', 'A4: every v0.2.2 provenance row preserved byte for byte, in order')
    cols = cp[0].split('\t'); rows = [dict(zip(cols, x.split('\t'))) for x in cp[len(bp) - 1:-1]]
    want = {a['release_path']: a for a in decl['additions']}
    require(len(rows) == len(want) and all(r['release_path'] in want and r['sha256'] == r['original_sha256'] == want[r['release_path']]['sha256']
            and r['bytes'] == str(want[r['release_path']]['bytes']) and r['original_path'] == want[r['release_path']]['original_path'] for r in rows),
            'A4: exactly the declared provenance rows appended')
    require(all((R / 'evidence' / n).read_bytes() == (HR / 'evidence' / n).read_bytes() for n in ('EXCLUDED.tsv', 'REDACTIONS.tsv')), 'A4: exclusion and redaction tables unchanged')
    require(all(sha(R / a) == want[a]['sha256'] for a in want), 'A4: declared evidence files present with their declared hashes')
    tlog = json.loads((R / ev['transition_log']['path']).read_text())
    require(tlog['result_tables'] == {n: sha(R / 'evidence' / n) for n in ('PROVENANCE.tsv', 'EXCLUDED.tsv', 'REDACTIONS.tsv')}, 'A4: transition log matches the current tables')
    pe = A['paper_edit']; bt = (R / pe['base_copy']).read_text(); ct = (R / pe['path']).read_text()
    i, k = bt.find(pe['anchor']), len(ct) - len(bt)
    require(bt.count(pe['anchor']) == 1 and ct[:i] == bt[:i] and ct[i + k:] == bt[i:] and
            hashlib.sha256(ct[i:i + k].encode()).hexdigest() == pe['inserted_sha256'], 'A4: paper source = v0.2.2 plus exactly the declared remark at its anchor')
    vl = A['version_labels']; rb = (HR / 'README.md').read_text()
    require(rb.count(vl['readme_old_line']) == 1 and (R / 'README.md').read_text() == rb.replace(vl['readme_old_line'], vl['readme_new_line']), 'A4: README differs from v0.2.2 only in its version line')
    require(sha(R / 'paper/release_id.tex') == vl['release_id_sha256'] and sha(R / 'paper/seed_bsd.pdf') == A['paper_pdf_sha256'], 'A4: release identifier and rebuilt PDF bound')
    touched = set(A['base_copies']) | set(A['added_paths'])
    for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json'):
        require(not (touched & set(json.loads((R / 'review' / name).read_text())['files'])), 'A4: no edited path among the non-redirectable ' + name)
    print('A4_TRANSITION_PASS: v0.2.2 bindings hold on preserved bytes; the v0.2.3 delta is exactly the declared one')
print('PATCH_RECHECK_PASS: no new mathematical or large numerical replay claimed')
