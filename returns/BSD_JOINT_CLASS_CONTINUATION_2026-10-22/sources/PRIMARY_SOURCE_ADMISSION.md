# Source-specific admission check for complete class-kernel bounds

Date: 2026-10-22. Scope: primary-source screen and elementary presentation accounting; no new arithmetic bound, class computation, or novelty claim.

## Decision

No newly checked theorem supplies a small faithful seed class bound with its arithmetic hypotheses already satisfied. Do not reopen reflection, smaller-subfield norm relations, or arbitrary-field p-rationality as if their missing inputs had disappeared. The useful next gate for an integral/Fitting calculation is the complete target relation defect specified in `PRESENTATION_DEFECT.md`.

## Primary sources actually checked

1. **Gras, Théorèmes de réflexion**, JTNB 10 (1998), 399–499, primary article page: https://numdam.org/item/JTNB_1998__10_2_399_0/ . The statement requires a group of automorphisms of order prime to p. The October 7 source audit already checks the full statements and the torus workaround. The full GL2 group fails the order hypothesis. A prime-to-p subgroup repairs that hypothesis but leaves an uncontrolled mirror component; for the standard two-dimensional constituent the Kummer involution exchanges its two torus characters. This is not a new failed mechanism, and it does not rule out all reflection arguments.

2. **Hofmann–Johnston, Algorithms for p-rationality and for p-saturation of units**, arXiv:2609.15190v1, 14 September 2026: https://arxiv.org/html/2609.15190v1 . Freshly checked Theorem 3.9, the discussion of the cyclotomic-unit index formula in the introduction, and Algorithms 15.1 and 15.5. Algorithm 15.1 concerns quasi-p-rationality; Algorithm 15.5 explicitly takes the class number as an input. The class-free real-cyclotomic method uses the special cyclotomic-unit index theorem. The seed's degree-24 field has signature (4,10), so that method does not apply. This source was already checked in `BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/class_control/REPORT.md`; it is not a new opening.

3. **Liu, On the p-rank of class groups of p-extensions**, arXiv:2212.09888v1: https://arxiv.org/html/2212.09888v1 . The class-group application is for Galois p-extensions over the stated base fields; the seed point field has degree p^2-1 and is non-Galois over Q. No matching reduction to the theorem's p-extension setup is available here. The general embedding-problem statements have their own cohomological hypotheses, which have not been verified for an alternate seed construction. No application is claimed.

4. **Biasse–Fieker–Hofmann–Page, Norm relations and computational problems in number fields**, arXiv:2002.12332v4 and published DOI https://doi.org/10.1112/jlms.12563 . Fresh primary text: https://arxiv.org/html/2002.12332v4 . Proposition B / Proposition 3.7 controls class groups after inverting the denominator of an actual norm relation, and retains the denominator-primary error before that inversion. Its use requires both a valid relation and controlled auxiliary class groups. The prior subgroup obstruction excludes the proposed strictly smaller-degree reconstruction of the faithful point-field character. Neither denominator inversion nor S-unit p-saturation supplies the coefficient-p class bound. The corrected v4 source records a correction to Theorem 4.11; no runtime theorem from that part is newly imported here.

5. **Schaefer–Stoll, How to do a p-descent on an elliptic curve**, author manuscript: https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf . Section 5 explicitly keeps both S-units modulo powers and S-class p-torsion in the virtual-unit source. The existing project source applications already authenticate the actual incidence norm and local-source interface. This check does not upgrade their grades.

## What not to infer

- A p-saturated unit subgroup is not a p-saturated class presentation.
- A class presentation on selected prime ideals has a generator defect even if every supplied relation is exact.
- More p-adic digits of a matrix on those selected generators do not remove an unknown target relation defect.
- The joint norm/local repair quotient is already in the October 15 record. Rewriting it here would not constitute a new construction.

FIN, ORDER9 and Q36 are unchanged by this source check.
