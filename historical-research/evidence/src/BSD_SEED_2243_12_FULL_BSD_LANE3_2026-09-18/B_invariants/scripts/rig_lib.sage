# Rigorous (ball-arithmetic) real period and canonical heights for elliptic curves over Q with Delta != 0.
# Omega: AGM with enclosure b_n <= AGM <= a_n.  Heights: Tate's series for the x-normalised archimedean Neron function
# on a translated model with x > 0 on E(R), with an explicit rigorous tail bound; non-archimedean part exact for points in E0.
# All normalisations: BSD / Cremona (hhat(P) ~ h(x(P))).

def real_roots_rig(E, RB):
    """Isolating intervals (certified, Sage real_roots) of the real roots of 4x^3+b2x^2+2b4x+b6, as RB balls, sorted increasing."""
    R = PolynomialRing(QQ,'X'); X = R.gen()
    f = 4*X**3 + E.b2()*X**2 + 2*E.b4()*X + E.b6()
    RIF_ = RealIntervalField(RB.precision())
    rts = sorted([r for r,_ in f.roots(RIF_)], key=lambda I: I.lower())
    return [RB(r) for r in rts]

def agm_rig(a, b, RB):
    """a>=b>0 balls. Returns ball enclosing AGM(a,b), using b_n <= AGM <= a_n."""
    for _ in range(200):
        a, b = (a+b)/2, (a*b).sqrt()
        if (a-b).upper() < (RB(2)**(-RB.precision()+20)).upper(): break
    lo = min(a.lower(), b.lower()); hi = max(a.upper(), b.upper())
    return RB(lo).union(RB(hi))

def real_period_rig(E, RB):
    """Omega_E = int_{E(R)} |omega| for the given model's invariant differential. Delta>0: 2*pi/AGM(sqrt(e1-e3),sqrt(e1-e2));
    Delta<0: pi/AGM with the complex-root formula is not needed here (both calibration curves and seed have Delta>0)."""
    assert E.discriminant() > 0
    e3, e2, e1 = real_roots_rig(E, RB)
    w1 = RB.pi() / agm_rig((e1-e3).sqrt(), (e1-e2).sqrt(), RB)
    return 2*w1, w1

def tate_lambda_rig(E, P, RB, N=110):
    """x-normalised archimedean Neron function lambda'(P) (lambda' = lambda_std + (1/12)log|Delta|), P a real point, via Tate's series
    on the translated model x~ = x + c (c chosen so x~ >= 1 on E(R)). Rigorous: ball arithmetic + tail bound 4^{-N} * M/6 with
    M >= sup_{E(R)} |log z|, z(t) = 1 - b4 t^2 - 2 b6 t^3 - b8 t^4 (b's of translated model)."""
    rts = real_roots_rig(E, RB)
    emin = rts[0]
    c = QQ(ceil(1 - emin.lower())) + 1   # then x~ = x + c >= e_min + c >= 2 on E(R) (margin for root-isolation width)
    # translated curve: x = x~ + r with r = -c
    Et = E.change_weierstrass_model([1, -c, 0, 0])
    b2, b4, b6, b8 = [QQ(v) for v in Et.b_invariants()]
    # rigorous check that x~ >= 1 on E(R): smallest root of translated 2-division poly >= 1
    rts_t = real_roots_rig(Et, RB)
    assert rts_t[0].lower() > 0.5, "translation failed"   # x~ >= e_min~ > 1/2 on E(R)
    # t-range on E(R): [0, 1/e1~] U [1/e2~, 1/e3~] (Delta>0) or [0, 1/e1~] (one real root)
    if len(rts_t) == 3:
        e3t, e2t, e1t = rts_t
        ranges = [(RB(0), 1/e1t), (1/e2t, 1/e3t)]
    else:
        e1t = rts_t[0]; ranges = [(RB(0), 1/e1t)]
    # rigorous range of z over the t-ranges: extrema of the quartic z(t) are at endpoints or at real critical points
    # (certified isolating intervals of the real roots of z'(t)); each is evaluated in interval arithmetic.
    RI = RealIntervalField(RB.precision())
    Rp = PolynomialRing(QQ,'X'); X = Rp.gen()
    zpoly = 1 - b4*X**2 - 2*b6*X**3 - b8*X**4
    crit = [r for r,_ in zpoly.derivative().roots(RI)]
    zlo = +Infinity; zhi = -Infinity
    for (lo, hi) in ranges:
        loI = RI(lo.lower(), lo.upper()); hiI = RI(hi.lower(), hi.upper())
        pts = [loI, hiI] + [r for r in crit if r.upper() >= loI.lower() and r.lower() <= hiI.upper()]
        for I in pts:
            zi = zpoly(I)
            zlo = min(zlo, zi.lower()); zhi = max(zhi, zi.upper())
    assert zlo > 0, "z not bounded away from 0"
    M = max(abs(RR(zlo).log()), abs(RR(zhi).log()))
    M = RR(M)*1.000001 + 1e-30
    # series
    xt = QQ(P[0]) + c
    t = RB(1)/RB(xt)
    S = RB(0); w4 = RB(1)
    for n in range(N):
        z = 1 - b4*t**2 - 2*b6*t**3 - b8*t**4
        S += w4*z.log()
        w = 4*t + b2*t**2 + 2*b4*t**3 + b6*t**4
        t = w/z
        w4 = w4/4
    tail = RB(4)**(-N) * RB(M)/6
    lam = RB(xt).log()/2 + S/8
    lam = lam + RB(0).add_error(tail.upper())
    return lam, dict(c=c, M=M, tail=tail, zlo=zlo, zhi=zhi)

def kill_multiplier(E):
    """k with k*P in E0(Q_p) for all p (E assumed minimal): lcm of Tamagawa numbers c_p (|E(Q_p)/E0(Q_p)| = c_p)."""
    return lcm([E.local_data(p).tamagawa_number() for p in ZZ(E.discriminant()).prime_factors()] + [1])

def hhat_rig(E, P, RB, N=110):
    """Canonical height (BSD normalisation) of P in E(Q), E a global minimal model. Uses Q = k*P in E0 everywhere:
    hhat(Q) = 2*lambda'_oo(Q) + log den(x(Q)); hhat(P) = hhat(Q)/k^2."""
    assert E.is_global_minimal_model() if hasattr(E,'is_global_minimal_model') else True
    k = kill_multiplier(E)
    Q = k*P
    for p in ZZ(E.discriminant()).prime_factors():
        assert Q.has_good_reduction(p), "k*P not in E0 at %s"%p
    lam, info = tate_lambda_rig(E, Q, RB, N=N)
    h = 2*lam + RB(QQ(Q[0]).denominator()).log()
    return h/k**2, dict(k=k, info=info)

def height_pairing_rig(E, P, Q, RB):
    hP,_ = hhat_rig(E,P,RB); hQ,_ = hhat_rig(E,Q,RB); hPQ,_ = hhat_rig(E,P+Q,RB)
    return hP, hQ, (hPQ - hP - hQ)/2

def reg_rig(E, P, Q, RB):
    a, b, c = height_pairing_rig(E, P, Q, RB)
    return a*b - c*c, (a, b, c)
