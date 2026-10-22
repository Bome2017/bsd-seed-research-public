"""Source-convention controls only. No seed Kato values are evaluated."""
from fractions import Fraction as Q
import json

# Coefficients are increasing powers of one formal group element.
def twist(poly, chi):
    return [Q(a)*Q(chi)**(-i) for i,a in enumerate(poly)]

cases=0
for c in (2,3,7,11,17):
    assert twist([c*c,-c*c],c)==[Q(c*c),Q(-c)]
    # Inverse variable sigma^-1 twists in the opposite direction.
    for ell,a in ((3,-1),(2243,1),(4547,0),(5843,-1)):
        assert Q(-a,ell**2)*ell==Q(-a,ell)
        cases+=1

# τ sends the shifted source prime to the target augmentation prime.
shifted=0
for p in (5,7,11,13,17,19,23,29,31,37):
    c=1+p
    old=[-Q(1,c),Q(1)]
    got=twist(old,c)
    assert got==[-Q(1,c),Q(1,c)]  # (gamma-1)/c
    wrong=twist([-1,1],c)
    assert sum(wrong)!=0         # untwisted augmentation is not the right ideal
    shifted+=1

def valuation(n,p):
    if n==0:
        raise ValueError("zero is excluded")
    v=0
    while n%p==0:
        v+=1;n//=p
    return v

e=Q(2242,2243)
assert valuation(e.numerator,19)-valuation(e.denominator,19)==1
assert valuation(e.numerator,59)-valuation(e.denominator,59)==1
assert e!=0    # as a constant in Λ_(U), it is invertible

print(json.dumps({
    "status":"EXACT_SOURCE_CONVENTION_CONTROLS_PASS",
    "smoothing_euler_cases":cases,
    "shifted_prime_cases":shifted,
    "wrong_untwisted_augmentation_rejected":shifted,
    "e_2243":str(e),
    "v19_e_2243":1,
    "v59_e_2243":1,
    "scope":"formal coefficient identities, not Galois-cohomology or seed Kato evaluations"
},indent=2))
