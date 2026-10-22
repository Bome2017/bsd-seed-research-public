#!/usr/bin/env python3
"""Independent finite modular arithmetic for the SW corrected split height.
No PARI, Sage, numerical height oracle, or curve database is used.
See DERIVATION.md and PROOF.md for the analytic and denominator inputs.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt, gcd
from pathlib import Path
import json, time, resource, argparse

A2,A4,A6=-1,-66020924,-65074271436
P=2243
BAD=(2,3,2243,4547,5843)
P1=(F(-3031),F(327384))
P2=(F(-2394),F(281520))

def on_curve(R):
    if R is None: return True
    x,y=R
    return y*y == x*x*x + A2*x*x + A4*x + A6

def add(R,S):
    if R is None: return S
    if S is None: return R
    x,y=R; u,v=S
    if x==u:
        if y+v==0: return None
        lam=(3*x*x+2*A2*x+A4)/(2*y)
    else: lam=(v-y)/(u-x)
    xx=lam*lam-A2-x-u
    return (xx,-y+lam*(x-xx))

def mul(n,R):
    out=None
    while n:
        if n&1: out=add(out,R)
        n//=2
        if n: R=add(R,R)
    return out

def coords(R):
    x,y=R; d=isqrt(x.denominator)
    assert d*d == x.denominator
    a=x*d*d; b=y*d**3
    assert a.denominator==b.denominator==1
    a,b=int(a),int(b)
    assert gcd(a,d)==gcd(b,d)==1
    return a,b,d

def smooth_checks(R):
    a,b,d=coords(R); out={}
    for ell in BAD:
        if d%ell==0: out[str(ell)]='infinity (smooth)'; continue
        x=a*pow(d*d,-1,ell)%ell; y=b*pow(d**3,-1,ell)%ell
        fx=(3*x*x+2*A2*x+A4)%ell; fy=2*y%ell
        assert (fx,fy)!=(0,0), (ell, R)
        out[str(ell)]={'x':x,'y':y,'Fx':fx,'Fy':fy}
    return out

def vp(n,p=P):
    assert n!=0
    v=0
    while n%p==0: n//=p; v+=1
    return v

def rat_mod(x,M):
    return x.numerator*pow(x.denominator,-1,M)%M

def divpolys(R,M):
    x,y=(rat_mod(t,M) for t in R)
    b2=4*A2; b4=2*A4; b6=4*A6; b8=4*A2*A6-A4*A4
    inv2y=pow(2*y,-1,M)
    base={0:0,1:1,2:2*y%M,
          3:(3*x**4+b2*x**3+3*b4*x*x+3*b6*x+b8)%M,
          4:(2*y*(2*x**6+b2*x**5+5*b4*x**4+10*b6*x**3+10*b8*x*x+(b2*b8-b4*b6)*x+b4*b8-b6*b6))%M}
    @lru_cache(None)
    def psi(n):
        if n<0: return (-psi(-n))%M
        if n in base: return base[n]
        k=n//2
        if n%2:
            z=psi(k+2)*pow(psi(k),3,M)-psi(k-1)*pow(psi(k+1),3,M)
        else:
            z=psi(k)*inv2y*(psi(k+2)*psi(k-1)**2-psi(k-2)*psi(k+1)**2)
        return z%M
    return psi

def log_unit_over_p(u):
    M=P*P; assert u%P
    w=pow(u%(M),P-1,M)
    assert (w-1)%P==0
    return ((w-1)//P)*pow(P-1,-1,P)%P

def curve_invariants():
    b2=4*A2; b4=2*A4; b6=4*A6; b8=4*A2*A6-A4*A4
    c4=b2*b2-24*b4
    c6=-b2**3+36*b2*b4-216*b6
    disc=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    assert c4**3-c6*c6==1728*disc
    assert vp(disc)==1 and c4%P and c6%P
    M=P**3
    z=disc*pow(c4**3,-1,M)%M
    q=(z+744*z*z)%M
    assert vp(q)==1
    ell=log_unit_over_p(q//P)
    assert ell!=0
    k=(-c6*pow(c4,-1,P))%P
    return {'c4':c4,'c6':c6,'discriminant':disc,'q_mod_p3':q,'q_over_p_mod_p2':q//P,
            'log_q_over_p_mod_p':ell,'C_inverse_squared_mod_p':k}

def one_height(Q,digits,inv):
    assert on_curve(Q)
    R=add(Q,Q); assert on_curve(R)
    a,b,d=coords(R)
    smooth=smooth_checks(R)
    assert d%P
    n=P-1; m=2*n; M=P**digits
    psi=divpolys(R,M)
    pn=psi(n); p2n=psi(2*n)
    s=vp(pn); s2=vp(p2n)
    assert s==s2 and s>=1 and digits-s>=2
    phi=(rat_mod(R[0],M)*pn*pn-psi(n-1)*psi(n+1))%M
    assert phi%P
    reduced_M=P**(digits-s)
    # Certified divisions remove exactly s digits, leaving digits-s.
    pn_unit=(pn//P**s)%reduced_M
    p2n_unit=(p2n//P**s)%reduced_M
    U=(-pow(d,n*n,reduced_M)*p2n_unit*pow(2*pn_unit*phi,-1,reduced_M))%reduced_M
    t=(-2*phi*(P**s)*pn_unit*pn_unit*pow(p2n_unit,-1,reduced_M))%reduced_M
    assert U%P and t%P==0
    logU=log_unit_over_p(U)
    tf=t//P%P
    sigma_height=2*logU%P
    correction=inv['C_inverse_squared_mod_p']*tf*tf*pow(inv['log_q_over_p_mod_p'],-1,P)%P
    h=(sigma_height-correction)*pow(m*m,-1,P)%P
    return {'R_x':str(R[0]),'R_y':str(R[1]),'R_a':a,'R_b':b,'R_d':d,
            'smooth_reductions':smooth,'n':n,'m':m,'precision_digits':digits,
            'psi_n':pn,'psi_2n':p2n,'v_psi_n':s,'v_psi_2n':s2,'phi_n':phi,
            'quotient_precision_digits':digits-s,'U_mod_p2':U%(P*P),'t_mod_p2':t%(P*P),
            'log_U_over_p_mod_p':logU,'uncorrected_mP_height_over_p':sigma_height,
            'Tate_correction_mP_over_p':correction,'height_P_over_p_mod_p':h,
            'division_polynomial_cache':psi.cache_info()._asdict()}

def run(digits):
    inv=curve_invariants()
    points={'P1':P1,'P2':P2,'P1_plus_P2':add(P1,P2)}
    rows={key:one_height(Q,digits,inv) for key,Q in points.items()}
    h1,h2,h12sum=(rows[t]['height_P_over_p_mod_p'] for t in points)
    off=(h12sum-h1-h2)*pow(2,-1,P)%P
    matrix=[[h1,off],[off,h2]]
    det=(h1*h2-off*off)%P
    assert det!=0, 'Computation inconclusive: determinant is zero at this precision'
    return {'prime':P,'model':[0,A2,0,A4,A6],'invariants':inv,'point_calculations':rows,
            'height_matrix_divided_by_p_mod_p':matrix,'determinant_divided_by_p2_mod_p':det,
            'regulator_valuation':2,'normalized_Reg_gamma_mod_p':det,
            'method':'Independent division-polynomial global denominator plus low-precision Bernardi/Tate correction; standard-library exact integers only'}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--digits',type=int,default=5); ap.add_argument('--output',required=True); args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))
    # The host rejects RLIMIT_AS and RLIMIT_DATA changes. Precision and
    # recurrence inputs are bounded below, and peak RSS is checked after run.
    assert 4 <= args.digits <= 8
    started=time.monotonic(); result=run(args.digits)
    result['wall_seconds']=time.monotonic()-started
    result['peak_RSS_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert result['peak_RSS_bytes'] < 1024**3
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['height_matrix_divided_by_p_mod_p','determinant_divided_by_p2_mod_p','regulator_valuation','wall_seconds','peak_RSS_bytes']},indent=2))
