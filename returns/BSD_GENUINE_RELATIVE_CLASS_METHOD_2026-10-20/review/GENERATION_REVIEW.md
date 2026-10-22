# Independent generation and relative-relation review

Date: 2026-10-20. This review concerns the actual degree-24 5-division point field of the seed, with the retained maximal order and scalar-2 automorphism. It is not a class-group computation or a FIN certificate.

## What a complete upper bound would require

Let A be that field, sigma its scalar-2 automorphism, iota=sigma^2, and B=A^{iota}. The two faithful scalar characters over F_5 have sigma-eigenvalues 2 and 3. The image of Cl(B) in Cl(A) is iota-fixed, so it has zero projection to both faithful components.

An exact pseudo-principal relation I=(alpha) j(a), with a an ideal of B, therefore gives a genuine relation in each faithful class component without principalizing a. This is a useful distinction from a relation I=(alpha) j(a) J with an unaccounted residual ideal J: the latter still contains the class [J]. Reducing its norm does not eliminate that class.

If a specified prime-ideal list generates the complete class group, its faithful projections give a surjection F_5^N -> (Cl(A)/5)^chi. Any matrix R of authenticated projected relations then proves

    dim_F5 Cl(A)[5]^chi = dim_F5 (Cl(A)/5)^chi <= N-rank_F5(R).

For this upper bound one does not need every relation, a saturated relation lattice, or an exact class number. One does need generation of the complete class group, or a separate bound on the omitted quotient. Selected relations among selected primes alone only bound their selected image.

## Actual complete-cutoff inventory

`prime_orbits.gp` exhaustively counts all prime ideals of norm at most 419775 in the retained maximal order. At primes not dividing the power-basis index it uses exact polynomial factorization and the literal scalar polynomial; at index primes it uses `idealprimedec` and `nfgaloisapply`. The scalar polynomial is integral. Twenty-one small non-index primes were cross-checked by the actual ideal method before the full count.

The output is:

| Quantity | Count |
| --- | ---: |
| Rational primes examined | 35,373 |
| Prime ideals under the norm cutoff | 35,749 |
| Index primes requiring actual ideal decomposition | 10 |
| Scalar-free prime orbits, hence columns per faithful character | 8,918 |

The prime-orbit count is exact arithmetic under the retained maximal-order input. The assertion that this cutoff generates the class group is separate. Its recorded source is unmodified PARI 2.17.3: `buch2.c` lines 3809–3819 searches `GRHchk`, labels the resulting `LIMC2` as a generating bound assuming GRH, and the three prior unmodified-runtime logs each print `LIMC2 = 419775`. `GRH_CUTOFF_SOURCE_BINDING.json` binds those files. This is a software-derived GRH-conditional generating bound, not an unconditional certificate or a newly independently certified analytic inequality. The theory lane records any stronger source check or certification attempt. Counting the primes itself removes none of these conditions.

`norm_inventory_result.gp` contains all prime-ideal norm multiplicities, including nonfaithful ideals, for the explicit-formula generation test. Its format is [419775,35749,35373,rows], each row [rational_prime,residue_degree,multiplicity]. It has 8,515 rows and reproduces the prime-ideal total.

For an unconditional fallback, Milne's Algebraic Number Theory, Theorem 4.3, supplies the Minkowski bound (24!/24^24)(4/pi)^10 sqrt(|D_A|). Replacing pi by 3 and sqrt(D_A) by its ceiling gives the conservative integer in `DISCRIMINANT_GENERATION_BOUND.json`, approximately 2.8046e98. This does not prove that every prime up to that enormous bound is necessary; it only shows that this elementary fallback does not certify the short list.

## The larger-prime structural panel

The parent panel computes actual seed Frobenius actions at coefficient primes 5,7,11,13 and counts faithful divisor columns below norm 2000: respectively 71,54,25,27. These are generator-demand measurements at a fixed cutoff, not class dimensions. A fall in this fixed-cutoff count does not imply an easier complete problem as the field degree grows.

I independently checked all 300 unramified p=5 rows against the actual degree-24 field and its scalar action. All matched, with total 71 (`SCALING_CROSSCHECK.json`). The p=7,11,13 portion was read as code, not reconstructed from their full number fields. Repeated Frobenius eigenvalues other than 1 contribute no faithful column because the cyclic Frobenius group contains a nonidentity scalar. The identity-versus-unipotent case at eigenvalue 1 must use the actual finite group structure; the parent code does this.

## Relative ramification and the base-ideal test

The exact discriminant ratio is D_A/D_B^2=2^4*5*4547^6. Exact contraction of prime ideals gives four finite ramified primes for A/B: one above 2, one above 5, and two above 4547. There is also one inert relative prime above 5. All five primes in this inventory are fixed by iota. Thus none has a faithful scalar component. The signatures (4,10) and (4,4) show that two real places of B ramify.

The content-stripping algorithm is valid for ideals: an iota-invariant ideal is extended from B exactly when its exponents at the ramified primes are even. Split-prime exponents must match by invariance, inert primes have relative ramification degree one, and ramified primes have degree two. Norm being a square alone would not prove this assertion. The independent replay checks invariance and all four ramified exponent conditions, and independently reconstructs the complete ramification list from the field embeddings.

## First arithmetic batch: verified, but no class-rank gain

The first batch chose eight scalar-free prime orbits, of prime-ideal norms

    7, 2401, 28561, 29, 841, 841, 31, 53.

It produced 196 exact identities I=(alpha) C J, where C is an extended base ideal. `replay_relative.gp` verifies every input I from its declared prime exponents, every multiplier identity, every discarded base ideal, and all scalar prime actions. It uses direct `nfgaloisapply`, independently of the producer's scalar-action matrix. All checks pass.

The 17 scalar residual-support collisions were also replayed. The cancellation formula is correct: if J_i=sigma^k J_j, then I_i/sigma^k I_j=(alpha_i/sigma^k alpha_j)(C_i/sigma^k C_j). On character chi this gives the row c_i-chi(sigma)^k c_j. Both actual projected matrices have rank zero. No literal ideal-cancelling nontrivial relative unit was produced. Therefore this batch yields no new upper bound on the selected faithful class image, let alone the complete component.

Later gcd refinements or scalar closures must retain all remaining prime support. A mod-5 null vector in an exponent matrix is not, by itself, a unit: it can be a virtual unit with a fifth-power ideal, precisely the class-supported contribution under investigation.

## Complete support refinement of this finite batch

The subsequent exact gcd refinement includes all 716 distinct scalar conjugates of the residual ideals and all 32 initial prime ideals. It produces 743 pairwise-coprime ideal atoms, stable under the scalar action. The atoms need not be prime: each is a legitimate ideal class, and the pairwise-coprime factorization preserves the exact divisors used here.

I independently reconstructed every one of the 196 divisor rows as the literal fractional ideal I/J, checked all 743 scalar actions with `nfgaloisapply`, and reconstructed every faithful character projection. All passed (`replay_support.gp`). There are 185 faithful support columns: 8 original and 177 newly introduced columns.

Separate Python elimination gives rank 156 for each character matrix, and also rank 156 for its restriction to the 177 new columns. Therefore the rank of the subspace of relations supported only on the original eight columns is

    rank(R) - rank(R_private) = 156-156 = 0.

`PRIVATE_FACTOR_CERTIFICATE.json` is stronger bookkeeping than a printed rank: for each character it contains an explicit matrix T with R_original=R_private*T over F_5. Every entry of that equality is checked. Thus any F_5-linear combination of these 196 rows which cancels all newly introduced columns also cancels every original column. No rearrangement of this fixed relation family can eliminate one of the eight original faithful class generators.

The 29-dimensional quotient of the expanded formal support module is not the full class group and is not a complete class bound. The eight original generators also were never shown independent in the actual class group; the result only says that this batch supplies no new relation among them. It is a bounded failure of this particular relation construction, not an impossibility theorem for relative-class methods or FIN.

There is also an exact conclusion about the units available from this batch. The anti-divisor map has 392 input rows and 743 ideal-atom columns. I reconstructed it from the authenticated divisors, checked an exact 80-column nullspace, and found ranks 312 and 80 modulo 5 respectively. These lower bounds plus the exact zero product certify the full rational nullspace without trusting a printed rational rank. All 80 actual multiplier products were recomputed: 78 are +1 and two are -1 (`replay_unit_kernel.gp`). Any additional integral vector in the same rational kernel has an integer multiple in this basis, so its multiplier is torsion. The field has a real embedding; hence its roots of unity are only +1 and -1. Integral saturation of this fixed batch therefore cannot uncover a nontrivial 5-adic unit direction. This conclusion is about the tested family only.

The theory lane's independent unconditional BDDF criterion test fails at this cutoff (`theory/BDDF_RESULT.json`). Its rational upper/lower estimates are conservative: the left side is bounded above by about 56.182 while the right side is bounded below by 352. This excludes that sufficient certification test at this cutoff; it does not show that the prime list fails to generate. The GRH-conditioned software generating-bound status remains separate.

## Final accounting against the complete cutoff list

The 177 private orbit symbols were also classified by their actual prime support, not simply their ideal norms. I independently trial-divided every norm by all 35,373 rational primes through 419775. Exactly 156 symbols retain a nontrivial cofactor after all those primes are removed, proving that each has support above a rational prime larger than the cutoff and hence outside the prime-ideal generating list. For the other 21 symbols, I independently factored and reconstructed the actual ideals; every supporting prime ideal has norm at most 419775. This also checks the residue degrees, which cannot be inferred merely from small rational prime factors.

The outside-support 156-column submatrix has rank 156 for each faithful character. `OUTSIDE_SUPPORT_FACTOR_CERTIFICATE.json` supplies explicit matrices with

    R_bounded_selected = R_outside * T  over F_5.

Every entry is checked by separate Python arithmetic. Consequently, replacing the 21 inside symbols by their expressions in the full cutoff generating list cannot create a relation on that list: all available row rank is already used by the outside symbols. Even retaining the software GRH generation premise, the resulting complete presentation allowance is unchanged:

    8918 + 156 - 156 = 8918  per faithful character.

This is an independently checked failure to improve the complete bound, stronger than merely noting that the original eight columns survive. It neither computes the actual class dimension nor says that any of those 8918 allowances is attained. The classification and ranks are recorded in `COMPLETE_ACCOUNTING_REVIEW.json`; the exact inside-prime ideal checks are in `replay_private_support.gp`.

## Sources and scope

- [Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorem 4.3: unconditional ideal-class representatives and Minkowski bound.
- [Current PARI general number-field documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html): GRH status of BNF output, generating-bound checks, exact ideal operations, and `bnfcertify`.

Current PARI's `bnfcertify(...,1)` can certify the class-group quotient without certifying fundamental units, but it still takes a BNF structure. It is not an available certificate for an arbitrary selected relative-relation matrix. The source statement must not be replaced by the stronger assertion that all class certification requires fundamental units.

Retained inputs are the seed field, maximal order, scalar action, and prior arithmetic reductions. This review supplies exact generating-set inventory and relation replays; it does not independently recertify the full BSD-to-field reduction. FIN, ORDER9 and Q36 are not changed by the first batch.
