"""Separate reconstruction of all norms and private-prime eligibility.

Reads the immutable uploaded packet; does not run its norm producer.
Private support across rows is separately checked by the C/GMP direct verifier.
"""
from pathlib import Path
from math import gcd, prod
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'inputs/BSD_FIN_SOURCE_EXPERIMENTS_2026-10-21'
cs = json.loads((SRC/'inputs/seed_polynomial.json').read_text())['G_coefficients']
z, w = s.symbols('z w')
G = s.Poly.from_list(cs, z).as_expr()
disc = abs(int(s.discriminant(G.subs(z, w*w), w)))
bad = prod(s.primerange(2, 65537)) * disc
rows = json.loads((SRC/'results/combined_support_rows.json').read_text())
counts = {'rational': 0, 'quadratic': 0}
for row in rows:
    if row['kind'] == 'rational':
        a, b = row['key']
        # Homogenized Horner evaluation of degree12 G(a^2/b^2).
        n = cs[0]
        for j, c in enumerate(cs[1:], 1):
            n = n*a*a + c*pow(b, 2*j)
        n = abs(n)
    else:
        a, b, c = row['key']
        n = abs(int(s.resultant(G, (a+b*z)**2-c*c*z, z)))
    assert n == int(row['norm']), row['key']
    m = n
    while (g := gcd(m, bad)) > 1:
        m //= g
    assert m == int(row['large_unramified_norm_part']), row['key']
    private = int(row['private_norm_part'])
    assert private > 1 and m % private == 0 and gcd(private, bad) == 1
    counts[row['kind']] += 1

out = {'status':'PASS_ALL_NORMS_AND_PRIVATE_ELIGIBILITY',
       'counts': counts, 'rows':len(rows),
       'method':'homogenized integer Horner and symbolic resultants, independent of supplied norm producer',
       'scope':'Reconstructs all saved norm inputs and exclusions of small/discriminant primes. Cross-row private support is a separate exact direct-product check. Retains the field identification.'}
(ROOT/'review/PRO_NORM_RECHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
