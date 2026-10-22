# Complete affine norm on the class-supported mirror source

The full scalar-compatible source has dimension five, and its actual affine-line norm kernel has dimension three. The three-dimensional kernel has two valuation directions, one ordinary-class direction, and no ordinary-unit direction. The actual local Kummer restrictions at 3 and 389 have combined rank three on it. The full admitted intersection is therefore zero.

This upgrades the earlier mirror experiment from necessary split-prime global rows to an exact norm-kernel certificate on the whole saved source. In particular, the globally repaired ordinary-class direction has a literal norm cube; the locally repaired ordinary-class direction has a noncube norm. The mismatch is not caused by an incomplete finite set of global rejection rows.

The control is the -3 twist of 389a1, with minimal model y²+y=x³-21x-27, conductor3501, rank zero and bad reduction at3. It is not the seed or a rank-two ordinary control. No seed endpoint or new coefficient-prime coverage follows.

## Scope and source custody

The retained source is eleven actual cube classes in the degree-eight point field, including units, all S-valuations for S={3,389}, and the nontrivial ordinary class. Its class group and S-class group are C3. The saved BNF certificate is recorded as BNF_CERTIFIED=1 in inputs/scan.out; the historical run took2236ms. The BNF is retained, not rebuilt or freshly certified in this run. Its original stderr contains only the stack-limit warning. The source class count, support and independent residue-rank certificate are retained from the previous exact export. Source bindings identify every copied file.

An initial expectation of a one-dimensional full global kernel confused the prior H0-restricted statement with the whole source. The exact dimension assertion failed before any accepted norm outcome. That run and its downstream files are preserved in rejected_candidate_shape/. The subsequent ADAPTATION.md was sealed before the accepted computation: the full necessary global kernel has dimension3, while its H0 part has dimension1.

## Actual map and complete rank certificate

The point field is

    A=Q[w]/(w^8-4w^7-17w^6+12w^5+270w^4+33w^3-1101w²-1218w+3945).

The affine-line field is

    B=Q[z]/(z^8-54432z^4+4992192z²-246903552).

Use the exact short-model line cubic and field embedding constructed in construct.gp. The affine norm of each of the five scalar-basis elements is computed as a cubic-algebra norm and independently replayed as a 3×3 multiplication determinant. norm_polynomials.json gives all five rational polynomials in z.

All three columns of global_norm_kernel in norm_map.json have literal cube roots in B, stored in candidate_cube_roots.gp. Independent B-prime cube characters give a rank-two lower bound on the norm image. At (q,z)=(19,2) and(73,9), the first and third scalar columns give the matrix

    [0 2; 2 1] mod3,

whose determinant is2. Thus the five-dimensional source has norm-image rank exactly2 and norm-kernel dimension exactly3. Ten actual residue rows are retained. The standard-library Python checker independently re-evaluates all norm polynomials, roots, cubic characters and matrix ranks. Finite zero rows are never used as positive cube certificates.

The previously selected locally repaired false class

    (0,0,0,0,0,0,1,1,1,1,2)

has character1 at the first B-prime (19,2), so its norm is not a cube in B. The other prior work established noncubeness even in the full torsion field using a fully splitting prime; this experiment does not replace that field distinction.

## Unit, class and valuation contributions

The valuation map on the exact norm kernel has rank2. Its kernel is one-dimensional, and the saved ordinary-class map is nonzero on that line. The intersection with the four-dimensional ordinary-unit source is zero. The class map and literal ideal identity I³=(beta) are retained and replayed through inputs/class_witness.gp; verify_exact.gp checks the ideal identity and its source binding again.

Consequently the three norm-cube directions are not merely unit directions or point columns. This control exercises the class-supported piece absent from the trivial-class-group controls. The full norm gate alone admits it; the local gate removes it.

## Same ordinary class, incompatible actual repairs

In the fixed ordinary-class coordinate, both following source vectors have class1:

    global repair: (0,0,0,0,0,0,0,1,2,2,1),
    local repair:  (0,0,0,0,0,0,2,2,2,2,1).

Their difference is the actual ordinary-unit combination (1,2,0,0). The first has literal norm cube and local3 defect (0,2,0,1,0,0,0,0,0,0), with local389 defect zero. The second satisfies both local places but has norm character2 at (19,2). The latter is twice the previously selected false candidate, which had ordinary-class coordinate2; the orientation correction is explicit. class_contrast.gp/.json checks the common class and literal original-source unit difference. The independent Python check verifies the unit difference and opposing admission patterns.

## Exact local rejection

The local images were independently resampled at45 digits with a fixed fresh random seed. Twenty rational samples have exact Hensel and cube-class precision certificates, with minimum margin37. Their rowspaces agree with the previously saved full local images. Sampling is accepted only after reaching the independently known local image dimension, two at3 and one at389.

On the exact three-dimensional norm kernel the local3 block has rank2, the local389 block rank1, and their stacked rank is3. Thus their common kernel is zero. complete_certificate.json exports the actual original-source vectors, both block restrictions, class/valuation filtration, and the previously false candidate's norm characters.

This also specifies why checking local3 alone would be incomplete: it leaves a one-dimensional direction, which local389 removes. Conversely the389 block alone leaves two directions. The conclusion comes from their actual joint matrix, not dimension subtraction without checking intersection.

## Replay and status

python3 replay.py reconstructs the five norms, three cube roots, negative residue map, authenticated local images and full certificate in a clean temporary directory. All nine arithmetic output files reproduce byte-for-byte. Accepted GP stderr is empty. The independent finite-field/rational-Hensel checks pass. No new BNF calculation, remote job or publication occurred here.

This is complete arithmetic for this saved coefficient-three control. It supports a specific architecture—actual global norm admission followed by simultaneous local admission—and shows why neither valuation-zero truncation nor a single local block suffices. It does not supply an upper bound across seed coefficient primes. FIN, ORDER9 and Q36 remain unchanged.
