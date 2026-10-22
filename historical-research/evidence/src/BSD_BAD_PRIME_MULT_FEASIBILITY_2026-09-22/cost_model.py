# Cost projection for the recorded multiplicative-prime route, from MEASURED per-prime rates of the present
# implementation (producer apwit, verifier wverify; single-threaded, one 2^24 segment at the target height) and the
# measured msl rate of the p=3 run. Usage: python3 cost_model.py <prod_ms_at_Ta> <Ta> <prod_ms_at_Tb> <Tb>
import math, sys
def R(x):  # Riemann-type prime count approximation, relative error << 1e-4 here
    L = math.log(x); return x / L * (1 + 1/L + 2/L**2 + 6/L**3)
def fit(c1, x1, c2, x2):  # c(q) = a + b q^{1/4}, fitted through two measured points (ms)
    b = (c2 - c1) / (x2**0.25 - x1**0.25); a = c1 - b * x1**0.25; return a, b
def integral(fun, T, steps=4000):  # sum over primes q<=T of fun(q)  ~  int_2^T fun(x)/ln x dx
    s, x0 = 0.0, 2.0
    for i in range(steps):
        xa = x0 * (T / x0) ** (i / steps); xb = x0 * (T / x0) ** ((i + 1) / steps); xm = math.sqrt(xa * xb)
        s += fun(xm) / math.log(xm) * (xb - xa)
    return s
ver = lambda q: 1e-6 * (13.9 + 1.553 * (math.log2(q) - 26.2))   # recorded verifier model, re-confirmed at 3.9e13
MSL = 10782.0 / 14847836159                                        # measured msl CPU-s per n (p=3 run, m=81)
if __name__ == "__main__":
    ca, Ta, cb, Tb = map(float, sys.argv[1:5]); a, b = fit(ca, Ta, cb, Tb)
    prod = lambda q: 1e-3 * max(a + b * q**0.25, 0.0)
    print(f"producer fit: c(q) = {a:.4f} + {b:.3e} q^(1/4) ms")
    for p, T in [(2243, 39119884424954), (5843, 168703974800528), (2243, 69894025714890), (5843, 314608319666054)]:
        np_, P, V = R(T), integral(prod, T) / 3600, integral(ver, T) / 3600; M = MSL * T / 3600
        tot = P + V + M
        print(f"p={p} T={T:.4e} primes~{np_:.3e}  producer {P:.3e} CPU-h  verifier {V:.3e}  msl>= {M:.3e}  TOTAL {tot:.3e} CPU-h"
              f"  wall@16 workers x1.35 HT = {tot*1.35/16/24/365:.2f} years")
