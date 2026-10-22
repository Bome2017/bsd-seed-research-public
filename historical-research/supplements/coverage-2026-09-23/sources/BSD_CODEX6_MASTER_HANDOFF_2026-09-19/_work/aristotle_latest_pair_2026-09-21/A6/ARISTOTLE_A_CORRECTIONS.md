# Corrections to the previous return, and what is machine-checked after them

This file records the corrections requested in the latest review, applied to the record in
`ARISTOTLE_A_RETURN.md` (which is left unedited for provenance).  Each item states the previous
claim, the correction, and where the corrected statement now lives.  Nothing here settles a new
Sha prime, proves finiteness, or compares the real leading term with the regulator.

All Lean files in `RequestProject/` were rebuilt from scratch in this session against
Lean 4.28.0 / Mathlib `8f9d9cff…`: the build is clean, the sources contain no `sorry`, and the
theorems named below depend only on `propext`, `Classical.choice`, `Quot.sound`.

---

## 1. The local Tate pairing is symmetric, not alternating

*Previous claim (§3.4 of the return, `RequestProject/IsotropicSharpness.lean`).*  The sharpness
of the duality bound was proved in a **symplectic** (alternating) model and presented as the
content of Poitou–Tate for `E[n]`.

*Correction.*  For odd `n` the local pairing on `H¹(ℚ_v, E[n])` obtained from the Weil pairing
and the cup product is **symmetric**: the Weil pairing is antisymmetric, the cup product on
degree-one classes is antisymmetric, and the signs cancel (Poonen–Rains, *Random maximal
isotropic subspaces and Selmer groups*, §4.1).  An alternating countermodel therefore does not,
by itself, speak about the arithmetic pairing.

*What is now proved.*  `RequestProject/SymmetricIsotropySharpness.lean`,
`SeedBSD.Symmetric.duality_bound_is_sharp_symmetric`: in the split **symmetric** space
`V = Fⁿ × Fⁿ` with `ω(x,y) = ∑ᵢ (x₁ᵢy₂ᵢ + x₂ᵢy₁ᵢ)`, the form is symmetric and nondegenerate, and
for every `d ≤ n` there are two totally isotropic subspaces of dimension `n` meeting in dimension
exactly `d`.  `duality_bound_is_sharp_symmetric_oddPrime` specialises to `F = 𝔽_p`, `p` odd, and
also exhibits a vector with `ω(x,x) ≠ 0`, i.e. the form there is genuinely non-alternating.

So the conclusion ("maximal isotropy alone bounds the intersection by nothing better than
`½ dim V`") survives the correction, but it now rests on a model of the right symmetry type.
The header of `IsotropicSharpness.lean` carries the correction and the cross-reference.

## 2. The Iwasawa description skipped the Mordell–Weil directions

*Previous claim (§4, card C6).*  Kato's divisibility bounds `char(X_∞)`, the control theorem
gives `X_∞/(γ−1)X_∞ ↠ Ш[p^∞]^∨`, and hence the valuation of a leading Taylor coefficient of
`L_p` bounds `#Ш[p^∞]`.

*Correction.*  The dual Kummer sequence is

    0 → Ш[p^∞]^∨ → Sel_{p^∞}(E/ℚ)^∨ → ℤ_p² → 0,

so the control-theorem source still carries the two Mordell–Weil directions and need not be
finite.  A characteristic ideal with unit leading coefficient does not bound the cardinality of
the coinvariants.

*What is now proved.*  `RequestProject/IwasawaControl.lean`:

* `SeedBSD.Iwasawa.coinvariants_infinite_of_charIdeal_T_sq` — over `Λ = ℤ_p⟦T⟧` the module
  `X = (Λ/(T))²` is elementary with characteristic ideal `(T)·(T) = (T²)`, and `T²` is a
  distinguished polynomial of degree `2` (so `μ = 0`, `λ = 2`) with unit leading coefficient;
  yet `T` annihilates `X`, so the coinvariants `X/TX ≅ ℤ_p²` are **infinite**.  This is the
  review's countermodel, machine-checked.
* `SeedBSD.Iwasawa.ker_eq_bot_of_surjective_sandwich` and
  `SeedBSD.Iwasawa.sha_dual_vanishes_of_rank_two_source` — the correct positive form.  If a
  Noetherian module `M` (in the application `ℤ_p²`) surjects onto `S = Sel^∨` and `S` surjects
  back onto `M`, then both maps are isomorphisms and `ker(S ↠ M) = Ш[p^∞]^∨ = 0`.

The moral is the review's: the Iwasawa input one needs is not "the leading coefficient is a
unit" in isolation, but that the coinvariant source is *exactly* `ℤ_p²` with no extra finite
part — a strictly stronger arithmetic statement.  The `p = 7` route's leading-term theorem,
primary finiteness, height nondegeneracy and regulator integrality remain necessary; a
main-conjecture equality alone would not supply them uniformly in `p`.

## 3. Directions that should not be recorded as closed

* **"An Euler system or main-conjecture input is logically necessary."** (§3.4, §5.1 of the
  return.)  Withdrawn.  What the sharpness theorems show is that *duality alone* bounds nothing;
  they do not exclude other independently proved arithmetic input.  The corrected reading is
  recorded in the header of `SymmetricIsotropySharpness.lean`.
* **"The seed has no exploitable specificity."** (§3.5, §5.3.)  Withdrawn as stated.  What the
  family identities prove is that the *advertised* features — `x(P₁) = 4547`, `A ∣ a₂, a₄`, the
  exponent pattern `(3,1,2)`, the constant `2⁸·3²` — are family-level, hence not seed-specific.
  Explaining the coordinates through a family is not a proof that the family supplies no useful
  arithmetic.  `RequestProject/Family.lean` now says exactly this.
* **The discriminant identity is not a conductor formula.** (§3.5.)  `family_disc` is an
  identity for the discriminant of the given model.  Deducing conductor exponents needs
  minimality and the local valuation data at each prime; for the seed these are the separate
  computations in `RequestProject/SeedData.lean` (which do include the `4547`-minimality check).
  The docstrings in `Family.lean` are corrected accordingly.

## 4. The retained implication, stated as the review states it

`RequestProject/Assembly.lean`, `SeedBSD.card_eq_nine_of_large_prime_torsion_free`: for a torsion
abelian group `A` with `A[p] = 0` for every prime `p ≥ 11`, with `A[2] = A[5] = A[7] = 0`, and
with `#A[3^∞] = 9`, one has `#A = 9`.  This is the endgame assembly for

    (∀ p ≥ 11, Ш(E/ℚ)[p] = 0)  ⟹  #Ш(E/ℚ) = 9

given the known small-primary components, and it avoids square-order and threshold machinery for
this particular strategy.  It is a conditional: the universal vanishing premise is the
outstanding arithmetic problem, and formalising its consequence proves no instance of it.

## 5. Status

Unchanged by these corrections: no new Sha prime is settled, finiteness is not proved, and no
comparison of the real leading term with the regulator is attempted.  The previous return's
verdict (`ARISTOTLE_NO_SURVIVOR`) stands, with the negative arguments above downgraded from
"closed" to "not established by the material in hand".
