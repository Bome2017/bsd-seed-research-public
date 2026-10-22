"""Independent exact model and point arithmetic, without any Sha value."""
from pathlib import Path
import json

def invariants(a):
    a1,a2,a3,a4,a6=a
    b2=a1*a1+4*a2; b4=a1*a3+2*a4; b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    return (b2*b2-24*b4, -b2**3+36*b2*b4-216*b6,
            -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)

old=invariants([0,-1,1,-10,-20])
new=invariants([0,-1,1,-22826,2411880])
assert new[0]==47**2*old[0]
assert new[1]==(-47)**3*old[1]
assert new[2]==47**6*old[2]==-11**5*47**6
for x,y in [(63,1104),(110,1104)]:
    assert y*y+y==x**3-x*x-22826*x+2411880
result={'status':'PASS','twist_discriminant':-47,'c4_ratio':47**2,
        'c6_ratio':(-47)**3,'discriminant_ratio':47**6,
        'two_rational_points_checked':True,
        'rank_upper_bound':'retained fresh PARI ellrank result, not independently rerun by this arithmetic checker'}
Path(__file__).with_name('EXACT_MODEL_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('TWIST_MODEL_AND_POINT_CHECK_PASS')
