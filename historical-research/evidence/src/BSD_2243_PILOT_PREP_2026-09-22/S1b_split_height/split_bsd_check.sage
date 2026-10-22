# Consistency of PARI's split-multiplicative p-adic normalization (extended height regulator, L-invariant in
# ellpadicbsd) with the p-adic BSD formula, on small curves with split multiplicative p >= 5 and rank >= 1.
# Evidence about normalization only (p-adic BSD is a conjecture); not load-bearing for the sufficient certificate.
import sys
pari.allocatemem(2*10**9)
labs = ["43a1","53a1","57a1","65a1","77a1","91a1","91b1","106b1","118a1","122a1","143a1","155a1","158b1","203b1",
        "389a1","433a1","446d1","563a1","571b1","643a1","655a1","664a1","681b1","707a1","709a1","718b1","794a1"]
n = 8
for lab in labs:
    E = EllipticCurve(lab); N = E.conductor(); G = E.gens(); r = len(G)
    if r == 0: continue
    for p in prime_divisors(N):
        if p < 5 or N % p**2 == 0 or E.ap(p) != 1: continue
        try:
            e = pari(E); B = e.ellpadicbsd(p, n); R = e.ellpadicregulator(p, n, [list(P.xy()) for P in G])
            sh = B[1] / R
            print(lab, "p=%d" % p, "rank=%d" % r, "r_L=%s" % B[0], "BSDquot/Reg =", sh, " Sha_an =", E.sha().an()); sys.stdout.flush()
        except Exception as ex:
            print(lab, "p=%d" % p, "ERR", str(ex)[:100]); sys.stdout.flush()
