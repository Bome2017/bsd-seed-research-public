from sage.all import *
from pathlib import Path
import json
root=Path(__file__).parent
P=PolynomialRing(QQ,'X'); X=P.gen(); pol=X**5-5*X**3+5*X-46846
assert pol.change_ring(GF(11)).is_irreducible()
D=X**4-3*X**2+1
assert (X**5-5*X**3+5*X)**2-4==(X**2-4)*D**2
assert 46846**2-4==224**2*43737
Q=Qp(11,prec=14)
a=Q(1)
for i in range(6): a=a-(a*a-a-10934)/(2*a-1)
sq=2*a-1
epsilon=23423+112*sq
gamma=-5829-56*a
gammabar=-5829-56*(1-a)
alpha=gamma/gammabar
pts=[(QQ(1778638)/9,QQ(1169009812)/27),(QQ(6466626346478)/36517849,QQ(2366996613841078836)/220677361507)]
f=lambda P: Q(P[0]-QQ(11*43737)/3)*Q(P[1]+QQ(1)/2)+sq*Q(-4*P[0]**2+QQ(161*43737)/6*P[0]-QQ(785*43737**2)/18)
rows={}
for label,value in [('epsilon',epsilon),('alpha11',alpha),('fP1',f(pts[0])),('fP2',f(pts[1]))]:
    v=ZZ(value.valuation()); unit=(value/11**v).residue(); log=ZZ(unit.log(GF(11)(2)))
    rows[label]={'valuation':int(v),'residue':int(unit),'signature':[int(v%5),int(log%5)]}
assert rows['epsilon']['signature']==[0,4]
assert rows['alpha11']['signature']==[4,0]
assert rows['fP1']['signature']==rows['fP2']['signature']==[0,0]
K=NumberField(pol,'t'); t=K.gen(); KK=K.extension(PolynomialRing(K,'s').gen()**2-43737,'s'); s=KK.gen()
z=(t+224*s/(t**4-3*t**2+1))/2
assert z**5==23423+112*s
result={'independent_engine':'Sage, not submitted Python checker','mod11_irreducible':True,'Chebyshev_polynomial_identity':True,'exact_fifth_root_in_compositum':True,'local_rows':rows}
(root/'independent_local.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
