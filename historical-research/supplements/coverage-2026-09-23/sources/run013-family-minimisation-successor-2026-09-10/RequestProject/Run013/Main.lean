/-
Run013 — `Main.lean`

The exported headline theorem: the frozen primary target of `TARGET.md` §4.

For every `q` in the exact frozen family `F_62`,

    Sel^{phi_q}(E_q / Q)      = {1, -31, q, -31 q},
    Sel^{hat phi_q}(E'_q / Q) = {1}.

Here `SelmerSet a b` is the honest isogeny-Selmer group inside `Q*/Q*^2` (see
`Selmer.lean`), `(phiA q, phiB q) = (30 q, -31 q^2)` are the coefficients of `E'_q` and
`(dualA q, dualB q) = (-15 q, 64 q^2)` are the coefficients of `E_q`, which is what fixes
the orientation (see `Isogeny.lean`, `phi_coeffs` and `dual_coeffs`).
-/
import RequestProject.Run013.PhiSelmer
import RequestProject.Run013.DualPhiSelmer
import RequestProject.Run013.Isogeny
import RequestProject.Run013.LocalThirtyOne
import RequestProject.Run013.FullTwoSelmer
import RequestProject.Run013.BSDTwoBookkeeping

namespace Run013

/-- **RUN013 PRIMARY THEOREM.**

For every prime `q` in the frozen family `F_62`, the `phi_q`-Selmer group of `E_q` is
exactly `{1, -31, q, -31 q}` and the dual `hat phi_q`-Selmer group of `E'_q` is trivial. -/
theorem run013_primary_theorem_min {q : ℕ} (hq : F62min q) :
    SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls ((q : ℚ)), cls (-(31 * (q : ℚ)))} ∧
    SelmerSet (dualA q) (dualB q) = {cls 1} :=
  ⟨phi_selmer_eq_min hq, dual_phi_selmer_eq_min hq⟩

/-- The audited statement, preserved verbatim on the six-field family. -/
theorem run013_primary_theorem {q : ℕ} (hq : F62 q) :
    SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls ((q : ℚ)), cls (-(31 * (q : ℚ)))} ∧
    SelmerSet (dualA q) (dualB q) = {cls 1} :=
  run013_primary_theorem_min hq.toMin

/-- The two Selmer orders that feed the isogeny-Selmer comparison. -/
theorem run013_selmer_orders_min {q : ℕ} (hq : F62min q) :
    (SelmerSet (phiA q) (phiB q)).ncard = 4 ∧ (SelmerSet (dualA q) (dualB q)).ncard = 1 :=
  ⟨phi_selmer_ncard_min hq, dual_phi_selmer_ncard_min hq⟩

/-- The audited statement, preserved verbatim on the six-field family. -/
theorem run013_selmer_orders {q : ℕ} (hq : F62 q) :
    (SelmerSet (phiA q) (phiB q)).ncard = 4 ∧ (SelmerSet (dualA q) (dualB q)).ncard = 1 :=
  run013_selmer_orders_min hq.toMin

end Run013
