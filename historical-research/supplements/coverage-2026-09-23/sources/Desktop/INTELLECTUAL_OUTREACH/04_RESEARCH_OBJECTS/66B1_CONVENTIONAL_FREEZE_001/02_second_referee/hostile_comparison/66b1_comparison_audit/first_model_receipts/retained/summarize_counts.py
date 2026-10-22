"""Recheck the independent CSV and print exact family/control summaries."""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / 'independent_counts.csv').open(newline='') as stream:
    rows = [{key: int(value) for key, value in row.items()}
            for row in csv.DictReader(stream)]
errors = defaultdict(list)
unsigned, signed = defaultdict(Counter), defaultdict(Counter)
family = []
for r in rows:
    p, n = r['p'], r['N_min']
    if n != r['N_descent']:
        errors['model_count'].append(p)
    if ((r['chi_neg2'], r['chi33']) == (-1, -1)) != (r['v2'] == 2):
        errors['signed_character_criterion'].append(p)
    if r['chi33'] != r['q_over3'] * r['q_over11']:
        errors['reciprocity'].append(p)
    f = p % 8 == 5 and r['q_over3'] == -1 and r['q_over11'] == 1
    if int(f) != r['family']:
        errors['family_flag'].append(p)
    if f:
        family.append(r)
        if r['v2'] != 2:
            errors['family_valuation'].append(p)
        if r['trace'] % 8 != 2:
            errors['family_trace'].append(p)
    unsigned[str((r['chi2'], r['chi33']))][r['v2']] += 1
    signed[str((r['chi_neg2'], r['chi33']))][r['v2']] += 1
out = {
    'primes_checked': len(rows),
    'family_checked': len(family),
    'family_below_4000': sum(r['p'] < 4000 for r in family),
    'unsigned_controls': {k: dict(sorted(v.items())) for k, v in unsigned.items()},
    'signed_controls': {k: dict(sorted(v.items())) for k, v in signed.items()},
    'exceptions': dict(errors),
    'first_family': family[0] if family else None,
    'last_family': family[-1] if family else None,
}
(root / 'verification_summary.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
if errors:
    raise SystemExit(1)
