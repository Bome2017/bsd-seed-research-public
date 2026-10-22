from sage.all import *
from pathlib import Path
# Independent convention control, not the large Shimura source calculation.
E=EllipticCurve(QQ,[0,0,1,-1,0]);Y=E(0,0);Tw=E.quadratic_twist(-7)
R=RealField(120)
basis=E.period_lattice().basis(prec=120)
area=R(abs((basis[0].conjugate()*basis[1]).imag()))
l1,tail1=E.lseries().deriv_at1(2000)
l0,tail0=Tw.lseries().at1(2000)
ratio=R(7).sqrt()*R(l1)*R(l0)/(2*area*Y.height(precision=120))
assert abs(ratio-2)<R(1e-12)
out=('37a1, K=-7, canonical Heegner point (0,0), modular degree 2, Manin 1.\n'
     'CST predicted K-height / absolute BSD height = '+str(ratio)+'\n'
     'This is an exploratory convention control, not a certified CM computation for the large Shimura curve.\n')
print(out)
Path(__file__).with_name('HEIGHT_CONVENTION_CONTROL.txt').write_text(out)
