# Complete-source common-point kernel experiment

Date: 2026-10-15. Status: exact arithmetic and full-source matrix certificates under the retained source grades. No new coefficient-prime result or uniform bound.

## Result

The common-point detector was applied to the full supplied source, with the known excess columns removed from the working inputs. It has zero kernel modulo points on every displayed scalar-compatible source after a small prefix of actual residue blocks. This is a complete-source claim for the three certified controls, and only a displayed-source claim for seed3 and28042a1.

| Case | Ambient source | Scalar-compatible source | Exact global norm kernel | After local admission | Point dimension | First prefix with injective raw evaluation on whole scalar source |
|---|---:|---:|---:|---:|---:|---|
|1913b1|9|3|2|2|0|997|
|389a1|10|4|2|2|2|73,151|
|433a1|13|6|3|2|2|223,967|
|Seed3, source-conditional|15|4|not recomputed here|4|2|811,1213,1543|
|28042a1, incomplete source|13|4|not recomputed here|3|1|487,691|

The exact global maps in the first three rows come from the parallel actual affine-norm calculations, with positive cube roots and independent negative residue ranks. They are imported as complete kernel matrices in the original G coordinates. The fresh433 local certificate authenticates the local rows; those rows are byte-identical to the prior ones, so the older local precision caveat is addressed by that separate new certificate, not by matrix agreement alone.

On the whole scalar source, M takes values in the eight-coordinate multiplicative residue space. It is not declared to take values in the two-dimensional elliptic local Kummer space before global admission. Its restriction to genuine Selmer classes has that interpretation. This keeps the false-source columns in the containing-space test without misclassifying them as E[3] cohomology.

These calculations distinguish three different facts: a full global norm kernel, the further Selmer local conditions, and a detector kernel after quotienting by rational points. Detector rows are never imposed as new Selmer conditions.

## A whole-source certificate, not a supplied-class rank

Let A be the displayed F_3 source, U a necessary-admission containing space, W the full point image and M the stacked source-evaluation map. The common-point invisible space is

    Z = {u in U : M(u) is in M(W)}
      = W + (U intersect ker M).

The equality follows by subtracting a single point representative. Thus Z=W can be checked using all source columns, without supplying a list of true excess classes. A sufficiently small/zero kernel is not absence of the detected image: genuine excess can remain and be detected injectively.

The code reconstructs scalar, global-necessary, scalar-plus-local, joint-necessary and available exact-global kernels from their equations. Each stored prefix includes every invisible source vector, separate versus common-point kernel dimensions, and the raw evaluation kernel. Unit/valuation/class support is retained for residual vectors. Separate quotients permit different point repairs at different places; the common quotient requires one repair at all places.

For the exact-global-and-local kernels, and separately for the prior joint-necessary kernels, exhaustive enumeration of their coefficient combinations agrees with the computed common-point kernel. The largest such containing space here has dimension four. No known-class column enters this step.

Only after KERNEL_RESULTS.json is written and hashed does compare_holdout.py read the supplied class lists. Every supplied span then agrees with the recovered joint kernel. This is a retrospective withheld-column experiment, not a claim that the workers were historically unaware of the results. On1913 the complete containing source and independent actual membership together certify that no extra unlisted Selmer direction remains. On the seed and28042, that conclusion is restricted to the displayed source and does not repair missing ambient completeness.

## The concrete433 residual class

The exact global norm kernel has one more direction than the point plane. Its source exponent vector is

    (1,2,0,2,1,2,0,0,1,0,0,0,1).

It is an actual global cohomology class by the independent norm calculation. It is not a Selmer class: the authenticated local maps at3 and433 reject it.

The newly sealed auxiliary scan also gives a useful point-repair comparison. At223 its local value equals the Kummer image of P1, with unique point coefficients (1,0). At967 it equals that of P2, with coefficients (0,1). Each separate quotient is therefore zero, but no common point explains both places. The common-point detector has zero kernel modulo W on the whole three-dimensional global norm kernel after these two places. It is essential not to call this detected class Sha; it fails the Selmer local conditions at the bad/coefficient places.

This completes an actual residual-kernel test: a globally admitted non-point class survives separate good-place quotients but is exposed by point-repair incompatibility, and its non-Selmer status is determined independently by local admission.

## Fresh arithmetic and checks

For433, SCAN_CONTRACT.md predeclares the first six eligible good split primes at most100000, with source factors units and no class columns in selection or evaluation. The sealed run returns223,967,1663,2659,3163,3463. It reads the original ordered generator list G unchanged. The90-second GP alarm and1GB stack limit are explicit; the run took less than a second and did no BNF computation.

replay_433_literal.py independently evaluates all13 literal source polynomials at all eight roots for all six primes:624 exact character evaluations. It imports no producer library or true-class matrix. It checks field roots, curve equations, order-three torsion and Hensel leading-unit character arithmetic. Every row matches. No nonunit literal representative occurred in these six blocks.

All other blocks are bound saved arithmetic from the preceding packet:24 blocks for each of1913,389,seed3,28042. Their original literal replays and source interfaces retain their grades. This run does not label those reused blocks as newly computed.

## Limits

An injective detector on a certified complete U/W controls its invisible kernel. It does not force U/W or Sel_3/W to be zero;1913 is a complete countercontrol with two genuine detected excess directions. The whole-source scalar injection also includes false global source classes, so its target dimension must not be identified with Sha dimension.

The seed and28042 source qualifications remain unchanged. No additional seed prime is settled. The missing cross-prime/image bound is not supplied by these fixed-prime source certificates. FIN, ORDER9 andQ36 remain unchanged.

Files: KERNEL_RESULTS.json, ADMISSION_FILTRATION.json, HOLDOUT_COMPARISON.json,433_COMMON_REPAIR.json andFRESH_433_LITERAL_REPLAY.json. Exact norm/source interfaces are bound in exact_global/ and INPUT_BINDINGS.json. RESUME.md gives the replay order.
