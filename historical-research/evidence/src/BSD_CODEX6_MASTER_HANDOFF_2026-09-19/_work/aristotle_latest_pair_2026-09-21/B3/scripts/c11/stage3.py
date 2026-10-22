"""Stage 3: modular symbols [a/m]^+ of the seed curve from the stage-2 bucket sums,
and assembly of the depth-1 Mazur-Tate approximation mod p.

  Re lambda(a/m) = -c_a - w * c_B,   B = -(a N)^{-1} mod m,   w = +1,
  c_a = sum_j S_m[j] cos(2 pi j a/m),   S_m[j] = sum_{n = j (m)} (a_n/n) e^{-2 pi n/(m sqrt N)}
  [a/m]^+ = Re lambda(a/m) / omega_1        (omega_1-normalisation, as in the retained runs)
"""
import math, sys
from math import comb, gcd

N = 6503188012738584
OM1 = 0.028044901519436404448309401807930384171
W = 1  # root number

def read_buckets(fn):
    B = {}
    cur = None
    for line in open(fn):
        if line.startswith("#"): continue
        t = line.split()
        if t[0] == "m":
            cur = int(t[1]); B[cur] = {}
        else:
            B[cur][int(t[0])] = float(t[1])
    return B

def symbols(S, m):
    c = {}
    for a in range(m):
        c[a] = sum(S[j]*math.cos(2*math.pi*j*a/m) for j in range(m))
    out = {}
    for a in range(m):
        if gcd(a, m) != 1: continue
        B = (-pow(a*N % m, -1, m)) % m
        out[a] = (-c[a] - W*c[B]) / OM1
    return out

def identify(v, lat=1024):
    r = round(v*lat)
    return r/lat, abs(v - r/lat)

def teich(a, p, k):
    mod = p**k; x = a % mod
    for _ in range(k+3): x = pow(x, p, mod)
    return x

def jlog(u, p, n=1):
    mod = p**(n+1)
    v = (u*pow(teich(u, p, n+1), -1, mod)) % mod
    g, cur = 1+p, 1
    for j in range(p**n):
        if cur == v: return j
        cur = (cur*g) % mod
    raise RuntimeError

def alpha_inv_mod(ap, p, prec):
    mod = p**prec; x = ap % p
    for _ in range(prec+2):
        x = (x - (x*x - ap*x + p)*pow((2*x-ap) % mod, -1, mod)) % mod
    return pow(x, -1, mod)

def report(fn):
    B = read_buckets(fn)
    print("bucket file:", fn)
    for m in sorted(B):
        S = B[m]
        sym = symbols(S, m)
        print(f"\n=== m = {m} ===")
        mx = 0.0
        for a in sorted(sym):
            val, d = identify(sym[a])
            mx = max(mx, d)
            print(f"  [{a}/{m}]^+ = {sym[a]:.9f}   ->  {val}   (dist {d:.2e})")
        print(f"  max distance to (1/1024)Z: {mx:.3e}")
    return B

def assemble(B, p):
    """depth-1 Mazur-Tate: P(T) = sum_{u in (Z/p^2)^*} (al^-2 [u/p^2]^+ - al^-3 [u/p]^+)(1+T)^{j(u)}"""
    S2 = symbols(B[p*p], p*p)
    S1 = symbols(B[p], p)
    v2 = {a: identify(S2[a])[0] for a in S2}
    v1 = {a: identify(S1[a])[0] for a in S1}
    # values are in (1/1024)Z; multiply through by 1024 (a p-unit) at the end we divide back
    ap = {5: -2, 7: -2, 11: -2}[p]
    prec = 6; mod = p**prec
    ai = alpha_inv_mod(ap, p, prec)
    A2 = pow(ai, 2, mod); A3 = pow(ai, 3, mod)
    inv1024 = pow(1024, -1, mod)
    poly = [0]*4
    for u in range(1, p*p):
        if u % p == 0: continue
        j = jlog(u, p)
        n2 = int(round(v2[u]*1024)); n1 = int(round(v1[u % p]*1024))
        cc = (A2*n2 - A3*n1) * inv1024 % mod
        for k in range(4):
            poly[k] = (poly[k] + cc*comb(j, k)) % mod
    return [x % mod for x in poly], [x % p for x in poly]

if __name__ == "__main__":
    B = report(sys.argv[1])
    for p in (7, 11):
        if p*p in B and p in B:
            full, red = assemble(B, p)
            print(f"\np = {p}: P_1 coefficients mod {p}^6 = {full}")
            print(f"p = {p}: [T^0],[T^1],[T^2],[T^3] mod {p} = {red}")
            print(f"p = {p}: C_{p} = [T^2] L_{p} mod {p} = {red[2]}")
