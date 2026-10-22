/-
Run013 — `FullTwoSelmer.lean`

**LEVEL B.**

Two parts.

1. *Unconditional.*  The four classes `1, -31, q, -31 q` are pairwise distinct, so the
   `phi_q`-Selmer group proved in `PhiSelmer.lean` has exactly `4` elements and the dual
   Selmer group has exactly `1`.

2. *Conditional on external input.*  Mathlib currently has no Galois cohomology, hence no
   `Sel_2(E/Q)` and no `Sha(E/Q)`.  The isogeny-Selmer comparison sequence of
   `BSD_CHAIN.md` §2 is therefore **not** re-proved here; it is supplied as an explicit
   hypothesis of the theorems below, which are pure (and completely proved) statements of
   finite group theory.  Everything in this section is labelled

       CONDITIONAL_ON_EXTERNAL_INPUT.

   No axiom is introduced.
-/
import RequestProject.Run013.PhiSelmer
import RequestProject.Run013.DualPhiSelmer

namespace Run013

/-! ## Distinctness of the four classes -/

theorem cls_eq_iff {a b : ℚ} (ha : a ≠ 0) (hb : b ≠ 0) :
    cls a = cls b ↔ ∃ t : ℚ, t ≠ 0 ∧ b = a * t ^ 2 := by
  rw [cls_of_ne ha, cls_of_ne hb, qcl_eq_qcl]
  constructor
  · rintro ⟨t, ht⟩
    refine ⟨(t : ℚ), t.ne_zero, ?_⟩
    have hc := congrArg (fun x : ℚˣ => (x : ℚ)) ht
    push_cast at hc
    exact hc
  · rintro ⟨t, ht, hab⟩
    refine ⟨Units.mk0 t ht, ?_⟩
    apply Units.ext
    push_cast
    exact hab

/-- A prime is not a rational square. -/
theorem not_isSquare_prime_rat {q : ℕ} (hq : q.Prime) : ¬ ∃ t : ℚ, (q : ℚ) = t ^ 2 := by
  rintro ⟨t, ht⟩
  have h1 : IsSquare ((q : ℕ) : ℚ) := ⟨t, by rw [ht]; ring⟩
  rw [Rat.isSquare_natCast_iff] at h1
  obtain ⟨a, ha⟩ := h1
  have hadvd : a ∣ q := ⟨a, ha⟩
  rcases (Nat.Prime.eq_one_or_self_of_dvd hq a hadvd) with rfl | rfl
  · simp at ha; exact hq.one_lt.ne' ha
  · have := hq.one_lt
    nlinarith [ha]

section Distinct

variable {q : ℕ}

theorem cls_one_ne_negthirtyone : cls (1 : ℚ) ≠ cls (-31 : ℚ) := by
  rw [Ne, cls_eq_iff one_ne_zero (by norm_num)]
  rintro ⟨t, ht, h⟩
  nlinarith [sq_nonneg t]

theorem cls_one_ne_q (hq : q.Prime) : cls (1 : ℚ) ≠ cls ((q : ℚ)) := by
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne_zero
  rw [Ne, cls_eq_iff one_ne_zero hq0]
  rintro ⟨t, ht, h⟩
  exact not_isSquare_prime_rat hq ⟨t, by linarith⟩

theorem cls_one_ne_negthirtyoneq (hq : 0 < q) :
    cls (1 : ℚ) ≠ cls (-(31 * (q : ℚ))) := by
  have hq0 : (0 : ℚ) < q := by exact_mod_cast hq
  rw [Ne, cls_eq_iff one_ne_zero (neg_ne_zero.mpr (by positivity))]
  rintro ⟨t, ht, h⟩
  nlinarith [sq_nonneg t]

theorem cls_negthirtyone_ne_q (hq : 0 < q) : cls (-31 : ℚ) ≠ cls ((q : ℚ)) := by
  have hq0 : (0 : ℚ) < q := by exact_mod_cast hq
  rw [Ne, cls_eq_iff (by norm_num) (by positivity)]
  rintro ⟨t, ht, h⟩
  nlinarith [sq_nonneg t]

theorem cls_negthirtyone_ne_negthirtyoneq (hq : q.Prime) :
    cls (-31 : ℚ) ≠ cls (-(31 * (q : ℚ))) := by
  have hq0 : (0 : ℚ) < q := by exact_mod_cast hq.pos
  rw [Ne, cls_eq_iff (by norm_num) (neg_ne_zero.mpr (by positivity))]
  rintro ⟨t, ht, h⟩
  exact not_isSquare_prime_rat hq ⟨t, by linarith⟩

theorem cls_q_ne_negthirtyoneq (hq : 0 < q) :
    cls ((q : ℚ)) ≠ cls (-(31 * (q : ℚ))) := by
  have hq0 : (0 : ℚ) < q := by exact_mod_cast hq
  rw [Ne, cls_eq_iff (by positivity) (neg_ne_zero.mpr (by positivity))]
  rintro ⟨t, ht, h⟩
  nlinarith [sq_nonneg t, mul_pos hq0 (mul_pos hq0 hq0)]

end Distinct

/-- **The `phi_q`-Selmer group has exactly four elements.** -/
theorem phi_selmer_ncard_min {q : ℕ} (hq : F62min q) :
    (SelmerSet (phiA q) (phiB q)).ncard = 4 := by
  have hqp := hq.prime
  have hqpos := hq.pos
  rw [phi_selmer_eq_min hq]
  rw [Set.ncard_insert_of_notMem (by
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff]
      push_neg
      exact ⟨cls_one_ne_negthirtyone, cls_one_ne_q hqp, cls_one_ne_negthirtyoneq hqpos⟩)
      (Set.toFinite _),
    Set.ncard_insert_of_notMem (by
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff]
      push_neg
      exact ⟨cls_negthirtyone_ne_q hqpos, cls_negthirtyone_ne_negthirtyoneq hqp⟩)
      (Set.toFinite _),
    Set.ncard_insert_of_notMem (by
      simp only [Set.mem_singleton_iff]
      exact cls_q_ne_negthirtyoneq hqpos) (Set.toFinite _),
    Set.ncard_singleton]

/-- The audited statement, preserved verbatim on the six-field family. -/
theorem phi_selmer_ncard {q : ℕ} (hq : F62 q) :
    (SelmerSet (phiA q) (phiB q)).ncard = 4 :=
  phi_selmer_ncard_min hq.toMin

/-- **The dual Selmer group has exactly one element.** -/
theorem dual_phi_selmer_ncard_min {q : ℕ} (hq : F62min q) :
    (SelmerSet (dualA q) (dualB q)).ncard = 1 := by
  rw [dual_phi_selmer_eq_min hq, Set.ncard_singleton]

/-- The audited statement, preserved verbatim on the six-field family. -/
theorem dual_phi_selmer_ncard {q : ℕ} (hq : F62 q) :
    (SelmerSet (dualA q) (dualB q)).ncard = 1 :=
  dual_phi_selmer_ncard_min hq.toMin

/-! ## Conditional consequences: full `2`-Selmer and Sha

`CONDITIONAL_ON_EXTERNAL_INPUT`.  The following are theorems of finite group theory.
They become the statements of `BSD_CHAIN.md` §2 once the (externally supplied)
isogeny-Selmer comparison sequence is instantiated. -/

/-- Exactness bookkeeping for
`0 → K → Sel^phi → Sel_2 → Sel^{hat phi}` with `#K = 2`, `#Sel^phi = 4`,
`#Sel^{hat phi} = 1`:  it forces `#Sel_2 = 2`.

This is the step that must **not** be replaced by multiplying the two isogeny-Selmer
orders: the order-`2` kernel term is divided out. -/
theorem card_middle_of_exact {A B C D : Type*} [CommGroup A] [CommGroup B] [CommGroup C]
    [CommGroup D] (f : A →* B) (g : B →* C) (h : C →* D)
    (hf : Function.Injective f)
    (hex1 : f.range = g.ker) (hex2 : g.range = h.ker)
    (hA : Nat.card A = 2) (hB : Nat.card B = 4) (hD : Nat.card D = 1) :
    Nat.card C = 2 := by
  -- `D` is trivial, hence `g` is surjective
  have hDsub : Subsingleton D := Nat.card_eq_one_iff_unique.mp hD |>.1
  have hker : h.ker = ⊤ := by
    ext z; simp [Subsingleton.elim (h z) 1]
  have hgsurj : Function.Surjective g := by
    intro c
    have : c ∈ g.range := by rw [hex2, hker]; trivial
    exact this
  -- `ker g = range f` has order `2`
  have hcardker : Nat.card (g.ker : Subgroup B) = 2 := by
    rw [← hex1, ← hA]
    exact Nat.card_congr (Equiv.ofBijective (f.rangeRestrict)
      ⟨fun a b hab => hf (congrArg Subtype.val hab), f.rangeRestrict_surjective⟩).symm
  -- the first isomorphism theorem
  have hiso : Nat.card (B ⧸ g.ker) = Nat.card C :=
    Nat.card_congr (QuotientGroup.quotientKerEquivOfSurjective g hgsurj).toEquiv
  have hsplit : Nat.card B = Nat.card (B ⧸ g.ker) * Nat.card (g.ker : Subgroup B) :=
    Subgroup.card_eq_card_quotient_mul_card_subgroup _
  rw [hcardker, hiso, hB] at hsplit
  omega

/-- Exactness bookkeeping for `0 → Sha(E)[phi] → Sha(E)[2] → Sha(E')[hat phi]`:
if the two outer groups are trivial then so is `Sha(E)[2]`.

This is exactly the step that distinguishes "rank zero" from "trivial `Sha[2]`":
rank information is not used. -/
theorem subsingleton_of_exact {X Y Z : Type*} [CommGroup X] [CommGroup Y] [CommGroup Z]
    (u : X →* Y) (v : Y →* Z) (hex : u.range = v.ker)
    (hX : Subsingleton X) (hZ : Subsingleton Z) : Subsingleton Y := by
  constructor
  intro y₁ y₂
  have key : ∀ y : Y, y = 1 := by
    intro y
    have hy : y ∈ v.ker := by simp [MonoidHom.mem_ker, Subsingleton.elim (v y) 1]
    rw [← hex] at hy
    obtain ⟨x, rfl⟩ := hy
    rw [Subsingleton.elim x 1, map_one]
  rw [key y₁, key y₂]

/-- A `2`-primary torsion abelian group with trivial `2`-torsion is trivial:
`Sha[2] = 0` upgrades to `Sha[2^∞] = 0`. -/
theorem eq_one_of_two_primary {G : Type*} [CommGroup G]
    (hpow : ∀ g : G, ∃ n : ℕ, g ^ (2 ^ n) = 1)
    (h2 : ∀ g : G, g ^ 2 = 1 → g = 1) : ∀ g : G, g = 1 := by
  have key : ∀ n : ℕ, ∀ g : G, g ^ (2 ^ n) = 1 → g = 1 := by
    intro n
    induction n with
    | zero => intro g hg; simpa using hg
    | succ m ih =>
        intro g hg
        refine ih g (h2 _ ?_)
        rw [← pow_mul, ← pow_succ]
        exact hg
  intro g
  obtain ⟨n, hn⟩ := hpow g
  exact key n g hn

end Run013
