# Step 7a: E' = E/<T>: model, minimality, local data (PARI + Sage generic Tate), torsion, psi-images of generators, eclib saturation, mwrank gens.
from sage.libs.eclib.all import mwrank_MordellWeil
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
a=-5*A; b=4*A*B
E=EllipticCurve([0,a,0,b,0]); T=E(0,0); P1=E(A,6*n*A); P2=E(36*n^2,12*n*(m-2*n^2))
Ep=EllipticCurve([0,-2*a,0,a^2-4*b,0])
print("E' =",Ep.ainvs(), " (-2a, a^2-4b) = (",-2*a,",",a^2-4*b,") = (10A,",factor(a^2-4*b),")")
# check against Sage's own Velu isogeny
phi=E.isogeny(T); print("Sage Velu codomain:",phi.codomain().ainvs()," isomorphic to E'?",phi.codomain().is_isomorphic(Ep))
def psi(P):
    if P==0 or P==T: return Ep(0)
    x,y=P.xy(); return Ep(y^2/x^2, y*(b-x^2)/x^2)
def psihat(Q):
    X,Y=Q.xy()
    if X==0: return E(0)
    return E(Y^2/(4*X^2), Y*(a^2-4*b-X^2)/(8*X^2))
Q1=psi(P1); Q2=psi(P2); Tp=Ep(0,0)
print("psi(P1) =",Q1,"  psi(P2) =",Q2)
print("psihat(psi(P1)) == 2*P1:",psihat(Q1)==2*P1, "  psihat(psi(P2)) == 2*P2:",psihat(Q2)==2*P2)
print("psi(P1+P2) == psi(P1)+psi(P2):",psi(P1+P2)==Q1+Q2)
print("Delta' =",Ep.discriminant(),"=",factor(Ep.discriminant()), " sign:",sign(Ep.discriminant()), " real_components:",Ep.real_components())
print("c4' =",Ep.c4(),"=",factor(Ep.c4()))
print("is_global_minimal_model:",Ep.is_global_minimal_model()," minimal_model:",Ep.minimal_model().ainvs(), " iso:",Ep.isomorphism_to(Ep.minimal_model()))
print("conductor:",factor(Ep.conductor()), " same as E:",Ep.conductor()==E.conductor())
for p in Ep.conductor().prime_factors():
    ld=Ep.local_data(p, algorithm='generic'); ld2=Ep.local_data(p)
    print("p=%d generic-Tate: %s f=%d c=%d v(D)=%d split=%s nonsplit=%s | pari: %s c=%d"%(p,ld.kodaira_symbol(),ld.conductor_valuation(),ld.tamagawa_number(),ld.discriminant_valuation(),
        ld.has_split_multiplicative_reduction(),ld.has_nonsplit_multiplicative_reduction(),ld2.kodaira_symbol(),ld2.tamagawa_number()))
print("tamagawa_product':",Ep.tamagawa_product(), " root_number':",Ep.root_number())
print("torsion':",Ep.torsion_subgroup().invariants()," gens:",Ep.torsion_subgroup().gens(), " lutz_nagell:",Ep.torsion_subgroup(algorithm='lutz_nagell').invariants(), " two_torsion_rank:",Ep.two_torsion_rank())
print("#E'(F_p) p=5,7,11:",[Ep.change_ring(GF(p)).cardinality() for p in [5,7,11]])
print("Tp in psi(E(Q))? Tp is 2-divisible? division_points(2):",Tp.division_points(2))
# eclib saturation of {psi(P1), psi(P2)} with automatic index bound
Em=Ep.minimal_model(); iso=Ep.isomorphism_to(Em)
c=Em.mwrank_curve(); mw=mwrank_MordellWeil(c, True)
v=[]
for Q in [iso(Q1),iso(Q2)]:
    x,y=Q.xy(); d=x.denominator().lcm(y.denominator()); v.append((x*d,y*d,d))
mw.process(v, saturation_bound=0)
res=mw.saturate(max_prime=-1, min_prime=2)
print("eclib saturate(psi P1, psi P2) on minimal E': (ok,index,unsat) =",res)
sat=[(~iso)(Em(pt)) for pt in [[QQ(t[0])/QQ(t[2]),QQ(t[1])/QQ(t[2])] for t in mw.points()]]
print("saturated basis on E' model:",sat)
print("Reg(psi P1, psi P2) =",Ep.regulator_of_points([Q1,Q2],precision=200), "  4*Reg(E) =",4*E.regulator_of_points([P1,P2],precision=200))
print("Reg(saturated) =",Ep.regulator_of_points(sat,precision=200))
G=Ep.gens(proof=True, use_database=False, algorithm='mwrank_lib'); print("E'.gens(proof=True) =",G," certain:",Ep.gens_certain(), " Reg:",Ep.regulator_of_points(G,precision=200))
# express sat basis in terms of psi-images and Tp
for g in sat+G:
    f=[(i,j,e) for i in range(-3,4) for j in range(-3,4) for e in range(2) if 2*g==i*Q1+j*Q2+e*Tp or g==i*Q1+j*Q2+e*Tp]
    f2=[(i,j,e) for i in range(-3,4) for j in range(-3,4) for e in range(2) if 2*g==i*Q1+j*Q2+e*Tp]
    print("  ",g,": g = combo",[t for t in f if g==t[0]*Q1+t[1]*Q2+t[2]*Tp],"; 2g = combo",f2)
print("Omega' (PARI 2*omega[1], 53 bits):",2*Ep.pari_curve().omega()[0], "  Omega (E):",2*E.pari_curve().omega()[0])
print("CPS bound E' (minimal):",Em.CPS_height_bound(), " Silverman:",Em.silverman_height_bound())
