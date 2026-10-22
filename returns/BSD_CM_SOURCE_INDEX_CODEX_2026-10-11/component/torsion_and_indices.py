"""Exact small-field controls; no elliptic-curve package is used here."""
import json, math
from pathlib import Path
root=Path(__file__).resolve().parent

def add(a,b): return a^b

def mul(a,b):
    # F4 = F2[u]/(u^2+u+1), encoded a0+2*a1.
    z=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): z ^= 1 << (i+j)
    if z & 4: z ^= 7
    return z

F4_points=[]
for x in range(4):
    for y in range(4):
        lhs=add(add(mul(y,y),mul(x,y)),y)
        rhs=add(mul(mul(x,x),x),mul(x,x))
        if lhs==rhs: F4_points.append([x,y])
F5_points=[]
for x in range(5):
    for y in range(5):
        if (y*y+x*y+y-x*x*x-x*x-1878418*x+485198548)%5==0:
            F5_points.append([x,y])
assert len(F4_points)+1==8
assert len(F5_points)+1==9
assert (-19)%8==5
assert pow((-19)%5,2,5)==1
assert 20576640%11!=0
assert math.gcd(6-(-3),14-(-2))==1
assert 20576640//(14*5)==293952
assert 20576640%(14*5)==0
out={'status':'EXACT_SMALL_FIELD_AND_INDEX_CONTROLS_PASSED','F4_model':'y^2+xy+y=x^3+x^2, u^2+u+1=0','F4_affine_points':F4_points,'F4_order':len(F4_points)+1,'F5_affine_points':F5_points,'F5_order':len(F5_points)+1,'torsion_consequence':'E(Q(sqrt(-19)))_tors = 0, using prime-to-residue-character reduction injectivity at2and5','eisenstein_annihilators':[9,16],'image_order_gcd':1,'geometric_component_orders':[14,5],'cokernel_order_gcd':1,'classical_degree':20576640,'shimura_degree':293952,'source_multiplier':2*(-3-6)-(-2-14),'classical_degree_mod11':20576640%11}
(root/'TORSION_AND_INDICES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
