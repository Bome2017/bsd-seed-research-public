# Actual paired norms and the term a bound must retain

The two complete saved sources for389a1 and its -3 twist support literal paired norm maps. Their source-coordinate matrices compose to zero modulo cubes. They give homology dimensions0 and1, respectively. On the mirror side, the image has two independent valuation directions and no valuation-zero direction; the remaining homology is exactly the ordinary-class line.

This is actual paired arithmetic, computed before local Selmer rows. It supports testing an upper bound through the companion field's unit/ideal norm indices. It does not by itself bound the admitted image or prove a new seed result.

## Source-independent production

The inputs are the previous certified complete sources and their exact affine norms, copied and hashed in INPUT_BINDINGS.json. The point-field sources have dimensions10 and11, with scalar-compatible parts of dimensions4 and5. No point rank, known Sha order, analytic value or local admission matrix enters paired.gp's construction of the maps.

The line field of each curve is identified with the point field of its -3 twist by exact rational field isomorphisms. The code verifies the defining polynomial identities. For every scalar source column, its actual affine norm is transported through the isomorphism into the other point field. Independent source residue coordinates identify a candidate exponent vector; then an exact cube root certifies the coordinate identity in the number field. There are nine such literal identities, four in one direction and five in the other. A source-coordinate solve without these cube identities would not be accepted.

Write SA and SB for the two scalar spaces, with A=389a1 and B=its mirror. In their recorded bases the maps are

    NA: SA -> SB,
    NB: SB -> SA.

Both have rank2, and NB NA=0 and NA NB=0. Explicit matrices and field elements are in paired.json and paired_certificate.gp. check_exact.gp independently verifies all nine cube identities, field maps, scalar coordinates and zero composites. check_matrices.py independently verifies the finite-field conclusions.

## The arithmetic quotient

The result is

    ker NA = im NB, dim2,
    dim(ker NB / im NA)=1.

The mirror image im NA has valuation rank2 and zero intersection with the valuation-zero source. Its complement in ker NB is represented by

    (0,0,0,0,0,0,0,1,2,2,1),

whose ordinary-class coordinate is1. Therefore the one-dimensional homology is class-supported. This conclusion follows from complete source arithmetic and its ideal-class map, without using local admission or a known Selmer dimension.

Only afterward, check_exact.gp compares im NB with the retained rational-point image on389a1: they agree. That recovers the already-known containing bound2 for this control. It is not an independent new seed result or a uniform theorem.

## Why homology alone is not a bound on excess

Let P be an admitted subspace of ker N, W its rational-point subspace, and J=im Nopposite. There is an exact sequence

    0 -> (P intersect J)/(W intersect J)
      -> P/W
      -> (P+J)/(W+J) -> 0.

The last term is controlled by the norm-complex homology after removing the point image. The first term is not. Thus a small homology quotient does not give a bound on P/W unless the admitted opposite-norm image is independently controlled.

An abstract countercontrol is an exact two-periodic complex of four-dimensional F3 spaces with both maps rank2. Its homology vanishes. Taking P=J of dimension2 and W=0 leaves excess2; taking W=J leaves excess0. This is an algebraic scope check, not an arithmetic model or a statement that1913b1 realizes that norm-image position.

The positive control1913b1 is the appropriate arithmetic discriminator: it has two genuine admitted unit-supported classes and rank0. If both are opposite norms, then homology-only control misses actual excess. This test requires companion-field units or actual norm preimages. The bounded search found no cached1913 companion BNF/units in the named prior experiment roots; none were supplied by the unit-index worker. No new BNF was launched, and no outcome for that discriminator is claimed.

## Concrete continuation supported by these maps

The distinct candidate being tested by the companion calculation is a bound on the entire global norm kernel from the integral S-unit norm index and the companion S-class group. That would retain both norm-image and homology contributions rather than dropping the first term above. The present matrices can authenticate such a bound against389/mirror; they do not establish its general arithmetic inequality. A bound obtained simply by inserting the already-known norm-kernel dimension is inadmissible as an independent estimate.

The p=3 twin fields and actual ideals are part of this construction. Nothing here gives a prime-independent field or an index bound as the coefficient prime varies. FIN, ORDER9 and Q36 remain unchanged.

## Replay and implementation record

Run python3 replay.py with PARI_GP set if necessary. The accepted GP processes have empty stderr and exit code0; the independent matrix checker passes. The exact arithmetic outputs reproduce byte-for-byte in a clean temporary directory.

The first exporter applied a kernel to a redundant list of norm-image columns and printed the number of zero columns as an H0 dimension. The actual maps and ranks were correct, but that dimension label was rejected. The corrected computation first takes an independent image basis. The accepted H0 intersection dimension is0. The failed bookkeeping version is retained under rejected_redundant_image_columns.

No new BNF, expensive source computation, detector-prime search, local-image experiment, publication or seed certificate was performed in this subtask.
