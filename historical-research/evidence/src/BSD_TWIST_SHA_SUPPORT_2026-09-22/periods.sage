R.<x> = QQ[]
Eseed = EllipticCurve([0,-22735,0,106272484,0])
print("SEED given  :", Eseed.ainvs(), "  is_minimal:", Eseed.is_minimal())
Es = Eseed.minimal_model(); print("SEED minimal:", Es.ainvs())
print("  conductor:", Es.conductor(), " = ", factor(Es.conductor()))
print("  disc:", Es.discriminant(), "  >0 ?", Es.discriminant()>0, "  real components:", Es.real_components())
print("  reduction at 7:", Es.local_data(7) if Es.conductor()%7==0 else "GOOD (7 does not divide N_seed)")
Et = EllipticCurve([0,159145,0,5207351716,0]).minimal_model()
print()
print("TWIST minimal:", Et.ainvs())
prec=200
bs = Es.period_lattice().basis(prec=prec); bt = Et.period_lattice().basis(prec=prec)
print()
print("SEED   basis w1,w2 :", bs[0]); print("                    ", bs[1])
print("TWIST  basis w1,w2 :", bt[0]); print("                    ", bt[1])
R7 = RealField(prec)(7).sqrt()
# candidate identities
for name,val in [("Om(twist)*sqrt7 / Im(w2_seed)", bt[0]*R7/bs[1].imag()),
                 ("Om(twist)*sqrt7 / (2*Im(w2_seed))", bt[0]*R7/(2*bs[1].imag())),
                 ("Om(twist) / Om(seed)", bt[0]/bs[0]),
                 ("Om(twist)*sqrt7 / Om(seed)", bt[0]*R7/bs[0])]:
    print("%-36s = %s" % (name, val))
