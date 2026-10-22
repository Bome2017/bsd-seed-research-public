# Local detector review and an executed seed comparison

2026-10-13. **LOCAL_DETECTOR_SUPPORTED; SEED_LOCAL_TARGET_WITH_ZERO_GLOBAL_IMAGE_COMPUTED.**

Pro's one-place nontriviality proof and degree-five splitting-field argument survive this separate-agent review under their stated retained inputs. I also executed a bounded comparison on the actual seed. It finds a nonzero local quotient outside the global point image at auxiliary prime 1783, even though the separately retained seed 5-primary certificate rules out a nonzero global Selmer class with that signature.

This supplies a concrete contrast between a local target and the image of globally admissible classes. It is an experimental result, not a new seed upper bound. FIN, ORDER9, Q36 and coefficient-prime coverage are unchanged.

## 1. What Pro's calculation establishes

The reviewed return is pinned to lab commit `0048c241f4737ddc5b6d4044a04599d3910a96da`. All eight remote added files match the uploaded packet; its seven manifest entries verify, and its executable output replays byte-for-byte.

Independent exact arithmetic reproduces the signatures at the selected place above 11:

| Representative | valuation mod 5 | leading-unit discrete logarithm mod 5 |
|---|---:|---:|
| epsilon | 0 | 4 |
| alpha_11 | 4 | 0 |
| f(P1) | 0 | 0 |
| f(P2) | 0 | 0 |

The determinant is 4 modulo 5. Under the retained rank, saturation and all-place Selmer-membership inputs, this proves the two classes independent in the dual-isogeny Sha quotient. A class-group or fundamental-unit computation is unnecessary for this lower bound. The previous complete Selmer calculation remains necessary for the upper bound identifying the quotient with these two directions.

I also independently verified irreducibility modulo 11 of

    t^5 - 5t^3 + 5t - 46846,

and the exact fifth-root identity in its compositum with Q(sqrt(43737)). Restriction/corestriction through the quadratic extension justifies descent of splitting to the quintic field. The supplied nonzero covering has period, index and minimum splitting degree all equal to 5. No explicit projective coordinates for a quintic-field point were computed.

[AUDIT.md](AUDIT.md) records the proof review and its retained dependencies. This is same-team written review with independently implemented arithmetic, not human or kernel certification.

## 2. A new comparison on the actual seed

Before calculation, the scan protocol fixed coefficient prime 5, ascending good auxiliary primes q <= 30000, the condition v5(#E(F_q))=1, and a stop at the first place where both saturated basis points are locally 5-divisible.

It stopped at **q=1783**:

    #E(F_1783) = 1730 = 5 * 346,
    P1 mod 1783 = (535,1095) = [5](159,1682),
    P2 mod 1783 = (1172,1589) = [5](289,63).

For R=(3,872),

    [346]R = (1591,1089) != O,
    [5](1591,1089) = O.

PARI and a separate standard-library Python implementation agree. The latter independently counted and enumerated all 1730 points, verified the displayed group-law identities, and reproduced all 47 admitted scan rows through the first hit.

Good reduction and q != 5 identify E(Q_q)/5 with E(F_q)/5. Retaining the full rank-two basis and rational torsion of order two therefore gives

    (E(Q_1783)/5E(Q_1783)) / image(E(Q)/5E(Q)) = F_5.

But the retained seed certificate already gives Sha(E/Q)[5]=0. Consequently this local target's nonzero classes do not extend to globally admissible 5-Selmer classes. This last assertion uses that existing certificate; the scan neither reproves it nor computes a new Selmer group.

The two cases now separate the operations explicitly:

| Case | Local class outside global point image | Globally admissible class with nonzero signature |
|---|---|---|
| Positive control, coefficient 5, place 11 | Two explicit directions | Yes, by the retained descent theorem and representatives |
| Actual seed, coefficient 5, place 1783 | One explicit direction | No, using the retained independent 5-primary certificate |

These are not identical descent representations: the control uses a rational isogeny, while the seed uses full multiplication by 5. The comparison tests the local-target/global-admission distinction, not an identification of their Selmer groups.

[Seed computation and proof](seed_probe/RESULT.md) · [sealed protocol](seed_probe/SEED_PROBE.md) · [exact output](seed_probe/RESULT.json).

## 3. Transfer and the next discriminating question

The seed's full residual image does permit a family of local detectors. The joint-cocycle/Chebotarev proof in [TRANSFER_ANALYSIS.md](TRANSFER_ANALYSIS.md) shows that suitably chosen good places jointly detect every nonzero Sha[p] class. This revisits a mechanism already present in the pencil and cyclic-detection records; it is not a new upper-bound theorem. No finite scan certifies completeness of that detector family.

The next substantive arithmetic question is therefore about the **image**: what explicit global compatibility prevents a local signature from extending to an all-place Selmer class on the seed, while admitting the two control signatures? The new q=1783 result is an exact known-zero test for any proposed compatibility rule. Pro's two explicit classes are exact nonzero tests. A candidate rule must distinguish them without taking the known Sha answers as inputs.

This return has not constructed that compatibility rule. It has executed and verified the seed-side comparison needed to test one. Merely producing more local targets, or repeating joint detection, would not answer this question or supply the missing cofinite bound.

## 4. Reproduction and source boundaries

[REPLAY.md](REPLAY.md) gives the commands and receipts. [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) binds the retained seed data and prior collision records. The supplied packet is preserved unmodified in `input/`.

Fresh work here: exact local signatures and compositum audit; bounded seed reduction scan; independent replay of the seed finite-field arithmetic; explicit full-image detector comparison with old records.

Retained rather than recomputed: global rank and saturation, all-prime residual image, the original all-place isogeny descent membership, the earlier seed 5-primary certificate, and the previous covering smoothness identification. No new numerator, regulator or seed Selmer computation is claimed.
