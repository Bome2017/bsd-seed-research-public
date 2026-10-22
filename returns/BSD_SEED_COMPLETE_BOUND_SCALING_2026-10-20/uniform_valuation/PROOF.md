# The seed's primitive valuation contribution across coefficient primes

2026-10-20. Written deduction under the retained torsion-field source,
full residual image, conductor and local representation inputs. Same-team
reviews and finite orbit checks are included separately. This is not a
formal proof, a novelty claim, or a bound on units or ideal classes.

## Statement and its use

Let E be the original curve

    y^2 = x^3 - 22735*x^2 + 106272484*x.

For a good coefficient prime p>=5, let A and B be the nonzero point and
covector fields of E[p]. Use the scalar character chi(a)=a, its integral
Teichmuller lift, and the inverse character on B. Set

    S = {2,3,p,2243,4547,5843}.

Let D_A,S and D_B,S be the primitive free prime-divisor lattices over S,
tensored with Z_p. The incidence norm u is the actual correspondence
lambda(v)=1. Define t_D,chi as the Z_p-length of the cokernel of

    u : D_A,S^chi -> D_B,S^(chi^-1).

The retained reverse-incidence identity vu=uv=p on these components makes
this cokernel killed by p. Its length also equals the dimension of the
kernel after reduction modulo p.

Under the stated inputs,

    t_D,chi = 1 if p is in {19,59,487}, and 0 otherwise.       (1)

In particular it is identically zero on

    D = {good p>=5 : p not in {19,59,487}}.

This is uniform in coefficient p. It eliminates the valuation term only.
On D, any admitted norm-kernel class is an ordinary virtual unit modulo
pth powers; it need not be an ordinary unit. If r_U is the authenticated
rank of incidence norm on the full ordinary chi-unit space, and k_C is
the dimension of the class-map kernel which survives its connecting/common
unit-repair obstruction, the complete containing-source bound remains

    dim K_chi <= (p+1)/2 - r_U + k_C.                       (2)

One may always replace k_C by dim Cl(A)[p]^chi to obtain a weaker bound.
Neither r_U nor k_C is bounded uniformly by (1). For a bound of two, their
combination would have to satisfy r_U-k_C >= (p-3)/2. This is the arithmetic
scaling requirement, not an assertion that it holds. Additional actual
local conditions can strengthen (2), but require joint admission rather
than unrelated corrections on each row.

## 1. Primitive divisor coefficients

Fix q in S and a prime of the full splitting field above it. Let I and D_q
be inertia and decomposition. A prime of A corresponds to a D_q-orbit P
on nonzero vectors; a prime of B to a D_q-orbit Q on nonzero covectors.
Their ramification indices e_P,e_Q are the sizes of the respective
I-orbits. For a representative lambda of Q the actual integer coefficient is

    u_D(Q,P) = (e_Q/e_P) * #{v in P : lambda(v)=1}.          (3)

Indeed the splitting-field valuation of the element evaluated at v in P
is |I|/e_P times its normalized P-valuation. Summing over the incidence
fiber and dividing by |I|/e_Q gives (3). It is integral because it is a
map of actual divisor lattices. Replacing it by the unweighted incidence
count gives the wrong mod-p map at ramified primes.

An orbit with a nontrivial scalar stabilizer contributes zero to a faithful
scalar character: an invariant coefficient would satisfy (chi(a)-1)x=0
for a!=1, and chi(a)-1 is a p-adic unit. We use this criterion at the
additive places and the coefficient place.

## 2. Multiplicative places

Suppose q!=p is multiplicative, p does not divide v_q(Delta_min), and
let epsilon=1 for split and -1 for nonsplit reduction. Tate uniformization
gives full unipotent inertia

    (x,y) -> (x+t*y,y), t in F_p,

and Frobenius, modulo that inertia, epsilon*diag(q,1).

There are two inertia-orbit families on vectors: singleton formal points
(x,0), x!=0, and size-p orbits with fixed y!=0. Covectors have singleton
orbits (0,b), b!=0, and size-p orbits with fixed a!=0. In the faithful
scalar components, (3) gives the two channels

    formal vector -> nonfixed covector: p times inversion;
    nonformal vector -> fixed covector: inversion.

For the first, there is one incidence point and e_Q/e_P=p. For the second,
there are p incidence points and e_Q/e_P=1/p. The cross term sums a
nontrivial character and is zero. Inversion matches chi with chi^-1.
Thus the two channel indices are exactly one and zero.

Frobenius multiplies the formal source label by epsilon*q and the
nonformal label by epsilon. The formal faithful channel is retained
precisely if epsilon*q=1 modulo p. The other channel is retained precisely
if epsilon=1. Its norm is already a unit. Passing to decomposition orbits
introduces no p-index: these extra label actions have orders dividing p-1.
Consequently

    t_D,chi(q) = 1_{p divides q-epsilon}.                   (4)

The seed's retained multiplicative data are

| q | epsilon | v_q(Delta_min) | q-epsilon |
|---|---:|---:|---:|
|3|-1|2|4|
|2243|1|1|2242=2*19*59|
|5843|-1|2|5844=12*487|

For good p>=5 none of these discriminant valuations is divisible by p.
Their total contribution is exactly the right side of (1).

## 3. Additive places: retain the wild place correctly

At 2 the actual conductor exponent is 3. The Artin conductor is the sum
of the codimension of inertia invariants (at most two) and the Swan
conductor. Therefore wild inertia acts nontrivially on every prime-to-2
Tate module. For p>=5, a pro-2 group has finite image in GL_2(Z_p), because
the congruence kernel is pro-p; reduction is injective on that image.
Its nontrivial finite 2-group has an involution. Weil pairing gives
inertial determinant one. The only nonidentity involution in SL_2(F_p)
for odd p is -Id. Thus -Id belongs to inertia, eliminating every faithful
scalar divisor component above 2.

This argument uses conductor exponent three, not the assertion that I_1^*
at residue characteristic two is potentially multiplicative. That tempting
assertion is false here. The exact model has v_2(c4)=4 and v_2(Delta)=8,
so v_2(j)=4; it is potentially good. Both the correction and the repaired
argument are recorded in the independent reviews.

At 4547 the retained type III gives tame potentially good inertia of
order four (coefficient p is good, so p!=4547). Its square is -Id. The
same scalar-stabilizer argument eliminates this divisor component. This
step uses the type III theorem, not additive reduction alone.

## 4. The coefficient place: ordinary and supersingular

The seed is nonanomalous at every good p>=5. Its rational two-torsion
makes #E(F_p) even. For p>=7, Hasse's interval has no positive even
multiple of p: its upper endpoint is below 2p, and p itself is odd.
At p=5 the retained count is 8, also recovered in the new local run.

In the good ordinary case the representation is upper triangular with
quotient the unramified character whose Frobenius value is alpha, where
alpha!=1 modulo p. Inertia has full first diagonal image F_p^* and second
diagonal entry one. Multiply a Frobenius lift by a suitable inertia
element to make both diagonal entries alpha. The resulting matrix is
alpha*Id+N with N^2=0. Raising it to p gives alpha*Id in characteristic p.
Thus the decomposition group contains the nontrivial scalar alpha*Id.
Every decomposition orbit on vectors and covectors has nontrivial scalar
stabilizer, so both faithful divisor components vanish. This proof permits
the split and nonsplit ordinary extensions; no diagonal splitting is assumed.

In the good supersingular case over Q_p, the level-two fundamental-character
inertia is the nonsplit Cartan F_(p^2)^*. It acts transitively on nonzero
vectors, and on nonzero covectors. The divisor permutation module is
scalar-trivial, so again its faithful component vanishes.

Sections 2-4 exhaust S and prove (1). Good places outside S are not
included: the theorem does not claim their divisor modules vanish.

## 5. Independent numerical binding and remaining arithmetic

The actual degree-24 seed point field at p=5 has signature (4,10) and
scalar action T->2T. Exact maximal-order prime decomposition gives zero
faithful divisor dimensions except for one line above 2243. Formula (3)
maps that line by a unit. The explicit field computation agrees with (1)
and did not use a known Sha5 vanishing result.

The separate finite-group checker builds source and covector orbits and
counts incidences before comparing with (4). Its finite tests check the
implementation and normalization; the argument above, not extrapolation
from those tests, provides the uniform statement.

The actual seed's unit/class computation at p=5 returned no table before
its explicit stack overflows. Thus (2) at p=5 is still (3-r_U)+k_C with
both arithmetic quantities unmeasured. In particular, a zero valuation
term supplies no upper bound on unseen ideal classes.

## Inputs and sources

- Retained seed conductor, local types, multiplicative signs and full
  residual image: canonical MASTER_BSD_DAG.md, local-data table and image
  inputs; new exact model/point-field checks are recorded separately.
- Schaefer--Stoll, How to do a p-descent on an elliptic curve, especially
  section 7 (source and incidence maps), primary author copy:
  https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf.
- Serre, Proprietes galoisiennes des points d'ordre fini des courbes
  elliptiques (1972), section 1.11: retained ordinary/supersingular local
  representation inputs. Primary author archive checked in this run:
  https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf.
- Tate uniformization, Artin/Swan conductor formula, Weil pairing, and
  the tame type-III inertia description are imported local arithmetic
  facts. This report does not claim a new independent proof of them.
- Retained general_character/PROOF.md and LOCAL_DIVISOR_PROOF.md in
  BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15 establish the
  full unit/class/divisor bound and primitive normalization. This return
  specializes that normalization uniformly to the actual seed.
