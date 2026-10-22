# Exact check on the Sage/eclib reference symbols of the operator relations used as run-internal consistency checks:
#   p | N (U_p):  a_p [r] = sum_{j<p} [(r+j)/p]            (p = 3, 3 || N)
#   p !| N (T_p): a_p [r] = sum_{j<p} [(r+j)/p] + [p r]    (p = 5, r = b/5, [p r] = [b] = [0])
# a_p values: PARI ellap (a_3 of the M=3 curves from validation/ref/pari_ref_output.txt; a_5 = [-2,-3,-4] for 37a1, 389a1, 446d1).
from fractions import Fraction as F
from math import gcd
import os
os.chdir(os.path.expanduser('~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/validation'))
sym = {}
for l in open('ref/sage_symbols_output.txt'):
    p = l.split()
    if p and p[0] == 'SYM': sym[(p[1], int(p[2]), F(int(p[4]), int(p[3])))] = F(p[5])
def S(lab, sg, r):
    r = r - (r.numerator // r.denominator)
    return sym[(lab, sg, r)]
ap3 = {'15a1': -1, '24a1': -1, '57b1': 1, '141a1': 1, '141d1': -1}
ok = True; n = 0
for lab, a in ap3.items():
    for sg in (1, -1):
        for m in (9, 27):
            for b in range(1, m):
                if gcd(b, m) != 1: continue
                n += 1
                if a * S(lab, sg, F(b, m)) != sum(S(lab, sg, F(b + m * j, 3 * m)) for j in range(3)): ok = False; print('MISMATCH', lab, sg, m, b)
print(f'U_3: a_3 [b/m] = sum_j [(b+mj)/3m], m in (9,27), both signs, 5 curves with 3 || N: {n} identities, all hold: {ok}')
a5 = {'37a1': -2, '389a1': -3, '446d1': -4}
ok2 = True; n2 = 0
for lab, a in a5.items():
    for sg in (1, -1):
        for b in range(1, 5):
            n2 += 1
            if a * S(lab, sg, F(b, 5)) != sum(S(lab, sg, F(b + 5 * j, 25)) for j in range(5)): ok2 = False; print('MISMATCH', lab, sg, b)
print(f'T_5: a_5 [b/5] = sum_j [(b+5j)/25] + [0] ([0] = 0 at rank >= 1), 37a1/389a1/446d1, both signs: {n2} identities, all hold: {ok2}')
