#!/usr/bin/env python3
"""Additional checks: division-free polynomials; projective multiplication;
exact small-multiple global denominators; quadratic-height identities.
This is a separate verifier, not an independent implementation of the analytic
height theorem. It uses no PARI or other elliptic-curve software.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
import json,time,resource
import certify_d5 as main

p=2243; a2=-1; a4=-66020924; a6=-65074271436
ROOT=Path(__file__).resolve().parent

def a_polys(R,M=None):
    # A_n=psi_n for n odd, psi_n/(2y) for n even: no inversions by 2y.
    if M:
        x,y=(main.rat_mod(z,M) for z in R)
        red=lambda z:z%M
    else:
        x,y=R
        red=lambda z:z
    b2=4*a2; b4=2*a4; b6=4*a6; b8=4*a2*a6-a4*a4
    B=red((2*y)**4)
    base={0:0,1:1,2:1,
          3:red(3*x**4+b2*x**3+3*b4*x*x+3*b6*x+b8),
          4:red(2*x**6+b2*x**5+5*b4*x**4+10*b6*x**3+10*b8*x*x+(b2*b8-b4*b6)*x+b4*b8-b6*b6)}
    @lru_cache(None)
    def A(n):
        if n in base: return base[n]
        k=n//2
        if n%2:
            L=A(k+2)*A(k)**3; Rr=A(k-1)*A(k+1)**3
            return red(B*L-Rr if k%2==0 else L-B*Rr)
        return red(A(k)*(A(k+2)*A(k-1)**2-A(k-2)*A(k+1)**2))
    def psi(n): return red(A(n) if n%2 else 2*y*A(n))
    return psi

def projective_t(R,n,M):
    # Independently multiply in short-Weierstrass Jacobian coordinates.
    shift=a2*pow(3,-1,M)%M
    AA=(a4-a2*a2*pow(3,-1,M))%M
    BB=(a6-a2*a4*pow(3,-1,M)+2*a2**3*pow(27,-1,M))%M
    xr=(main.rat_mod(R[0],M)+shift)%M; yr=main.rat_mod(R[1],M)
    base=(xr,yr,1); out=None; checks=0
    def check(T):
        nonlocal checks
        if T is None:return
        X,Y,Z=T
        assert (Y*Y-X**3-AA*X*Z**4-BB*Z**6)%M==0
        assert any(c%p for c in T), 'Nonprimitive projective step; cannot certify precision'
        checks+=1
    def double(T):
        if T is None:return None
        X,Y,Z=T
        S=4*X*Y*Y%M; L=(3*X*X+AA*Z**4)%M
        XX=(L*L-2*S)%M
        T2=(XX,(L*(S-XX)-8*Y**4)%M,2*Y*Z%M)
        check(T2);return T2
    def plus(T,S):
        if T is None:return S
        if S is None:return T
        X1,Y1,Z1=T; X2,Y2,Z2=S
        U1=X1*Z2**2%M; U2=X2*Z1**2%M
        S1=Y1*Z2**3%M; S2=Y2*Z1**3%M
        H=(U2-U1)%M; rr=(S2-S1)%M
        if H==0 and rr==0:return double(T)
        XX=(rr*rr-H**3-2*U1*H*H)%M
        TT=(XX,(rr*(U1*H*H-XX)-S1*H**3)%M,H*Z1*Z2%M)
        check(TT);return TT
    while n:
        if n&1:out=plus(out,base)
        n//=2
        if n:base=double(base)
    X,Y,Z=out
    assert Y%p
    # x_old = X/Z^2 - a2/3; t=-x_old/y.
    return (-(X-shift*Z*Z)*Z*pow(Y,-1,M))%M, checks

def main_checks():
    results={}; inv=main.curve_invariants()
    r4=main.run(4);r7=main.run(7)
    assert r4['height_matrix_divided_by_p_mod_p']==r7['height_matrix_divided_by_p_mod_p']
    assert r4['determinant_divided_by_p2_mod_p']==r7['determinant_divided_by_p2_mod_p']
    results['precision_4_vs_7']='PASS'
    denominator_checks=[]; jacobian_checks=[]; bad_no_cancel=[]; division_free=[]
    points={'P1':main.P1,'P2':main.P2,'P1_plus_P2':main.add(main.P1,main.P2)}
    for key,Q in points.items():
        R=main.add(Q,Q); a,b,d=main.coords(R); n=p-1
        directpsi=a_polys(R,p**7)
        fastpsi=main.divpolys(R,p**7)
        indices=[n-1,n,n+1,2*n]
        for j in indices:assert directpsi(j)==fastpsi(j)
        division_free.append({'point':key,'indices':indices,'match':True})
        tt,jsteps=projective_t(R,n,p**4)
        # Recompute t from independent division-free polynomials at 7 digits.
        pn=directpsi(n); p2n=directpsi(2*n)
        s=main.vp(pn);assert s==main.vp(p2n)
        phi=(main.rat_mod(R[0],p**7)*pn*pn-directpsi(n-1)*directpsi(n+1))%(p**7)
        M=p**(7-s)
        td=(-2*phi*p**s*(pn//p**s)**2*pow(p2n//p**s,-1,M))%M
        assert tt==td%(p**4)
        assert tt%(p*p)==r7['point_calculations'][key]['t_mod_p2']
        jacobian_checks.append({'point':key,'t_mod_p4':tt,'checked_projective_steps':jsteps,'match':True})
        ep=a_polys(R)
        for k in [1,2,3,5,7,19]:
            S=main.mul(k,R); assert main.on_curve(S)
            en=isqrt(S[0].denominator)
            assert en*en==S[0].denominator
            proposed=d**(k*k)*ep(k)
            assert proposed.denominator==1 and abs(proposed)==en
            denominator_checks.append({'point':key,'multiple':k,'exact_match':True,'denominator_bits':en.bit_length()})
        # This finite check rules out bad-prime cancellation for the actual n.
        for ell in main.BAD:
            if d%ell==0:
                bad_no_cancel.append({'point':key,'ell':ell,'reason':'formal: monic homogenized phi_n is a unit'})
            else:
                fn=a_polys(R,ell)
                ps=fn(n)
                ph=(main.rat_mod(R[0],ell)*ps*ps-fn(n-1)*fn(n+1))%ell
                assert ps or ph
                bad_no_cancel.append({'point':key,'ell':ell,'psi_n_mod_ell':ps,'phi_n_mod_ell':ph,'no_common_zero':True})
    results['division_free_checks']=division_free
    results['Jacobian_checks']=jacobian_checks
    results['small_exact_global_denominator_checks']=denominator_checks
    results['actual_bad_prime_no_cancellation_checks']=bad_no_cancel
    # Parallelogram, scaling and a unimodular basis change; no target fitted.
    h1=r7['point_calculations']['P1']['height_P_over_p_mod_p']; h2=r7['point_calculations']['P2']['height_P_over_p_mod_p']
    Qsum=main.add(main.P1,main.P2)
    Qdiff=main.add(main.P1,(main.P2[0],-main.P2[1]))
    hsum=r7['point_calculations']['P1_plus_P2']['height_P_over_p_mod_p']
    hdiff=main.one_height(Qdiff,7,inv)['height_P_over_p_mod_p']
    hdouble1=main.one_height(main.add(main.P1,main.P1),7,inv)['height_P_over_p_mod_p']
    assert (hsum+hdiff-2*h1-2*h2)%p==0
    assert (hdouble1-4*h1)%p==0
    Q12=main.add(main.P1,main.add(main.P2,main.P2))
    h12=main.one_height(Q12,7,inv)['height_P_over_p_mod_p']
    offnew=(h12-hsum-h2)*pow(2,-1,p)%p
    detnew=(hsum*h2-offnew**2)%p
    assert detnew==r7['determinant_divided_by_p2_mod_p']
    results['quadratic_checks']={'parallelogram':'PASS','scaling_by_2':'PASS','unimodular_basis_change':'PASS',
                                 'h_P1_minus_P2_over_p':hdiff,'h_2P1_over_p':hdouble1,'new_basis_determinant':detnew}
    # The normalized first digits are checked directly with integer arithmetic.
    mat=r7['height_matrix_divided_by_p_mod_p']; z=mat[0][0]*mat[1][1]-mat[0][1]**2
    results['determinant_integer_arithmetic']={'integer':z,'residue':z%p,'nonzero':z%p!=0}
    results['verdict']='ALL_CHECKS_PASS'
    return results

if __name__=='__main__':
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))
    t=time.monotonic();result=main_checks()
    result['wall_seconds']=time.monotonic()-t
    result['peak_RSS_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert result['peak_RSS_bytes']<1024**3
    (ROOT/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['verdict','wall_seconds','peak_RSS_bytes']},indent=2))
