# Sources, source grade and actual reading

## Primary paper

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024), 855–919.

- Published URL: https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en
- Local PDF: /Users/bsm/BSD_BKS_INDEX_PREFLIGHT_CHECK_CODEX_2026-10-01/sources/BKS2024_published.pdf
- SHA-256 is recorded in INPUT_BINDINGS.json.
- The live published-PDF fetch timed out. The existing local published PDF was read instead; it is not represented as a newly downloaded document.
- Read §2.1 (Betti and etale image lattices, primitive plus input, period and actual smoothing), Hypothesis 2.2, relevant §5.1–5.2 height definitions, §6.1 interpolation, and §6.3–6.4 Coleman/Rubin proof.
- Visually inspected printed pages 896 and 903 from the local PDF. Images are included under sources/. They show the root factor and the smoothed proof. Text extraction was used for the surrounding sections.
- Matching arXiv v2 HTML was freshly accessed: https://arxiv.org/html/1910.07404v2 . Published and v2 numbering agree for the interfaces used here.

The local/global Tate-duality and Euler-characteristic facts used in the review are explicit standard imports, not formalized or independently re-proved from foundational cohomology. The submitted argument's use of them was checked. BKS Remark 5.4 identifies its height with Nekovar's; a new full audit connecting every saved numerical height routine to that convention was not performed.

## Pinned project inputs

The lab baseline is 5f183c24999cadac414451ed3601db7e666b0bea on research/state-sync-2026-10-04.

- Weak order, d4d86454: context/WEAK_ORDER_PROOF.md.
- Foundation audit, 54637ae1: context/FOUNDATION_CHECK.md.
- Integral placement, f3b3ce88: context/MW_PLACEMENT.md.
- Integral criterion, b9c4e1d4: context/INTEGRAL_MATCHING.md and ALGEBRA_REVIEW.md.
- User submission: context/SUBMITTED_PROOF.md and USER_REQUEST.txt.

These keep their written-proof / retained-input grades. No full seed residual-image, basis or certificate replay was made here. The integral (p)-height-one inequality remains essential; the weak-order inequality alone is not enough.

## Actual numerical evidence used

INPUT_BINDINGS.json records original paths and copied hashes. Evidence files include the m=5 and m=25 symbol receipts, the old exact symbol adapter and extraction proof, the minimal-model p=17 regulator proof and PARI/Sage outputs, and the p=5 height calibration outputs.

- New execution: exact rational point arithmetic, finite-field point counts, local-log residues, downstream cofactor and determinant arithmetic.
- Re-execution: the old exact symbol-to-cyclotomic adapter on saved symbol outputs.
- Not re-executed: Arb coefficient generation, source modular-symbol interval evaluation, Sage/PARI height engines, any actual Kato evaluator.

## Collision check

The older BKS combination ledger already knew Rubin's formula and its Sha-finiteness hypothesis. The submitted zero/nonzero case split changes that particular interface; it is not a newly discovered source theorem.

The September 25 p=17 regulator report already required a depth-three / second-digit cyclotomic test. This return does not claim that threshold as new. Its fresh calculation is the actual local-log/cofactor vector and its use in the derivative's coordinate-content equation.

The October 6 one-sided-screen correction already rejected treating p=17's zero first digit as a disproof of cofinite success. The calculation here is consistent with that correction.

The fixed-lattice lemma is ordinary commensurability and compatible realizations, not a novel fixed arithmetic annihilator. It only constrains normalization support. No exhaustive literature novelty search was attempted.
