# Step 5: 2-Selmer rank / Sha[2] of the seed by three independent 2-descents, with calibration on Cremona curves of known Sha.
import subprocess, re
from sage.schemes.elliptic_curves.descent_two_isogeny import two_descent_by_two_isogeny
MW='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/mwrank'
def mwrank_lines(ainvs):
    out=subprocess.run([MW,'-q','-v','1','-S','-1'],input=str(list(ainvs)).replace(' ','')+'\n',capture_output=True,text=True,timeout=300).stdout
    keep=[l.strip() for l in out.splitlines() if re.search(r'rk\(|Rank|rank\(E\)|#III|#E\(Q\)/2E|Sha|phi\'\(III|determined',l)]
    return keep
def pari_info(E):
    e=E.pari_curve(); r1,r2,s,L=e.ellrank(); T=E.two_torsion_rank()
    nc=len(pari.ell2cover(e))
    return dict(r1=int(r1),r2=int(r2),s=int(s),T=T,C=int(r2)+T+int(s),ell2cover=nc)
cal=[('14a1',None),('1088j1',None),('1088j2',None),('960d1',None),('1610f3',None),('389a1',None),('571a1',None)]
print("=== CALIBRATION (expected dim Sel2 = rank + dim E(Q)[2] + dim Sha[2]; Sha from Cremona table, Sha=4 read as (Z/2)^2) ===")
for lab,_ in cal:
    E=EllipticCurve(lab)
    sha=E.sha().an_numerical() if False else None
    print("\n---",lab,E.ainvs()," rank(table)=",E.rank(), " tors=",E.torsion_order()," two_torsion_rank=",E.two_torsion_rank(), " Sha_an(Cremona db)=", E.database_attributes().get('sha') if hasattr(E,'database_attributes') else 'n/a')
    print("  PARI ellrank:",pari_info(E))
    if E.two_torsion_rank()>0:
        print("  Sage/Miller two_descent_by_two_isogeny (n1,n2,n1',n2'):",two_descent_by_two_isogeny(E,verbosity=0))
    for l in mwrank_lines(E.ainvs()): print("  mwrank:",l)
print("\n\n=== SEED ===")
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
E=EllipticCurve([0,-5*A,0,4*A*B,0])
print("PARI ellrank:",pari_info(E))
print("Sage/Miller two_descent_by_two_isogeny, verbosity=1:")
res=two_descent_by_two_isogeny(E,verbosity=1)
print("returned (n1,n2,n1',n2') =",res)
for l in mwrank_lines(E.ainvs()): print("  mwrank:",l)
print("Sage selmer_rank(pari) =",E.selmer_rank(algorithm='pari')," selmer_rank(mwrank) =",E.selmer_rank(algorithm='mwrank'), " rank_bound(mwrank) =",E.rank_bound(algorithm='mwrank'))
