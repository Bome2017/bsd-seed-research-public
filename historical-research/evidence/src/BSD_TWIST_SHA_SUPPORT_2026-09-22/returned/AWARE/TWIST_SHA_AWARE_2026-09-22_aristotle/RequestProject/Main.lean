import Mathlib

/-!
# Certified arithmetic data for the quadratic twist `E^{-7}`

This file machine-checks the *finite arithmetic inputs* used in the hostile audit of the
prime support of `Ш(E^{-7}/Q)` (see `AUDIT_STAGE_I.md`, `AUDIT_STAGE_II.md`).

Everything here is a finite computation about the Weierstrass model

    E^{-7} :  y² = x³ + 159145 x² + 5207351716 x

and about its traces of Frobenius `a_ℓ` at small good primes `ℓ`.  Nothing here is an
Iwasawa-theoretic or BSD statement: the file exists so that the numerical facts the audit
leans on (invariants, reduction types, torsion bound, residual-image certificates) are
kernel/compiler-checked rather than asserted.

The bridge from these certificates to statements about the mod-`p` Galois representation
(irreducibility, surjectivity) is classical group theory + Chebotarev and is documented in
the audit text; it is *not* formalised here, since Mathlib has no `ρ̄_{E,p}`.
-/

namespace TwistSha

/-! ## 1. Weierstrass invariants -/

/-- `a₂` coefficient of the model `y² = x³ + a₂x² + a₄x` of `E^{-7}`. -/
def A2 : ℤ := 159145

/-- `a₄` coefficient of the model `y² = x³ + a₂x² + a₄x` of `E^{-7}`. -/
def A4 : ℤ := 5207351716

/-- Standard `b₂` invariant (`a₁ = a₃ = a₆ = 0`). -/
def b2 : ℤ := 4 * A2
/-- Standard `b₄` invariant. -/
def b4 : ℤ := 2 * A4
/-- Standard `b₆` invariant. -/
def b6 : ℤ := 0
/-- Standard `b₈` invariant. -/
def b8 : ℤ := -A4 ^ 2

/-- Standard `c₄` invariant. -/
def c4 : ℤ := b2 ^ 2 - 24 * b4
/-- Standard `c₆` invariant. -/
def c6 : ℤ := -b2 ^ 3 + 36 * b2 * b4 - 216 * b6
/-- Discriminant of the model. -/
def disc : ℤ := -b2 ^ 2 * b8 - 8 * b4 ^ 3 - 27 * b6 ^ 2 + 9 * b2 * b4 * b6

/-- The invariants of the given model of `E^{-7}`, and the relation `c₄³ - c₆² = 1728 Δ`. -/
theorem invariants :
    c4 = 155281214032 ∧ c6 = -19291412299579840 ∧
    disc = 1951401451332224483990307737856 ∧ c4 ^ 3 - c6 ^ 2 = 1728 * disc := by
  refine ⟨by norm_num [c4, b2, b4, A2, A4], by norm_num [c6, b2, b4, b6, A2, A4],
    by norm_num [disc, b2, b4, b6, b8, A2, A4], by norm_num [c4, c6, disc, b2, b4, b6, b8, A2, A4]⟩

/-- Factorisation of the discriminant.  Since `v_q(Δ) < 12` at every bad prime, the model is
minimal at every prime, so its differential is a Néron differential. -/
theorem disc_factorization :
    disc = 2 ^ 8 * 3 ^ 2 * 7 ^ 6 * 2243 * 4547 ^ 3 * 5843 ^ 2 := by
  norm_num [disc, b2, b4, b6, b8, A2, A4]

/-- Factorisation of `c₄`.  Together with `disc_factorization` this gives the valuations
`(v(c₄), v(Δ))` at every bad prime, which for `p ≥ 5` determines the Kodaira type. -/
theorem c4_factorization : c4 = 2 ^ 4 * 7 ^ 2 * 43 * 1013 * 4547 := by
  norm_num [c4, b2, b4, A2, A4]

/-- The conductor reported for `E^{-7}` factors as stated (the exponents at `2, 3, 7, 2243,
4547, 5843` are `3, 1, 2, 1, 2, 1`). -/
theorem conductor_factorization :
    (318656212624190616 : ℤ) = 2 ^ 3 * 3 * 7 ^ 2 * 2243 * 4547 ^ 2 * 5843 := by norm_num

/-- `j(E^{-7})` is not an algebraic integer: its denominator `689197281363 = 3²·2243·4547³/…`
is `> 1`.  Concretely `1728 c₄³ = j · Δ` with `v_{2243}(Δ) = 1 > 0 = v_{2243}(c₄³)`, so
`v_{2243}(j) < 0`.  Hence `E^{-7}` does **not** have complex multiplication. -/
theorem j_not_integral_at_2243 :
    ¬ (2243 : ℤ) ∣ c4 ∧ (2243 : ℤ) ∣ disc := by
  constructor
  · norm_num [c4, b2, b4, A2, A4]
  · norm_num [disc, b2, b4, b6, b8, A2, A4]

/-! ## 2. Point counts and traces of Frobenius

`apOf p` is `p + 1 - #E(F_p)` computed by summing Legendre symbols of the cubic.
Only used at primes of good reduction, i.e. `p ∉ {2, 3, 7, 2243, 4547, 5843}`. -/

/-- Legendre symbol of `a` mod an odd prime `p`, as an integer in `{-1, 0, 1}`. -/
def legendreVal (a p : ℕ) : ℤ :=
  let r := a % p
  if r = 0 then 0 else if r ^ ((p - 1) / 2) % p = 1 then 1 else -1

/-- `x³ + 159145 x² + 5207351716 x` reduced mod `p`. -/
def cubicMod (x p : ℕ) : ℕ := (x * x % p * x + 159145 % p * (x * x % p) + 5207351716 % p * x) % p

/-- Trace of Frobenius `a_p = p + 1 - #E(F_p)` of `E^{-7}` at a good prime `p`. -/
def apOf (p : ℕ) : ℤ := -((List.range p).map (fun x => legendreVal (cubicMod x p) p)).sum

/-- Traces of Frobenius at the first good primes.  (All are even, consistent with the rational
`2`-torsion point `(0,0)`.) -/
theorem ap_small :
    apOf 5 = 2 ∧ apOf 11 = -2 ∧ apOf 13 = 4 ∧ apOf 17 = 6 ∧ apOf 19 = -4 ∧
    apOf 23 = 0 ∧ apOf 29 = 0 ∧ apOf 31 = 8 ∧ apOf 37 = 10 ∧ apOf 41 = -6 := by
  native_decide

/-- `#E(F_ℓ) = ℓ + 1 - a_ℓ` at a good prime `ℓ`. -/
def orderOverFp (l : ℕ) : ℤ := (l : ℤ) + 1 - apOf l

/-- The orders `#E^{-7}(F_ℓ)` for `ℓ = 5, 11, 13, 17` have gcd `2`.  Since torsion injects into
`E(F_ℓ)` for odd `ℓ` of good reduction, `#E^{-7}(Q)_tors` divides `2`; the point `(0,0)` has
order `2`, so `E^{-7}(Q)_tors ≅ Z/2`.  In particular no prime `p ≥ 5` divides the torsion. -/
theorem torsion_divides_two :
    Int.gcd (Int.gcd (orderOverFp 5) (orderOverFp 11))
      (Int.gcd (orderOverFp 13) (orderOverFp 17)) = 2 := by
  native_decide

/-! ## 3. Reduction type at the multiplicative primes

At a prime `q` of multiplicative reduction the reduction is *split* iff `-c₆` is a square mod
`q`.  This decides whether the `q`-adic `L`-function has an exceptional (trivial) zero at the
central point. -/

/-- Is `d` a square mod `p`? -/
def isSquareMod (d p : ℕ) : Bool := (List.range p).any (fun t => t * t % p = d % p)

/-- `-c₆ mod q`, for `q` a prime of multiplicative reduction. -/
def negC6Mod (q : ℕ) : ℕ := ((-c6) % (q : ℤ)).toNat

/-- Reduction is **non-split** multiplicative at `2243` and **split** multiplicative at `5843`
(and split at `3`).  The split prime `5843 ≥ 5` is the one that produces a trivial zero of the
`p`-adic `L`-function. -/
theorem multiplicative_split_types :
    isSquareMod (negC6Mod 2243) 2243 = false ∧
    isSquareMod (negC6Mod 5843) 5843 = true ∧
    isSquareMod (negC6Mod 3) 3 = true := by
  native_decide

/-! ## 4. Residual image certificates

For a good prime `ℓ ≠ p`, the characteristic polynomial of `ρ̄_p(Frob_ℓ)` is
`x² - a_ℓ x + ℓ mod p`, with discriminant `d_ℓ = a_ℓ² - 4ℓ`.

* If `ρ̄_p` is reducible then `d_ℓ` is a square mod `p` for **every** good `ℓ ≠ p`.
* If the image lies in the normaliser of a split Cartan then for every good `ℓ ≠ p` either
  `a_ℓ ≡ 0` or `d_ℓ` is a square mod `p`.
* If it lies in the normaliser of a non-split Cartan then for every good `ℓ ≠ p` either
  `a_ℓ ≡ 0` or `d_ℓ` is a non-square mod `p`.
* If the projective image is `A₄`, `S₄` or `A₅` then `u_ℓ = a_ℓ²/ℓ mod p` lies in
  `{0,1,2,4} ∪ {roots of u² - 3u + 1}` for every good `ℓ ≠ p`.

So a single `ℓ` violating a bullet rules out the corresponding case. -/

/-- `d_ℓ = a_ℓ² - 4ℓ` reduced mod `p`. -/
def discFrobMod (l p : ℕ) : ℕ := (((apOf l) ^ 2 - 4 * (l : ℤ)) % (p : ℤ)).toNat

/-- `a_ℓ mod p`. -/
def apMod (l p : ℕ) : ℕ := ((apOf l) % (p : ℤ)).toNat

/-- Certificate that `ρ̄_p` is **irreducible**: `d_ℓ` is a nonzero non-square mod `p`. -/
def irredCert (p l : ℕ) : Bool :=
  discFrobMod l p ≠ 0 && !isSquareMod (discFrobMod l p) p

/-- For every prime `p ≥ 5` admitting a rational `p`-isogeny by Mazur's theorem
(`p ∈ {5,7,11,13,17,19,37,43,67,163}`) there is a good prime `ℓ` whose Frobenius characteristic
polynomial is irreducible mod `p`.  Hence `ρ̄_p` is irreducible for **every** prime `p ≥ 5`:
`E^{-7}` has no Eisenstein prime `≥ 5`. -/
theorem irreducible_certificates :
    [(5, 17), (7, 5), (11, 5), (13, 17), (17, 11), (19, 5), (37, 17), (43, 5), (67, 5),
      (163, 5)].all (fun pl => irredCert pl.1 pl.2) = true := by
  native_decide

/-- Certificate ruling out the normaliser of a **non-split** Cartan: `a_ℓ ≢ 0` and `d_ℓ` is a
nonzero square mod `p`. -/
def killNonsplitCert (p l : ℕ) : Bool :=
  apMod l p ≠ 0 && discFrobMod l p ≠ 0 && isSquareMod (discFrobMod l p) p

/-- Certificate ruling out the normaliser of a **split** Cartan: `a_ℓ ≢ 0` and `d_ℓ` is a
non-square mod `p`. -/
def killSplitCert (p l : ℕ) : Bool :=
  apMod l p ≠ 0 && discFrobMod l p ≠ 0 && !isSquareMod (discFrobMod l p) p

/-- Certificate ruling out an exceptional projective image (`A₄`, `S₄`, `A₅`):
`u = a_ℓ²/ℓ mod p` avoids `{0,1,2,4}` and the roots of `u² - 3u + 1`. -/
def killExceptionalCert (p l : ℕ) : Bool :=
  let u := (((apOf l) ^ 2 * (l : ℤ) ^ (p - 2)) % (p : ℤ)).toNat
  (u ≠ 0 && u ≠ 1 && u ≠ 2 && u ≠ 4) && ((u * u + 1 + 3 * p * p - 3 * u) % p ≠ 0)

/-- Full surjectivity certificates for `5 ≤ p ≤ 37`: for each such `p` the listed good primes
rule out, in order, the reducible and non-split-Cartan cases, the split-Cartan case, and the
exceptional cases.  With the classification of maximal subgroups of `GL₂(F_p)` (`p ≥ 5`) this
means `ρ̄_p` is surjective for every prime `5 ≤ p ≤ 37`. -/
theorem surjectivity_certificates :
    [(5, 13, 17, 17), (7, 11, 5, 5), (11, 17, 5, 5), (13, 5, 17, 5), (17, 5, 11, 5),
      (19, 11, 5, 11), (23, 11, 5, 5), (29, 5, 11, 5), (31, 19, 5, 5), (37, 5, 17, 5)].all
      (fun t => killNonsplitCert t.1 t.2.1 && killSplitCert t.1 t.2.2.1 &&
        killExceptionalCert t.1 t.2.2.2) = true := by
  native_decide

/-! ## 5. Supersingular / ordinary behaviour at small primes

`p` is supersingular for `E^{-7}` iff `a_p = 0` (for `p ≥ 5`), and *anomalous* iff `a_p = ±1`.
Among good `p < 300` the supersingular ones are `23, 29, 131, 167, 281`, and there are no
anomalous ones (all `a_p` are even). -/

/-- The good primes below `50` at which `E^{-7}` is supersingular are exactly `23` and `29`;
none of the good primes below `50` is anomalous. -/
theorem supersingular_below_fifty :
    ([5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].filter (fun p => apOf p = 0)) = [23, 29] ∧
    ([5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].filter
      (fun p => apOf p = 1 ∨ apOf p = -1)) = [] := by
  native_decide

/-! ## 6. Why the certified real interval does not pin down `v_p(L/Ω)`

The certified input is an *interval* for `L(E^{-7},1)`, hence an interval for the algebraic
quotient `L(E^{-7},1)/Ω`.  The only unconditional constraint available on the denominator of
that rational number at primes `p ≥ 5` is `p`-integrality of the modular symbol (valid here
because `ρ̄_p` is irreducible for all `p ≥ 5`, §4), i.e. the denominator is `{2,3}`-smooth,
with **no bound on the exponents**.

The lemma below shows that such a constraint is compatible, for *every* prime `p`, with a
value in the interval whose numerator is divisible by `p`.  So the certified numerics plus
residual irreducibility do not exclude `v_p(L/Ω) > 0` at any prime, and therefore the
Kato/Kobayashi upper bound `v_p(#Ш) ≤ v_p(L·#tors²/(Ω·∏c_v))` — whose hypotheses *are*
verified here — yields no vanishing statement at any single prime. -/

/-- Dyadic rationals with numerator divisible by `p` are dense: for every positive `p` and
every nonempty open interval there is `p·m/2^k` inside it. -/
theorem exists_p_divisible_dyadic_mem_Ioo (p : ℕ) (hp : 0 < p) (a b : ℝ) (hab : a < b) :
    ∃ (m : ℤ) (k : ℕ), a < (p * m) / 2 ^ k ∧ (p * m) / 2 ^ k < b := by
  set x : ℝ := (a + b) / 2 with hx
  have hxa : a < x := by rw [hx]; linarith
  have hxb : x < b := by rw [hx]; linarith
  have hpR : (0:ℝ) < (p:ℝ) := by exact_mod_cast hp
  obtain ⟨k, hk⟩ := pow_unbounded_of_one_lt ((p : ℝ) / (x - a)) (by norm_num : (1:ℝ) < 2)
  have h2 : (0:ℝ) < 2 ^ k := by positivity
  have hlt : (p:ℝ) / 2 ^ k < x - a := by
    rw [div_lt_iff₀ h2]
    rw [div_lt_iff₀ (by linarith : (0:ℝ) < x - a)] at hk
    linarith
  refine ⟨⌊x * 2 ^ k / p⌋, k, ?_, ?_⟩
  · have h1 := Int.sub_one_lt_floor (x * 2 ^ k / p)
    rw [lt_div_iff₀ h2]
    have h3 : x * 2 ^ k / p - 1 < (⌊x * 2 ^ k / p⌋ : ℝ) := h1
    have h4 := mul_lt_mul_of_pos_left h3 hpR
    rw [mul_sub, mul_div_cancel₀ _ (ne_of_gt hpR)] at h4
    rw [div_lt_iff₀ h2] at hlt
    nlinarith
  · have h2' := Int.floor_le (x * 2 ^ k / p)
    rw [div_lt_iff₀ h2]
    have h4 := mul_le_mul_of_nonneg_left h2' (le_of_lt hpR)
    rw [mul_div_cancel₀ _ (ne_of_gt hpR)] at h4
    nlinarith

/-- Instantiated at the certified interval for `L(E^{-7},1)/Ω`, which the package's data place
inside `(391.99779, 392.00221)`: for **every** prime `p` there is a rational in that interval
with `{2}`-smooth denominator and numerator divisible by `p`.  Hence no `p`-adic valuation of
the algebraic `L`-value is determined by the certified interval together with `p`-integrality;
rounding to the nearest integer is an extra, unjustified step. -/
theorem certified_interval_does_not_pin_valuation (p : ℕ) (hp : 0 < p) :
    ∃ (m : ℤ) (k : ℕ), (391.99779 : ℝ) < ((p : ℝ) * (m : ℝ)) / 2 ^ k ∧
      ((p : ℝ) * (m : ℝ)) / 2 ^ k < (392.00221 : ℝ) :=
  exists_p_divisible_dyadic_mem_Ioo p hp _ _ (by norm_num)

/-! ## 7. `A₂ = 0` is sufficient but not necessary for an integral derived regulator

In the Bertolini–Darmon leading-term formalism the `k`-th derived height is only known to be
valued in `p^{-A_k} Z_p`, where `p^{A_k}` is the exponent of the saturation defect
`S̄^{(k)}/S^{(k)}`.  Hence `A_k = 0` forces the Gram matrix of the pairing to be integral and so
forces `v_p(R_der) ≥ 0`: **sufficient**.

The converse fails already as linear algebra: a symmetric Gram matrix all of whose entries have
valuation `-1` can have determinant a `p`-adic unit.  The example below (at `p = 5`) is such a
matrix, and it is even non-degenerate — so `v_p(R_der) ≥ 0` cannot be turned back into a
statement about the saturation defect.  Calling the two conditions "equivalent" is therefore an
error, not a shorthand. -/

/-- A symmetric `2 × 2` rational matrix whose entries all have denominator `5`, i.e. `5`-adic
valuation `-1`, and whose determinant is `1`. -/
def defectGram : Matrix (Fin 2) (Fin 2) ℚ := !![1/5, 2/5; 2/5, 29/5]

/-- `defectGram` is symmetric, as a Gram matrix of an even derived height must be. -/
theorem defectGram_symm : defectGram.transpose = defectGram := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [defectGram]

/-- Every entry of `defectGram` has denominator `5`: the pairing is genuinely non-integral. -/
theorem defectGram_entries_nonintegral : ∀ i j, (defectGram i j).den = 5 := by
  intro i j; fin_cases i <;> fin_cases j <;> simp [defectGram] <;> norm_num

/-- Nevertheless `det = 1`, a `5`-adic unit.  So "the regulator has non-negative valuation"
does **not** imply "the saturation defect vanishes": the implication `A₂ = 0 ⇒ v_p(R_der) ≥ 0`
is strict, and the two statements are not equivalent. -/
theorem defectGram_det_unit : defectGram.det = 1 := by
  simp [defectGram, Matrix.det_fin_two_of]; norm_num

end TwistSha
