#!/usr/bin/env python3
"""
SECOND assembly referee, independent numerical checks (2026-09-15).
Built on Lane 5's _verify/msym_check.py (imported, not modified).

What is checked here that msym_check.py does NOT check:

  (T1) the A_r-TRANSPORT itself, on every generator of the primed Hecke algebra:
           rho(u') A_r = A_r u'      i.e.   iota_r(u') := A_r^{-1} rho(u') A_r = u'
       for u' in { <d>, U'_p, T'_l },  A_r = W_{M} (U'_p)^r,  M = N_g p^r,
       with rho(<d>) = <d>^{-1}, rho(U'_p) = U_p, rho(T'_l) = T_l.
       This is the algebraic content of C1 (carrier collapse) and C2 (balance).

  (T2) the CARRIER COLLAPSE consequence:  rho(t_2) A_r t_3 = A_r t_2 t_3
       for random pairs t_2,t_3 in the primed algebra  ==>  the functional depends on
       t_2 (x) t_3 only through the product t_2 t_3.

  (T3) the C4/C4b NORMALIZATION LEFTOVER:  U_p A_r = A_r U'_p, equivalently
           <U'_p y, A_r U'_p z> = <y, A_r (U'_p)^2 z>,
       i.e. of the three U'_p produced by BCPV Cor 4.11 one lands on factor 1 and
       exactly two land on the carrier.

  (T4) the TAME transport L5-T5 = A5 (NOT exercised by msym_check.py):
           pr^t_{1,*} W_{N p^s} = W_{N_g p^s} pr^t_{2,*},
           pr^t_{2,*} W_{N p^s} = W_{N_g p^s} pr^t_{1,*},
       plus the commutations used in C4/C5/C7:
           pd_* varpi_{1,*} = varpi_{1,*} pd_*,   pd_* U'_p = U'_p pd_*,  pd_* <n> = <n> pd_*
       for pd = pr^t_1 (forgetful) AND pd = pr^t_2 (quotient).

Exact arithmetic mod two large primes.  Weight 2, Manin symbols for Gamma_1(L).
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from msym_check import (ManinSpace, operator_matrix, diamond_matrix, mmul, madd,
                        mscale, is_zero, identity, matmul, rank_mod)

I2 = (1, 0, 0, 1)

def Uprime(space, p, ell):
    """U'_p on MS(L) via the classical coset matrices [[1,b],[0,p]]."""
    return operator_matrix(space, space, [(1, b, 0, p) for b in range(p)], ell)

def Utrans(space, p, ell):
    """U_p = Poincare transpose of U'_p, cosets [[p,0],[a L,1]]."""
    L = space.L
    return operator_matrix(space, space, [(p, 0, a * L, 1) for a in range(p)], ell)

def T_l(space, l, ell):
    """T_l (UNPRIMED) for a prime l not dividing the level L, on Gamma_1(L) modular symbols.
       Right coset reps: [[1,b],[0,l]] (b mod l) together with eta_l . diag(l,1), where
       eta_l in SL_2(Z) has bottom row = (0,l) mod L  (i.e. eta_l = diag(l^{-1},l) mod L).
       Verified below by [T_l, U'_p] = 0 and W T_l W = <l>^{-1} T_l = T'_l."""
    L = space.L
    from msym_check import lift_to_sl2
    eta = lift_to_sl2(0, l % L, L)
    mats = [(1, b, 0, l) for b in range(l)] + [matmul(eta, (l, 0, 0, 1))]
    return operator_matrix(space, space, mats, ell)

def W(space, ell):
    L = space.L
    return operator_matrix(space, space, [(0, -1, L, 0)], ell)

def diam(space, d, ell):
    return diamond_matrix(space, [d], ell)

def mpow(A, k, ell):
    R = identity(len(A))
    for _ in range(k): R = mmul(R, A, ell)
    return R

RESULTS = []
def check(name, A, B, ell):
    ok = is_zero(madd(A, B, ell, -1))
    RESULTS.append((name, ok))
    print(f"  {name:66s} {'PASS' if ok else 'FAIL'}")
    return ok

# ------------------------------------------------------------------ transport
def transport_case(Ng, p, r, ell):
    M = Ng * p ** r
    print(f"=== TRANSPORT  N_g={Ng}, p={p}, r={r}: native level M={M}, prime={ell}")
    S = ManinSpace(M, ell)
    print(f"  dim MS({M}) = {S.dim}")
    Wm = W(S, ell); Up = Uprime(S, p, ell); Ut = Utrans(S, p, ell)
    check("(vi-a) W^2 = 1", mmul(Wm, Wm, ell), identity(S.dim), ell)
    # A_r = W (U'_p)^r
    Ar = mmul(Wm, mpow(Up, r, ell), ell)
    # (T1a) diamonds:  rho(<d>) A = A <d>   with rho(<d>) = <d>^{-1}
    for d in [x for x in range(2, M) if __import__("math").gcd(x, M) == 1][:4]:
        dd = diam(S, d, ell); dinv = diam(S, pow(d, -1, M), ell)
        check(f"(T1a) <{d}>^-1 A_r = A_r <{d}>   [rho(<d>)=<d>^-1]",
              mmul(dinv, Ar, ell), mmul(Ar, dd, ell), ell)
    # (T1b) U'_p :  rho(U'_p) A = A U'_p , rho(U'_p) = U_p     <-- also (T3)
    check("(T1b)=(T3) U_p A_r = A_r U'_p   [C4 leftover: 2 U'_p on carrier]",
          mmul(Ut, Ar, ell), mmul(Ar, Up, ell), ell)
    # (T1c) T'_l for a prime l not dividing M:  rho(T'_l) = T_l := W T'_l W  (defn via Rosati);
    #       transport says T_l A_r = A_r T'_l, which given A_r = W U'^r reduces to
    #       W T'_l W W U'^r = W U'^r T'_l  <=>  T'_l commutes with U'_p  (checked separately).
    l = 2
    while M % l == 0: l += 1
    Tl = T_l(S, l, ell)                              # unprimed T_l
    Tp = mmul(Wm, mmul(Tl, Wm, ell), ell)            # T'_l := W T_l W
    dl = diam(S, pow(l, -1, M), ell)
    check(f"(T0) W T_{l} W = <{l}>^-1 T_{l}  (so W T_l W = T'_l, i.e. rho(T'_l) = T_l)",
          Tp, mmul(dl, Tl, ell), ell)
    check(f"(T1c') T'_{l} U'_p = U'_p T'_{l}  (commutativity of the primed algebra)",
          mmul(Tp, Up, ell), mmul(Up, Tp, ell), ell)
    check(f"(T1c) T_{l} A_r = A_r T'_{l}   [rho(T'_l) = T_l]",
          mmul(Tl, Ar, ell), mmul(Ar, Tp, ell), ell)
    # (T2) carrier collapse: rho(t2) A_r t3 = A_r t2 t3 for random t2,t3 in <U'_p, T'_l, <d>>
    rng = random.Random(20260915)
    gens = [("U'", Up, Ut), (f"T'{l}", Tp, Tl)]
    for d in [x for x in range(2, M) if __import__("math").gcd(x, M) == 1][:2]:
        gens.append((f"<{d}>", diam(S, d, ell), diam(S, pow(d, -1, M), ell)))
    for trial in range(3):
        i, j = rng.randrange(len(gens)), rng.randrange(len(gens))
        k, m = rng.randrange(len(gens)), rng.randrange(len(gens))
        t2 = mmul(gens[i][1], gens[j][1], ell); rt2 = mmul(gens[i][2], gens[j][2], ell)
        t3 = mmul(gens[k][1], gens[m][1], ell)
        lhs = mmul(rt2, mmul(Ar, t3, ell), ell)
        rhs = mmul(Ar, mmul(t2, t3, ell), ell)
        check(f"(T2) rho(t2) A_r t3 = A_r t2 t3   [t2={gens[i][0]}{gens[j][0]}, t3={gens[k][0]}{gens[m][0]}]",
              lhs, rhs, ell)

# ------------------------------------------------------------------ tame transport
def tame_case(Ng, t, p, s, ell):
    N = Ng * t
    Lbig = N * p ** s; Lsm = Ng * p ** s
    print(f"=== TAME  N_g={Ng}, t={t}, N={N}, p={p}, s={s}: {Lbig} -> {Lsm}, prime={ell}")
    Sb = ManinSpace(Lbig, ell); Ss = ManinSpace(Lsm, ell)
    print(f"  dim MS({Lbig}) = {Sb.dim}, dim MS({Lsm}) = {Ss.dim}")
    pd1 = operator_matrix(Sb, Ss, [I2], ell)              # pr^t_{1,*} forgetful (tau -> tau)
    pd2 = operator_matrix(Sb, Ss, [(t, 0, 0, 1)], ell)    # pr^t_{2,*} quotient  (tau -> t tau)
    Wb = W(Sb, ell); Ws = W(Ss, ell)
    check("(T4a) pr^t_{1,*} W_big = W_small pr^t_{2,*}   [L5-T5 / A5]",
          mmul(pd1, Wb, ell), mmul(Ws, pd2, ell), ell)
    check("(T4b) pr^t_{2,*} W_big = W_small pr^t_{1,*}   [L5-T5 / A5]",
          mmul(pd2, Wb, ell), mmul(Ws, pd1, ell), ell)
    Upb = Uprime(Sb, p, ell); Ups = Uprime(Ss, p, ell)
    check("(T4c) pr^t_{1,*} U'_p = U'_p pr^t_{1,*}", mmul(pd1, Upb, ell), mmul(Ups, pd1, ell), ell)
    check("(T4d) pr^t_{2,*} U'_p = U'_p pr^t_{2,*}", mmul(pd2, Upb, ell), mmul(Ups, pd2, ell), ell)
    for n in [x for x in range(2, Ng * p ** s) if __import__("math").gcd(x, Lbig) == 1][:2]:
        db = diam(Sb, n, ell); ds = diam(Ss, n, ell)
        check(f"(T4e) pr^t_{{1,*}} <{n}> = <{n}> pr^t_{{1,*}}", mmul(pd1, db, ell), mmul(ds, pd1, ell), ell)
        check(f"(T4f) pr^t_{{2,*}} <{n}> = <{n}> pr^t_{{2,*}}", mmul(pd2, db, ell), mmul(ds, pd2, ell), ell)

def tame_p_commute(Ng, t, p, s, ell):
    """pd_* varpi_{1,*} = varpi_{1,*} pd_*  (tame and p directions commute), both pd choices."""
    N = Ng * t
    A = N * p ** (s + 1); B = N * p ** s; C = Ng * p ** (s + 1); D = Ng * p ** s
    print(f"=== TAME/p COMMUTATION  {A} -> {B} -> {D}  vs  {A} -> {C} -> {D}, prime={ell}")
    SA = ManinSpace(A, ell); SB = ManinSpace(B, ell); SC = ManinSpace(C, ell); SD = ManinSpace(D, ell)
    pi_AB = operator_matrix(SA, SB, [I2], ell)     # varpi_{1,*}: N p^{s+1} -> N p^s
    pi_CD = operator_matrix(SC, SD, [I2], ell)     # varpi_{1,*}: N_g p^{s+1} -> N_g p^s
    for nm, mat in (("pr^t_1", (1, 0, 0, 1)), ("pr^t_2", (t, 0, 0, 1))):
        pdA = operator_matrix(SA, SC, [mat], ell)
        pdB = operator_matrix(SB, SD, [mat], ell)
        check(f"(T4g) {nm}_* o varpi_(1,*) = varpi_(1,*) o {nm}_*",
              mmul(pdB, pi_AB, ell), mmul(pi_CD, pdA, ell), ell)

# ---------------------------------------------------------------- appended: orientation
def orientation_case(Ng, p, r, ell):
    """C2 orientation clause:  A_r^t = (U_p)^r W  versus  A_r = W (U'_p)^r.
       W^2 = 1 and W U'_p W = U_p force (U_p)^r W = W (U'_p)^r, i.e. A_r^t = A_r."""
    M = Ng * p ** r
    S = ManinSpace(M, ell)
    Wm = W(S, ell); Up = Uprime(S, p, ell); Ut = Utrans(S, p, ell)
    Ar  = mmul(Wm, mpow(Up, r, ell), ell)        # A_r   = W (U'_p)^r
    Art = mmul(mpow(Ut, r, ell), Wm, ell)        # A_r^t = (U_p)^r W
    print(f"=== ORIENTATION  N_g={Ng}, p={p}, r={r}, M={M}, prime={ell}")
    check("(T5) W U'_p = U_p W  (AL intertwining)", mmul(Wm, Up, ell), mmul(Ut, Wm, ell), ell)
    check(f"(T5') A_r^t = (U_p)^{r} W  equals  A_r = W (U'_p)^{r}   [A_r SELF-ADJOINT]",
          Art, Ar, ell)

if __name__ == "__main__":
    for ell in (1000003, 999983):
        transport_case(5, 3, 1, ell)
        transport_case(7, 2, 1, ell)
        transport_case(3, 5, 1, ell)
        tame_case(5, 2, 3, 1, ell)
        tame_case(3, 2, 5, 1, ell)
        tame_p_commute(5, 2, 3, 0, ell)
        for c in ((5,3,1),(5,3,2),(7,2,1),(3,5,1)): orientation_case(*c, ell)
    bad = [n for n, ok in RESULTS if not ok]
    print(f"\n{len(RESULTS)} checks, {len(bad)} failures")
    if bad:
        for n in bad: print("  FAIL:", n)
        print("SOME FAIL")
    else:
        print("ALL PASS")

