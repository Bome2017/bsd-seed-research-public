E = EllipticCurve([0,159145,0,5207351716,0]).minimal_model()
C = E.isogeny_class()
print("isogeny class size:", len(C), "  degree matrix row 0:", C.matrix()[0])
for i,F in enumerate(C.curves):
    print()
    print("--- curve %d : %s ---" % (i, F.ainvs()))
    print("    conductor:", F.conductor()==E.conductor(), "  torsion:", F.torsion_order(), "  tamagawa prod:", F.tamagawa_product())
    print("    j:", F.j_invariant())
    for q in [7,4547]:
        ld=F.local_data(q); vj=F.j_invariant().valuation(q)
        ss=None
        if vj>=0:
            ss=EllipticCurve_from_j(GF(q)(F.j_invariant())).is_supersingular()
        print("      q=%-5d kodaira=%-6s c_q=%d  v_q(j)=%d  pot.%s" % (q, ld.kodaira_symbol(), ld.tamagawa_number(), vj, ("SUPERSINGULAR" if ss else "ORDINARY") if ss is not None else "MULT"))
    print("    omega_1:", F.period_lattice().basis(prec=120)[0])
    print("    real components:", F.real_components())
print()
print("Mazur rational-isogeny list for Edi89 Thm 4.6.3 condition (2): p not in {2,3,5,7,11,13,17,19,37,43,67,163}")
print("  does E admit a Q-isogeny of degree 4547?", 4547 in [d for d in C.matrix()[0]])
print("  does E admit a Q-isogeny of degree 7?   ", 7 in [d for d in C.matrix()[0]])
