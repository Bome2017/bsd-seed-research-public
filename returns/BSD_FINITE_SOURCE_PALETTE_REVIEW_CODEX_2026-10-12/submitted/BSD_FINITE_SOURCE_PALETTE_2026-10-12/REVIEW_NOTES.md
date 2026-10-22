# Adversarial checks and remaining qualifications

Date: 2026-10-12. This is the author's own review ledger, not another agent's review, external endorsement, or a formal proof certificate.

## Mathematical failure modes addressed

**Homothety is not equality.** The proof fixes an optimal J_1 quotient followed by a least-degree isogeny, and proves the proper image equals T_pE before discussing the open curve. Multiplying the parametrization by p invalidates that step; no claim for such a source is made.

**Irreducibility on the wrong elliptic curve.** The least-degree-isogeny argument is applied to the dual map out of E, whose residual image is retained. It does not presume residual irreducibility on E_1 in order to prove that the isogeny to E_1 is prime to p.

**A hidden cusp denominator.** The open/proper quotient is explicitly a quotient of the cusp permutation module. It has abelian action, but simultaneously embeds in E[p^infinity]. Its p-torsion is forbidden by the two-dimensional residual representation. No bound on the order of the cuspidal subgroup is asserted or needed.

**A spurious Tate twist.** With H^1(-, Z_p(1)), purity puts an untwisted permutation module at the boundary. Adding an extra cyclotomic twist would change the written argument.

**A nonrational base cusp.** The map uses cusp 0. The commonly used infinity cusp of the point-level X_1 model is generally not rational.

**Manin integrality confused with unitness.** The optimal X_0 good-prime unit is a retained input; CNS compares it to the optimal X_1 quotient; a prime-to-p isogeny preserves unitness. Integrality alone or optimality alone is not used as a universal unit theorem.

**Period-anchor provenance.** The number 144 is a retained receipt from the pinned normalization note, not independently regenerated. Its real-period and Manin conventions must remain those described there. At p >= 5 the real-component factor 2 is harmless; an arbitrary p-factor would not be.

**A Bezout combination of inadmissible sources.** At each p the construction selects an admissible pair. It never combines a pair involving an integer divisible by p into a purported p-integral Euler system. The gcd M^2 is a normalization control only.

**A missing p-Euler factor.** The interpolation comparison and its cancellation are retained exactly. The separate Rubin prefactor is not cancelled again. The actual H is in U-coordinates.

**Confusing absence of normalization exceptions with Sha support.** There remains an uncomputed actual standard leading coefficient and a nonnegative intrinsic Kato defect. This return does not prove any upper bound for either. Three smoothing pairs are not three global Sha witnesses.

## Executed checks

The standard-library script and its deterministic output are in checks/. It passes 100 exact gcd controls, 1,132 nonzero-residue coverage cases, 24 bad-modulus controls, 364 input vectors for common-unipotent-invariant checks, ten malformed/excluded input controls, and 17 small-field seed point counts by two independent elementary implementations. The point counts only mark small ordinary/supersingular examples; they are not coefficient evaluations.

All unbounded assertions are justified by written arguments in PROOF.md, not by extrapolation from those finite controls. The script explicitly emits no Sha conclusion for any row.

## Review priority

A subsequent reviewer should first check Sections 2-4 of PROOF.md: the cohomological pushforward direction, the finite boundary quotient and exact abelian-action argument, and the match of the retained period receipt to the primitive quotient. The three-pair arithmetic is elementary. The final implication also requires the retained Kato and height-review chain, which was not independently rebuilt in this return.

FIN, ORDER9 and Q36 are unchanged. No formalization, independent human review or separate same-team model review was performed for this new construction.
