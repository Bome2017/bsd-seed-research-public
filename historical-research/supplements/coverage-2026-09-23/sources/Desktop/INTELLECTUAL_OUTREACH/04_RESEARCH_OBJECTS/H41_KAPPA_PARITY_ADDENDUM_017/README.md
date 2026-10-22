# H41_KAPPA_PARITY_ADDENDUM_017

**κ is odd — PROVED (referee-audited).** The index κ of the pulled-back character `q^*ξ_E` in the primitive `f`-line of the
character group `X_J` of `J₀(2p)` at 2 is odd, by the chain Theorem A (regular-model intersection theory: `B − A = 3(2^{m+1} − 1)`,
odd slopes) → Theorem B (node residues of `overline(dlog F_p)` are `±s_x`, hence 1 mod 2) → Theorem C (the toric residue map has kernel
the residue-free differentials; with the odd Manin constant, κ even is impossible). Consequences: the negative E and B bits
(Theorems D, D′), conditionally on the vertex identification and (K2)–(K5); G and F stay OPEN.

Two fresh Claude referees under a no-repair mandate audited the exact texts carried here: the proof (revision 2, `825c91d2…`)
**PASS WITH REMARKS**; the companion lemma (revision 1, `4094e2a4…`) **FAIL** on one delimited clause, repaired as revision 2
(`29091400…`) and re-audited **PASS WITH REMARKS**, defect removed. The lemma (Theorem G) proves the two inputs that had been
operator-fixed only: Input 1 (thicknesses `e_x ∈ {1,3}`, exactly two of thickness 3, `UV = 2^{e_x}`, the regular dual graph,
`Σ 1/e_x = 2^m/3`) and (K1) (`Φ_J ≅ Z/3·2^m`, `sp_J([0] − [∞])` of exact order `2^m`). The operator reviewed revision 1 of the proof
before the audits and has NOT re-audited the sealed texts.

**Not promoted:** positions G and F, the negative one-cycle theorem, the vertex identification `E₀ ∈ {E, B}`, `(C)`, the H41 seed,
the positive branch.

    ADDENDUM.md    theorems, the operator's review and mandate, the three audits, status flags, custody, promotion, ladder
    R/             the working directory H41_KAPPA_PARITY_2026-09-14 as it stood when the reports were received, byte for byte:
                   KAPPA_PARITY_PROOF.md (rev 2), GRAPH_LEMMA.md (rev 2), history/ (both revisions 1), audits/ (operator review,
                   three referee reports), computation/ (generators), receipts/ (diffs, verbatim receipts, checkers, gp receipt)
    computation/   build_addendum.py, custody_and_reproduction.py, verify_verbatim_blocks.py
    receipts/      CARRIED_ARTIFACT_CUSTODY, REPRODUCTION, PRIOR_OBJECTS, CANONICAL_VERBATIM, VERBATIM_VERIFICATION

**Next: positions G and F, and the vertex identification.** **The H41 seed remains unproved.**
