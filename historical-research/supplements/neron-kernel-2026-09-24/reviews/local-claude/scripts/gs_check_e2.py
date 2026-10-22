# Nonzero branch at e = n = 2 (p=5) and e = 2 < n = 3 (p=2): force Bb = C = 0 mod p^e so the (be,ga) sums survive.
import itertools, random, numpy as np
random.seed(7)
def run(p, n, e, k=40):
    c = p**e; R = np.array(list(itertools.product(range(c), repeat=4)), dtype=np.int64); ok = True; worst = 0; nz = 0
    for _ in range(k):
        u = random.choice([x for x in range(1, c) if x % p]); a = random.choice([x for x in range(1, c) if x % p])
        A, D = random.randrange(c), random.randrange(c)
        ph = (a*u*(R[:,0]*R[:,3] - p**n*R[:,1]*R[:,2]) + R[:,0]*D + A*R[:,3]) % c
        s = np.exp(2j*np.pi*ph/c).sum(); t = p**(3*e)
        dev = max(abs(abs(s)-t), abs((s/t)**c - 1)*t); worst = max(worst, dev); nz += abs(s) > 1e-6
        ok &= dev < 1e-6*t
    print(f"p={p} n={n} e={e} forced-support cases={k} nonzero={nz} max_dev={worst:.2e} -> {'PASS' if ok else 'FAIL'}")
run(5, 2, 2); run(2, 3, 2); run(7, 2, 1)
