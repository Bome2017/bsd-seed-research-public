# Sources and reading scope

2026-10-12. All mathematical source imports remain distinct from the exact Python replay.

## Primary sources

**SW.** William Stein and Christian Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Mathematics of Computation 82 (2013), 1757-1792.

https://www.wstein.org/papers/mcom2649-iwasawa-alg.pdf

Section 3.1, printed pp.1762-1764: the ordinary modular-symbol distribution and finite projections P_n; Proposition 3.5: their coefficient precision; Section 6.1 and Theorem 7.3, printed pp.1776,1778: ordinary Selmer torsion and integral Kato divisibility; Proposition 7.2: residual-to-p-adic surjectivity for p>=5. The ordinary case is the only one imported here. The seed's earlier certificate had already applied these inputs at 5. The published author offprint was read in the web parser. Requested screenshots of this host failed; no successful visual inspection of its pages is claimed. No copy or PDF byte hash is distributed.

**Greenberg.** Ralph Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv:math/9809206v1 (18 September 1998); published as a chapter in *Arithmetic Theory of Elliptic Curves*, Lecture Notes in Mathematics 1716 (1999), 51-144.

https://arxiv.org/pdf/math/9809206

Proposition 4.14 and proof, printed pp.52-53 in the arXiv version: a cotorsion cyclotomic Selmer group with no base-field p-primary torsion has no proper finite-index Lambda-submodule. This is used by Pontryagin duality to rule out finite submodules of the dual. Its statement was checked in the PDF page image at zero-based page 51 and its proof in parsed text. The discussion of injectivity of global restriction, printed p.26, was also inspected. The full published chapter was not separately compared line-by-line with the arXiv version.

The structure theorem for finitely generated torsion Z_p[[U]]-modules, exactness of Pontryagin duality on discrete p-primary groups, inflation--restriction, and the Kummer exact sequence are the standard algebraic/cohomological inputs explicitly used in PROOF.md. They are not outputs of the finite checks.

## Retained seed records, all at one commit

Repository `Bome2017/bsd-seed-lab`, commit `0e8bb6859d1391e6d449b1ef02aff2cfd85310f1`.

- `work/returns/BSD_FINITE_SOURCE_PALETTE_REVIEW_CODEX_2026-10-12/REPORT.md`: authenticates the standard ordinary source/period comparison for the selected family. Blob `e31dae4ebdf33f9bc1e73a8682c936a6831bb26e`.
- `work/state-sync-2026-09-30/release/v0.2.6/evidence/src/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_CERTIFICATE.md`: the rigorous historical symbol certificate, ordinary distribution normalization and old unit coefficient. Blob `008c22932c67d6df5fe4948bd55f1f2dcd930e56`.
- The same directory's `run/SYMBOLS_m25.txt` and `run/SYMBOLS_m5.txt`: complete small exact tables, copied into inputs/. Their content hashes are checked by the script and recorded in SOURCE_BINDINGS.json.
- `work/state-sync-2026-09-30/release/v0.2.6/evidence/src/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md`: the historical rank, torsion, full residual-image, ordinary Kato and normalized-regulator inputs. Blob `291e618f69600e05864c9d2542dc1de1688a37ba`. Its old symbol evidence is superseded by P5_CERTIFICATE; its historical date-specific status is not promoted to the present endpoint ledger.
- `work/returns/BSD_BOCKSTEIN_CERTIFICATE_REVIEW_CODEX_2026-10-12/ARITHMETIC_INTERFACE.md`: the matched height coordinate and retained r_17=1 used only to describe a future finite-precision target. Blob `bf4523894bf5e81e8203aa6da7099bec9e74b67d`, as bound in the supplied review. No new 17-adic height run is claimed.
- `work/returns/BSD_KATO_EXCESS_CONTENT_SOURCE_TEST_CODEX_2026-10-07/SOURCE_TESTS.md`: prior scoped tests explain why source units and generic characteristic equalities do not give a cofinite content bound. Blob `72e80256a6f91dfed95fa307c0fc226a25401d8c`. The present tower argument adds a specific old unit value and an actual finite-submodule theorem; it does not contradict that caution.

## What is retained, not replayed

The original large Fourier-coefficient/ball-arithmetic certification, the modular-symbol denominator theorem, rank/descent, global residual-image proof, Manin inputs and matched numerical heights are retained at their existing grades. Only the two small exact tables and their downstream arithmetic are replayed here. No source coefficient at a new prime, full p-adic series, or number-field Selmer group is computed.

The assertion of no new coefficient table recovered is scoped to the paths/searches inspected in this session; a code search on unindexed/default branches does not establish absence from the whole repository. No exhaustive novelty or duplicate-result search is claimed.
