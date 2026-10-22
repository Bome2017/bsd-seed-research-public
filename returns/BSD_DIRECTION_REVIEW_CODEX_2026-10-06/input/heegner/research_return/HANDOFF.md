# HANDOFF — next unresolved arithmetic step

1. **Control of the cross-prime index (main).** Fix a supersingular inert `ℓ` (`a_ℓ = 0`,
   `(−23/ℓ) = −1`). Produce a quantity `A(ℓ) ∈ ℤ/(ℓ + 1)`, defined independently of `Sha`, with

       A(ℓ) ≢ 0 (mod p)  ⇒  P_ℓ ∉ pE(H_ℓ)    for every admissible p ∣ ℓ + 1.

   * Candidate: the image of the Heegner Mazur–Tate element `θ_ℓ ∈ ℤ[G_ℓ]` in `I_G/I_G²`,
     compared with the derived class (Bertolini–Darmon type).
   * Requirement: `A(ℓ)` must not factor as (`Sha`-dependent scalar) × (regulator); otherwise it
     reproduces the record's `C_p` wall (W06).
   * Do **not** try to obtain this from Néron–Tate heights. `PROOF.md` Prop. 4 proves that route
     cannot work for any `p ∣ ℓ + 1`.
2. **Coverage (independent of 1).** Prove that for all large `p` there is an inert `ℓ` with
   `a_ℓ = 0` and `p ∣ ℓ + 1`. Alternatively, find a replacement family of auxiliary primes in
   which Lemma 1 stays exact for many moduli at once. Without this, even a perfect answer to
   item 1 controls only the primes it happens to reach. The data to `10⁵` miss 37 and 41, with
   `p = 23` excluded anyway.
3. **Imports to re-verify before reuse.**
   * Kolyvagin's structure theorem in its mod-`p`, `ν = 1` form, with the sign convention
     `ε_0 = −w(E/ℚ)`.
   * Gross's Prop. 3.7 norm relation for inert `ℓ` with `u_K = 1`.
4. **Not recommended:** computing Heegner points at level `N ≈ 6.5·10¹⁵`, or extending the
   supersingular-prime table as a substitute for item 2.
