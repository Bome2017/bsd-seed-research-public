from sage.all import *
import json,glob,time
E=EllipticCurve(QQ,[1,1,1,3,12]);maps=[(fn,json.load(open(fn))) for fn in sorted(glob.glob('map_*_0.json'))]
for q in prime_range(7,100000):
 if E.discriminant().valuation(q)!=0:continue
 if any(QQ(c).denominator()%q==0 for _,j in maps for c in j['x_coeffs']+j['Y_factor_coeffs']):continue
 if any(EllipticCurve(QQ,[QQ(c) for c in j['target_ainvs']]).discriminant().valuation(q)!=0 for _,j in maps):continue
 e=E.change_ring(GF(q));roots=e.division_polynomial(5).roots(multiplicities=False)
 if len(roots)!=12:continue
 pts=[]
 for xx in roots:
  pts+=list(e.lift_x(xx,all=True))
 if len(pts)!=24:continue
 P=pts[0];Q=next((T for T in pts if all(T!=k*P for k in range(5))),None)
 if Q is None:continue
 pair=P.weil_pairing(Q,5);assert pair!=1
 print('FIRST FULL5 PRIME',q,'basis',P,Q,'pairing',pair,flush=True)
 out={'q':int(q),'P':list(map(int,P)),'Q':list(map(int,Q)),'weil_pairing':int(pair),'maps':[]}
 for fn,j in maps:
  C=EllipticCurve(GF(q),[QQ(c) for c in j['target_ainvs']]);RP=PolynomialRing(GF(q),'X');r=RP([QQ(c) for c in j['x_coeffs']]);s=RP([QQ(c) for c in j['Y_factor_coeffs']]);
  def image(T):
   if T==e(0):return C(0)
   xx,yy=T.xy();RR=r(xx);YY=s(xx)*(2*yy+e.a1()*xx+e.a3());return C(RR,(YY-C.a1()*RR-C.a3())/2)
  P1,Q1=image(P),image(Q);ep=P1.weil_pairing(Q1,5);k=next(k for k in range(1,5) if pair**k==ep)
  alladd=all(image(A+B)==image(A)+image(B) for A in [e(0)]+pts for B in [e(0)]+pts)
  out['maps'].append({'map':fn,'image_P':list(map(int,P1)),'image_Q':list(map(int,Q1)),'target_pairing':int(ep),'multiplier_mod5':int(k),'all_625_additions_in_reduction':bool(alladd)})
  print(fn,'multiplier',k,'addition',alladd,flush=True);assert alladd
 json.dump(out,open('PAIRING_CHECKS.json','w'),indent=2);break
else:raise RuntimeError('no split prime within bound')
