load('/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/scripts/rig_lib.sage')
RB = RealBallField(4000)
def show(x, d=60): return "%s  (radius %.3e)" % (x.mid().n(digits=d), float(x.rad()))
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
E=EllipticCurve([0,-5*A,0,4*A*B,0])
T=E(0,0); P1=E(A,6*n*A); P2=E(36*n^2,12*n*(m-2*n^2))
print("E =",E.ainvs(), " global minimal:", E.is_global_minimal_model(), " Delta>0:", E.discriminant()>0)
# exact 2-division roots: 0, (5A -/+ 3 sqrt(mA))/2 ; compare with certified isolation
rts = real_roots_rig(E, RB)
s = RB(m*A).sqrt()
exact = [RB(0), (5*A - 3*s)/2, (5*A + 3*s)/2]
print("root isolation vs exact closed form overlap:", [rts[i].overlaps(exact[i]) for i in range(3)])
Om, w1 = real_period_rig(E, RB)
# independent closed-form computation with exact roots
w1b = RB.pi()/agm_rig((exact[2]-exact[0]).sqrt(), (exact[2]-exact[1]).sqrt(), RB)
print("omega_1 (real period of identity component) =", show(w1))
print("omega_1 via exact roots                     =", show(w1b), " overlap:", w1.overlaps(w1b))
print("Omega_E = 2*omega_1 (two real components)   =", show(Om))
print("PARI E.omega[1] (default 53-bit) =", E.pari_curve().omega()[0])
k = kill_multiplier(E); print("kill multiplier k (lcm c_p) =", k, "; 2*P1, 2*P2, 2*(P1+P2) in E0 at all bad p:",
    all((k*Q).has_good_reduction(p) for Q in [P1,P2,P1+P2] for p in ZZ(E.discriminant()).prime_factors()))
print("E0 membership of P1,P2 themselves:", {str(p):[P1.has_good_reduction(p),P2.has_good_reduction(p),(P1+P2).has_good_reduction(p)] for p in ZZ(E.discriminant()).prime_factors()})
h1, i1 = hhat_rig(E, P1, RB); h2, i2 = hhat_rig(E, P2, RB); h12, i12 = hhat_rig(E, P1+P2, RB)
print("Tate-series data P1:", {kk:(str(v)[:40]) for kk,v in i1['info'].items()})
pair = (h12 - h1 - h2)/2
Reg = h1*h2 - pair**2
print("hhat(P1)        =", show(h1))
print("hhat(P2)        =", show(h2))
print("hhat(P1+P2)     =", show(h12))
print("<P1,P2>         =", show(pair))
print("Reg(P1,P2)      =", show(Reg))
print("check: T-translate hhat(P1+T) =", show(hhat_rig(E,P1+T,RB)[0]))
# cross-checks with non-rigorous independent implementations
ep = E.pari_curve()
import cypari2
print("PARI ellheight at 400 bits: h(P1) =", pari('default(realprecision,120)') , pari('ellheight(ellinit([0,-22735,0,106272484,0]),[4547,327384])'))
print("PARI Reg at 120 digits:", pari('matdet(ellheightmatrix(ellinit([0,-22735,0,106272484,0]),[[4547,327384],[5184,281520]]))'))
print("Sage regulator_of_points (400 bits):", E.regulator_of_points([P1,P2], precision=400))
print("|Reg_rig - Reg_PARI| <", (Reg - RB(pari('matdet(ellheightmatrix(ellinit([0,-22735,0,106272484,0]),[[4547,327384],[5184,281520]]))').sage())).abs().upper())
print("PARI omega at 120 digits:", pari('ellinit([0,-22735,0,106272484,0]).omega[1]'))
save(dict(Om=Om, w1=w1, Reg=Reg, h1=h1, h2=h2, pair=pair), '/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/out/s06_seed_balls.sobj')
