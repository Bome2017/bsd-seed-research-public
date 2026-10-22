import sys
for l in open('curves_s1a.txt'):
    if l.startswith('#'): continue
    lab, ai, N, M, aM, w = l.strip().split('|'); ai = [int(x) for x in ai.split()]; M = int(M)
    E = EllipticCurve(ai)
    assert E.conductor() == int(N) and E.ap(M) == int(aM) and E.root_number() == int(w) and E.discriminant() > 0, lab
    print("CURVE", lab, E.conductor(), E.root_number(), E.ap(M), E.period_lattice().basis()[0]); sys.stdout.flush()
    for sg in [1, -1]:
        f = E.modular_symbol(sign=sg, implementation='eclib')
        for m in [M, M**2, M**3]:
            for b in range(1, m):
                if gcd(b, m) == 1: print("SYM", lab, sg, m, b, f(QQ(b)/m))
        sys.stdout.flush()
