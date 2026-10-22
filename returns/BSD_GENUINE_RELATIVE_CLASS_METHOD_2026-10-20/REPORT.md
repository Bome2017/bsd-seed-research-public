# Actual seed: relative-class reduction tested

Date: 2026-10-20. Verdict: **NO_NEW_COMPLETE_SEED_BOUND_FROM_TESTED_RELATIVE_FAMILY**.

I implemented and tested a relative-class method on the original seed, not
another memory setting or control curve. It produced exact arithmetic
relations, but after accounting for every residual ideal it gave **zero new
relations on the original class generators and zero new unit directions**.
The bounded experiment therefore does not establish the small complete
bound needed for FIN. It also does not prove that relative-class methods
cannot work.

## What was actually computed

Let A be the seed's degree-24 nonzero-five-torsion point field, sigma the
scalar-2 automorphism, tau=sigma^2, and K=A^tau of degree 12. The two
faithful scalar characters have eigenvalues 2 and 3 over F_5. Their entire
class contribution lies in the relative norm kernel for A/K. Bounding
Cl(K) alone would miss it.

The implemented reduction keeps the exact ideal identity

    I = (alpha) j(a) J.

Here j(a) is extended from K, and J is the remaining primitive ideal. A
faithful character kills j(a) whether or not a is principal. Every such
discarded ideal was checked for tau invariance and even valuations at
the four relatively ramified finite primes. The residual J was retained.
The procedure uses exact maximal-order ideal arithmetic and relative
content stripping; it does not invoke bnfinit or rnfisnorm. It is a bounded
implementation of this relative reduction operation, not a full execution
of Cohen's relative class/unit algorithm with all its stopping tests.

Eight actual scalar prime orbits, powers and mixed products produced
196 exact identities. The first collision check found 17 residual
collisions, but their faithful relation ranks were zero. I then tested
the stronger cancellation mechanism: ideal gcds refined all scalar
residual support into 743 pairwise-coprime ideal atoms.

| Complete support accounting, per faithful character | Value |
| --- | ---: |
| Original generator columns | 8 |
| Additional residual-support columns | 177 |
| Relation rows | 196 |
| Rank of all rows | 156 |
| Rank after retaining only additional columns | 156 |
| Relations supported only on original columns | **0** |

The last line is rank-nullity: 156-156=0. An independent implementation
also constructs an explicit matrix T with R_original=R_private*T over
F_5. Therefore every combination cancelling the new support cancels
the old columns too. All 743 atom norms are non-fifth-powers, so their
disjoint divisor supports remain independent modulo five. The calculation
does not miss additional closures because of fifth-power atoms.

The expanded formal quotient has dimension 185-156=29. **That is not the
dimension of Cl(A), the surviving class contribution, or Sha.** The
selected columns have not been proved to generate those groups.

## The unit contribution was checked as well

The exact anti-divisor matrix, including scalar translates, has 392 rows,
rank 312, and an 80-dimensional rational kernel. Every kernel-basis
multiplier was evaluated in A, with its principal ideal and relative norm
checked. The results were 78 copies of +1 and two copies of -1.

This also excludes a hidden unit from saturating this particular kernel:
an integral kernel vector has a nonzero integer multiple in the tested
basis span, so its multiplier is a root of unity. A has real embeddings,
so its only roots of unity are ±1; both are fifth powers. The family
therefore supplies no new faithful unit direction. This statement is
exhaustive for the generated family, not for the field's unit group.

## Completeness was not replaced by a selected-generator calculation

The actual maximal-order inventory contains 35,749 prime ideals of norm
at most 419775, giving 8,918 columns per faithful character. This cutoff
comes from the retained PARI GRH checker. Counting the ideals exactly does
not remove that hypothesis.

The relation batch was also compared to this larger inventory. Of its
177 additional support orbits, 21 are supported entirely inside the
cutoff and 156 have support outside it. The outside-column submatrix has
rank 156 in both characters. Thus these rows only eliminate the 156
added symbols: the resulting GRH-conditional presentation bound remains
8918+156-156=8918. It is nowhere near the required small bound.

I tested a separate unconditional generating criterion, Belabas–Diaz y
Diaz–Friedman Corollary 5.2, at T=419776 using the complete ideal-norm
inventory. It fails: rigorous rational bounds give left side <56.182 and
right side >352. This is failure of a sufficient test, not proof that
the prime list does not generate. Generation modulo five remains
uncertified without GRH here.

## What would suffice, and what the across-prime test measured

For this upper-bound objective, a full class number and complete unit
basis are stronger than necessary. The written presentation argument gives

    dim K_chi <= (p+1)/2 - r_U + m - r_C + q.

Here r_U is a verified unit norm/local rank; m counts selected faithful
ideal columns; r_C is the rank of authenticated relations; and q is the
dimension of the class quotient missed by the selected generators. The
retained valuation term is zero on the stated good-prime domain away from
19,59,487. If it is nonzero, it must be added. Bounding the full ordinary
class group is conservative and includes any surviving class-supported
contribution; no companion-class injectivity is assumed.

Missing relations merely weaken this upper bound. Missing generators
cannot be ignored. A generation-modulo-p certificate q=0 and enough
actual relation/unit rank would suffice without computing full class
orders or saturating all relations. This is a certificate interface, not
a new seed estimate.

For p=5,7,11,13 I computed the seed's exact Frobenius/scalar orbit counts
at a common norm cutoff 2000. The faithful column counts are 71,54,25,27;
the full faithful unit dimensions are 3,4,6,7. All 301 saved seed point
counts were checked independently, and all 300 unramified p=5 rows were
matched to actual number-field ideal actions. These are fixed-cutoff
generator counts, **not** class dimensions or completed relation-rank
tests at the larger primes. Their decrease does not establish a decreasing
complete bound. No growing unit-rank or cross-prime class-bound theorem
was obtained.

## Decision and evidence grade

- **REMOVED:** the need to principalize base ideals for faithful relative
  relations; also the unnecessary requirement of full class orders and
  a full unit basis for a sufficient upper-bound certificate.
- **EXCLUDED:** this generated family, including all its scalar translates,
  gcd-support combinations and integral unit-kernel saturation, as a source
  of a new small bound. Enlarging or rearranging these same saved rows
  cannot fix that result.
- **OPEN:** new relative arithmetic that closes support on a certified
  generating set, together with actual unit norm/local rank. Neither a
  smaller residual norm nor another individual identity supplies that.

The changed method ran successfully; the limitation found is arithmetic
closure, not memory. No new base-field prime was settled. **FIN, ORDER9,
Q36 and the complete seed class/unit bound remain unchanged.**

The proofs are written deductions under retained field/source inputs;
the computations are exact PARI/Python checks, with separate arithmetic
replays and a separate mathematical review. They are not proof-assistant
certification or a novelty claim. The original rank, residual-image,
maximal-order and BSD-to-source inputs retain their prior grades.

Evidence: [arithmetic report](arithmetic/ARITHMETIC_REPORT.md),
[independent arithmetic replay](review/GENERATION_REVIEW.md),
[rank and saturation review](review/REVIEW_OF_RANK_FORMULA.md),
[sufficient presentation proof](theory/PRESENTATION_BOUND.md),
[unconditional generation test](theory/BDDF_RESULT.json),
[replay instructions](REPLAY.md).
