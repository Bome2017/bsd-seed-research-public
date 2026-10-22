# SEED_SPECIALIZATION

* **Curve and parametrization.**
  * Minimal model `y² = x³ − x² − 66020924x − 65074271436`, `N = 2³·3·2243·4547²·5843`.
  * Finite counts use the original model `y² = x³ − 22735x² + 106272484x` (`x ↦ x + 7578`,
    `u = 1`); `a_ℓ` is identical at odd good `ℓ`.
  * A fixed optimal parametrization `X₀(N) → E` is assumed. Its Manin constant affects only
    `p = 2`, which is excluded.
* **Field.**
  * `K = ℚ(√−23)`, class number 3, `u_K = 1`.
  * Heegner hypothesis: kernel-checked (`SeedFinite.lean`).
  * `w(E^{−23}) = −1`. Certified `L′(E^{−23}, 1) ∈ [39.512236, 40.182321]` (record), so
    `rank E(K) = 3` and `y_K` is torsion (record, Gross–Zagier–Kolyvagin import).
* **Residual image.** Retained A.3: `ρ̄_{E,p}` is surjective for all odd `p`. This is used in
  Lemma 2 and in `E(H_ℓ)[p] = 0`.
* **Excluded coefficient primes.**
  * `p = 2, 3`, since Lemma 2 needs `p ≥ 5`. Both are settled in the record anyway.
  * `p = 23`, since `K ⊂ ℚ(E[23])`.
  * `p ∣ N` (2243, 4547, 5843), since Kolyvagin's descent needs good reduction.
  * The domain of Lemma 3 is therefore all primes `p ≥ 5` with `p ∤ 23N`, ordinary or
    supersingular.
* **Auxiliary primes.**
  * `ℓ ∤ 23N`, inert in `K`, `a_ℓ = 0`.
  * Kernel-checked instances: 281, 661, 839.
  * Computed (Python): 30 such `ℓ < 10⁵`, listed in `checks/supersingular_inert_100000.out.json`.
  * `ℓ = 3391` would govern `p = 53`.
* **Still conditional.**
  * Kolyvagin's structure theorem in its mod-`p` form, and the sign `ε_0 = −w(E/ℚ)` of `y_K`.
  * Gross's norm relation.
  * Silverman's lower bound, used only to motivate Prop. 4; Prop. 4 itself needs only that
    `y_ℓ` is non-torsion.
  * Non-torsion of `y_ℓ` for a given `ℓ`. This holds if some `L′(E/K, χ, 1) ≠ 0` for a
    character `χ` of conductor `ℓ` (Gross–Zagier–Zhang); it is not checked here.
* **No periods or lattices** enter this construction. Q36 normalizations are untouched.
