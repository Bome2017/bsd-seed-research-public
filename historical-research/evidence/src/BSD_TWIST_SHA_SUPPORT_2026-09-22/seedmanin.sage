Es = EllipticCurve([0,-22735,0,106272484,0]).minimal_model()
N = Es.conductor()
print("SEED minimal:", Es.ainvs(), "  N =", N, "=", factor(N))
print("odd primes l with l^2 | N_seed  (ARS Cor 3.7 candidate support of c_0(E_seed)):",
      [l for l,e in factor(N) if l>2 and e>=2])
print("is 7 among them?", 7 in [l for l,e in factor(N) if l>2 and e>=2], "   (7 | N_seed ?", N%7==0, ")")
print()
for q in [2,3,2243,4547,5843]:
    ld = Es.local_data(q); vj = Es.j_invariant().valuation(q)
    ss = None
    if vj>=0 and q>3:
        ss = EllipticCurve_from_j(GF(q)(Es.j_invariant())).is_supersingular()
    print("  q=%-5d kodaira=%-6s c_q=%d additive=%s v_q(j)=%d  pot.%s  q mod 4 = %d" % (
        q, ld.kodaira_symbol(), ld.tamagawa_number(), ld.has_additive_reduction(), vj,
        ("SUPERSINGULAR" if ss else "ORDINARY") if ss is not None else "-", q%4))
print()
print("torsion:", Es.torsion_order(), "  tamagawa product:", Es.tamagawa_product())
print("isogeny class size:", len(Es.isogeny_class()), " degrees:", Es.isogeny_class().matrix()[0])
print("non_surjective:", Es.galois_representation().non_surjective())
print("real components:", Es.real_components(), "  disc>0:", Es.discriminant()>0)
print("rank (from record, not recomputed): 2")
