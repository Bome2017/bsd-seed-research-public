# Review of the explicit norm-one unit and residual irreducibility

2026-10-13. Same-team, separate-agent written review. I read REPORT.md,
seed3/RESULT.md, the portable checker and its saved output, the original
covering certificate and its replay, and irreducible_source.gp/.out. I ran
no new arithmetic and do not present this as an independent numerical replay
or a formal certificate.

## Verdict

The claimed positive norm-one unit represents an actual nonzero seed
Sha[3] direction, under the retained covering-to-cohomology identification
and rank upper bound. It is not merely an arbitrary noncube field unit.
The separate orbit calculation proves residual irreducibility at 3 and
excludes a rational 3-isogeny. It does not prove full residual image or good
reduction at 3.

## Why the unit remains a non-point class

Let phi_T be the retained Weil-pairing descent homomorphism from
H^1(Q,E[3]) to K*/K*^3. Let xi_1,xi_2 be the precise Selmer lifts whose
images are the reconstructed beta_1,beta_2, allowing the retained Cardano
inversion convention. Their all-place membership and the four image
independence are supplied by the earlier covering certificate and its
replay, rather than by the new class-group computation.

The image independence means that beta_1-beta_2 is not in the span of the
two point images: such membership would be a nontrivial relation among
the four independent columns. The retained rank upper bound of two and
E(Q)[3]=0 make E(Q)/3E(Q) two-dimensional. Since the two displayed point
images are themselves independent, they span its entire image. Thus
xi_1-xi_2 has nonzero image in Sha(E/Q)[3]. This deduction does not need
injectivity of phi_T on all of H^1: image independence already implies
the needed independence in its source.

The portable certificate checks that epsilon=beta_1/(beta_2*g^3) is a
global unit by factoring the complete compact product and checking all
its finite valuations are zero. Removing the literal cube does not change
its Kummer class. Consequently epsilon represents precisely the preceding
non-point direction. This positive conclusion does not use completeness
of the GRH class-group calculation. The full (0,1,1) filtration still
retains that separate qualification.

## Anti-invariance and exact norm one

The even defining polynomial gives the involution tau(w)=-w, and the
portable output records the exact check tau(T)=-T. For a global class xi,
naturality of restriction and the Weil pairing gives, in K*/K*^3,

    tau(phi_T(xi)) = phi_{tau(T)}(xi) = -phi_T(xi).

This is an equality of Kummer classes. It does not assert that arbitrary
chosen field representatives are literal inverses.

It follows that

    [epsilon/tau(epsilon)] = 2[epsilon].

Multiplication by two is invertible on the F_3-vector space, so this remains
nonzero modulo the rational-point plane. On the other hand the field
identity

    (epsilon/tau(epsilon))*tau(epsilon/tau(epsilon)) = 1

is literal. Since K/Q(w^2) is quadratic, epsilon_minus is an actual global
unit of relative norm one. The checker binds the exported compact factors
to this quotient; it does not merely test its norm numerically. No claim
that every norm-one unit is a Selmer image follows or is needed.

## Orbit argument

The separate saved check establishes that f_K is irreducible of degree
eight, T is a nonzero 3-torsion point in E(K), and its y-coordinate has
minimal polynomial of degree eight. Hence

    Q(T_y)=Q(T)=K,

and the G_Q-orbit of T has eight elements. There are exactly eight nonzero
vectors in E[3]. The action on them is therefore transitive. A nonzero
proper invariant line would have two nonzero vectors and contradict this
transitivity. Thus E[3] is irreducible, excluding a rational 3-isogeny.

Transitivity alone does not determine the whole image in GL_2(F_3).
Moreover 3 divides the retained seed conductor. The example remains
outside the good-prime p>=5 Kato/receiver domains. It supplies a genuine
non-isogeny control for a proposed unit exclusion, not a transfer theorem
or a new upper bound at another prime.

FIN, ORDER9, Q36 and prime coverage remain unchanged.
