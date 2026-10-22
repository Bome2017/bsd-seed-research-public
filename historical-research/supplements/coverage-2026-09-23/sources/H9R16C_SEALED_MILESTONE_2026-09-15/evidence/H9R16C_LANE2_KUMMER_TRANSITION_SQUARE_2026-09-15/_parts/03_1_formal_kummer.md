# 03 — Derivation (Lane 2)

## 03.1 The formal part: Kummer naturality over a fixed base

**Lemma F (fixed-base Kummer naturality).** Let `F` be a number field, `A`, `B` abelian varieties
over `F`, and `φ ∈ Hom_F(A,B) ⊗_Z Z_p`. Write `Â(F) := A(F) ⊗ Z_p` and
`Kum_A : Â(F) → H^1(F, T_pA) := lim_n H^1(F, A[p^n])`. Then

    (F1)  Kum_B ∘ φ = H^1(F, T_pφ) ∘ Kum_A          on Â(F);
    (F2)  Kum_A is injective;
    (F3)  for L/F finite, res_{L/F}: H^1(F, T_pA) → H^1(L, T_pA) is injective.

*Proof.* (F1) For `φ ∈ Hom_F(A,B)` the Kummer sequences `0 → A[p^n] → A(F̄) → A(F̄) → 0` map to
those of `B` by `φ`, so the connecting maps commute at every `n`; pass to `lim_n`. Both sides of (F1)
are `Z_p`-linear in `φ`, and for fixed `x` they are continuous in `φ` (the target
`H^1(G_{F,S}, T_pB)` is a finitely generated `Z_p`-module for `S` containing the bad places and `p`,
and Kummer classes are unramified outside `S`); they agree on a `Z`-basis of `Hom_F(A,B)`, hence on
`Hom_F(A,B) ⊗ Z_p`. (F2) `A(F)` is finitely generated, so `Â(F) = lim A(F)/p^n`; each
`A(F)/p^n → H^1(F, A[p^n])` is injective and `lim` is left exact (this is S4 Lemma 2.2).
(F3) The kernel is `H^1(Gal(L/F), T_pA^{G_L})` and `T_pA^{G_L} = T_p(A(L)_tors) = 0`. ∎

**Lemma T (Tate faithfulness).** `Hom_F(A,B) ⊗ Z_p → Hom_{Z_p}(T_pA, T_pB)` is injective (S6).
Hence two `Z_p`-combinations of algebraic correspondences that agree on `T_p` (equivalently, on
`H^1_ét(X̄, Z_p(1))` of the curves) agree as maps `Â(F) → B̂(F)`. ∎

**Extensions used below, all formal.**

1. *Idempotents.* `e ∈ End_F(A) ⊗ Z_p` idempotent (e.g. `e'_r`): (F1) with `φ = e` shows
   `Kum(eÂ(F)) ⊂ H^1(F, eT_pA)`, and (F2) restricts to the direct summand.
2. *Carrier coefficients.* For a finite free `Z_p`-module `B` and `x ∈ Hom_{Z_p}(B, Â(F))`, define
   `Kum(x)(b) := Kum(x(b))`. Then `Kum: Hom(B, Â(F)) → Hom(B, H^1(F, T_pA)) = H^1(F, Hom(B, T_pA))`
   is injective and satisfies (F1) for post-composition with `φ` and pre-composition with any
   `Z_p`-linear `β: B' → B`. (Pre-composition commutes with everything; post-composition is (F1).)
3. *MRS twists.* For `I ∈ FMod_O(F)`, `A` with `O → End_F(A)`, and `f ∈ Hom_{O[G_F]}(I,J)`,
   `φ ∈ Hom_F(A,B)` `O`-linear, the map `f ⊗ φ` of S3 Prop. 1.6(ii) is an `F`-homomorphism of abelian
   varieties and `T_p(f⊗φ) = f ⊗ T_pφ` under S3 Thm. 2.2(iii) (functoriality in `I` and `V` is part of
   that theorem). So Lemma F applies verbatim to twists.
4. *Change of group ring.* If `ρ: O' → O` is a ring map, `A'` an `O'`-variety, `A` an `O`-variety,
   `φ: A' → A` with `φ∘a = ρ(a)∘φ`, and `I = I' ⊗_{O'} O` with the induced `G_F`-action, then
   `i ⊗ v ↦ (i⊗1) ⊗ φ(v)` defines `I' ⊗_{O'} A' → I ⊗_O A` over `F`. Proof: by S3 Thm. 1.4 both
   sides are functors of points `(I ⊗ A(R⊗L))^{Gal(L/F)}`; the map is functorial in `R` and
   `Gal(L/F)`-equivariant; Yoneda. Its Tate realization is `(i⊗1) ⊗ T_pφ` by S3 Thm. 2.2. ∎

**Consequence C-F.** For any `K_0`-rational homomorphism `τ^MW` between (p-completed, idempotent-cut,
carrier-valued) MRS twists of Jacobians, the square

    P_{r+1} --Kum--> H^1(K_0, T_{r+1})
       | τ^MW              | H^1(K_0, T_p τ^MW)
       v                   v
    P_r'    --Kum--> H^1(K_0, T_r')

commutes and both rows are injective. **Ordinary Kummer functoriality makes the square formal the moment
the étale vertical arrow is the Tate realization of a `K_0`-rational element of `Hom ⊗ Z_p`.** No
Selmer, Sha, control, or reciprocity input enters. Everything non-formal in H9R16-C is therefore
located in exactly two places, treated in 03.2–03.5:

* (a) that the BCPV-side objects and transitions are realizations of `K_0`-rational point-level data
  (Galois descent of the finite point; `K_0`-rationality of every operator used);
* (b) that the contracted BCPV classes are compatible under that realized transition (an étale
  identity; by Lemma T it is equivalent to an identity of correspondences).
