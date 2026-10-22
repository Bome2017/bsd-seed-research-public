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
require(all(sha(R / p) == h for p, h in applied['unchanged'].items()), 'claim index, evidence provenance and retained verifier unchanged')
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
    require(all(sha(R / p) == h for p, h in editorial['current_bindings'].items()), 'v0.2.2 editorial source and navigation bindings')
    require(all(sha(R / p) == h for p, h in editorial['unchanged'].items()), 'claim grades, original evidence provenance and Lean source unchanged')
print('PATCH_RECHECK_PASS: no new mathematical or large numerical replay claimed')
