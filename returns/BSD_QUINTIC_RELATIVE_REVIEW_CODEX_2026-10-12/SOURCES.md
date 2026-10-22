# Sources, reading scope, and retained inputs

October 12, 2026. This return is a written derivation and desk review. It does not recertify the original large symbol computation, global residual image, saturated point lattice, or analytic rank certificate.

## Fresh primary theorem check

K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290, §14, especially Theorem 14.2(2), Corollary 14.3 and the following remarks, printed pp.234–236.

https://www.numdam.org/article/AST_2004__295__117_0.pdf

The definition of the Selmer group, the rational character part, the nonvanishing hypothesis, the finite abelian field hypothesis, and the conclusion for the full character-part Selmer group were read in the full primary text. Rendered printed p.235 was also inspected by the parent reviewer; the source agent inspected pp.234–236. The download is locally bound by SHA-256

`3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.

The browser fetch rejected the PDF because of its size; it was downloaded and rendered locally. The primary PDF and page images are in a local-only temporary cache and are not redistributed in the return.

Only the published character-part finiteness theorem is imported. The exact relative order, an integral unit normalization, a main-conjecture equality, and BSD are not imported. The application to the norm-zero part and the transfer decomposition are deductions proved in this return.

## Fresh analytic-normalization check

T. Dokchitser, R. Evans, H. Wiersema, *On a BSD-type formula for L-values of Artin twists of elliptic curves*, arXiv:1905.04282v2 / J. reine angew. Math. 773 (2021), §1.1, Notations 16–18 and Lemma 36(2)–(5).

https://arxiv.org/pdf/1905.04282

The separate analytic reviewer read the full-source text at these locations for real periods, finite differential factors, conductor/discriminant normalization and relative height scaling. The conjectural identification with Sha is not used. The finite Fourier identity is rederived directly in ANALYTIC_AUDIT.md.

## Project sources

The nine supplied files are preserved unchanged under `submitted/BSD_QUINTIC_RELATIVE_LEADING_TERM_2026-10-12/` and match the author commit `8365c394f1017280a6463d7f25afac2e321c0c25`. Its eight-entry manifest and five historical source-blob bindings are verified in INPUT_BINDINGS.json.

The input's baseline is `84a7333af028ff5bc694bc82bcb3c768a019f5c6`. Its cited tower audit supplies both primary 5-vanishing over Q and F and the full equality E(F)=E(Q). The latter retains the stronger residual-image assumptions explicitly stated in that audit. Its period audit supplies the original table normalization. The saved local reduction types and analytic rank remain retained inputs.

The supplied exact checker was read before execution. Its output agrees byte-for-byte with the supplied RESULTS.json; the replay is saved as checks/SUBMITTED_REPLAY.json. This checks exact formulas on the old table, not a fresh modular-symbol or Sha calculation.

## Review boundary

The analytical review and Kato source check were carried out by separate model agents in the same working team, followed by parent review. This is not independent human acceptance or machine formalization. No external research job, class-group computation, relative 19-descent, new coefficient-prime campaign, or expert-repository promotion was performed.
