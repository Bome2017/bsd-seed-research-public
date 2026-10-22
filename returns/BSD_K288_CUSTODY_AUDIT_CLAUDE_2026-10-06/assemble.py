#!/usr/bin/env python3
"""K288 custody audit, part 3: w(p,l) = c2 / ((a_l - 2) * R(p,l)) mod p for the nine certified runs (Claude, 2026-10-06).

Inputs: c2_from_symbols.json (part 1, certified symbols) and tamereg_audit.out (part 2, fresh tame regulator).
Checks, per (p, l):
  (i)   a_l - 2 == -#E(F_l) mod p (the two written forms of the Euler factor agree because l == 1 mod p);
  (ii)  w is the same for the least and the second-least primitive root (c2 recomputed from the symbols for both);
  (iii) w == 288 mod p.
Then the nine residues are combined by CRT and by rational reconstruction.
Output: K288_AUDIT.json
"""
import json, math, pathlib, re
from fractions import Fraction

HERE = pathlib.Path(__file__).parent
RUNS = pathlib.Path('/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/seed_runs')
c2rows = {(r['p'], r['l']): r for r in json.load(open(HERE / 'c2_from_symbols.json'))}


def symbols(run, l):
    sym = {}
    for line in open(RUNS / run / 'msl.txt'):
        if line.startswith('XB '):
            t = line.split(); k = t.index('cand')
            num, den = t[k + 1].split('/'); assert den == '1024'
            sym[int(t[1])] = Fraction(int(num), 1024)
    return sym


def c2_for(run, p, l, g):
    sym, ind, x = symbols(run, l), {}, 1
    for e in range(l - 1):
        ind[x] = e; x = x * g % l
    c1 = sum((ind[a] % p) * sym[a] for a in sym); c2 = sum(math.comb(ind[a] % p, 2) * sym[a] for a in sym)
    assert c1.denominator == 1 and c2.denominator == 1 and int(c1) % p == 0
    return int(c2)


rows = []
for line in open(HERE / 'tamereg_audit.out'):
    m = re.match(r'ROW p=(\d+) l=(\d+) #E\(F_l\)=(\d+) a_l=(-?\d+) M=(\d+) data=(.*)$', line.strip())
    if not m:
        continue
    p, l, Nl, al, M = map(int, m.groups()[:5])
    data = json.loads(m.group(6))
    r1 = c2rows[(p, l)]
    assert (al - 2) % p == (-Nl) % p, f'(i) fails at {p},{l}'
    ws = []
    for g, h1, h2, b12, dM, dE in data:
        c2 = c2_for(r1['run'], p, l, g)
        if g == r1['g']:
            assert c2 == r1['c2'], 'c2 differs from part 1'
        assert dE % p != 0, f'R = 0 at {p},{l},g={g}'
        ws.append((g, c2, dE, c2 * pow((al - 2) * dE, -1, p) % p))
    w = ws[0][3]
    rows.append({'p': p, 'l': l, 'run': r1['run'], '#E(F_l)': Nl, 'a_l': al, 'M': M,
                 'g': ws[0][0], 'c2': ws[0][1], 'c2_mod_p': ws[0][1] % p, 'R': ws[0][2],
                 'w': w, '288_mod_p': 288 % p, 'w_is_288': w == 288 % p,
                 'second_generator': {'g': ws[1][0], 'c2_mod_p': ws[1][1] % p, 'R': ws[1][2], 'w': ws[1][3]},
                 'generator_invariant': ws[0][3] == ws[1][3]})
    print(f"p={p:2d} l={l:3d} a_l={al:4d} #E={Nl:3d} g={ws[0][0]:2d} c2={ws[0][1] % p:2d} R={ws[0][2]:2d} "
          f"w={w:2d} 288 mod p={288 % p:2d} {'OK' if w == 288 % p else 'MISMATCH'}   g'={ws[1][0]:2d}: w={ws[1][3]:2d}")

assert len(rows) == 9
Mod = math.prod(r['p'] for r in rows)
W = 0
for r in rows:
    Mi = Mod // r['p']; W = (W + r['w'] * Mi * pow(Mi, -1, r['p'])) % Mod


def ratrec(x, m):
    """Least-height a/b == x mod m (half-extended Euclid; Wang's bound sqrt(m/2))."""
    bound = math.isqrt(m // 2); r0, r1, s0, s1 = m, x % m, 0, 1
    while r1 > bound:
        q = r0 // r1; r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
    return (r1, s1) if abs(s1) <= bound and math.gcd(r1, abs(s1)) == 1 else None


rr = ratrec(W, Mod)
summary = {'modulus': Mod, 'crt_value': W, 'rational_reconstruction': rr, 'wang_bound': math.isqrt(Mod // 2),
           'all_nine_w_eq_288': all(r['w_is_288'] for r in rows), 'all_generator_invariant': all(r['generator_invariant'] for r in rows)}
print(json.dumps(summary))
json.dump({'rows': rows, 'summary': summary}, open(HERE / 'K288_AUDIT.json', 'w'), indent=1)
