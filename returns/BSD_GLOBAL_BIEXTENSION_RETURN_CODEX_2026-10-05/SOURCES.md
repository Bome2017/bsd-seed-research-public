# Sources, conventions, and proof grades

Primary sources read for this attempt (2026-10-05):

- [K.-S. Tan, Refined theorems of the Birch and Swinnerton-Dyer type, AIF 45 (1995), 317–374](https://aif.centre-mersenne.org/item/10.5802/aif.1457.pdf). Definitions 2.2(a) and 2.6, printed pp. 330 and 334. Browser text and the existing cache were read; no new visual scan inspection is claimed.
- [J. S. Milne, Abelian Varieties, corrected author text dated January 2, 2022](https://www.jmilne.org/math/xnotes/AVs.pdf). Sections 9–10, especially the Poincare universal property and the line-bundle square construction. Used to specify (2.1). The exact seed integral extension remains the separately named retained G2 input.
- [Burns–Kurihara–Sano, On derivatives of Kato's Euler system and the Mazur–Tate conjecture, arXiv:2103.11535](https://arxiv.org/pdf/2103.11535). Section 2.1, algebraic constant; Conjecture 3.4 and Theorem 4.1. Checked to distinguish the conjectural algebraic leading-term import from the retained fixed-p proof of W. No conjecture is promoted to theorem here.
- [Bullach–Honnor, On the refined ‘Birch–Swinnerton-Dyer type’ conjectures of Mazur and Tate, current author manuscript](https://dominikbullach.github.io/MazurTate.pdf). Theorems 1.4 and 1.7, Remark 1.8(b). The split-multiplicative leading-term statement is not the needed positive-rank regulator formula. This source check is limited to these statements and does not audit the entire paper.

Retained project records copied byte-for-byte and hashed in INPUT_BINDINGS.json:

- G2_PROOF.md and G2_REVIEW.md: normalized rational Poincare lifts, retained integral identity-component geometry, factor-two normalization, full Kummer/Galois input and G2 domain. Their earlier review grade is preserved.
- THEOREM_W_REPAIRED.md: fixed-p scalar, period convention, composite regularization repair, p-primary adaptation. No common rational scalar or unitness is supplied.
- U22_LINK2_REVIEW.md: scoped missing geometric comparison and the corrected trace-cycle issue. In particular it does not rule out every geometric mechanism.
- HISTORICAL_LINE_SEP18.md: used specifically to identify prior occurrence of the squared determinant carrier and the LINE comparison in Sections 4 and 6. Its other exploratory/heuristic claims and any stronger nonexistence wording are not promoted.
- PART2_BRIDGES.py: retained release claim ledger for B.17/B.19. It is a claim ledger, not an independent proof verifier.
- P17_MSL.txt, P17_RETAINED_RECEIPT.json and SINGLETON_SPEC_RETAINED.md: old exact-identified plus symbols, their receipt/hash, and generator/period convention. The arithmetic recombination is new; their original analytic certification is retained rather than rerun.
- checks/retained_pairing_check.gp: copied unchanged from the independent G2 audit; replayed on its three small normalization cases.

The supplied task packet is preserved under input/. Its 3 listed manifest entries and ZIP hash verify. It proposes a construction; its proposed payoff is not itself an established comparison theorem.

New mathematical derivations in PROOF.md and code controls are by this worker. They have not been independently accepted, formally verified, or assessed for literature novelty. Numerical/check outputs do not certify the global modular section. No memory file is a mathematical proof source in this return.
