# Exact eclib modular symbols [b/m]^{+,-} for 234446a1 (rank 4), m = 25, 5, 7, 27.  Output: SYM label sign m b value eclib
import sys
E = EllipticCurve([1,-1,0,-79,289]); L = E.period_lattice().basis()
print("CURVE 234446a1", E.conductor(), E.root_number(), L[0], L[1]); sys.stdout.flush()
for sg in [1, -1]:
    f = E.modular_symbol(sign=sg, implementation='eclib')
    for m in [25, 5, 7, 27]:
        for b in range(1, m):
            if gcd(b, m) == 1: print("SYM 234446a1", sg, m, b, f(QQ(b)/m), "eclib")
        sys.stdout.flush()
