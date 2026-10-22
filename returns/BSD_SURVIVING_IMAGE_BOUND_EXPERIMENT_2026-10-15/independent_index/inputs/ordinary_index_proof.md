# Integral incidence norms and a mirror class-number prediction

2026-10-13. Written review and deduction by another agent in the same team.
The producer's exact identities and code were inspected; its run was not
independently regenerated. Cached class-group completeness retains its
original GRH-dependent grade. No class group of the new field was computed.

## 1. The constructed map is the arithmetic source-admission norm

The inspected files are `checks/affine_norm.gp`, its output, and
`data/affine_norm_certificate.gp`. They use the original model

    y^2 = x^3 - 22735 x^2 + 106272484 x.

The retained torsion coordinates are on the minimal model; the script
correctly changes x by +7578. This is necessary: the rejected unshifted
trial is not a certificate for this incidence map.

Write a=-22735 and b=106272484. The new field is

    B = Q(z),
    z^8 - 10695389742 z^4 + 189820747845720 z^2
        - 9532613477773235547 = 0.

It has signature (2,3). The script takes slope s=z/3 and the displayed
intercept t, and forms the actual line-intersection polynomial

    G(x)=x^3+(a-s^2)x^2+(b-2st)x-t^2.

The map from the old torsion field A=Q(w) into B[x]/G is checked against
the defining polynomial and both coordinates of the torsion point. It
also checks that G divides the 3-division polynomial. The latter is
separable since E is nonsingular in characteristic zero, so this is an
etale incidence algebra, not a nonreduced substitution.

The three intersection points are nonzero 3-torsion points and their sum
is O. Three distinct nonzero elements of F_3^2 with sum zero form an
affine line not through zero. The irreducible degree-eight slope
polynomial gives eight distinct conjugate lines, the full set of such
lines. Thus B is the algebra of nonzero linear forms on E[3], with each
form represented by its level-one affine line.

Consequently the norm being computed is precisely

    u = N_{D/B} o i_{D/A},  D=B[x]/G.

This identification is the source construction in Schaefer--Stoll,
*How to do a p-descent on an elliptic curve*, Corollary 7.9 and
Proposition 7.10, with the explicit p=3 model in Section 10:
https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf

All four saved norm values have exact cube roots in B, checked by equality
in B. This establishes vanishing of this actual global admission norm
on the four specified classes. It is stronger than testing a selection
of split-prime residues. It is not a new upper bound on their span.

## 2. Integral composition, including the scalar-character convention

The following is a direct counting argument, not an assumed reflection
principle. Let V=E[p] and let A and B be the etale algebras of V minus
zero and V-dual minus zero. For a function alpha on nonzero vectors set

    u(alpha)(lambda) = product_{lambda(P)=1} alpha(P).

The transpose incidence norm is

    v(beta)(P) = product_{lambda(P)=1} beta(lambda).

Both are actual inclusion/norm maps and preserve global units. Counting
linear forms taking value one at both P and Q gives the exact identity

    vu(alpha)(P) = alpha(P)^p
                      product_{Q not in <P>} alpha(Q).

For Q=P there are p forms; for Q=aP with a not equal to one there are
none; for independent P,Q there is exactly one. The dual identity holds
for uv. On the minus eigenspace for P maps to -P, the extra product
cancels in pairs Q,-Q. In additive notation on completed unit lattices,

    vu = p Id,       uv = p Id.                         (1)

Use the internal scalar pullbacks sigma_a^A f(P)=f(aP) and
sigma_a^B g(lambda)=g(a lambda). Direct substitution gives

    u sigma_a^A = sigma_{a^{-1}}^B u.

Thus u takes the chi component to the chi^{-1} component. It is
incorrect to identify the two characters for general p. Their ranks
agree; the required odd scalar component has rank (p+1)/2. At p=3
the character is its own inverse and its rank is two.

Let U_A and U_B denote the actual free Z_p unit lattices in one such
matched pair of nontrivial odd components. Equation (1) implies that u
and v are injective and both cokernels are killed by p. Every Smith
exponent is consequently either zero or one. If u has s exponents equal
to one in rank d, v has d-s, and

    dim_Fp ker(u mod p) = length_Zp coker(u) = s.       (2)

This is an arithmetic invariant of the actual unit lattices. A matrix
on a convenient unsaturated subgroup does not compute it. Equation (1)
alone permits every s between zero and d, so it supplies no small
uniform bound on the source-admitted unit space.

## 3. Actual seed consequence at 3

The prior portable nonpoint-unit certificate and the new point-unit
certificate put two independent actual classes in the unit group.
Their anti-invariant reductions fill the rank-two minus unit space.
Their independence is inherited from the four retained independent
descent images. This step retains the grade of those certificates; it
does not infer independence from the desired Sha order.

Both classes are actual admitted H^1 classes. The affine norms above
are cubes. A cube root of a global unit is itself a global unit, by
valuation at every prime. Hence u is zero modulo 3 on the entire
minus unit lattice. Combining with (1) and (2) gives

    coker(u on minus units) = (Z/3)^2,
    v on minus units is an isomorphism.                (3)

These are statements about completed lattices; no basis of the entire
target unit group has been computed. The conclusions follow from the
two certified source classes, the exact rank, and the integral norm
compositions. A finite-index guessed target basis is not substituted.

## 4. A derived class-number formula for the index

There is a further independently testable consequence. Suppose the
nonzero vector orbit is transitive; the dual orbit is then transitive
as well. Let A+ and B+ be the subfields fixed by the internal scalar -1.
Let h denote ordinary ideal class numbers. Put

    R = (p^2-1)/4,
    s_minus = length_Zp coker(u: U_A^- -> U_B^-).

Then the following written deduction gives

    s_minus = R/2 + v_p(h_B/h_A) + v_p(h_A+/h_B+).     (4)

Here the full minus component is used. For p greater than three this is
larger than the one scalar-character component relevant to descent.

Proof of (4):

* For every Galois matrix g, the numbers of fixed nonzero vectors and
  fixed nonzero covectors are equal: both are p to the nullity of g-I,
  minus one. The corresponding permutation characters therefore agree.
  Artin formalism gives zeta_A=zeta_B. For the quotients by plus/minus,
  fixed orbit counts are one half of the sum of the fixed-vector counts
  for g and -g. Thus zeta_A+=zeta_B+ also. This proves the needed
  arithmetic equivalence rather than assuming that the fields are
  isomorphic.
* Logarithms at all complex embeddings give real Euclidean spaces with
  complex conjugation invariant and scalar -1 anti-invariant. On these
  spaces u and v are transpose incidence matrices. Equation (1) hence
  gives absolute real determinant p^(R/2). The unit-lattice index is
  this determinant times covol(U_A^-)/covol(U_B^-).
* Splitting the units into plus and minus lattices changes the index by
  a power of two only: multiplying any unit class by two expresses it
  as its plus part plus its minus part. The plus lattice agrees with
  the units of the fixed field up to a power-of-two index. Therefore
  the ratio of odd covolumes agrees, at odd primes, with

       (Reg A / Reg A+) / (Reg B / Reg B+).

  All Euclidean versus usual regulator factors cancel because the two
  pairs have the same signatures and the same involution on their
  embedding sets. This is why no uncomputed p-adic regulator unit is
  hidden here.
* The analytic class-number formula, together with the equal zeta
  functions, replaces that regulator ratio by

       h_B h_A+ / (h_A h_B+)

  up to a power of two. Discriminants and archimedean factors agree
  within each arithmetically equivalent pair. All four fields have a
  real embedding, so their roots of unity are exactly plus/minus one.
  Taking p-valuations proves (4).

The analytic class-number formula used here is the number-field theorem,
not BSD or an assertion about an elliptic-curve L-value. A primary
reference is MIT 18.785, Theorem 19.12:
https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec19.pdf

For p=3, R=2 and (3) says s_minus=2. The two plus fields are isomorphic.
One way to see this without a polynomial coincidence is that the map
from a projective covector to its kernel is an equivariant bijection to
projective vectors in dimension two; at p=3 projective vectors are
exactly nonzero vectors modulo plus/minus. It follows that

    v_3(h_B/h_A)=1.                                   (5)

The retained A class group is [12,6,2], so v_3(h_A)=2. Under that retained
class-group grade, (5) predicts v_3(h_B)=3. This does NOT compute h_B,
prove h_B=432, determine its 3-primary group structure, or claim a new
Sha bound. It is a concrete mirror-field class-number prediction to
check independently if a future budget allows that computation.

There is also an explicit curve-side identification at p=3. The Weil
pairing gives V-dual = V tensor det(V)^(-1). Modulo 3 this determinant
character is the quadratic character of Q(sqrt(-3)), so V-dual is the
3-torsion representation of E^(-3). Thus B is a nonzero-torsion point
field of that specific quadratic twist. Applying the source-admission
theorem to the twist makes v its affine-line admission norm, after the
canonical double-dual identification. Since v is invertible on the minus
unit lattice modulo 3, this twist has no nonzero unit-supported global
cohomology class in that source component. This says nothing about the
twist's ideal-class-supported cohomology, its rank, or its Sha. For p
greater than three the cyclotomic twist is generally not a quadratic
elliptic-curve twist, so this last identification must not be extrapolated.

## 5. Local-row correction and the remaining use

The producer repaired a historical empty-matrix error. For local Kummer
image zero, every coordinate of the local image must vanish. The
annihilator is the full local dual space, so the correct row block is
the entire evaluation matrix. Skipping it because an empty matrix has
no rows is mathematically wrong. The corrected reported dimensions are

    local source kernel 4; local unit kernel 2;
    local plus global source kernel 4.

The local dimension test is dim E(Q_l)/3E(Q_l) =
dim E(Q_l)[3] + indicator(l=3). The number of nonzero rational local
3-torsion points is the number of degree-one completions of the
nonzero-torsion field. Thus zero expected image at 2, 2243, 4547 does
not rely on a random point search. Positive local images still retain
the local arithmetic and precision grade of the helper. The corrected
source kernel equals the independently known four-class lower space;
the old narrative of three additional locally admitted classes removed
only by global relations must not be retained.

The exact map u and its integral unit index now expose a specific source
quantity one can compute without an L-value or a Sha answer. Formula
(4) also explains why the transpose identity alone cannot furnish the
desired bound: the actual unit lattice can carry an asymmetric class-
number contribution even when the two fields have identical zeta
functions. For p greater than three, one must additionally resolve the
individual scalar-character component and local conditions. No bound
on those arithmetic indices across p has been proved here.
