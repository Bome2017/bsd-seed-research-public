# Three-way local-signature experiment: actual result

The same local arithmetic now separates the named known point and excess classes on the actual seed and on both full-image positive controls. An explicit false candidate also produces a nonzero local signature, but an actual affine norm rejects it first. Thus the supported classifier has two indispensable stages: global/all-local admission, then local Kummer comparison with the entire global point image.

| Tested input | Global admission | Local quotient test | What is established |
|---|---|---|---|
| mirror389 false repaired class | Fails actual affine norm at q=151 | Nonzero already at q=127 | Local detection alone would give a false positive |
| All point classes on 389a1; point columns on the other curves | Genuine Kummer classes | Zero by the point quotient, verified in every block | Calibration and representative invariance |
| Two admitted excess classes of 1913b1 | Retained exact norm and all-place certificates | Rank two at q=997 | Both known non-point directions detected |
| Two admitted excess classes of 28042a1 modulo its point | Retained exact norm and all-place certificates | Rank two using q=487,691 | Both known non-point directions detected |
| Actual seed beta1,beta2 modulo P1,P2 | Retained actual class certificates | Rank two using q=811,2767 | Both already-known seed 3-primary directions detected |

The seed matrix is [[0,1],[1,2]] over F_3, determinant 2. These entries came from literal arithmetic on the supplied field elements, not from the known Sha order. The point annihilator was formed without looking at the excess columns. The short row selection is retrospective within the predeclared scan.

The negative calibration is especially concrete. At q=151 its three actual values along a non-origin affine torsion line are 93,68,125. Their product is 15, and 15^50=32 mod151, a nontrivial cubic root of unity. Therefore the global affine norm is not a cube. The same candidate's nonzero local signature cannot be interpreted as Sha. See `PROOF.md` and `mirror389_false/GLOBAL_NORM_REJECTION.json`.

## What was executed

The original four-case contract selected the first 24 eligible good split primes per curve, with q<=100000 and 90 seconds per curve. The parent then requested the same negative calibration on the mirror false class; its scope is preserved separately. All five scans completed, giving 120 prime blocks. No class-number calculation or additional coefficient-prime computation was launched in this task.

`analyze_signatures.py` computes all annihilators and quotient ranks. `literal_replay.py` independently recomputes their values from exact rational-coefficient actual class polynomials, using Hensel leading units rather than the source exponent matrix. It passed all 120 blocks. `representative_controls.py` passed 6,912 unit-cube changes, 4,608 actual nonunit cube changes, 2,304 uniformizer changes and 1,584 point shifts.

A real normalization error was caught during replay: literal seed P2 vanishes modulo 2767 at root index7. Its q-adic valuation is 3 and its leading unit is 916; stripping that cube valuation restores the correct character. The corrected checker does this systematically. The initial field-variable export failure is retained in each applicable `failed_field_variable_export/` directory. Neither failure is hidden behind a successful exit code.

The parent's independent checker separately reproduced the 96 true-case blocks without producer libraries or source-coordinate matrices and checked its own representative changes. That review is in `../independent_review/LOCAL_REPLAY.json`; it is a separate scope from this lane's producer-side controls.

## An explanation, not another scan

The written argument `JOINT_EVALUATION_DENSITY.md` derives joint Kummer evaluation surjectivity from full GL_2(F_3) image and actual independence of the classes. It then applies Chebotarev to the rank difference between all local classes and the rational-point columns. This explains why a single local prime can be blind even to genuine excess.

For the seed's two point and two named excess directions, the conditional densities among split good primes are:

- rank-zero detector: 4177/6561;
- rank-one detector: 2336/6561;
- rank-two detector: 48/6561.

The parent sealed these counts before the independent exhaustive matrix enumeration, which matches them exactly. This is a theorem deduction on the known subspace, not an estimate fitted to 24 primes. No finite-sample confidence statement is made.

## Input grades and the remaining seed question

1913b1's complete source was certified in the preceding run, with an independent algebraic rank-zero bound and exact admitted classes. For 28042a1, class-source completeness remains unconfirmed after the preceding certification timeout; its explicit lower classes, local membership, rank-one bound and point saturation are separate retained inputs. The seed's ambient source completeness retains its prior grade. The present detector needs the named genuine classes and full point plane; it does not upgrade those completeness grades.

This supplies an arithmetic explanation of how known excess can be distinguished from points without an L-value or regulator quotient, and shows precisely why global admission cannot be skipped. It does not exclude additional classes or bound the dimension of a complete source: the joint-evaluation theorem accommodates any finite excess. The next seed-wide input must still control that complete admitted quotient across coefficient primes. More local successes on already-known columns cannot supply that upper bound.

FIN, ORDER9, Q36 and base-field coefficient-prime coverage are unchanged. This is a completed discriminatory experiment on the requested three categories, including the actual seed's known non-point directions, with a written mechanism explaining its local behavior.
