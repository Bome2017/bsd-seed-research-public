# Independent seed-matrix review

The clean producer transcript was parsed directly by `check_producer_matrices.py`.
Its printed rank fields were not used. The checker accepted only the two GP
stack-size warnings in stderr, required the final completion marker, and bound
the source and transcript by SHA-256 in `SEED_MATRIX_CHECK.json`.

All 26 complete principal-ideal valuation rows of the four displayed source
elements are zero modulo 3. Thus A0=A and W0=W. The raw cyclic class matrix is

    [0, 8, 8, 8]
    [0, 0, 4, 4]
    [0, 0, 0, 0]

in cyclic factors [12,6,2]. Conversion to actual 3-torsion coordinates gives

    C = [0, 2, 2, 2]
        [0, 0, 2, 2].

The independent calculation obtains

    rank C = 2,  rank C(W) = 1,
    ker C = span(e1, e3-e4),  ker C intersect W = span(e1).

The three quotient dimensions are therefore

    (valuation, global-unit, ideal-class) = (0,1,1).

In particular the ratio beta1/beta2 of the two *algorithmically reconstructed*
cubic representatives is the unit-quotient direction, and one remaining cubic
direction accounts for the class quotient. These are the specific representatives
in `actual_representatives.gp`; the Cardano/descent convention may invert a
historical cubic class. No equality with a differently signed historical
representative is being asserted.
These statements are invariant under adding any point directions to the cubic
representatives. The companion abstract checker verified all 81 such changes
for every one of the 2,193 nested subspace flags in F3^4 (177,633 cases total).

## Grades and limitations

This is an independent exact linear-algebra replay of the supplied number-field
matrices. It is not a second calculation of the number field, ideal classes or
the original cubics. The full (0,1,1) classification retains the class-group
completeness grade of the producer's cached BNF. It does not establish a new
upper bound on Sha or extend the result to another coefficient prime.

An exact principal-ideal generator for the cube-root ideal of the cubic ratio
can independently authenticate the *positive* unit relation without assuming
completeness of the class group. The producer supplies a compact certificate
for that purpose. The matrix replay itself does not verify the compact
generator factors, so it must not be described as an independent authentication
of that additional arithmetic identity.

Combined with an authenticated unit relation and the retained independent
classes modulo the point plane, the positive unit direction refutes the
class-only explanation for these actual seed classes. It does not assert that
unit directions must survive for other primes, or give a uniform vanishing
criterion.
