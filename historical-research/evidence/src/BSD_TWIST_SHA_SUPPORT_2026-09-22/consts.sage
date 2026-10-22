Em = EllipticCurve([0,159145,0,5207351716,0]).minimal_model()
print("is_minimal:", Em.is_minimal())
print("root_number:", Em.root_number())
print("torsion t:", Em.torsion_subgroup().order())
print("real_components:", Em.real_components())
print("d = _multiple_of_degree_of_isogeny_to_optimal_curve:", Em._multiple_of_degree_of_isogeny_to_optimal_curve())
print("isogeny class size:", len(Em.isogeny_class()))
print("isogeny degrees:", Em.isogeny_class().matrix()[0])
print("conductor squarefree?", Em.conductor().is_squarefree())
print("omega_1 (200 bits):", Em.period_lattice().basis(prec=200)[0])
try:
    print("manin_constant():", Em.manin_constant())
except Exception as e:
    print("manin_constant() raised:", type(e).__name__, e)
