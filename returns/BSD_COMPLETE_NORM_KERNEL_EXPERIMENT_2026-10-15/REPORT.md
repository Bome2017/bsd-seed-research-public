# Complete norm maps, common-point kernels, and an adaptive class-source test

Date: 2026-10-15. Status: **ACTUAL COMPLETE-SOURCE EXPERIMENTS; SPLIT-PRIME SEPARATION DEDUCTION; NO NEW SEED BOUND**.

This continues the experiments from lab commit87cdf8c9. The original question was whether the new detector could control an entire containing source rather than only the already-known classes. We computed actual norm maps, then used the results to strengthen the detector argument and to extend the experiment to a nontrivial class-group source. No new seed coefficient prime, FIN, ORDER9 or Q36 conclusion is claimed.

## 1. The complete arithmetic, not only selected columns

All rows below concern coefficient prime3. The source dimensions are dimensions over F3. Complete-source and original rank/image inputs retain their stated historical certification; the norm maps and the additional local checks were executed in this run.

| Control | Complete multiplicative source | Scalar-compatible source | Exact global norm kernel | After all required local conditions | Rational-point image |
|---|---:|---:|---:|---:|---:|
|1913b1|9|3|2|2|0|
|389a1|10|4|2|2|2|
|433a1|13|6|3|2|2|
|−3 twist of389a1 (“mirror”)|11|5|3|0|0|

For each scalar basis we computed the actual cubic incidence-algebra norm into the degree-eight affine-line field. Literal cube roots prove a subspace lies in its kernel; independent noncube residue ranks prove that no further source direction lies there. This certifies the entire map, unlike treating finitely many zero residue tests as a proof of cubehood. Across the four controls, eighteen scalar-basis norms and ten kernel cube roots were checked. Independent multiplication determinants reproduce the norms.

The genuine positive control1913b1 retains its two excess directions. The norm test is therefore not being fitted to erase Sha.389a1 retains exactly the point plane.433a1 retains one additional, genuinely globally admitted class; its norm is an exact cube. Both local3 and local433 reject that extra class. Continuing to add global norm tests would never remove it.

Sources and exact certificates: [two primary controls](norm_controls/REPORT.md), [433a1](norm433/RESULT.md), [mirror](norm_mirror/RESULT.md).

## 2. We changed the next experiment when the first result demanded it

The first two controls suggested a possible simplification: perhaps the norm kernel was just the valuation-zero scalar source. That candidate was explicitly tested.433a1 disproves it: its extra norm-cube class has nonzero valuation vector

    (1,2,0,2,1,2,0,0,1).

We consequently expanded the calculation to the mirror source, whose ordinary class group and S-class group are both C3. Its exact global norm kernel has two valuation directions and one ordinary-class direction, with no ordinary-unit intersection. Local3 has rank2 on this kernel; local389 supplies the remaining independent row. Their joint kernel is zero.

This also repaired an earlier scope error: a one-dimensional global kernel had been computed only inside the valuation-zero source H0. The full global kernel has dimension3. The failed full-dimension expectation and its correction are preserved in the mirror packet.

The mirror now gives a literal comparison between two representatives of the same ordinary class, expressed in its original eleven-generator source:

    globally admitted: (0,0,0,0,0,0,0,1,2,2,1),
    locally admitted:  (0,0,0,0,0,0,2,2,2,2,1).

The first has a cube norm but fails local3. The second passes both local tests but has noncube norm, witnessed already at the affine-line place (q,z)=(19,2). They differ by ordinary-unit exponents(1,2,0,0). The obstruction is the incompatibility of the repairs, now verified against the **complete** global map. Separate existence of a global repair and a local repair does not provide a common one.

That suggested another candidate: perhaps local admission removes class-supported excess, leaving only units. We tested it against the seed's actual known classes, retaining their existing membership proofs. The ordinary-class coordinate matrix on(P1,P2,beta1,beta2) is

    [0 2 2 2; 0 0 2 2].

The point image is its first two columns. Modulo that point image, the surviving row is(0,0,2,2), of rank1. Thus genuine seed3 excess has a class-supported direction; beta1−beta2 supplies the unit direction. On28042, by contrast, the point itself exhausts the known class image, and its two known excess directions have unit representatives. The support rule fails, with a precise difference between raw class support and support **after quotienting by points**. These are deductions from retained known classes, not newly discovered seed classes. Coefficient3 is bad for the seed, so this does not disprove a narrower theorem restricted to good coefficient primes at least5. See [class comparison](class_comparison/REPORT.md).

## 3. Common-point detection now tests entire sources

For a finite scalar-compatible source U, point image W and stacked residue map E_Q, the invisible space before taking the point quotient is

    Z_Q = {x in U : E_Q(x) in E_Q(W)}
        = W + (U intersect ker E_Q).

The same point coefficients must repair every place. Separate local quotients allow different coefficients and lose information.

New433 evaluations make this explicit. Its extra global class agrees with P1 at223 and with P2 at967, uniquely at each place. Both separate quotients vanish. The common quotient detects the incompatibility. Raw residue evaluation at these two primes is injective on all six scalar source coordinates, not only on the three globally admitted coordinates.

The first injective prefixes on the whole displayed scalar sources are1913:997;389:73,151;433:223,967;seed3:811,1213,1543;28042:487,691. Complete-source claims apply to the first three. The seed source retains its historical conditional grade;28042 remains incomplete. No matrix operation repairs an omitted ambient source direction.

Known excess columns were withheld from the kernel computation and compared only after its output was hashed. This is a retrospective withheld-column check, not a historically blinded discovery. The six fresh433 blocks have624 independently replayed literal field/character evaluations. See [joint-kernel report](joint_kernel/REPORT.md).

## 4. The experiments led to a stronger general separation argument

There was a legitimate concern that an arbitrary noncube in the affine-line field could become a cube in the full torsion field, and therefore remain invisible at every completely split prime. That concern does **not** apply to the actual homogeneous source and norm image when −I is in the residual image.

Schaefer–Stoll identifies both modules as the central weight-one summands. The central involution acts as−1 on each. Averaging and inflation–restriction therefore show that restriction to the full torsion field is injective on their H1. Chebotarev then separates every nonzero element of any finite scalar-compatible source. Hence finitely many eligible prime blocks make E_Q injective and Z_Q=W. A greedy existence argument needs at most dim(U) suitably chosen blocks; it gives no bound here on their sizes or the length of a sequential search.

This is a written deduction with a separate same-team mathematical review, under the explicit source/image inputs. It strengthens the previous argument from true classes to the entire authenticated scalar source, including false global candidates. Its ambient residue target must not be silently replaced by the local elliptic Kummer target before admission. The [proof](review/SPLIT_PRIME_COMPLETENESS.md), [review](review/INDEPENDENT_COMPLETENESS_REVIEW.md), and an explicit Cardano countercontrol preserve that distinction.

Finite geometric-module checks at3,5,7,11,13 support the module implementation. They are **not** number-field descents at those primes or evidence of a seed-wide bound.

## 5. What has accumulated toward the seed

We now have complete control examples separating four operations: constructing a containing source, global norm admission, simultaneous local admission, and detection modulo one common rational-point image. We have also removed the possibility of a permanent split-prime blind kernel for an authenticated scalar source under the stated image hypothesis. These are direct answers to the requested completeness/kernel experiments.

They do not give a small bound on the **image of the genuine surviving classes**.1913b1 is the deliberate countercontrol: the detector is complete and injective, yet its genuine excess has dimension2. A complete detector can expose a large group faithfully. For the seed's unresolved primes, a further arithmetic constraint on the admitted image or on the global/local repair intersection is still needed. Neither dimension of a tested source nor success at coefficient3 supplies that constraint across coefficient primes.

No candidate new arithmetic relation survived that would justify launching an unrelated p>=5 source computation. The adaptive output is the exact repair-comparison data and the stronger separation theorem, not a claim that finite controls imply FIN. The accompanying class-projection comparison tests whether even the apparent support-based explanation survives known positive classes.

## 6. Verification and limits

All four arithmetic replays passed in fresh temporary directories, with their saved exact products byte-identical. The433 and mirror local-image checks include26 rational Hensel certificates. Prior source BNF, rank, saturation, global image and all-place membership inputs were retained rather than all recomputed. Field/norm implementations share PARI but use distinct exact norm and multiplication-determinant checks; independent Python code verifies residues, matrices and Hensel inequalities.

The root replay exposed a packaging issue: one runner rewrote a receipt containing elapsed-time logs. Arithmetic products were unchanged. Its old manifest is preserved, and the runner now writes a receipt only when explicitly requested. The current package is resealed; no frozen earlier return was edited.

This work has no formal proof-assistant verification or literature novelty claim. Publication preserves evidence and scope. FIN, ORDER9, Q36 and coefficient-prime coverage remain unchanged.
