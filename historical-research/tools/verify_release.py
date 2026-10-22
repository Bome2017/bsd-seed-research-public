#!/usr/bin/env python3
"""Verify this release. Python 3 standard library only; it never writes inside evidence/.

  python3 tools/verify_release.py            hashes, index consistency and the fast replays (about a minute)
  python3 tools/verify_release.py --lean     additionally replays the Lean core (needs a Lean 4.32.2 + Mathlib v4.32.2
                                             project; set LEAN_PROJECT to its directory, default ~/proximity-prize)
  python3 tools/verify_release.py --record   also writes review/VERIFICATION_RUN.md

Checks:
  1. every file listed in evidence/PROVENANCE.tsv exists and has the recorded sha256;
  2. every evidence item of claims/claims.json is listed there with the same sha256;
  3. replays: exact curve data; the certified Mazur-Tate coefficients from the certified symbol tables; the independent
     2243-adic height certificate (in a temporary copy); the exact F_2243 rank computation of the compression
     obstruction; the Atkin-Lehner pairing on the certified m = 27, 81 tables.
Nothing here reruns a large certificate: those need the coefficient corpus (data/LARGE_DATA.md).
"""
import hashlib, io, json, os, shutil, subprocess, sys, tempfile, time, contextlib
from pathlib import Path

REL = Path(__file__).resolve().parent.parent
EV = REL / 'evidence' / 'src'
results = []
if sys.flags.optimize:
    raise SystemExit("Verification requires assertions enabled (no -O / PYTHONOPTIMIZE).")


def record(name, ok, detail=''):
    results.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}{('  -- ' + detail) if detail else ''}", flush=True)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def run(cmd, cwd=None, timeout=600):
    t = time.time()
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout + r.stderr, time.time() - t


# 1. evidence hashes
rows = [l.split('\t') for l in (REL / 'evidence' / 'PROVENANCE.tsv').read_text().splitlines()[1:]]
bad = [r[0] for r in rows if not (REL / r[0]).is_file() or sha(REL / r[0]) != r[2]]
record(f'evidence hashes ({len(rows)} files)', not bad, f'{len(bad)} mismatches: {bad[:3]}' if bad else '')
prov = {r[0]: r[2] for r in rows}

# 2. claim index consistency
claims = json.loads((REL / 'claims' / 'claims.json').read_text())['claims']
mism = [(c['id'], ev['path']) for c in claims for ev in c['evidence'] if prov.get(ev['path']) != ev.get('sha256')]
record(f'claim evidence bound to provenance ({sum(len(c["evidence"]) for c in claims)} items, {len(claims)} claims)', not mism, str(mism[:3]) if mism else '')

# Regeneration and graph checks are distinct from evidence hash agreement.
for generator in ('build_index.py', 'build_brief.py'):
    code, out, dt = run([sys.executable, '-B', str(REL / 'tools' / generator), '--check'])
    record('generated consistency: ' + generator, code == 0, out[-250:].strip())
import re
paper_ids = set()
for tex in (REL / 'paper').rglob('*.tex'):
    paper_ids.update(re.findall(r'\\cid\{([^{}]+)\}', tex.read_text()))
known_ids = {c['id'] for c in claims}
record('manuscript claim IDs resolve (not a semantic proof check)', not (paper_ids-known_ids), str(sorted(paper_ids-known_ids)))
review_maps = [REL / 'review' / name for name in ('REVIEW_BINDINGS.json', 'SECOND_REVIEW_BINDINGS.json')]
bad_review = []
for review_bindings in review_maps:
    if not review_bindings.exists():
        bad_review.append(str(review_bindings.relative_to(REL)))
        continue
    if review_bindings.exists():
        rb = json.loads(review_bindings.read_text())
        bad_review += [p for p,h in rb['files'].items() if not (REL/p).is_file() or sha(REL/p)!=h]
record('review replay bindings', not bad_review, str(bad_review[:3]) if bad_review else '')

# 3a. exact curve data and 3b. coefficients from certified symbols
for script in ('curve_invariants.py', 'coefficients_from_symbols.py', 'coefficient_verifier_regression.py', 'lattice_local_checks.py', 'archive_privacy_regression.py', 'receipt_join.py'):
    code, out, dt = run([sys.executable, '-B', str(REL / 'tools' / 'replay' / script)])
    record(f'replay {script}', code == 0 and 'ALL PASS' in out, f'{dt:.1f} s')

code, out, dt = run([sys.executable, '-B', str(REL / 'tools/replay/lattice_local_checks.py'), '--inject-failure'])
record('lattice-local failure control is rejected', code == 1 and 'CHECK_FAILED: intentional negative control' in out and 'ALL PASS' not in out)

# Independent paper-review arithmetic is a consistency replay, not an analytic certificate.
with tempfile.TemporaryDirectory() as tmp:
    dst = Path(tmp) / 'checks.json'
    code, out, dt = run([sys.executable, '-B', str(REL / 'review/pro_report/independent_checks.py'), str(dst)])
    same = dst.exists() and dst.read_bytes() == (REL / 'review/pro_report/independent_checks.json').read_bytes()
    record('paper-review exact arithmetic consistency replay', code == 0 and same, f'{dt:.1f} s; no large numerical certificate replay')

# 3c. independent 2243-adic height certificate, in a temporary copy (the certificate folder is never written)
d5 = EV / 'BSD_2243_D5_INDEPENDENT_2026-09-23'
with tempfile.TemporaryDirectory() as tmp:
    cp = Path(tmp) / 'd5'
    shutil.copytree(d5, cp)
    code, out, dt = run([sys.executable, '-B', str(cp / 'certify_d5.py'), '--digits', '7', '--output', str(Path(tmp) / 'replay.json')], cwd=tmp)
    ok = code == 0
    if ok:
        got = json.loads((Path(tmp) / 'replay.json').read_text())
        ref = json.loads((d5 / 'CERTIFICATE.json').read_text())
        keys = ['height_matrix_divided_by_p_mod_p', 'determinant_divided_by_p2_mod_p', 'regulator_valuation']
        ok = all(got[k] == ref[k] for k in keys)
        detail = f"det/p^2 = {got['determinant_divided_by_p2_mod_p']} mod 2243, valuation {got['regulator_valuation']}; {dt:.1f} s"
    else:
        detail = out[-300:]
    record('replay 2243-adic height certificate (certify_d5.py)', ok, detail)
    # Never mistake an imported old success file for fresh verifier output.
    (cp / 'VERIFICATION.json').unlink(missing_ok=True)
    code, out, dt = run([sys.executable, '-B', str(cp / 'verify_d5.py')], cwd=tmp)
    ver = json.loads((cp / 'VERIFICATION.json').read_text()) if (cp / 'VERIFICATION.json').exists() else {}
    record('replay 2243-adic height verifier (verify_d5.py)', code == 0 and ver.get('verdict') == 'ALL_CHECKS_PASS', f"verdict {ver.get('verdict')}; {dt:.1f} s")

# 3d. exact rank computation behind the compression obstruction
cmpd = EV / 'BSD_2243_COMPRESSION_ATTEMPT_2026-09-23' / 'checks'
with tempfile.TemporaryDirectory() as tmp:
    shutil.copy(cmpd / 'p2243_relation_rank.py', tmp)
    code, out, dt = run([sys.executable, '-B', str(Path(tmp) / 'p2243_relation_rank.py')], cwd=tmp)
    ref = (cmpd / 'p2243_relation_rank.txt').read_text()
    key = [l for l in ref.splitlines() if l.startswith('rank{c0,c1,c2}')]
    record('replay F_2243 relation rank (compression obstruction)', code == 0 and key and key[0] in out, f'{dt:.1f} s')

# 3e. Atkin-Lehner pairing on the certified p = 3 tables (the script's data path is redirected to the released copy)
src = (cmpd / 'check_wq_pairing.py').read_text().replace(
    "R = '/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run'",
    f"R = {str(EV / 'BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19' / 'run')!r}")
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(src, 'check_wq_pairing.py', 'exec'), {'__name__': '__main__'})
out = buf.getvalue()
ref = (cmpd / 'check_wq_pairing.txt').read_text()
record('replay W_Q pairing on certified m = 27, 81 tables', out.strip() == ref.strip())

# optional: Lean core of the supersingular bridge
if '--lean' in sys.argv:
    proj = Path(os.environ.get('LEAN_PROJECT', str(Path.home() / 'proximity-prize')))
    lean = EV / 'BSD_A3_LEAN_CORE_2026-09-22' / 'A3Core.lean'
    if (proj / 'lakefile.toml').exists() or (proj / 'lakefile.lean').exists():
        version_code, version, _ = run(['lake', 'env', 'lean', '--version'], cwd=proj)
        mf = json.loads((proj / 'lake-manifest.json').read_text())
        mathlib = next(x for x in mf['packages'] if x['name'] == 'mathlib')
        pinned = version_code == 0 and '4.32.2' in version and mathlib.get('rev') == '905b95818eb32af7874a58b427f50c1711a5e96c'
        record('Lean and Mathlib pinned versions', pinned, version.strip())
        code, out, dt = run(['lake', 'env', 'lean', str(lean)], cwd=proj, timeout=1800)
        ref = (EV / 'BSD_A3_LEAN_CORE_2026-09-22' / 'build6.log').read_text()
        same = out.strip() == ref.strip()
        record('Lean replay A3Core.lean (output identical to the recorded build6.log: 11 theorems, axioms propext/Classical.choice/Quot.sound only)',
               code == 0 and same and 'sorry' not in out, f'{dt:.0f} s')
    else:
        record('Lean replay A3Core.lean', False, f'no Lean project at {proj}')

n_ok = sum(1 for _, ok, _ in results if ok)
print(f'\n{n_ok}/{len(results)} checks passed')
if '--record' in sys.argv:
    lines = ['# Verification run', '', f'Run at {time.strftime("%Y-%m-%d %H:%M:%S %Z")} with `python3 tools/verify_release.py {" ".join(sys.argv[1:])}`.', '',
             '| check | result | detail |', '|---|---|---|']
    lines += [f'| {n} | {"PASS" if ok else "FAIL"} | {d} |' for n, ok, d in results]
    lines += ['', f'{n_ok}/{len(results)} checks passed.']
    (REL / 'review').mkdir(exist_ok=True)
    (REL / 'review' / 'VERIFICATION_RUN.md').write_text('\n'.join(lines) + '\n')
sys.exit(0 if n_ok == len(results) else 1)
