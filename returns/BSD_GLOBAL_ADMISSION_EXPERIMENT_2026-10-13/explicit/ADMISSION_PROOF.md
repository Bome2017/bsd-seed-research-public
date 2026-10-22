# A computed global-admission row and a rejected local class

Date: 2026-10-13. Grade: written theorem application with exact certified number-field and finite-field computations; not human review or formal verification. This is a control experiment on the specified rational 5-isogeny, not a seed bound.

## What was calculated independently of Sha

The two curves and isogeny are retained from the explicit control:

A=[0,0,1,-19766893413,-1937478573143510],
F=[0,0,1,-14959712463303,-22270654620235278500],
phi:A->F of degree 5.

No Sha order, numerator, height, or L-value was an input to this computation. In particular the absence of a phi-kernel of Sha(A) below is an output of this descent calculation, not an assumption.

The complementary descent lives in the kernel field of hatphi, rather than the real quadratic field used for the two positive classes. We constructed

K'=Q(a), a^4-a^3+54671a^2-54671a+597816451=0.

It is isomorphic to Q(root(X^4+218685X^2+9564625845)). Its discriminant is 239115646125. PARI's unconditional bnf certification returns 1; the class group is C60 x C12 x C4 x C2 x C2.

The actual dual kernel polynomial on F is

X^2+4446595X+24714780636239/5.

The script constructs an order-five point T over K', verifies that the quotient is Q-isomorphic to A, and chooses the automorphism tau satisfying tau(T)=2T. Thus the required eigenspace is the eigenvalue 2 space; it is not selected by matching an expected Sha dimension.

## The complete eligible global source

Write K'(S,5) for elements modulo fifth powers with valuations divisible by 5 outside S. Sage's proof-enabled selmer_space constructs this Kummer space from certified class and unit arithmetic; it does not compute or assume an elliptic-curve Selmer group.

For S empty, the computed space has dimension 2. On the saved generator basis, tau has matrix

    [2 0]
    [3 4].

Therefore the required eigenvalue 2 space is exactly <(1,1)> and has dimension 1. The generators, coordinate maps, and complete arithmetic transcript are in admission.json and admission.out.

Miller–Stoll Theorem 11, with the same source matching as the earlier explicit control, gives

    Sel_phi(A/Q) = ker(K'(empty,5)^(1) -> U_{5,11}).

Here the target is explicitly the product of **local unit quotients**

    U_{5,11} = product over v in {5,11} of
      (O_{K'} tensor Z_v)^* / ((O_{K'} tensor Z_v)^*)^5.

It is not another global S-unit space or a linear dual. The map is localization: each global source class has valuations divisible by 5 at these places, so it has local unit representatives after dividing by local fifth powers. These define the displayed local unit classes. The source is restricted to its required Galois eigenspace.

Indeed Sigma1={11}, Sigma2=empty, w=1 and A(Q5)[phi]=0. The exceptional inequality-only case does not occur. For the upper bound used here even the inclusion in the displayed global source would suffice.

We compute the descent map directly, rather than infer it from the class-group dimension. Starting with T, the script evaluates the usual Miller product

    f5 = g(T,T)^2 g(2T,2T) g(4T,T),

where g(P,Q) is the line through P,Q divided by the vertical line through P+Q (with the standard vertical-line convention when P+Q=O). Its divisor is 5(T)-5(O). In the local parameter t=-x/y, each nonvertical line has leading term -t^(-3) and each vertical line has leading term t^(-2). The product above therefore has leading term -t^(-5), not +t^(-5). Multiplying it by -1 produces the leading-coefficient-one normalization. Because -1=(-1)^5, these two functions define exactly the same fifth-power descent class. The saved numerical values are for the script's unnegated Miller product; the membership and nontriviality tests are unaffected.

At the retained rational points

    Q1=(6288329,-11502941299),
    Q2=(8502485,21568458354),

the complete Kummer-space coordinate vectors are

    f5(Q1)=(3,3), f5(Q2)=(2,2).

They are nonzero and span the entire eligible eigenline. Rational points automatically satisfy all local Kummer conditions. Consequently, without using their rank or Sha order,

    Sel_phi(A/Q) = image(F(Q)/phi A(Q)),
    Sha(A/Q)[phi] = 0.

This is a statement about the phi-kernel, not the whole Sha(A)[5]. The existing two positive classes belong to the opposite isogeny kernel Sha(F)[hatphi]. Those groups must not be conflated.

## A nonzero local class excluded by the complete global source

Before the auxiliary scan, local_scan_protocol.md fixed ascending primes q <= 5000, good for the curves, not 5, splitting completely in K', the first residue root embedding, and the first point with a non-fifth-power descent value.

The initial implementation omitted the necessary q = 1 mod 5 restriction. Its q = 4 mod 5 rows were invalid fifth-power tests and are preserved as an explicitly superseded trial in historical_trial/. The corrected complete scan requires q = 1 mod 5 and again has first success q = 331. In the embedding a->67, the kernel point is T=(85,247), and

    #F(F331)=325,
    f5(Q1)=112, f5(Q2)=89,
    112^66=89^66=1 mod 331.

Thus the entire eligible global eigenline has zero localization in the fifth-power quotient. Yet the actual local point R=(1,102) satisfies

    f5(R)=40, 40^66=150 !=1 mod 331.

The reduction point is smooth and lifts to a Q_331 point. Since 331 is good and different from 5, its descent class is an actual nonzero local isogeny-Kummer class. It cannot be the localization of any global phi-Selmer class: every such global class is already in the eigenline whose local image was computed to be zero.

This proves failure of global admission without reading a Sha value or deducing rejection from a previously known vanishing theorem. The test is complete because the global candidate source was independently computed, not because a finite list of global points or classes happened to have zero image.

## An explicit ideal-class compatibility equation

We also enlarged the source by allowing valuations at the four primes above 11. This is a diagnostic source enlargement, not a relaxation silently used in the Selmer theorem.

Order the primes P1,...,P4 as in admission.json. Their class coordinates in C60 x C12 x C4 x C2 x C2 are

    (59,0,1,0,0), (1,0,3,0,0),
    (43,2,3,1,0), (17,10,1,1,0).

Modulo 5Cl(K'), their classes form the row

    c=(4,1,3,2).

The automorphism permutes their indices by [2,3,1,0] (zero-based). Its eigenvalue 2 divisor line is generated by

    v=(1,4,3,2).

The exact compatibility equation for valuations of a global element is

    c dot valuations(alpha) = 0 mod 5.

This follows by taking the principal ideal (alpha): valuations outside 11 are multiples of 5, so the remaining divisor must vanish in Cl(K')/5Cl(K'). But

    c dot v =1 mod 5.

Thus no nonzero vector on this particular character-valued local divisor line can occur as the valuations of a globally eligible element. This obstruction is a computed ideal class, not Sha in another notation.

The complete 5-dimensional enlarged Kummer space gives valuation matrix

    [0 0 1 0 0]
    [0 1 0 0 0]
    [1 0 0 0 0]
    [1 2 3 0 0].

Its rank is 3, its image is exactly ker(c), and the eigenvalue 2 part remains one-dimensional with zero valuation at 11. This directly verifies both the obstruction and the absence of a hidden additional direction in the enlarged source.

## Boundary for transfer to the seed

This gives the process a concrete successful prototype: compute a finite global Kummer source, impose its Galois eigenspace condition, and compare its actual image with a nonzero local target. It separates globally admitted positive control classes from a locally valid but globally excluded class without using an analytic or Sha answer.

The seed has no rational 5-isogeny under its retained full residual image. Its corresponding source is not this quartic field or this one-dimensional eigenspace. A seed exclusion would require a certified source for the seed's full 5-torsion representation and its actual global/local image. This computation does not establish that source bound, nor any uniformity in coefficient primes.

FIN, ORDER9, Q36 and unresolved seed-prime coverage remain unchanged.

## Sources and checks

Freshly read: Miller–Stoll, Explicit isogeny descent on elliptic curves (23 January 2011), §§2–3 and Theorem 11, https://www.mathe2.uni-bayreuth.de/stoll/papers/isogeny-descent.pdf . This gives the source eigenspace and local kernel description. The concrete field, Galois action, class/unit spaces, point evaluations and prime 331 values were computed here.

Retained source conditions: named minimal models and isogeny, local Tamagawa ratios, w=1, 43737 being a nonsquare modulo 5, and the displayed points. Rank and saturation are not needed to prove the new isogeny-kernel vanishing because an explicit rational point already spans the fully computed eligible source.
