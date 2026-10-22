# Unit admission: exact signature and representation screen

2026-10-13. Written deduction, under the retained covering-to-cohomology and
four-class independence inputs. This is not a uniform Selmer bound or a new
determination of an endpoint. The point-unit witness mentioned in Section 2
has passed the separate portable factorization checker recorded in
`../checks/verify_new_units.out` (`INDEPENDENT_UNIT_1_PASS` and
`NEW_UNITS_PORTABLE_PASS`, empty stderr). I inspected its source binding and
literal cube-correction checks; I did not rerun that separate arithmetic job.

## 1. The actual seed norm-one unit space has dimension exactly two

Let

    K = Q[w]/(w^8 - 1188376638 w^4 - 7030398068360 w^2
               - 117686586145348587),
    K+ = Q(w^2),       tau(w) = -w.

Retain the earlier exact field/3-torsion identification and irreducibility
certificate. Independently, the standard-library checker performs exact Sturm
counts on this octic and on its quartic in w^2. Both have exactly two real
roots. Thus the signatures are (2,3) and (2,1), respectively. This calculation
does not use the cached class group or its completeness.

Write E_K=O_K^*, and N=ker(Norm(K/K+):E_K -> E_K+). Dirichlet's theorem gives
rank E_K=4 and rank E_K+=2. Norm has full rank: the norm of a unit already in
K+ is its square. Hence rank N=2. The field K has real embeddings, so its
roots of unity are just +/-1; in particular it has no 3-torsion roots of
unity. It follows that

    dim_F3 N/N^3 = 2.

The natural map N/N^3 -> K^*/K^*3 is injective. Indeed a cube root in K of a
unit is a unit, and if u^3 is norm one, Norm(u)^3=1 in K+. The absence of
nontrivial cube roots of unity forces Norm(u)=1.

Moreover its image is exactly the minus eigenspace of E_K/E_K^3 under tau.
One inclusion is literal norm one. Conversely, for any anti-invariant unit
class [a], the unit a/tau(a) has norm one and represents 2[a]. Multiplication
by 2 is invertible modulo 3. Therefore no extra finite norm index is lost.

This is an exact ambient upper bound, not a GRH class-number conclusion.

## 2. The two witnessed units exhaust this actual source

Let a1,a2,beta1,beta2 denote the specific reconstructed descent images of
P1,P2 and the two retained cubic Selmer lifts. The Cardano inversion choices
are those in the producer's `actual_representatives.gp`. Their independence
in K^*/K^*3 is the retained exact four-column residue certificate.

The preceding return supplies a witnessed global unit epsilon representing
beta1/beta2. This continuation constructs a witnessed global unit u1
representing a1. In each case applying u -> u/tau(u) gives an actual
norm-one unit representing twice the same class. Naturality of the Weil
pairing makes every original descent image anti-invariant as a Kummer class.

With those two unit witnesses accepted, their classes are independent:
a relation between a1 and beta1/beta2 would contradict the four-column
independence. They therefore form a basis of the two-dimensional N/N^3.
Every norm-one unit class is then the image of an actual Selmer class,
because both basis elements have that property and the Selmer group and
its descent image are F3-vector spaces.

This proves that global additivity and all local Kummer conditions do not
cut down this *particular* two-dimensional unit space at all. This conclusion
comes from two authenticated basis classes and the ambient upper bound; it
is not inferred from passing finitely many residue tests.

There is a second consequence. Let A=span(a1,a2,beta1,beta2) and W=span(a1,a2).
Every unit class in A is anti-invariant, hence belongs to N/N^3. Thus

    A intersect (E_K/E_K^3) = span(a1,beta1/beta2),
    W intersect (E_K/E_K^3) = span(a1).

The second equality follows from four-column independence, without a
nonprincipality assertion from the class-group cache. Since the preceding
exact principal-ideal calculations show that all four source elements have
valuations divisible by 3 everywhere, the two exact filtration sequences
now force

    (valuation quotient, unit quotient, class quotient) dimensions = (0,1,1).

This removes the BNF-completeness qualification from this particular
four-class filtration: use signatures and two literal unit witnesses instead
of trusting the class-group size. It does not certify the
entire class group or exclude Selmer classes outside this four-dimensional A.

## 3. What scalar symmetry gives for larger coefficient primes

For comparison, suppose E[p] has full GL2(Fp) image, p odd. Put Kp=Q(T) for
a nonzero p-torsion point, and Kp+=Q({T,-T}). Embeddings correspond to the
p^2-1 nonzero vectors. Complex conjugation has eigenvalues +1,-1. It fixes
p-1 vectors, and has p(p-1)/2 two-element orbits. Consequently

    signature Kp  = (p-1, p(p-1)/2),
    signature Kp+ = (p-1, (p-1)^2/4).

The second formula counts unordered pairs {v,-v} fixed by conjugation:
they come from both eigenlines, giving p-1 real embeddings. Thus

    rank norm-one units = (p^2-1)/4.

Kp has real embeddings, so there are no p-torsion roots of unity. As above,
this is also the dimension of the corresponding minus unit space modulo p.

The scalar group C=Fp^* acts on Kp by T -> aT. On archimedean places its
permutation character has values

    identity: (p^2+p-2)/2;     a=-1: (p-1)/2;     other a: 0.

Subtract the trivial character for the product-formula hyperplane. For the
odd Teichmuller character omega (or its inverse, depending on the action
convention), the multiplicity is

    ((p^2+p-2)/2 - (p-1)/2)/(p-1) = (p+1)/2.

Dirichlet's equivariant logarithmic description gives this characteristic-zero
unit character. Here reduction is legitimate for this *scalar component*:
|C|=p-1 is invertible in Zp, its Teichmuller idempotents are integral, and
there is no p-torsion in the unit group. The omega component is free of rank
(p+1)/2 and its reduction has that same dimension. This claim does not
require an integral comparison with a particular archimedean basis.

Thus the full scalar homogeneity required of descent images improves the
quadratic norm-one dimension to a linear dimension, but does not give a
constant bound. The remaining affine-line norm condition is real arithmetic.

## 4. Global additivity is an additional arithmetic map

Schaefer--Stoll's long version, Corollary 7.9 and Proposition 7.10, identifies
the cohomology image by scalar homogeneity and the kernel of a norm map
between the torsion-point and affine-line etale algebras. It is not enough
to impose anti-invariance. Its Lemma 7.7 proves the underlying function-space
criterion: homogeneous Fp-valued functions whose sums on every affine line
missing zero vanish are linear.

For a deliberately simplified comparison, the checker imposes these line
relations on Fp-valued functions on Fp^2\{0}, also invariant under
c(x,y)=(x,-y). The scalar-homogeneous space has dimension (p+1)/2; its full
affine-line kernel has dimension 1 after c-invariance. This agrees with the
lemma: the remaining linear function is a multiple of x. The checker verifies
this exactly at p=3,5,7,11,13,17,19,23,31. On the transpose map's
inverse-scalar-character component the formal residual kernel instead has
dimension (p-1)/2; the two formal kernel dimensions sum to (p+1)/2, as
required by the composition-by-p identity. Treating both scalar characters
as the same when p>3 would give a false comparison.

**That one-dimensional model is not an upper bound for arithmetic units.**
The actual seed's two witnessed admitted unit classes contradict any
such replacement. Characteristic-zero logarithmic unit modules and formal
archimedean permutation modules do not come with a p-integral, norm-compatible
identification. The arithmetic norm map is tested modulo *p-th powers in the
target number field*, not by reducing real logarithm coordinates modulo p.
Its lattice content is not supplied by the real character calculation.

The modular coefficient representation also carries the cyclotomic action on
mu_p. Omitting that action does not identify an archimedean function lattice
with the cohomological source. The formal comparison deliberately claims no
such identification; it is a countercontrol against making one implicitly.

For the full G=GL2(Fp), p divides |G|. Invariants/Hom_G and integral reduction
are not exact in general, and characteristic-zero multiplicities do not
automatically compute residual socle multiplicities. In particular the
two-dimensional natural residual representation must not simply be treated
as a two-dimensional characteristic-zero representation of the same finite
group. The scalar subgroup argument above avoids this issue precisely because
its order is prime to p; it does not resolve the full arithmetic norm map.

## 5. Integral incidence norms give a sharper index statement

Let A be the etale algebra of nonzero torsion vectors and B the etale
algebra of affine lines missing zero. Use the actual incidence norm

    u(alpha)(line) = product_{P in line} alpha(P),

and its transpose

    v(beta)(P) = product_{lines containing P} beta(line).

For literal anti-invariant functions alpha(-P)=alpha(P)^(-1), counting
incidences gives

    vu(alpha)(P) = alpha(P)^p * product_{Q outside <P>} alpha(Q)
                = alpha(P)^p.

The last product cancels in pairs Q,-Q. The same argument gives uv(beta)=beta^p.
These are identities of actual norm maps, so they hold on global units and
their p-adic completions. They do not discard ideal-class or local conditions.

For internal scalar pullbacks sigma_a(alpha)(P)=alpha(aP), the line norm
interchanges the omega and omega^(-1) components. Both have rank
r=(p+1)/2, and both are torsion-free at p. On their full integral lattices,

    v u = p I,             u v = p I.

Smith exponents of u and v over Zp are therefore either 0 or 1. If s is the
number of 1-exponents for u, then

    dim_Fp ker(u mod p) = v_p(det u) = s,  0 <= s <= r,
    dim_Fp ker(v mod p) = r-s.

Here determinants mean determinants between primitive lattice bases. The
formula is not valid with a silently nonsaturated collection of target units.

For the actual seed at p=3, Section 2 proves that every class of the
two-dimensional source norm-one unit space is cohomologically admitted.
Schaefer--Stoll's necessary norm relation then says u of each source unit is
a cube in the target field. A cube root of a unit is a unit, and its norm to
the target plus field is 1 (there are no cube roots of unity there). Thus
u sends the full source lattice into 3 times the full target lattice.
Both Smith exponents are 1:

    Smith(u) = (3,3),       v is a Z3-lattice isomorphism.

This is an exact derived index statement using the two passed unit witnesses.
It needs no target fundamental-unit basis to be computed. It is not a
numerical claim about a chosen target generator list.

The incidence identities alone cannot force s<=1 at larger p: for every
0<=s<=r, the abstract pair

    u = diag(p repeated s times, 1 repeated r-s times),
    v = diag(1 repeated s times, p repeated r-s times)

satisfies both integral identities. These examples are lattice controls,
not claimed number-field realizations. The source arithmetic must determine
s; the exact identities restrict its possible exponents but not their count.

## 6. Collision check against the September 29 construction

The original `METHOD.md`, `RETURN.md`, and `work/selmer.gp` already do the
following: build an S-unit/class source, impose local Kummer conditions,
screen relative norms, test torsion additivity at split primes, construct
cubics, and replace alpha by alpha/tau(alpha) for norm-one normalization.
They explicitly warn that omitting norm/additivity admits false classes.
Neither norm-one normalization nor the idea of adding source relations is new.

The present additional calculation is narrower: it uses exact signatures
and two independently witnessed unit classes to determine the **entire
genuine norm-one unit component** and its image modulo the rational-point
plane, without class-group completeness. It tests whether further admission
conditions can remove that component; at the actual seed's coefficient 3
they cannot, because two admitted classes already span it. The experiment
does not claim the same outcome at p>=5.

The open comparison at larger p is an integral bound on the kernel/content
of the actual affine-line norm map on the scalar unit component, together
with its interaction with the ideal-class source. The rank (p+1)/2 identifies
its ambient size; it supplies no bound on its surviving arithmetic kernel.

## Sources and checks

- Primary p-descent source: E.F. Schaefer and M. Stoll, *How to do a p-descent
  on an elliptic curve*, long version, §§7, Lemmas 7.6--7.7, Cor. 7.9, Prop. 7.10:
  https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf
- Equivariant Dirichlet input: B. Poonen, *The p-adic closure of a subgroup
  of rational points on a commutative algebraic group*, Lemma 5.1 and its proof:
  https://math.mit.edu/~poonen/papers/leopoldt.pdf
- Retained exact source: BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29,
  METHOD.md, RETURN.md, work/selmer.gp, and the covering-certificate replay.
- Fresh exact checks: `check_representation_screen.py`, output
  `REPRESENTATION_CHECK.json`. Only standard-library Python; runtime below one
  second. The first development run had a local variable-name error before
  producing output; it was corrected. No BNF initialization or coefficient
  evaluation was performed.

FIN, ORDER9, Q36 and coefficient-prime coverage are unchanged.
