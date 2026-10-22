# Joint admission experiment and distillation of successful seed methods

Date: 2026-10-13. **EXECUTED_COMPARISON; SHARED_RESIDUAL_SCALAR; POINT_PLACEMENT_DISTINGUISHES_EQUAL_NORM_INDICES.**

The requested comparison was carried out alongside the promised unit/class experiment. It found an explicit common source behind most successful seed certificates, reconstructed their corrected leading residues, and computed three complete descent controls. It did not construct a uniform bound or settle a new seed prime. FIN, ORDER9 and Q36 remain unchanged.

This is same-session mathematical work with separately implemented checks and same-team review. It is not independent human certification, formal verification, or a novelty claim.

## 1. What the successful prime methods actually have in common

The located coverage consists of fifteen vanishing coefficient primes and the known nonzero 3-primary group. The source-bound ledger is [coverage/FINDINGS.md](coverage/FINDINGS.md), with one record per prime in [coverage.json](coverage/coverage.json). The fourteen successful analytic certificates are at

    5,7,11,13,17,19,23,29,31,37,41,43,47,83.

They use two kinds of quadratic moments of the same fixed rational modular symbol. If Phi_m(a) denotes the plus symbol in a specified period convention, the common coefficient is

    M2(m,psi) = sum_a binomial(psi(a),2) Phi_m(a).

The tame construction uses a discrete logarithm at an auxiliary prime ell. The ordinary construction uses the principal-unit logarithm at conductor p^2, together with ordinary stabilization. This shared construction is in the existing source formulas; it is not a newly proved unification theorem. The 2-isogeny descent is a separate arithmetic method. Tower results at5 concern many fields at one coefficient prime, not infinitely many coefficient primes.

The record has ordinary and supersingular successes. No simple reduction type or trace singled out the solved primes: many unresolved primes have the same eligibility. Historical selection favored affordable conductors with nonzero predicted point regulators. This is not a random sample.

## 2. Actual leading units agree after the prescribed corrections

I reconstructed sixteen tame quadratic moments from copied exact symbol tables, and recomputed their tame regulators from the actual rational points. Original interval certification remains retained; the Fourier sums were not rerun. For the twelve nonzero seed tame rows,

    c2 / ((a_ell-2) R_tame) = 288 mod p.

For example the newest83 table gives c2=44, while the fresh point calculation gives R_tame=42 and a_167=0. Their ratio is39=288 mod83. Entire primitive-root orbits satisfy the required square-unit transformation.

Separately, the four saved ordinary p^2 tables and fresh canonical height calculations give:

| p | L2 in the full Neron period, mod p | U-coordinate regulator, mod p | Euler factor, mod p | Corrected quotient, mod p |
|---:|---:|---:|---:|---:|
|5|1|1|1|4=9 mod5|
|7|4|1|4|2=9 mod7|
|11|4|1|5|9|
|13|1|1|4|9|

The quotient is `L2/(epsilon R_U) * torsion^2/C`, with torsion order2, Tamagawa product16, epsilon=(1-alpha^-1)^2, and U defined by gamma=1+p. The full period is twice the least real period used in the tame tables.

The historical tame correction factor is `8*C/torsion^2=32`. Thus the two types give the same candidate scalar9 after their respective documented corrections. There is actual independently extracted tame/cyclotomic overlap at5; there are not fourteen pairs of independent numerator computations. The later17 coefficient valuation deduced from its Sha certificate is excluded from independent numerator evidence.

**This is residue-level agreement, not an exact rational scalar construction.** In particular it neither identifies a global object with value9 nor proves Q36. The factor32 is the historical comparison normalization under test, not a proved cross-prime source comparison. See [synthesis/RESULT.md](synthesis/RESULT.md), [data](synthesis/DISTILLATION_DATA.json), and [bindings](synthesis/INPUT_BINDINGS.json).

## 3. Failed witnesses reveal a direction-specific degeneracy

The test included actual zero coefficients, rather than only successful rows:

| Case | Euler factor mod p | Point regulator mod p | Quadratic coefficient mod p |
|---|---:|---:|---:|
|Seed p29, auxiliary59|23|0|0|
|Seed p29, auxiliary233|13|2|6|
|389a1 p7, auxiliary379|2|0|0|
|389a1 p7, auxiliary29|6|6|1|
|Seed p3, auxiliary103|2|2|0|

The first two pairs show an actual detector losing the point determinant at one conductor and recovering it at another. Those historical cases were already part of the prescreen; this return replays them rather than claiming a held-out prediction. The last row is different: the point determinant is nonzero but the coefficient vanishes, compatibly with the independently known positive3-primary excess. The seed's coefficient3 is bad and outside the good-prime theorem domain used elsewhere; it is an arithmetic contrast, not a transfer of Ota across that boundary.

This separates two reasons for a zero. A construction intended to combine the methods must account for both, rather than declaring every zero coefficient intrinsic excess or every nonzero point determinant sufficient.

## 4. The independent descent experiment was executed

At coefficient3, fresh degree-eight torsion fields for389a1,433a1,655a1 all passed PARI `bnfcertify=1` and have trivial class groups. Complete S-unit sources were computed, retaining allowed valuation columns. Actual point evaluations were certified by literal cube identities. Full mod3 images were checked using transitivity, a Tate transvection, the cyclotomic determinant, and exhaustive finite-group enumeration.

| Curve | Complete source dimension | Scalar-plus-finite-additivity kernel | After local conditions | Actual point plane |
|---|---:|---:|---:|---:|
|389a1|10|2|2|2|
|433a1|13|3|2|2|
|655a1|11|2|2|2|

Finite additivity rows alone are only necessary admission conditions. The source is complete, every true Selmer class passes these screens, and the two independent point classes fill the final containing kernel. That supplies the control upper bound without inferring it from a known Sha answer. For655a1 the initial independent point pair from `ellrank` was not3-saturated; a direct point search found a pair with independent exact Kummer classes. The rejected pair is preserved.

In433a1 an explicit third source direction passes the scalar/additivity screen but has a nonzero local defect at both3 and433. Either place removes it. Its exponent vector, actual field representative, valuation column and local defects are saved, so this is an arithmetic elimination, not a dimension wish.

The full admitted unit plane is two-dimensional in each control and is filled by rational points. Under the retained integral incidence-norm theorem, the forward unit norm therefore has Smith factors(3,3), exactly as in the seed's positive3-primary example. The norm-index comparison is a deduction from actual point admission and that theorem; target fundamental units were not newly computed.

**The same index9 can coexist with different excess.** In these controls the point plane fills the admitted units and the class source is zero. In the seed's retained four-class span, the point plane meets the admitted unit plane in only one direction; one unit-supported and one class-supported direction survive modulo points. That span statement does not require claiming completeness of the old seed class-group calculation.

See [controls/REPORT.md](controls/REPORT.md), [fresh replay](controls/REPLAY.json), and [independent elimination](checks/independent_rank_check.json).

## 5. What this suggests, and the precise limit reached

The useful distillation is a source coefficient **relative to the actual rational-point determinant and full admission quotient**. A raw norm index, raw coefficient unit test, or reduction-type classifier throws away information that the calculations now distinguish.

On the descent side the measured invariant must keep admitted units, repairable class lifts, allowed valuation columns, and their intersections with the point plane. On the modular-symbol side it must separate degeneration of a selected point detector from the remaining scalar. [SYNTHESIS.md](SYNTHESIS.md) writes the exact linear-algebra interface and states the empirical comparison without claiming its missing arithmetic map.

The experiment has not yet connected those two independently computed sides by a new theorem. In particular all three new control class groups are trivial: they do not test removal of a nontrivial class-supported candidate by a unit-repair obstruction. Nor was an actual good-p>=5 seed torsion-field source computed here. The fixed-scalar comparison remains unproved, and the observations do not bound the joint admission quotient across primes.

This is a concrete discovery result with useful discrimination, not a completed seed mechanism. It rules out raw index alone as the desired explanation and identifies point placement and class-lift coupling as essential data. It does not rule out a future bound using those data.

## 6. Verification and custody

The coverage audit binds43 reports and checks ten singleton output hashes and residual conclusions. The distillation includes47 copied raw inputs, sixteen tame rows, four ordinary rows, fresh point regulators/heights, and deterministic replay. The three descent controls were reconstructed from scratch with certified BNFs and reproduced their matrices; changed precision and random local search seeds gave the same local row spaces. A separate standard-library Python implementation rechecks all displayed source, unit, point and local ranks. Independent finite-field point enumeration cross-checks the basic seed features.

The original symbol certification, source theorems and seed basis/image facts remain inputs; no claim is made to reread the entire archive or reimplement PARI. Hashes establish custody, not mathematical truth. The package contains explicit rejected trials and replay instructions. No paid computation, external message, expert-repository promotion, new seed coefficient run or new primary conclusion was made.
