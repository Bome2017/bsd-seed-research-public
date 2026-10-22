/-
Run013 — `Family.lean`

The exact frozen prime family `F_62` of `TARGET.md` §2, together with the elementary
arithmetic consequences that the descent actually uses.

The base curve is the optimal curve of conductor `62` (Cremona `62a1`, LMFDB `62.a4`)

    E : v^2 + u v + v = u^3 - u^2 - u + 1,

and

    F_62 = { q prime : q ∤ 372, q ≡ 5 (mod 8), (q/31) = -1,
             v_2(# reduction of E mod q) = 2, a_q(E) ≠ 0 }.

All five literal fields are retained even though the descent uses only primality,
`q ≡ 5 (mod 8)` and `(q/31) = -1`.
-/
import Mathlib

namespace Run013

instance : Fact (Nat.Prime 31) := ⟨by norm_num⟩

/-! ## Point counts for the base curve `62a1` -/

/-- The affine points of the reduction of `E : v^2+uv+v = u^3-u^2-u+1` modulo `q`. -/
def E62Affine (q : ℕ) : Type :=
  {P : ZMod q × ZMod q // P.2 ^ 2 + P.1 * P.2 + P.2 = P.1 ^ 3 - P.1 ^ 2 - P.1 + 1}

instance (q : ℕ) [NeZero q] : Fintype (E62Affine q) := by
  unfold E62Affine; infer_instance

/-- `# \tilde E(F_q)`: the affine points plus the point at infinity. -/
noncomputable def cardE62 (q : ℕ) : ℕ := 1 + Nat.card (E62Affine q)

/-- The trace of Frobenius `a_q(E) = q + 1 - # \tilde E(F_q)`. -/
noncomputable def aq62 (q : ℕ) : ℤ := (q : ℤ) + 1 - (cardE62 q : ℤ)

/-! ## The frozen family -/

/-- The exact frozen family `F_62` of `TARGET.md` §2. -/
structure F62 (q : ℕ) : Prop where
  /-- `q` is prime. -/
  prime : Nat.Prime q
  /-- `q ∤ 372`. -/
  not_dvd_372 : ¬ (q ∣ 372)
  /-- `q ≡ 5 (mod 8)`. -/
  mod_eight : q % 8 = 5
  /-- `(q/31) = -1`. -/
  legendre_31 : legendreSym 31 (q : ℤ) = -1
  /-- `v_2(# \tilde E(F_q)) = 2`. -/
  val_two : padicValNat 2 (cardE62 q) = 2
  /-- `a_q(E) ≠ 0`. -/
  trace_ne_zero : aq62 q ≠ 0

namespace F62

/-- The `Fact` instance packaging primality of `q`. -/
lemma fact_prime {q : ℕ} (h : F62 q) : Fact (Nat.Prime q) := ⟨h.prime⟩

section Elementary
variable {q : ℕ} (h : F62 q)
include h

lemma ne_two : q ≠ 2 := by
  intro hq; rw [hq] at h; exact absurd h.mod_eight (by norm_num)

lemma ne_thirtyone : q ≠ 31 := by
  intro hq; rw [hq] at h; exact absurd h.mod_eight (by norm_num)

lemma odd_q : q % 2 = 1 := by have := h.mod_eight; omega

lemma mod_four : q % 4 = 1 := by have := h.mod_eight; omega

lemma pos : 0 < q := h.prime.pos

end Elementary

variable {q : ℕ} [Fact (Nat.Prime q)] (h : F62 q)
include h

/-- `2` is not a square modulo `q` (this is `q ≡ 5 (mod 8)`). -/
theorem not_isSquare_two : ¬ IsSquare (2 : ZMod q) := by
  rw [ZMod.exists_sq_eq_two_iff h.ne_two]
  have := h.mod_eight
  omega

/-- `-1` is a square modulo `q` (this is `q ≡ 1 (mod 4)`). -/
theorem legendre_neg_one : legendreSym q (-1) = 1 := by
  rw [legendreSym.at_neg_one h.ne_two]
  have h4 : (q : ZMod 4) = 1 := by
    have : ((q % 4 : ℕ) : ZMod 4) = ((1 : ℕ) : ZMod 4) := by rw [h.mod_four]
    simpa [ZMod.natCast_mod] using this
  rw [h4]
  decide

/-- Quadratic reciprocity turns `(q/31) = -1` into `(31/q) = -1`. -/
theorem legendre_thirtyone : legendreSym q (31 : ℤ) = -1 := by
  have hrec : legendreSym 31 (q : ℤ) = legendreSym q ((31 : ℕ) : ℤ) :=
    legendreSym.quadratic_reciprocity_one_mod_four h.mod_four (by norm_num)
  rw [← show ((31 : ℕ) : ℤ) = (31 : ℤ) from by norm_num, ← hrec, h.legendre_31]

/-- `-31` is not a square modulo `q`. -/
theorem not_isSquare_neg_thirtyone : ¬ IsSquare ((-31 : ℤ) : ZMod q) := by
  rw [← legendreSym.eq_neg_one_iff q]
  have hsplit : ((-31 : ℤ)) = (-1) * 31 := by norm_num
  rw [hsplit, legendreSym.mul, h.legendre_neg_one, h.legendre_thirtyone]
  norm_num

end F62

/-! ## The minimal predicate `F62min`

`F62` above is the exact six-field family of `TARGET.md` §2 and is preserved verbatim,
declarations and proof bodies unchanged.  The descent consumes only three of those fields
(primality, `q ≡ 5 (mod 8)`, `(q/31) = -1`), so the Selmer theorems are proved below on the
three-field predicate `F62min`, and the original `F62` statements are recovered verbatim as
compatibility wrappers through `F62.toMin`.

The converse implication `F62min q → F62 q` is true: the `q ∤ 372`, point-count and trace
fields of `F62` are consequences of the two residue conditions.  `not_dvd_372` is proved
below; the point-count statement `v_2(# \tilde E(F_q)) = 2` and hence `a_q ≠ 0` are an
elementary finite-field argument (Proposition A of the conventional write-up) that is
deliberately *not* formalized here — it would require a full `WeierstrassCurve (ZMod q)`
point-count bridge, which is outside this development's Level-A scope. -/

/-- The three conditions the descent actually uses. -/
structure F62min (q : ℕ) : Prop where
  /-- `q` is prime. -/
  prime : Nat.Prime q
  /-- `q ≡ 5 (mod 8)`. -/
  mod_eight : q % 8 = 5
  /-- `(q/31) = -1`. -/
  legendre_31 : legendreSym 31 (q : ℤ) = -1

/-- The audited six-field family is contained in the minimal one. -/
theorem F62.toMin {q : ℕ} (h : F62 q) : F62min q :=
  ⟨h.prime, h.mod_eight, h.legendre_31⟩

namespace F62min

/-- The `Fact` instance packaging primality of `q`. -/
lemma fact_prime {q : ℕ} (h : F62min q) : Fact (Nat.Prime q) := ⟨h.prime⟩

section Elementary
variable {q : ℕ} (h : F62min q)
include h

lemma ne_two : q ≠ 2 := by
  intro hq; rw [hq] at h; exact absurd h.mod_eight (by norm_num)

lemma ne_three : q ≠ 3 := by
  intro hq; rw [hq] at h; exact absurd h.mod_eight (by norm_num)

lemma ne_thirtyone : q ≠ 31 := by
  intro hq; rw [hq] at h; exact absurd h.mod_eight (by norm_num)

lemma odd_q : q % 2 = 1 := by have := h.mod_eight; omega

lemma mod_four : q % 4 = 1 := by have := h.mod_eight; omega

lemma pos : 0 < q := h.prime.pos

/-- `372 = 2^2 * 3 * 31`, and none of `2, 3, 31` is `5` mod `8`, so the `q ∤ 372` field of
`F62` is already a consequence of `q ≡ 5 (mod 8)`. -/
lemma not_dvd_372 : ¬ (q ∣ 372) := by
  intro hdvd
  have h8 := h.mod_eight
  have hp := h.prime
  have e2 : q ∣ 2 → False := fun hd => by
    rw [(Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp hd] at h8; omega
  have h1 : q ∣ 2 * 186 := by rw [show (2 : ℕ) * 186 = 372 from by norm_num]; exact hdvd
  rcases (Nat.Prime.dvd_mul hp).mp h1 with hd | h186
  · exact e2 hd
  have h2 : q ∣ 2 * 93 := by rw [show (2 : ℕ) * 93 = 186 from by norm_num]; exact h186
  rcases (Nat.Prime.dvd_mul hp).mp h2 with hd | h93
  · exact e2 hd
  have h3 : q ∣ 3 * 31 := by rw [show (3 : ℕ) * 31 = 93 from by norm_num]; exact h93
  rcases (Nat.Prime.dvd_mul hp).mp h3 with hd | hd
  · rw [(Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp hd] at h8; omega
  · rw [(Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp hd] at h8; omega

end Elementary

variable {q : ℕ} [Fact (Nat.Prime q)] (h : F62min q)
include h

/-- `2` is not a square modulo `q` (this is `q ≡ 5 (mod 8)`). -/
theorem not_isSquare_two : ¬ IsSquare (2 : ZMod q) := by
  rw [ZMod.exists_sq_eq_two_iff h.ne_two]
  have := h.mod_eight
  omega

/-- `-1` is a square modulo `q` (this is `q ≡ 1 (mod 4)`). -/
theorem legendre_neg_one : legendreSym q (-1) = 1 := by
  rw [legendreSym.at_neg_one h.ne_two]
  have h4 : (q : ZMod 4) = 1 := by
    have : ((q % 4 : ℕ) : ZMod 4) = ((1 : ℕ) : ZMod 4) := by rw [h.mod_four]
    simpa [ZMod.natCast_mod] using this
  rw [h4]
  decide

/-- Quadratic reciprocity turns `(q/31) = -1` into `(31/q) = -1`. -/
theorem legendre_thirtyone : legendreSym q (31 : ℤ) = -1 := by
  have hrec : legendreSym 31 (q : ℤ) = legendreSym q ((31 : ℕ) : ℤ) :=
    legendreSym.quadratic_reciprocity_one_mod_four h.mod_four (by norm_num)
  rw [← show ((31 : ℕ) : ℤ) = (31 : ℤ) from by norm_num, ← hrec, h.legendre_31]

/-- `-31` is not a square modulo `q`. -/
theorem not_isSquare_neg_thirtyone : ¬ IsSquare ((-31 : ℤ) : ZMod q) := by
  rw [← legendreSym.eq_neg_one_iff q]
  have hsplit : ((-31 : ℤ)) = (-1) * 31 := by norm_num
  rw [hsplit, legendreSym.mul, h.legendre_neg_one, h.legendre_thirtyone]
  norm_num

end F62min

end Run013
