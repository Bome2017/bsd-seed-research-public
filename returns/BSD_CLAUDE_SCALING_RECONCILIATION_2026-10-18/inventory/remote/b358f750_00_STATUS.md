# Status — Cloud review of the Néron-normalized paired kernel

**Mathematical status: `NORMALIZATION_CONFIRMED_DENOMINATOR_EXPLICIT`**
**Operational tag: `LOCAL_HANDOFF_NOT_NEEDED`** (no step needed Sage, PARI, FLINT or Lean)

## Statement proved (written, at the stated import grades)

1. **Unit scale** (Phase 1; `01_NORMALIZATION_REVIEW.md`). For every prime `p >= 5` with `p ∤ N`,
   `v_p(M) = v_p(d)`. Hence `u_E = ed/(c_E^2 M) ∈ Z_p^x`, and
   `K_E(z,z) = (4 pi^2/A_E) <Theta(z,z), f> ∈ Z_p^x` iff `psi(z) ≢ 0 (mod p)`.
   - Route: Kim–Ota Cor. 6.7 and Thm 1.1 under CR+, checked at the seed; the replayed
     identification `(M) = xi_{f_B}`; the replayed identity `eta_f(N) = (r)`; ARS Thm 2.1.
   - It does **not** prove `p ∤ M`.
2. **Explicit lattice** (Phase 2; `02_DENOMINATOR_LATTICE.md`).
   - For the packet theta forms `G = Theta(z,w)` (`z, w ∈ Z[X]`, `deg z = 0`),
     `2·4547·omega_G ∈ H^0(J_0(N)^Neron, Omega^1)`, i.e. `D0 = 9094`.
   - Therefore `2^10·4547·K_E(G) ∈ Z`, and a fortiori `2^17·4547·K_E(G) ∈ Z` (the join form, `b = 1`).
   - Inputs: CNS Prop. 5.14 and Thm 6.12 + Prop. 6.2, the explicit theta expansions at every cusp
     (`03` Lemma 4/4'), the chosen-map pullback and `c_E | 2^9`.
   - Denominator bit length: 23 (sharper form) or 30 (join form). Radius needed for exact
     identification: `< 1.07e-7`, resp. `< 8.39e-10`.

## Weakest links (recorded, not hidden)

- Kim–Ota Remark 6.6(1). The non-ordinary case of the freeness Theorem 6.5 is asserted with a
  one-sentence justification. The seed's supersingular good primes depend on it.
- CNS Prop. 5.14 / 6.2 / 6.12 are imported: statements checked, proofs not replayed.
- `03` Lemma 4/4' are prior lab written proofs with numerical/enumeration checks, re-checked here at
  levels `5^2`, `7^2`, `11^2`.
- Retained inputs keep their grades: `c_E | 2^9` and the chosen map, residual surjectivity A.3, and the
  2-local `2^8 S ⊆ H`, which the join route uses.

## Explicit remaining gap

The reconstruction denominator is no longer open. What remains is **analytic**.

- No certified enclosure of `K_E(z,z)` exists at the seed with radius below `1/(2B)`. Producing one requires
  the seed pair numerators, whose cost was previously modeled as far beyond the lab's allowances; that
  cost is unchanged here.
- The value `b = 1` at 4547 was not tested for sharpness.
- The toy curve is not covered: its own level would need the N2–N4 computation redone.

No seed witness, `M_2(p)`, new Sha component, FIN, ORDER9 or Q36 is claimed.
