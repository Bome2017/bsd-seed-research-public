# H41_DEFINITIONS_ERRATA_BOUNDARY_ADDENDUM_012

A **definition / errata / boundary object, not a proof attempt**, frozen before the `(D3) ⟹ (C)` attack.
Its job is to stop a corrected theorem from being proved and then attributed to an imprecise sealed
statement. Every quoted definition is extracted mechanically from its sealed source and machine-verified
byte for byte. All prior objects are byte-identical; nothing sealed is edited.

**1. Errata to ADDENDUM_011** (preserved byte-for-byte). Its statement that `(D1)` "cannot die on the
2-adic side" is superseded by: *`(D1)` has no remaining valuation/parity obstruction* — characteristic-2
special-fibre and geometric pathologies are **not** excluded. Its sentence calling `(D3) ⟹ (C)` "a statement
about the integral / finite-flat 2-torsion realisation" is also superseded.

**2. Canonical definitions, verbatim.** `(C) χ_p = α_p mod 2` is recorded as a Betti-character statement
on `H₁(X₀(2p)(ℂ),ℤ)`, with every defining source quoted. `(D3)` is quoted with its neighbours — and its
hypotheses are stated in **three sealed places that do not agree**; no canonical list exists, so any use
must discharge the union `(B)`, `(D)`, `(D1)`, `(D2)`, special-fibre description.

**3. `(C) ⟺ (C′)` is UNPROVED IN THE SEALED RECORD** and withdrawn as a proved dependency — asserted in
`ADDENDUM_005`, argued nowhere. `S₀ ∈ E₀(ℚ)[2]` cannot be part of the definition of `(C′)`.

**4. Three specification defects frozen, with a prohibition:** `ω̄_f` is undefined; `Ω` versus `ω` is
unresolved; the integral model is not fixed. None of those symbols may be used in a bridge proof until a
definition/model-resolution lemma fixes them.

**5. No integral carrier exists in the architecture** — no Néron-model subgroup, finite-flat group scheme,
identity-component or component-group object has been specified as the carrier of `(D3) ⟹ (C)`. The
record-wide scan finds four lines: the superseded `ADDENDUM_011` sentence; Stage II lines 28 and 142,
both about the identity component of the real locus `E₀(ℝ)⁰`; and Stage I line 230, inside the
real-period table. None specifies an integral object.

**Unproved bridge candidates, not conclusions.** The generic-fibre shape `χ_p = e₂(T_p,·)`,
`α_p mod 2 ⇝ π̂(S₀)`, with the binding qualification that the Betti-functional / Weil-pairing
identification must be pinned down (sign, eigenspace, polarization, normalization). Conditional
rationality: *if* `T_p = π̂(S₀)`, then `S₀` is rational, since `T_p` is and `π̂` is an injective
`ℚ`-morphism — a consequence of `(C′)`, never an input. And a warning not to choose a finite-flat carrier
at `2 ‖ N`, where the Néron 2-torsion is quasi-finite and `T_p` may specialize outside the identity
component.

**Next stage, by directive:** prove `(C) ⟺ T_p = π̂(S₀)` on the generic fibre first, independently of
`(D3)`; only then ask what `(D3)` supplies.

    ADDENDUM.md      the eight sections, with machine-verified verbatim blocks
    computation/     build_addendum.py, verify_verbatim_blocks.py, audit_integral_carrier.sh
    receipts/        CANONICAL_VERBATIM, VERBATIM_VERIFICATION, INTEGRAL_CARRIER_ABSENCE

**The H41 seed remains unproved.**
