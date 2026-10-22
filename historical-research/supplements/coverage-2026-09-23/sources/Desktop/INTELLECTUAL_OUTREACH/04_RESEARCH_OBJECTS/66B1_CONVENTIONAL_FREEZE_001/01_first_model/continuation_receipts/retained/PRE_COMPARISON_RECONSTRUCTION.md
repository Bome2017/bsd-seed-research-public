# PRE-COMPARISON RECONSTRUCTION: 66b1

This document is frozen before opening counts_66b1.py, counts_66b1_output.txt, or the 62a1 mechanism capsule. No conclusions from a previous conversation or another model are used. Source papers have been inspected on the web.

## Staging qualification

An initial archive-inspection command read every member whose basename was README.md or TASK.md. It inadvertently displayed 03_arithmetic_receipts/README.md as well as the two root documents. That revealed the inventory and the stated number 38 of qualifying primes below 4000, but not the code, valuation results, individual point counts, or control-table entries. This limited exposure was disclosed before proceeding. Consequently the arithmetic prediction below is blind to the withheld numerical outcomes, but the directory-access protocol was not literally perfect.

## 1. Period gate

Use a global minimal Neron differential omega. Define Omega^+ as the least positive real period of that differential, and Omega_R = integral over E(R) of |omega|. Each real component is a translate of the identity component and has the same invariant measure. Thus Omega_R = c_infinity Omega^+, where c_infinity is the number of real components. A real nonsingular Weierstrass cubic has two real components when its cubic discriminant is positive. Here Delta_min=528>0. Twisting multiplies the discriminant by q^6 before minimization; minimization changes it by a positive twelfth power. Its sign stays positive. In particular, for the positive twists considered here c_infinity=2.

Zhai, arXiv:1409.0231, p.2, defines Lalg_Z(E,1)=L(E,1)/Omega^+_E, with Omega^+ expressly the least positive real period of a Neron differential on a global minimal equation. Therefore, for this curve and its positive twists:

    Omega_R = 2 Omega^+;
    L(E^q,1)/Omega_R(E^q) = (1/2) Lalg_Z(E^q,1);
    v2(L(E^q,1)/Omega_R(E^q)) = v2(Lalg_Z(E^q,1))-1.

Miller, arXiv:1010.2431, p.1, explicitly defines the BSD period as integral over the full E(R). Banwait-Huang, arXiv:2601.16044v3, Definition 2.1 (p.3) follows Miller. Definition 2.7 defines Lalg using that Omega. Their proof of Theorem 2.14, remark (2), p.8, explicitly says their convention agrees with Cai-Li-Zhai [7] and that one subtracts the component-count valuation when using Zhai's convention. Cai-Li-Zhai, arXiv:1712.01271v2, pp.1-2, explicitly define Omega as the real Tamagawa factor, equal to Omega^+ or 2 Omega^+ according to connectedness. These sources determine the Banwait-Huang convention, not merely a guess from their unexpanded symbol.

Consequently the established datum L/Omega_R=1/4 is compatible with Lalg_Z=1/2: the valuations are respectively -2 and -1. Under Zhai's twist conclusion v2(Lalg_Z)=1, the full-period target is exactly 0, not 1.

BSTW qualification: arXiv:2409.01350v2, Conjecture 1.1 p.2, calls Omega_E a Neron period; Theorem 10.12 p.89 prints a full BSD formula with only finite Tamagawa factors. I have not located an explicit definition of this symbol as an integral over all real components. Merely calling it a Neron period does not settle the factor of two. Indeed Skinner's arXiv:1407.1093, the proof of Theorem C, section 3.3 p.25 (one of BSTW's references), defines his Neron period by an integral over a generator of H_1(E(C),Z)^+, which gives the primitive/least real period up to sign. Skinner's theorem is for odd primes and is insensitive to the component factor. Therefore it would be circular to infer BSTW's exact factor of two solely from its displayed BSD equality or its odd-prime proof. The literal BSTW-period import is not certified here. No downstream BSD conclusion using an unqualified identification of BSTW's symbol is authorized.

This is a source-normalization qualification, not an obstruction to the explicitly defined Miller/Banwait-Huang full-real-period target above. A standalone analytic-plus-descent experiment with that explicit target remains mathematically coherent. Any later stronger BSD transfer must either resolve the BSTW convention or use a separately stated theorem with an explicit full-real convention.

## 2. Analytic input

Zhai Theorem 1.7 (p.5): optimal E/Q, odd Manin constant, positive discriminant, nonzero rational 2-torsion, and L(E,1) nonzero; q an odd prime coprime to the conductor, q=1 mod4, with v2(N_q)=1-v2(Lalg_Z(E,1)) nonzero. Then L(E^q,1) is nonzero, v2(Lalg_Z(E^q,1))=1, and E^q(Q) and Sha(E^q) are finite.

The packet explicitly labels optimality, Manin constant 1, conductor 66, rank-zero central-value datum, and torsion Z/4 as established curve data. LMFDB's conductor-66 listing independently matches the coefficients, conductor, discriminant, rank, torsion, and Manin constant. The character-and-point argument in section 4 below supplies v2(N_q)=2, which equals 1-(-1). The family congruence gives q=1 mod4 and excludes 2,3,11, hence conductor coprimality. Thus Zhai 1.7 applies on the proposed prime family, with full-real-period analytic valuation 0.

Banwait-Huang Theorem 2.14 case (3) does NOT apply. Its common splitting hypothesis fails at 2 (q=5 mod8) and at 3 ((q/3)=-1). Condition (3a) requires v2(N_q)=1, whereas the rational 4-torsion already forces 4|N_q at every odd good prime. Condition (3b) asks for v2 of their full-period Lalg equal to -1, but 66b1 gives -2. Condition (3c) requires 2 split, false. Condition (3d) requires the quotient's rational 2-torsion to have order 2, whereas the quotient below has full rational 2-torsion of order 4. No change of notation can repair this without changing the theorem.

The literal BSTW Theorem 10.12 also has a separate applicability obstruction: condition (iii) says a_3(E)=0. At the nonsplit multiplicative prime 3 of 66b1, a_3=-1. Banwait-Huang Theorem 2.13 is a different, sharpened transfer statement and must not be silently substituted for BSTW 10.12.

ANALYTIC_CHAIN_66B1 = VIABLE_WITH_CONDITIONS: Zhai to the explicitly defined full-real BSD(2) target is viable; arithmetic equality is still to be proved, the Banwait-Huang case-(3) shortcut fails, and the BSTW-based full-BSD import is withheld.

## 3. Model and Selmer-shape reconstruction

Let u,v denote the minimal-model coordinates. Completing the square gives

    (2v+u+1)^2 = 4u^3+5u^2-6u-3.

The rational 2-torsion root is u=1. Set

    X=4(u-1), Y=8v+4u+4.

Direct expansion gives

    Y^2-X^3-17X^2-64X
      =64(v^2+uv+v-u^3-u^2+2u+1).

The inverse is u=X/4+1, v=(Y-X-8)/8. The corresponding projective linear map has determinant 32 and preserves [0:1:0], so it is an elliptic-curve isomorphism over Q and over every odd good finite field. Its discriminant is 2^16*33. Importantly, its displayed differential satisfies f^*(dX/(2Y))=(1/2)du/(2v+u+1). The nonminimal model's displayed differential is NOT the minimal Neron differential. This is another independent possible factor-of-two error.

For C_q: y^2=x^3+17qx^2+64q^2x, the quotient by {(0,0),O} is

    C'_q: y^2=x^3-34qx^2+33q^2x=x(x-q)(x-33q).

One quotient map, away from x=0, is

    x'=x+17q+64q^2/x, y'=y(1-64q^2/x^2).

Substitution verifies the target equation. The map extends, has kernel {(0,0),O} and degree 2. In particular C'_q has full rational 2-torsion, with nonidentity abscissae 0,q,33q. C_q has just one rational involution because 33 is nonsquare over Q.

A common unramified-outside-S ambient group is Q(S,2), S={2,3,11,q}. These are four distinct primes. Squareclasses are uniquely (-1)^e0*2^e1*3^e2*11^e3*q^e4, so the common ambient has 32 elements. This is an upper ambient, not a statement that each Selmer group must actually use every prime and sign.

With phi:C_q->C'_q, the phi Kummer map is x on C'_q, with the exceptional value at (0,0) equal to 33q^2, hence class 33. The four quotient torsion points give exactly

    {1,33,q,33q}.

All four are therefore globally realized and locally soluble everywhere; none can be removed by a genuine local obstruction. They are a mandatory lower bound on Sel^phi, not four speculative extra Sha classes. The dual Kummer value of the unique rational 2-torsion point of C_q is 64q^2, class 1. A trivial dual Selmer group is structurally possible.

There is no dimension contradiction: in the exact isogeny-Selmer comparison the rational dual-kernel term has order 2 (phi kills C_q[2]). If the proposed groups have orders 4 and 1, Sel^2(C_q) has order 2, the minimal size compatible with its rational 2-torsion. Thus the target is compatible with rank zero and Sha[2]=0.

I have not claimed the uniform upper bounds at every local place. They require a descent proof. No necessary real or global Kummer obstruction to the stated lower classes is found.

PREREGISTERED_SELMER_SHAPE = PLAUSIBLE.

## 4. Blind finite-field prediction

On C:y^2=x^3+17x^2+64x, T=(-8,8) lies on the curve. The tangent slope is -1 and 2T=(0,0). Thus T has exact order 4 in every odd good characteristic; the excluded characteristics are 2,3,11.

For y^2=x^3+a x^2+b x and y(P)!=0, the tangent formula gives

    x(2P)=[(3x^2+2ax+b)^2-4(x^3+ax^2+bx)(a+2x)]/(4y^2)
          =((x^2-b)/(2y))^2.

Therefore a half of T would force -8 to be square, equivalently -2 square. The infinity and y=0 cases cannot double to T and are excluded before division.

If 33 is nonsquare, the only rational involution is (0,0). A finite abelian 2-group with exactly two elements killed by 2 has one cyclic factor, so the 2-Sylow is cyclic. In a cyclic group of order 2^e an order-4 element is a double whenever e>=3. Thus if both -2 and 33 are nonsquares, v2(#C(k))=2.

In fact this condition is exact. If 33 is square, full 2-torsion together with T already forces a subgroup of order 8. If 33 is nonsquare but s^2=-2, the equation for doubling abscissa -8 factors as

    (x^2-64)^2+32(x^3+17x^2+64x)
       =(x^2+(16+4s)x+64)(x^2+(16-4s)x+64).

The discriminants of the factors are -32+128s and -32-128s, with product 32^2*33. Exactly one is square. A root x of that factor gives a curve point with

    y=(x^2-64)/(4s),

since the quartic equation says (x^2-64)^2=-32f(x). Its double has abscissa -8 and is T or -T; negation gives a half of T. The numerator is nonzero: the quartic at x=8 is 2048*33 and at x=-8 is 2048, nonzero in good characteristic. Therefore the Sylow group has order at least 8.

Prediction for every prime p not in {2,3,11}:

    v2(#C(F_p))=2  iff  (-2/p)=-1 and (33/p)=-1.

For the proposed family q=5 mod8, (-1/q)=+1 and (2/q)=-1, hence (-2/q)=-1. Reciprocity gives

    (33/q)=(q/3)(q/11)=-1.

So I predict v2(N_q)=2 throughout the proposed family, N_q=4 mod8 and a_q=2 mod8. The point-count and trace conditions and q not dividing 6N are redundant in the original family. The separate signs at 3 and 11 are retained for the descent target; the finite-field lemma consumes only their product.

A control table split only by ((2/p),(33/p)) across ALL good odd primes is expected NOT to be uniform in its second-character-minus columns: the missing (-1/p) changes (-2/p). This is predicted before seeing the table and is not a post-hoc repair.

POINT_COUNT_MECHANISM = DIRECT_62A1_ANALOGUE, understood as the independently reconstructed cyclic-2-Sylow/unhalved-rational-4-torsion architecture on the proposed q=5 mod8 family. The relevant signed character is -2, not 2. The label does not assert that the unsigned pair controls all primes, nor does it rely on reading the withheld capsule.

## Preliminary disposition

The period-converted Zhai target is mathematically coherent in the explicitly fixed full-real convention. A local-descent experiment is justified, but not a claim that Banwait-Huang case (3) or the literal BSTW Theorem 10.12 proves the result. A wrong local upper bound would require revising or rejecting the Selmer prediction; an obstruction to one of its four globally realized lower classes would instead expose an error in local conventions or computation. Strong-BSD transfer stays gated pending a fully applicable, normalization-explicit source chain. No result about Sha or BSD for the twist family is claimed in this frozen document.
