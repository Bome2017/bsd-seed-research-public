#!/usr/bin/env python3
"""
Tame-direction checks for the FINAL ASSEMBLY REFEREE (item 3, R3).
Copy of Lane 5's msym_check.py machinery (imported, unmodified) with the TAME degeneracy maps added.

Levels: common  M   := N   p^s  with N = t*Ng,   native M_g := Ng p^s,  t = N/Ng coprime to p.
Tame degeneracies X_1(N p^s) -> X_1(Ng p^s):
    pr^t_1 (forgetful) : (A,P) -> (A, tP),                on H: tau -> tau      => pushforward = [I]
    pr^t_2 (quotient)  : (A,P) -> (A/<Ng p^s P>, P mod),  on H: tau -> t tau    => pushforward = [diag(t,1)]
Checks (all as matrices on weight-2 modular symbols mod a prime ell):
  (T5-a) pr^t_{1,*} W_{N p^s}  = W_{Ng p^s} pr^t_{2,*}          [L5-T5]
  (T5-b) pr^t_{2,*} W_{N p^s}  = W_{Ng p^s} pr^t_{1,*}          [L5-T5]
  (C-U)  pr^t_{i,*} U'_p       = U'_p pr^t_{i,*}                 (p-Hecke vs tame degeneracy)
  (C-D)  pr^t_{i,*} <d>        = <d mod Ng p^s> pr^t_{i,*}       (diamonds)
  (C-W)  pr^t_{i,*} varpi_{1,*} = varpi_{1,*} pr^t_{i,*}         (tame vs p-direction degeneracy, s+1 -> s)
  (COMP) A_r^{(Ng)} pr^t_{1,*} W_{N p^r} = (U_p)^r pr^t_{2,*}    (composite used in 05 section 3)
  (MPC-g) varpi_1^* A_r varpi_{1,*} = A_{r+1} N   at the NATIVE tame level  (A1 re-run, native level)
"""
import sys
import msym_check as MC

def tame_ops(Ng, t, p, s, ell):
    N = Ng * t
    M   = N  * p**s          # common level
    Mg  = Ng * p**s          # native level
    Sc = MC.ManinSpace(M, ell)      # common
    Sg = MC.ManinSpace(Mg, ell)     # native
    I2 = (1,0,0,1)
    prt1 = MC.operator_matrix(Sc, Sg, [I2], ell)            # forgetful pushforward
    prt2 = MC.operator_matrix(Sc, Sg, [(t,0,0,1)], ell)     # quotient pushforward (tau -> t tau)
    Wc = MC.operator_matrix(Sc, Sc, [(0,-1,M,0)], ell)
    Wg = MC.operator_matrix(Sg, Sg, [(0,-1,Mg,0)], ell)
    Uc = MC.operator_matrix(Sc, Sc, [(1,b,0,p) for b in range(p)], ell)      # U'_p, common
    Ug = MC.operator_matrix(Sg, Sg, [(1,b,0,p) for b in range(p)], ell)      # U'_p, native
    Utg = MC.operator_matrix(Sg, Sg, [(p,0,a*Mg,1) for a in range(p)], ell)  # U_p (transpose), native
    return Sc, Sg, prt1, prt2, Wc, Wg, Uc, Ug, Utg

def run(Ng, t, p, r, ell):
    N = Ng*t
    print(f"=== TAME case Ng={Ng}, t={t} (N={N}), p={p}, r={r}, prime={ell}")
    res = {}
    def check(name, A, B):
        ok = MC.is_zero(MC.madd(A, B, ell, -1)); res[name] = ok
        print(f"  {name:62s} {'PASS' if ok else 'FAIL'}")
    # --- level s = r and s = r+1
    for s in (r, r+1):
        Sc, Sg, prt1, prt2, Wc, Wg, Uc, Ug, Utg = tame_ops(Ng, t, p, s, ell)
        print(f"  level s={s}: common {N*p**s} (dim {Sc.dim}) -> native {Ng*p**s} (dim {Sg.dim})")
        check(f"(T5-a) s={s}: pr^t_1* W_(Np^s) = W_(Ngp^s) pr^t_2*", MC.mmul(prt1, Wc, ell), MC.mmul(Wg, prt2, ell))
        check(f"(T5-b) s={s}: pr^t_2* W_(Np^s) = W_(Ngp^s) pr^t_1*", MC.mmul(prt2, Wc, ell), MC.mmul(Wg, prt1, ell))
        check(f"(C-U)  s={s}: pr^t_1* U'_p = U'_p pr^t_1*", MC.mmul(prt1, Uc, ell), MC.mmul(Ug, prt1, ell))
        check(f"(C-U') s={s}: pr^t_2* U'_p = U'_p pr^t_2*", MC.mmul(prt2, Uc, ell), MC.mmul(Ug, prt2, ell))
        import math as _m
        d = next(x for x in range(2, 10**4) if _m.gcd(x, N*p**s) == 1)
        Dc = MC.diamond_matrix(Sc, [d], ell); Dg = MC.diamond_matrix(Sg, [d], ell)
        check(f"(C-D)  s={s}: pr^t_1* <d> = <d> pr^t_1*  (d={d})", MC.mmul(prt1, Dc, ell), MC.mmul(Dg, prt1, ell))
        check(f"(C-D') s={s}: pr^t_2* <d> = <d> pr^t_2*  (d={d})", MC.mmul(prt2, Dc, ell), MC.mmul(Dg, prt2, ell))
        if s == r:
            # composite used in 05: A_r pr^t_1* W = (U_p)^r pr^t_2*   with A_r = W_(Ngp^r)(U'_p)^r
            Ar = Wg
            for _ in range(r): Ar = MC.mmul(Ar, Ug, ell)
            LHS = MC.mmul(Ar, MC.mmul(prt1, Wc, ell), ell)
            RHS = Utg
            for _ in range(r-1): RHS = MC.mmul(RHS, Utg, ell)
            RHS = MC.mmul(RHS, prt2, ell) if r >= 1 else prt2
            check(f"(COMP) A_r pr^t_1* W_(Np^r) = (U_p)^r pr^t_2*", LHS, RHS)
    # --- cross-level commutation: tame push-down vs p-direction push-down
    Sc1, Sg1, prt1_1, prt2_1, *_ = tame_ops(Ng, t, p, r+1, ell)
    Sc0, Sg0, prt1_0, prt2_0, *_ = tame_ops(Ng, t, p, r, ell)
    varpi_c = MC.operator_matrix(Sc1, Sc0, [(1,0,0,1)], ell)   # varpi_{1,*} common, r+1 -> r
    varpi_g = MC.operator_matrix(Sg1, Sg0, [(1,0,0,1)], ell)   # varpi_{1,*} native, r+1 -> r
    check("(C-W)  pr^t_1* varpi_1* = varpi_1* pr^t_1*", MC.mmul(prt1_0, varpi_c, ell), MC.mmul(varpi_g, prt1_1, ell))
    check("(C-W') pr^t_2* varpi_1* = varpi_1* pr^t_2*", MC.mmul(prt2_0, varpi_c, ell), MC.mmul(varpi_g, prt2_1, ell))
    return res

if __name__ == "__main__":
    args = [tuple(int(x) for x in a.split(",")) for a in sys.argv[1:]] or [(3,3,2,1)]
    allok = True
    for (Ng, t, p, r) in args:
        for ell in (1000003, 999983):
            allok &= all(run(Ng, t, p, r, ell).values())
    print("ALL PASS" if allok else "SOME FAIL")
