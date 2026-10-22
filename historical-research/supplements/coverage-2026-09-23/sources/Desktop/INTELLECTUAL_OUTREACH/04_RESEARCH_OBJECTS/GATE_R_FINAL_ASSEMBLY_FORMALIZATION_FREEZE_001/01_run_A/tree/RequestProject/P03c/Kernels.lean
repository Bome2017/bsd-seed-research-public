import RequestProject.P03b.Additivity

namespace P03c

open Run013 SDyadic Descent P01 P03a P03b WeierstrassCurve

/-! # P03c — the bundled homomorphisms and their exact kernels

P03a built `phiPoint` and `dualPhiPoint` as total functions on mathlib's actual point types.
P03b certified that both respect the group law.  **Both are double-run Lean certified.**

Two things follow, and this file is exactly those two things:

1. the maps may now legitimately be **bundled** as additive homomorphisms — that needs
   `map_add`, which is `P03b.isogeny_point_maps_additive`, and nothing else;
2. their **exact kernels** can be computed.

The bundling below is plumbing and is proved.  The kernel theorem is the single target.

## Why the kernels should be short

For `φ`, suppose `φ(P) = O`.

* `P = O` is immediate.
* `P = some h` with `x = 0`: on these models `x = 0` forces `y = 0`
  (`Descent.Wab_x_eq_zero`), so `P` is the point `(0,0)`, which is `P01.Tpt hP`.
* `P = some h` with `x ≠ 0`: by `P03a.phiPoint_some_of_ne` the image is an actual
  `Affine.Point.some`, and `WeierstrassCurve.Affine.Point.some_ne_zero` says that is never
  `O`.  Contradiction.

The dual side is the same argument with `T'` in place of `T`.

**No new algebraic identity is needed.**  P03a already encoded precisely the exceptional
fibres whose classification becomes this theorem, and P01 already named the points.  That is
the staging paying off, and it is why this target is much smaller than P03b's.

## Boundary

NOT in this file, and not to be added:
`φ̂ ∘ φ = [2]`, `φ ∘ φ̂ = [2]`, any composite identity, field-embedding naturality,
`ker δ = im φ`, `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD.
-/

/-- `φ` bundled as an additive homomorphism.  `map_add` is the certified P03b theorem. -/
noncomputable def phiHom {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (Ecurve ε m q).toAffine.Point →+ (E'curve ε m q).toAffine.Point :=
  AddMonoidHom.mk' (phiPoint hP) (isogeny_point_maps_additive ε m q hP).1

/-- `φ̂` bundled as an additive homomorphism. -/
noncomputable def dualPhiHom {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point →+ (Ecurve ε m q).toAffine.Point :=
  AddMonoidHom.mk' (dualPhiPoint hP) (isogeny_point_maps_additive ε m q hP).2

@[simp] theorem phiHom_apply {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (Ecurve ε m q).toAffine.Point) : phiHom hP P = phiPoint hP P := rfl

@[simp] theorem dualPhiHom_apply {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (E'curve ε m q).toAffine.Point) : dualPhiHom hP P = dualPhiPoint hP P := rfl

/-! ## The P03c target -/

/--
**Target.**  The exact kernels of the two bundled homomorphisms.

`ker φ = {O, T}` and `ker φ̂ = {O, T'}` — stated as membership, which is the form every
later stage will consume.  `Tpt` and `T'pt` are P01's named points `(0,0)` on `E_q` and
`E'_q` respectively.

This is a kernel theorem about **actual** `AddMonoidHom`s between **actual** mathlib point
groups.  It is not a statement about `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш or rank, and it says nothing
about the composites `φ̂ ∘ φ` or `φ ∘ φ̂`, which are P03d. -/
theorem isogeny_kernels (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (∀ P : (Ecurve ε m q).toAffine.Point,
        P ∈ (phiHom hP).ker ↔ P = 0 ∨ P = Tpt hP)
  ∧ (∀ P : (E'curve ε m q).toAffine.Point,
        P ∈ (dualPhiHom hP).ker ↔ P = 0 ∨ P = T'pt hP) := by
  constructor
  · intro P
    rw [AddMonoidHom.mem_ker, phiHom_apply]
    constructor
    · intro h
      cases P with
      | zero => exact Or.inl rfl
      | some hns =>
        rename_i x y
        by_cases hx : x = 0
        · subst hx
          have hy : y = 0 := Wab_x_eq_zero (a := dualA ε m q) (b := dualB ε m q) hns.left
          subst hy
          exact Or.inr (Wab_pt_eq hns (T_mem hP) rfl rfl)
        · rw [phiPoint_some_of_ne hP hns hx] at h
          exact absurd h (Affine.Point.some_ne_zero _)
    · rintro (rfl | rfl)
      · exact phiPoint_zero hP
      · exact phiPoint_Tpt hP
  · intro P
    rw [AddMonoidHom.mem_ker, dualPhiHom_apply]
    constructor
    · intro h
      cases P with
      | zero => exact Or.inl rfl
      | some hns =>
        rename_i X Y
        by_cases hX : X = 0
        · subst hX
          have hY : Y = 0 := Wab_x_eq_zero (a := phiA ε m q) (b := phiB ε m q) hns.left
          subst hY
          exact Or.inr (Wab_pt_eq hns (T'_mem hP) rfl rfl)
        · rw [dualPhiPoint_some_of_ne hP hns hX] at h
          exact absurd h (Affine.Point.some_ne_zero _)
    · rintro (rfl | rfl)
      · exact dualPhiPoint_zero hP
      · exact dualPhiPoint_T'pt hP

end P03c
