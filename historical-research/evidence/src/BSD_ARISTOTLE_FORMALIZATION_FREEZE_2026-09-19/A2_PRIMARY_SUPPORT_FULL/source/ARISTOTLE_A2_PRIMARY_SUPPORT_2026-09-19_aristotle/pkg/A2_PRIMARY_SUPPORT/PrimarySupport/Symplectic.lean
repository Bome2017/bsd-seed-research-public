import PrimarySupport.Defs

/-!
# A2 — stretch target S1: a nondegenerate alternating pairing into a cyclic group

A finite abelian group carrying a nondegenerate alternating biadditive pairing into `ZMod N` has
square order.  The proof splits off hyperbolic planes: an element `x` of maximal order `m` pairs
onto a generator `c` of the image subgroup, which has order `m` as well; a partner `y` with
`β x y = c` also has order `m`; the plane `H` they span has order `m ^ 2` and its perpendicular `K`
is a complement carrying a pairing of the same kind, so induction on the order applies.
-/

namespace PrimarySupport

namespace Symp

variable {G : Type*} [AddCommGroup G] {N : ℕ}

lemma beta_zsmul_left (β : G →+ G →+ ZMod N) (a : ℤ) (x w : G) : β (a • x) w = a • β x w := by
  rw [map_zsmul, AddMonoidHom.zsmul_apply]

lemma beta_zsmul_right (β : G →+ G →+ ZMod N) (a : ℤ) (x w : G) : β x (a • w) = a • β x w :=
  map_zsmul (β x) a w

lemma beta_nsmul_left (β : G →+ G →+ ZMod N) (a : ℕ) (x w : G) : β (a • x) w = a • β x w := by
  rw [map_nsmul, AddMonoidHom.nsmul_apply]

lemma beta_nsmul_right (β : G →+ G →+ ZMod N) (a : ℕ) (x w : G) : β x (a • w) = a • β x w :=
  map_nsmul (β x) a w

/-- An alternating pairing is skew. -/
lemma beta_skew (β : G →+ G →+ ZMod N) (halt : ∀ x, β x x = 0) (x y : G) : β x y = - β y x := by
  have h : β x x + β y x + (β x y + β y y) = 0 := by
    have h2 := halt (x + y)
    simpa [map_add, AddMonoidHom.add_apply] using h2
  rw [halt x, halt y] at h
  linear_combination (norm := abel) h

/-- In a cyclic group, an element killed by `m` is a multiple of any element of order `m`. -/
lemma zmod_mem_zmultiples {m : ℕ} (hm : 0 < m) {c z : ZMod N} (hc : addOrderOf c = m)
    (hz : m • z = 0) : ∃ k : ℤ, z = k • c := by
  classical
  let T : AddSubgroup (ZMod N) :=
    { carrier := {w | m • w = 0}
      zero_mem' := by simp
      add_mem' := by
        intro a b ha hb
        simp only [Set.mem_setOf_eq] at *
        rw [smul_add, ha, hb, add_zero]
      neg_mem' := by
        intro a ha
        simp only [Set.mem_setOf_eq] at *
        rw [smul_neg, ha, neg_zero] }
  have hcT : c ∈ T := by
    show m • c = 0
    rw [← hc]
    exact addOrderOf_nsmul_eq_zero c
  have hzT : z ∈ T := hz
  obtain ⟨g, hg⟩ := (inferInstance : IsAddCyclic T).exists_zsmul_surjective
  have hgT : m • (g : ZMod N) = 0 := g.2
  have hTeq : T = AddSubgroup.zmultiples (g : ZMod N) := by
    apply le_antisymm
    · intro w hw
      obtain ⟨k, hk⟩ := hg ⟨w, hw⟩
      exact ⟨k, congrArg Subtype.val hk⟩
    · rintro w ⟨k, rfl⟩
      exact T.zsmul_mem g.2 k
  have hgord : addOrderOf (g : ZMod N) ∣ m := addOrderOf_dvd_of_nsmul_eq_zero hgT
  haveI hTfin : Finite T := by
    rw [hTeq]
    refine Nat.finite_of_card_ne_zero ?_
    rw [Nat.card_zmultiples]
    exact (Nat.pos_of_dvd_of_pos hgord hm).ne'
  have hcard : Nat.card T ≤ m := by
    rw [hTeq, Nat.card_zmultiples]
    exact Nat.le_of_dvd hm hgord
  have hceq : AddSubgroup.zmultiples c = T := by
    refine AddSubgroup.eq_of_le_of_card_ge ?_ ?_
    · rintro w ⟨k, rfl⟩
      exact T.zsmul_mem hcT k
    · rw [Nat.card_zmultiples, hc]
      exact hcard
  rw [← hceq] at hzT
  obtain ⟨k, hk⟩ := hzT
  exact ⟨k, hk.symm⟩

/-- The order of an internal direct sum of two subgroups with trivial intersection. -/
lemma card_sup_eq_mul (H K : AddSubgroup G) (hinf : H ⊓ K = ⊥) :
    Nat.card (H ⊔ K : AddSubgroup G) = Nat.card H * Nat.card K := by
  have hb : Function.Bijective
      (fun p : H × K => (⟨(p.1 : G) + (p.2 : G),
        AddSubgroup.mem_sup.mpr ⟨p.1, p.1.2, p.2, p.2.2, rfl⟩⟩ : (H ⊔ K : AddSubgroup G))) := by
    constructor
    · rintro ⟨⟨h, hh⟩, ⟨k, hk⟩⟩ ⟨⟨h', hh'⟩, ⟨k', hk'⟩⟩ heq
      have heq' : h + k = h' + k' := congrArg Subtype.val heq
      have hmem : h - h' ∈ H ⊓ K := by
        refine ⟨H.sub_mem hh hh', ?_⟩
        have hrw : h - h' = k' - k := by linear_combination (norm := abel) heq'
        rw [hrw]
        exact K.sub_mem hk' hk
      rw [hinf] at hmem
      have hh0 : h - h' = 0 := hmem
      have hhh : h = h' := by linear_combination (norm := abel) hh0
      subst hhh
      have hkk : k = k' := by linear_combination (norm := abel) heq'
      subst hkk
      rfl
    · rintro ⟨w, hw⟩
      obtain ⟨h, hh, k, hk, rfl⟩ := AddSubgroup.mem_sup.mp hw
      exact ⟨(⟨h, hh⟩, ⟨k, hk⟩), rfl⟩
  rw [← Nat.card_eq_of_bijective _ hb, Nat.card_prod]

/-- Main induction for S1. -/
theorem isSquare_card_aux : ∀ (n : ℕ) (G : Type) [AddCommGroup G] [Finite G] (N : ℕ)
    (β : G →+ G →+ ZMod N), Nat.card G ≤ n → (∀ x, β x x = 0) →
    (∀ x, (∀ y, β x y = 0) → x = 0) → IsSquare (Nat.card G) := by
  intro n
  induction n with
  | zero =>
    intro G _ _ N β hle _ _
    exact absurd hle (by simpa using Nat.card_pos.ne')
  | succ n ih =>
    intro G _ _ N β hle halt hnd
    by_cases htriv : ∀ x : G, x = 0
    · have hone : Nat.card G = 1 := by
        haveI : Subsingleton G := ⟨fun a b => by rw [htriv a, htriv b]⟩
        simp
      exact ⟨1, by rw [hone, one_mul]⟩
    push_neg at htriv
    haveI : Nontrivial G := by
      obtain ⟨z, hz⟩ := htriv
      exact ⟨0, z, fun h => hz h.symm⟩
    obtain ⟨x, hx⟩ : ∃ x : G, addOrderOf x = AddMonoid.exponent G :=
      AddMonoid.exists_addOrderOf_eq_exponent AddMonoid.ExponentExists.of_finite
    set m := AddMonoid.exponent G with hm
    have hm1 : 1 < m := AddMonoid.one_lt_exponent
    have hm0 : 0 < m := lt_trans Nat.zero_lt_one hm1
    have hmx : m • x = 0 := by rw [← hx]; exact addOrderOf_nsmul_eq_zero x
    -- a partner `y` pairing with `x` onto a generator of the image
    obtain ⟨g, hg⟩ := (inferInstance : IsAddCyclic (β x).range).exists_zsmul_surjective
    set c : ZMod N := (g : ZMod N) with hc
    have hgen : ∀ z ∈ (β x).range, ∃ k : ℤ, z = k • c := by
      intro z hz
      obtain ⟨k, hk⟩ := hg ⟨z, hz⟩
      exact ⟨k, (congrArg Subtype.val hk).symm⟩
    obtain ⟨y, hy⟩ : ∃ y : G, β x y = c := g.2
    have hcm : m • c = 0 := by
      rw [← hy, ← beta_nsmul_left β m x y, hmx, map_zero, AddMonoidHom.zero_apply]
    have hordc : addOrderOf c = m := by
      refine Nat.dvd_antisymm (addOrderOf_dvd_of_nsmul_eq_zero hcm) ?_
      rw [← hx]
      refine addOrderOf_dvd_of_nsmul_eq_zero (hnd _ ?_)
      intro z
      obtain ⟨k, hk⟩ := hgen (β x z) ⟨z, rfl⟩
      rw [beta_nsmul_left β (addOrderOf c) x z, hk, smul_comm, addOrderOf_nsmul_eq_zero c,
        smul_zero]
    -- `y` also has order `m`
    have hmy : m • y = 0 := by
      have hdvd : addOrderOf y ∣ m := AddMonoid.addOrder_dvd_exponent y
      exact addOrderOf_dvd_iff_nsmul_eq_zero.mp hdvd
    have hordy : addOrderOf y = m := by
      refine Nat.dvd_antisymm (AddMonoid.addOrder_dvd_exponent y : addOrderOf y ∣ m) ?_
      rw [← hordc]
      refine addOrderOf_dvd_of_nsmul_eq_zero ?_
      rw [← hy, ← beta_nsmul_right β (addOrderOf y) x y, addOrderOf_nsmul_eq_zero y, map_zero]
    -- arithmetic helpers
    have hzsmul_zero : ∀ (a : ℤ) (z : G), m • z = 0 → (m : ℤ) ∣ a → a • z = 0 := by
      rintro a z hz ⟨k, rfl⟩
      rw [mul_comm, mul_zsmul, natCast_zsmul, hz, smul_zero]
    have hdvd_of_zsmul_c : ∀ a : ℤ, a • c = 0 → (m : ℤ) ∣ a := by
      intro a ha
      rw [← hordc]
      exact addOrderOf_dvd_iff_zsmul_eq_zero.mpr ha
    -- the hyperbolic plane and its perpendicular
    set H : AddSubgroup G := AddSubgroup.zmultiples x ⊔ AddSubgroup.zmultiples y with hH
    set K : AddSubgroup G :=
      { carrier := {z | ∀ w ∈ H, β z w = 0}
        zero_mem' := by intro w _; simp
        add_mem' := by
          intro a b ha hb w hw
          simp only [Set.mem_setOf_eq] at *
          rw [map_add, AddMonoidHom.add_apply, ha w hw, hb w hw, add_zero]
        neg_mem' := by
          intro a ha w hw
          simp only [Set.mem_setOf_eq] at *
          rw [map_neg, AddMonoidHom.neg_apply, ha w hw, neg_zero] } with hK
    have hxH : x ∈ H := AddSubgroup.mem_sup_left (AddSubgroup.mem_zmultiples x)
    have hyH : y ∈ H := AddSubgroup.mem_sup_right (AddSubgroup.mem_zmultiples y)
    have hmemH : ∀ w ∈ H, ∃ a b : ℤ, w = a • x + b • y := by
      intro w hw
      obtain ⟨u, hu, v, hv, rfl⟩ := AddSubgroup.mem_sup.mp hw
      obtain ⟨a, ha⟩ := hu
      obtain ⟨b, hb⟩ := hv
      exact ⟨a, b, by rw [← ha, ← hb]⟩
    have hK_iff : ∀ z : G, β z x = 0 → β z y = 0 → z ∈ K := by
      intro z h1 h2 w hw
      obtain ⟨a, b, rfl⟩ := hmemH w hw
      rw [map_add, beta_zsmul_right β a z x, beta_zsmul_right β b z y, h1, h2, smul_zero,
        smul_zero, add_zero]
    have hpair_plane : ∀ a b : ℤ, β (a • x + b • y) x = -(b • c) ∧ β (a • x + b • y) y = a • c := by
      intro a b
      constructor
      · rw [map_add, AddMonoidHom.add_apply, beta_zsmul_left β a x x, beta_zsmul_left β b y x,
          halt x, smul_zero, zero_add, beta_skew β halt y x, hy, smul_neg]
      · rw [map_add, AddMonoidHom.add_apply, beta_zsmul_left β a x y, beta_zsmul_left β b y y,
          halt y, smul_zero, add_zero, hy]
    -- `H ⊓ K = ⊥`
    have hinfHK : H ⊓ K = ⊥ := by
      rw [AddSubgroup.eq_bot_iff_forall]
      rintro w ⟨hwH, hwK⟩
      obtain ⟨a, b, rfl⟩ := hmemH w hwH
      have h1 : β (a • x + b • y) x = 0 := hwK x hxH
      have h2 : β (a • x + b • y) y = 0 := hwK y hyH
      rw [(hpair_plane a b).1] at h1
      rw [(hpair_plane a b).2] at h2
      have hb : b • c = 0 := by
        have hneg : -(b • c) = 0 := h1
        simpa using hneg
      rw [hzsmul_zero a x hmx (hdvd_of_zsmul_c a h2), hzsmul_zero b y hmy (hdvd_of_zsmul_c b hb),
        add_zero]
    -- `H ⊔ K = ⊤`
    have hsupHK : H ⊔ K = ⊤ := by
      rw [eq_top_iff]
      intro z _
      have hu : m • (-(β z x)) = 0 := by
        rw [smul_neg, ← beta_nsmul_right β m z x, hmx, map_zero, neg_zero]
      have hv : m • (β z y) = 0 := by
        rw [← beta_nsmul_right β m z y, hmy, map_zero]
      obtain ⟨b, hb⟩ := zmod_mem_zmultiples hm0 hordc hu
      obtain ⟨a, ha⟩ := zmod_mem_zmultiples hm0 hordc hv
      have hhH : a • x + b • y ∈ H :=
        AddSubgroup.add_mem _ (AddSubgroup.mem_sup_left ⟨a, rfl⟩)
          (AddSubgroup.mem_sup_right ⟨b, rfl⟩)
      have hzk : z - (a • x + b • y) ∈ K := by
        refine hK_iff _ ?_ ?_
        · rw [map_sub, AddMonoidHom.sub_apply, (hpair_plane a b).1, ← hb]
          abel
        · rw [map_sub, AddMonoidHom.sub_apply, (hpair_plane a b).2, ← ha, sub_self]
      exact AddSubgroup.mem_sup.mpr ⟨_, hhH, _, hzk, by abel⟩
    -- cardinalities
    have hcardH : Nat.card H = m * m := by
      have hinfxy : AddSubgroup.zmultiples x ⊓ AddSubgroup.zmultiples y = ⊥ := by
        rw [AddSubgroup.eq_bot_iff_forall]
        rintro w ⟨⟨a, ha⟩, ⟨b, hb⟩⟩
        have hwy : β w y = a • c := by rw [← ha]; exact beta_zsmul_left β a x y ▸ (by rw [hy])
        have hwy0 : β w y = 0 := by
          rw [← hb, beta_zsmul_left β b y y, halt y, smul_zero]
        have hac : a • c = 0 := by rw [← hwy, hwy0]
        rw [← ha]
        exact hzsmul_zero a x hmx (hdvd_of_zsmul_c a hac)
      rw [hH, card_sup_eq_mul _ _ hinfxy, Nat.card_zmultiples, Nat.card_zmultiples, hx, hordy]
    have hcardG : Nat.card G = (m * m) * Nat.card K := by
      have h1 : Nat.card (H ⊔ K : AddSubgroup G) = Nat.card H * Nat.card K :=
        card_sup_eq_mul H K hinfHK
      rw [hsupHK] at h1
      rw [← hcardH, ← h1, Nat.card_congr (AddSubgroup.topEquiv (G := G)).toEquiv]
    -- the restricted pairing on `K`
    let β' : K →+ K →+ ZMod N :=
      AddMonoidHom.mk' (fun z : K => (β (z : G)).comp K.subtype)
        (fun a b => by ext w; simp)
    have halt' : ∀ z : K, β' z z = 0 := fun z => halt (z : G)
    have hnd' : ∀ z : K, (∀ w : K, β' z w = 0) → z = 0 := by
      intro z hz
      have hzero : ∀ w : G, β (z : G) w = 0 := by
        intro w
        have hw : w ∈ H ⊔ K := by rw [hsupHK]; trivial
        obtain ⟨h, hh, k, hk, rfl⟩ := AddSubgroup.mem_sup.mp hw
        have h1 : β (z : G) h = 0 := z.2 h hh
        have h2 : β (z : G) k = 0 := hz ⟨k, hk⟩
        rw [map_add, h1, h2, add_zero]
      exact Subtype.ext (hnd (z : G) hzero)
    have hcardK : Nat.card K ≤ n := by
      have hKpos : 0 < Nat.card K := Nat.card_pos
      have : Nat.card K < Nat.card G := by
        rw [hcardG]
        calc Nat.card K = 1 * Nat.card K := (one_mul _).symm
          _ < (m * m) * Nat.card K := by
              refine (Nat.mul_lt_mul_right hKpos).mpr ?_
              nlinarith
      omega
    obtain ⟨t, ht⟩ := ih K N β' hcardK halt' hnd'
    exact ⟨m * t, by rw [hcardG, ht]; ring⟩

/-- S1. -/
theorem isSquare_card (G : Type) [AddCommGroup G] [Finite G] (N : ℕ) (β : G →+ G →+ ZMod N)
    (halt : ∀ x, β x x = 0) (hnd : ∀ x, (∀ y, β x y = 0) → x = 0) : IsSquare (Nat.card G) :=
  isSquare_card_aux (Nat.card G) G N β le_rfl halt hnd

end Symp

end PrimarySupport
