# Sources and reading scope

Fresh primary-source screen, 2026-10-15:

- Fisher–Newton, *Computing the Cassels–Tate pairing on the 3-Selmer group of an elliptic curve*, [author PDF](https://www.dpmms.cam.ac.uk/~taf1000/papers/ctp3.pdf). Read the introduction, Lemmas 1.1–1.2, Theorem 1.3, local-duality discussion, and Problem 3.5. The paper separates the source-element admission test from normalized functions on a torsor. Its global splitting step is the earlier B3 stop. Its pairing formula needs evaluations on the torsor; direct pairing of admitted Kummer images is zero.
- Creutz, *Second p-descents on elliptic curves*, [author PDF](https://www.math.canterbury.ac.nz/~b.creutz/Papers/sec-p-desc.pdf), and [university preprint](https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2012/creutz-21.pdf). Screened the introduction and second-descent algorithm description; no whole-paper audit or implementation verification.
- [Official Magma handbook, descent](https://magma.maths.usyd.edu.au/magma/handbook/text/1570), entries `ThreeDescentCubic`, `ThreeSelmerElement`, `NineDescent`, `NineSelmerSet`. It documents conversion from a specified source element to a cubic, and then computation of the locally soluble lift set. The latter returns −1 for an empty set. The implemented routine requires transitive flex action and can require degree-nine class/unit computations. No local executable or online run was available/performed.

Historical stop actually read:

`/Users/bsm/BSD_P3_CASSELS_TATE_RETURN_OPUS_2026-09-29/METHOD.md`, `K_B3A.md`, `STATE.json`, `RETURN.md`. The first two distinguish feasible local residue work from the missing normalized global function. The stop is scoped to that seed-sized implementation and budget; it is not an impossibility theorem.

The numerical/label inputs are bound in `INPUTS.json`. Their mathematical grades remain those of the preceding exact-descent packets and independent admission review. In particular, the 28042a1 lower bound does not use its unconfirmed full class-group calculation. The present replay verifies the six explicit field elements and norm assertions; it does not rerun rank descents, all-place admission, or source-completeness certificates.
