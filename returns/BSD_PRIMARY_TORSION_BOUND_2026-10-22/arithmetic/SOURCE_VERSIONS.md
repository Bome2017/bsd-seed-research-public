# Source binding and version distinction

## Lemke Oliver–Wang–Wood

Published: *The average size of 3-torsion in class groups of 2-extensions*, Forum of Mathematics, Pi 13 (2025), e19. DOI https://doi.org/10.1017/S2050508625000009 . Full primary PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6AABE169B5BA8192FE036455DE4F806F/S2050508625000009a.pdf/the-average-size-of-3-torsion-in-class-groups-of-2-extensions.pdf

Saved SHA-256 d5051ab0d37f9985f1adea5cbfee2263812ce96de2b354598448765411344ce5, 711575 bytes. Printed page7, Lemma2.1: its displayed d is absolute degree; the later proof introduces relative degree. The full PDF is CC-BY 4.0 as stated on its first page. Reading scope: lemma, associated class-norm definitions and proof; no average theorem is applied to this seed.

Author preprint: https://wangjiuya.github.io/research/3tor2ext.pdf . Saved SHA-256 91cbb5df29a7e108958d85c1dd1e0795fcebf8c30481bbfe93f29eb0d381b510, 696133 bytes. Printed page6, Lemma2.1 explicitly defines d as relative degree. The norm range and numerator at quadratic degree are tested here. This source-version distinction is left explicit, not silently repaired by borrowing different parts from different statements. Retain the URL/hash when distributing; redistribution license for this author copy was not investigated.

## Original Ellenberg–Venkatesh

*Reflection Principles and Bounds for Class Group Torsion*, IMRN (2007), rnm002. DOI https://doi.org/10.1093/imrn/rnm002 . Author manuscript:
https://people.math.wisc.edu/~ellenberg/Scholz-submit-july17.pdf . The theory lane independently read the quadratic-relative norm window in its Lemma3. This arithmetic lane tests that wider prime range, but does not import the manuscript's asymptotic expression as an explicit numerical bound. Its absolute-class numerator is different from the relative-class expression.

## Seed inputs

`seed_nf.gp`, `nf12.gp`, `relative_fields.gp` are byte-identical retained exact objects from the previously published seed field construction and scalar tower. `BINDINGS.json` hashes them. This run checks agreement of their defining polynomials and the scalar action identities. It retains, rather than freshly recertifies, maximal-order completeness and the full residual-image field identification.

## Later project work read before resumption

`../inputs/BSD_FIN_SOURCE_EXPERIMENTS_2026-10-21/REPORT.md` and `ANALYTIC_OBSTRUCTION_PROOF.md` were read. Their unchanged Cayley families and old whole-order bound are not repeated here. Their local type-III discriminant lower bounds are retained only in the explicitly scoped scaling calculation.
