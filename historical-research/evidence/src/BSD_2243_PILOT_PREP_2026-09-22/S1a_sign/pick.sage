# pick small curves with M in {5,7}, M || N, multiplicative (split a_M=+1 / nonsplit a_M=-1), both root numbers
from sage.databases.cremona import CremonaDatabase
C = CremonaDatabase()
want = {}
for N in [Integer(n) for n in range(10, 1500)]:
    for M in [5, 7]:
        if N % M or N % (M*M) == 0: continue
        for lab, data in sorted(C.allcurves(N).items()):
            if not lab.endswith('1'): continue
            E = EllipticCurve(data[0]); aM = E.ap(M); w = E.root_number()
            if E.discriminant() <= 0: continue
            key = (M, aM, w, len(N.prime_divisors()) > 1)
            if key not in want: want[key] = (str(N)+lab, data[0])
for k in sorted(want): print(k, want[k])
