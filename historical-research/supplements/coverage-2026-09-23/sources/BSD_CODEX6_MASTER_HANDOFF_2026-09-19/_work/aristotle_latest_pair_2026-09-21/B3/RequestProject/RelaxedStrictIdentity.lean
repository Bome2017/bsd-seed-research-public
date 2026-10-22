import Mathlib

/-!
# The relaxed/strict dimension identity does not transpose bounds

The Greenberg–Wiles comparison between a strict Selmer structure and its relaxed dual
produced, in the earlier report, the relation

    dim Sel_rel = dim Sel_str + 1 + d,      d = dim E(Q_p)[p],

and the report then asserted that an upper bound for one side yields a *lower* bound for the
other.  That inference is invalid, and this file records the correct elementary logic.

* `RelStr.le_of_le` : from `x = y + C`, an upper bound `y ≤ B` gives the upper bound
  `x ≤ B + C`.  Upper bounds transfer to upper bounds.
* `RelStr.le_of_le'` : symmetrically, `x ≤ B` gives `y ≤ B`.
* `RelStr.lower_from_lower` : a *lower* bound on one side gives a lower bound on the other;
  that is the only direction in which lower bounds propagate.
* `RelStr.no_bound` : the identity by itself bounds neither side — for every `B` there are
  solutions with both sides larger than `B`.

Consequently the identity alone cannot be used as the "exact remaining arrow": producing an
upper bound for `Ш` from auxiliary classes needs an extra orthogonality or annihilation
input, which the identity does not supply.
-/

namespace RelStr

theorem le_of_le {x y C B : ℕ} (h : x = y + C) (hy : y ≤ B) : x ≤ B + C := by omega

theorem le_of_le' {x y C B : ℕ} (h : x = y + C) (hx : x ≤ B) : y ≤ B := by omega

theorem lower_from_lower {x y C B : ℕ} (h : x = y + C) (hy : B ≤ y) : B + C ≤ x := by omega

/-- The identity `x = y + C` puts no upper bound on either side. -/
theorem no_bound (C B : ℕ) : ∃ x y : ℕ, x = y + C ∧ B < x ∧ B < y :=
  ⟨B + 1 + C, B + 1, rfl, by omega, by omega⟩

end RelStr
