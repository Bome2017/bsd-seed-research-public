# OpenAI overlooked-source screen

Date: 2026-10-11. Repository pin: `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

## Result

**No additional OpenAI manuscript has passed an applicability screen as a new source of the seed's missing upper control or exact arithmetic comparison in this pass.** One previously catalogue-only family was checked beyond its abstract; its actual global applications do not supply that control. This is a bounded search result, not an assertion that the entire collection is irrelevant or that every proof has been read.

All OpenAI mathematical assertions below are assertions of released model-produced manuscripts. This screen is not independent validation of their main theorems.

## New-to-reading-record source actually inspected

[The p-adic section conjecture, October 6, 2026](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-p-adic-section-conjecture-October-6-2026).

The prior October 11 screen contained the catalogue listing and repository inventories. A targeted search of its narrative Markdown, excluding the catalogue, and of the subsequent CM comparison return found no discussion of this family. Its source files were not among the previously fetched arithmetic manuscripts. This establishes **previously unexamined in those two returns**, not never mentioned anywhere on the host.

Fetched and bound source files: `01-introduction.tex`, `02-preliminaries.tex`, `07-sections.tex`, `08-global-sections.tex`. Read the introduction and the full global-consequences section; the two other files are retained references and were not fully audited. See `sources/openai_overlooked/BINDINGS.json` for exact source URLs and SHA-256.

### Actual statements

The claimed local theorem is a bijection between local points of a **smooth proper genus-at-least-two curve** and splittings of its **full arithmetic étale fundamental group**. The global section gives

\[
\operatorname{loc}\operatorname{Sec}(C/K)
=C(\mathbb A_K)_\bullet^{\mathrm{f\text{-}cov}}.
\]

It then explicitly retains the hypothesis

\[
C(\mathbb A_K)_\bullet^{\mathrm{f\text{-}cov}}=C(K)
\]

to conclude the global section conjecture. Its abelian-target corollary assumes a nonconstant map to an abelian variety with **finite rational-point group and zero maximal divisible Sha subgroup**. The elliptic-target variant assumes full Selmer corank **zero** at some coefficient prime, invokes the companion low-corank converse, and obtains finite rank-zero target arithmetic. Its modular-curve corollary instead invokes Stoll's finite-descent result.

The final restriction gives finiteness of the localization image at each finite place over a number field with no CM subfield. It explicitly disclaims an effective or uniform bound and does not assert finiteness of the whole global section set.

### Exact applicability screen

The fixed seed has rank two. It therefore does not satisfy either the finite-point abelian-target hypothesis or the zero-corank elliptic-target hypothesis. The modular curve statement may cover a modular curve mapping to the seed, but its input consists of **full nonabelian sections**, not arbitrary classes in `Sel_p(E)/W` or the Kato derivative. No map lifting every excess Selmer class to such a section is supplied in this manuscript.

Consequently one cannot infer a Sha bound by replacing the full fundamental group with its abelian quotient. The missing comparison is precisely a lifting statement from the actual seed's abelian cohomology classes to global nonabelian sections, together with a conclusion controlling their image; neither the cited section theorem nor the paper's global applications establishes it.

**Disposition:** source newly read at the global-interface level, but no new seed assignment recommended. It is not evidence for a cofinite content estimate, an exact `C_2 = 288(a_ell-2)R` comparison, or Q36. This excludes the application just tested, not nonabelian approaches generally.

## Catalogue false positives not promoted to leads

The catalogue's **Deligne–Drinfeld conjecture** is about the rational Grothendieck–Teichmüller Lie algebra being free on odd-weight generators. It is **not** a compatible-companions theorem. The abstract resolves the ambiguous title; there was no reason to import a nonexistent common-realization result from it.

The already-read families—low-Selmer-corank BSD, pointwise 2-converse, Goldfeld/mean twist rank, Milne rationality, CM Hodge, and imaginary-quadratic modularity—were not counted again as new sources. The prior CM comparison already followed the actual Kummer-CM coefficient construction and fixed-source denominator mechanism from the most relevant of these.

## Boundary of this search

The screen revisited all 372 family headings in the pinned catalogue and selected the previously unexamined arithmetic section-conjecture family for primary-source scope checking. It did not read 719 manuscripts, prove the local section theorem, or exhaust every possible adaptation. No new seed arithmetic was computed. FIN, ORDER9 and Q36 are unchanged by this screen.
