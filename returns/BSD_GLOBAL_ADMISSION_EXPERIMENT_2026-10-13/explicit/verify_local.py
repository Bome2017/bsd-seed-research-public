"""Independent standard-library checks of the corrected finite-field scan and rows.
Does not independently certify Sage/PARI class/unit groups or source theorem.
"""
from fractions import Fraction as Q
import json, hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
r=json.loads((P/'admission.json').read_text())
A4=-14959712463303;A6=-22270654620235278500
fpoly=[597816451,-54671,54671,-1,1]
def val(cs,x,p):
    out=0
    for z in reversed(cs):
        c=Q(z);out=(out*x+c.numerator*pow(c.denominator,-1,p))%p
    return out
def on(R,p):
    if R is None:return True
    x,y=R;return (y*y+y-x*x*x-A4*x-A6)%p==0
def neg(R,p):return None if R is None else (R[0],(-R[1]-1)%p)
def add(P,Qp,p):
    if P is None:return Qp
    if Qp is None:return P
    x,y=P;X,Y=Qp
    if P==neg(Qp,p):return None
    slope=((3*x*x+A4)*pow(2*y+1,-1,p) if P==Qp else (Y-y)*pow(X-x,-1,p))%p
    xx=(slope*slope-x-X)%p
    yy=(-y-1+slope*(x-xx))%p
    return xx,yy
def mul(n,R,p):
    S=None
    while n:
      if n&1:S=add(S,R,p)
      R=add(R,R,p);n//=2
    return S
def line(P,Qp,R,p):
    if P is None or Qp is None:return 1
    if P==neg(Qp,p):return (R[0]-P[0])%p
    x,y=P;X,Y=Qp
    slope=((3*x*x+A4)*pow(2*y+1,-1,p) if P==Qp else (Y-y)*pow(X-x,-1,p))%p
    num=(R[1]-y-slope*(R[0]-x))%p
    S=add(P,Qp,p)
    return num if S is None else num*pow(R[0]-S[0],-1,p)%p
def miller(T,R,p):
    V=T;f=1
    for bit in (0,1):
      f=f*f*line(V,V,R,p)%p;V=add(V,V,p)
      if bit:
        f=f*line(V,T,R,p)%p;V=add(V,T,p)
    assert V is None
    return f
def prime(n):return n>1 and all(n%d for d in range(2,int(n**.5)+1))
pointQ=[(6288329,-11502941299),(8502485,21568458354)]
scan=[]
for q in range(2,332):
    if not prime(q) or q%5!=1 or q in (3,5,11,61,239):continue
    roots=[x for x in range(q) if val(fpoly,x,q)==0]
    if len(roots)!=4:continue
    a=roots[0];T=tuple(val(cs,a,q) for cs in r['coordinate_coefficients']['T'][:2]);assert on(T,q) and mul(5,T,q) is None
    points=[tuple(z%q for z in Qp) for Qp in pointQ];assert all(on(z,q) for z in points)
    values=[miller(T,R,q) for R in points]
    assert values==[val(cs,a,q) for cs in r['coordinate_coefficients']['fQ']]
    if not all(values):continue
    row={'q':q,'root':a,'point_values':values,'fifth_test':[pow(z,(q-1)//5,q) for z in values]}
    scan.append(row)
assert scan==r['scan']
assert [z['q'] for z in scan if z['fifth_test']==[1,1]]==[331]
h=r['hit'];q=331;T=tuple(h['T'][:2]);R=tuple(h['local_point'][:2]);assert on(R,q)
assert miller(T,R,q)==40 and pow(40,66,331)==150
count=1
for x in range(q):
    disc=(1+4*(x*x*x+A4*x+A6))%q
    count+=1 if disc==0 else (2 if pow(disc,(q-1)//2,q)==1 else 0)
assert count==325==h['group_cardinality']
b=r['ideal_boundary'];c=b['class_row_mod5'];v=b['chi_divisor_basis'][0]
assert sum(x*y for x,y in zip(c,v))%5==1
Vm=b['valuation_matrix']
assert all(sum(c[i]*Vm[i][j] for i in range(4))%5==0 for j in range(5))
image={tuple(sum(Vm[i][j]*e[j] for j in range(5))%5 for i in range(4)) for e in __import__('itertools').product(range(5),repeat=5)}
ker={x for x in __import__('itertools').product(range(5),repeat=4) if sum(c[i]*x[i] for i in range(4))%5==0}
assert image==ker and len(image)==125
m=r['empty_galois_matrix'];ev=[]
for x,y in __import__('itertools').product(range(5),repeat=2):
    if (m[0][0]*x+m[0][1]*y-2*x)%5==0 and (m[1][0]*x+m[1][1]*y-2*y)%5==0:ev.append([x,y])
assert ev==[[x,x] for x in range(5)]
assert r['point_vectors']==[[3,3],[2,2]]
out={'status':'PASS','corrected_scan_rows':len(scan),'first_hit':331,'actual_local_miller_value':40,'local_fifth_power_test':150,'point_fifth_power_tests':[1,1],'independent_point_count':count,'class_boundary_dot':1,'valuation_image_size':len(image),'eligible_eigenline_size':len(ev),'scope':'Finite-field/group/linear-algebra replay; certified number-field source remains Sage/PARI computation','input_sha256':hashlib.sha256((P/'admission.json').read_bytes()).hexdigest()}
(P/'independent_local.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
