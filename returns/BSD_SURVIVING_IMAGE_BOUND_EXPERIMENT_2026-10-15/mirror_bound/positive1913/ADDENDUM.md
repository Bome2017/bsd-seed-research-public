# Genuine excess can be an opposite-norm boundary

The proposed countertest succeeds, and exact reverse preimages can be exhibited without a companion BNF. For1913b1, both retained independent Sha[3] unit classes lie in the image of the transposed affine norm on actual global units.

This refutes the rule “opposite-norm boundaries are point classes.” It does not refute a bound on the entire kernel using an independently proved unit index and companion class number.

## Retained arithmetic used

The curve is [1,1,0,-34,-135], conductor1913. The retained degree-eight point-field BNF is certified, its class group is trivial, and its complete S-unit source has dimension9. Its four-dimensional valuation-zero source is the global-unit source. The two known classes have literal global norm-cube certificates and all-place Selmer admission under the recorded Schaefer–Stoll theorem. Independent algebraic2-descent gives rank0, with rational torsion order2. Therefore their two independent Selmer classes give independent Sha[3] classes without assuming any primary Sha order or finiteness.

This addendum does not rerun the BNF, rank descent or all local admission. It binds their files, checks the actual unit identities, verifies mod3 independence and the retained admission matrices, and replays both forward and reverse norms exactly. No analytic Sha label enters the calculation.

## The integral deduction

Let A be the point field and B the affine-line field. Let LA and LB denote the odd global-unit lattices after tensoring with Z3; torsion of order prime to3 disappears. Both have rank2. One way to see this is that the full fields have signature(2,3), while their quotients by the central sign involution have signature(2,1). The unit-rank difference is2. The actual source computation independently has antiunit rank2.

Let n:LA->LB be the forward incidence norm and nᵗ:LB->LA the norm for the transposed correspondence. On an odd multiplicative function, composing the two norms gives its cube: a point is counted three times, while the other points occur in opposite pairs and cancel. Thus

    nᵗ n = 3,
    n nᵗ = 3

on these Z3 lattices. This is the actual incidence correspondence, not a presumed perfect pairing between arbitrary numerical matrices.

The two retained independent antiunit classes exhaust LA/3LA, and each forward norm is a cube in B. A cube root of a global unit is a global unit. Consequently n(LA) is contained in3LB. Since both maps are integral and their product is3I, the forward Smith valuations are(1,1), and nᵗ is a Z3-isomorphism. Thus reverse-norm image need not consist of point directions.

This Smith statement is a deduction on Z3 lattices. No complete integral matrix for the companion unit basis was computed, and no assertion about its prime-to3 global index is needed.

## Literal reverse preimages

Let uj be the two actual retained global units and rj their saved forward norm cube roots. Write τA and τB for the sign involutions. Set

    αj = uj / τA(uj),
    βj = rj / τB(rj).

These are strict antiunits. Scalar compatibility shows that αj represents twice the original class modulo cubes, so the two remain independent and retain their Selmer membership.

The program checks that all four elements have unit ideals, that each element times its sign conjugate is1, and that

    n(αj)=βj³,
    nᵗ(βj)=αj

as literal number-field identities, for j=1,2. Thus the conclusion is stronger than an existence inference from Smith valuations: the exact preimages β1,β2 are stored in reverse_certificate.gp.

To compute nᵗ, fix the generic short-model point (X,Y) in A. With a=-c4/48 and the line parameter z=6m, the incidence polynomial is the monic degree-three gcd

    Q(m)=gcd(m⁴−2Xm²+2Ym+a, fB(6m)).

The reverse norm is the algebra norm of βj(6m) in A[m]/Q. The separate checker verifies that Q has degree3 and divides both defining relations. It computes the reverse norm via a3×3 multiplication determinant. It also reconstructs both forward norms by multiplication determinants. No companion class group or fundamental-unit calculation is used.

## Consequence for the proposed upper-control architecture

The earlier exact sequence must retain

    (admitted classes intersect opposite norm image)
        / (point classes intersect opposite norm image).

For this actual control that term contains both independent genuine excess directions. Because rank0 and rational3-torsion zero give no point direction, they cannot be discarded as rational points. The paired homology quotient alone cannot bound the full excess, even when its maps are arithmetically authenticated.

An integral unit-index/companion-class bound on the whole global kernel is a distinct proposal and is not invalidated by this test. It must include this surviving norm-image contribution; the1913 control is now an explicit test for that requirement.

## Verification and rejected attempt

Accepted verification has empty GP stderr. Four independently formed multiplication determinants and four unit ideals pass. The Python matrix checker verifies unit support, odd-unit rank2, class independence and retained admission rows. A clean replay reproduces the exact certificate and JSON byte-for-byte.

The first trial used the nonexistent PARI name polgcd rather than gcd. Its subsequent success-like stdout and outputs were rejected because stderr contained errors. The entire failed trial is retained in rejected_polynomial_api/. No conclusion uses it.

This is a new exact comparison of retained genuine excess with the reverse norm image. It is not a new seed primary certificate, a whole-Sha order, or a bound across coefficient primes. FIN, ORDER9 and Q36 remain unchanged.
