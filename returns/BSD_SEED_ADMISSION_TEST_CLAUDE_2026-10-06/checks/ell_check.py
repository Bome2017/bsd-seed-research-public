# Independent re-implementation (Claude, 10-06): ell_i mod p from the certified XB rational candidates.
# mu(a+p^2) = alpha^-2 [a/p^2]^+ - alpha^-3 [a/p]^+, alpha == a_p mod p; u(a) = ((a^(p-1) mod p^2)-1)/p * (p-1)^-1 mod p.
import re, sys
from fractions import Fraction
from math import comb
def xb(path):
    d = {}
    for line in open(path):
        m = re.match(r'XB (\d+) plus .*?cand (-?\d+)/(\d+) contains 1 unique 1', line)
        if m: d[int(m.group(1))] = Fraction(int(m.group(2)), int(m.group(3)))
    return d
def modp(x, p): return x.numerator * pow(x.denominator, -1, p) % p
p, ap = 5, -2
hi, lo = xb(sys.argv[1]), xb(sys.argv[2])
units = [a for a in range(1, p*p) if a % p]
assert sorted(hi) == units, ("missing high symbols", sorted(set(units) - set(hi)))
assert sorted(lo) == list(range(1, p)), "missing low symbols"
inv = pow(ap % p, -1, p)
def u(a): return ((pow(a, p-1, p*p) - 1)//p) * pow(p-1, -1, p) % p
for i in range(4):
    full = sum((inv**2) * modp(hi[a], p) * comb(u(a), i) - (inv**3) * modp(lo[a % p], p) * comb(u(a), i) for a in units) % p
    high = sum((inv**2) * modp(hi[a], p) * comb(u(a), i) for a in units) % p
    print(f"ell_{i} mod {p}: full-measure {full}, high-level-only {high}")
# the cancellation claim, checked on the fibres
for b in range(1, p):
    us = sorted(u(b + p*j) for j in range(p))
    assert us == list(range(p)), (b, us)
print("fibre check: for each b mod 5, u(b+5j) runs over F_5 bijectively")
