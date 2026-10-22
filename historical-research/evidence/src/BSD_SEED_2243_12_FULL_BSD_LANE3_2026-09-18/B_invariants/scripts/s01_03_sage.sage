# Steps 1-3 cross-check in Sage (independent of the PARI script's code path: Sage uses its own Tate's algorithm in ell_local_data.py)
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
E=EllipticCurve([0,-5*A,0,4*A*B,0])
print("E =",E)
print("is_minimal():",E.is_minimal(), " is_global_minimal_model:", E.is_global_minimal_model() if hasattr(E,'is_global_minimal_model') else 'n/a')
Em=E.minimal_model(); print("minimal_model():",Em.ainvs())
print("isomorphism E->Em:", E.isomorphism_to(Em))
print("discriminant:",E.discriminant(),"=",factor(E.discriminant()))
print("conductor:",E.conductor(),"=",factor(E.conductor()))
print("real_components():",E.real_components())
print("torsion_order():",E.torsion_order(), " torsion_subgroup gens:",E.torsion_subgroup().gens(), " (algorithm pari default)")
print("torsion via 'doud':",E.torsion_order(), E.torsion_subgroup(algorithm='doud').invariants() if True else '')
print("torsion via 'lutz_nagell':",E.torsion_subgroup(algorithm='lutz_nagell').invariants())
print("two_torsion_rank:",E.two_torsion_rank())
for p in E.conductor().prime_factors():
    ld=E.local_data(p, algorithm='generic')
    ld2=E.local_data(p)  # default (pari)
    print("p=%d  generic-Tate: kodaira=%s f=%d c_p=%d disc_val=%d  split?%s nonsplit?%s additive?%s | pari: kodaira=%s c_p=%d"%(
        p, ld.kodaira_symbol(), ld.conductor_valuation(), ld.tamagawa_number(), ld.discriminant_valuation(),
        ld.has_split_multiplicative_reduction(), ld.has_nonsplit_multiplicative_reduction(), ld.has_additive_reduction(),
        ld2.kodaira_symbol(), ld2.tamagawa_number()))
print("tamagawa_product:",E.tamagawa_product())
print("root_number:",E.root_number())
print("j:",E.j_invariant())
