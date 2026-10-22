load('/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/scripts/rig_lib.sage')
RB = RealBallField(4000)
def show(x, d=45): return "%s  (radius %.3e)" % (x.mid().n(digits=d), float(x.rad()))
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
E=EllipticCurve([0,-5*A,0,4*A*B,0]); T=E(0,0); P1=E(A,6*n*A); P2=E(36*n^2,12*n*(m-2*n^2))
bal=load('/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/out/s06_seed_balls.sobj')
Om=bal['Om']; Reg=bal['Reg']
cp=E.tamagawa_product(); tor=E.torsion_order()
C = Om*Reg*cp/tor**2
print("=== E ===  prod c_p =",cp," #tors =",tor)
print("C := Omega*Reg*prod c_p/#tors^2 =", show(C,50))
print("PARI ellbsd(E)*Reg (non-rigorous cross-check):", RB(pari('default(realprecision,80); ellbsd(ellinit([0,-22735,0,106272484,0]))').sage())*Reg)
# ---------------- E' = E/<T> ----------------
psi = E.isogeny(T); Ev = psi.codomain()
print("\n=== E' = E/<T> (Velu model) ===", Ev.ainvs())
# normalise to y^2 = x(x^2 + a'x + b') form: Velu model may be translated; find iso to standard form
Estd = EllipticCurve([0,10*A,0,9*m*A,0])
iso_std = Ev.isomorphism_to(Estd); print("iso Velu -> standard [0,10A,0,9mA,0]:", iso_std)
Em = Estd.minimal_model(); iso_min = Estd.isomorphism_to(Em)
print("minimal model E'_min =", Em.ainvs(), "  via", iso_min, "  global minimal of standard form:", Estd.is_global_minimal_model())
print("Delta' =", Em.discriminant(), "=", factor(Em.discriminant()), " sign:", sign(Em.discriminant()), " real comps:", Em.real_components())
print("conductor' =", factor(Em.conductor()), " same as E:", Em.conductor()==E.conductor())
for p in ZZ(Em.discriminant()).prime_factors():
    ld=Em.local_data(p, algorithm='generic'); ld2=Em.local_data(p)
    print("  p=%d kodaira=%s c_p=%d (pari: %s, %d) split=%s nonsplit=%s"%(p, ld.kodaira_symbol(), ld.tamagawa_number(), ld2.kodaira_symbol(), ld2.tamagawa_number(), ld.has_split_multiplicative_reduction(), ld.has_nonsplit_multiplicative_reduction()))
cpv = Em.tamagawa_product(); print("prod c_p(E') =", cpv)
tv = Em.torsion_subgroup(); print("E'(Q)_tors:", tv.invariants(), " lutz_nagell:", Em.torsion_subgroup(algorithm='lutz_nagell').invariants())
g=0
for p in primes(5,80):
    if Em.discriminant() % p: g=gcd(g, Em.reduction(p).cardinality())
print("gcd #E'(F_p), good p in [5,80]:", g)
torv = Em.torsion_order()
# points on the standard model
Tp = Estd(0,0)
phi = iso_std*psi   # E -> Estd
iP1 = phi(P1); iP2 = phi(P2)
print("psi(P1) =", iP1, " psi(P2) =", iP2, " psi(T) =", phi(T))
Rp = Estd(-2243, -107664)   # from mwrank output ("Curve E' Point [-2243:-107664:1]"); verified on curve here
print("R' =", Rp, "on curve: True")
# Kummer map alpha': E'(Q) -> Q*/Q*^2 for E': y^2 = x^3 + a'x^2 + b'x : (X,Y) -> X (X != 0), T'=(0,0) -> b', O -> 1.
# It is a homomorphism with kernel = image of the isogeny INTO E' from y^2 = x^3 - 2a'x^2 + (a'^2-4b')x  (Silverman-Tate III.5);
# that curve is y^2 = x^3 - 20A x^2 + 64AB x, isomorphic to E via (x,y) = (4x_E, 8y_E), so the kernel is psi(E(Q)).
# (An earlier run of this script used a'^2-4b' for alpha'(T'); corrected here: alpha'(T') = b' = 9mA.)
def sqf(q): q=QQ(q); return (q.numerator()*q.denominator()).squarefree_part()
ap, bp = 10*A, 9*m*A
alpha = lambda P: 1 if P.is_zero() else (sqf(bp) if P[0]==0 else sqf(P[0]))
print("alpha'(T') =", alpha(Tp), " alpha'(R') =", alpha(Rp), " alpha'(T'+R') =", alpha(Tp+Rp), " alpha'(psi P1) =", alpha(iP1), " alpha'(psi P2) =", alpha(iP2))
print("homomorphism check alpha'(T')*alpha'(R') == alpha'(T'+R') mod squares:", sqf(alpha(Tp)*alpha(Rp))==alpha(Tp+Rp))
print("images of T', R' independent in Q*/Q*^2 (none of alpha(T'), alpha(R'), alpha(T'+R') is 1):", all(v!=1 for v in [alpha(Tp),alpha(Rp),alpha(Tp+Rp)]))
# 2R' in psi(E(Q)) + <T'> : find the combination
found=[]
for a in range(-3,4):
    for b in range(-3,4):
        for e in range(2):
            for d in range(2):
                if 2*Rp == phi(a*P1+b*P2+e*T) + d*Tp: found.append((a,b,e,d))
print("2R' = psi(a P1 + b P2 + e T) + d T' with (a,b,e,d) in", found)
# candidate basis of E'(Q)/tors: choose from {R', psi P1, psi P2}
toM = iso_min
cands = {'R':Rp, 'psiP1':iP1, 'psiP2':iP2}
Hm = Em.height_pairing_matrix([toM(Rp),toM(iP1),toM(iP2)], precision=200)
print("Gram(R', psiP1, psiP2) on E'_min (200 bits):\n", Hm, "\n det =", Hm.det())
a,b,e,d = found[0]
basis = (Rp, iP2) if a % 2 else (Rp, iP1)
print("chosen basis of E'(Q)/tors:", basis, "(since 2R' = psi(%d P1 + %d P2 + ...) and the coefficient of the omitted point is odd)"%(a,b))
Bm = [toM(Q) for Q in basis]
Omv, w1v = real_period_rig(Em, RB)
Regv, (h1v,h2v,pv) = reg_rig(Em, Bm[0], Bm[1], RB)
print("Omega' (rigorous, E'_min, Delta'>0 => 2*omega_1') =", show(Omv,50))
print("Reg' (rigorous) =", show(Regv,50))
print("  hhat'(R') =", show(h1v,40), " hhat'(basis2) =", show(h2v,40), " pairing =", show(pv,40))
print("check hhat'(psi P1) = 2 hhat(P1):", show(hhat_rig(Em, toM(iP1), RB)[0],40), " vs ", show(2*bal['h1'],40))
# eclib independent: gens and saturation on E'
Gv = Em.gens(proof=True, use_database=False)
print("eclib E'.gens(proof=True) =", Gv, " certain:", Em.gens_certain(), " regulator:", Em.regulator_of_points(Gv, precision=200))
print("eclib saturation of chosen basis:", Em.saturation(Bm))
print("Sage/eclib saturation of [psiP1, psiP2] (index should be 2):", Em.saturation([toM(iP1),toM(iP2)])[1:])
Cv = Omv*Regv*cpv/torv**2
print("\nC' := Omega'*Reg'*prod c_p'/#tors'^2 =", show(Cv,50), "  (#tors' =", torv, ")")
print("C'/C =", show(Cv/C,50))
print("Omega'*prod c'/(Omega*prod c) =", show(Omv*cpv/(Om*cp),40), "   Reg'/Reg =", show(Regv/Reg,40))
save(dict(C=C, Cv=Cv, Omv=Omv, Regv=Regv), '/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/out/s07_balls_rerun.sobj')
