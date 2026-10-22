# Sources and retained-input boundaries

2026-10-12. The calculations and the relative identity are new derivations in this packet, not novelty claims. No third-party full papers are redistributed.

## Primary mathematical sources

**Dokchitser-Evans-Wiersema (DEW).** *On a BSD-type formula for L-values of Artin twists of elliptic curves*, arXiv:1905.04282v2; published in J. reine angew. Math. 773 (2021), 199-230.

https://arxiv.org/pdf/1905.04282

Read the number-field BSD normalization in Section 1.1, Notations 15-18, the conductor induction formula in Section 2.5, and Lemma 36(2)-(5) with its proof. The formula fixes full real periods and finite differential corrections; Lemma 36 fixes field-relative height scaling. These normalizations are used, but the conjectured equality with Sha is NOT assumed. The PDF's parsed text was read. Browser screenshots failed, so no successful visual rendering or byte hash is claimed for this source. No table in its Section 3 is used.

**Birch-Stevens Fourier formula.** A printed primary-source use with explicit conventions is Constantinescu-Nordentoft, *Non-vanishing of Geodesic Periods of Automorphic Forms*, Geometric and Functional Analysis (2025), equations (3.9)-(3.10).

https://link.springer.com/article/10.1007/s00039-025-00715-z

The finite-character/modular-symbol identity is used with the packet's explicitly chosen orientation. The four-character product is unchanged by simultaneous path reversal. Section 3 of PROOF.md also explains the direct finite Fourier derivation, so no normalization is inferred from an abstract.

**Maistret-Shukla.** *On the factorization of twisted L-values and 11-descents over C_5-number fields*, arXiv:2501.09515v1.

https://arxiv.org/html/2501.09515v1

Read Sections 1.1-1.3, in particular Conjectures 1.1 and 1.3, Theorems 1.4 and 1.6, and the hypotheses of the descent algorithm. This is a scope check, not a theorem proving this seed's relative Sha. Its ideal-to-Sha statement is conjectural. Its practical descent setting is CM with additional splitting conditions, which cannot be applied to this non-CM seed. Its rank-zero formula is not used after dropping the rank hypothesis.

**Stein-Wuthrich.** *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013).

https://www.wstein.org/papers/mcom2649-iwasawa-alg.pdf

Section 3, printed page 1763, was visually inspected for character/layer conventions. No new Iwasawa assertion is imported here: the tower result is retained from the pinned review. The present finite character sums do not improve the earlier finite-layer precision theorem for the infinite p-adic coefficient.

## Pinned project inputs

Every path below is in `Bome2017/bsd-seed-lab` at
`84a7333af028ff5bc694bc82bcb3c768a019f5c6`.

- `work/returns/BSD_CYCLOTOMIC5_MOMENT_REVIEW_CODEX_2026-10-12/REPORT.md` and `TOWER_AUDIT.md`, especially Section 6: E(Q_n)=E(Q), rank two, 5-primary tower vanishing. Read in full; stronger residual-image hypotheses retained, not recertified.
- `work/returns/BSD_FINITE_SOURCE_PALETTE_REVIEW_CODEX_2026-10-12/PERIOD_AUDIT.md`: original normalized-newform table, minimal-model change u=1, Omega_E=2 omega_1. Read in full.
- `work/state-sync-2026-09-30/release/v0.2.6/evidence/src/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run/SYMBOLS_m25.txt`: all 20 rows read; copied from the automatically mounted predecessor ZIP and checked against the fresh pinned Git blob. Only this small data file is redistributed here.
- `work/state-sync-2026-09-30/release/v0.2.6/evidence/src/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md`, read lines 38-62: retained local types/Tamagawa values and rational torsion. This historical file is not used for its superseded analytic-rank status or its old claims of coverage.

## Not performed

No original large symbol/Fourier replay, denominator-lattice recertification, residual-image proof, new point saturation, number-field Tate algorithm, actual Sha calculation, or new p-adic coefficient evaluation. No independent model agent or human reviewer was used. The ideal support of an algebraic L-value is explicitly distinguished from the support of Sha.
