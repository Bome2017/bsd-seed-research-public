import Mathlib

/-!
# The localization kernel: a Selmer group is not its finite-place image

`SelmerDualityCountermodel.lean` (and the report accompanying it) modelled the `p`-Selmer
group of an elliptic curve as an intersection `G ⊓ L` of a global subspace with a product of
local conditions, taken inside a **finite** sum of local cohomology groups, and then placed
the image of the Mordell–Weil group inside that intersection.  That identification is wrong
in general: for a finite set of places `S` the correct relation is the exact sequence

    0 → ker(loc_S) → Sel_p(E) → im(loc_S) ⊓ L_S → 0,

so the finite-place intersection computes only the *image* of the Selmer group under
localization at `S`.  Identifying Selmer with that intersection requires the injectivity of
`loc_S` (cf. Poonen–Rains, Remark 4.15).

## What is proved here

* `LocKer.finrank_comap_eq` : the dimension count implied by that exact sequence, in pure
  linear algebra.  For a linear map `f : V → W` of finite-dimensional spaces and a subspace
  `L ≤ W`, writing `Sel := f⁻¹(L)`,

      dim Sel = dim ker f + dim (im f ⊓ L).

* `LocKer.finrank_ker_pos` / `LocKer.ker_ne_bot` : consequently, if the Selmer space has
  dimension at least `2` while the finite-place intersection has dimension at most `1`, the
  localization map has nonzero kernel.  This is the abstract form of the failure below.

* `LocKer.seed_affine_card_F11`, `LocKer.seed_card_F11`, `LocKer.eleven_not_dvd_seed_card` :
  the arithmetic input making that failure concrete for the seed curve
  `E : y^2 = x^3 - 22735 x^2 + 106272484 x` at `p = 11` (a prime of good reduction, since
  `11 ∤ N = 2^3 · 3 · 2243 · 4547^2 · 5843`): the reduction has `14` points over `F_11`, and
  `11 ∤ 14`.

## The arithmetic reading (written mathematics, not formalized here)

Since `11 ∤ #Ẽ(F_11) = 14` and the formal group of `E/Q_11` is torsion free
(`e = 1 < p - 1`), one gets `E(Q_11)[11] = 0`, so the local Kummer image at `11` has
`F_11`-dimension `1`.  At the bad places the group `H^1(Q_ℓ, E[11]) = 0` by the corollary
recorded in `SeedBadPlacePrimes.lean`.  Hence the intersection of the image of localization
at the finite bad places together with `11` has dimension at most `1`, whereas the two
independent rational points give `dim Sel_11(E) ≥ 2`.  By `LocKer.finrank_ker_pos` the
localization map has a nonzero kernel, and the Mordell–Weil plane cannot be placed inside
the finite local intersection.
-/

namespace LocKer

open Module

variable {F V W : Type*} [Field F] [AddCommGroup V] [Module F V] [AddCommGroup W]
  [Module F W] [FiniteDimensional F V]

/-- **The localization exact sequence, dimension form.**  For `f : V → W` and `L ≤ W`, the
"Selmer space" `f⁻¹(L)` sits in `0 → ker f → f⁻¹(L) → im f ⊓ L → 0`; hence its dimension is
the sum of the dimension of the localization kernel and the dimension of the intersection of
the image with the local conditions. -/
theorem finrank_comap_eq (f : V →ₗ[F] W) (L : Submodule F W) :
    finrank F (Submodule.comap f L) =
      finrank F (LinearMap.ker f) + finrank F (LinearMap.range f ⊓ L : Submodule F W) := by
  have hle : LinearMap.ker f ≤ Submodule.comap f L := fun x hx => by
    simp only [Submodule.mem_comap, LinearMap.mem_ker.1 hx]
    exact L.zero_mem
  have hrank := LinearMap.finrank_range_add_finrank_ker (f.domRestrict (Submodule.comap f L))
  rw [LinearMap.range_domRestrict, Submodule.map_comap_eq, LinearMap.ker_domRestrict,
    (Submodule.comapSubtypeEquivOfLe hle).finrank_eq] at hrank
  omega

/-- If the Selmer space has dimension at least `2` but the image of localization meets the
local conditions in dimension at most `1`, the localization map has a nonzero kernel. -/
theorem finrank_ker_pos (f : V →ₗ[F] W) (L : Submodule F W)
    (hsel : 2 ≤ finrank F (Submodule.comap f L))
    (himg : finrank F (LinearMap.range f ⊓ L : Submodule F W) ≤ 1) :
    0 < finrank F (LinearMap.ker f) := by
  have := finrank_comap_eq f L
  omega

theorem ker_ne_bot (f : V →ₗ[F] W) (L : Submodule F W)
    (hsel : 2 ≤ finrank F (Submodule.comap f L))
    (himg : finrank F (LinearMap.range f ⊓ L : Submodule F W) ≤ 1) :
    LinearMap.ker f ≠ ⊥ := by
  intro h
  have := finrank_ker_pos f L hsel himg
  rw [h] at this
  simp at this

/-! ### The seed curve modulo 11 -/

/-- The affine points of the reduction of `y^2 = x^3 - 22735 x^2 + 106272484 x` mod `11`. -/
def seedAffinePoints : Finset (ZMod 11 × ZMod 11) :=
  Finset.univ.filter fun P => P.2 ^ 2 = P.1 ^ 3 - 22735 * P.1 ^ 2 + 106272484 * P.1

theorem seed_affine_card_F11 : seedAffinePoints.card = 13 := by decide

/-- Including the point at infinity, the reduction of the seed curve mod `11` has `14`
points. -/
theorem seed_card_F11 : seedAffinePoints.card + 1 = 14 := by
  rw [seed_affine_card_F11]

/-- `11` does not divide that order; hence the reduction carries no `11`-torsion. -/
theorem eleven_not_dvd_seed_card : ¬ (11 ∣ (seedAffinePoints.card + 1)) := by
  rw [seed_card_F11]; decide

end LocKer
