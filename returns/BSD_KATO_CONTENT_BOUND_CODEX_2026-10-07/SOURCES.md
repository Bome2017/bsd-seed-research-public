# Source and dependency ledger

Lab baseline: **eddb24fe53e7450d7b9ff553ff3fd6ed038857ef** on research/state-sync-2026-10-04. All copied inputs are bound in INPUT_BINDINGS.json. Their grades are preserved; a matching hash is not mathematical validation.

## Newly read primary duality statements

J.S. Milne, *Arithmetic Duality*, February 28, 2026:

https://www.jmilne.org/math/xnotes/Tate100.pdf

- Printed p.5, “Global duality (variant)”: finite-S Poitou–Tate, for a finite G_S-module whose order is invertible outside S. Apply at E[p^n], with p in S. The compact/discrete limit and the fine-Selmer interpretation are derived in this return, not quoted as the displayed finite theorem.
- Printed pp.7–8: Cassels–Tate, with divisible kernels and alternation for a polarization induced by a rational divisor. The elliptic curve's identity divisor supplies it. Primary finiteness is obtained before this pairing is used to deduce even length.
- Printed pp.2–3: local finite-module Tate duality supplies the local H² interpretation.

These statements were read through the primary PDF's extracted text. Screenshot requests returned references without displayed page pixels; no fresh visual page inspection is claimed.

Milne, *Arithmetic Duality Theorems*, second edition, I §6 (especially 6.26), was also consulted through the author's primary PDF for the divisible-kernel statement:

https://www.jmilne.org/math/Books/ADTnot.pdf

No conjectural BSD leading-term formula is imported from either source. The exact torsion correction w_p is the elementary deduction in CONTENT_BOUND_PROOF.md, not a new assertion attributed to Milne.

## Retained arithmetic and complex inputs

| Copied input | Interface used | Grade retained |
|---|---|---|
| context/INTEGRAL_MATCHING.md §§2–7 | Integral Kato 13.4(3) via 13.14, all height-one primes; local acyclicity on D; actual two-term finite-free complex | Written/source-matched deduction; independent review pending |
| context/ALGEBRA_REVIEW.md | Preceding primitive derivative criterion and finite-error safeguards | Written review |
| context/FOUNDATION_CHECK.md | Transported class/lattice and derived control | Author source audit |
| context/WEAK_ORDER_PROOF.md | z=Uy; nonzero derivative forces rank two and primary finiteness | Written deduction with retained imports |
| context/MW_PLACEMENT.md | Full Mordell–Weil lattice is saturated; derivative placed integrally | Written deduction |
| context/RUBIN_COMPARISON.md | Matched height/Coleman equation and root-dependent Euler factor | Written source review and finiteness-free case split |
| context/COFINITE_NORMALIZATION.md | Fixed rational map/source has finite normalization support | Written commensurability argument; no intrinsic content bound |
| context/SEED_CALIBRATION.md | Local logs/cofactors and saved height conventions | Exact arithmetic plus retained height outputs |

The source-matching documents carry their own precise Kato and BKS citations. Those entire source transports have not been independently re-proved here. The retained rank-two basis, residual surjectivity, good-prime non-anomalousness and bad-local input table are also not newly certified.

The new content proof does not use the Rubin comparison, fixed-source normalization, a nonsingular height determinant, or an ordinary filtration. Those enter only the optional coefficient reformulation in VALUATION_TARGET.md.

## Reading, replay and scope

The user review and pasted text were read in full. The integral matching, preceding algebra review, placement argument and Rubin documents were read at the interfaces used here. Relevant foundation/control sections and the earlier duality dossiers were checked for conflicts. The new maximal-minor proof was developed directly from the actual presentation; it is not claimed as a rediscovery-free literature theorem.

The predecessor ZIP is preserved as context/RUBIN_PREDECESSOR.zip. Five predecessor manifests verify: 33, 22, 14, 19 and 22 entries. Three predecessor exact check programs were replayed byte-for-byte against their saved outputs. The new program checks 288 small polynomial-matrix cases and two necessary finite-error controls. These checks do not certify general theorems or compute a seed Kato class.

No exhaustive historical or literature novelty search was performed. No Lean theorem, independent expert review, numerical Kato value, new primary vanishing or cofinite estimate is claimed.
