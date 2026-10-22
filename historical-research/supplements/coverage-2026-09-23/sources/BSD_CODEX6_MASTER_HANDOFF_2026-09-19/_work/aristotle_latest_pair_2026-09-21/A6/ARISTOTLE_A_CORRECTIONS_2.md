# Second round of corrections (review of 2026-09-20, revision 2)

This file applies the latest review.  As before, `ARISTOTLE_A_RETURN.md` and
`ARISTOTLE_A_CORRECTIONS.md` are left unedited for provenance; this file is the current record.
Nothing here settles a new Sha prime, proves finiteness, proves order nine, or touches `q = 36`.

---

## 0. Compilation, independently replayed

The review notes that compilation had so far been producer-reported.  In this session the whole
development was rebuilt from a cold `lake build` against the pinned toolchain (Lean 4.28.0,
Mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365` as fixed by `lake-manifest.json`) and checked
again, in the same session, item by item:

* `lake build` completes with all 9 modules of `RequestProject/` built and no errors or warnings;
* a source scan finds no occurrence of `sorry`, `admit`, `axiom`, or `@[implemented_by]`;
* `#print axioms` on every headline theorem — `card_eq_nine_of_large_prime_torsion_free`,
  `card_eq_nine_of_prime_torsion_free`, `duality_bound_is_sharp`,
  `duality_bound_is_sharp_symmetric`, `duality_bound_is_sharp_symmetric_oddPrime`,
  `greenberg_wiles_rhs_eq_one`, `target_B_does_not_give_order_nine`,
  `coinvariants_infinite_of_charIdeal_T_sq`, `ker_eq_bot_of_surjective_sandwich`,
  `exists_surjection_iff_ker_eq_bot`, `sha_dual_vanishes_iff_rank_two_source`,
  `seed_coincidences_are_generic`, `seed_disc` — reports only
  `propext`, `Classical.choice`, `Quot.sound` (and `seed_disc` only `propext`, `Quot.sound`).

## 1. The surjection sandwich: retained, and now stated as the equivalence it is

The review accepts the lemma

> surjections `ℤ_p² ↠ S ↠ ℤ_p²` force both maps to be isomorphisms,

and observes correctly that, with `S = Sel_{p^∞}(E/ℚ)^∨` and the dual Kummer sequence

    0 → Ш[p^∞]^∨ → Sel_{p^∞}(E/ℚ)^∨ → ℤ_p² → 0

supplying the second arrow, *constructing the first arrow independently would prove
`Ш[p^∞] = 0`* — and that the archive does not construct it, because under that exact sequence the
existence of the first surjection is **equivalent** to primary Sha-vanishing.

That is exactly right, and the equivalence is now machine-checked rather than left as a remark.
`RequestProject/IwasawaControl.lean`:

* `SeedBSD.Iwasawa.exists_surjection_iff_ker_eq_bot`: for a surjection `v : S ↠ M` of `R`-modules
  with `M` Noetherian,

      (∃ u : M →ₗ[R] S, Surjective u)   ↔   ker v = 0.

  Left to right is the sandwich lemma (the composite is a surjective endomorphism of a Noetherian
  module, hence injective).  Right to left: if `ker v = 0` then `v` is an isomorphism and `v⁻¹` is
  the required surjection.
* `SeedBSD.Iwasawa.sha_dual_vanishes_iff_rank_two_source`: the same statement with `M = ℤ_p²`,
  i.e. in the shape of the dual Kummer sequence — the existence of any surjection
  `ℤ_p² ↠ Sel_{p^∞}(E/ℚ)^∨` is equivalent to `Ш[p^∞]^∨ = 0`.

The consequence is recorded in the docstrings in the review's own terms: the lemma is not a
reduction of the arithmetic problem, it is a precise statement of it.  Producing the first arrow
*is* the outstanding task; formalising the implication has not performed any part of it.  The
one-directional packaging `sha_dual_vanishes_of_rank_two_source` is retained because it is what an
arithmetic construction would be plugged into.

## 2. Scope of the symmetric isotropy file: the localisation kernel

The review's remaining qualification is accepted: the symmetric file's prose loosely identified
`Sel_n(E)` with an intersection of two maximal isotropic subspaces, while its actual Lean theorem
is abstract linear algebra, and it does not remove the localisation kernel.

Corrected in the sources, with no change to any theorem statement:

* `RequestProject/SymmetricIsotropySharpness.lean` now carries a `Scope and the localisation
  kernel` section in the header.  It states that `Sel_n(E)` is the kernel of the global-to-local
  map `H¹(ℚ, E[n]) → ∏_v H¹(ℚ_v, E[n])/im(E(ℚ_v)/n)`; that the intersection `X ∩ L` inside the
  restricted product is the quotient of `Sel_n(E)` by the everywhere-locally-trivial classes
  `Ш¹(ℚ, E[n])`; and that nothing in the file bounds or mentions that kernel.  It also records
  that the restricted-product Poitou–Tate formalism realising both subspaces as maximal isotropic
  in one nondegenerate space is not developed here.
* The docstring of `duality_bound_is_sharp_symmetric` no longer writes
  `dim Sel_n(E) = dim(X ∩ L)`; it speaks only of `dim(X ∩ L)` and flags the scope.
* The same two corrections are applied to the alternating file
  `RequestProject/IsotropicSharpness.lean`.

The mathematical conclusion is unchanged and is one-directional: isotropy *alone* yields no bound
better than `½ dim V`, in a space of the correct symmetry type.  It is a no-go for one method, not
a statement about `Sel_n(E)`.

## 3. Broad impossibility claims: retracted

Per the review, the following are withdrawn from the record.  Each was an over-reading of a
correct but narrow result; the narrow results stand.

* **`ARISTOTLE_A_RETURN.md` §5, items 1–3, read as global impossibility.**  Retracted as global
  claims.  What is proved is: the Greenberg–Wiles Euler characteristic for `(E[n], Kummer)` is the
  product formula (so *that* count carries no information), and isotropy alone bounds an
  intersection by nothing beyond half the dimension, sharply.  Neither excludes other, independent
  arithmetic input, including input that also happens to be phrased through duality.
* **"An Euler system or main-conjecture input is logically necessary."**  Already withdrawn in
  `ARISTOTLE_A_CORRECTIONS.md` §3; re-affirmed as withdrawn.
* **"The seed has no exploitable specificity" / the seed is mathematically hopeless.**  Retracted.
  The proved statement is only that the *advertised* coincidences — `x(P₁) = 4547`, `A | a₂, a₄`,
  the exponent pattern `(3,1,2)`, the constant `2⁸·3²` — are identities of the two-parameter
  family `y² = x(x² − 5Ax + 4AC)`, hence family-level rather than seed-level.  A family
  explanation of the coordinates is not a proof that the family supplies no useful arithmetic, and
  neither archive justifies declaring the seed hopeless.
* **"Artin–Verdier gives nothing uniform" as a closure.**  Downgraded: what was actually checked is
  that the finiteness theorem for *finite* étale sheaves reproduces per-level finiteness.  No
  impossibility for the étale route is claimed.
* **The discriminant identity is not a conductor formula.**  Re-affirmed from
  `ARISTOTLE_A_CORRECTIONS.md` §3: `family_disc` is an identity for the discriminant of the given
  model; conductor exponents additionally need minimality and local valuations, which for the seed
  are the separate checks in `RequestProject/SeedData.lean`.

Retained without change, because each is a machine-checked positive statement rather than an
impossibility claim: the two defective success conditions (`target_B_does_not_give_order_nine`,
and the level-bound equivalence in `RequestProject/Assembly.lean`), the local data and
`c_{4547} = 2` computation at `4547`, the Iwasawa countermodel, and the conditional endgame
`card_eq_nine_of_large_prime_torsion_free`.

## 4. Status after these corrections

* No additional prime is settled; `Ш[p]` is uncontrolled outside `{2, 3, 5, 7}`.
* `FIN`, order nine, and `q = 36` remain open.
* The single outstanding arithmetic object is unchanged and now stated sharply: a surjection
  `ℤ_p² ↠ Sel_{p^∞}(E/ℚ)^∨`, equivalently `Ш[p^∞] = 0`, uniformly in `p`.
* The verdict of `ARISTOTLE_A_RETURN.md` is reduced to what its evidence supports: no candidate
  survived *its own gate in that run*.  It is not a proof that no candidate can survive.
