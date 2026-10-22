# Independent brute-force check of the local Gauss sums used in Lemma N2 (own code, not the cloud script).
# Gs(a,l;p^e) = sum_{r in L_p/p^e L_p} e((a*Q(r) + B(r,l))/p^e), l in L_p^#.
# Claim (Eichler level p^n, e<=n): Gs in {0} U p^{3e}*mu_{p^e}.  Claim (division, maximal order, e=1): Gs in {0} U -p^3*mu_p.
import itertools, random, numpy as np
random.seed(20260924)
def check(label, p, e, Qfun, Bfun, lvecs, u_list=(1,)):
    c = p**e; R = np.array(list(itertools.product(range(c), repeat=4)), dtype=np.int64)
    worst = 0.0; nz = 0; tot = 0; ok = True
    for u in u_list:
        for a in [x for x in range(1, c) if x % p][:3]:
            qa = (a * Qfun(R, u)) % c
            for l in lvecs:
                ph = (qa + Bfun(R, l, u)) % c
                s = np.exp(2j*np.pi*ph/c).sum(); tot += 1
                if abs(s) < 1e-6: continue
                nz += 1
                target = p**(3*e)
                z = s / target
                dev = max(abs(abs(s) - target), abs(z**c - 1) * target)
                worst = max(worst, dev)
                if dev > 1e-6 * target: ok = False
    print(f"{label}: p={p} e={e} cases={tot} nonzero={nz} max_dev={worst:.2e} -> {'PASS' if ok else 'FAIL'}")
    return ok
res = []
# Eichler: Q = u(al*de - p^n be*ga); l = u^{-1}(A, Bb/p^n, C/p^n, D) => B(r,l) = al*D + A*de - be*C - Bb*ga (integer)
for (p, n, e, full) in [(5,2,1,True), (7,2,1,True), (2,3,1,True), (2,3,2,True), (2,3,3,False), (5,2,2,False), (3,2,1,True)]:
    Q = lambda R, u, p=p, n=n: u*(R[:,0]*R[:,3] - p**n*R[:,1]*R[:,2])
    Bf = lambda R, l, u: R[:,0]*l[3] + l[0]*R[:,3] - R[:,1]*l[2] - l[1]*R[:,2]
    c = p**e
    if full: L = list(itertools.product(range(c), repeat=4))
    else: L = [tuple(random.randrange(c) for _ in range(4)) for _ in range(60)]
    us = [x for x in range(1, min(c, 7)) if x % p][:2]
    res.append(check(f"Eichler n={n}", p, e, Q, Bf, L, us))
# Division at p=3: O_B x Z_3 = Z_3[i] + Z_3[i]pi, nrd = x1^2+x2^2 - 3(y1^2+y2^2); B = 2u*diag(1,1,-3,-3)
# dual: l = (A/2u, Bb/2u, C/(6u), D/(6u))  => B(r,l) = r0*A + r1*Bb - r2*C - r3*D   (2 is a 3-unit)
p = 3
Qd = lambda R, u: u*(R[:,0]**2 + R[:,1]**2 - 3*(R[:,2]**2 + R[:,3]**2))
Bd = lambda R, l, u: R[:,0]*l[0] + R[:,1]*l[1] - R[:,2]*l[2] - R[:,3]*l[3]
# B(r,l) above uses l already scaled; phases e(B/3) with l's y-part in (1/3)Z means the linear term is (r2*C + r3*D)/3 with C,D integers mod 3.
# For Gs the pairing needs B(r,l)/3; x-part of l integral gives integer*r/3 too. Enumerate all l mod 3 L^#:
Ld = list(itertools.product(range(3), repeat=4))
def check_div(p, u_list=(1,2)):
    c = p; R = np.array(list(itertools.product(range(c), repeat=4)), dtype=np.int64); ok = True; nz = 0; tot = 0; worst = 0
    for u in u_list:
        for a in (1, 2):
            for l in Ld:
                # x-part of l has B-pairing 2u*r0*A' with A' in Z_3 -> integer multiples; y-part has pairing (-6u)*r2*C' with C' in (1/9)Z? use B(r,l)=r0*A+r1*Bb+r2*C+r3*D mod 3 generic
                ph = (a*Qd(R,u) + R[:,0]*l[0] + R[:,1]*l[1] + R[:,2]*l[2] + R[:,3]*l[3]) % c
                s = np.exp(2j*np.pi*ph/c).sum(); tot += 1
                if abs(s) < 1e-6: continue
                nz += 1; z = -s/p**3; dev = max(abs(abs(s)-p**3), abs(z**p - 1)*p**3); worst = max(worst, dev)
                if dev > 1e-6*p**3: ok = False
    print(f"Division maximal order: p={p} e=1 cases={tot} nonzero={nz} max_dev={worst:.2e} -> {'PASS' if ok else 'FAIL'}")
    return ok
res.append(check_div(3))
print("ALL_PASS" if all(res) else "SOME_FAIL")
