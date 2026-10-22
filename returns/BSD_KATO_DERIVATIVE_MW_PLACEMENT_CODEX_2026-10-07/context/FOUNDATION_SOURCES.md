# Source record

## This pass

- Kato, *P-adic Hodge theory and values of zeta functions of modular forms*,
  [Astérisque 295 (2004)](https://www.numdam.org/item/AST_2004__295__117_0/).
  Local PDF hash-bound. Read §§8.2–8.5, 8.10–8.12, 12.4–12.7, 13.3–13.4,
  13.8, 13.10 and relevant §13.13. Visually checked printed pp.225 and 230
  for the representation/Euler and smoothing formulas. The earlier pass
  visually inspected pp.221–222.
- Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic
  curves*, [published 2024 PDF](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en).
  Checked §2.1, Hypothesis 2.2, (2.3.1), the §4 assumptions and Proposition
  4.4. The printed finiteness assumptions remain part of the source;
  this audit supports the separately written weak-order adaptation.
- Prior return at lab commit d4d86454eedd7e3be2c0b398f4a8210fa4abc4a3:
  WEAK_ORDER_PROOF.md, TAME_COMPARISON.md and HANDOFF.md, copied unmodified.
- The user's supplied desk-level assessment is recorded in REVIEW_SCOPE.md.
  It is conditional feedback, not a claim that a human referee has certified
  the source transport.

The sheaf/Galois control and elementary lattice arguments are written in the
new proof. Standard local Tate-module descriptions and global cohomological
dimension are explicit imports; they were not re-proved in Lean. The
seed's residual-image, rank and local-data certificates remain retained.

No exhaustive literature or novelty search was performed. Full PDFs are
bound by hash and source URL, not redistributed. Hashes establish identity.
