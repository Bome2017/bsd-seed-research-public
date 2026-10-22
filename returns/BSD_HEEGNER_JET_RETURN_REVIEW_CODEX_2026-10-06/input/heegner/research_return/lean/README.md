# lean/ — new Lean sources of this run

These are new sources, separate from the accepted BFR modules, which are not modified or
re-proved here:

* `RequestProject/Continuation/CrossPrimeKolyvagin.lean`
  * Kolyvagin derivative identity in any ring.
  * Cross-prime invariance.
  * Root-of-unity factor `m/(ζ − 1)`.
  * Supersingular characteristic polynomial mod `p`.
* `RequestProject/Continuation/HeightObstruction.lean`
  * `‖m/(ζ − 1)‖² ≥ m²/4`.
  * Weighted-sum lower bound.
  * The height obstruction inequality (Prop. 4 core).
* `RequestProject/Continuation/SeedFinite.lean`
  * Heegner hypothesis for `ℚ(√−23)`.
  * Inertness of 281, 661 and 839.
  * Factorizations of `ℓ + 1`.
* `RequestProject/Continuation/SeedPointCounts.lean`
  * `a_ℓ = 0` for `ℓ = 281, 661, 839`, by kernel enumeration of all `ℓ²` pairs.
  * About 9.5 minutes of build time.

Toolchain: `lean-toolchain` (Lean 4.28.0), Mathlib as pinned in `lake-manifest.json`.

Build:

    lake build RequestProject.Continuation.CrossPrimeKolyvagin RequestProject.Continuation.SeedFinite \
      RequestProject.Continuation.SeedPointCounts RequestProject.Continuation.HeightObstruction

The transcript is in `BUILD_TRANSCRIPT.txt`. `AxiomAudit.lean` produces `AXIOM_AUDIT.txt`.
Every audited declaration uses only `propext`, `Classical.choice` and `Quot.sound`, or a
subset of them.

The sources contain no `sorry`, no `admit` and no `native_decide`, and add no axioms.

**Formal scope.** Heegner points, ring class fields, Selmer groups, Kolyvagin's theorem,
Néron–Tate heights and the identification of point counts with `#E(𝔽_ℓ)` are not formalized.
The Lean statements are the algebraic, inequality and finite-arithmetic steps named in
`PROOF.md`, at their literal scope.
