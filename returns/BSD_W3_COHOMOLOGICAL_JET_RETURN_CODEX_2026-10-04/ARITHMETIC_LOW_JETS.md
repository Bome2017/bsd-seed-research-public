# Three coefficients vanish for arithmetic reasons

Grade: WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS_AND_THE_INTEGRAL_EULER_SYSTEM_BOUND. This is not an upper bound. It identifies three coefficients of the actual source, rather than discarding them because the curve has rank two.

For the genuine family coordinate F_p of this return,

    F_p in (T,S)^2 Z_p[[T,S]].                           (LJ1)

In particular f_00=f_10=f_01=0 exactly. This is stronger than their maximal-ideal divisibilities in TEN_POINT_CERTIFICATE.md. The following global argument, not local freeness alone, is needed.

## 1. The global complex and its singular localization

Let C=RΓ(G_(Q,Σ),U), using the retained unramified/extended-sheaf conventions. At the bad primes q≠p the retained residual local cohomology is zero on our domain; perfectness and derived base change therefore make the corresponding family local complex zero. Thus permitting those primes in Σ introduces none of the omitted local corrections. At p take the actual quotient M, with RΓ(Q_p,M)=R[-1].

Global perfectness, p-cohomological dimension two, and residual global H^0=0 represent C by a finite free complex

    C^1 -> C^2

in degrees one and two. The global Euler characteristic for this odd rank-two representation gives rank C^1=rank C^2+1. Let

    C_Sel=fib(C -> RΓ(Q_p,M)).

It is consequently a square two-term finite free complex, written

    R^d --A(T,S)--> R^d                                 (LJ2)

in degrees one and two. This is an integral Selmer complex for the specified ordinary condition; no arbitrary presentation of Sha is being posited.

## 2. Its determinant divides the actual Euler-system coordinate

The integral deformation Euler-system inequality applies to our genuine family system: use Ochiai 2006 Theorem 2 (equivalently the height-one global-cohomology version reviewed in Ochiai arXiv:1802.06427v3, Theorem 4.5). For its family-image hypotheses, use the full SL_2(I) image in retained COFINITE_HIDA_CONTROL.md §6. In SL_2(I), the commutator of diag(2,1/2) and [[1,1/3],[0,1]] is [[1,1],[0,1]]. Lift the two matrices to G_Q. Their commutator lies in the cyclotomic kernel, since the cyclotomic character is abelian. This supplies the required unit transvection; a lift of -I supplies the required scalar. The signs of complex conjugation have rank one each. All coefficient components are power-series rings. The optimized system is nonzero on the required components; alternatively the component-completion argument in retained VERIFIED_DERIVATION.md §3.3 leaves the tested component unchanged. Thus the source hypotheses, including its integral image condition, have been accounted for under the retained full-family-image result. The resulting one-sided inequality is

    char_R H^2(C) divides char_R(H^1(C)/R Z_p(1)).       (LJ3)

This is an imported Euler-system theorem, not a use of the full two-variable main-conjecture equality. The arithmetic source is nonzero: its reciprocity at a noncentral critical arithmetic point has a nonzero critical L-value and nonzero period/Euler factors. This is rational nonvanishing only; it gives no valuation bound.

The same theorem makes H^2(C) torsion; Euler characteristic gives rank H^1(C)=1. As the kernel of a map of finite free modules, H^1(C) is a second syzygy, hence reflexive over the regular local ring R. A rank-one reflexive module over this factorial ring is free. Choose H^1(C)=Re and write Z_p(1)=z e, loc^s(e)=ell in R. Then F_p=ell z in the chosen Coleman frame, and ell and z are nonzero.

It follows that H^1(C_Sel)=0. Put Delta=det A. The localization exact sequence gives, at each height-one prime,

    char_R H^2(C_Sel)=(ell) char_R H^2(C)=(Delta).

Equation (LJ3) therefore implies Delta divides F_p in R. Divisibility at every height-one prime gives integral divisibility because R is normal and factorial. No pseudo-null group is set equal to zero by this argument.

## 3. The two actual rational points force a double zero

Now base-change the complex to the point T=S=0 in characteristic zero. Its coefficient representation is V_p(E); the ordinary local condition is the Bloch–Kato/Kummer condition because the seed is good ordinary and non-anomalous. The global Kummer classes of the saturated points P_1,P_2 give two independent elements of H^1 of this specialized Selmer complex. This does not assume T_p Sha=0.

Consequently A(0,0) has kernel dimension at least two over Q_p. Work in the completed local ring at (T,S), namely Q_p[[T,S]]. Row and column operations split off a constant invertible block of A. Its remaining block has size at least two and every entry lies in (T,S). Therefore

    Delta in (T,S)^2 Q_p[[T,S]].

Since Delta divides F_p integrally, F_p has the same double-zero property. A series in Z_p[[T,S]] lying in (T,S)^2 Q_p[[T,S]] has zero constant and linear coefficients in Z_p. This proves (LJ1).

This proof does not bound the quadratic or cubic coefficients. It does not identify the remaining determinant with a nonzero height regulator. If additional global directions exist, the determinant can vanish to still higher order.

## 4. The remaining finite arithmetic value

Writing only terms relevant modulo m^4, we have

    F_p = a T^2 + b TS + c S^2
        + d T^3 + e T^2 S + f T S^2 + g S^3  (mod m^4),

where a,b,c are required modulo p^2 and d,e,f,g modulo p. These are seven genuine arithmetic coefficients, carrying ten F_p-digits of precision. They have not been evaluated in this return.

For the ten-point test, at least one of a,b,c nonzero modulo p^2 or one of d,e,f,g nonzero modulo p is sufficient for seed primary vanishing. A quadratic coefficient divisible by p may still give index three; it must not be thrown away by checking only the first residual quadratic form.

The claim is still conditional on the retained cofinite Hida input. In particular, the existence of the square Selmer complex and the determinant divisibility are not a proof that its determinant has a nonzero quadratic or cubic term.
