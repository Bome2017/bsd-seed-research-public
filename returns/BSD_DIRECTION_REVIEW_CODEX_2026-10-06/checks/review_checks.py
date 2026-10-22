"""Independent bounded arithmetic and custody controls; no Sha computation."""
import hashlib
import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--arithmetic-only', action='store_true')
parser.add_argument('--output', type=Path, default=ROOT/'checks/REPLAY_RESULTS.json')
args = parser.parse_args()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))

def factors(n):
    out = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out

def count(q):
    # Independently use the minimal model, not the submitted original model.
    squares = {y*y % q for y in range(1, q)}
    total = 1
    for x in range(q):
        rhs = (x*x*x - x*x - 66020924*x - 65074271436) % q
        total += 1 if rhs == 0 else 2 if rhs in squares else 0
    return total

manifests = []
for lane in (() if args.arithmetic_only else ('heegner', 'coinvariant')):
    base = ROOT / 'input' / lane
    for mf in sorted(base.rglob('MANIFEST.sha256')):
        relative = str(mf.relative_to(base))
        # The current Heegner return manifest explicitly uses project-relative names.
        # Archived task manifests are historical receipts, not current archive manifests.
        if (lane == 'heegner' and relative == 'historical_task/MANIFEST.sha256') or (lane == 'coinvariant' and relative.startswith('input/')):
            manifests.append({'manifest': str(mf.relative_to(ROOT)), 'count': 0, 'matched': 0,
                              'failures': [], 'role': 'historical_receipt_not_revalidated'})
            continue
        manifest_root = base if lane == 'heegner' and relative == 'research_return/MANIFEST.sha256' else mf.parent
        rows = []
        for line in mf.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            digest, rel = line.split(maxsplit=1)
            rel = rel.lstrip('*')
            path = (manifest_root / rel).resolve()
            if not path.is_relative_to(base.resolve()):
                rows.append({'path': rel, 'status': 'unsafe_path'})
            elif not path.is_file():
                rows.append({'path': rel, 'status': 'missing'})
            else:
                actual = sha(path)
                rows.append({'path': rel, 'status': 'match' if actual == digest else 'mismatch',
                             'expected': digest, 'actual': actual})
        manifests.append({'manifest': str(mf.relative_to(ROOT)), 'root': str(manifest_root.relative_to(ROOT)), 'count': len(rows),
                          'matched': sum(r['status'] == 'match' for r in rows),
                          'failures': [r for r in rows if r['status'] != 'match']})

table = json.loads((ROOT/'input/heegner/research_return/checks/supersingular_inert_100000.out.json').read_text())
aux = []
for row in table['primes']:
    q = row['l']
    n = count(q)
    fs = factors(q+1)
    result = {'ell': q, 'prime': prime(q), 'inert': pow(-23 % q, (q-1)//2, q) == q-1,
              'points': n, 'a_ell': q+1-n, 'factors': fs,
              'factorization_matches': fs == row['l_plus_1_factors']}
    assert result['prime'] and result['inert'] and result['a_ell'] == 0 and result['factorization_matches']
    aux.append(result)

# Exact group-ring coefficient identity in Z[C_m].
identities = []
for m in range(2, 101):
    d = list(range(m))
    lhs = [d[(i-1) % m] - d[i] for i in range(m)]
    rhs = [m-1] + [-1]*(m-1)
    assert lhs == rhs
    identities.append(m)

# Arithmetic countercontrol, not a claimed Heegner-point example.
prime_power_bug = {'m': 50, 'failed_prime': 5, 'squarefree_failure_index': 5,
                   'old_quotient': 10, 'wrongly_retains_failed_prime': 10 % 5 == 0,
                   'correct_radical_quotient': 2}
assert prime_power_bug['wrongly_retains_failed_prime']

# h=2+s-epsilon with even s gives h<=2 iff s=0, independently of MW localization.
dimension_cases = []
for s in range(0, 22, 2):
    for epsilon in (0, 1):
        h = 2+s-epsilon
        assert (h <= 2) == (s == 0)
        dimension_cases.append({'sha_dimension': s, 'local_image_dimension': epsilon, 'h': h})

result = {'manifest_checks': manifests, 'auxiliaries_recounted': aux,
          'auxiliary_count': len(aux), 'group_ring_identities': identities,
          'prime_power_countercontrol': prime_power_bug, 'dimension_controls': dimension_cases,
          'ordinary_spot_checks': [{'p': p, 'a_p': p+1-count(p)} for p in (31, 47, 53, 331)],
          'scope': 'Manifest identity and finite arithmetic only. No derived Heegner point, Kato value, class group, or Sha computation.'}
result['unmanifested_coinvariant_continuation'] = [
    {'path': rel, 'sha256': sha(ROOT/'input/coinvariant'/rel)}
    for rel in ('COINVARIANT_DESCENT.md', 'Coinvariant/Descent.lean')]
args.output.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'auxiliaries': len(aux), 'manifests': [
    {'path': m['manifest'], 'matched': m['matched'], 'count': m['count'], 'failures': m['failures']}
    for m in manifests], 'ordinary_spot_checks': result['ordinary_spot_checks']}, indent=2))
