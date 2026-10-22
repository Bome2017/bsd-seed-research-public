"""Independent check of the BSD-predicted #Sha(E^{-7}/Q) for the seed's twist by -7.
Pure Python floats (no PARI/mpmath available). Inputs: seed model, L(E^{-7},1) interval from release K.2.
Everything printed is a NUMERICAL check of a prediction, not a theorem."""
import math

# Seed E: y^2 = x^3 + a x^2 + b x  (minimal, u = 1 per claim A.1)
a, b = -22735, 106272484
d = -7
# Twist E^d: y^2 = x^3 + d a x^2 + d^2 b x  (minimal: d is a 2-adic unit square (-7 = 1 mod 8), v_7(Delta)=6)
ad, bd = d * a, d * d * b
print("twist model: y^2 = x^3 + %d x^2 + %d x" % (ad, bd))

def real_roots(A, B):
    # roots of x^3 + A x^2 + B x = x (x^2 + A x + B)
    disc = A * A - 4 * B
    assert disc > 0, "expected three real roots"
    s = math.sqrt(disc)
    return sorted([0.0, (-A + s) / 2, (-A - s) / 2], reverse=True)

def agm(x, y):
    for _ in range(60):
        x, y = (x + y) / 2, math.sqrt(x * y)
        if abs(x - y) < 1e-15 * x:
            break
    return x

def real_period(A, B):
    e1, e2, e3 = real_roots(A, B)
    # integral over the identity component of dx/(2y) = pi / AGM(sqrt(e1-e3), sqrt(e1-e2)); two components => x2
    return 2 * math.pi / agm(math.sqrt(e1 - e3), math.sqrt(e1 - e2))

Om_E = real_period(a, b)
Om_T = real_period(ad, bd)
print("Omega_E      = %.12f" % Om_E)
print("Omega_E^{-7} = %.12f   (Omega_E/sqrt7 = %.12f)" % (Om_T, Om_E / math.sqrt(7)))

# Tamagawa numbers of E^{-7} (twist rules; chi_{-7} unramified away from 7):
# 2: chi trivial at 2 (-7 is a 2-adic square) -> same as E: I1*, c=2
# 3: (-7/3) = -1: nonsplit I2 -> split I2: c = 2
# 2243: (-7/2243) = -1: split I1 -> nonsplit I1: c = 1
# 4547: (-7/4547) = +1 (split in K): type III unchanged: c = 2
# 5843: (-7/5843) = -1: nonsplit I2 -> split I2: c = 2
# 7: good reduction twisted by the ramified character -> I0*, c_7 = #E(F_7)[2]
def legendre(x, p):
    return pow(x % p, (p - 1) // 2, p)
for p in (3, 2243, 4547, 5843):
    print("  (-7/%d) = %s" % (p, {1: '+1', p - 1: '-1'}[legendre(-7, p)]))
# E mod 7: x (x^2 + a x + b) mod 7
a7, b7 = a % 7, b % 7
roots7 = [x for x in range(7) if (x * x + a7 * x + b7) % 7 == 0]
E_F7_2tors = 1 + 1 + len(roots7)  # O, (0,0), and roots of the quadratic
c7 = E_F7_2tors
print("E mod 7: x(x^2 + %d x + %d); quadratic roots in F_7: %s -> #E(F_7)[2] = %d -> c_7(E^{-7}) = %d" % (a7, b7, roots7, E_F7_2tors, c7))
tam = 2 * 2 * 1 * 2 * 2 * c7
print("Tamagawa product E^{-7} =", tam)

# Torsion of E^{-7}: (0,0) has order 2. Full 2-torsion iff disc(x^2 + ad x + bd) is a square; (0,0) in 2E iff bd square and ad +/- 2 sqrt(bd) squares.
disc = ad * ad - 4 * bd
r = math.isqrt(disc)
print("disc of quadratic =", disc, "square?", r * r == disc)
rb = math.isqrt(bd)
print("bd square?", rb * rb == bd)
tors = 2  # assumption: Z/2 (no full 2-torsion, (0,0) not divisible by 2; other torsion orders not excluded here)

L_lo, L_hi = 9.054319, 9.054421  # release K.2 interval for L(E^{-7},1)
for L in (L_lo, L_hi):
    q = L * tors * tors / (Om_T * tam)
    print("L = %.6f -> BSD-predicted #Sha(E^{-7}/Q) = L*tors^2/(Omega*Tam) = %.6f" % (L, q))
print("Sanity: with Omega_E/sqrt7 instead:", L_lo * 4 / (Om_E / math.sqrt(7) * tam))
