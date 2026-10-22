from sage.all import *
import time,json,os
os.chdir('/Users/bsm/BSD_COMPARISON_EXPERIMENT_CODEX_2026-10-11/torsion')
E=EllipticCurve(QQ,[1,1,1,3,12]); F=NumberField(E.division_polynomial(5),'u');u=F.gen()
print('FIELD',F,flush=True)
for label,coeff in [('113',[1,1,1,-1669982047,-25795561267816]),('167',[1,1,1,1878418,-485198548])]:
 C=EllipticCurve(QQ,coeff); t=time.monotonic(); print('START ROOTS',label,flush=True)
 roots=C.division_polynomial(5).change_ring(F).roots(multiplicities=False)
 print('ROOTS',label,len(roots),'seconds',time.monotonic()-t,flush=True)
 for i,r in enumerate(roots):
  # Y=2y+a1*x+a3, so Y^2=4x^3+b2*x^2+2b4*x+b6.
  f=lambda A,x:4*x**3+A.b2()*x**2+2*A.b4()*x+A.b6()
  ratio=f(C,r)/f(E,u); print('SQUARE ROOT',label,i,flush=True)
  sq=ratio.sqrt(all=True)
  print('Y FACTORS',len(sq),flush=True)
  for j,s in enumerate(sq):
   out={'label':label,'source_ainvs':list(map(str,E.a_invariants())),'target_ainvs':list(map(str,C.a_invariants())),'field_polynomial':str(F.polynomial()),'x_coeffs':list(map(str,r.polynomial().list())),'Y_factor_coeffs':list(map(str,s.polynomial().list())),'checks':{'x_fits_division_polynomial':C.division_polynomial(5)(r)==0,'curve_identity':s*s*f(E,u)==f(C,r)}}
   fn=f'map_{label}_{i}_{j}.json';json.dump(out,open(fn,'w'),indent=2); print('SAVED',fn,flush=True)
