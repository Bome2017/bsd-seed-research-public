# Step 4 route (a): eclib/mwrank via Sage. Generators with proof, saturation of <P1,P2> with automatic (proved) index bound.
from sage.libs.eclib.all import mwrank_EllipticCurve, mwrank_MordellWeil
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
E=EllipticCurve([0,-5*A,0,4*A*B,0])
T=E(0,0); P1=E(A,6*n*A); P2=E(36*n^2,12*n*(m-2*n^2))
print("P1 =",P1," P2 =",P2)
G=E.gens(proof=True, use_database=False, algorithm='mwrank_lib')
print("E.gens(proof=True) =",G, " gens_certain:",E.gens_certain())
print("rank (proof=True):",E.rank(proof=True, only_use_mwrank=True))
print("heights (Sage, BSD normalization):", [g.height(precision=100) for g in G])
print("h(P1),h(P2) =",P1.height(precision=100),P2.height(precision=100))
M=E.height_pairing_matrix([P1,P2],precision=200); print("height pairing matrix <P1,P2> (200 bits):\n",M)
print("Reg(P1,P2) =",M.det())
Mg=E.height_pairing_matrix(G,precision=200); print("Reg(gens) =",Mg.det())
# express mwrank generators in terms of T,P1,P2: search small coefficients
for g in G:
    found=[]
    for a in range(-3,4):
        for b in range(-3,4):
            for e in range(2):
                if a*P1+b*P2+e*T==g: found.append((a,b,e))
    print("generator",g," = a*P1+b*P2+e*T with (a,b,e) in",found)
# Sage/eclib saturation of [P1,P2] with automatic index bound (max_prime=-1)
Emin=E.minimal_model(); phi=E.isomorphism_to(Emin)
Q1=phi(P1); Q2=phi(P2)
print("on minimal model: Q1 =",Q1," Q2 =",Q2)
c=Emin.mwrank_curve()
mw=mwrank_MordellWeil(c, True)
v=[]
for Q in [Q1,Q2]:
    x,y=Q.xy(); d=x.denominator().lcm(y.denominator()); v.append((x*d,y*d,d))
mw.process(v, saturation_bound=0)
print("--- eclib saturate(max_prime=-1) verbose ---")
res=mw.saturate(max_prime=-1, min_prime=2)
print("result (ok, index, unsat) =",res)
print("saturated basis:",mw.points(), " regulator:",mw.regulator())
print("E.saturation([P1,P2]) =",E.saturation([P1,P2]))
print("CPS_height_bound(minimal reduced model) =",Emin.CPS_height_bound())
print("silverman_height_bound(Emin, default) =",Emin.silverman_height_bound(), " mwrank:",Emin.silverman_height_bound(algorithm='mwrank'))
print("CPS on original (globally minimal, not reduced) model:", c.CPS_height_bound() )
