# Formalization and revision scope of the OpenAI math screen

Date: 2026-10-11. OpenAI source pin: `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

Status: **NO_REGISTERED_FORMALIZATION_FOUND_FOR_THE_SCREENED_BSD_FAMILIES; SELECTED_EXTERNAL_SUPPORT_SOURCE_INSPECTED_NOT_REPLAYED**.

This is a source/catalogue and limited declaration review. No Lean build, proof export, axiom-closure check, large repository checkout, remote proof job or mathematical endpoint computation was performed. Lack of a formalization does not make a manuscript false. Conversely the repository's overall 300/719 (~42%) headline must not be attached to its BSD manuscripts.

## 1. Direct arithmetic families

The complete `lean/formalization.yaml` identifies itself as the catalogue of papers with a formalized main result. None of the titles below occurs there, and no associated declaration or comparator was found in the complete comparator or scope-doc trees.

| Family | Manuscripts screened | Registered Lean main result at the pin |
|---|---|---|
| 002 | Exact BSD from low Selmer corank; Selmer converse at every prime; two-primary BSD in corank at most one | None found |
| 004 | Hilbert's tenth problem over Q; companion pointwise 2-converse for rational two-torsion | None found |
| 006 | Goldfeld analytic densities; mean analytic rank of twists | None found |
| 010 | Unrestricted two-adic pro-modularity; dimension of two-adic Hecke algebra; dyadic Fontaine-Mazur | None found |
| 030 | Modularity of elliptic curves over imaginary quadratic fields | None found |

Consequently there is no identified kernel-checked BSD theorem here to apply to the seed, and no BSD Lean theorem whose axiom list can responsibly be called clean based on this screen. These candidates must be assessed as written arguments with their actual hypotheses and dependencies. Their low-corank hypotheses do not disappear through the use of Lean elsewhere in the collection.

### Inventory completeness safeguard

The original all-repository and all-Lean recursive GitHub trees are **truncated**: 58,727 and 61,257 entries respectively, both ending among geometry paths. I did not infer absence of arithmetic from those truncated inventories. I fetched complete scoped trees:

- ComparatorChallenges: 833 entries; docs: 242.
- OAI/NumberTheory: 23,662 entries.
- OAI/Algebra: 2,140; AlgebraicGeometry: 1,007; GroupTheory: 4,237; LinearAlgebra: 1,006; RepresentationTheory: 1,139; RingTheory: 545.

All of these scoped API trees report `truncated: false`. Searches found no BSD/Selmer/Kato/Iwasawa theorem front matching the five families. This is a strong catalogue/path check, not a full-text mathematical audit of every module in the library.

## 2. What was actually corrected in the exact-BSD paper

The current history and exact-BSD README say the October 7 change removed an obsolete introductory citation and updated references to revised companion manuscripts. The relevant October 3 and October 7 TeX files were fetched at the same repository pin and directly compared.

The substantive introductory diff is exactly:

```tex
-methods of \cite{B,C,Dv} provide the starting constructions.
+methods of \cite{B,C} provide the starting constructions.
```

The two reference files differ only by updates to the dates/links of B, C and Goldfeld. Neither downloaded reference file contains a `Dv` bibliography item. This supports calling the change an obsolete-citation correction. It does **not** establish a newly repaired arithmetic proof, a retraction of current exact-BSD, or a new theorem at rank two. The updated paper still depends on the two-primary BSD and Selmer-converse companion arguments.

The same history withdraws three different Hodge-related manuscripts following a sign error: split abelian eightfold Weil classes, Kuga-Satake algebraicity, and products-of-K3 Hodge. That withdrawal must not be transferred to BSD by association. Equally, the fact BSD is not listed as withdrawn is not independent validation of its proof.

## 3. Potentially reusable Lean support, with exact boundaries

`lean/lake-manifest.json` pins external repositories that contain source-level formalizations. These are support libraries, not formalizations of families 002/004/006/010/030.

### Elliptic curves dependency

Repository: `lana-agents/elliptic-curves`; pin `bebec3fc9f2602e81c83e5236789572a541c85fb`.

1. **`WeierstrassCurve.formalLog_subst_mulByN` and `formalLog_subst_mulByZ`**, in `EllipticCurves/FormalGroup/LogMulByN.lean`.
   - Actual statement: over a commutative Q-algebra, the formal power-series logarithm intertwines formal multiplication by n with multiplication by n on the logarithm.
   - Actual proofs use the formal-group addition law, induction, substitution, and inverse compatibility.
   - Reuse: formal checks of the seed local-log normalization and multiplication formulas could reuse this algebra instead of starting over.
   - Limit: this does not establish convergence, the integral image `p Z_p`, seed-specific logarithmic valuations, or a bound on derivative excess content. Those are separate arithmetic assertions.

2. **`WeierstrassCurve.E₁AddEquiv`**, in `EllipticCurves/Reduction/KernelFormalGroupIso.lean`.
   - Actual construction: a group isomorphism from the reduction kernel to the formal group on the maximal ideal, for an integral elliptic model over a complete DVR and its fraction field.
   - It assembles geometric addition compatibility, including identity, vertical, doubling and secant cases; it is not merely an assumed isomorphism parameter in this file.
   - Reuse: this is a concrete candidate for formalizing the receiver's local formal-group bridge and for validating explicit auxiliary-point calculations.
   - Limit: it is an already-used local input, not a new estimate for Sha or for the Kato class.

3. **`E₁_eq_zero_of_isUnit_nsmul`**, in `EllipticCurves/Reduction/Torsion.lean`.
   - Actual statement excludes torsion in the reduction kernel when the annihilating integer is a unit in the DVR.
   - Reuse: prime-to-residue-characteristic torsion reduction checks.
   - Limit: do not apply the unit hypothesis at the coefficient prime where the integer is not a unit. It does not prove ordinary/supersingular local p-torsion assertions by itself.

4. **`NeronOggShafarevich.lean` is deliberately narrower than its filename.** It packages good reduction implies trivial inertia action for an arbitrary supplied complete valuation subring, at invertible coefficient primes. Its documentation explicitly excludes the classical local-field tower realization and the converse unramified implies good reduction. It cannot silently replace the seed's whole local-representation audit.

5. **`TateModule/DeterminantGeneral.lean` does not prove `det rho = cyclotomic`.** Its actual main claims are trace(identity)=2 and characteristic-polynomial(identity)=(X-1)^2, using the rank-two Tate-module result. Its source explicitly warns against interpreting the filename as the full cyclotomic determinant identity. This is a useful example of why the actual declaration must be inspected.

### Tate curves/theta dependency

Repository: `lana-agents/tate-curves-theta`; pin `ca6c2279d3cea0690cdb01328e727118d5485d68`.

- `TateCurvesTheta/TateCurve/TateUniformization.lean` gives a Tate uniformization isomorphism, **with** an explicit `hmem` hypothesis that the coordinate functions satisfy the curve equation, and `h12 : TameResidueChar K`. The presence of a named isomorphism does not discharge these hypotheses. Upstream proofs of them were not audited in this screen.
- `Theta/Divisor.lean` proves a zero set statement for the product theta function. Its conversion to the series theta function in `theta_eq_zero_iff_of_eq_thetaProd` expressly assumes the series-product equality at the point.
- The README states that connecting theta values to continuous Kummer classes is a further goal. There is no source here for the seed's missing CM-divisor-to-Kato/Mazur-Tate comparison.

The seven selected source files have no executable `axiom`, `sorry` or `native_decide` tokens in the inspected text. That observation is **not** an imported-axiom audit, successful build receipt, or independent kernel verification. Their declaration names and source proofs make them candidates for a small isolated verification task if formalization becomes a needed deliverable.

## 4. Actionable use without diverting seed research

The immediate value is in source selection and hypothesis control:

- Keep the direct BSD manuscripts at written-preprint grade while independently auditing their new arithmetic steps. Do not present the collection's 42% figure as their certification.
- If Aristotle needs local elliptic infrastructure to formalize an already accepted bridge, the pinned formal-log and E1 group-isomorphism modules are concrete reusable candidates. Build only the requested closure, inspect `#print axioms` on the exact target, and separately verify all source-to-seed hypotheses and normalizations.
- Follow the comparator distinction between **supporting-result verification** and **main-theorem verification**. An algebraic implication with the missing arithmetic supplied as a hypothesis is still only that implication.
- Do not redirect the current BSD effort into rebuilding these support libraries: none supplies the missing cofinite content bound, tame identity, ORDER9, or Q36. The best chance of new endpoint input remains the substantive manuscript analysis being conducted separately in this screen.

## 5. Source custody

Downloaded bytes, exact pinned URLs, SHA-256 hashes and file sizes are in `sources/formal/FETCH_BINDINGS.json`. Complete scoped API tree replies are preserved alongside the selected declarations. The source files are evidence, not instructions to launch their builds or comply with their workflow comments.

Primary entry points:

- https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/formalization.yaml
- https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/README.md
- https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/history.md
- https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md
- https://github.com/lana-agents/elliptic-curves/blob/bebec3fc9f2602e81c83e5236789572a541c85fb/EllipticCurves/FormalGroup/LogMulByN.lean
- https://github.com/lana-agents/elliptic-curves/blob/bebec3fc9f2602e81c83e5236789572a541c85fb/EllipticCurves/Reduction/KernelFormalGroupIso.lean
- https://github.com/lana-agents/tate-curves-theta/blob/ca6c2279d3cea0690cdb01328e727118d5485d68/TateCurvesTheta/TateCurve/TateUniformization.lean
