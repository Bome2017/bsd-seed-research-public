/-
Run013 — `LocalInfinity.lean`

The archimedean local condition of `src/infinity/INFINITY.md`.

For `q > 0` and `d < 0` every term of the dual covering
  `n^2 = d u^4 - 15 q u^2 v^2 + (64 q^2 / d) v^4`
is nonpositive, and at least one is strictly negative on a nonzero projective pair.
Hence the dual covering has no real point in a negative square class.
-/
import RequestProject.Run013.Basic

namespace Run013

/-- **Archimedean exclusion for the dual covering.** -/
theorem localinf_dual (q : ℝ) (hq : 0 < q) (d : ℝ) (hd : d < 0) :
    ¬ Cov ℝ (-15 * q) (64 * q ^ 2) d := by
  rintro ⟨u, v, n, huv, hn⟩
  have hd' : (64 * q ^ 2) / d < 0 := div_neg_of_pos_of_neg (by positivity) hd
  have h1 : d * u ^ 4 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hd.le (by positivity)
  have h2 : (-15 * q) * u ^ 2 * v ^ 2 ≤ 0 := by
    have : (0:ℝ) ≤ u ^ 2 * v ^ 2 := by positivity
    nlinarith
  have h3 : (64 * q ^ 2 / d) * v ^ 4 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hd'.le (by positivity)
  have hn2 : (0 : ℝ) ≤ n ^ 2 := sq_nonneg n
  by_cases hu : u = 0
  · have hv : v ≠ 0 := fun h => huv ⟨hu, h⟩
    have h3' : (64 * q ^ 2 / d) * v ^ 4 < 0 :=
      mul_neg_of_neg_of_pos hd' (by positivity)
    nlinarith
  · have h1' : d * u ^ 4 < 0 := mul_neg_of_neg_of_pos hd (by positivity)
    nlinarith

end Run013
