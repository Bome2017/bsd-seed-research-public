# K-R25c: numerical bookkeeping for route K at nonsplit p = 3 (rank 0; rank 1 if cheap).
# Input: cands.txt lines "label N rank tors tam sha_an tag" (Cremona curvedata, fields 1,29,36,39,45).
# Route K prediction (O2 as derived in D5): v3(char(Sel^vee)(0)) <= v3(L_3(0)).
# Algebraic side (Euler characteristic, classical/primitive Selmer, nonsplit p: no p-local factor):
#   C = v3(sha) + sum_l v3(c_l) - 2 v3(#tors).
# Analytic side: A = v3 of the constant term of Sage's 3-adic L-series (modular symbols, MTT, alpha = a_3 = -1);
#   B = v3(2 * L(E,1)/Omega_E) (exact L_ratio) as an independent cross-check of A.
# Negative controls (must be CAUGHT on flagged curves):
#   NC1 imprimitive Selmer: C + sum_{l | N mult, l != 3} v3(1 - a_l/l)  (extra Euler factors on the Selmer side)
#   NC2 local-points bookkeeping: C + sum_{l nonsplit, l != 3} v3(#E(Q_l)[3^inf])  (wrong local term)
import sys, time
t0 = time.time()
p = 3
def v3(q):
    q = QQ(q)
    return Infinity if q == 0 else q.valuation(3)
rows = [l.split() for l in open(sys.argv[1]).read().splitlines()]
out = []
nA = nS = nR1 = 0
for r in rows:
    lab, N, rk, tors, tam, sha, tag = r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5]), r[6]; ai = sage_eval(r[7])
    E = EllipticCurve(QQ, ai); assert E.conductor() == N
    if E.ap(3) != -1: continue
    if tag == 'A' and rk == 0: nA += 1
    elif tag == 'S' and rk == 0:
        if nS >= 25: continue
        nS += 1
    elif tag == 'A' and rk == 1:
        if nR1 >= 12: continue
        nR1 += 1
    else: continue
    loc = []
    ns2 = sp1 = False; nc1 = nc2 = 0
    for ld in E.local_data():
        l = ZZ(ld.prime().gen()); c = ld.tamagawa_number()
        if l == 3: loc.append((3, str(ld.kodaira_symbol()), c, 'ns')); continue
        if ld.has_multiplicative_reduction():
            al = E.ap(l); typ = 'sp' if al == 1 else 'ns'
            nc1 += v3(1 - al/l)
            if typ == 'ns':
                # E(Q_l)[3^inf] for nonsplit mult. reduction: 3-part of gcd(l+1, ...) from the component group too
                n3 = v3(l + 1) if c % 3 != 0 else v3(l+1) + v3(c)
                nc2 += n3
                if l % 3 == 2: ns2 = True
            if typ == 'sp' and l % 3 == 1: sp1 = True
        else: typ = 'add'
        loc.append((int(l), str(ld.kodaira_symbol()), int(c), typ))
    C = v3(sha) + sum(v3(x[2]) for x in loc) - 2*v3(tors)
    Lp = E.padic_lseries(3)
    s = Lp.series(4)
    c0 = s[0]
    A = c0.valuation() if c0 != 0 else Infinity
    Aprec = c0.precision_absolute()
    if rk == 0:
        B = v3(2*E.lseries().L_ratio())
        ok = (C <= A) and (A == B or (A >= Aprec and B >= Aprec))
        line = "%s N=%d r=0 tors=%d sha=%d C=%s A=%s(prec %s) B=%s route_K[C<=A]=%s eq=%s NC1=%s NC2=%s flags=%s%s%s loc=%s" % (
            lab, N, tors, sha, C, A, Aprec, B, C <= A, C == A,
            'CAUGHT' if C + nc1 > A else 'pass', 'CAUGHT' if C + nc2 > A else 'pass',
            'ns2 ' if ns2 else '', 'sp1 ' if sp1 else '', '9|sha' if sha % 9 == 0 else '', loc)
    else:
        c1 = s[1]
        line = "%s N=%d r=1 tors=%d sha=%d C=%s L3(0)val=%s L3'(0)val=%s(prec %s) flags=%s%s loc=%s" % (
            lab, N, tors, sha, C, A, c1.valuation() if c1 != 0 else 'oo', c1.precision_absolute(),
            'ns2 ' if ns2 else '', 'sp1 ' if sp1 else '', loc)
        try:
            R = E.padic_regulator(3); line += " Reg3=%s" % R
        except Exception as e:
            line += " Reg3=UNSUPPORTED(%s)" % str(e)[:60]
    print(line); sys.stdout.flush()
print("counts: rank0 A-set %d, rank0 sha-9 set %d, rank1 %d; wall %.1fs" % (nA, nS, nR1, time.time()-t0))
