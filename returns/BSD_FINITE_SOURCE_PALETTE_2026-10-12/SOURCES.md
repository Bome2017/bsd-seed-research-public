# Sources, retained inputs and reading scope

Date: 2026-10-12. This file records attribution, not independent certification of the full input chain. Third-party publications are not redistributed. Primary sources were inspected through the web reader; a separate container download failed, so no PDF byte hashes are claimed.

## Primary published/source inputs

**BKS.** David Burns, Masato Kurihara and Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024), 855-919. DOI 10.2969/jmsj/90699069.

https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en

Read Section 2.1, equations (2.1.1)-(2.1.5), printed pp. 863-865: image lattice, relative symbol, primitive plus condition and actual smoothing normalization. PDF pages 9 and 10 (zero based) were visually inspected. Lemma 5.8's height/Bockstein diagram was checked against the retained review. The conjectural leading-term formula is not imported as a theorem. The paper does not itself state the finite palette or prove this seed's input value 144.

**CNS.** Kestutis Cesnavicius, Michael Neururer and Abhishek Saha, *The Manin constant and the modular degree*, arXiv:1911.09446.

https://arxiv.org/pdf/1911.09446

Lemma 6.5, printed p. 42, gives the Manin-constant comparison for connected-kernel newform quotients and integrality for arbitrary newform elliptic quotients. This page was visually inspected. The introduction, printed p. 2, records good/semistable-prime unit results for optimal parametrizations. This return retains the seed's existing good-prime Manin conclusion, rather than re-proving its cited geometric sources. No blanket unit assertion for nonoptimal maps is used.

**Mascot.** Nicolas Mascot, *Moduli-friendly Eisenstein series over the p-adics and the computation of modular Galois representations*, Research in Number Theory 8, article 48 (2022). DOI 10.1007/s40993-022-00329-6.

https://link.springer.com/article/10.1007/s40993-022-00329-6

Section 2.3, equations (2.3.2)-(2.3.3) and Example 2.3.4: all X_1(N) cusps lie over Q(mu_N); cusp 0 is rational in the point-level model whereas infinity generally is not. Only that cusp arithmetic is used.

Standard structural inputs used explicitly in the proof are localization/purity for a smooth curve with punctures, Poincare duality, surjectivity on Tate modules for a connected-kernel quotient, and the integral differential relation for dual isogenies. These are named, not represented as outputs of the finite Python checks.

## Pinned lab inputs

Repository: `Bome2017/bsd-seed-lab`.
Commit: `581f7a26a1d110bcd6131739f94569e4810a719e`.

1. `work/returns/BSD_BOCKSTEIN_CERTIFICATE_REVIEW_CODEX_2026-10-12/REPORT.md`.
   Git blob: `501a944208355884c1a84bd0433d32b5bd90ac48`.
   Retained corrected-content identity and ordinary height-ratio implication. Its independent input chain was not replayed here.
2. `work/returns/BSD_BOCKSTEIN_CERTIFICATE_REVIEW_CODEX_2026-10-12/ARITHMETIC_INTERFACE.md`.
   Read for target-lattice and cyclotomic-coordinate requirements. File content was returned with truncation only at the closing section; no unseen arithmetic is used. No separately verified blob hash is claimed here.
3. `work/returns/BSD_RUBIN_COORDINATE_FOLLOW_CODEX_2026-10-07/COFINITE_NORMALIZATION.md`.
   Git blob: `0c6786f2459637be3480e13cb8ba4f963a3b714e`.
   Retained full ordinary interpolation comparison, source convention, exact c_N, and the recorded one-fifth symbol. Its unknown J is precisely what the new primitive-quotient argument replaces for a newly chosen family.

These connector responses were read at their pinned paths. They are references, not byte-for-byte input copies included in the package. Git blob identifiers specify source identity and do not certify mathematics.

## Inputs not recomputed

The global residual-image theorem, optimal good-prime Manin conclusion, full rank-two saturation, and original exact symbol receipt [1/5]^+ = 144 remain retained. The review's earlier 864/360 checks are not counted as new checks of this return. The current script does not evaluate a modular symbol, Kato coefficient, height or Selmer group.

## New reasoning versus imports

The new written reasoning is the least-degree-isogeny argument; exclusion of a finite abelian-action boundary quotient inside E[p^infinity]; the resulting literal image-lattice equality for a specified map; use of the retained period anchor with that equality; and the finite three-pair construction. The final standard-coefficient implication is a composition with the retained review, not an independent proof of its all-height-one Kato foundation.
