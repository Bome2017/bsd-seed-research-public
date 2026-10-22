from sage.all import *
import json,pathlib
out=pathlib.Path(__file__).parent
R=PolynomialRing(QQ,'X');X=R.gen()
E=EllipticCurve(QQ,[0,-1,0,-66020924,-65074271436]); f5=R(E.division_polynomial(5)); h=X**3-X**2-66020924*X-65074271436
results=[]
for r in [ZZ(1089),ZZ(1089+1783)]:
 norm=QQ(f5.resultant(h-r*r))/125
 support=[];nn=abs(ZZ(norm.numerator()))
 for l in prime_range(2,100000):
  v=nn.valuation(l)
  if v:support.append([int(l),int(v)]);nn//=l**v
 points=[]
 for l in [7,73,1783]:
  F=GF(l);El=E.change_ring(F);g=f5.change_ring(F).gcd((h-r*r).change_ring(F));rows=[]
  for xx,e in g.roots():
   P=El(xx,F(r));assert 5*P==El(0)
   rows.append({'x':int(xx),'y':int(F(r)),'multiples':[[a,int((a*P)[0]),int((a*P)[1]),int((a*P)[1]-F(r))] for a in range(1,5)]})
  points.append({'prime':l,'point_count':int(El.cardinality()),'gcd_polynomial':str(g),'torsion_points_y_r':rows})
 results.append({'r':int(r),'norm':str(norm),'small_prime_support':support,'cofactor':str(nn),'local_data':points})
(out/'leak_repair.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
