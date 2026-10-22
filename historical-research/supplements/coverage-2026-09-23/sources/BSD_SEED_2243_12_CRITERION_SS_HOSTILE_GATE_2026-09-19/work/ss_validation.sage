# Consistency validation of Criterion SS (not a proof): theta_1 mod p from exact eclib symbols [a/p^2]^+ at a good supersingular p.
# theta_1 (full sum over (Z/p^2)^x) = sum_a x_a gamma^{j(a)}, gamma = image of 1+p, j(a) = -(a^(p-1)-1)/p mod p (Fermat quotient);
# in F_p[X]/(X^p) (gamma -> 1+X): c_k = sum_a x_a C(j(a), k) mod p.  Rank r: forced c_0 = ... = c_{r-1} = 0 (mod p; c_0 = 0 exactly).
import sys
tests = [("446d1", [1,-1,0,-4,4], 19), ("446d1", [1,-1,0,-4,4], 61), ("389a1", [0,1,1,-2,0], 107), ("571b1", [0,-1,1,-929,-10595], 17)]
for lab, ai, p in tests:
    E = EllipticCurve(ai); assert E.ap(p) == 0 and E.conductor() % p != 0
    r = E.rank(); ms = E.modular_symbol(sign=1, implementation='eclib')
    m = p * p; xs = {}
    for a in range(1, m):
        if a % p: xs[a] = ms(QQ(a) / m)
    assert all(x.denominator() % p != 0 for x in xs.values())
    def j(a): return (-((pow(a, p - 1, p * p) - 1) // p)) % p
    c = [sum(xs[a] * binomial(j(a), k) for a in xs) for k in range(4)]
    cmod = [ (GF(p)(x.numerator()) / GF(p)(x.denominator())) for x in c]
    # independent check of the labelling: a/omega(a) = (1+p)^j(a) mod p^2
    ok = all(Mod(a, m) * Mod(pow(a, p, m), m)**-1 == Mod(1 + p, m)**j(a) for a in xs)
    rho = E.galois_representation().is_surjective(p)
    sha = E.sha().an_numerical() if r > 0 else E.sha().an()
    print(f"CURVE {lab} p={p} rank={r} rho_p surjective={rho} Sha_an={sha} | labelling check {ok} | c_0 exact = {c[0]} | c_0..c_3 mod p = {list(cmod)}")
    first = next((k for k in range(4) if cmod[k] != 0), None)
    print(f"   first nonzero coefficient index mod p: {first} (rank {r}); criterion (c_r != 0 mod p) {'APPLIES -> Sha[p^inf] = 0 certified' if first == r else 'does not apply'}")
    sys.stdout.flush()
