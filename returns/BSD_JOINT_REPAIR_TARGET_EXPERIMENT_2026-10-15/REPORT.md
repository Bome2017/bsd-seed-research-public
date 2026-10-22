# Joint repair experiment: arithmetic values, genuine unit excess, and point occupancy

Date: 2026-10-15. Parent return: lab commit `f4f96e41ff8d5a60dfd49c17a7d2b654e8a20ec9`.

**Result: the concrete experiment was executed. It distinguishes arithmetic that a rank-only account misses, and constructs two positive unit-excess controls. It supplies no independent upper bound for the seed. FIN, ORDER9 and Q36 remain open.**

This continues the requested discovery process. It does not restart a singleton seed-prime certificate or present an additional equivalent criterion as a bound. All coefficient-prime calculations here are at 3. The new controls have ranks zero and one; they are not evidence for a theorem requiring rank two and coefficient prime at least 5.

## 1. The test that was actually run

The proposed arithmetic object is the joint global/local repair obstruction on an ordinary class lift, with the genuine unit contribution and rational-point image retained separately. The question was whether its behavior is determined by the ranks of the two maps, whether a small number of new split-prime blocks reliably detects it, and whether admitted units can be identified with point directions under good reduction and full residual image.

Before new residue calculations, `heldout/PREDICTIONS.md` fixed ten sources, twelve split primes per source, the selection rule, the protected point/seed classes and the failure tests. Selection used splitting, reduction and definedness of source elements, not the resulting row ranks. The panel consists of eight prior rank-two controls, the rank-zero mirror of 389a1, and the actual seed's known four-class span at 3. The seed's cached complete-source grade remains conditional; the four literal classes are protected independently of that completeness claim.

PARI generated 120 new split-prime blocks. A separate standard-library implementation recomputed the field-root identities, elliptic addition, cubic residues and all rows from the exported exact source polynomials. The analysis compared all 120 singles and all 660 unordered within-source pairs against three local aggregates.

With **all** local conditions, every initial single and pair recovers the corresponding saved kernel. That is 780 finite-panel comparisons, not a uniform theorem. All four genuine seed classes survive every new block, as they must.

## 2. A prospective follow-up breaks the tempting generalization

The initial result was not accepted as a law. An older mirror block at 127 already failed. A separately sealed extension therefore calculated the next 60 eligible mirror split primes after 16981, without rank-based selection.

Six allow an unwanted class to survive the single-block screen:

`19219, 22699, 23671, 26431, 33751, 45841`.

The first failure and a passing prime have **identical rank data**:

| Mirror auxiliary prime | Global unit rank | Local unit rank | Joint unit rank | Dual overlap | Separately repairable class dimension | Mixed obstruction rank |
|---|---:|---:|---:|---:|---:|---:|
| 19219 | 3 | 4 | 4 | 3 | 1 | 0 |
| 18757 | 3 | 4 | 4 | 3 | 1 | 1 |

At 19219, the class lift has a common unit repair `(2,2,2,2)` in the bound unit coordinates. A sparse surviving source exponent vector is

`(0,0,0,0,0,0,1,1,1,1,2)`.

It has zero valuation and zero defect at every retained local place. A fresh row at 17791 evaluates to 1 on it and rejects it. Thus it is a false survivor of the incomplete global screen, not a genuine Sha class. Literal rows, repair vectors and source bindings are in `heldout_analysis/MIRROR_EXTENSION.json`.

All fifteen pairs formed from the six failing blocks, and even their six-block union, leave the same class line. Those combinations were selected after seeing the single-block outcomes and are explicitly labelled post hoc. They refute an unqualified arbitrary-two-prime rule without changing the original sealed panel result. The next larger detecting prime is 19483; its exported row evaluates to 1 on the same vector.

The same global repair `(0,1,2,2)` and local repair `(2,2,2,2)` work at both comparison primes. Their difference `(1,2,0,0)` lies in the global unit kernel at 19219, spanned by `(2,1,0,0)`, but not at 18757, whose kernel is spanned by `(1,0,0,0)`. This identifies the changing arithmetic datum explicitly.

The experimental conclusion is precise: **the actual mixed arithmetic functional, not the marginal ranks or the overlap dimension, determines the class rejection.** This rules out that rank-only shortcut. It does not rule out an arithmetic estimate for the functional.

## 3. Two actual positive controls test the unit component

The bounded primary-data search found no rank-two row with predicted Sha divisible by 9 below conductor 500000. That is only a database-selection fact. The experiment therefore explicitly changed rank, retaining good reduction at 3 and full mod-3 image. Analytic Sha labels selected candidates but did not enter the proofs.

| Curve | Fresh algebraic rank | Source completeness | Independently authenticated classes | Consequence under the descent imports |
|---|---:|---|---|---|
| 1913b1 | 0 | `bnfcertify=1`; trivial class group | Two independent actual global units | `Sel_3 ≅ F_3²`, hence `Sha[3] ≅ F_3²` |
| 28042a1 | 1 | Certification timed out; no complete upper claim | Two independent actual units and the rational point | `dim Sel_3 ≥ 3`, hence `dim Sha[3] ≥ 2` |

These are software-assisted arithmetic deductions, not formal verification or claims of literature novelty. Neither asserts the order of the whole 3-primary group.

The global admission was checked beyond finite split-prime rows. Each surviving representative has a literal cube root for its actual affine-line norm in the dual degree-eight field. A separate determinant computation checks those norm identities. Scalar/source bindings are exact cubes. Local samples have rational Hensel certificates and sufficient precision to preserve their cube classes, and they span the independently determined local-image dimensions. Algebraic 2-descent establishes the rank bounds without an L-value.

For 1913b1, the independent review found that scalar compatibility plus complete local conditions already bounds the source kernel by two; finite additivity rows are unnecessary for that upper bound. Exact affine norm cubes prove that the two surviving elements really belong to cohomology and Selmer.

For 28042a1, unconfirmed BNF completeness is not used for the lower bound: exact residue independence and literal global/local membership suffice. Its computed class placement of the point retains the conditional source grade. The unconditional lower-bound observation is that two explicit unit representatives survive independently modulo the rank-one rational-point subgroup.

The primary admission theorem is Schaefer–Stoll, Corollary 7.9, Proposition 7.10 and §10.1 of [How to do a p-descent on an elliptic curve](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf). Source hypotheses, the incidence algebra, coordinate transport and the separate review are retained in `source_screen/`. Completeness, explicit membership, rank and full-image checks are distinct inputs, not interchangeable certificates.

These controls show that good reduction, full residual image and even trivial class group do not identify admitted units with rational-point directions at 3. Any proposed bound for this descent mechanism must control that unit quotient as well as repaired class directions. The conclusion is scoped to these actual curves and the coefficient-3 mechanism.

## 4. Other local places cannot silently disappear

On the initial panel, local 3 alone and all local places give the same ordinary-class admission. The stronger claim that local 3 can replace every local condition is false. It leaves a valuation-supported direction in all 78 mirror single/pair cases and in three cases for 1246c1. The missing conditions at 389, or at 2 and 89 respectively, remove those directions.

These are valuation-supported failures, not failures of the narrower ordinary-class statement. They are exported with actual exponent vectors and place-by-place defects.

## 5. What this changes for the seed research

The experiment now supplies three different arithmetic outcomes with literal representatives:

1. A false class survivor whose rejection depends on a specific mixed residue value, even when all rank data agree.
2. Genuine unit-supported excess under good reduction and full residual image, certified independently of an analytic Sha prediction.
3. The seed's retained excess at 3, whose unit and class components both remain visible and protected.

This is a stronger test bench for an independent arithmetic bound than a list of vanishing controls. A candidate explanation must reproduce all three outcomes. It cannot infer vanishing from class-group triviality, marginal rank, or the successful first twelve split primes.

The unproved step remains an **upper estimate for the actual point-relative unit kernel and admitted class quotient for the seed across coefficient primes**. This run neither supplies that estimate nor shows it impossible. It does not justify calling the source framework a demonstrated route to FIN. No original seed prime was newly settled.

## 6. Verification and custody

The independent field/elliptic/residue replay passes all **180 blocks, 1440 torsion-point instances, 16992 cubic symbols and 5760 additivity rows**. The 180 blocks comprise the original 120 and the separately sealed 60-prime extension. Exact point-relative linear algebra produced 2340 initial profiles; extension profiles and literal counterexamples are separate.

Rejected runs are retained: GP stack reconfiguration stopped initial file execution; a field-variable serialization bug produced invalid source JSON; a dual-field variable-priority error affected the first norm run. Accepted outputs were rerun and checked. The serialization repair did not change a single arithmetic block. These are corrected implementation failures, not mathematical evidence.

Hashes bind inputs and outputs. They do not certify the descent theorem, the inherited seed computations or the mathematical deductions. The separate review is an additional AI-assisted source/code/arithmetic check, not human certification. Endpoint records remain unchanged.
