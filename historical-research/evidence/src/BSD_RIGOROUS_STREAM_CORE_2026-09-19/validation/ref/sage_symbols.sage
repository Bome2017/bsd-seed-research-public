# Exact eclib modular symbols [b/m]^+ and [b/m]^- (Sage default normalisation) for the rigorous-core validation.
# Output lines: SYM label sign m b value   and   CURVE label N w omega1 omega2
import sys
curves = [("37a1", [0,0,1,-1,0], [25,5,7,27]), ("389a1", [0,1,1,-2,0], [25,5,7,27]), ("446d1", [1,-1,0,-4,4], [25,5,7,27]),
          ("15a1", [1,1,1,-10,-10], [9,27,81]), ("24a1", [0,-1,0,-4,4], [9,27,81]), ("57b1", [1,0,1,-7,5], [9,27,81]),
          ("141a1", [0,1,1,-12,2], [9,27,81]), ("141d1", [0,-1,1,-1,0], [9,27,81])]
for lab, ai, ms in curves:
    E = EllipticCurve(ai)
    L = E.period_lattice().basis()
    print("CURVE", lab, E.conductor(), E.root_number(), L[0], L[1]); sys.stdout.flush()
    for sg in [1, -1]:
        try:
            f = E.modular_symbol(sign=sg, implementation='eclib')
            impl = 'eclib'
        except Exception as e:
            f = E.modular_symbol(sign=sg, implementation='num'); impl = 'num'
        for m in ms:
            vals = [(b, f(QQ(b)/m)) for b in range(1, m) if gcd(b, m) == 1]
            for b, v in vals:
                print("SYM", lab, sg, m, b, v, impl)
        sys.stdout.flush()
