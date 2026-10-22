Es = EllipticCurve([0,-22735,0,106272484,0]).minimal_model()
C = Es.isogeny_class()
print("seed isogeny class size:", len(C), " degrees:", C.matrix()[0])
for i,F in enumerate(C.curves):
    ld = F.local_data(4547); j = F.j_invariant()
    ss = EllipticCurve_from_j(GF(4547)(j)).is_supersingular() if j.valuation(4547)>=0 else None
    print("  curve %d: %s" % (i, F.ainvs()))
    print("     4547: kodaira=%-5s c=%d v(j)=%d pot.%s" % (ld.kodaira_symbol(), ld.tamagawa_number(), j.valuation(4547), "SS" if ss else "ORD" if ss is not None else "MULT"))
    print("     N same:", F.conductor()==Es.conductor(), " prod c_v:", F.tamagawa_product(), " tors:", F.torsion_order())
print()
print("CNS p=2 exception for SEED: val_2(N)>=3 and NO p'|N with p'=3 mod 4 ?")
N=Es.conductor(); print("  val_2(N) =", N.valuation(2), "  primes = 3 mod 4 dividing N:", [p for p,_ in factor(N) if p%4==3])
