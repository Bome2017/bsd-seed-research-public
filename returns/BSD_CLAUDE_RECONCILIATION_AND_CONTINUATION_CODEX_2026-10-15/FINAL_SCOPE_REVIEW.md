# Final scope review before publication

2026-10-15. Reviewer: separate Codex worker responsible for the exact twist admission calculation and earlier coupling/source review.

**Verdict: root `REPORT.md` accurately separates the new arithmetic experiments from a seed bound, subject to the explicit grade clarifications below.** It does not claim FIN, ORDER9, Q36, a new seed-prime certificate, or a uniform arithmetic estimate. Its distinction between joint repair incompatibility and the ordinary ray pushout is mathematically essential and is preserved correctly.

This is a scope review, not another computation or literature audit. I read the current root report, `class_lift_review/COMPATIBILITY_REVIEW.md`, the relevant arithmetic-row map, `class_lift/mirror389/RESULT.md`, `class_lift/mirror389/ray/RESULT.md`, and the exact twist receipt. I did not rerun source engines, class-group certification, or the final packaging/upload checks during this review.

## Required grade clarifications

1. **Retain the saved certification grade accurately.** I initially inferred a GRH qualification from the `1613a1_grh` name and the then-current compatibility review. The root worker pointed out the later certification receipt, which I read directly: `certify_saved.gp` reads the saved BNF and calls `bnfcertify`; its output is `BNFCERTIFY_SAVED_GRH_BNF=1;MS=1295558`, with only the stack warning in stderr. Thus the suffix is historical. The accepted control retains complete saved BNF certification, not a fresh independent certification and not a current GRH assumption. The subordinate compatibility review's GRH wording needs correction; the root report itself was not overstating this point.

2. **State the local-image completeness input.** The negative arithmetic conclusion requires quotienting by the full local Kummer image, not just a sample-generated lower bound. The detailed review states how the expected dimensions are obtained and filled: dimension two at 3 and one at 389, under the retained descent injection and local dimension formula. The root summary should retain that dependency in one explicit sentence. Rational Hensel checks and higher precision authenticate the samples; they do not alone prove completeness of the local image.

3. **Remove a stale sentence in the subordinate mirror result.** `class_lift/mirror389/RESULT.md` currently says, after explaining the joint obstruction, “Consequently no ordinary ray-class order-nine lift is claimed.” Read literally, that conflicts with the subsequently completed ray calculation. Replace it by: “This joint obstruction is not a surviving ordinary ray-class obstruction. The separate ray calculation finds an order-nine lift before the local allowance and an order-three lift afterward.” Root `REPORT.md` already makes this distinction correctly.

## Claims supported at the stated grade

### Joint class obstruction

The domain of the repair-compatibility map is the intersection of class directions admitting the two marginal repairs. Its value lies in `U/(ker(G|U)+ker(L|U))`, and is independent of repair and lift choices. Vanishing is equivalent to a common repair. In mirror389 both repair kernels vanish and the actual difference `(1,2,0,0)` is nonzero. Thus the report may say this class passes each stated screen separately but fails the joint screen.

The four-row certificate is stronger evidence than dimensions alone: scalar and selected additivity rows together with an authenticated local row recover the class coordinate. Because these global rows are only necessary conditions, failure is an exclusion, while passing them is not automatically a global cohomology or Selmer certificate. The root report retains this distinction.

The full eleven-dimensional joint-kernel computation prevents attributing this particular result to removal of S-valuation directions. It does not produce a uniform seed bound. The rank-zero/bad-at-3 change of control domain is explicitly disclosed.

### Ray calculation

The actual presentation has a raw ray group, a quotient by cubes of its residue kernel, and a further quotient by the local Kummer allowance. Their reported structures and lift orders are different objects:

    R/(3 K_res) = C9 x C3^5,        lift order 9;
    R/(3 K_res + A_loc) = C3^4,     lift order 3.

The latter allows all ordinary global-unit repairs. The joint screen also requires global compatibility, which the ordinary ray quotient does not preserve. Root `REPORT.md` correctly refuses to identify the surviving joint obstruction with an ordinary ray boundary. No seed-theoretic inference follows from these fixed-field presentations alone.

### Scalar admission

The exact base-level modular-symbol sums for 6465c1 at discriminants -83 and -107 are both 20 in the pure imaginary eigencycle convention, or 10 in the historical twice-imaginary convention. Both have 5-adic valuation one. Their preregistered unit-twist requirement therefore fails.

The resulting status must remain `NOT_ADMITTED`, with neither scalar hypothesis confirmed or rejected. The root report correctly stops before interpreting a Gross outcome and retains the independent absence of a unit comparison between a primitive mod-5 eigenfunction and the geometric Fornea--Gehrmann normalization. Exact symbol row arithmetic and software replay do not amount to formal certification of the entire modular-symbol normalization implementation; the detailed receipt states its actual source grade.

## Claims not audited here

The nine-source custody count, ZIP/chunk byte counts, remote publication/readback and no-change claims are operational statements for the root worker's own receipts. This review does not independently certify them. Likewise, the historical theorem antecedents retain their existing grades; this review does not upgrade them.

After the textual clarifications above, no mathematical scope change to the root report is required. The defensible new contribution is an actual nonzero repair-compatibility example, its distinct raw-ray versus allowed-ray behavior, and a failed exact admission test that prevents a misleading scalar interpretation. The missing independent seed bound remains missing.
