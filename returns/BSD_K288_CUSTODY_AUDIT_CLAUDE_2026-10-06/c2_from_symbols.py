#!/usr/bin/env python3
"""K288 custody audit, part 1: c0, c1, c2 for the nine certified singleton runs, recomputed from the raw msl.txt
symbol lines (Claude, 2026-10-06; fresh code, does not import recompute_downstream.py).

Convention (SINGLETON_SPEC v1): g = least primitive root mod l; c_k = sum over a in (Z/l)^x of
binom(ind_g(a) mod p, k) * [a/l]^+, with [a/l]^+ = (plus candidate)/1024 from the certified XB line.
The symbols themselves are taken as certified by the engine run (interval identification, unique candidate);
this script re-checks the hash binding, the uniqueness flags, integrality and symmetry, then redoes the arithmetic.
Output: c2_from_symbols.json
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction

RUNS = pathlib.Path('/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/seed_runs')
NINE = [('l103', 17, 103), ('p19_l191_v2', 19, 191), ('p23_l47', 23, 47), ('p29_l233_v2', 29, 233),
        ('p31_l311', 31, 311), ('p37_l149', 37, 149), ('p41_l83', 41, 83), ('p43_l173', 43, 173),
        ('p47_l283', 47, 283)]


def least_primitive_root(l):
    qs = [q for q in range(2, l) if (l - 1) % q == 0 and all(q % d for d in range(2, math.isqrt(q) + 1))]
    return next(g for g in range(2, l) if all(pow(g, (l - 1) // q, l) != 1 for q in qs))


def parse_symbols(path, l):
    sym = {}
    for line in open(path):
        if not line.startswith('XB '):
            continue
        t = line.split()
        b = int(t[1])
        # token layout: XB b plus [mid +/- rad] cand N/1024 contains 1 unique 1 minus [...] cand M/1024 contains 1 unique 1
        i = t.index('plus'); j = t.index('minus')
        plus, minus = t[i:j], t[j:]
        for part in (plus, minus):
            k = part.index('cand')
            assert part[k + 2:k + 6] == ['contains', '1', 'unique', '1'], f'b={b}: candidate not unique: {part}'
        num, den = plus[plus.index('cand') + 1].split('/')
        assert den == '1024' and b not in sym, f'b={b}: bad denominator or duplicate'
        sym[b] = Fraction(int(num), 1024)
    assert set(sym) == {b for b in range(1, l) if math.gcd(b, l) == 1}, 'label set is not (Z/l)^x'
    return sym


out = []
for run, p, l in NINE:
    d = RUNS / run
    man = json.load(open(d / 'RUN_MANIFEST.json'))
    rep = json.load(open(d / 'SINGLETON_REPORT.json'))
    h = hashlib.sha256(open(d / 'msl.txt', 'rb').read()).hexdigest()
    assert h == man['msl_output_sha256'], f'{run}: msl.txt hash differs from RUN_MANIFEST'
    assert (man['p'], man['l']) == (p, l) and (rep['p'], rep['l']) == (p, l), f'{run}: p/l mismatch'
    assert (l - 1) % p == 0 and ((l - 1) // p) % p != 0, f'{run}: l is not 1 mod p exactly once'
    sym = parse_symbols(d / 'msl.txt', l)
    assert all(v.denominator == 1 for v in sym.values()), f'{run}: non-integral symbol'
    assert all(sym[b] == sym[l - b] for b in sym), f'{run}: [a]+ != [-a]+'
    g = least_primitive_root(l)
    ind, x = {}, 1
    for e in range(l - 1):
        ind[x] = e; x = x * g % l
    c = [sum(math.comb(ind[a] % p, k) * int(sym[a]) for a in sym) for k in range(3)]
    row = {'run': run, 'p': p, 'l': l, 'g': g, 'msl_sha256': h, 'n_symbols': len(sym), 'c0': c[0], 'c1': c[1], 'c2': c[2],
           'c0_mod_p': c[0] % p, 'c1_mod_p': c[1] % p, 'c2_mod_p': c[2] % p,
           'report_g': rep['generator'], 'report_c2': int(rep['c2']), 'report_c2_mod_p': rep['c2_mod_p'],
           'matches_report': (g, c[2], c[2] % p) == (rep['generator'], int(rep['c2']), rep['c2_mod_p'])}
    out.append(row)
    print(f"{run:12s} p={p:2d} l={l:3d} g={g:2d} c0={c[0]} c1={c[1]} (mod p {c[1] % p}) c2={c[2]} (mod p {c[2] % p})  report match: {row['matches_report']}")
json.dump(out, open(pathlib.Path(__file__).with_name('c2_from_symbols.json'), 'w'), indent=1)
bad = [r['run'] for r in out if not r['matches_report'] or r['c0'] != 0 or r['c1_mod_p'] != 0]
print('ALL NINE OK' if not bad else f'PROBLEMS: {bad}')
sys.exit(1 if bad else 0)
