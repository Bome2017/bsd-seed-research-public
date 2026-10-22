# Joint Kummer evaluation and the exact local-detection distribution

Date: 2026-10-15. Written deduction from elementary Galois cohomology, the retained descent realization, and Chebotarev. Not a novelty claim, a statistical fit, or an upper bound on Sha.

## Statement on a known subspace

Let V=E[3], assume the residual image is G=GL_2(F_3), and let c_1,...,c_d be linearly independent genuine classes in Sel_3(E/Q). Put d=r+s, with the first r classes a basis of the full rational-point Kummer image. The remaining s classes are a basis only of a specified known subspace of Sha[3]; there is no assumption that they exhaust it.

For good auxiliary primes q other than 3, outside the finite ramification set and splitting completely in Q(E[3]), let j_q be the rank of the map from this known quotient to

    (E(Q_q)/3E(Q_q)) / loc_q(E(Q)/3E(Q)).

Then the conditional Chebotarev distribution of j_q, among those split primes, is exactly the distribution

    rank([W | C]) - rank(W)

for a uniformly counted 2-by-(r+s) matrix over F_3, where W is its first r columns. This is a statement about asymptotic prime densities, not independent sampling of the first 24 primes.

## 1. Joint evaluation is surjective

Choose continuous cocycles representing c_i and write rho:G_Q -> G. Their tuple gives a homomorphism

    h:G_Q -> V^d semidirect G,
    g |-> ((c_1(g),...,c_d(g)),rho(g)).

Its image is finite. If J=ker(rho), its image N=h(J) in V^d is a G-stable F_3-subspace: conjugation by any lift of g in G acts diagonally by g on N.

First, H^1(G,V)=0. Indeed, the central element z=-I acts on V by -1. For a cocycle a, comparing a(zg) and a(gz) gives

    (z-1)a(g)=(g-1)a(z).

Since z-1 is invertible in F_3, a(g)=(g-1)v for v=(z-1)^(-1)a(z), so a is a coboundary.

Second, V is simple, and End_G(V)=F_3. Simplicity follows from the action of the elementary matrices, and commuting with both elementary unipotents forces an endomorphism to be scalar. The module V^d is semisimple because it is explicitly a direct sum of simple copies of V. This does NOT assert that F_3[G] is semisimple; 3 divides |G|.

If N were proper, the nonzero semisimple quotient V^d/N would have a simple quotient isomorphic to V. Hence some nonzero G-linear map V^d -> V would kill N. By the scalar endomorphism calculation, that map is (v_i) |-> sum a_i v_i with a nonzero vector (a_i) in F_3^d. Thus the cocycle sum a_i c_i vanishes on J, and descends to a cocycle on G. The preceding H^1 calculation makes its global class zero, contradicting independence. Therefore

    N=V^d.

The image of h surjects onto G and contains the full kernel V^d, so it is all V^d semidirect G. No H^2 vanishing or splitting assumption for a separate extension is used; this finite extension was constructed from the actual cocycles.

## 2. Frobenius is the local Kummer evaluation

At a good q different from 3, the unramified subgroup of H^1(Q_q,V) equals the local Kummer image. When rho(Frob_q)=I, both are naturally two-dimensional: H^1_unr is V/(Frob_q-1)V=V, and E(Q_q)/3E(Q_q) has dimension dim E(F_q)[3]=2. Formal-group and reduction kernels have no 3-primary contribution at q different from 3.

Thus the tuple of local classes is the vector in V^d supplied by the Frobenius of the joint extension. The retained descent embedding expresses that vector through its pairings with the eight nonzero torsion points; its eight cubic-residue characters are an injective coordinate realization. Taking a quotient by the point columns therefore gives exactly the displayed rank difference.

Conjugation on a kernel element v in V^d is simultaneous multiplication by an element of G. The rank difference is invariant under this action. Hence its level sets are unions of conjugacy classes in the joint Galois group. Chebotarev assigns each such union its cardinality divided by the group order. Conditioning on rho(Frob_q)=I cancels the common factor |G| and leaves uniform counting on V^d. The required density theorem is [Milne, Algebraic Number Theory, Theorem 8.31](https://www.jmilne.org/math/CourseNotes/ANT.pdf). Removing finitely many additional source-denominator or bad-reduction primes does not change these densities.

## 3. Exact counts

The parent sealed the following predictions before the independent enumeration; its file hash is bound by `DENSITY_ENUMERATION.json`. `density_enumeration.py` enumerates every matrix in the four small spaces and computes both ranks independently of the prime scan.

| Point rank r | Known excess dimension s | j=0 count | j=1 count | j=2 count | Total |
|---:|---:|---:|---:|---:|---:|
| 0 | 2 | 1 | 32 | 48 | 81 |
| 1 | 2 | 73 | 608 | 48 | 729 |
| 2 | 2 | 4177 | 2336 | 48 | 6561 |
| 2 | 0 | 81 | 0 | 0 | 81 |

For r=2,s=2, the rank-two detection count is particularly simple: both point columns must be zero, while the two excess columns must form an invertible 2-by-2 matrix. There are |GL_2(F_3)|=48 such matrices among 3^8=6561. For rank zero, decompose by the point-matrix rank: rank two contributes 48*81, rank one contributes 32*9, rank zero contributes 1. Their sum is 4177; the remaining 2336 give rank one. The other rows follow by the same count, and the exhaustive code confirms each integer.

Thus, for the seed's named r=2,s=2 span, full detection at one split prime has density 48/6561; some detection has density 2384/6561. Multiple rank-one local detectors can jointly distinguish both excess directions, as the actual primes 811 and 2767 do. The first 24 deterministic eligible primes are not independent random draws, so these densities are not converted into confidence intervals or finite-search error probabilities.

## 4. Limits and interpretation

This theorem applies only after genuine cohomological admission and independence have been established. The mirror false candidate has no such global cocycle because its affine norm is noncube; its nonzero local residue signature cannot be fed into this theorem as an additional Sha column.

The argument works with any finite d, including arbitrarily many excess directions. It explains the observed local blindness and supplies detection primes for a specified nonzero known quotient. It does not bound the size of that quotient, prove completeness of a source, exclude unknown classes, or control coefficient primes uniformly. Nor does it assert nonzero torsor localization in H^1(Q_q,E): the detected information is in its V-valued Kummer lift modulo global points.

The panel's full-image and class-independence inputs retain their original grades. The parent additionally checked the point-field Galois groups in `incidence_review/panel_image.gp`; those checks support applicability but do not replace the explicit class membership proofs. No new prime scan was performed for this deduction.
