#!/usr/bin/env python3
"""
H_pi generator-level checks on weight-2 Manin symbols (exact mod a large prime ell).

Builds on Lane 5's msym_check.py (imported verbatim, sha256 f99115c1...).

Checks, for X_1(M) <- X_1(pM), M = N_g p^r:
  (G1) varpi_{1,*} T'_l      = T'_l varpi_{1,*}          l | / N_g p
  (G2) varpi_{1,*} U'_p      = U'_p varpi_{1,*}
  (G3) varpi_{1,*} U'_l      = U'_l varpi_{1,*}          l | N_g
  (G4) varpi_{1,*} <dt>_{pM} = <dt mod M>_M varpi_{1,*}  all dt in (Z/pM)^*
and the SAME list for the two pullbacks varpi_1^*, varpi_2^* in the form
      X_{pM} o varpi^*  =  varpi^* o X_M     (equivariance of the INJECTION),
plus injectivity of varpi_1^*, varpi_2^* (rank = dim MS(M)).

Convention (inherited from Lane 5 01/msym_check.py): on modular symbols the operator
written as a sum over the standard coset representatives is the PRIMED (star) operator;
its transpose is the unprimed one.  Both are tested.
"""
import sys, math
from msym_check import (ManinSpace, operator_matrix, diamond_matrix, mmul, madd, mscale,
                        is_zero, identity, rank_mod, coset_reps_gamma1, H_coset_reps,
                        matmul, lift_to_sl2)

def sigma_l(L, l):
    """sigma in SL_2(Z) with sigma = diag(l^{-1}, l) mod L."""
    li = pow(l, -1, L)
    # bottom row (c,d) = (0, l) mod L  -> lift to SL2 then fix upper-left mod L
    for t in range(0, 200):
        c = t * L
        d = l + 0
        for s in range(0, 200):
            dd = l + s * L
            if math.gcd(c, dd) == 1 and (c or dd):
                a, b, cc, ddd = lift_to_sl2(c % L, dd % L, L)
                if cc % L == 0 and ddd % L == l % L and a % L == li % L:
                    return (a, b, cc, ddd)
        # widen
    # fallback: brute force search over small SL2 matrices
    for a in range(-3 * L, 3 * L):
        if a % L != li % L: continue
        for c in range(-3 * L, 3 * L, 1):
            if c % L != 0: continue
            for d in range(-3 * L, 3 * L):
                if d % L != l % L: continue
                # a*d - b*c = 1
                if c == 0:
                    if a * d == 1: return (a, 0, 0, d)
                    continue
                if (a * d - 1) % c == 0:
                    b = (a * d - 1) // c
                    return (a, b, c, d)
    raise ValueError("no sigma_l")

def Tprime_mats(L, l):
    """coset reps for T'_l at level L, l coprime to L."""
    assert math.gcd(l, L) == 1
    mats = [(1, b, 0, l) for b in range(l)]
    mats.append(matmul(sigma_l(L, l), (l, 0, 0, 1)))
    return mats

def Uprime_mats(L, l):
    assert L % l == 0
    return [(1, b, 0, l) for b in range(l)]

def Utranspose_mats(L, l):
    """transpose (unprimed) U_l at level L (l | L): sum over [[l,0],[a L,1]].  Lane 5 msym_check.py."""
    assert L % l == 0
    return [(l, 0, a * L, 1) for a in range(l)]

def run(Ng, p, r, ell, verbose=True):
    M = Ng * p ** r; pM = p * M
    print(f"=== N_g={Ng} p={p} r={r}:  M={M} -> pM={pM}   (mod {ell})")
    SM = ManinSpace(M, ell); SpM = ManinSpace(pM, ell)
    print(f"    dim MS(M)={SM.dim}  dim MS(pM)={SpM.dim}")
    I2 = (1, 0, 0, 1); alpha_inv = (1, 0, 0, p); alpha = (p, 0, 0, 1)
    push1 = operator_matrix(SpM, SM, [I2], ell)
    pull1 = operator_matrix(SM, SpM, coset_reps_gamma1(M, p), ell)
    pull2 = operator_matrix(SM, SpM, [matmul(alpha_inv, g) for g in H_coset_reps(M, p)], ell)
    push2 = operator_matrix(SpM, SM, [alpha], ell)
    res = {}
    def chk(name, A, B):
        ok = is_zero(madd(A, B, ell, -1)); res[name] = ok
        print(f"    {name:62s} {'PASS' if ok else 'FAIL'}")
    # --- injectivity of the two pullbacks
    r1 = rank_mod(pull1, ell); r2 = rank_mod(pull2, ell)
    res["rank pull1"] = (r1 == SM.dim); res["rank pull2"] = (r2 == SM.dim)
    print(f"    rank(varpi_1^*) = {r1} / {SM.dim}   {'INJ' if r1==SM.dim else 'NOT INJ'}")
    print(f"    rank(varpi_2^*) = {r2} / {SM.dim}   {'INJ' if r2==SM.dim else 'NOT INJ'}")
    rp = rank_mod(push1, ell)
    print(f"    rank(varpi_{{1,*}}) = {rp} / {SM.dim}  (mod ell; p-adic surjectivity is 04 S3)")
    # --- generators
    gens = []
    ells_tame = sorted({q for q in range(2, 40) if Ng % q == 0 and all(q % d for d in range(2, q))})
    for l in ells_tame:
        gens.append((f"U'_{l} (l|N_g)", Uprime_mats(M, l), Uprime_mats(pM, l)))
    gens.append((f"U'_{p} (p)", Uprime_mats(M, p), Uprime_mats(pM, p)))
    good = [l for l in (2,3,5,7,11,13) if math.gcd(l, pM) == 1][:3]
    for l in good:
        gens.append((f"T'_{l} (l coprime)", Tprime_mats(M, l), Tprime_mats(pM, l)))
    gens.append((f"U^t_{p} (UNPRIMED, control)", Utranspose_mats(M, p), Utranspose_mats(pM, p)))
    for (nm, mats_M, mats_pM) in gens:
        XM = operator_matrix(SM, SM, mats_M, ell)
        XpM = operator_matrix(SpM, SpM, mats_pM, ell)
        chk(f"(G) push1 o {nm}_pM = {nm}_M o push1", mmul(push1, XpM, ell), mmul(XM, push1, ell))
        chk(f"(E1) {nm}_pM o pull1 = pull1 o {nm}_M", mmul(XpM, pull1, ell), mmul(pull1, XM, ell))
        chk(f"(E2) {nm}_pM o pull2 = pull2 o {nm}_M", mmul(XpM, pull2, ell), mmul(pull2, XM, ell))
    # --- unprimed T_l = <l> T'_l control (Hida Control p.3 / Ohta (1.5.4)): expect (G) PASS, (E2) FAIL,
    #     (E1) PASS -- i.e. the UNPRIMED ring is the one carried by varpi_1^*.
    for l in good[:1]:
        TpM = operator_matrix(SpM, SpM, Tprime_mats(pM, l), ell)
        TM = operator_matrix(SM, SM, Tprime_mats(M, l), ell)
        DpM = diamond_matrix(SpM, [l], ell); DM = diamond_matrix(SM, [l], ell)
        XpM = mmul(DpM, TpM, ell); XM = mmul(DM, TM, ell)
        nm = f"T_{l} = <{l}>T'_{l} (UNPRIMED, control)"
        chk(f"(G) push1 o {nm}_pM = {nm}_M o push1", mmul(push1, XpM, ell), mmul(XM, push1, ell))
        chk(f"(E1) {nm}_pM o pull1 = pull1 o {nm}_M", mmul(XpM, pull1, ell), mmul(pull1, XM, ell))
        chk(f"(E2) {nm}_pM o pull2 = pull2 o {nm}_M", mmul(XpM, pull2, ell), mmul(pull2, XM, ell))
    # --- varpi_2^* = W_{pM} varpi_1^* W_M  (Lane 5 (iv'))
    wM = (0, -1, M, 0); wpM = (0, -1, pM, 0)
    W_M = operator_matrix(SM, SM, [wM], ell); W_pM = operator_matrix(SpM, SpM, [wpM], ell)
    chk("(W) varpi_2^* = W_pM o varpi_1^* o W_M", pull2, mmul(W_pM, mmul(pull1, W_M, ell), ell))
    chk("(deg) varpi_{1,*} varpi_1^* = p^2", mmul(push1, pull1, ell), mscale(identity(SM.dim), p*p, ell))
    # --- diamonds (G4): all d in (Z/pM)^*, compare with <d mod M> and with <d^{-1} mod M>
    bad_red = []; bad_e2 = []
    for dt in range(1, pM):
        if math.gcd(dt, pM) != 1: continue
        DpM = diamond_matrix(SpM, [dt], ell)
        DM = diamond_matrix(SM, [dt % M], ell)
        if not is_zero(madd(mmul(push1, DpM, ell), mmul(DM, push1, ell), ell, -1)):
            bad_red.append(dt)
        if not is_zero(madd(mmul(DpM, pull2, ell), mmul(pull2, DM, ell), ell, -1)):
            bad_e2.append(dt)
    res["(G4) push1 <dt>_pM = <dt mod M>_M push1 for ALL dt"] = (not bad_red)
    res["(E2-diamond) <dt>_pM pull2 = pull2 <dt mod M>_M for ALL dt"] = (not bad_e2)
    print(f"    (G4)  push1 o <dt>_pM = <dt mod M>_M o push1, all {sum(1 for d in range(1,pM) if math.gcd(d,pM)==1)} units: "
          f"{'PASS' if not bad_red else 'FAIL at ' + str(bad_red[:5])}")
    print(f"    (E2d) <dt>_pM o pull2 = pull2 o <dt mod M>_M, all units:                 "
          f"{'PASS' if not bad_e2 else 'FAIL at ' + str(bad_e2[:5])}")
    return res

if __name__ == "__main__":
    cases = [(5, 3, 1), (1, 5, 1), (2, 3, 2), (7, 3, 1)]
    if len(sys.argv) > 1:
        cases = [tuple(int(x) for x in a.split(",")) for a in sys.argv[1:]]
    allok = True
    for (Ng, p, r) in cases:
        for ell in (1000003, 999983):
            res = run(Ng, p, r, ell)
            for k, v in res.items():
                if not v: print("   !! FAILED:", k)
            allok &= all(res.values())
    print("ALL PASS" if allok else "SOME FAIL")
