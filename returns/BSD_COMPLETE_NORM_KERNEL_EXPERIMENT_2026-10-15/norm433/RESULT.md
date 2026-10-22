# Complete global norm kernel for 433a1

The complete scalar-compatible source has dimension six. Its actual affine-line norm map has image dimension three and kernel dimension three. The kernel is precisely the two rational-point classes together with one additional valuation-supported class. Both local places, 3 and 433, reject the additional class. Thus the full admitted intersection is exactly the two-dimensional point plane.

This tests the entire saved source, not only known point columns. It disproves the proposed rule that the global norm kernel must equal the scalar-compatible valuation-zero source: the additional literal norm-cube class has nonzero valuation vector. The distinction is global admission versus local Selmer admission. No conclusion about the seed's unresolved coefficient primes follows.

## Exact arithmetic objects

The curve is y²+xy=x³+1. The retained complete source is thirteen actual elements G_i in the degree-eight point field

    A = Q[w]/(w^8-54w^4-217w²-243).

The saved source includes all allowed S-valuation, unit and class directions for S={3,433}; its ordinary class group is trivial. Source completeness, its certified BNF and the rank-two point basis remain retained inputs. This run replays the thirteen literal scalar-involution identities and both literal point-map identities.

Write a=-c4/48, b=-c6/864 in the short model. The affine-line field is

    B = Q[z]/(z^8-54z^4-186840z²-243), m=z/6.

The three torsion points of the line are represented in

    G(X)=X³-m²X²+(m⁴+2a)X-m⁶-2am²+4b,
    Y=mX-(m⁴+a)/(2m).

The saved exact field embedding reconstructs w from Y. The map takes each source element to the determinant of multiplication by its image in B[X]/G, modulo cubes. Both PARI's norm operation and a separately constructed 3×3 multiplication determinant give the same six values. The map is computed on all six scalar-basis columns; see norm_data.gp and norm_polynomials.json.

## Complete kernel certificate

The two point columns and the extra vector

    v=(1,2,0,2,1,2,0,0,1,0,0,0,1)

are independent. For all three actual products of G_i, candidate_cube_roots.gp contains a literal B-element whose cube equals its affine norm. These are positive certificates, not extrapolations from zero residue lists.

The other direction is certified by six degree-one B-prime evaluations above 43,67,103. The rows at (43,1), (67,19), (103,15), restricted to the first three scalar columns, form

    [2 0 1; 0 0 1; 1 2 1] mod 3,

with determinant 2. These three independent noncube characters prove norm-image dimension at least three. The three literal cube classes prove dimension at most three. Thus the norm kernel is exactly the displayed three-dimensional space. The primes need only have simple degree-one B-roots; full splitting of the entire torsion field is unnecessary for a negative B-cube certificate.

The Python standard-library checker independently evaluates the rational norm polynomials, verifies simple roots and cubic characters, and checks the finite-field matrices and determinant. It does not regenerate the number fields.

## The extra class is globally admitted but locally rejected

The extra has S-valuation vector

    (1,2,0,2,1,2,0,0,1),

whereas both point columns have zero valuations. Its source is consequently a valuation direction, not an ordinary class-group direction. On the retained Schaefer–Stoll global source criterion, its scalar compatibility and literal affine norm cube provide global cohomological admission. No assertion about full Selmer admission is inferred from those two properties.

The local Kummer images were resampled with a fresh fixed seed at 45-digit precision. Their rowspaces match the retained local images. Six exact rational Hensel samples satisfy the cube-class precision inequalities, independently rechecked in local_witness_check.py; the smallest margin is 43. Sampling reaches the independently determined full local image dimensions, two at 3 and one at 433.

The extra's saved quotient vectors are

    at 3:   (1,2,0,0,1,0,2,2,0,2,1,1,0,2),
    at 433: (2,0,0,0,0,1,0).

Fresh local quotient row bases may differ, but the full rowspaces agree and both reject the extra. The combined local restriction to the three-dimensional exact norm kernel has rank one; its kernel is exactly the original point plane. complete_certificate.json gives every matrix in the original thirteen-source coordinate system.

## Replay and limitations

Run python3 replay.py. It uses local bound inputs and the PARI executable named by PARI_GP or the recorded default. All eight arithmetic products reproduce byte-for-byte in an empty temporary directory. Every accepted GP process has exit code zero and empty stderr; independent rational-Hensel and finite-field checks pass.

Rejected implementation attempts are retained: an incorrect executable path, a GP brace error in the rank exporter, and an incorrect coefficient extraction from a polmod while reconstructing the involution. The last issue was caught by the literal field identity, repaired by lifting the polmod before extracting coefficients, and followed by a clean replay. No output from those failed attempts is accepted.

The finite source and the full norm map are now controlled for this one curve at coefficient prime 3. This is a complete control calculation and a counterexample to a proposed simplification, not a uniform bound, a new BSD theorem, or new seed prime coverage. FIN, ORDER9 and Q36 are unchanged.
