#!/usr/bin/env python3
"""Exact certificate-threshold accounting; does not evaluate a Hecke L-value."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
HERE=Path(__file__).resolve().parent
source=HERE/'inputs/RETAINED_ANALYTIC_INPUT.json'
bindings=json.loads((HERE/'inputs/BINDINGS.json').read_text())
for binding in bindings:
    bound=HERE/binding['copied_path']
    assert hashlib.sha256(bound.read_bytes()).hexdigest()==binding['sha256']
x=json.loads(source.read_text())
def f(z):return F(int(z['numerator']),int(z['denominator']))
def obj(z):return {'numerator':str(z.numerator),'denominator':str(z.denominator)}
pi=f(x['pi_interval'][0]); lam=f(x['lambda_lower'])
Vmin=pi**3*lam**6/384
Tup=F(int(x['sqrtQ_upper_integer'])*int(x['L_value_upper_ceiling']))/(2*pi)**6
assert Vmin>31756
assert Tup < 42*10**71
# If each of the positive T,V0 enclosures has relative width <= eps,
# the ratio interval has width <= 2 eps * Tup/(64 V0_lower).
# Use 3 in place of 2 and V0_lower >= 31756 for a conservative gate.
ratio_upper=F(42*10**71,64*31756)
rows=[]
for J in (1,10**6,10**12,10**24):
    D=128*J
    q=3*ratio_upper*D**2
    bits=max(1,q.numerator.bit_length()-q.denominator.bit_length())
    while F(2**bits)<=q:bits+=1
    digits=1
    while 10**digits<=q:digits+=1
    assert 3*ratio_upper/F(2**bits)<F(1,D**2)
    assert 3*ratio_upper/F(10**digits)<F(1,D**2)
    rows.append({'assumed_certified_unit_index_upper_J':str(J),'denominator_upper_D':str(D),'required_absolute_ratio_width_less_than':obj(F(1,D**2)),'sufficient_relative_binary_precision_bits':bits,'sufficient_relative_decimal_precision_digits':digits})
# Distinct reduced rational candidates with bounded denominators cannot collide
# within width 1/D^2, independently of numerator size.
from math import gcd,isqrt
# An optimistic absolute-L precision gate for THIS reconstruction criterion.
# V0plus >= b, D=128 floor(V0plus/b), and x/floor(x)^2 < 2 for x>=1.
# Any admitted ratio enclosure has width >= sqrt(Q)*width(L)/(64*(2*pi)^6*V0plus).
# Thus width(L) < (2*pi)^6*b/(128*sqrt(Q)); use pi upper and sqrt lower.
piup=f(x['pi_interval'][1]); q=int(x['arithmetic_conductor_Q'])
sqrtlo=isqrt(q); assert sqrtlo**2 <= q < (sqrtlo+1)**2
Lgate=(2*piup)**6*31756/F(128*sqrtlo)
assert Lgate < F(91,10**54)
# Control the floor inequality by its proof: for integer n>=1 and n<=x<n+1,
# x/n^2 < (n+1)/n^2 <= 2.
for n in range(1,1001): assert F(n+1,n*n)<=2
controls=[]
for D in (2,3,5,8,12):
    rs=sorted(set(F(a,b) for b in range(1,D+1) for a in range(-3*b,3*b+1)))
    mind=min(b-a for a,b in zip(rs,rs[1:]))
    assert mind>=F(1,D**2)
    controls.append({'D':D,'minimum_observed_spacing':obj(mind),'candidate_count':len(rs)})
out={'status':'EXACT_THRESHOLD_ACCOUNTING_PASS_NOT_A_SEED_CERTIFICATE','source':'inputs/RETAINED_ANALYTIC_INPUT.json','source_provenance':bindings[0]['original_path'],'copied_input_bindings_verified':len(bindings),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'relative_log_covolume_lower_floor':31756,'retained_T_upper_rounded':str(42*10**71),'T_upper_fraction':obj(Tup),'ratio_upper_rounded':obj(ratio_upper),'precision_gate_examples_not_observed_unit_indices':rows,'optimistic_absolute_L_width_gate_for_this_reconstruction_only':{'exact_upper_fraction':obj(Lgate),'safe_upper_bound':{'numerator':'91','denominator':str(10**54)},'description':'Any admitted instance of the stated interval-width criterion needs absolute L interval width below 9.1e-53; this is not a runtime or algorithmic impossibility bound.'},'finite_spacing_checks':controls,'seed_input_gate':{'rank_six_authenticated_relative_unit_subgroup':'NOT_FOUND_IN_CHECKED_COMPLETED_PACKETS','five_saturation_of_that_subgroup':'NOT_SUPPLIED','two_sided_relative_L_value_enclosure':'NOT_SUPPLIED; retained value is a one-sided upper bound'},'endpoints_changed':False}
(HERE/'RECONSTRUCTION_GATE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'precision_rows':rows,'seed_input_gate':out['seed_input_gate']},indent=2))
