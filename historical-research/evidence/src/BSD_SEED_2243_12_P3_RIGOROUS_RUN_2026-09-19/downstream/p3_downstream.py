#!/usr/bin/env python3
"""Downstream p = 3 evaluation (exact rational arithmetic) from the rigorously identified symbols.

usage: p3_downstream.py RUN_OUT_DIR [LANE3_IDENT_DIR]

Inputs:
  RUN_OUT_DIR/SYMBOLS_m81.txt, SYMBOLS_m27.txt : lines "b plus minus" (exact fractions; x_b = Re lambda(b/m)/omega_1)
  RUN_OUT_DIR/ap/ap_000000.bin                 : verified a_q (a_3 read from here)
  LANE3_IDENT_DIR/p3_weights_n{3,4}_j{0,1,2}.txt : Lane 3's audited weights (a_{n,j} = sum_b w_b [b/3^n]^+, alpha = a_3 = -1)

Method (SW Sect. 3; F1 CP-F; Lane 3 04_P3.md Sect. 4): nonsplit multiplicative measure mu(b + 3^n Z_3) = alpha^-n [b/3^n]^+,
alpha = a_3 = -1;  P_n(T) = sum_{a=1,2} sum_{j<3^(n-1)} mu(omega(a) 4^j + 3^n Z_3) (1+T)^j,  a_{n,j} = coefficient of T^j.
Weights are taken from Lane 3's files AND recomputed independently here (must be identical).

Checks (theorem-forced unless marked): a_{n,0} = 0 (n = 2,3,4); a_{4,1} = 0 mod 27; SW Prop. 3.5 congruences between depths
(a_{n+1,j} = a_{n,j} mod 3^{e_{n-1,j}}); U_3 chain 81 -> 27 -> 9 -> 3 and [1/3]^+ = [2/3]^+ = 0; symmetry [b]^+ = [m-b]^+,
[b]^- = -[m-b]^-; every x_b has even numerator over 1024 (F1: x_b in (1/c_E)Z within (1/512)Z) [extra check].
"""
import sys, os, struct
from fractions import Fraction as F
from math import comb, gcd

RUN = sys.argv[1]
L3 = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser('~/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/D_primes/ident')
fails = []
def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok: fails.append(msg)

def read_symbols(m):
    plus, minus = {}, {}
    for l in open(f'{RUN}/SYMBOLS_m{m}.txt'):
        if l.startswith('#'): continue
        b, p, q = l.split(); plus[int(b)] = F(p); minus[int(b)] = F(q)
    return plus, minus

def v3(x):
    """3-adic valuation of a nonzero rational."""
    x = F(x); n, d = x.numerator, x.denominator; v = 0
    while n % 3 == 0: n //= 3; v += 1
    while d % 3 == 0: d //= 3; v -= 1
    return v

def mod3k(x, k):
    """residue of a 3-integral rational mod 3^k."""
    x = F(x); M = 3 ** k
    assert x.denominator % 3 != 0
    return (x.numerator * pow(x.denominator, -1, M)) % M

# a_3 from the verified coefficient file (primes 2, 3, 5, ... in order)
raw = open(f'{RUN}/ap/ap_000000.bin', 'rb').read(8)
a2_, a3 = struct.unpack('<2i', raw)
print(f'a_3 (verified a_q file) = {a3}')
check(a3 == -1, 'a_3 = -1 (nonsplit multiplicative at 3, alpha = a_3 = -1)')
alpha = F(a3)

s81, m81 = read_symbols(81); s27, m27 = read_symbols(27)
check(sorted(s81) == [b for b in range(1, 81) if b % 3] and sorted(s27) == [b for b in range(1, 27) if b % 3],
      f'symbol sets complete: {len(s81)} of 54 at m=81, {len(s27)} of 18 at m=27 (plus and minus)')

# ---------- weights: Lane 3 files and independent recomputation ----------
def lane3_weights(n, j):
    L = open(f'{L3}/p3_weights_n{n}_j{j}.txt').read().split('\n')[1]
    return [int(x) for x in L.strip('[]').split(',')]

def teich3(a, n):
    """Teichmuller representative of a mod 3^n (omega(1) = 1, omega(2) = -1), by the limit a^(3^k)."""
    M = 3 ** n; t = a % M
    for _ in range(n + 2): t = pow(t, 3, M)
    return t

def my_weights(n, jj):
    m = 3 ** n; w = [0] * (m - 1)
    for a in (1, 2):
        t = teich3(a, n)
        for j in range(3 ** (n - 1)):
            b = (t * pow(4, j, m)) % m
            w[b - 1] += (-1) ** n * comb(j, jj)        # alpha^-n = (-1)^n
    return w

check(teich3(2, 4) == 80 and teich3(1, 4) == 1, 'Teichmuller representatives mod 81: omega(1) = 1, omega(2) = -1')
same = all(lane3_weights(n, j) == my_weights(n, j) for n in (3, 4) for j in (0, 1, 2))
check(same, "Lane 3 weight files p3_weights_n{3,4}_j{0,1,2} == independent recomputation (all 6 vectors identical)")

def coeff(n, j, sym):
    w = my_weights(n, j); return sum(F(w[b - 1]) * sym[b] for b in sym)

# depth-2 symbols from the m=27 run via U_3 (exact, a_3 [c/9] = sum_j [(c+9j)/27])
s9 = {c: sum(s27[c + 9 * j] for j in range(3)) / alpha for c in range(1, 9) if c % 3}
m9 = {c: sum(m27[c + 9 * j] for j in range(3)) / alpha for c in range(1, 9) if c % 3}
s3 = {c: sum(s9[c + 3 * j] for j in range(3)) / alpha for c in (1, 2)}
m3 = {c: sum(m9[c + 3 * j] for j in range(3)) / alpha for c in (1, 2)}
check(all(s27[c] == sum(s81[c + 27 * j] for j in range(3)) / alpha for c in s27) and
      all(m27[c] == sum(m81[c + 27 * j] for j in range(3)) / alpha for c in m27),
      'U_3 relation 81 -> 27 exact for all 18 residues, both signs (the m=27 run is an independent computation)')
check(s3[1] == 0 and s3[2] == 0, f'[1/3]^+ = [2/3]^+ = 0 (forced by U_3 and L(E,1) = 0): got {s3[1]}, {s3[2]}')
check(all(s81[b] == s81[81 - b] for b in s81) and all(m81[b] == -m81[81 - b] for b in m81) and
      all(s27[b] == s27[27 - b] for b in s27) and all(m27[b] == -m27[27 - b] for b in m27),
      'symmetry [b/m]^+ = [(m-b)/m]^+ and [b/m]^- = -[(m-b)/m]^- (m = 81, 27)')
ev = all((x * 1024).denominator == 1 and int(x * 1024) % 2 == 0 for x in list(s81.values()) + list(s27.values()))
check(ev, 'extra (F1 CP-F): every plus symbol has EVEN numerator over 1024, i.e. lies in (1/512)Z')
evm = all((x * 1024).denominator == 1 and int(x * 1024) % 2 == 0 for x in list(m81.values()) + list(m27.values()))
print(('INFO ' if evm else 'INFO ') + f'minus symbols all in (1/512)Z: {evm} (not a required check)')

# ---------- coefficients ----------
a4 = [coeff(4, j, s81) for j in range(3)]
a3c = [coeff(3, j, s27) for j in range(3)]
a2c = [coeff(2, j, s9) for j in range(3)]
# Lane 3 file-weights route (must equal the recomputed route exactly)
a4_files = [sum(F(lane3_weights(4, j)[b - 1]) * s81[b] for b in s81) for j in range(3)]
check(a4 == a4_files, 'a_{4,j} via Lane 3 weight files == via recomputed weights (j = 0, 1, 2)')
print(f'a_{{4,0..2}} = {[str(x) for x in a4]}   (exact rationals; symbols normalised by omega_1)')
print(f'a_{{3,0..2}} = {[str(x) for x in a3c]}   (from the independent m = 27 run)')
print(f'a_{{2,0..2}} = {[str(x) for x in a2c]}   (depth 2 via U_3 from m = 27; Lane 3: a_{{2,2}} = 2[2/9]^+ = {2 * s9[2]})')
check(a2c[2] == 2 * s9[2], 'depth-2 formula a_{2,2} = [7/9]^+ + [2/9]^+ = 2[2/9]^+ (Lane 3 W2 line)')
check(all(x.denominator % 3 != 0 for x in a4 + a3c + a2c), 'all coefficients are 3-integral (denominators powers of 2)')
check(a4[0] == 0 and a3c[0] == 0 and a2c[0] == 0, 'a_{n,0} = 0 exactly for n = 2, 3, 4 (L(E,1) = 0; Lane 3 forced check)')
check(mod3k(a4[1], 3) == 0, f'a_{{4,1}} = 0 mod 27 (ord_T L_3 >= 2; F1 / Lane 3 forced check): a_{{4,1}} mod 27 = {mod3k(a4[1], 3)}')
# SW Prop. 3.5 (c = 0): ord_3(a_{n+1,j} - a_{n,j}) >= e_{n-1,j} = min_{1<=i<=j} ord_3 C(3^(n-1), i)
def e(n, j): return min(v3(comb(3 ** n, i)) for i in range(1, j + 1))
for j in (1, 2):
    d43 = a4[j] - a3c[j]; d32 = a3c[j] - a2c[j]
    check(d43 == 0 or v3(d43) >= e(2, j), f'SW Prop 3.5: ord_3(a_{{4,{j}}} - a_{{3,{j}}}) >= e_{{2,{j}}} = {e(2, j)}  (got {"inf" if d43 == 0 else v3(d43)})')
    check(d32 == 0 or v3(d32) >= e(1, j), f'SW Prop 3.5: ord_3(a_{{3,{j}}} - a_{{2,{j}}}) >= e_{{1,{j}}} = {e(1, j)}  (got {"inf" if d32 == 0 else v3(d32)})')
print(f'e_{{3,j}} (j = 1..6) = {[e(3, j) for j in range(1, 7)]}  -> a_{{4,2}} = a_2 mod 3^{e(3, 2)}')

# ---------- verdict ----------
r = mod3k(a4[2], 3); r_sw = mod3k(a4[2] / 2, 3)
o = 3 if r == 0 else v3(F(r))
print(f'RESULT a_{{4,2}} = {a4[2]}  (exact, omega_1 normalisation)')
print(f'RESULT a_{{4,2}} mod 27 = {r}   [SW / Neron-period normalisation (x_b/2): {r_sw} mod 27]')
print(f'RESULT ord_3(a_{{4,2}} mod 27) = {">= 3" if o == 3 else o}')
case = {0: 'B (ord 0: contradiction with Sha_an = 9)', 1: 'C (ord 1: impossible for finite Sha)', 2: 'A (ord 2: #Sha[3^inf] = 9)', 3: 'D (a_{4,2} = 0 mod 27: depth 4 insufficient)'}[o]
print(f'CASE {case}')
print('DOWNSTREAM_CHECKS_' + ('PASS' if not fails else 'FAIL'), f'failures={len(fails)}')
sys.exit(1 if fails else 0)
