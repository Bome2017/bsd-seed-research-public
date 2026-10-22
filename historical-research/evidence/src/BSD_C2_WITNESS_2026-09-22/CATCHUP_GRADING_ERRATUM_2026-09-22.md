# Erratum to CATCHUP_GRADING_2026-09-22.md, §B (run 1, "sharp form")

Filed 2026-09-22 as a separate file. The graded file is left byte-identical because
`~/BSD_SUPERSINGULAR_SIGNED_BRIDGE_2026-09-22/SOURCE_BINDINGS.json` pins its sha256 (871a2287…).

**Recorded:** `c̄_2(p) = −c_{p−3}`.
**Correct:** `M_2 = Σ_x x² v(x) = −c_{p−3}` and `c̄_2 = −M_2/2`, hence **`c̄_2(p) = c_{p−3}/2`**.

Here `v(x) = Σ_{i<p} c_i x^i` is the Lagrange interpolant of the conductor-p² packet on F_p. Run 1's Lean states the
two facts separately (`momentZ_two_eq_neg_coeff`, `c2bar_eq_neg_inv_two_mul_moment_two`). Its report is right. The
grading conflated the moment with the coefficient.

Unit status is unchanged, since −2 is a unit: `c_2(p) ∈ Z_p^×  ⟺  M_2 ≠ 0  ⟺  c_{p−3} ≠ 0`. Numerical recheck over
p ∈ {5,7,11,13,23,29,131}, 200 random packets each: 0 violations. The supersingular counterpart is
`b̄_2 = +M_2/2 = −c_{p−3}/2` (see `~/BSD_SUPERSINGULAR_SIGNED_BRIDGE_REVIEW_2026-09-22/REVIEW.md` §3).
