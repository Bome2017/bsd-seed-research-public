#!/usr/bin/env python3
"""Independent exact arithmetic checks of the October 22 BSD GitHub delta.
Inputs are transcribed from commit 1c782871e9b26787b6cd1909ee37bafe947b0a69.
Checks published numerical implications, NOT seed field/ideal completeness.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json
BASE = Path(__file__).resolve().parent
Q = 28547674832087657668957548697971229827174630890330043601254247772342191764557483490297987200412941641241664000000000000
sqrtQhi = 168960571826943275378497531250215852256375148863032392000001
Lhi = 1511064551295557957
pi_lo = F(1570796326794896619,500000000000000000)
pi_hi = F(3141592653589793239,10**18)
delta = 2**4*5*4547**6
assert delta == 707033045140895852346320
assert isqrt(Q)+1 == sqrtQhi
C = F(sqrtQhi*Lhi)/(2*pi_lo)**6
assert C < 42*10**71

def ceil(x): return -(-x.numerator//x.denominator)
def log_floor(n,p):
    k=0
    while p**(k+1)<=n:k+=1
    return k

def hyp_upper(x, parity, n=18):
    # Positive sinh/cosh Taylor terms; successive tail ratios decrease.
    s=sum((x**(2*k+parity)/factorial(2*k+parity) for k in range(n)),F(0))
    e=2*n+parity
    tail=x**e/factorial(e)
    ratio=x*x/((e+1)*(e+2))
    assert 0 <= ratio < 1
    return s+tail/(1-ratio)

# (max norm, count of pairs, radius numerator, denominator, reported 5-rank)
rows=[
(7,2,6889807,16777216,106),
(29,4,169974821345,344119977181184,131),
(31,6,84987435883,240158725111808,132),
(53,8,169974922187,7016156116287488,142),
(67,10,169974922187,22651340547162112,146),
(73,12,169974922187,34780369899225088,147),
(113,14,169974922187,309109329691148288,155),
(137,16,169974922187,809697375747571712,159),
(149,18,169974922187,1232114980732534784,160),
(151,20,169974922187,1317057186513289216,161),
(181,22,169974922187,3259213197780975616,164),
(223,24,169974922187,9252182936768217088,168),
(229,26,169974922187,10565676458976477184,168)]
sq2hi=F(141421356237309504881,10**20)
assert sq2hi**2>2
packing=[]
for x,m,a,b,r in rows:
    radius=F(a,b)
    sep=2**24*x**20*hyp_upper(sq2hi*radius,1)**4*hyp_upper(radius,0)**16
    assert sep < delta, ('separation failed',x)
    upper=ceil(4*C/(m*(pi_lo**3/6)*radius**6))
    rank=log_floor(upper,5)
    assert rank == r, ('rank differs',x,rank,r)
    assert 2*radius < F(8559630657335159781,10**18)
    packing.append({'max_norm':x,'pairs':m,'radius':[a,b],'computed_rank_upper':rank,
                    'computed_order_upper':str(upper),'separation_pass':True})
assert packing[0]['computed_order_upper']=='334809554342956104676612913920139327331389754537007507521626340458250851040'
assert min(t['computed_rank_upper'] for t in packing)==106
# The strict prime norm windows use q < delta^(1/20) or delta^(1/10).
assert 15**20 < delta < 16**20
assert 242**10 < delta < 243**10
# Relative reconstruction: reproduces the stated sufficient error policy.
bmin=31756
precision=[]
for J in [1,10**6,10**12,10**24]:
    D=128*J
    required=F(3*42*10**71,64*bmin)*D*D
    bits=0
    while 2**bits<=required:bits+=1
    digits=0
    while 10**digits<=required:digits+=1
    precision.append({'hypothetical_J':str(J),'bits':bits,'decimal_digits':digits})
assert [r['bits'] for r in precision]==[236,276,316,396]
assert [r['decimal_digits'] for r in precision]==[72,84,96,120]
abs_L_upper=(2*pi_hi)**6*bmin/(128*isqrt(Q))
assert abs_L_upper < F(91,10**54)
output={'status':'PASS_EXACT_NUMERICAL_RECONSTRUCTION',
        'input_commit':'1c782871e9b26787b6cd1909ee37bafe947b0a69',
        'packing_prefixes':packing,'precision_table':precision,
        'absolute_L_width_gate_upper_decimal_for_display':float(abs_L_upper),
        'norm_window_integer_bounds':[15,242],
        'scope':'Exact calculations using retained field/analytic inputs. No new ideal decomposition, unit basis, class group, or Selmer result.'}
(BASE/'NUMERIC_CHECK_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='packing_prefixes'},indent=2))
print('Verified all 13 common-radius prefixes; ranks:',[r['computed_rank_upper'] for r in packing])
