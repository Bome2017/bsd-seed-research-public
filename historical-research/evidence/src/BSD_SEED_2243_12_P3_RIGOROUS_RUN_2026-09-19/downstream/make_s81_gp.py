import sys
from fractions import Fraction as F
run = sys.argv[1]; v = [F(0)] * 80
for l in open(f'{run}/SYMBOLS_m81.txt'):
    if l.startswith('#'): continue
    b, p, q = l.split(); v[int(b) - 1] = F(p)
open('s81.gp', 'w').write('S81 = [' + ', '.join(str(x) for x in v) + '];\n')
print('s81.gp written:', sum(1 for x in v if x != 0), 'nonzero of 54 units')
