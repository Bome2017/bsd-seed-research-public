PERIOD_FULL_REAL = RESOLVED
BSTW_PERIOD_CONVENTION = AMBIGUOUS
ZHAI_1_7 = APPLIES
DESCENT_MODEL = VERIFIED
PHI_SELMER_PREDICTION = PROVED
DUAL_SELMER_PREDICTION = PROVED
FINITE_FIELD_MECHANISM = PROVED
BSD2_EXPLICIT_FULL_REAL = PROVED
PRIOR_ART_BLOCKER = UNRESOLVED

# FROZEN_PRE_COMPARISON_RECONSTRUCTION

Stage I, version 1. Scope: original PK66B1 design packet and publicly located primary sources. No other model's reconstruction or prior conversations are inputs. This is a mathematical reconstruction, not a machine-checked proof. The accompanying symbolic/finite checks are corroboration only. Any subsequent change to this frozen record must be separately recorded.

## 1. Family, notation, and period

Throughout, q is prime, q = 5 (mod 8), (q/3) = -1, (q/11) = +1. In particular q is positive, q does not divide 66, and (33/q) = -1 by reciprocity.

E is Cremona 66b1:

    y^2 + xy + y = x^3 + x^2 - 2x - 1.

Its minimal invariants are (c4,c6,Delta)=(97,-17,528). Omega+ always denotes the least positive real period of the minimal Neron differential, as in Zhai, NOT a period of an arbitrary integral equation. Define Omega_R = integral over E(R) of |omega_min| and L_R^alg=L/Omega_R. Positive discriminant gives two real components. Translation identifies their measures, and each has measure Omega+. Therefore

    Omega_R = 2 Omega+,
    L_R^alg = L_Z^alg / 2,
    v2(L_R^alg) = v2(L_Z^alg) - 1.

These identities apply to the base and its positive twists. For the particular q-family here, the explicit minimal models below also give Omega+_q=Omega+_1/sqrt(q) and Omega_R,q=Omega_R,1/sqrt(q).

Primary base input: Cremona, Algorithms for Modular Elliptic Curves, Chapter 2 section 2.8 defines the table period as twice the least positive period for a rectangular lattice. Table 4, printed page 314, row 66B(E), gives the exact rank-zero modular-symbol ratio L/Omega_R=1/4. Hence L_Z^alg(E,1)=1/2, with valuations -2 and -1 respectively. This does not use the table's analytic Sha column or assume BSD. Cremona's database documentation establishes optimality of 66b1 and Manin constant 1.

Zhai Theorem 1.7 applies: optimality and odd Manin constant; positive discriminant; rational nonzero 2-torsion; nonzero base L-value; odd good prime q=1 (mod 4); and v2(N_q)=1-v2(L_Z^alg(E,1))=2, which is independently proved below. Its conclusion is L(E_q,1) nonzero and v2(L_Z^alg(E_q,1))=1. Consequently v2(L_R^alg(E_q,1))=0. It also gives finiteness of Mordell-Weil and Sha. The isogeny Selmer identities are not stated in that theorem.

BSTW's inspected Neron-period notation and its odd-p localized period bases do not fix the factor of 2 required here. No choice is inferred from making its BSD formula work. BSTW_PERIOD_CONVENTION remains AMBIGUOUS.

## 2. Models, isogenies, and differentials

Completing the square gives

    (2y+x+1)^2=(x-1)(4x^2+9x+3).

Set X=4(x-1), Y=8y+4x+4, with inverse x=X/4+1, y=(Y-X-8)/8. Then

    C: Y^2 = X(X^2+17X+64).

Thus A=17, B=64, A^2-4B=33 are derived, not assumed. The unique nonzero rational 2-torsion point is T=(0,0), corresponding to (1,-1) on the original equation. The other 2-torsion x-coordinates are (-17 +/- sqrt(33))/2. P=(-8,8), corresponding to (-1,1) on the original equation, has 2P=T and exact order 4.

For twists:

    C_q: Y^2=X(X^2+17qX+64q^2),
    C'_q: V^2=U(U-q)(U-33q).

Put a=17q, b=64q^2, D=a^2-4b=33q^2. Then

    phi(X,Y)=(X+a+b/X, Y(1-b/X^2)),
    hatphi(U,V)=((U-2a+D/U)/4, V(1-D/U^2)/8).

The maps extend to the omitted kernel points. Their composition is [2]. C_q has only T as nonzero rational 2-torsion; C'_q has T'_0=(0,0), T'_1=(q,0), T'_{33}=(33q,0). The dual sends T'_1 and T'_{33} to T; its kernel is {O,T'_0}.

Nonminimal discriminants:

    Delta(C_q)=2^16*3*11*q^6,
    Delta(C'_q)=2^14*3^2*11^2*q^6.

Global minimal models for this q-family are

    E_q: z^2+xz=x^3+((17q-1)/4)x^2+4q^2x,
    E'_q: v^2+uv=u^3-((31q+1)/4)u^2-2q^2u.

The maps to the nonminimal models are (X,Y)=(4x,8z+4x), (U,V)=(q+4u,8v+4u). Minimal invariants are

    E_q: (97q^2,-17q^3,528q^6),
    E'_q: (1057q^2,34255q^3,4356q^6).

Minimality holds at 2 because c4 is odd, and at odd bad primes because discriminant valuations are less than 12. Bad primes on both curves are exactly 2,3,11,q.

On C, dX/(2Y)=omega_min/2. The same factor 1/2 holds between each displayed nonminimal twist differential and its minimal differential. On minimal differentials phi pulls back omega'_min to omega_min, and hatphi pulls back omega_min to 2 omega'_min.

## 3. Kummer maps, support, and charts

All classes are modulo squares. The convention is Sel^phi(C_q) inside H^1(Q,C_q[phi]); its local images come from C'_q points:

    delta_phi(O)=1, delta_phi(T'_0)=33,
    delta_phi(U,V)=U for U nonzero.

Thus delta_phi(T'_1)=q and delta_phi(T'_{33})=33q. The dual Kummer map on C_q is

    delta_hatphi(O)=1, delta_hatphi(T)=64q^2=1,
    delta_hatphi(X,Y)=X for X nonzero.

For y^2=x(x^2+Ax+B), the homogeneous covering for class d is

    N^2=d Z^4+A Z^2 W^2+(B/d)W^4, (Z,W) nonzero,

with weights (Z,W,N)=(1,1,2). On W nonzero, x=d Z^2/W^2 and y=d Z N/W^3. The chart W=0 accounts for O and requires class d=1. The chart Z=0 accounts for (0,0) and requires class d=B. N=0 includes the remaining 2-torsion points. No denominator chart or zero-y case is discarded.

The common support is Q({2,3,11,q},2)=<-1,2,3,11,q>, with 32 classes. The sharper supports are

    G_phi=<-1,3,11,q> (16 classes),
    G_hatphi=<-1,2,q> (8 classes).

Proof: for integral A,B and a prime ell not dividing B, a nonzero x-coordinate with negative valuation n gives valuation 3n on the cubic, whereas positive n gives valuation n from Bx. Thus n is even. Exceptional Kummer values also have even valuations outside B. Apply with B=33q^2 and B=64q^2 respectively.

## 4. Exact local images and complete intersections

The exact local images are:

| Place | H_phi | H_hatphi |
|---|---|---|
| real | positive class only | both signs |
| 2 | {1,5}=<q> | {1,3,5,7}, all unit classes |
| 3 | Q_3^*/Q_3^{*2} | {1} |
| 11 | Q_11^*/Q_11^{*2} | {1} |
| q | Q_q^*/Q_q^{*2} | {1} |
| other finite primes ell | unramified unit subgroup | unramified unit subgroup |

### Real

For C'_q, U<0 makes U(U-q)(U-33q)<0; all nontrivial exceptional values are positive. Thus H_phi is trivial. On C_q, (-8q,8q sqrt(q)) is a real point with negative X, so the dual image has both signs.

### phi at 2

Write n=v2(U). Since B'=33q^2 is odd, n is even if nonzero. For n<0,

    (1-q/U)(1-33q/U)=1-34q/U+33q^2/U^2 = 1 (mod 8).

For n>0, n>=2 and (U-q)(U-33q)=1 (mod 8). In either case the equation forces U to be a square. If n=0 and U=3 (mod 4), both U-q and U-33q have valuation 1. Their halves are odd and differ by 16q, so their product is 1 (mod 8). Dividing the equation by 4 forces U=1 (mod 8), a contradiction. Thus the only possible unit classes are 1 and 5. They occur at O and T'_1. T'_0 has class 33=1 in Q_2 and T'_{33} has class 5. Therefore H_phi,2={1,5} exactly.

### dual at 2

For X nonzero,

    (Y/X)^2=X+17q+64q^2/X.

If n=v2(X)<0 or n>6, dominant terms force n even. For n=1,3,5 with X=2^n u and u odd, the right side is respectively 5+2u, 5, or 5+2u^{-1} modulo 8. These are never 1 modulo 8, excluding all odd n. Conversely, for each odd unit u set X=4u: the right side is 17q+4u+16q^2/u=1 (mod 8), hence a square in Q_2. This realizes every unit class. Exceptional points have trivial class.

### dual at 3 and 11

For ell=3,11, b=64q^2 is a square unit. If v_ell(X) is nonzero, the unit correction to the dominant square factor is 1 modulo ell, so the equation forces X to be a square. For X a unit, use

    X^2+17qX+64q^2=(X+17q/2)^2-33q^2/4.

The last term has valuation exactly 1. If X+17q/2 vanishes modulo ell, the quadratic factor has valuation 1, impossible in Y^2=X times that factor. Otherwise it is a square unit by Hensel, again forcing X square. Hence both dual images are trivial.

At 3, the phi classes q (a nonsquare unit) and 33 (odd valuation) already generate the full group. At 11 they do NOT: q is a square unit. The missing nonsquare unit is supplied by the local point U=2q. Its equation is V^2=-62q^3; modulo 11 the coefficient -62 is 4 and q is a square. Hensel gives V in Q_11. Its Kummer value 2q is a nonsquare unit because (2/11)=-1. Together with 33 this gives the full phi image at 11.

### At q

By reciprocity (33/q)=-1. Thus the phi images 33 and q give an unramified nonsquare and a uniformizer, so the phi image is full. For the dual, put n=v_q(X). If n<=0, the quadratic factor is X^2 times a unit equal to 1 modulo q. If n>=2, it is 64q^2 times such a unit. Both cases force X square. If n=1, write X=qu; then Y^2=q^3 u(u^2+17u+64). The quadratic in u has nonsquare discriminant 33 and no root modulo q, giving an impossible odd valuation 3. Hence the dual image is trivial.

### Other finite places

Both curves have good reduction, and the degree-2 isogeny is invertible on the formal group. The finite-field quotient has order 2, since the isogenous curves have equal point counts and the kernel has two rational points. Together with the valuation support argument, this identifies the local image with the two-element unramified unit subgroup for each isogeny.

### Global upper bounds

For phi, after support and the real place write d=3^a 11^b q^c, a,b,c in {0,1}. In Q_2, both 3 and 11 have class 3, and q has class 5. Membership in {1,5} forces a=b. Thus the upper bound is {1,33,q,33q}; all four occur globally from C'_q[2](Q). Therefore

    Sel^phi(C_q)={1,33,q,33q}.

For the dual, write d=(-1)^s 2^a q^c. The 2-adic unit condition forces a=0. The trivial q-adic image forces c=0. The trivial 3-adic image excludes -1, forcing s=0. Therefore

    Sel^hatphi(C'_q)={1}.

This eliminates every other global squareclass, rather than merely checking survival of the predicted ones.

## 5. Finite-field mechanism

For every odd good p, P=(-8,8) retains order 4. If (33/p)=+1, full rational 2-torsion together with P gives a subgroup of order 8. If (33/p)=-1, the 2-Sylow subgroup is cyclic, and its order exceeds 4 exactly when P is divisible by 2.

The duplication formula gives

    X(2R)=(X^2-64)^2/[4X(X^2+17X+64)].

The condition X(2R)=-8 becomes (X+8)^4+32X^2=0. Any half therefore produces a square root of -2. Conversely, if s^2=-2, factor that quartic as

    [X^2+(16-4s)X+64][X^2+(16+4s)X+64].

The two discriminants are 16(-2-8s) and 16(-2+8s); their product is 16^2*132, of squareclass 33. When (33/p)=-1, exactly one discriminant is a nonzero square. A resulting root X is not 0 or +/-8 for p not dividing 66. The quartic identity gives

    X(X^2+17X+64)=-(X^2-64)^2/32,

so Y=s(X^2-64)/8 produces a point, and its sign can be chosen to halve P. This supplies the y-coordinate, not just a root of the duplication equation.

The exact criterion is

    v2(#E(F_p))=2 iff (33/p)=-1 and (-2/p)=-1.

The second character is -2, not 2 for arbitrary good primes. For the proposed q-family, both are -1. Thus N_q=4 (mod 8), a_q=q+1-N_q=2 (mod 8), and a_q is nonzero. Hasse gives |a_q|<q, hence q is ordinary.

Independent finite corroboration: 1,226 good primes below 10,000; zero exceptions to the exact criterion; 82 family primes. Symbolic model/isogeny/discriminant/duplication checks also pass. Neither these counts nor packet counts substitute for the proof.

## 6. The kernel and the 2-Selmer group

The Galois-module sequence 0 -> E_q[phi] -> E_q[2] -> E'_q[hatphi] -> 0 induces the exact sequence

    0 -> E'_q(Q)[hatphi]/phi(E_q(Q)[2])
      -> Sel^phi(E_q) -> Sel_2(E_q) -> Sel^hatphi(E'_q).

No general surjectivity onto the last term is claimed. Here that term is trivial. The first term has order 2: E'_q(Q)[hatphi]={O,T'_0}, while phi(E_q(Q)[2])={O}. Its Kummer image is <33>, NOT the full four-element quotient 2-torsion image. Therefore

    Sel_2(E_q) = <33,q>/<33>, of order 2.

The Kummer exact sequence 0 -> E_q(Q)/2E_q(Q) -> Sel_2(E_q) -> Sha(E_q)[2] -> 0, together with |E_q(Q)[2]|=2, forces rank zero and Sha[2]=0. Every nonzero element of a 2-primary torsion group has a multiple of order 2, so Sha[2^infty]=0 without needing finiteness for this implication.

## 7. Torsion, Tamagawa factors, and BSD(2)

A rational half of T would have X=+/-8q. At -8q its Y-coordinate requires sqrt(q), and at +8q it requires sqrt(33q). Neither is rational. Thus the twist's rational 2-primary torsion is exactly Z/2Z.

The minimal discriminant valuations at 2,3,11,q are 4,1,1,6. At 2 the coefficient (17q-1)/4 is odd; the tangent cone at the singular point is z^2+xz+x^2, irreducible over F_2. Hence reduction is nonsplit I4 and c2=2. At 3 and 11, use the multiplicative split test (-c6/ell)=(17q/ell): split I1 at 3 and nonsplit I1 at 11, both with c=1. At q, Tate's auxiliary cubic is t(t^2+17t+64), with one simple rational root since (33/q)=-1. Reduction is I0*, with c_q=1+1=2. All other finite factors are 1.

    (c2,c3,c11,cq)=(2,1,1,2), product=4.

Zhai supplies finiteness of Sha, and the descent supplies its odd order. Hence

    v2(|Sha| product(c_ell) / |E_q(Q)_tors|^2)=0+2-2=0
      = v2(L(E_q,1)/Omega_R,q).

This proves BSD at 2 with the explicitly defined full real period. It does not claim Sha=1 or L_R^alg=1.

## 8. Prior-art disposition and separate full-BSD corollary

Banwait-Huang v3, Theorem 2.14 case (3), does not apply. Its branch E(Q)[2]=Z/2 is the right structural branch, but the family has v2(N_q)=2 rather than 1; the base full-real value has valuation -2 rather than -1; 2 is inert rather than split in Q(sqrt(q)); and the quotient has full rational 2-torsion. Its general splitting requirement also fails at 2 and 3.

BSTW Theorem 10.12 is not an independent source of BSD(2), because BSD(2) is already a hypothesis. As printed it additionally requires a3(E)=0, whereas a3(66b1)=-1. HOWEVER BSTW's introductory Theorem 1.7 explicitly lists 66b1 and states full BSD for squarefree twists with nonzero L-value and ordinary twisting primes; these latter conditions hold here. Example 1 also lists 66b1. This stronger existing claim must not be omitted. The inspected route does not resolve the literal hypothesis mismatch and period convention, so no verified normalized replacement for the explicit descent is extracted from it. This is why PRIOR_ART_BLOCKER is UNRESOLVED rather than NOT_FOUND. No novelty claim is made.

Zhai's prose after Theorem 1.7 says that classical descent and Tamagawa calculations can verify BSD(2) for the curves under discussion, but it does not supply the present explicit local images. This is additional attribution risk, not a substitute for the local proof.

Nam's thesis Theorem 4.9 fails its condition requiring splitting of 2 in the twisting field or good reduction at 2. Here 2 is inert and E has bad reduction at 2. Its stated conclusion is algebraic rank zero; analytic nonvanishing there is obtained under BSD, not an unconditional normalized BSD(2) formula.

Cai-Li-Zhai's v2(N)=1/full-real base valuation -1 framework fails here. Shu-Zhai's condition (Tor) fails because the quotient has full rational 2-torsion. Kriz-Li's no-rational-cyclic-4-isogeny hypothesis also fails because P generates such a rational subgroup. Bounded exclusion of these routes is not a novelty proof.

Separate corollary, invoking Banwait-Huang v3 Theorem 2.13 and its odd-prime inputs: the full strong BSD formula follows AFTER the independently proved BSD(2). Its hypotheses are verified as follows. E is semistable of conductor 66; D=q and (D,198)=1; Zhai gives analytic nonvanishing; BSD(2) is proved above; a3=-1 is allowed; q is ordinary. Rational isogenies of degrees 3 and 7 are excluded by the Frobenius discriminant a5^2-4*5=-16, nonsquare modulo 3 and 7. Degree 5 is excluded by a7^2-4*7=-12, nonsquare modulo 5. Here a5=2 and a7=-4 come from direct counts. For residual primes 2,3,11 choose multiplicative witness primes 3,11,3 respectively: each has minimal-discriminant valuation 1, so the residual representation is ramified there. Thus every hypothesis of that upgrade theorem holds. This corollary uses the cited preprint and its stated unpublished dependencies; it is not claimed as a consequence of elementary descent alone, and it does not use BSTW's undefined factor of 2.

## Frozen conclusion

For every prime in the stated family:

    Sel^phi = {1,33,q,33q}; Sel^hatphi = {1}; |Sel_2|=2;
    rank=0; Sha[2]=Sha[2^infty]=0;
    E_q(Q)[2^infty]=Z/2Z;
    (c2,c3,c11,cq)=(2,1,1,2);
    Omega_R=2 Omega+;
    v2(L_Z^alg)=1; v2(L_R^alg)=0;
    v2(|Sha| product(c_ell)/|tors|^2)=0;
    v2(N_q)=2; a_q=2 (mod 8), hence q ordinary.

BSTW period convention remains ambiguous. Banwait-Huang case (3) fails. Prior-art blockage remains unresolved because an explicit stronger BSTW statement already includes this curve; the absence of a verified route here is not absence of prior art. Stage I ends with this frozen reconstruction.
