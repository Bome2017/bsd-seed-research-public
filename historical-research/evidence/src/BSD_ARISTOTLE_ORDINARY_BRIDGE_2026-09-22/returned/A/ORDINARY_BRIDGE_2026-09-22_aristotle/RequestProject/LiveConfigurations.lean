import Mathlib

/-!
# Task 5 / Task 6 bookkeeping: the live-configuration enumeration

This file formalises the *purely arithmetic* content of the configuration count that appears in
Task 5 and Task 6 of the ordinary-bridge audit.  Nothing arithmetic-geometric is formalised here;
the inputs are the numerical shapes

* `s⁺ = 2 + d⁺`  (the rank-two Mordell–Weil contribution plus the plus-part corank of the
  divisible Shafarevich–Tate subgroup),
* `s⁻ = r⁻ + d⁻`,
* `σ = 4` together with the derived-height order inequality in the two forms used in the audit.

The point of the two theorems below is exactly the distinction the audit has to respect:
the inequality `σ ≥ 2·max(s⁺, s⁻)` forces `d⁺ = 0` but leaves six configurations alive, while
adding the minus-side input `s⁻ = 0` (which comes from the certified twist datum, not from the
inequality) leaves only the configuration with vanishing divisible part.
-/

namespace OrdinaryBridge

/-- **Task 5 (replayed).** If `σ = 4` and `σ ≥ 2·max(s⁺, s⁻)` with `s⁺ = 2 + d⁺` and
`s⁻ = r⁻ + d⁻`, then `d⁺ = 0` is forced, but exactly six configurations of `(r⁻, d⁻)` survive:
`(0,0)`, `(0,1)`, `(0,2)`, `(1,0)`, `(1,1)`, `(2,0)`.  In particular the inequality alone does
**not** force `d⁻ = 0`. -/
theorem live_configurations (dplus rminus dminus : ℕ)
    (h : 2 * max (2 + dplus) (rminus + dminus) ≤ 4) :
    dplus = 0 ∧
      ((rminus = 0 ∧ dminus = 0) ∨ (rminus = 0 ∧ dminus = 1) ∨ (rminus = 0 ∧ dminus = 2) ∨
        (rminus = 1 ∧ dminus = 0) ∨ (rminus = 1 ∧ dminus = 1) ∨ (rminus = 2 ∧ dminus = 0)) := by
  have h1 : 2 + dplus ≤ max (2 + dplus) (rminus + dminus) := le_max_left _ _
  have h2 : rminus + dminus ≤ max (2 + dplus) (rminus + dminus) := le_max_right _ _
  omega

/-- All six configurations of `live_configurations` are genuinely compatible with the inequality:
the enumeration is sharp, so the order inequality by itself cannot force the divisible part to
vanish. -/
theorem live_configurations_sharp :
    ∀ p ∈ [((0 : ℕ), (0 : ℕ), (0 : ℕ)), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 2, 0)],
      2 * max (2 + p.1) (p.2.1 + p.2.2) ≤ 4 := by
  decide

/-- **Task 6 (plus side, with the minus-side input).**  When the minus part of the pro-`p` Selmer
group vanishes (`s⁻ = r⁻ + d⁻ = 0`), the first anticyclotomic derived height vanishes identically,
so the order inequality reads `σ ≥ 2·rank S = 2·(2 + d⁺ + s⁻)`.  With `σ = 4` this forces the
whole divisible part to vanish: `d⁺ = d⁻ = 0`. -/
theorem divisible_part_vanishes (dplus rminus dminus : ℕ)
    (hminus : rminus + dminus = 0)
    (hrho : 2 * (2 + dplus + (rminus + dminus)) ≤ 4) :
    dplus = 0 ∧ dminus = 0 := by
  omega

end OrdinaryBridge
