from sage.all import *
from pathlib import Path
import json, time

ROOT=Path(__file__).resolve().parents[1]
E=EllipticCurve(QQ,[1,1,1,3,12]); basis=[E(0,3),E(7,17)]
records=[]

def poly_from_json(F, cs):
    return PolynomialRing(F,'X')([F(QQ(c)) for c in cs])

def image_xy(P,j,F):
    x,y=P.xy(); r=poly_from_json(F,j['x_coeffs']); s=poly_from_json(F,j['Y_factor_coeffs'])
    xx=r(x); YY=s(x)*(2*y+x+1)
    return xx,(YY-xx-1)/2

def kummer_over_prime(C,P,q):
    # The fifth division point is computed, never replaced by an unrelated
    # projection [#E(Fq)/5]P. We restrict to v5(#E(Fq))=1.
    F=GF(q); c=C.change_ring(F); point=c([F(t) for t in P.xy()])
    n=c.cardinality(); assert n%5==0 and n%25!=0
    K=GF(q**5,name='b'); d=C.change_ring(K); point5=d([K(t) for t in P.xy()])
    divs=point5.division_points(5); assert len(divs)==5
    Q=divs[0]; assert 5*Q==point5
    fq=d(Q[0]**q,Q[1]**q)-Q
    assert 5*fq==d(0) and d(fq[0]**q,fq[1]**q)==fq if fq!=d(0) else True
    # All 5 division points in this degree-five field differ by rational torsion.
    assert all(d(R[0]**q,R[1]**q)-R==fq for R in divs)
    if fq==d(0): return c(0)
    return c(F(fq[0]),F(fq[1]))

def repr_point(P):
    return None if P.is_zero() else [str(c) for c in P.xy()]

for ell, mapname,Ycoords in [
 (113,'map_113_1_0.json',[QQ(39736379971)/293764,QQ(7496759272384463)/159220088]),
 (167,'map_167_0_0.json',[480,22723])]:
    t0=time.time(); j=json.loads((ROOT/'torsion'/mapname).read_text())
    C=EllipticCurve(QQ,[QQ(c) for c in j['target_ainvs']]);Y=C(Ycoords)
    F=GF(ell**4,name='a'); EF=E.change_ring(F)
    torsion=[]
    for x in EF.division_polynomial(5).roots(multiplicities=False):
        torsion += list(EF.lift_x(x,all=True))
    assert len(torsion)==24
    smooth=[]; nodes=[]
    r=F(80 if ell==113 else 7); v=F(10 if ell==113 else 8)
    for T in torsion:
        x,y=image_xy(T,j,F);a1,a2,a3,a4,a6=[F(QQ(c)) for c in j['target_ainvs']]
        assert y*y+a1*x*y+a3*y==x**3+a2*x*x+a4*x+a6
        gx=a1*y-3*x*x-2*a2*x-a4; gy=2*y+a1*x+a3
        if gx or gy:
            YY=y+(x+1)/2
            zeta=(YY+v*(x-r))/(YY-v*(x-r))
            assert zeta**5==1 and zeta!=1
            smooth.append((T,zeta))
        else:nodes.append(T)
    assert len(smooth)==4 and len(nodes)==20
    T,zeta=smooth[0]
    assert EF(T[0]**ell,T[1]**ell)==int(ell%5)*T
    localcoords=[]
    c1points=[]
    for P in basis:
        c1=kummer_over_prime(E,P,ell)
        c1points.append(repr_point(c1))
        # K_ell/F_ell has residue degree two. Its arithmetic Frobenius
        # cocycle is twice the F_ell cocycle on the invariant eigenline.
        c1F=EF(0) if c1.is_zero() else EF([F(c) for c in c1.xy()])
        pair=T.weil_pairing(2*c1F,5)
        aa=next(i for i in range(5) if zeta**i==pair)
        localcoords.append(aa)
    rec={'ell1':ell,'map':mapname,'Y':list(map(str,Ycoords)),
         'toric_source_T':repr_point(T),'toric_zeta':str(zeta),
         'smooth_images':4,'node_images':20,'ell1_kummer_frob_q':c1points,
         'ell1_pairing_coordinates_frob_q_squared':localcoords,'tests':[]}
    print('TORIC',ell,'a',localcoords,flush=True)
    for q in prime_range(13,500):
        if q in [113,167] or E.conductor()%q==0 or C.conductor()%q==0 or q==5:continue
        if kronecker(-19,q)!=-1 or q%5 in [1,4]:continue
        en=E.change_ring(GF(q)).cardinality();cn=C.change_ring(GF(q)).cardinality()
        if en%5 or en%25==0 or cn%5 or cn%25==0:continue
        try:
            cs=[kummer_over_prime(E,P,q) for P in basis]
            cy=kummer_over_prime(C,Y,q)
        except Exception as err:
            raise RuntimeError(f'finite Kummer calculation q={q} failed') from err
        G=next((P for P in cs if not P.is_zero()),None)
        if G is None:continue
        FF=GF(q);CF=C.change_ring(FF); xx,yy=image_xy(G,j,FF); Gtarget=CF(xx,yy)
        assert 5*Gtarget==CF(0) and Gtarget!=CF(0)
        b=[next(k for k in range(5) if k*G==2*P) for P in cs]
        by=next(k for k in range(5) if k*Gtarget==2*cy)
        det=(localcoords[0]*b[1]-localcoords[1]*b[0])%5
        item={'ell2':int(q),'base_order':int(en),'raised_order':int(cn),
              'base_kummer_frob_q':[repr_point(P) for P in cs],
              'Y_kummer_frob_q':repr_point(cy),'chosen_base_torsion_G':repr_point(G),
              'image_G':repr_point(Gtarget),'point_coordinates':b,'Y_coordinate':by,
              'detector':det,'instrument_scalar':int(GF(5)(by)/GF(5)(det)) if det else None}
        rec['tests'].append(item);print('PAIR',ell,q,'a',localcoords,'b',b,'Y',by,'det',det,'instrument',item['instrument_scalar'],flush=True)
        if sum(r['detector']!=0 for r in rec['tests'])>=4:break
    rec['elapsed_seconds']=time.time()-t0;records.append(rec)
    (ROOT/'checks/MIXED_INSTRUMENT.json').write_text(json.dumps({'status':'executed instrumentation, not CM source','records':records},indent=2)+'\n')
