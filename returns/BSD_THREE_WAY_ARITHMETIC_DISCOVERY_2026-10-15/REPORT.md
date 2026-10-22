# Three-way arithmetic experiment: a predictive distinction, including the seed

Date: 2026-10-15. Parent lab return: `52c2b796933200f0ee3895a6a750089cd801be72`.

**Result:** the experiment now distinguishes a false partially admitted class, genuine excess, and rational-point directions using actual source arithmetic. For the false class we constructed a fixed degree-24 polynomial that explains which auxiliary primes miss it. Separately, two explicit point-relative signatures detect the seed's two known 3-primary excess directions. This is an experimental and written arithmetic result, not an upper bound on the remaining seed obstruction.

No new seed coefficient-prime vanishing is asserted. FIN, ORDER9 and Q36 remain open. The coefficient prime in this return is 3; the larger primes below are auxiliary places, not additional Sha-primary certificates.

## 1. The three cases are tested differently for a mathematical reason

| Actual input | Global affine-norm admission | Local signature after removing all rational-point images | Supported interpretation |
|---|---|---|---|
| Mirror's false class | Fails; fixed norm is noncube | Can be nonzero | A nonzero signature alone would give a false positive |
| Genuine admitted excess on 1913b1,28042a1 and the seed | Passes by retained exact cube identities and local admission | Nonzero; detects both displayed excess directions | Genuine classes outside the point subgroup |
| Rational-point directions | Passes | Identically zero | The signatures deliberately factor through the quotient by points |

The global gate and the quotient signature serve different purposes. A failed global gate rejects a candidate. A nonzero point-relative signature only proves excess **after** genuine Selmer membership has been established. We did not impose vanishing of the latter as a new Selmer condition.

## 2. A fixed arithmetic object predicts the false-class failures

For the mirror curve `y²+y=x³−21x−27`, use the retained false source

    a = G7 G8 G9 G10 G11².

Its exact affine-line norm b lies in the fixed degree-eight field

    B=Q[z]/(z⁸−54432z⁴+4992192z²−246903552).

The norm is constructed from the actual torsion incidence algebra, not inferred from observed prime outcomes. Two conjugate values of b determine all32 additivity equations for a split-prime block. Literal source identities supply the needed scalar-odd relation.

The arithmetic explanation is stronger than a fit to ranks. The conjugate norm classes form a nonzero, irreducible two-dimensional Kummer module over K=Q(E[3]). The nonzero claim is witnessed at the completely split prime18757 by

    b(8881)=4376,
    4376^6252=14673 !=1 (mod18757).

Thus adjoining their cube roots gives an extension M/K of degree9. We also eliminated z to obtain an explicit irreducible degree-24 polynomial, recorded in `frobenius/splitting_polynomial.gp.data`, whose splitting field is M. Its nine nonzero coefficients are supplied exactly.

Outside the stated finite exclusions,

    this false class passes a split-prime block
    iff the degree-24 polynomial splits completely at that prime.

Under the verified torsion-field and written Kummer argument, Chebotarev therefore gives an exact **relative density1/9** of misses among primes splitting completely in K. This is not a random-trial assumption or a finite stopping guarantee.

Before generating the new source-character rows, we sealed predictions for40 fresh eligible primes. The norm predictor correctly identified all40 outcomes. The false class survives precisely at

    51439, 56701, 58237.

It is rejected at the other37. The complete polynomial has24 roots at the three misses and6 at the other37; that last equivalent check is post hoc, not an additional held-out prediction. All72 earlier calibration cases also match.

This explains why equal map ranks and equal overlap dimensions previously gave opposite results: they had different Frobenius states in one fixed arithmetic extension. The field construction replaces that unexplained variation with a testable rule. It concerns this fixed false class, not the unknown Sha quotient.

## 3. The point-relative calculation works on the actual seed

For a good auxiliary q splitting completely in the 3-torsion field, reduce the specified field representatives at its eight roots and take cubic-residue characters. Compute the annihilator of the entire rational-point image **before** applying it to the excess columns.

With the seed columns ordered `(P1,P2,beta1,beta2)`, the fresh calculations give

    q=811:  (0,0,0,1),
    q=2767: (0,0,1,2).

Both rows are obtained by adding the first two root-character coordinates in the saved root ordering. Their excess minor has determinant2 modulo3. Consequently they detect both known excess directions while annihilating every combination of the two rational-point directions. In combination they distinguish all nine elements of the known two-dimensional excess quotient.

This assertion uses the retained genuine membership of beta1,beta2 and the full saturated point lattice. It does not require completeness of the currently generated ambient source. It establishes no bound on additional, unlisted classes.

The same calculation gives:

| Panel | Point dimension | Known excess dimension detected | Auxiliary detector places |
|---|---:|---:|---|
| 1913b1 |0|2|997 alone, two independent rows|
| 28042a1 |1|2|487 and691|
| Seed |2|2|811 and2767|
| 389a1 point control |2|0|All point-relative rows vanish|

The first24 eligible split primes were computed in each panel, with a separate24-prime false-candidate calibration. The false class already has a nonzero signature at127, but its actual norm is noncube at151. That is the needed negative control against misusing the second column of the first table.

The map is from an E[3]-Kummer lift modulo the global-point image to a corresponding local quotient. It is **not** localization of a nontrivial Sha torsor to H1(Q_q,E): that torsor localization remains zero.

## 4. Why a genuine class can be invisible at many auxiliary primes

The joint Kummer extension of r independent point classes and s independent admitted excess classes has kernel E[3]^(r+s), under the stated full-image hypothesis. The proof retains that this is a sum of simple modules; it does not assume the entire group algebra is semisimple.

At split good primes, the quotient-signature rank is the rank of a2-by-(r+s) Frobenius matrix minus the rank of its first r columns. Counting these matrices gives, for the seed's known r=2,s=2 span, the relative densities

    signature rank0: 4177/6561,
    signature rank1: 2336/6561,
    signature rank2:   48/6561.

Thus blindness at an individual auxiliary prime is expected even for genuine excess; it cannot be interpreted as absence of that excess. These are exact conditional asymptotic densities from the written joint-evaluation argument, not a completeness claim for the finite scan. `local_signatures/JOINT_EVALUATION_DENSITY.md` records the proof and exact enumeration.

## 5. One tempting refinement was actually tested and rejected

Requiring the affine norm's cube root to be integral or a unit does not separate points from genuine unit-supported excess. Exact computations on six named representatives confirm this. There is also a direct reason: the norm of a unit is a unit, so any cube root automatically has every finite valuation zero.

Moreover, multiplying each of five genuine representatives by1/2³ preserves its Kummer class but changes the norm root to s/8, with exact integral-basis denominator8. Root integrality is not even invariant under this legitimate change of representative. That candidate is excluded at its first failed step. We did not keep adding precision to it. A9-lifting/Cassels–Tate computation requires additional covering and global-lift data; no such value was computed in this return. Its status and precise prerequisites are in `secondary/`.

## 6. Verification and grade

The root worker separately reconstructed all120 local blocks from literal rational field polynomials, without importing the producer's row code, and checked9,864 representative/point-shift controls. One nonunit literal representative required Hensel lifting: seed P2 at q2767 has valuation3 and leading unit916. Accounting for that cube factor recovers the same character; the prime was not dropped.

A separate standard-library calculation checks320 affine-norm products and1,280 additivity triples across the40 fresh predictions. Independent finite algebra checks the incidence matrix, integer Smith factors, all48 GL2(F3) actions and both relevant irreducibility statements. Fresh Galois-group computations confirm full GL2(F3) for the five torsion fields. The source admissions, point ranks and saturation retain their previous grades; these are not silently re-certified by residue calculations.

The written proofs use standard Kummer theory, Chebotarev and the actual descent description in Schaefer–Stoll. No literature novelty or formal verification is claimed. A separate agent reviews the proof interfaces; neither that nor publication is independent human certification.

The discovery is specific: there is now an arithmetic explanation for the false-prime misses, and actual signatures distinguishing genuine seed excess from points. These are usable tests for future constructions. They do not yet supply the independent size bound needed to finish the seed.
