# Testing complete bounds at larger primes and on the actual seed

2026-10-20. **SAME-CURVE UNIT BOUND STAYS SMALL AT FIVE; SEED VALUATION
CONTRIBUTION CONTROLLED UNIFORMLY; COMPLETE CLASS CONTRIBUTION STILL OPEN.**

The requested experiment was executed on the same successful curve at a
larger coefficient prime and on the original seed. It did not establish a
new complete bound on the seed or a cofinite FIN bound. It did produce a
written uniform calculation of one contribution for the actual seed,
under retained local arithmetic inputs.

## Results, keeping the class term present

| Test | Complete ordinary unit part | Ordinary class contribution | Valuation kernel | Complete source conclusion |
|---|---|---|---|---|
| 1664n1 at 3, previous return | kernel 1 | certified contribution 1 | 0 | certified upper 2, retained |
| Same 1664n1 at 5, new arithmetic | full unit dimension 3; norm rank at least 1; kernel at most 2 | provisional C3; certification timed out | 0 | at most 2 + dim Cl(A)[5]^chi; class term not removed |
| Original seed at 3, recovered record | kernel 2 | two known independent surviving class images; full class presentation remains conditional | retained complete S presentation | existing conditional complete bound 4 is attained; no new bound |
| Original seed at 5, new arithmetic | full dimension 3; norm rank not measured | no class table obtained | 0 | (3-r_U)+k_C, both arithmetic terms unmeasured |
| Original seed, every good p>=5 outside {19,59,487} | dimension (p+1)/2; actual norm rank still needed | actual surviving ordinary class kernel still needed | **0 by written proof** | (p+1)/2-r_U+k_C; no uniform numerical upper bound |

The previous p3 control's unit kernel is one and class contribution one;
the new p5 test must not be described as merely repeating that unit rank.
The new calculation shows that the *unit upper bound* stays at most two,
not that the full source bound stays two.

## 1. What was computed on the actual seed

The governing model is

    y^2 = x^3 - 22735*x^2 + 106272484*x.

The new coefficient-five point field has degree24 and signature (4,10).
The construction verifies its actual torsion point, the field equation,
and the order-four scalar automorphism T->2T. Exact maximal-order prime
factorization and scalar action were computed above every prime in
S={2,3,5,2243,4547,5843}.

Only 2243 has a nonzero faithful scalar divisor component. Its primitive
incidence map is a unit modulo five once the ramification ratio is
included. Therefore all allowed valuation contributions are controlled,
not just the valuations of a few supplied elements. See
[the actual field and divisor proof](seed_five/DIVISOR_PROOF.md).

The class/unit computation did not return a table. It exhausted the
512 MB GP stack and, in one recorded adaptation, the 2 GB stack. The
second failure occurred after18.41 seconds, before any provisional class
or unit output. The field had already been reduced by polredbest; this
was not an unreduced raw polynomial passed without preprocessing. No
class-zero or small-class claim follows from these failures.

This is an actual arithmetic stop in the chosen implementation, not a
mathematical impossibility claim. No known seed Sha5 certificate was used
to infer unit rank, class size, or completeness.

## 2. What transfers from that calculation across coefficient primes

The seed-five valuation profile prompted a general calculation in the
same source. The [written proof](uniform_valuation/PROOF.md) shows

    t_D,chi = 1_{p in {19,59,487}}

for good coefficient primes p>=5, under the retained local representation
and source inputs. In particular it is zero on the cofinite domain D.

At a multiplicative bad place q, the two primitive incidence channels
have factors p and1. The p-channel survives Frobenius exactly when
p divides q-epsilon, with epsilon the split/nonsplit sign. For this seed,
those factors are 4,2242 and5844, yielding exactly19,59,487. At the
coefficient place, nonanomalous ordinary decomposition contains a
nonidentity scalar; supersingular inertia is transitive. The additive
places have an inertial -Id. These facts eliminate the remaining
faithful divisor components.

The proof was corrected during review: type I1* at residue2 does not imply
potentially multiplicative reduction. The actual seed has v2(j)=4. The
valid argument uses conductor exponent3, positive Swan conductor, and a
nontrivial wild2-group whose involution acts as -Id. This correction is
preserved in [the local arithmetic review](review/UNIFORM_LOCAL_ARITHMETIC_REVIEW.md).

This removes one entire term uniformly for the actual seed. It does not
remove ordinary class-supported virtual units or turn the desired unit
rank into a geometric rank. Those two distinctions are explicit in (2)
of the proof. No claim of literature novelty is made.

## 3. The same-curve scaling test

We kept1664n1 fixed and changed the coefficient from3 to5. All13 compact
candidate units were authenticated by exact principal-ideal identities,
using332 factors and291 prime ideals. Their residue images span the
entire three-dimensional faithful unit space. Thus this is a bound on
all units, despite the BNF unit list not being certified as fundamental.

The actual incidence-norm residues have rank at least one. Hence the
full unit kernel is at most two. A separate replay reconstructs the
multiplicative values before taking residue logarithms and obtains the
same ranks. This is not a detector restricted to an incomplete span.

The provisional class table is C3. Its unconditional class-quotient
certification did not finish within the recorded110-second alarm, so we
retain the complete bound

    dim K_chi <= 2 + dim Cl(A)[5]^chi.

Replacing the class term by zero would require either that missing
certificate or another independent arithmetic bound. A GRH-dependent
class table is not promoted to a complete unconditional source theorem.
See [the same-curve proof](same_curve_scaling/PROOF.md).

## 4. Why coefficient three on the seed was not rerun

The existing four literal norm-cube representatives already have rank
four, including two independent ordinary class images. The old
conditional complete upper four is attained. Recalculating their
connecting map cannot reduce this source to two. The old class
certification also already failed with an enormous generation bound;
there was no changed certification method to justify repeating it.

The [seed-three recovery](seed_three/REPORT.md) preserves the existing
grade and checks the saved matrices. It is not a new number-field
computation or a new proof of the seed's known primary excess.

## 5. What this says about FIN

On the uniform valuation-zero domain, the complete source target is

    (p+1)/2 - r_U(p) + k_C(p).

Here r_U is an actual arithmetic rank on the full ordinary unit space,
and k_C includes the full surviving ordinary class contribution after
the same norm/local repair is imposed. A sufficient complete upper two
would require r_U-k_C >= (p-3)/2. The experiment has not established that
inequality on the seed even at5, much less across primes.

The next arithmetic operation must therefore obtain complete unit/class
information or a rigorous kernel bound without relying on an uncertified
BNF table. More local divisor calculations are no longer needed on D.
Increasing a detector's rank on known classes does not substitute for
class completeness. The existing files permit a changed class/unit
algorithm to start from an authenticated seed field rather than repeat
its construction; no such new successful algorithm is claimed here.

**FIN, ORDER9, Q36 and original seed-prime coverage are unchanged.** The
new uniform statement concerns the valuation contribution only. The
complete-bound question remains unresolved, with its uncomputed terms
kept visible rather than estimated from the controls.

## Verification and grade

- Separate exact field, scalar, prime-ideal and unit authentication replay.
- Separate direct multiplicative residue extraction for the same-curve
  unit bound, rather than trusting the producer's rank output.
- Portable seed field/divisor replay with byte-identical arithmetic files.
-79 explicit local group models and158 faithful-character checks,
  including the exceptional p=487 case;96 ramification negative controls.
- Same-team written reviews of the uniform deduction and arithmetic scope.

These are computation, written deduction and model review under named
retained inputs. They are not human peer review or proof-assistant
verification. Failed class calculations and their resource receipts are
included. Hashes bind the artifacts; they do not certify the mathematics.
