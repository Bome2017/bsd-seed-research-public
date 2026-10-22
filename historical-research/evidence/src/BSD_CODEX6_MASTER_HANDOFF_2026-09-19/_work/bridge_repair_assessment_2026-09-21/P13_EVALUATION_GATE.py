#!/usr/bin/env python3
"""Prepare the exact C13 formula and cutoff; never start a coefficient run."""
from pathlib import Path
from math import comb
import hashlib
import json
import os
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CORE = Path('/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19')
P11 = ROOT / '_work/active_full_bsd/p11'
binding = json.loads((P11 / 'CERTIFICATE_BINDINGS.json').read_text())
for item in binding['engine_files']:
    assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest() == item['sha256']

p, ap = 13, -4
m = p*p
weights = {b: pow(ap, -2, p) * comb(-((pow(b, p-1, m)-1)//p) % p, 2) % p
           for b in range(1, m) if b % p}
omega = {a: pow(a, p, m) for a in range(1, p)}
independent = {omega[a]*pow(1+p, j, m) % m: pow(ap, -2, p)*comb(j, 2) % p
               for a in omega for j in range(p)}
assert weights == independent and len(weights) == 156
folded = {b: (weights[b] + weights[m-b]) % p
          for b in weights if b < m-b and (weights[b]+weights[m-b]) % p}
groups = {a: [b for b in folded if folded[b] == a] for a in sorted(set(folded.values()))}
assert len(folded) == 66
assert sum(comb(j, 2) for j in range(p)) == 286
env = os.environ.copy()
env['DYLD_LIBRARY_PATH'] = '/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4/Odarwin-x86_64'
cutoffs = []
for modulus in (169, 13):
    command = [str(CORE/'src/arbcore'), 'tmin', '0', '-22735', '0', '106272484', '0',
               str(modulus), '6503188012738584', '1024']
    output = subprocess.run(command, env=env, text=True, capture_output=True, check=True).stdout
    tmin = int(next(line.split()[1] for line in output.splitlines() if line.startswith('TMIN ')))
    count = (tmin + 2**24) // 2**24
    cutoffs.append({'modulus': modulus, 'command': command, 'arb_output': output,
                    'tmin': tmin, 'rounded_cutoff': count*2**24-1, 'total_segments': count,
                    'reused_segments_available': min(count, len(binding['segments'])),
                    'new_segments_required': max(0, count-len(binding['segments']))})
answer = {
    'status': 'THEOREM_AND_CUTOFF_GATE_PASS_NO_ARITHMETIC_RUN',
    'p': p, 'a_p': ap, 'point_count': 18,
    'alpha_mod_13': 9, 'alpha_inverse_square_mod_13': 9,
    'interpolation_factor_mod_13': 4, 'formal_group_multiplier': 36,
    'lower_level_quadratic_sum': 286, 'nonzero_folded_symbols': len(folded),
    'predeclared_folded_groups': groups, 'two_exact_weight_derivations_agree': True,
    'cutoffs': cutoffs, 'engine_identities_checked': binding['engine_files'],
    'retained_C11_bindings_sha256': hashlib.sha256((P11/'CERTIFICATE_BINDINGS.json').read_bytes()).hexdigest(),
    'free_disk_bytes_at_gate': shutil.disk_usage(ROOT).free,
    'full_coefficient_corpus_rehashed_in_this_gate': False,
    'new_coefficient_generation_started': False,
    'modular_symbol_sum_started': False,
    'runtime_benchmark_for_C13': None,
    'memory_choice': 'existing table-free engine; no T-sized coefficient table',
    'conclusion': 'Nonzero C13 would imply seed 13-primary vanishing with retained qualifications; zero is inconclusive. No uniform-tail claim.',
}
(HERE/'P13_EVALUATION_GATE.json').write_text(json.dumps(answer, indent=2)+'\n')
print(json.dumps({k:answer[k] for k in ['status','nonzero_folded_symbols','two_exact_weight_derivations_agree']}, indent=2))
for c in cutoffs:
    print(json.dumps({k:c[k] for k in ['modulus','rounded_cutoff','total_segments','reused_segments_available','new_segments_required']}))
