#!/usr/bin/env python3
"""p = 5 downstream evaluation from the rigorously identified symbols (exact rationals; 5-adic numbers mod 5^K).

usage: p5_downstream.py RUN_OUT_DIR [--lp5 LIST] [--no-lp5]

Routes:
  A: the audited six-symbol formula (SW gate addendum, master certificate N6):
       a_2 = 3([2/25]+ + [3/25]+ + [4/25]+ + [11/25]+) + 4([9/25]+ + [12/25]+)   (mod 5)
  B: independent re-implementation of SW's depth-2 approximation (good ordinary p = 5):
       P_2(T) = sum_{a=1..4} sum_{j=0..4} mu(omega(a) 6^j + 25 Z_5) (1+T)^j,
       mu(b + 25 Z_5) = alpha^-2 [b/25]+ - alpha^-3 [b/5]+,  alpha = unit root of x^2 - a_5 x + 5 (Hensel, mod 5^K),
       omega = Teichmuller (computed as a^(5^K) mod 5^K); a_{2,j} = sum mu * C(j, k).  SW Prop 3.5 (c = 0): a_2 = a_{2,2} (mod 5).
  C: comparison with the historical LP5 double-precision values (consistency only).
Checks (theorem-forced unless marked): a_{2,0} = 0 exactly; a_{2,1} = 0 mod 5; route A = route B mod 5; T_5 Hecke relation between
m = 25 and m = 5 (both signs; [0]^+ = L(E,1)/Omega^+ = 0, [0]^- = 0); sum_c [c/5]^+ = (a_5 - 2)[0]^+ = 0; symmetries; lattice
(1/512)Z [extra]; 3-integrality irrelevant here, denominators must be prime to 5.
"""
import sys, os, struct
from fractions import Fraction as F
from math import comb

RUN = sys.argv[1]; K = 20; P = 5; PK = P ** K
LP5 = [-54, 16, 90, -52, None, -76, 16, 76, -52, None, -54, 90, 90, -54, None, -52, 76, 16, -76, None, -52, 90, 16, -54]
use_lp5 = '--no-lp5' not in sys.argv
fails = []
def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok: fails.append(msg)
def rd(m):
    plus, minus = {}, {}
    for l in open(f'{RUN}/SYMBOLS_m{m}.txt'):
        if l.startswith('#'): continue
        b, p, q = l.split(); plus[int(b)] = F(p); minus[int(b)] = F(q)
    return plus, minus
def zp(x):
    """rational with denominator prime to 5 -> integer mod 5^K"""
    x = F(x); assert x.denominator % P != 0, 'denominator divisible by 5'
    return (x.numerator * pow(x.denominator, -1, PK)) % PK
def v5(n):
    n %= PK
    if n == 0: return K
    v = 0
    while n % P == 0: n //= P; v += 1
    return v

# a_5 from the verified a_q file (primes 2, 3, 5, ... in order)
a5 = struct.unpack('<3i', open(f'{RUN}/ap/ap_000000.bin', 'rb').read(12))[2]
print(f'a_5 (verified a_q file) = {a5}')
s25, m25 = rd(25); s5, m5 = rd(5)
check(sorted(s25) == [b for b in range(1, 25) if b % 5] and sorted(s5) == [1, 2, 3, 4], f'symbol sets complete: {len(s25)} at m = 25, {len(s5)} at m = 5 (both signs)')
check(all(s25[b] == s25[25 - b] for b in s25) and all(m25[b] == -m25[25 - b] for b in m25) and all(s5[b] == s5[5 - b] for b in s5) and all(m5[b] == -m5[5 - b] for b in m5),
      'symmetries [m-b]^+ = [b]^+ and [m-b]^- = -[b]^- (m = 25, 5)')
check(all(x.denominator % 5 != 0 for x in list(s25.values()) + list(s5.values())), 'all symbol denominators prime to 5 (c = 0 in SW Prop 3.5)')
check(all((x * 512).denominator == 1 for x in list(s25.values()) + list(s5.values())), 'extra: every plus symbol lies in (1/512)Z (master N7 lattice (1/c_E)Z, c_E | 512)')
print('INFO all plus symbols integral:', all(x.denominator == 1 for x in list(s25.values()) + list(s5.values())))
# ---- Hecke T_5 (5 does not divide N): a_5 [c/5] = sum_{j<5} [(c+5j)/25] + [c] = ... + [0];  [0]^+ = 0 = [0]^-
check(all(a5 * s5[c] == sum(s25[c + 5 * j] for j in range(5)) for c in s5) and all(a5 * m5[c] == sum(m25[c + 5 * j] for j in range(5)) for c in m5),
      'T_5 Hecke relation a_5[c/5] = sum_j [(c+5j)/25] + [0] for c = 1..4, both signs, with [0] = 0 (L(E,1) = 0)')
check(sum(s5.values()) == 0, 'T_5 at r = 0: sum_{c=1..4} [c/5]^+ = (a_5 - 2)[0]^+ = 0')
# ---- route A (six-symbol formula, exact) ----
S6 = 3 * (s25[2] + s25[3] + s25[4] + s25[11]) + 4 * (s25[9] + s25[12])
rA = zp(S6) % 5
print(f'ROUTE_A six-symbol value 3([2]+[3]+[4]+[11]) + 4([9]+[12]) = {S6}  -> mod 5 = {rA}')
# ---- route B (full depth-2 measure, 5-adic) ----
alpha = a5 % P                                                  # unit root: alpha = a_5 mod 5
for _ in range(2 * K):
    f = (alpha * alpha - a5 * alpha + 5) % PK; df = (2 * alpha - a5) % PK
    alpha = (alpha - f * pow(df, -1, PK)) % PK
check((alpha * alpha - a5 * alpha + 5) % PK == 0 and alpha % 5 != 0, f'alpha = unit root of x^2 - ({a5})x + 5 mod 5^{K}; alpha mod 25 = {alpha % 25} (gate: 13)')
if a5 == -2: check(alpha % 25 == 13, 'seed: alpha = 13 mod 25 (master certificate N6)')
teich = {a: pow(a, P ** K, PK) for a in range(1, 5)}
check([teich[a] % 25 for a in range(1, 5)] == [1, 7, 18, 24], f'Teichmuller lifts mod 25 = {[teich[a] % 25 for a in range(1, 5)]} (gate: 1, 7, 18, 24)')
ia = pow(alpha, -1, PK)
coef = [0, 0, 0]; seen = []
for a in range(1, 5):
    for j in range(5):
        b = (teich[a] * pow(6, j, 25)) % 25; seen.append(b)
        mu = (ia * ia * zp(s25[b]) - ia * ia * ia * zp(s5[b % 5])) % PK
        for k in range(3): coef[k] = (coef[k] + mu * comb(j, k)) % PK
check(sorted(seen) == [b for b in range(1, 25) if b % 5], 'residues omega(a) 6^j (a = 1..4, j = 0..4) run over all 20 units mod 25')
print(f'ROUTE_B a_{{2,0}} = {coef[0]} (mod 5^{K})')
print(f'ROUTE_B a_{{2,1}} = {coef[1]} (mod 5^{K}); ord_5 = {v5(coef[1])}')
print(f'ROUTE_B a_{{2,2}} = {coef[2]} (mod 5^{K}); mod 5 = {coef[2] % 5}; ord_5 = {v5(coef[2])}')
check(coef[0] == 0, 'a_{2,0} = 0 exactly (total mass (1 - 1/alpha)^2 [0]^+ = 0)')
check(coef[1] % 5 == 0, 'a_{2,1} = 0 mod 5 (a_1 = 0 since ord_T L_5 >= 2; SW Prop 3.5 e_{1,1} = 1)')
check(coef[2] % 5 == rA, f'route B a_{{2,2}} mod 5 = {coef[2] % 5} equals route A (six-symbol) mod 5 = {rA}')
# alpha^-3 [b/5] part vanishes mod 5 (gate addendum): check explicitly
part5 = sum((ia ** 3) * zp(s5[(teich[a] * pow(6, j, 25)) % 5]) * comb(j, 2) for a in range(1, 5) for j in range(5)) % PK
check(part5 % 5 == 0, f'the alpha^-3 [b/5]^+ contribution to a_{{2,2}} vanishes mod 5 (sum_j C(j,2) = 10): ord_5 = {v5(part5)}')
# ---- normalisations ----
print('NORMALISATION omega_1 (symbols x_b = Re lambda_f(b/m)/omega_1, as computed; = master N6/N9 and LP5):  a_{2,2} mod 5 =', coef[2] % 5)
print('NORMALISATION f-Neron (divide by Omega_E^+ = 2 omega_1, Delta > 0):                               a_{2,2} mod 5 =', (coef[2] * pow(2, -1, 5)) % 5)
print('NORMALISATION SW with the curve parametrisation (factor c_E/2, c_E = 2^k | 512, k unknown):   residues for k = 0..9:',
      [(coef[2] * pow(2, k, 5) * pow(2, -1, 5)) % 5 for k in range(10)])
print('=> every normalisation in play differs by a 5-adic unit (5 does not divide c_E); ord_5 a_{2,2} is normalisation-independent.')
# ---- route C (historical LP5, consistency only) ----
if use_lp5:
    same = all(LP5[b - 1] is None or F(LP5[b - 1]) == s25[b] for b in range(1, 25))
    check(same, 'route C: all 20 rigorous [b/25]^+ equal the historical LP5 double-precision identifications (consistency only)')
    check(S6 == 152, f'route C: six-symbol value {S6} equals the historical LP5 value 152 (consistency only)')
ord5 = v5(coef[2])
print(f'RESULT a_{{2,2}} mod 5 = {coef[2] % 5} (omega_1 normalisation); ord_5(a_2) = ord_5(a_{{2,2}} mod 5) = {0 if coef[2] % 5 else ">= 1"}')
print('DOWNSTREAM_P5_' + ('PASS' if not fails else 'FAIL'), f'failures={len(fails)}')
sys.exit(1 if fails else 0)
