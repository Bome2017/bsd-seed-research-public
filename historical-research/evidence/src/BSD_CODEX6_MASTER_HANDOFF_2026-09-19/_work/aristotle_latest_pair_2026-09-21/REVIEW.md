# Aristotle A6 and B3: what is new and what it establishes

2026-09-21. These archives contain material beyond the A5 and B2 versions previously supplied. Original archives are unchanged. [Archive hashes and normalized file comparisons](ARCHIVE_COMPARISON.json) and [replayed checks](CHECKS.json) preserve the evidence. Attached directions were treated as document content, not authorization for a new arithmetic run.

## 1. Exact changes

| Return | Added content | Other changes |
|---|---|---|
| 9193…-6 (A6) | A preliminary 13-reduction note and ReductionAt13.lean | Summary extended; 23 files byte-identical to A5 |
| 5544… (3) (B3) | C11 numerical specification, two Lean modules, and a separate numerical pipeline with captured buckets/symbols: 14 files | Status and summary extended; 17 files byte-identical to B2 |

Top-level archive-directory names were normalized before comparison. The differences are not just archive renaming. Unchanged earlier proofs were not re-audited.

## 2. A6 supplies a formal version of the known reduction check at 13

[ReductionAt13.lean](A6/RequestProject/ReductionAt13.lean) constructs the reduced Weierstrass model, proves nonsingularity, and relates its affine solutions plus infinity to Mathlib's point type. It then gives
\[
\#E(\mathbf F_{13})=18,\qquad a_{13}=-4,\qquad13\nmid a_{13}.
\]

The source uses finite exact proofs, not an external numerical oracle. Independently enumerating all 169 affine pairs here gave 17 solutions and hence the same 18-point total; the model's discriminant is nonzero modulo 13. This confirms good ordinary reduction. The numerical point count was already present in B2; A6 adds the explicit formal identification with the curve's point type.

It contains no value of \(C_{13}\), no 13-primary vanishing result, and no threshold change. The word “planned” in its report does not authorize a local computation. The complete applicability chain of a hypothetical 13-primary proof is not audited by this finite-field check.

## 3. B3 is useful corroboration of the completed C11 calculation

The new [numerical specification](B3/ARISTOTLE_B_C11_SPEC.md) reports a distinct implementation using PARI prime traces, segmented multiplicative reconstruction, compensated floating-point bucket sums, and a cosine/Fricke transformation. Its [Lean assembly](B3/RequestProject/SeedC11Assembly.lean) and [value file](B3/RequestProject/SeedC11Value.lean) check the finite arithmetic applied to the supplied integer table.

Checks actually performed in this review:

* All 45 entries in the Lean denominator-121 table agree exactly with the [retained certified local table](../active_full_bsd/p11/run/SYMBOLS_m121.txt).
* All 110 unit-numerator entries in the supplied JSON agree with that same local table.
* Recomputing the cosine/Fricke transformation from the supplied bucket sums agrees at all 110 entries, after the documented global sign conversion. The largest observed distance to an integer is approximately \(8.19114\cdot10^{-11}\); this is a floating-point observation, not an interval bound.
* An independent exhaustive integer check verified the discrete logarithm weights, lower-level cancellation, 45-entry support, and residue.

The group sums are \((-110,-70,-10,102,-46)\), so
\[
2(-110)+3(-70)+5(-10)+6(102)+7(-46)=-190\equiv8\pmod{11}.
\]
Halving for the full real period gives \(4\bmod11\).

This corroborates the existing C11 result; it does not settle 11 a second time. B3 does not prove the arithmetic implication from the residue to Sha vanishing, but the local [11-primary theorem](../../audits/P11_PRIMARY_THEOREM.md) already supplies that implication at its retained grade. Its qualified conclusion is unchanged.

## 4. Exact replay qualifications

**Sign convention.** The supplied [stage3.py](B3/scripts/c11/stage3.py) uses the PARI sign and directly returns residues \(3,6,3\) at \(p=5,7,11\). The [README](B3/scripts/c11/README.md) instructs negation for the project's convention, giving \(2,1,8\). The JSON and Lean tables already use that latter convention. The raw script therefore does not directly print the report's \(C_{11}=8\) without this conversion. This is a documented normalization issue, not a discrepancy in the matched symbols.

**Numerical certification.** The archive does not contain its reported 6.9-GB prime-coefficient stream or full execution/validation logs. Its tail argument contains an unspecified asymptotic remainder, and its floating error estimates are approximate rather than fully enclosed. Therefore the supplied prose is not, by itself, an independently replayable rigorous numerical certificate. This does not undermine the separately retained Arb certificate, with which the supplied integers match.

**Lean boundary.** The three new Lean sources were inspected, and a comment-stripped scan found no sorry, admit, new axiom, unsafe, native_decide, or implemented_by declaration. No fresh Lean/Mathlib build was performed in this review. Clean builds and axiom sets remain producer-reported; the finite arithmetic was independently checked here. In particular the Lean value theorem proves a result about its integer table. It does not formalize the numerical identification of that table with modular symbols, the analytic \(p\)-adic L-function, or the Sha theorem.

**Resource boundary.** The reported 45 core-hours and 310-second downstream pass were not locally benchmarked. They describe the reported implementation, not a proven cost lower bound for other methods. No large coefficient computation, new prime test, or successor research branch was launched.

## 5. Effect on the current project

B3 provides useful alternative-implementation corroboration and formalization of the finite C11 arithmetic. A6 provides a formal prerequisite check at the next unsettled prime. Neither supplies \(C_{13}\), the required Stark ideal, a rank-one twist certificate, FIN, ORDER9, or Q36.

Preserve both as supporting evidence. The current threshold remains 1521 under FIN. Earlier 1089 wording and the statement that 11 is unresolved within B's historical files do not supersede the canonical master or the local 11-primary theorem.
