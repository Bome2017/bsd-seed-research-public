# What lower-degree class groups actually control

2026-10-20. Written elementary deduction in the actual seed's scalar
tower. This is not a new class-group upper bound.

Let A be the seed's degree-24 nonzero-five-torsion point field, with its
actual scalar automorphism sigma taking T to 2T. Put

    F = A^{<sigma>},       [F:Q]=6;
    F2 = A^{<sigma^2>},    [F2:Q]=12.

The sibling relative-source construction supplies actual embeddings.
The statements here use Gal(A/F)=C4 and the coefficient prime five.
They do not require a class-group completeness assumption.

## 1. Exact class transfer identities

For a Galois extension L/K of degree d=2 or 4, ideal extension j and
ideal norm N satisfy

    N j = d,          j N = sum_{g in Gal(L/K)} g

on ideal-class groups. These identities follow directly from the
ramification and residue degrees in prime ideal factorization, so
ramified places do not invalidate them.

On the 5-primary groups multiplication by d is invertible. Hence j is
injective, N is surjective, and

    Cl(L){5} = j Cl(K){5} direct_sum ker N.                 (1)

For the invariant part, jN=d gives

    Cl(L){5}^{Gal(L/K)} = j Cl(K){5}.                       (2)

This proves the relevant prime-to-extension-degree consequence usually
associated with ambiguous-class formulas without invoking an
uncomputed unit index.

Apply this to A/F2. Write

    R5 = ker(N_{A/F2}: Cl(A){5} -> Cl(F2){5}).

The exact result is

    Cl(A){5} = j Cl(F2){5} direct_sum R5,
    R5 = (Cl(A){5})^{sigma^2=-1}.                          (3)

The desired faithful characters chi(sigma)=2 and chi^-1(sigma)=3 modulo
five are both in R5, and all of R5 is their direct sum.

## 2. Lower-field class data leave exactly the desired remainder

The idempotents of Z_5[C4] split Cl(A){5} into four characters. The
degree-six field controls only the trivial component. The degree-twelve
field controls the trivial and quadratic components. The faithful
components are killed by both proper scalar-subfield norms.

In particular even unconditional proofs

    Cl(F){5}=0,       Cl(F2){5}=0

would not imply Cl(A)[5]^chi=0 or bound its dimension. They would only
identify all of Cl(A){5} with the remaining relative group R5.

The complete seed source bound on the already established
valuation-zero domain consequently remains

    dim K <= 3-r_U + dim(R5[5]^chi),                       (4)

or a sharper bound using the portion of R5 that survives the actual
incidence class map and its connecting obstruction. Neither part is
bounded by (1)-(3).

## 3. Ordinary field-norm unit indices cannot supply the missing 5-part

For an ordinary base-field unit u viewed in L, its field norm is u^d.
Therefore

    O_K^* / N_{L/K}(O_L^*)

is killed by d, whenever the displayed quotient is used. The same holds
for the corresponding norm-index subgroup appearing in an ambiguous
class formula: it is a quotient or subgroup of a group killed by d.
Its 5-primary part is zero for d=2 or 4.

Thus computing these ordinary extension-norm unit indices more
accurately cannot recover the missing faithful five-class part. This
statement is **not** about the incidence norm from the point field to
the covector field. That is a different correspondence, and its
unit index can have a nonzero 5-part.

This also does not say relative norm-one units are useless. A method
that constructs new actual units in A can supply incidence-norm rank
`r_U`; the sibling experiment tests that distinct possibility.

## 4. Exact countercontrol to the proposed class inference

For arbitrary r and n let

    M = (Z/5^n)^r,

and let sigma act by a fourth root of unity lifting 2 modulo five.
Then sigma^2=-1, so

    M^{C4}=M^{C2}=0,
    (1+sigma^2)M=0,
    (1+sigma+sigma^2+sigma^3)M=0.

Every proper scalar-subfield invariant and norm is zero, while the
relative five-rank is r and its length is rn. The inverse faithful
character works identically.

One may add these summands to any fixed module accounting for observed
lower-field class data. The lower-field data remain unchanged while
the faithful remainder grows. This is a module countercontrol to the
inference; it is not a claim that every such module is realized by the
seed or by a number field.

The checker verifies both faithful characters through modulus 5^5 and
ranks one through eight. The arbitrary-rank conclusion is the written
calculation, not extrapolation from the finite tests.

## 5. Why a norm relation through these subfields does not repair this

In characteristic zero, on a faithful C4 character the two nontrivial
subgroup norm elements act by

    1+i^2=0,       1+i+i^2+i^3=0.

No linear combination of such operators can give a nonzero scalar
identity on this component. The generalized norm-relation framework
requires an actual group-algebra identity; it does not provide one
merely because a tower exists.

In the full GL2(F5) normal closure, the stabilizers of F and F2 contain
nontrivial scalar subgroups. These scalar groups are central. Any
generalized norm operator through those fields therefore still
annihilates the faithful central-character representation, even when
left and right group-algebra coefficients are allowed.
This is a characteristic-zero representation argument. It does not
identify Cl(A)[5] with invariants in the class group of the full normal
closure, whose relative degree is divisible by five.

This excludes direct norm-relation reconstruction through these two
proper scalar fields. It does not classify all smaller fields in the
normal closure, all generalized norm relations, or all possible class
algorithms. The older full subgroup screen at coefficient seven is
not silently promoted to a coefficient-five enumeration.

## 6. What a changed relative computation would still have to certify

A relative algorithm may search ideals or elements in the faithful
part of A using the lower field as its coefficient field. That is a
different operation from transferring lower-field class bounds.
To yield an upper bound it must certify a generating presentation of
R5, or bound the relevant incidence-kernel component of R5. Actual
principal-ideal relations alone do not prove that their ideal list
generates it.

A relative class-number/regulator formula likewise still contains the
faithful relative arithmetic. No uncomputed relative regulator or
class number is removed by (1)-(3). Neither the geometric character
dimension nor lower-field class certification supplies that missing
arithmetic.

Thus this proposed direct class transfer does not pass admission as a
new complete bound. The remaining class target is the explicitly
identified R5[5]^chi, rather than an unspecified normalization.
