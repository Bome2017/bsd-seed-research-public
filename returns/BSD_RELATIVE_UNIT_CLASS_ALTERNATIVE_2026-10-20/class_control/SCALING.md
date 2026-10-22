# What a relative computation saves, and what still grows with p

2026-10-20. Written counting and transfer deduction under the retained
full GL2(F_p) residual-image and torsion-field source inputs. This is
not an arithmetic upper bound on units, classes, Selmer, or Sha.

## 1. The actual point field and its scalar quotients

Let p be an odd prime with full residual image, V=E[p], and A the field
of one nonzero point. Its embeddings are indexed by V minus {0}, so

    [A:Q]=p^2-1.

The scalar group Z=F_p^* acts internally on A. Choose complex
conjugation c=diag(1,-1), whose eigenvalues follow from oddness of the
elliptic representation. Put

    Aplus=A^{<-1>},      F=A^Z.

The name Aplus denotes scalar-negation invariants. It is NOT a
statement that Aplus is totally real or that A/Aplus is a CM extension.
The signatures below show that it is usually not totally real.

A has p-1 real embeddings, namely the nonzero vectors in the positive
eigenline of c. All remaining embeddings form conjugate pairs. Hence

    signature(A) = (p-1, p(p-1)/2),
    rank O_A^* = (p^2+p-4)/2.                              (1)

Embeddings of Aplus are pairs {v,-v}. Such a pair is fixed by c if v
lies in either eigenline. There are p-1 such pairs altogether. Thus

    [Aplus:Q]=(p^2-1)/2,
    signature(Aplus) = (p-1, (p-1)^2/4),
    rank O_Aplus^* = (p^2+2p-7)/4.                         (2)

Embeddings of F are the p+1 projective lines. Precisely the two
eigenlines are fixed by c, giving

    [F:Q]=p+1,
    signature(F)=(2,(p-1)/2),
    rank O_F^*=(p+1)/2.                                  (3)

For p=5 these give exactly the current seed outputs:

    F: (degree, signature, unit rank) = (6,(2,2),3),
    Aplus: (12,(4,4),7),
    A: (24,(4,10),13).

These are checked bindings to the actual fields already constructed,
not new class-group or unit computations.

## 2. The relative anti-unit rank is quadratic, not linear

For the quadratic extension A/Aplus, the norm image has finite index
in the lower unit group: it contains the squares of all lower units.
Consequently the norm-one unit group has free rank equal to the
rank difference in (1)-(2):

    rank ker(N:O_A^* -> O_Aplus^*) = (p^2-1)/4.            (4)

After tensoring with Z_p this is exactly the minus part for scalar -1,
because division by two is permitted. In particular the anti-unit
rank is NOT p+1 in general. Those numbers agree at p=5 and diverge
already at p=7, where the anti-unit rank is 12 rather than 8.

Thus a quadratic-relative unit engine still has a quadratic-rank
output if it computes the entire relative group. It avoids the plus
unit directions but does not by itself isolate the one descent
character.

## 3. A single faithful character has linear rank

For completeness, this follows by a direct archimedean character
count. Let W be the set of archimedean places of A, identified with
complex-conjugation orbits on V minus {0}. The equivariant Dirichlet
logarithm identifies the unit representation with the permutation
representation on W minus its one-dimensional constant subspace.

A scalar a fixes a place represented by v precisely when av=v or
av=cv. For a not equal to 1 or -1 neither can occur. Scalar -1 fixes
the (p-1)/2 complex places from the negative eigenline. Therefore the
permutation character has values

    #W=(p-1)(p+2)/2     at a=1,
    (p-1)/2            at a=-1,
    0                  at other scalars.

For a nontrivial scalar character chi, its multiplicity in the unit
representation is consequently

    ((p+2)+chi(-1))/2.

The trivial character loses one constant dimension and has
multiplicity (p+1)/2. In particular every odd character, including the
faithful descent character chi(a)=omega(a) and its inverse, has rank

    d_chi=(p+1)/2.                                      (5)

There are (p-1)/2 odd characters. Their total rank recovers (4):

    ((p-1)/2) * ((p+1)/2) = (p^2-1)/4.

Projection to one odd character removes a factor (p-1)/2 in unit-rank
bookkeeping compared with computing the whole anti-unit group. This
is a representation-rank statement, not a guaranteed runtime or
memory improvement. Constructing enough actual units with independent
character projections can bound the unit kernel without computing a
full unit system. Any inference requiring a full lattice or its index
must separately authenticate its p-saturation; rank over Q_p alone
is insufficient.

## 4. The same relative reduction retains the missing class component

Ideal extension and norm for A/Aplus satisfy Nj=2 and jN=1+sigma_-1.
As p is odd, they give the exact ordinary p-primary decomposition

    Cl(A){p} = j Cl(Aplus){p} direct_sum R_p,
    R_p=ker N_{A/Aplus}=(Cl(A){p})^{sigma_-1=-1}.          (6)

All odd scalar characters lie in R_p. For p=5 they are exactly the two
faithful characters. For general p the odd part may also contain
nonfaithful characters: the anti-part and one faithful component must
not be identified. The actual required component is R_p[p]^chi,
or the portion surviving the incidence class map and connecting
obstruction.

More generally, for any nontrivial subgroup H of the scalar group,
put A_H=A^H. Since |H| divides p-1, extension and norm split the
p-primary groups, and

    j Cl(A_H){p}=Cl(A){p}^H.

A faithful chi is nontrivial on every such H, so the H-norm annihilates
its component and the lower-field class group sees none of it. The
same statement holds for lifted lower-field units. Smaller scalar
fields are coefficient fields for a possible relative algorithm;
their class groups and unit groups are not substitutes for the
faithful relative arithmetic.

This is the precise structural limitation of the degree reduction.
An algorithm computing a certified presentation of R_p may still be
useful. A mere lower-field transfer, or a list of relations without
a certificate that it covers all relevant classes, does not supply
the missing upper bound.

## 5. Exact algebraic savings; no unsupported memory estimate

There are three distinct changes:

1. Quadratic-relative representation A/Aplus uses a base of degree
   (p^2-1)/2 and relative degree two. Its elements still have p^2-1
   rational coordinates in a generic basis. The full relative unit
   rank is (p^2-1)/4.
2. Full-scalar representation A/F uses a base of degree p+1 and
   relative degree p-1. Again their product is p^2-1. Merely rewriting
   the field in this tower does not make its faithful arithmetic a
   degree-(p+1) class calculation.
3. Targeting one faithful scalar component reduces the relevant unit
   rank to (p+1)/2. A successful dedicated algorithm would have to
   produce and certify this actual component, together with its
   ordinary relative class contribution.

These identities quantify structural degrees and output ranks.
They do not yield a RAM formula for BNF, factor bases, integral bases,
or relation collection. The observed seed stack overflows are
implementation/resource outcomes; no lower bound on all possible
algorithms is inferred from them.

## 6. The complete arithmetic requirement across coefficient primes

Retain the independently written primitive valuation result on

    D={good p>=5 : p not in {19,59,487}}.

There the valuation allowance is zero. If r_U(p) is an authenticated
rank of the actual incidence norm on the ordinary chi-unit space,
and k_C(p) bounds the ordinary-class contribution surviving its
incidence map and common unit-repair obstruction, then

    dim K_chi <= (p+1)/2 - r_U(p) + k_C(p).               (7)

A complete bound of two from (7) is supplied by

    r_U(p)-k_C(p) >= (p-3)/2.                            (8)

For a target b, replace the right side by (p+1)/2-b.
Equation (8) is a requirement for this sufficient certificate, not
an asserted arithmetic inequality or a necessary condition for
Selmer rank two by every possible method. Additional genuine local
conditions can improve the bound, but their ranks must be measured
jointly on the admitted space, including class lifts.

The retained geometric character-index value one cannot replace
the actual unit index: the historical lattice countercontrol already
shows the distinction. Likewise knowing that k_C is finite, or
bounding only the classes already found, is insufficient.

The scale is explicit:

| p | degree A | degree Aplus | full anti-unit rank | one odd-character rank | required r_U-k_C for bound 2 |
|---:|---:|---:|---:|---:|---:|
|5|24|12|6|3|1|
|7|48|24|12|4|2|
|11|120|60|30|6|4|
|17|288|144|72|9|7|
|31|960|480|240|16|14|
|53|2808|1404|702|27|25|
|83|6888|3444|1722|42|40|

This does identify the computational target more sharply: construct
linear-rank faithful arithmetic directly rather than generate the
whole quadratic-rank anti-space. It does not establish that such a
construction has the required norm rank or that its companion class
contribution stays small. No FIN, ORDER9, or Q36 conclusion is added.

## Inputs and scope

Read for this deduction: the actual current relative_source/FIELDS.json
and REPORT.md; the prior seed_five/REPORT.md;
BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/uniform_valuation/PROOF.md;
and BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15/
general_character/PROOF.md. Equivariant Dirichlet and the retained
field/source interpretation are theorem inputs. The signature count,
character multiplicities, transfer decomposition, and threshold are
derived above. No heavy computation or new class certificate was run.
