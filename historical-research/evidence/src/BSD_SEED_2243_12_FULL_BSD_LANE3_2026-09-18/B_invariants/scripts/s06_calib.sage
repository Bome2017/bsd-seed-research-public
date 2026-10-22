load('/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/scripts/rig_lib.sage')
RB = RealBallField(4000)
def show(x, d=50): return "%s +/- %.3e" % (x.mid().n(digits=d), float(x.rad()))
cal = {
 '389a1': dict(gens=[(-1,1),(0,0)], Reg='0.15246017794314375162432475705', Om='4.9804251217101101506427155839'),
 '1088j1': dict(gens=[(1,4),(5,8)], Reg='0.53166563164488849625626244683', Om='3.4388774203903975425030664350'),
 '1088j2': dict(gens=[(-5,8),(11,24)], Reg='0.53166563164488849625626244683', Om='1.7194387101951987712515332175'),
}
for lab, d in cal.items():
    E = EllipticCurve(lab); assert E.is_global_minimal_model() if hasattr(E,'is_global_minimal_model') else True
    Om, w1 = real_period_rig(E, RB)
    P, Q = [E(g) for g in d['gens']]
    R, (a,b,c) = reg_rig(E, P, Q, RB)
    print("====", lab, E.ainvs(), " Delta =", E.discriminant(), " real comps =", E.real_components())
    print("  Omega (rig) =", show(Om), "  rad =", Om.rad())
    print("  Cremona Omega =", d['Om'], "  |diff| =", (Om - RB(d['Om'])).abs().upper())
    print("  PARI omega[1] =", E.pari_curve().omega()[0], " ; 2*omega[1] vs rig:", (2*RB(E.pari_curve().omega()[0]) - Om).abs().upper())
    print("  Reg (rig) =", show(R), " rad =", R.rad())
    print("  Cremona Reg =", d['Reg'], "  |diff| =", (R - RB(d['Reg'])).abs().upper())
    print("  Sage regulator_of_points (200 bits) =", E.regulator_of_points([P,Q], precision=200))
    print("  hhat(P) rig =", show(a,35), " Sage:", P.height(precision=120))
