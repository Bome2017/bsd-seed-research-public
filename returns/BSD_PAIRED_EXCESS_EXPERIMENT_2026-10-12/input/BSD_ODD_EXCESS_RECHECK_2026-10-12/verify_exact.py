#!/usr/bin/env python3
"""Independent exact checks of the f97843a1 odd-excess control.

This does not compute a Selmer group, rerun PARI's rank computation,
or regenerate the overconvergent modular symbol. It checks the particular
Tate-algorithm branches needed for the displayed local factors. Source constants are explicitly
transcribed from the pinned proof and outputs. Requires Python 3.10+ and SymPy.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import gcd, isqrt
import json
import sympy as s

BASELINE = 'f97843a1b4768606787a9760ea4bad727a3dc4a1'
x = s.symbols('x')
d = 43737
Aa, Ab = -19766893413, -1937478573143510
Fa, Fb = -14959712463303, -22270654620235278500
AP = [(Q(1778638,9), Q(1169009812,27)),
      (Q(6466626346478,36517849), Q(2366996613841078836,220677361507))]
FP = [(Q(6288329),Q(-11502941299)),(Q(8502485),Q(21568458354))]
h = x*x-889319*x+139856084578
f = (x**5-1778638*x**4+4058589566895*x**3-2382059022317513158*x*x
     +555932503837435168004716*x-43668321039996772149044128719)
g = s.expand(h*s.diff(f,x)-2*f*s.diff(h,x))
M = s.Matrix([[-1,3],[-1,-2]])

def check(b: bool, name: str) -> None:
    if not b:
        raise AssertionError(name)

def add(P, R, a, modulus=None):
    # Short Weierstrass coordinates Y=y+1/2; None is infinity.
    def norm(t): return t % modulus if modulus else t
    def div(t,u): return t*pow(int(u)%modulus,-1,modulus)%modulus if modulus else t/u
    if P is None: return R
    if R is None: return P
    u,v=P; z,w=R
    if u==z:
        if norm(v+w)==0: return None
        lam=div(norm(3*u*u+a),norm(2*v))
    else:
        lam=div(norm(w-v),norm(z-u))
    xx=norm(lam*lam-u-z)
    return xx,norm(lam*(u-xx)-v)

def mul(k,P,a,modulus=None):
    if k<0:
        P=None if P is None else (P[0],(-P[1])%modulus if modulus else -P[1])
        k=-k
    ans=None
    while k:
        if k&1: ans=add(ans,P,a,modulus)
        P=add(P,P,a,modulus); k//=2
    return ans

def fracmod(q,m):
    q=Q(q)
    return q.numerator*pow(q.denominator,-1,m)%m

def oncurve(P,a,b): return P[1]*P[1]+P[1] == P[0]**3+a*P[0]+b

def rational_phi(P):
    z,Y=P[0],P[1]+Q(1,2)
    ev=lambda pol: Q(pol.subs(x,s.Rational(z.numerator,z.denominator)))
    return ev(f)/ev(h)**2, Y*ev(g)/ev(h)**3

def reduction_row(a,b,points,q):
    bb=fracmod(Q(b)+Q(1,4),q)
    curve=[(u,v) for u in range(q) for v in range(q) if (v*v-u**3-a*u-bb)%q==0]
    order=1+len(curve)
    check(order%5==0 and order%25!=0,'reduction has exactly one factor 5')
    G=next(P for P in curve if mul(5,P,a,q) is None)
    lookup={mul(k,G,a,q):k for k in range(5)}
    row=[]
    for z,y in points:
        P=(fracmod(z,q),fracmod(y+Q(1,2),q))
        projected=mul(order//5,P,a,q)
        check(projected in lookup,'projection lies in chosen cyclic subgroup')
        row.append(lookup[projected])
    return {'q':q,'group_order':order,'generator_short':G,'row':row}

def vp(q,p):
    q=Q(q)
    if not q: raise ValueError('zero has no finite valuation')
    n,z=q.numerator,q.denominator; v=0
    while n%p==0: n//=p; v+=1
    while z%p==0: z//=p; v-=1
    return v

def main():
    check(d==3*61*239 and d%4==1,'fundamental discriminant input')
    # Complete the square, twist, then translate x by d/3.
    for aa0,bb0,aa,bb in [(-10,-20,Aa,Ab),(-7820,-263580,Fa,Fb)]:
        xx=x+s.Rational(d,3)
        rhs=s.expand(xx**3-d*xx**2+aa0*d*d*xx+(s.Rational(bb0)+s.Rational(1,4))*d**3)
        check(s.expand(rhs-(x**3+aa*x+s.Rational(bb)+s.Rational(1,4)))==0,
              'exact quadratic twist/minimal model relation')
    check(all(oncurve(P,Aa,Ab) for P in AP),'A points')
    check(all(oncurve(P,Fa,Fb) for P in FP),'F points')
    eq=s.expand((x**3+Aa*x+s.Rational(4*Ab+1,4))*g*g
        -f**3-Fa*f*h**4-s.Rational(4*Fb+1,4)*h**6)
    check(eq==0,'isogeny polynomial identity')
    check(s.gcd(f,h)==1,'rational x map reduced')
    check(s.degree(f)==5 and s.degree(h)==2,'degree five')
    check(s.expand(h-(x-204106)*(x-685213))==0,'kernel factorization')
    # The exact derivative of the x map is g/h^3. This gives pullback of
    # dX/(2Y) equal to dx/(2y), and the leading term at infinity is x.
    check(s.cancel(s.diff(f/h**2,x)-g/h**3)==0,'differential pullback')
    FS=[(z,y+Q(1,2)) for z,y in FP]
    expected=[add(mul(-1,FS[0],Fa),mul(-1,FS[1],Fa),Fa),
              add(mul(3,FS[0],Fa),mul(-2,FS[1],Fa),Fa)]
    check([rational_phi(P) for P in AP]==expected,'both exact point images')
    check(M.det()==5,'point matrix determinant')
    K=[]
    for z in [204106,685213]:
        yy=Q(z**3+Aa*z+Ab)+Q(1,4)
        ratio=yy/d
        rn,rd=isqrt(ratio.numerator),isqrt(ratio.denominator)
        check(ratio>0 and rn*rn==ratio.numerator and rd*rd==ratio.denominator,'real kernel')
        K.append({'x':z,'Y2_div_d_square_root':str(Q(rn,rd))})
    rows={}
    counts={}
    for label,a,b,ps in [('A',Aa,Ab,AP),('F',Fa,Fb,FP)]:
        rr=[reduction_row(a,b,ps,q) for q in [7,19]]
        det=(rr[0]['row'][0]*rr[1]['row'][1]-rr[0]['row'][1]*rr[1]['row'][0])%5
        check(det!=0,'independent point pair mod5 '+label)
        rows[label]={'rows':rr,'det_mod5':det}
        counts[label]={str(q):1+sum((y*y+y-u**3-a*u-b)%q==0 for u in range(q) for y in range(q))
                       for q in [5,7,13,19]}
        check(counts[label]['5']==7,'ordinary non-anomalous at5')
    # Check model discriminants and the particular Tate branches used here.
    discs={}
    local_data={}
    local_products={}
    for label,a,b in [('A',Aa,Ab),('F',Fa,Fb)]:
        delta=-64*a**3-27*(4*b+1)**2
        discs[label]={'sign':-1 if delta<0 else 1,
                      'factorization':{str(k):int(v) for k,v in s.factorint(abs(delta)).items()}}
        check(delta<0,'connected real curve')
        check(max(discs[label]['factorization'].values())<12,'global minimality from discriminant')
        c4=-48*a; c6=-216*(4*b+1)
        loc=[]
        for q in (3,11,61,239):
            vc4,vc6,vd=vp(c4,q),vp(c6,q),vp(delta,q)
            if q==11:
                check(vc4==0 and pow((-c6)%q,(q-1)//2,q)==1,'split multiplicative at11')
                cq=int(vd)
                cp5=vp(cq,5)
                typ='split multiplicative I_'+str(cq)
                conductor_exp=1
                detail={'split_test_minus_c6':int((-c6)%q)}
            else:
                # In q-local short coordinates Y=y+1/2, shift x=X+r.
                # r=1 is necessary at q=3; r=0 works at the other two primes.
                r=1 if q==3 else 0
                a2=3*r; a4=3*r*r+a; a6=Q(r**3+a*r+b)+Q(1,4)
                check(a2%q==0 and a4%(q*q)==0 and fracmod(a6,q**3)==0,
                      'Tate I0-star divisibility hypotheses')
                # Earlier II/III/IV exit tests fail: q^2|a6, q^3|b8,
                # q^3|b6. Here a1=a3=0 in the q-local coordinates.
                b8=4*a2*a6-a4*a4; b6=4*a6
                check(fracmod(a6,q*q)==0 and fracmod(b8,q**3)==0 and fracmod(b6,q**3)==0,
                      'earlier Tate additive exits excluded')
                cb=fracmod(Q(a2,q),q); cc=fracmod(Q(a4,q*q),q); cd=fracmod(a6/q**3,q)
                disc_cubic=(cb*cb*cc*cc-4*cc**3-4*cb**3*cd-27*cd*cd+18*cb*cc*cd)%q
                check(disc_cubic!=0,'separable Tate cubic')
                roots=[z for z in range(q) if (z**3+cb*z*z+cc*z+cd)%q==0]
                cq=1+len(roots); cp5=vp(cq,5); conductor_exp=vd-4
                check(vd==6 and cq in (1,2,4),'I0-star local output')
                typ='I0*'
                detail={'x_shift':r,'Tate_cubic_coeffs':[1,cb,cc,cd],
                        'Tate_cubic_roots':roots,'Tate_cubic_discriminant':int(disc_cubic)}
            loc.append({'q':q,'v_c4':vc4,'v_c6':vc6,'v_Delta':vd,
                        'reduction':typ,'c_q':cq,'v5_cq':cp5,
                        'conductor_exponent':int(conductor_exp),**detail})
        local_data[label]=loc
        product=1; conductor=1
        for row in loc:
            product*=row['c_q']; conductor*=row['q']**row['conductor_exponent']
        check(product==(20 if label=='A' else 4),'full Tamagawa product')
        check(conductor==21042176859,'conductor from local data')
        local_products[label]={'Tamagawa_product':product,'conductor':conductor}
    # At q=7 and13, a rational torsion prime other than7,13 must divide gcd(10,18)=2.
    # Reduction at13 excludes7, at7 excludes13, and at5 excludes2.
    check(gcd(counts['A']['7'],counts['A']['13'])==2 and counts['A']['5']%2==1,
          'torsion exclusion using good reductions')
    # The rank upper bound remains retained. Local factors were checked above.
    selmer_ratio=Q(1,5)*Q(local_products['F']['Tamagawa_product'],local_products['A']['Tamagawa_product'])
    check(selmer_ratio==Q(1,25),'Cassels numerical ratio')
    log6=sum((Q(5**k,k) if k%2 else -Q(5**k,k)) for k in range(1,61))
    check(vp(log6,5)==1,'log6 valuation')
    logunit=log6/5
    # Lift alpha^2+alpha+5=0, alpha=4 mod5.
    alpha=4; mod=5
    for _ in range(1,10):
        alpha=next(alpha+k*mod for k in range(5) if ((alpha+k*mod)**2+(alpha+k*mod)+5)%(mod*5)==0)
        mod*=5
    ef=(1-pow(alpha,-1,mod))**2%mod
    R=4*5**2+4*5**3+4*5**4+3*5**5+4*5**7+3*5**9
    Runit=R//25
    HU=Runit*pow(fracmod(logunit,5**8),-2,5**8)%5**8
    J=4*5**4  # only known modulo 5^5
    L2_J=(J//25)*pow(fracmod(logunit,125),-2,125)%125
    L2_direct=4*25
    check(L2_J==L2_direct,'series/derivative leading coefficient')
    check(HU%5==4,'U-regulator is a unit')
    quotient_unit=(4*pow((Runit%5)*(ef%5)*4,-1,5))%5
    check(quotient_unit==1,'Q/25 mod5')
    # Independent paired-isogeny regulator identities as rational matrix algebra.
    Ha_s=s.Matrix([[s.Rational(3),s.Rational(3)],[s.Rational(3),s.Rational(1)]])
    # This is the displayed reduced F matrix, not an actual full F height.
    check((M.T*Ha_s*M)%5==s.zeros(2),'isogeny image isotropic mod5')
    v_raw_F=2; v_height_F=0; v_tam_F=0
    # From source-authenticated isogeny functoriality (not freshly evaluated A data):
    paired={'L2_A_mod25_derived':(L2_direct//5)%25,'v_L2_A_derived':1,
            'v_height_A_derived':0,'v_tam_A':1,'normalized_excess_A_derived':0,
            'normalized_excess_F_observed':2,'quotient_F_over_A_derived':25,
            'warning':'A numerator/height values are derived by isogeny, not a new independent run'}
    return {'status':'PASS_EXACT_RECHECK_UNDER_STATED_RETAINED_INPUTS',
            'baseline_commit':BASELINE,'polynomial_identity':True,'differential_pullback':1,
            'point_images_exact':True,'point_matrix':[list(map(int,M.row(i))) for i in range(2)],
            'kernel_real_checks':K,'reduction_certificates':rows,'small_counts':counts,
            'discriminants':discs,'local_Tamagawa_data':local_data,'local_products':local_products,
            'rational_torsion_order_both':1,'quadratic_twist_model_identity':True,
            'Cassels_selmer_ratio':str(selmer_ratio),
            'isogeny_Sha_dimension_difference':2,'F_Sha5_dimension_lower_bound':2,
            'p_adic_recheck':{'L2_mod125':L2_direct,'v_L2':2,'H_U_mod5pow8':int(HU),
                            'v_det_H_U':0,'Euler_mod5':int(ef%5),'Tamagawa_product_F':4,
                            'Q_mod125':25,'Q_over25_mod5':quotient_unit},
            'paired_isogeny_deduction':paired,
            'retained_not_recomputed':['rank upper bound from PARI',
                                      'overconvergent modular symbol and its error bounds'],
            'theorem_inputs_not_formalized':['Cassels isogeny-Selmer ratio',
                'specified branches of the Tate algorithm',
                'isogeny functoriality of canonical ordinary p-adic heights'],
            'formal_proof_assistant_verification':False,'new_seed_value':False}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
