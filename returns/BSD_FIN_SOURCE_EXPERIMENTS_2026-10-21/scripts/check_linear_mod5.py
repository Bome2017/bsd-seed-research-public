#!/usr/bin/env python3
"""Check a necessary private-valuation fact; only the linear mod-5 proof is claimed."""
from pathlib import Path
import json
from sympy import integer_nthroot
R = Path(__file__).resolve().parents[1]
rows = json.loads((R/'results/combined_support_rows.json').read_text())
linear = [r for r in rows if r['kind'] == 'rational']
quadratic = [r for r in rows if r['kind'] == 'quadratic']
assert len(linear) == 20180 and len(quadratic) == 260
lp = [i for i,r in enumerate(linear) if integer_nthroot(int(r['private_norm_part']),5)[1]]
qp = [i for i,r in enumerate(quadratic) if integer_nthroot(int(r['private_norm_part']),5)[1]]
assert not lp
out = {
    'status': 'PASS_LINEAR_MOD5_PRIVATE_SUPPORT',
    'linear_family_count': len(linear),
    'linear_private_parts_that_are_fifth_powers': lp,
    'quadratic_family_count': len(quadratic),
    'quadratic_private_parts_that_are_fifth_powers': qp,
    'linear_consequence': 'On the retained field/scalar inputs, the whole scalar-closed rational Cayley family has injective divisor map modulo 5, hence supplies no nonzero ordinary virtual-unit class.',
    'quadratic_qualification': 'Non-fifth-power rational norm alone does NOT certify both character projection ranks for a quadratic factor; no analogous mod-5 conclusion is asserted for these 260.'
}
text=json.dumps(out,indent=2)+'\n'
(R/'results/LINEAR_MOD5_CHECK.json').write_text(text)
print(text)
