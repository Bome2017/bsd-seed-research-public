# Sources, reading boundary and proof custody

## Published sources read in this run

1. K. Kato, *P-adic Hodge theory and values of zeta functions of modular
   forms*, Astérisque 295 (2004), 117–290.
   [Primary record](https://www.numdam.org/item/AST_2004__295__117_0/),
   [PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf).
   The preserved PDF and extracted text are bound in INPUT_BINDINGS.json.
   Read the cohomology conventions in §§8 and 12.2, the relevant parts of
   12.4–12.8, and the Euler-system application in 13.1–13.7 and 13.14.
   Printed pages 222, 226 and 234 were additionally rendered and visually
   inspected, so the integral/rational distinction does not rest on OCR.
   These are PDF pages 107, 111 and 119, counting from one.

   Theorem 13.4(3), not the rational display of 12.5(4), is the integral
   input. Section 13.14 supplies its passage to the modular zeta-image
   module; 12.6 preserves the actual smoothed-source inclusion. The
   theorem initially bounds the kernel of localization in degree two.
   INTEGRAL_MATCHING.md removes that local term on the selected component.

2. Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for
   elliptic curves*, J. Math. Soc. Japan 76 (2024), 855–919.
   [Published PDF](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en).
   Section 4's standing finiteness assumption was checked before deciding
   not to import its complex statement with that assumption deleted.
   The two-term representative here is instead derived from residual
   derived control and perfectness. This source does not prove the new
   residual nonvanishing premise.

3. Stacks Project, [Tag 066Z](https://stacks.math.columbia.edu/tag/066Z):
   bounded complexes with finite cohomology over a regular ring are
   perfect. [Tag 0FJH](https://stacks.math.columbia.edu/tag/0FJH): a regular
   local ring is a UFD. Both statements were read. The minimal-complex and
   unit-pivot arguments are written in this return.

Standard local Tate duality, the Tate-curve inertia description and the
potentially-good finite-inertia description retain their established
input grade. This run checks their application, including the monodromy
p-units and Frobenius signs; it does not reprove those general theorems.
The rank-two saturated basis and full residual image likewise remain
retained seed results, rather than fresh certificates from these checks.

## Preceding project inputs

- Weak-order deduction: lab d4d86454eedd7e3be2c0b398f4a8210fa4abc4a3.
- Foundation/source transport: lab 54637ae16c1856d065b8dada5aeab7c7ac33ced6.
- Integral point placement: lab f3b3ce88883969e37b48d4db34d5d843a4947283.

The critical proof files are copied without modification into context/.
The placement ZIP also retains the preceding sealed archives. Their
22-, 14- and 19-entry local manifests verified. The original submitted
criterion is preserved unchanged, including the citation corrected by
this review. INPUT_BINDINGS.json records every copied file and external
PDF/text hash. Hash verification is not mathematical verification.

The historical second-reader note pointed to the Kato citation issue;
the published pages were then checked directly in this run. No novelty
search or complete re-audit of the project's historical corpus is claimed.

## What was newly done

The algebraic criterion was checked, the integral image lifting was
written out, the coefficient-prime local correction was removed on the
target component, and the integral bad-local cones were checked. The
perfect-amplitude argument and their assembly are written deductions.
They are not independently certified merely because the exact arithmetic
controls pass. Residual derivative values were not computed.
