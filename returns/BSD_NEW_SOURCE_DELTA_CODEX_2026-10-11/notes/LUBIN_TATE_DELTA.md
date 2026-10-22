# A genuinely later local formula for the thesis's explicit missing interface

Checked 2026-10-11. Scope: a bounded primary-source delta search, not a proof of the seed comparison or a review of every proof in these papers.

## Result

**NEW_RELEVANT_SOURCE_INTERFACE_AVAILABLE; THESIS_PERIOD_MATCHING_NOT_ESTABLISHED.**

The missing finite-character interpolation formula named on printed page 29 of Sangiovanni Vincentelli's May 2024 thesis is no longer simply absent from the literature. A December 2024 paper gives Artin-character interpolation for the Schneider–Venjakob Lubin–Tate regulator. A 2026 preprint extends the formula through an unramified variable. This makes a precise local comparison possible; it does not supply the thesis's specific period equality or a seed Euler system.

## Primary statements inspected

1. **Sano–Venjakob, _On Lubin-Tate regulator maps and Kato's explicit reciprocity law_, arXiv:2412.12429v1, 17 December 2024.** [Record](https://arxiv.org/abs/2412.12429), [Corollary 2.6.5](https://arxiv.org/html/2412.12429v1).

   Read §§2.1, 2.3, Theorem 2.6.3 and Corollaries 2.6.5–6 (printed pp.20–23). The setup is a fixed local field L, a Lubin–Tate character, and a crystalline lattice whose specified twist is L-analytic. Corollary 2.6.5 assumes the stated filtration bound and absence of Frobenius eigenvalues 1 and π_L^{-1} on Dcris(V*(1)). It interpolates at ρ χ_LT^j for every finite-order ρ. For conductor n>0 and j≥0 its factor is

   \[
   \Omega^j\mathcal L_V(y)(\rho\chi_{LT}^j)
   =j!\pi_L^{n(1+j)}\tau(\rho)^{-1}\varphi_L^n
   \sum_{\sigma\in G_n}\rho(\sigma)
   \bigl(\widetilde{\exp}^{*}(\sigma^{-1}y_{\chi_{LT}^{-j},n})\otimes e_j\bigr).
   \]

   The j<0 branch uses the logarithm; the trivial-character branch has additional Euler inverses. Its Gauss sum is explicitly defined in §2.3 through the Lubin–Tate Fourier kernel. The formula is not a statement that these factors are p-units.

2. **Venjakob, _On the interpolation property of Kupferer's Lubin-Tate regulator maps_, 2026, 24-page preprint.** [Author entry](https://www.mathi.uni-heidelberg.de/~otmar/papervenjakob/venjakob36-en.html), [PDF](https://www.mathi.uni-heidelberg.de/~venjakob/papervenjakob/LT-maxabelian.pdf).

   Read Theorems 1.1–1.3, the notation, and the recalled Theorem 2.1. Visually checked printed page 3. The tower is X∞=F∞L∞, with F∞/F unramified and L∞/L Lubin–Tate. Theorem 1.2 controls unramified-character specialization; Theorem 1.3 supplies the finite-character formula after that twist. The crystalline/L-analytic conditions, Frobenius exclusions and trivial-character Euler inverses remain explicit. It includes p=2, but that extension is not the seed's missing issue. The author entry supplies the year; the fetched PDF header has no date. HTTP Last-Modified was 30 January 2026.

## Exact comparison with the thesis

The thesis does not merely lack an unnamed logarithm. Page 29 asks whether its Ωχ^univ equals the period in the then-unavailable finite-character interpolation. Definitions 8.2.2.10–15 define Ωχ^univ using signed anticyclotomic formal-group points and normalized local resolvents, with an additional tame factor. The new papers use Ω, τ(ρ), π-powers, Frobenius and de Rham basis vectors. These are different definitions requiring a proved dictionary.

Neither later text mentions Sangiovanni Vincentelli, the thesis's Ωχ^univ, or its signed local-resolvent construction. Thus the defensible change is **formula availability**, not **period equality proved**.

A bounded next calculation can now write both sides for the same inert local field L=K_p (unramified quadratic over Q_p), the same formal group/uniformizer, reciprocity convention, tame character, and de Rham basis. It must compare the entire factor, not identify Ωχ^univ with τ(ρ) by naming both a Gauss sum. Retain conductor parity and the exact powers of p. The thesis itself has conflicting prose about the parity of its period valuation around Remark 8.2.2.13/Proposition 8.2.2.14; use the construction and underlying local result, not either prose sentence alone.

Before applying this to a non-CM seed class, separately check the L-analytic representation hypothesis. The theta normalization concerns a CM character component. One cannot automatically substitute the entire rank-two representation of a non-CM elliptic curve after extending scalars to K_p. The papers do not furnish that passage.

Even a successful local dictionary would leave the global theta/Eisenstein pullback, its actual seed projection, the Kato comparison, and the required nonvanishing/content estimate to prove. This lead is relevant because it replaces an explicitly missing source formula by an explicit available one. It is not evidence of a completed FIN arrow.

## New-to-record and custody

No title/ID hits for `2412.12429`, `Kupferer`, `LT-maxabelian`, or `Sano ... Venjakob` were found in the bounded Markdown search of BSD_BUILD_MAP, both 2026-10-11 OpenAI screen/push folders, and the lab's work/returns tree. This does not certify absence from every file on the computer.

Bindings: `sources/lubin_tate/FETCH_BINDINGS.json`. PDFs and extracted text are local reading copies, not recommended public redistribution. The two PDF SHA-256 digests are respectively:

- `88d5774abf108d5a2ee150e72f1333f6a7d7e82ef0967fdc1c39c56567812b97`
- `8c054277a257c18a8040509a4bd5a198649180f2805e606da4b69ec65a6e4ea6`

No jobs submitted, no messages sent to authors, no lab edits or pushes. FIN, ORDER9 and Q36 unchanged.
