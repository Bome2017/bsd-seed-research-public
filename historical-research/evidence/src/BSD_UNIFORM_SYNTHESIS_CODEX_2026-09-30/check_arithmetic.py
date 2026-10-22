"""Small exact sanity checks; these do not certify imported arithmetic theorems."""
import json
from pathlib import Path

a1, a2, a3, a4, a6 = 0, -1, 0, -66020924, -65074271436
b2 = a1*a1 + 4*a2
b4 = 2*a4 + a1*a3
b6 = a3*a3 + 4*a6
b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
c4 = b2*b2 - 24*b4
delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
assert 2**3*3*2243*4547**2*5843 == 6503188012738584
assert delta % 2243 == 0 and delta % 2243**2 != 0
assert c4 % 2243 == 2005
saved = json.loads(Path(__file__).with_name('SEED_LOCAL_CHECK.json').read_text())
assert (delta, c4) == (saved['delta'], saved['c4'])

def fitting_valuation(rank, exponents, index):
    """Z_p^rank plus cyclic p-power factors. None denotes the zero ideal."""
    if index < rank:
        return None
    count = len(exponents)
    selected = max(0, rank + count - index)
    return sum(sorted(exponents)[:selected])

assert [fitting_valuation(2, [1,1], i) for i in (2,3,4)] == [2,1,0]
assert fitting_valuation(4, [], 2) is None
assert fitting_valuation(4, [], 4) == 0
cases = 0
for rank in (2,4,6):
    for paired_exponents in ([], [1,1], [2,2], [1,1,3,3]):
        d = rank + len(paired_exponents)
        first_even_unit = next(i for i in range(0,d+2,2)
                              if fitting_valuation(rank,paired_exponents,i) == 0)
        assert first_even_unit == d
        cases += 1
print(json.dumps({'local_2243':'PASS', 'fitting_module_cases':cases,
                  'finite_and_divisible_excess_controls':'PASS',
                  'scope':'integer arithmetic and abstract modules only'}, indent=2))
