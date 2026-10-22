from sage.all import *
import json,pathlib
out=pathlib.Path(__file__).parent
R=PolynomialRing(QQ,'X');X=R.gen();S=PolynomialRing(QQ,'Y');Y=S.gen()
E=EllipticCurve(QQ,[0,-1,0,-66020924,-65074271436]);f5=R(E.division_polynomial(5));cubic=X**3-X**2-66020924*X-65074271436
h=Y**5+1013*Y**4+799*Y**3+389*Y**2+655*Y+1152
prod=h*h(-Y);assert all(prod[i]==0 for i in range(1,11,2))
g=sum(prod[2*i]*cubic**i for i in range(6))
norm=QQ(f5.resultant(g))/5**g.degree()
nn=abs(ZZ(norm.numerator()));support=[]
for l in prime_range(2,100000):
 v=nn.valuation(l)
 if v:support.append([int(l),int(v)]);nn//=l**v
assert norm.valuation(1783)==5
# Each degree-one prime can be matched to an actual local5torsion point.
local=[]
for l,v in support:
 if l in [2,3,5,1783,2243,4547,5843]:continue
 F=GF(l);El=E.change_ring(F);ff=f5.change_ring(F);hh=h.change_ring(F);rows=[]
 for xx,e in ff.roots():
  rhs=cubic.change_ring(F)(xx)
  if rhs.is_square():
   yy=rhs.sqrt()
   for y in sorted(set([yy,-yy]),key=int):
    P=El(xx,y)
    if 5*P!=El(0):raise AssertionError('torsion')
    if hh(y)==0:
     orbit=[]
     for a in [1,2,4,3]:
      V=a*P;orbit.append({'a':a,'x':int(V[0]),'y':int(V[1]),'h_residue':int(hh(V[1]))})
     rows.append({'x':int(xx),'y':int(y),'scalar_orbit':orbit})
 local.append({'prime':l,'norm_valuation':v,'root_points':rows})
result={'h':str(h),'h_coefficients':[int(h[i]) for i in range(6)],'norm':str(norm),'norm_q_valuation':int(norm.valuation(1783)),'small_support':support,'remaining_cofactor':str(nn),'leak_local_data':local}
(out/'line_source_probe.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
