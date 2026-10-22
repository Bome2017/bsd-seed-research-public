# H41_G_GENERIC_FIBRE_IDENTIFICATION_ADDENDUM_013

**G, repaired after audit: `(C) ⟺ (C_gen) : T_p = q̂(S₀^B)`, on the generic fibre over `ℂ`.**

**Status: operator-audited, repaired as specified, NOT VERIFIED.** The operator's verdict on the draft (preserved
byte-for-byte in `01_audited_draft/`) was *REVISE BEFORE SEAL — MATHEMATICAL CORE OF G: PASS WITH REPAIRS*, with
recommended status *G = MATHEMATICALLY SOUND AFTER LOCAL REPAIRS*. Every repair is applied and listed in the §11
ledger. **The repaired text has not itself been re-audited.**

**The seal-blocking repair.** The draft used `π` both for the quotient `J → E₀` and for the parametrization `X → E₀`.
A mechanical inventory shows the **sealed record does the same, inside Stage II itself** — it defines `π` on `X` at
l.52, then writes `ker π` and `π(C₀)` at ll.161–164. Nothing sealed is renamed. G introduces `q : J → E₀` (connected
kernel), `φ = q ∘ AJ_∞ : X → E₀`, and `q̂ = λ_J⁻¹ q^∨ λ_{E₀}` with **principal** polarizations, and states a crosswalk:
every sealed `π_*` on curve cycles is `φ_*` and unaffected; every kernel, restriction or dual is `q` or `q̂`.

**The proof.**
* **(G1)** A literal branch cut `K = (κF)⁻¹((0,∞))` gives `∂K = div F`, winding `= ±(γ·K)`, and `∫_K ψ = 0` in one
  self-contained lemma — Lefschetz duality is no longer needed. With `K = 2c + β`, both `T_p = ι_X(β̄)` and
  `(−1)^{χ_p(x)} = (−1)^{x·β}`.
* **(G2)** A uniform lattice lemma: for any orientation-reversing involution of a unimodular `ℤ²`,
  `[H : L⁺+L⁻] = |v·u| ∈ {1,2}`, the primitive `U₀` functional is `±(v·–)`, its mod-2 dual is `v̄`, and the plus-line
  normalization is integral exactly in the rectangular case. So `S₀^B` is half a primitive anti-invariant cycle —
  real, nonzero — and `e_J(q̂s, t) = e_{E₀}(s, qt)` carries no degree factor.
* **(G3)** nondegeneracy; **(G4)** since `q̂` is a `ℚ`-rational closed immersion and `T_p` is rational, `(C_gen)` forces
  `S₀^B ∈ E₀(ℚ)[2]` — **rationality is a consequence, not an input.**

Every sign convention cancels mod 2. The two genuinely load-bearing choices are the `U₀` definition of `α_p` and the
principal polarizations in `q̂`.

**Not claimed.** `(C)` itself; anything about `(D3)`, M, R or characteristic 2; uniform `E₀ = E`. Level-specific
consequences are kept only as dependencies on `ADDENDUM_007`, not re-audited. Classical sources are not in the corpus;
the operator's citations (Milne Prop 13.2 and Ex 13.3; Stein Prop 3.3; McMullen) are recorded as such.

    ADDENDUM.md        the repaired G, crosswalk, repair ledger
    01_audited_draft/  PROOF_G.md, check_E0_side.py, E0_SIDE_CHECK.txt — exactly as audited
    computation/       build_addendum.py, verify_verbatim_blocks.py, check_lattice_lemma.py,
                       inventory_pi_uses.sh, audit_reference_presence.sh
    receipts/          VERBATIM_VERIFICATION, CANONICAL_VERBATIM, LATTICE_LEMMA_CHECK, PI_USAGE_INVENTORY,
                       REFERENCE_PRESENCE, AUDITED_DRAFT_CUSTODY

**The H41 seed remains unproved.**
