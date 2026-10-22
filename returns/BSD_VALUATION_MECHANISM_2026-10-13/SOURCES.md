# Sources, hypotheses and custody

The published inputs are used as theorems. Their complete proofs were not independently reconstructed. Third-party full texts are not redistributed. The local runtime could not download PDF bytes; no byte hash of a publication is claimed. The web reader supplied full text and the inspected page images.

## Primary theorem inputs

**BCS:** A. Burungale, F. Castella, C. Skinner, *Base change and Iwasawa Main Conjectures for GL2*, arXiv:2405.00270v2, Theorem 1.1.2, printed page 2. Journal publication: IMRN 2025, rnaf082.

https://arxiv.org/pdf/2405.00270v2
https://arxiv.org/html/2405.00270v2

Read the definition of ordinary Selmer, Conjecture 1.1.1, Theorem 1.1.2(a),(b), and the comparison with earlier ramification hypotheses. Theorem page 2 was visually inspected. Use part (b), not the rational equality in part (a). Good ordinary p>3, residual irreducibility, and a primitive cyclotomic-kernel transvection are the hypotheses used. The rank-at-most-one restriction in Corollary 1.3.1 is not imposed on Theorem 1.1.2 and is not silently extended.

**CGS:** F. Castella, G. Grossi, C. Skinner, *Mazur's main conjecture at Eisenstein primes*, arXiv:2303.04373v2 (15 October 2025); Mathematische Annalen 393 (2025), 2451--2506. Theorem A, printed page 2; Theorem 7.1.1; Section 2.1, Theorem 2.1.1 for normalization.

https://arxiv.org/html/2303.04373v2
https://arxiv.org/pdf/2303.04373

Theorem page 2 was visually inspected. Lambda_Q denotes the integral Iwasawa algebra for the rational base field, not a ring obtained by inverting p. The local constituent must differ from both 1 and the mod-p cyclotomic character. Theorem A has no rank restriction; Theorem D's rank-zero/rank-one classical BSD assertion is not used. The period is that of the given elliptic curve, including its isogeny scaling. Section 2.1 interpolation matches the standard measure; full-real versus primitive-plus period differs only by a 2-unit here.

**SP via SW:** W. Stein and C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757--1792. Theorem 6.1, printed p.1776, attributes the ordinary algebraic formula to Schneider and Perrin-Riou. Section 4.5, p.1774, gives the cyclotomic-coordinate regulator convention; Section 5.1 explicitly distinguishes valuation equality from full p-adic BSD.

https://wstein.org/papers/mcom2649-iwasawa-alg.pdf

Theorem page 1776 was visually inspected. This packet uses the good ordinary branch only. The algebraic theorem includes primary finiteness/nondegeneracy in its equality-of-order criterion and supplies the finite local corrections. Its proof is imported through this published formulation, not independently rederived from the original 1980s papers.

**PARI documentation:** canonical ordinary cyclotomic height and the regulator convention were compared to the experiment's named implementation. The installed producer was not rerun in this packet.

https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html#ellpadicregulator
https://pari.math.u-bordeaux.fr/dochtml/html/Modular_symbols.html

## Retained arithmetic (all at baseline f97843a1)

- The positive-control PROOF.md: isogeny, rank interval, 5-saturation, local factors, standard-measure twisting normalization, coefficient and regulator precision, independent Sha[5] lower bound.
- The positive-control REPORT.md: exact equation and scope of the original experiment.
- The correlated-valuation REPORT.md and outputs/RESULTS.json: control curves, named point pairs, coefficient and height valuations, and normalization.
- The original singleton outside audit RETURN.md: actual certified 17/103 result, not its conjectural prediction. The full large corpus and original verification chain are retained.
- VALUATION_TARGET.md: seed17 matched height valuation r=1. Its older source-index caveat was removed only for the later authenticated source family; the standard-measure seed17 inference does not apply to arbitrary historical Kato scalings.
- The prior Bockstein and finite-source review chain: used solely for the corollary about its named e_p. The usual-Selmer theorem and the positive-control conclusion do not depend on re-identifying the full-S complex.

Git blob bindings are in SOURCE_BINDINGS.json. Source documents were read through the connector, not copied byte-for-byte into the return. Code input digits are explicitly transcribed retained inputs. Neither a matching hash nor the new exact small checks recertifies their original computation.

## Mathematical review priorities

Check (1) the integral, not rational, main-conjecture statements; (2) the local Eisenstein characters of the positive twist; (3) the actual standard measure and the factor log(1+p)^2 in the height; (4) the order-of-vanishing argument establishing finiteness before using cardinalities; and (5) the reverse seed17 deduction's dependence on the old Sha17 input. In particular, it must not be presented as a new independent Sha17 proof.
