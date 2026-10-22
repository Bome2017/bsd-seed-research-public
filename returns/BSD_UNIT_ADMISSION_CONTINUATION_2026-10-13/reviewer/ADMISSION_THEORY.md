# Exact source admission and the unit/class coupling

2026-10-13. Written mathematical analysis by a separate agent in the same
team. This does not re-certify the cached class/unit groups. No heavy
computation was run. The current stage1 output was inspected, not rerun.

## 1. Source admission is stricter than norm one

Use R=Map_GQ(E[p],Qbar)=Q x K when the nonzero torsion points form one
orbit. Set alpha(O)=1. The Weil pairing defines w:E[p]->mu_p(Rbar).
For a function alpha on torsion points put

    partial(alpha)(T1,T2)=alpha(T1)alpha(T2)/alpha(T1+T2).

The exact sequence of Galois modules

    0 -> E[p] -> mu_p(Rbar) -> im(partial|mu_p(Rbar)) -> 0

gives a canonical source-admission obstruction

    D_G: R*/R*^p -> H^1(Q,im(partial|mu_p(Rbar))).

Its kernel is the image of w1:H^1(Q,E[p])->R*/R*^p. For prime p this
w1 is injective; the identity component is trivial modulo pth powers,
so it can be suppressed. These facts are stated in Cremona--Fisher--
O'Neil--Simon--Stoll, *Explicit n-descent I*, Lemma 3.1, and *III*, §2.3.
[Primary paper I](https://www.dpmms.cam.ac.uk/~taf1000/papers/n-descent-I.pdf)
[Primary paper III](https://mathe2.uni-bayreuth.de/stoll/papers/Explicit-Descent-III.pdf)

One exact arithmetic admission certificate is a symmetric rational
two-cochain rho satisfying

    partial(alpha)=rho^p,
    rho(T1,T2)rho(T1+T2,T3)=rho(T1,T2+T3)rho(T2,T3),
    alpha(T)=product_{i=0}^{p-1} rho(T,iT).

Such a certificate gives a genuine class. These are the compatibility
conditions in paper I, Lemmas 3.5 and 3.8. Thus merely finding independent
pth roots of partial(alpha), or testing addition at several split primes,
must not be silently promoted to a complete admission proof.

For a finite set S, local point evaluation gives linear defect maps

    D_v: K*/K*^p -> (K tensor Q_v)*/(K tensor Q_v)*^p
                         / w1,v(kappa_v(E(Q_v))).

The precise unramified-source and local-image algorithm is paper III,
Proposition 2.3 and Theorem 2.4. Retain all necessary places, including the
coefficient prime; do not replace unramified Kummer conditions at p by
valuation divisibility. On a complete finite source B, D=(D_G,(D_v)) is
an exact admission map. A finite residue implementation D_screen can
instead be used as a necessary screen. Its kernel is then a containing
space; a matching independent lower space can certify completeness of
that particular intersection without proving every individual screen
globally sufficient.

## 2. What anti-invariance does, and a uniform source-rank calculation

For tau:T->-T, every global cohomology image satisfies

    tau[alpha]=-[alpha], equivalently [alpha*tau(alpha)]=0.

This is only the scalar -1 part of linearity on E[p]. For every a in
F_p*, admission also requires

    [a]^*[alpha]=a[alpha].

These relations do not include addition of independent torsion points.
The explicit seed epsilon_minus is a positive countercontrol: anti-
invariance and even literal norm one do not imply a rational-point class.

There is an independent rank explanation for the sharp cut at p=3.
Assume E[p]\{0} is a single G_Q orbit, and write C=F_p* for scalar
automorphisms of K=Q(T). Complex conjugation has eigenvalues 1,-1 on
E[p], so K has signature

    (r1,r2)=(p-1, p(p-1)/2).

The real places form one regular C-orbit. Among complex places, the
negative conjugation eigenline gives one C/{+-1} orbit. The remaining
complex places form (p-1)/2 regular C-orbits. Dirichlet's unit theorem,
with its equivariant logarithmic embedding, therefore gives the rational
C-character of the units as

    ((p+1)/2) Reg_C + Ind_{ {+-1} }^C(1) - 1.

This character computation is derived here by counting the places; it is
not an estimate on a Selmer group. Since |C|=p-1 is prime to p, its
idempotents are integral over Z_p. The unit group has no p-primary roots
of unity: K has real embeddings. Consequently the scalar-character
eigenspace required by [a]^*alpha=alpha^a has F_p-dimension exactly

    (p+1)/2.

The tau=-1 eigenspace alone has dimension (p^2-1)/4. For p=3 both
dimensions are two, whereas for p=5 they are respectively three and six.
Thus the p=3 anti-norm unit bound does not extend as a dimension-two bound
at larger primes. Full scalar homogeneity is a concrete next necessary
constraint there; torsion additivity remains an additional constraint.

For the present degree-eight field, the same result is visible from
signature(K)=(2,3), signature(K^tau)=(2,1): relative unit rank is 4-2=2.
The certified point-unit direction and certified non-point unit direction
already fill this anti-invariant unit space. Any proposed extra necessary
condition that removes the latter is false for this seed at 3.

## 3. An actual coupling map, rather than an assumed pairing

For B=K(empty,p), meaning valuation zero modulo p at every finite prime,
let U be the image of O_K* modulo pth powers and C_K=Cl(K)[p]. There is
an exact sequence

    0 -> U -> B -> C_K -> 0.

Let D:B->Y be any named linear admission map, exact or a specified
necessary screen. For c in C_K choose beta with (beta)=a^p and [a]=c.
Define

    kappa_D(c)=D(beta) mod D(U) in Y/D(U).

This is independent of the lift because two lifts differ by a unit
class. A class-group direction is admitted precisely when its defect can
be cancelled by a unit correction. Elementary lifting gives

    0 -> ker(D|U) -> ker D -> ker kappa_D -> 0.

For a rational-point subspace W contained in ker D, quotienting gives

    0 -> (ker(D|U))/(W intersect U)
      -> (ker D)/W
      -> (ker kappa_D)/c(W) -> 0.

This is directly executable: express D on unit columns and chosen ideal-
class lift columns, then reduce the latter columns modulo the former's
column span. It avoids treating the unit and ideal-class terms as unrelated
or declaring a perfect pairing that has not been constructed. A uniform
rank lower bound on these actual defect matrices would be independent
arithmetic input; the exact sequences alone are not such a bound.

## 4. What the certified seed classes already force

Under the retained Cl(K)[3]=F_3^2 grade, the class images of P2 and beta1
are independent and span C_K. They are both actual admitted classes.
Therefore kappa_D is already forced to be zero on all of C_K, for every
legitimate necessary admission map D. This is a prediction fixed before
any new coupling computation. A nonzero result would identify a source or
implementation error, not reject those certified classes.

Similarly the actual point-unit and beta1-beta2 unit directions force
dim ker(D|U)>=2. The source-rank calculation above gives the matching
upper bound after exact anti-invariance. Thus, subject to source
completeness, the expected kernel has dimension 2+2=4, with excess
contributions one unit and one ideal-class direction after quotienting W.
The observed stage1 dimensions (all-valuation-zero six; anti-invariant
four; norm-plus-additivity-screen four) are consistent with this argument.
Their printed values are not used as a proof that finite residue sampling
establishes all global relations.

## 5. Duality does not create an extra exclusion here

The unit/class filtration is not itself a self-dual decomposition. No
canonical perfect pairing between its two graded pieces has been supplied.
Even a perfect alternating pairing on their two-dimensional excess would
be compatible with both directions surviving. A secondary pairing could
measure higher liftability, but would not eliminate actual Sha classes
from the first Selmer group. Treating its nonzero entries as membership
equations would reject the positive control.

The next concrete construction is therefore the block defect matrix above,
with exact scalar-homogeneity rows and independently calculated additivity
and local rows. Record which unit directions are removed before and after
each block. At 3 the certified classes and unit ranks already predict
saturation; there is no hidden smaller bound to obtain by extra valid
membership rows. For p>=5, the required scalar eigenspace is larger, and
the substantive new question is whether additive/local defect ranks admit
an arithmetic lower bound independent of knowing Sha. No such cross-prime
rank bound has been constructed in this note.

This identifies a concrete source constraint and its p=3 limitation. It
does not settle FIN, ORDER9, Q36 or another coefficient prime.

## 6. Continuation actually carried out after the analysis above

The subsequent producer did construct the affine-line norm in
Schaefer--Stoll Proposition 7.10 over an explicit degree-eight dual field
and supplied exact cube roots for all four actual class images. The
precise review and a further integral deduction are in
`reviewer/INCIDENCE_NORM_REVIEW.md`.

The new deduction is that the incidence norm and reverse incidence norm
compose to multiplication by p on the odd global-unit lattices. Thus
their Smith exponents are complementary zeros and ones, a restriction on
actual integral arithmetic rather than just on the rational permutation
representation. At p=3 the two certified admitted unit classes force
the forward index to be 9 and the reverse map to be an isomorphism.

The index also has a derived relative class-number expression. With A
the nonzero-point field, B its nonzero-covector field, and plus denoting
the scalar-minus-one fixed field, it is

    length coker(u on minus units)
      = (p^2-1)/8 + v_p(h_B/h_A) + v_p(h_A+/h_B+).

This is a number-field class-number calculation, with no elliptic BSD
assumption. At p=3 the plus fields are isomorphic, giving the concrete
new prediction v_3(h_B/h_A)=1. The target class group was not calculated;
its total order is not determined. The retained source class-group
grade remains attached to any numerical consequence using h_A=144.

Finally, the new local calculation repaired the old helper's handling
of a zero-dimensional local Kummer image. Such an image requires the
whole local evaluation vector to vanish. Omitting the row block was an
error. Corrected local-only kernel dimension is four, not seven, and
the local-only unit kernel has dimension two. Consequently this seed
does not demonstrate extra locally admitted directions removed only by
global conditions. The explicit four global classes and their exact
affine norms remain unaffected.
