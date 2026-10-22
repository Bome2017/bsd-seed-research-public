# Actual seed relative ideal arithmetic

Date: 2026-10-20. Status: `EXACT_RELATIVE_RELATIONS_NO_COMPLETE_BOUND_GAIN`.

This run performs arithmetic in the seed's actual degree-24 nonzero-five-torsion-point field A, with its scalar automorphism sigma of order four. It does not use a control curve or the known Sha[5] certificate. The tested object is the relative class contribution for A/Aplus, where tau=sigma^2 and [Aplus:Q]=12.

## Result

The implementation produced and authenticated 196 exact relative pseudo-relations. Refinement of their entire scalar-stable residual support gives 743 pairwise-coprime ideal atoms and 185 faithful character columns. The relation matrices have rank 156 in each of the two faithful F5 characters. However, every one of these 156 ranks is absorbed by additional ideal-class symbols; no relation is induced on the eight original generator orbits.

The stronger complete-list accounting has the same outcome. Among the 177 new character columns, 21 are supported entirely on prime ideals of norm at most 419775; 156 contain prime-ideal support beyond that bound. The submatrix on those latter 156 columns has rank 156. Thus adjoining this batch to the independently inventoried 8918-column GRH generator list gives, conservatively,

    8918 + 156 - 156 = 8918

in each faithful character. It does not decrease the complete generator bound. The GRH condition on that list has not been removed.

The exact anti-divisor relation kernel supplies no non-torsion relative unit. Its 80 rational basis vectors, cleared to integer vectors, give 78 products equal to +1 and two equal to -1. Saturating that kernel cannot conceal a non-torsion unit: every saturated-kernel product has some power equal to a product of those signs. Since A has a real embedding, its roots of unity are only +/-1, both trivial modulo fifth powers.

This is a scoped outcome for the tested relative-reduction producer. It is not a proof that relative class methods cannot supply a bound. FIN, ORDER9, Q36 and seed-prime coverage are unchanged.

## Exact relative driver

For each chosen integral ideal I the driver maintains

    I = (alpha) C J,

where C is extended from Aplus and J is primitive relative to Aplus. No base ideal is principalized. The anti-projection gives

    I/tau(I) = (alpha/tau(alpha)) J/tau(J).

To remove base content, the code starts with the ideal gcd J+tau(J). At a split relative prime this takes the minimum of the two exponents. At an inert relative prime every exponent is extended. At a ramified relative prime the extended exponent must be even, so an odd exponent is reduced by one. The actual four relatively ramified primes are authenticated by contraction into Aplus. Their rational supports are 2, 5 and 4547, consistent with the independently checked relative discriminant norm 2^4*5*4547^6.

PARI idealred supplies an LLL short multiplier. Its orientation is not guessed: the code tests the exact principal-ideal identity and corrects the direction if necessary. Every accepted row checks I=(alpha)CJ. Norm descent is strict, except that the first distinct nondecreasing alternative is retained for exact cycle testing.

This is Cohen's relative-content invariant and descent driver with an absolute LLL short-element choice. It is not a claim to implement Cohen's relative-HNF short-element routine in full. No bnfinit, class-group API, or rnfisnorm call is used.

## Tested family

Eight actual scalar prime-ideal orbits were used, with representative norms

    7, 2401, 28561, 29, 841, 841, 31, 53.

Each was raised to exponents 5,25,96,97,125,192,256,512, with two LLL directions. Six mixed products P_i^96 P_j^97 for the first four orbits were also tested. Each input permits at most four strictly decreasing steps. The 196 authenticated rows include intermediate alternatives; they are not 196 independent relations.

The ordinary scalar-collision test yielded 17 cycles, all zero in the two faithful projected rows. The subsequent repair did not stop at equality of complete residual ideals. It refined their common prime-ideal support by exact ideal gcds, divisions and scalar closure.

## Complete support and matrix calculation

The 716 distinct scalar-conjugate residual ideals, together with the 32 original scalar prime ideals, refine to 743 pairwise-coprime actual ideals. These atoms can be composite. Every original and residual ideal is reconstructed exactly as a product of the atoms. Sigma permutes them exactly. Every atom has norm which is not a perfect fifth power, so its valuation vector is nonzero modulo five; disjoint supports therefore make the atom divisor columns independent modulo five.

For a length-four scalar orbit with base atom B, the faithful projection sends sigma^k B to chi(sigma)^k B, with chi(sigma)=2 or 3 in F5. Shorter scalar orbits contribute zero. Each relation row is the projected divisor of I/J; the principal multiplier and base ideal vanish in the relative class quotient.

There are 185 faithful atom orbits: eight original and 177 private. Let R be either 196-by-185 relation matrix, and R_private its restriction to the private columns. The dimension of the rowspace supported on original columns is exactly

    rank(R) - rank(R_private) = 156 - 156 = 0.

The selected-support presentation has dimension 185-156=29. This gives at most a bound on the subgroup generated by that selected support. It is not a bound on the full faithful class group.

For complete-list accounting, the norm of each private atom is partially factored through every rational prime below 419776. A nontrivial remaining factor certifies actual rational prime support above 419775. For each small rational factor q, the code constructs the actual primes above q, tests their valuations on the atom, and compares q^f with 419775. This does not infer outside support merely because an atom has large norm. It certifies 21 inside and 156 outside private orbits. Both outside-column submatrices have rank 156, so no induced relation on the bounded-prime list survives their elimination.

## Exact unit test

For each of the 196 rows let d_i be its full atom divisor I_i/J_i. The actual unit candidate source is alpha_i/tau(alpha_i), with divisor d_i-tau(d_i). Including one sigma translate gives a 392-by-743 integer matrix H. It has rational rank 312. The computed kernel has dimension 80; its columns have coefficient L1 norm one or two. Each candidate product is evaluated as an exact element of A, its ideal is checked to be O_A, and its relative norm is checked to be one.

All products equal +/-1. This checks actual elements, not floating logarithms or vanishing residual divisor rows. A mod-five divisor relation alone would not have justified a unit assertion.

## Evidence and independent replay

- `batch_rows.gp`: 196 exact rows [id, tag, original exponents, I, alpha, C, J, steps].
- `closed_cycles.gp`: 17 scalar collisions and principal witnesses.
- `gcd_basis.gp`: pairwise-coprime atoms, norms and scalar permutation.
- `support_matrices.gp`: full reconstruction data and both character matrices.
- `private_support_result.gp`: per-orbit partial norm factorization and actual support classification.
- `complete_bound_accounting_result.gp`: inside/outside columns and outside ranks.
- `integer_kernel_data.gp`: exact anti-divisor matrix and rational-kernel basis.
- `unit_kernel_result.gp`: all 80 exact unit results.

The separate review lane independently replayed all 196 pseudo-relations and 17 collisions using nfgaloisapply rather than the producer's scalar matrix. It reconstructed every divisor row, independently checked matrix ranks in Python, and recomputed all 80 unit products. See the sibling review folder for its scoped receipts and remaining review limitations.

## Resources and custody

All stages are bounded local jobs with direct stdout/stderr and process-group termination. Accepted elapsed times include: batch 30.61s; scalar cycles 1.12s; gcd refinement 36.26s; support ranks 15.65s; integer kernel 1.24s; exact units 0.64s; support classification 1.17s. No arithmetic stage approached its wall limit. Maximum RSS was approximately 242 MB in the integer-kernel stage. Three early setup mistakes are preserved under rejected_* folders; they were not accepted mathematical output.

INPUT_BINDINGS.json binds the retained field data. The final manifest binds the actual executed scripts, including relative_setup.gp, raw outputs and dependency files. Individual runner receipts bind their entry scripts; they should not be misread as independently binding every transitively loaded file. Scripts append their raw evidence, so production replay should use a clean working directory. The sibling inputs folder contains portable copies of the retained field files; the executed setup script retains its original absolute source paths for exact custody.

No existing sealed result was edited. No remote job, paid computation or publication was performed by this arithmetic worker.
