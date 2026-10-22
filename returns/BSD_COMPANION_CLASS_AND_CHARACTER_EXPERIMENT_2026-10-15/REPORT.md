# Companion-class bounds and an actual larger-prime norm experiment

Started October15; recovered and completed October17,2026.
Parent lab commit d61b2af9653be14e1da758ae81f26209bde2a117.

**Results: conditional seed companion bound2 and full-source bound4;
actual p5 complete-unit bound2; conditional p5 full-source bound2.**

These experiments bound complete arithmetic spaces. They do not infer a
bound from a list of detected classes. The class-group completeness
qualification is substantial: the attempted unconditional certifications
did not finish. No seed endpoint or new coefficient prime is settled.

## 1. The seed companion contribution now has a numerical conditional bound

At coefficient3, the existing source-field class presentation is [12,6,2].
Fresh inspection and an independent integer-lattice check show that primes
over S={2,3,2243,4547,5843} generate that entire presented class group. In
particular two prime classes, over2243 and5843, have determinant -20 on
the3-primary coordinates, hence generate that part.

This presentation remains GRH-dependent. Under its completeness hypothesis,
the source S-class group vanishes. Exact field signatures and prime
permutations give ordinary minus unit rank2 and minus S-divisor rank2,
hence full S-unit rank4. The retained index theorem becomes

    s_A,S = 2 + c_B,S^-.

The actual incidence composition is multiplication by3, so its cokernel
is killed by3 and has length at most4. Therefore

    c_B,S^- <= 2,             dim K_A <= 4.

Here c_B,S^- is the companion's minus3-primary S-class LENGTH. No known
Selmer dimension, Sha order, or selected norm-kernel dimension enters this
argument. It supplies an independent conditional upper bound on the term
left blank in the preceding return. Class-supported directions are retained:
when S kills the source class group, they are represented in the enlarged
S-unit space rather than silently removed.

See [proof](seed_class/PROOF.md) and [exact checks](seed_class/source_cache/).

Two actual companion BNF strategies timed out at120seconds each. A separately
sealed attempt to certify the existing source class quotient timed out at
90seconds. No certificate was accepted, including where GP returned exit0
after an alarm. These resource outcomes are not mathematical counterexamples.

## 2. The method was actually carried to coefficient5

We constructed degree24 point fields, actual torsion points, scalar
automorphisms and prime-divisor actions for389a1 and37a1. Both have full
mod5 image by the exact field calculation and a primitive multiplicative
transvection. They have provisional ordinary class groups C3 and C2,
respectively; neither unconditional class certification completed.

The initial whole-source upper bound was3, conditional on those class
computations. We then improved the389 bound with an actual norm calculation.

The entire relevant ordinary unit space has dimension3. We authenticated
13 compact units by exact principal-ideal identities (317 distinct factors,
295 prime ideals). Their projected residue classes have rank3. This proves
spanning at5 without assuming a fundamental-unit basis or GRH.

For just one of those units, at the fully split prime1831, an actual affine
incidence product gives

    250 * 88 * 215 * 1268 * 223 = 693 (mod1831),
    693^366 = 123 != 1 (mod1831).

Thus its norm is not a fifth power. The norm map has rank at least1 on the
COMPLETE three-dimensional unit space, so its kernel has dimension at most2.
A separate checker rebuilt this witness from the field and compact unit
data, without reading the producer's residue/norm matrices.

The exact primitive divisor norm is injective modulo5 on the support in
question. Consequently the full global source, including unknown ideal-class
directions, satisfies

    dim K_389,5 <= 2 + dim Cl(A)[5]^chi.

Under the provisional class-group completeness assertion the last term is
zero, giving dim K_389,5<=2. The UNIT bound does not need GRH; the FULL-SOURCE
bound still does. This is the precise distinction between the new arithmetic
result and an unconditional complete descent.

See [actual bound proof](p5_norm_upper/PROOF.md),
[independent witness](character_review/P5_NORM_ADDENDUM.md), and
[unit authentication](p5_norm_upper/unit_authentication/REPORT.md).

## 3. What extends, and what does not

The exact characterwise S-unit/divisor/class sequence extends to oddp.
The scalar descent uses chi=omega, and the incidence norm targets chi^-1.
The ordinary unit rank is(p+1)/2. A bound retaining all class-supported
directions is

    dim K_chi <= s_U,chi + t_D,chi
                   + dim ker(Cl(A)[p]^chi -> Cl(B)[p]^(chi^-1)).

The final term uses the actual ideal correspondence, not merely a detected
subset of class generators. It has not been evaluated for new seed primes.

The full-minus companion bound extends too, with geometric constant
(p^2-1)/8, which grows withp. Tests at5,7,11 show the relevant GEOMETRIC
character incidence index is1, but actual global unit lattices cannot be
replaced by that geometric lattice. An explicit integral counterlattice
preserves the aggregate index and changes its character distribution.
This blocks that unsupported shortcut; it does not disprove a possible
arithmetic comparison theorem.

The number-field experiment is atp5. The p7/p11 matrices are algebraic
controls, not class-group or unit computations at those primes.

## 4. What the experiment learned about a seed route

The source method can turn class and unit arithmetic into an upper bound
on EVERY surviving direction. The seed companion term was bounded through
source S-class generation instead of a successful companion BNF. Atp5,
one actual non-fifth-power norm improved the complete-unit upper bound,
and the class term stayed visible throughout.

This is a worked bound experiment, but not an all-prime theorem. Its unresolved
inputs are sharply separated:

| Status | Item |
|---|---|
| REMOVED for this control | Need for a certified fundamental-unit basis to obtain the unit upper2: an authenticated unit and the independent ambient rank suffice. |
| CONDITIONAL | Seed companion upper2/source upper4 and389 full-source upper2 rely on complete class presentations. |
| EXCLUDED as an inference | Copying the coefficient3 constant1 into actual character-unit lattices for largerp from rational geometry alone. |
| OPEN | Unconditional class control at the tested fields, and enough arithmetic norm rank plus class-kernel control as coefficient primes grow. |

A next computation would have to sharpen or certify the class-kernel term,
or provide sufficiently many independent norm obstructions on the complete
unit space as p grows. More local signatures on a named set of Selmer
classes would not supply either. No claim is made that the present method
will finish FIN.

FIN, ORDER9, Q36 and seed-prime coverage remain unchanged. Publication and
manifest checks certify file custody, not mathematical truth. The written
deductions have a separate same-team review, not formal or human verification.
