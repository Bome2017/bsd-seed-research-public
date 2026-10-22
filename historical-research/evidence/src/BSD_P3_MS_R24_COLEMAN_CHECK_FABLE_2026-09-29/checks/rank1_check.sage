# Fable check: rank-1 leading-term bookkeeping at nonsplit p=3.
# Test: v3(a_1(L_3)) == v3(2*sha_an*Tam/tors^2) + v3(h_PARI(P)) - 1   (Reg_gamma = h/log_3(kappa(gamma)), v3(log_3 4)=1)
import sys
p = 3
rows = [l.split() for l in open(sys.argv[1]).read().splitlines() if l.strip()]
ok = 0; tot = 0
for r in rows:
    label, N, rk, tors, tam, sha = r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5])
    ai = eval(r[7])
    E = EllipticCurve(QQ, ai)
    if E.conductor() != N or E.ap(3) != -1:
        print(f"{label:8} SKIP a3={E.ap(3)} N={E.conductor()}"); continue
    try:
        L = E.padic_lseries(p)
        ser = L.series(n=6, prec=4)   # coefficients mod 3^k with known precision
        a0 = ser[0]; a1 = ser[1]
        v_a1 = a1.valuation() if a1 != 0 else 'inf'
        prec_a1 = a1.precision_absolute()
        gens = E.gens(); assert len(gens) == 1
        P = gens[0]
        # saturation
        Pl, ind, reg = E.saturation([P]); P = Pl[0]
        h = pari(E).ellpadicheight(p, 10, pari(P))   # PARI cyclotomic height (vector [h_cyc-part?]) 
        hv = h
        # PARI returns [a,b] : height = a + b*log? take the cyclotomic one via ellpadicregulator
        R = pari(E).ellpadicregulator(p, 10, [pari(P)])
        v_h = int(R.valuation(p))
        v_alg = int(QQ(2*sha*tam/tors**2).valuation(p))
        pred = v_alg + v_h - 1
        res = (v_a1 == pred)
        tot += 1; ok += int(res)
        print(f"{label:8} tors={tors} tam={tam} sha={sha} v3(a0)={a0.valuation() if a0!=0 else 'inf'} v3(a1)={v_a1} (prec {prec_a1}) v3(h)={v_h} v_alg={v_alg} pred={pred} match={res}")
    except Exception as e:
        print(f"{label:8} ERROR {type(e).__name__}: {str(e)[:100]}")
print(f"matched {ok}/{tot}")
