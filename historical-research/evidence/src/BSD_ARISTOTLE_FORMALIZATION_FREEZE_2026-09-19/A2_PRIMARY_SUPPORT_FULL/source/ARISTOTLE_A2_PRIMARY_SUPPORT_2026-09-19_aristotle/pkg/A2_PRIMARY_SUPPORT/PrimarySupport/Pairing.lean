import PrimarySupport.Defs

/-!
# A2 — stretch target S2: a nondegenerate alternating pairing with a NON-cyclic target

The cross product on `(ZMod 2)^3` is alternating and nondegenerate, on a group of order `8`, which
is not a square.  This is the reason the square-order statement S1 needs a cyclic target.
-/

namespace PrimarySupport

/-- The cross product on `(ZMod 2)^3`. -/
def crossZ2 (x y : Fin 3 → ZMod 2) : Fin 3 → ZMod 2 :=
  ![x 1 * y 2 - x 2 * y 1, x 2 * y 0 - x 0 * y 2, x 0 * y 1 - x 1 * y 0]

lemma crossZ2_add_right (x y z : Fin 3 → ZMod 2) :
    crossZ2 x (y + z) = crossZ2 x y + crossZ2 x z := by
  funext i
  fin_cases i <;> simp [crossZ2] <;> ring

lemma crossZ2_add_left (x y z : Fin 3 → ZMod 2) :
    crossZ2 (x + y) z = crossZ2 x z + crossZ2 y z := by
  funext i
  fin_cases i <;> simp [crossZ2] <;> ring

/-- The cross product as a biadditive map. -/
def crossHom : (Fin 3 → ZMod 2) →+ (Fin 3 → ZMod 2) →+ (Fin 3 → ZMod 2) :=
  AddMonoidHom.mk'
    (fun x => AddMonoidHom.mk' (fun y => crossZ2 x y) (crossZ2_add_right x))
    (fun x y => AddMonoidHom.ext fun z => crossZ2_add_left x y z)

lemma crossHom_apply (x y : Fin 3 → ZMod 2) : crossHom x y = crossZ2 x y := rfl

lemma crossZ2_self (x : Fin 3 → ZMod 2) : crossZ2 x x = 0 := by
  funext i
  fin_cases i <;> simp [crossZ2] <;> ring

lemma crossZ2_nondegenerate (x : Fin 3 → ZMod 2) (h : ∀ y, crossZ2 x y = 0) : x = 0 := by
  have e1 := congrFun (h ![1, 0, 0]) 1
  have e2 := congrFun (h ![1, 0, 0]) 2
  have e0 := congrFun (h ![0, 1, 0]) 2
  simp [crossZ2] at e0 e1 e2
  funext i
  fin_cases i <;> simp_all

lemma not_isSquare_eight : ¬ IsSquare (8 : ℕ) := by
  rintro ⟨r, hr⟩
  have hr8 : r ≤ 8 := by nlinarith
  interval_cases r <;> omega

end PrimarySupport
