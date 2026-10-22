# Exploratory check (Python, not kernel-checked): local images of P1, P2 at the auxiliary
# bad prime q for the exceptional coefficient primes p in {19, 59, 487}.
# E: y^2 = x^3 - x^2 - 66020924 x - 65074271436 (minimal model).
a2, a4, a6 = -1, -66020924, -65074271436
P1 = (-3031, 327384); P2 = (-2394, 281520)

def add(P, Q, q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if (x1 - x2) % q == 0:
        if (y1 + y2) % q == 0: return None
        lam = (3*x1*x1 + 2*a2*x1 + a4) * pow(2*y1, -1, q) % q
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, q) % q
    x3 = (lam*lam - a2 - x1 - x2) % q
    y3 = (-(y1 + lam*(x3 - x1))) % q
    return (x3, y3)

def mul(n, P, q):
    R = None; B = P
    while n:
        if n & 1: R = add(R, B, q)
        B = add(B, B, q); n >>= 1
    return R

def singular_x(q):
    # singular point of the reduction: f(x) = x^3 + a2 x^2 + a4 x + a6 and f'(x) both vanish
    return [x for x in range(q) if (x**3 + a2*x*x + a4*x + a6) % q == 0 and (3*x*x + 2*a2*x + a4) % q == 0]

out = {}
for (p, q, n, c) in [(19, 2243, 2242, 1), (59, 2243, 2242, 1), (487, 5843, 5844, 2)]:
    sx = singular_x(q)
    res = {}
    for name, P in [("P1", P1), ("P2", P2)]:
        Pq = (P[0] % q, P[1] % q)
        nonsing = not (Pq[0] in sx and Pq[1] == 0)
        Pc = mul(c, Pq, q) if c > 1 else Pq   # move into E_0 (c prime to p)
        img = mul(n // p, Pc, q)               # zero iff Pc in p * E~_ns(F_q) (cyclic, p || n)
        res[name] = {"reduction_nonsingular": nonsing, "local_class_zero": img is None}
    out[p] = {"q": q, "singular_x": sx, **res}
    print(p, out[p])
