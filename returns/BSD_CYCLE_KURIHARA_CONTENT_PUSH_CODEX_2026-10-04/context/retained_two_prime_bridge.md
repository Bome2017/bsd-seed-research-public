# Attempt (ii): obtain a unit at two Kato primes

## Reopening statement

**DERIVED — previous failure and new input.** The previously screened route transfers an unspecified-length unit witness to a character valuation estimate. Its first unresolved step was an independent bound on the witness length. Attempt (i) adds the multivariable Fitting lower bound and the exact initial form

    theta_L mod (p,J^(r_p+1)) = delta_n product_(q|n) T_q

at a minimum unit witness. This sharpens the transfer but does not shorten a witness. This file tests whether its algebra can provide the missing shortening.

## Proposition II.1: two-prime transfer with exact normalization

**DERIVED at the stated import grade.** For a good p>=5 and two distinct Kato primes q_1,q_2, let L be the C_p^2 compositum of their degree-p cyclotomic subfields and write J=(T_1,T_2) in F_p[Gal(L/Q)]. Using only the rank-two lower bound, BH Theorem 1.4(b), and BH Proposition 2.4,

    theta_L^MT mod (p,J^3) = delta_(q_1 q_2) T_1 T_2.        (II.1)

Here delta uses the total real period, as in v2 §5. In particular, if delta_(q_1 q_2) is a unit, every quotient gamma_i |-> gamma^(s_i), s_1 s_2!=0, produces a real degree-p field of actual conductor q_1 q_2 and

    theta_K^MT mod (p,t^3) = s_1 s_2 delta_(q_1 q_2) t^2,
    v_(zeta_p-1)(chi(theta_K^MT))=2.                         (II.2)

**DERIVED — proof independent of minimum-length selection.** Base rank two and dual Kummer give d_p>=2. Apply Lemma I.1 with the weaker exponent two to L and to each of its one-prime cyclotomic factors. Projection from conductor q_1q_2 to q_1 gives an Euler factor in (T_1)^2 multiplying an element in (T_1)^2, hence an element in (T_1)^4. Thus the pure quadratic T_1^2 coefficient of theta_L modulo p is zero; the other projection similarly kills the pure T_2^2 coefficient. Constant and linear terms are already zero. Expansion of the complete plus-symbol sum identifies the remaining coefficient with delta_(q_1 q_2), exactly as in Lemma I.3. The valuation and conductor argument is the degree-two instance of Proposition I.4.

**DERIVED — finite constructive content.** Given an already certified unit pair, choose both s_i=1. Then

    K = fixed field in L of kernel((u,v) |-> u+v),
    chi(gamma)=zeta_p

is an explicit abstract field/character construction and has exact depth two. There is no search for an additional prime and no diagonal cancellation problem. This does not provide the input unit pair. No such pair at an unsettled p was computed here.

## Candidate II-A: lower the degree by projection or conductor norms

**DERIVED — filtered-operation obstruction.** Let A and B be mod-p group algebras with augmentation ideals J_A,J_B. Any group homomorphism induces an algebra map carrying J_A^k into J_B^k. Addition and multiplication by an integral group-ring element preserve membership in a fixed augmentation power. Multiplication by a unit and its inverse does too. Therefore any finite sequence of these operations, starting with inputs in fourth augmentation powers, stays in a fourth augmentation power.

For a C_p output with p>=5 this forces character depth at least four: terms of degree at least four contribute depth at least four, and coefficients divisible by p contribute depth at least p-1>=4. Thus these operations cannot turn a length-four minimum-witness initial form into a v2 §5(i) witness. This is a theorem about the specified filtered operations, not a nonexistence theorem for new arithmetic constructions.

**DERIVED — nonunit division is the precise missing operation.** At a Kato prime the reduction of the norm factor is

    2-u-u^(-1)=-(u-1)^2/u.

It is a nonunit, not a harmless Euler unit. Formally differentiating a higher-degree polynomial or dividing this factor can lower degree, but no identity identifies that formal result with a full Mazur–Tate element at a smaller actual conductor or with the required two-prime Kurihara quantity. Such an identity would be a new arithmetic input. None was proved.

**DERIVED — first failing test.** K-S. The endpoint claim that primitivity plus these filtered operations forces a length-two unit holds equally in the retained four-generator countermodel, where it is false. K-P and subsequent endpoint tests are not promoted to passes. The filtered-operation lemma itself is retained as a scoped obstruction to this particular shortening strategy.

## Candidate II-B: separate the two rational basis points by two local conditions

**DERIVED — paired-state calculation.** Suppose two local conditions distinguish the two-dimensional Mordell–Weil Kummer subspace V perfectly. That fact is compatible with either

    S_good=V,
    S_excess=V direct_sum W,    dim_Fp W=2.

For both spaces use the same map to F_p^2: the identity on V and zero on W. The determinant of the map on the rational-point subspace is nonzero in both states. The second state still has two excess Selmer dimensions. Thus a determinant computed only from the two rational basis directions does not by itself prove a Selmer upper bound.

**DERIVED — G2 does not supply the omitted implication.** In the controlling brief, G2 uses trace -2 auxiliaries and proves a nonzero tame regulator. The target Kurihara conductors use trace +2 Kato primes. For odd p these are different congruences. Theorem W can have w_p=0 while its tame regulator is nonzero, so nondegeneracy of that regulator is not the missing unit numerator. A new theorem connecting these local determinants to the full Selmer space, not merely its rational-point subspace, would be needed.

**DERIVED — first failing test.** K-S. The same rational-point determinant is compatible with excess Selmer. This rejection does not say that p-dependent Kato-prime constructions are invalid; it isolates the extra global comparison they must establish.

## Candidate II-C: descend from an arbitrary unit vertex

**DERIVED — exact algebraic test.** B.20 guarantees a unit at some length, while B.21 identifies the first unit length with d_p. The module

    X=Z_p^2 direct_sum (Z/p)^2

has Fitt_2(X)=(p^2), Fitt_3(X)=(p), and Fitt_4(X)=Z_p. A primitive higher-index datum may therefore be a unit at length four while all length-two data have positive valuation. The statement that the minimum can always be reduced to the Mordell–Weil rank deletes precisely this torsion contribution.

**DERIVED — first failing test.** K-S. No validated descent identity removing the torsion contribution was found. A derivative or a change of notation is not an identity of Kurihara quantities of different conductor lengths.

## Numerical and coverage boundary

**DERIVED.** Equations (II.1)–(II.2) compare full BH elements with total-period Kurihara quantities. The production symbol is twice the total-period symbol on this seed; inserting production values without dividing by two would change the exact coefficient, although not its being a p-unit. These equations neither calculate nor constrain the singleton scalars to equal 288 or 24 as rational numbers. The comparison applies to every good p>=5 under the retained seed inputs, including 19,59,487. No new two-prime unit pair, unsettled primary vanishing, or infinite subset of vanishing primes has been established.
