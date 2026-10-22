# SEED_DELTA — change in mathematical knowledge (2026-10-06 continuation)

## 1. Exact quantified statements now proved, with prime domain

Let `K = ℚ(√−23)`, and let `y_n` be the Heegner points of conductor `n`. For an inert prime `ℓ`,
let `G_ℓ = ⟨σ⟩ ≅ ℤ/(ℓ+1)`, `D_ℓ = Σ_{i≤ℓ} iσ^i`, and let `P_ℓ` be the derived point
(`PROOF.md` §1).

* **(a)** For every prime `ℓ ∤ 23N` inert in `K` with `a_ℓ(E) = 0`:
  `(σ − 1)D_ℓ y_ℓ = (ℓ + 1)y_ℓ` in `E(H_ℓ)`. The algebra is kernel-checked; the input is
  Gross's norm relation.
* **(b)** For the same `ℓ` and every prime `p ≥ 5`, `p ≠ 23`, `p ∣ ℓ + 1`: `ℓ` is a Kolyvagin
  prime for `(E, K, p)`. This is a written proof using retained A.3, with its
  characteristic-polynomial step kernel-checked.
* **(c)** For the same `ℓ` and every such `p` with `p ∤ N`: `P_ℓ ∉ pE(H_ℓ) ⇒ Sha(E/ℚ)[p] = 0`.
  This is written and conditional on the imports listed in `ASSUMPTIONS.json`; its central
  import is Kolyvagin's structure theorem at `ν = 1`.
* **(d)** For the same `ℓ` with `y_ℓ` non-torsion, every odd `p ∣ ℓ + 1`, and every
  `μ ≤ min{ĥ(Q) : Q ∈ E(H_ℓ) non-torsion}`: `ĥ(D_ℓ y_ℓ)/p² ≥ μ`. All inequalities are
  kernel-checked; the height decomposition is written.
* **(e)** Seed instances, kernel-checked:
  * `ℚ(√−23)` satisfies the Heegner hypothesis for `N`.
  * `ℓ ∈ {281, 661, 839}` are inert with `a_ℓ = 0`.
  * Through these, single points `P_281`, `P_661` and `P_839` govern `p = 47`, `p = 331` and
    `p ∈ {5, 7}` respectively.

## 2. Independently controlled input newly used or constructed

* The `p`-independent derived point `P_ℓ` at a supersingular inert prime, and the exact
  all-moduli identity (a).
* Supersingular inert primes as simultaneous Kolyvagin primes (b).

Neither depends on `Sha`. The `p`-divisibility of `P_ℓ` is **not** independently controlled.
That is the open part.

## 3. Displayed implication to the seed obligation

    for every large p, some ℓ as in (b) with p ∣ (ℓ+1)/ι(ℓ)
        ⇒ (c) ⇒ Sha(E/ℚ)[p] = 0 for all large p   (uniform support)
        ⇒ together with the finite remainder: FIN, then ORDER9 via the record's settled primaries.

Both antecedents are open: control of `ι(ℓ)`, and the existence of `ℓ` for each `p`.

## 4. Before / after

* **Before:** the Heegner lane over `ℚ(√−23)` gave fixed-prime criteria only. The record marked
  it "no cross-prime index" (ROUTE_BLOCKED).
* **After:**
  * A cross-prime index exists in the precise sense of (a)–(c). One point controls all
    admissible prime factors of `ℓ + 1` at once. Nothing is computed, so no prime is newly
    settled.
  * The natural archimedean control is ruled out by (d), whatever strength of height lower
    bound is used.
  * No previously allowed excess configuration is ruled out. `Sha[p] ≅ (ℤ/p)²` remains
    compatible with everything proved here, by `P_ℓ ∈ pE(H_ℓ)` for all relevant `ℓ`.

## 5. First remaining arithmetic equation

Find `A(ℓ) ∈ ℤ/(ℓ + 1)` with independent control such that
`A(ℓ) ≢ 0 (mod p) ⇒ P_ℓ ∉ pE(H_ℓ)` for all admissible `p ∣ ℓ + 1`. The candidate is the
coefficient of `θ_ℓ` (the Heegner Mazur–Tate element) in `I_G/I_G²`, compared with the derived
class by a Bertolini–Darmon-type refined conjecture at a supersingular inert `ℓ`. Separately,
coverage needs supersingular inert `ℓ ≡ −1 (mod p)` for every large `p`. The data to `10⁵`
cover 28 primes and miss 37 and 41.
