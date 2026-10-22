# Cofinite integral control of the seed's ordinary Hida branch

Grade: WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS_AND_STANDARD_HIDA_THEOREMS.
This is not an independent review, a literature-novelty claim, or a Sha bound.

## Statement

Let f be the rational weight-two newform of the retained seed, of exact
conductor N. There is a fixed nonzero integer D, defined using the finite
weight-two tame-level Hecke spectrum, such that, for every good ordinary
prime p >= 5 with p not dividing D, the full localized ordinary Hida Hecke
algebra through f, with its specified tame diamond character, is

    T_p = Z_p[[T]].                                      (H1)

We use the weight convention T = [1+p]-1 after shifting weight two to
T=0. The arithmetic point (weight 3, wild character 1) is T=p, with
nebentypus omega^(-1). Its minimal local coefficient ring is Z_p. The
ordinary modular-symbol modules of either sign are free of rank one
over Z_p[[T]], and integral control specializes a generator to a
primitive generator of the corresponding classical module.

The integer D below has not been numerically computed. It is defined
without Sha, a Kato value, or an assumed uniform bound. Its finite support
is enough for this cofinite structural statement. No new finite list of
settled Sha primes is being asserted.

## 1. A stronger non-anomalous property of this seed

In the original integral equation

    y^2 = x^3 - 22735 x^2 + 106272484 x,

(0,0) is a rational point of order two. Its image in the minimal equation
is (-7578,0), under x_old = x_min + 7578. Reduction at any odd good p
preserves this prime-to-p torsion. Consequently #E(F_p) is even, and
a_p = p+1-#E(F_p) is even.

For p>=7, Hasse gives |a_p|<=2 sqrt(p)<p-1. Thus the only integers in
that interval congruent to 1 or -1 modulo p are 1 and -1 themselves,
which are odd. At p=5 an exact count gives #E(F_5)=8, hence a_5=-2.
We have proved, for every good seed p>=5,

    a_p is not congruent to either 1 or -1 modulo p.     (H2)

This also proves that the familiar oldform determinant
(p+1)^2-a_p^2 is a p-unit. We do not use an unproved level-raising
theorem with auxiliary prime equal to the coefficient prime.

## 2. Define the fixed exceptional integer

List the finitely many Galois orbits of normalized weight-two newforms h
with trivial character and level dividing N. Omit the orbit of f. For
each remaining h, strong multiplicity one supplies a prime q_h not
dividing N with

    a_(q_h)(h) != a_(q_h)(f).

Choose one such q_h for each orbit, let K_h be the coefficient field,
and set

    D_0 = product_h q_h *
                   |Norm_(K_h/Q)(a_(q_h)(h)-a_(q_h)(f))|,
    D = 2*N*phi(N)*D_0.

Empty products are one. All differences are nonzero algebraic integers,
so D is a fixed nonzero integer. Including the q_h themselves ensures
that the detecting Hecke operators are away from the coefficient prime.
The phi(N) factor removes any ambiguity about reducing a nontrivial
prime-to-p diamond character to the trivial tame character.

If p does not divide D, no other tame-level newform h in this list can
have residual representation isomorphic to E[p]. A residual congruence
would force the chosen algebraic integer to vanish at a prime above p,
and hence force p to divide its norm. All embeddings of the coefficient
field are covered by taking the norm.

This is a separation integer for Hecke eigensystems. It is NOT an
annihilator of Sha or an independent bound on the weight-three Kato
index.

## 3. Exclude the moving, p-new part of the weight-two fiber

Fix the ordinary maximal ideal m determined by f and its ordinary
U_p-root alpha_p. Fix trivial tame diamond character at N; at weight
two, the chosen torsion component of weight space also gives trivial
diamond character at p.

A classical ordinary weight-two eigenform in this fiber has conductor
dividing Np. If its primitive newform has conductor divisible by p,
the exponent of p is one and its central character is unramified at p.
It is Steinberg with an unramified twist. The weight-two trivial-character
newform relation is U_p^2=1. Its ordinary unramified quotient therefore
has residual Frobenius eigenvalue +1 or -1.

For the seed, the ordinary unramified quotient has eigenvalue
alpha_p modulo p, equal to a_p modulo p. The inertia characters of the
two residual constituents are 1 and the nontrivial cyclotomic character,
so this unramified quotient is distinguished. An isomorphism of the
residual representations must identify these quotient characters.
Equation (H2) excludes the purported p-new congruence.

Equivalently, m includes the ordinary U_p eigenvalue, and a p-new
weight-two eigenform with U_p=+/-1 cannot belong to it. The argument
uses the standard ordinary local representation and the Steinberg
newform relation. It does not assert good reduction for the p-new form.

The remaining eigenforms are ordinary p-stabilizations of newforms of
level dividing N. Section 2 excludes all of them except f. The two
p-stabilizations of f have roots alpha_p and p/alpha_p; only the former
is ordinary. Hensel's lemma puts alpha_p in Z_p, since a_p is a unit.
There is therefore exactly one classical eigensystem in this localized
weight-two fiber, and its coefficients are in Z_p.

## 4. Determine the integral algebra, rather than its rational points

Hida's integral control theorem identifies the weight-two fiber of the
full ordinary Hecke algebra with the Hecke algebra acting faithfully
on these classical forms. This is the full algebra, not a normalization
of an unspecified branch. The preceding section leaves just f_alpha.
It follows that

    T_p / T T_p = Z_p.                                 (H3)

There is no hidden nilpotent contribution in this claim: the localized
classical space is the single ordinary stabilization of the newform of
exact level N, with multiplicity one. Its faithful Hecke algebra is a
subalgebra of Q_p, contains Z_p, and is integral and finite over Z_p.
It is Z_p.

Hida's theorem says that T_p is finite free over Lambda=Z_p[[T]]. Its
Lambda-rank equals the Z_p-rank of (H3), which is one. Alternatively,
the cokernel of Lambda -> T_p is finitely generated and is zero modulo
T, so Nakayama makes this map surjective. The structural map is
injective by Lambda-freeness. This proves (H1).

This step would be invalid if one had only an isomorphism after
inverting p. Here the integral control theorem is used explicitly.

## 5. Primitive symbols and the weight-three point

Residual irreducibility is retained for this seed. Ordinary
p-distinguishedness follows because the two inertia characters are
different. EPW's integral multiplicity-one theorem makes the two
localized ordinary homology/modular-symbol modules free of rank one
over T_p. Its control theorem, or the equivalent cohomological
formulation in Maksoud (14), transports a generator integrally at an
arithmetic point. Use the stated Atkin--Lehner/sign identification when
changing between homology, ordinary cohomology and anti-ordinary
cohomology; do not drop it as an unnamed unit.

Since T_p=Lambda, specialization T=p has image Z_p. Thus, on this
cofinite ordinary domain, one can choose the actual coefficient DVR
to be Z_p, pi=p, and the weight-three point is unramified. The
primitive weight-three modular-symbol line is obtained from an
explicit free family module. Its primitive generator remains unique
only up to a unit.

This removes the possible ramification exponent e_p from the proposed
division by pi_p^2 on this domain. It does not prove that this symbol
has the same integral period as the local Gauss-sum frame in the
preceding Kato calculation. That comparison is a different map.

## 6. Full family image on the same domain

The rank-one algebra conclusion also makes a relevant source hypothesis
checkable. Use the cohomological big representation on the free rank-two
module over R=Z_p[[T]]. Its inertia has an unramified subline. In a basis
adapted to this line its matrices have shape

    [1 *; 0 delta],

where, with the weight-two shift used above, the diagonal character is
delta=chi^(-1)<chi>^(-w). At an inertia element with chi=1+p its value
is ((1+p)(1+T))^(-1). Put

    tau=((1+p)(1+T))^(-1)-1.

Then (p,tau)=(p,T), so tau is an allowed second regular parameter.
Tame inertia gives every nonzero residual value on the second diagonal.
Residual image contains SL_2(F_p), by the retained seed input.

These verify all four hypotheses of Boston's Proposition 3 in the
appendix to Mazur--Wiles, printed page 263: residual fullness; an
inertia matrix with diagonal (1,1+tau); all residual diagonal (1,b);
and the indicated triangular shape for all inertia. Consequently the
big image contains SL_2(R). We use the abstract proposition, whose
hypotheses do not require tame level one, rather than extending the
level-one examples in the body of that paper by assertion.

Two primitive rank-one direct summands of R^2 can be carried to each
other by an element of SL_2(R): extend primitive generators to bases,
then adjust the complementary vector by a unit to set the determinant
to one. Thus one can choose the complex embedding as in Futterer
Proposition 3.11 so that the Betti plus line is the ordinary unramified
line. This is a choice for each p, not a p-independent Betti
trivialization. It has not been silently substituted for the fixed
period vector in the earlier Kato packet.

With this choice, integral surjectivity of the Eichler--Shimura map
identifies the complementary sign line with the ordinary cusp-form
line. On the full localized algebra R the unit conclusion follows
integrally, as proved in SOURCE_UNIT_REPAIR.md. This repairs the
source's density argument on our cofinite domain. It still does not
identify that source's de Rham period with the explicit Gauss frame
for D(g)(1) used by the retained local-index calculation.

## 7. Source and review boundaries

Primary inputs: EPW Theorem 2.1.2 (integral finite freeness and control),
Theorem 2.3.1(5) (ordinary quotient), and Proposition 4.1.1 (free signed
modules); Maksoud (10), (14) and Definitions 2.1.3/2.3.5 fix the weight,
sign and primitive-period conventions. Classical newform decomposition,
the Steinberg relation a_p^2=1 at weight two with trivial character,
strong multiplicity one, Hasse and prime-to-p torsion reduction are the
standard additional inputs.

Section 6 uses Boston's abstract Proposition 3 (Mazur--Wiles appendix),
the ordinary family inertia characters, and Futterer Proposition 3.11
and Theorem 2.39 with their stated realizations. The scanned Boston
proposition, including its fourth hypothesis, was visually inspected.

The proof is specific to the residual eigensystem of this seed. It
does not turn an adjoint congruence theorem into a theorem annihilating
the standard E[p]-Selmer group. Neither a numerical value of D nor a
new Sha calculation has been obtained. Independent review should
concentrate on sections 3--5 and the choice of the full Hecke algebra.
