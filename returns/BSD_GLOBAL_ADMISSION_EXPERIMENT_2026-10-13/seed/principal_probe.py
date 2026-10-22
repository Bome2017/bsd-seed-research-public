from sage.all import *
import json, pathlib, time
out=pathlib.Path(__file__).parent
R=PolynomialRing(QQ,'X'); X=R.gen()
E=EllipticCurve(QQ,[0,-1,0,-66020924,-65074271436])
f5=R(E.division_polynomial(5))
r=ZZ(1089)
cubic=X**3-X**2-66020924*X-65074271436
norm=QQ(f5.resultant(cubic-r*r))/125
assert norm.denominator() in [1,5,25,125]
nn=abs(ZZ(norm.numerator())); small=[]
for l in prime_range(2,100000):
 v=nn.valuation(l)
 if v: small.append([int(l),int(v)]);nn//=l**v
q=1783; F=GF(q); Eq=E.change_ring(F)
poly=R(f5);fq=poly.change_ring(F)
factors=fq.factor()
P=Eq(1591,1089); assert 5*P==Eq(0)
rows=[]
for a in range(1,5):
 V=a*P
 rows.append({'a':a,'x':int(V[0]),'y':int(V[1]),'z_residue':int(V[1]-F(r))})
result={'normalization':'Norm from nonzero full5 torsion field of y(T)-1089, f5 resultant divided by5^3','f5':str(f5),'norm':str(norm),'small_prime_support':small,'unfactored_cofactor':str(nn),'q':q,'x_torsion_factor_degrees':[[int(f.degree()),int(e)] for f,e in factors],'q_torsion_rows':rows}
(out/'principal_probe.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
