## 03.3 Which dagger object; Shapiro and corestriction

### 03.3.1 The MRS inverse convention

S3 Lemma 1.3 and Theorem 2.2 let `σ` act on `I ⊗ V(L)` and on `I ⊗ T_ℓV` as `σ^{-1} ⊗ σ`; S3
Example 1.5(ii) says a rank-one lattice with character `χ` produces the twist by `χ^{-1}`. BCPV
Definition 4.6 lets `σ` act on `M^† = M ⊗_{Z_p[G_r]} Z_p[G_r]^†` by `<χ>_r^{-1/2}` with no inverse.

Therefore: **the MRS lattice realizing BCPV's `†` has character `c_r^{+1/2}`.** Check against (G2):
`x ∈ (I ⊗_O V(L))^{Gal}` with `I = O(c^{1/2})` means `c(σ)^{-1/2}·σx = x`, i.e. `σx = c(σ)^{1/2}x`,
which is exactly the law (G2) of the balanced point; and `T_p(I⊗_O V) = I ⊗_O T_pV` with `σ^{-1}⊗σ`
is `T_pV` twisted by `c^{-1/2}`, which is BCPV's `T_pV^†`.

H9R8 wrote "`I_r^†` … with **right** Galois action induced by `<χ>_r^{-1/2}`". A right action by
`c^{-1/2}` is the left action by `c^{+1/2}`, so the character is correct if "right" is read literally.
It must be written as a left action with the explicit sign; with a left action by `c^{-1/2}` the twist
has Tate module `T_pV^{(c^{+1/2})}`, which is not BCPV's module.

### 03.3.2 Type A versus type B

* **Type B** — `A_r^† = O_r(c^{1/2}) ⊗_{O_r} V_r`, `O_r = Z[G_r]` acting by Q-rational diamonds.
  `T_p(A_r^†) = T_pV_r ⊗_{Z_p[G_r]} Z_p[G_r]^†`: **BCPV's module** (same `Z_p`-rank as `T_pV_r`).
* **Type A** — H9R8's `A_r^{†,A} = Z[G_r](c^{1/2}) ⊗_Z V_r`. `T_p = Z_p[G_r]^† ⊗_{Z_p} T_pV_r`, of rank
  `|G_r|` times larger. It is **not** the module in which BCPV's classes live.
* **Comparison** — `μ_r : A_r^{†,A} → A_r^†`, `g ⊗ v ↦ <g>v`, is `K_0`-rational (both lattices carry
  `c^{1/2}`, and diamonds are Q-rational) and surjective.

Consequence for the tower: Kummer injectivity must be applied **in type B**. A compatible system
proved in type B does not lift through `μ_r` (not injective), and BCPV supply no type-A classes. The
square of the prompt, written with `T_r^{tr,†}`, is a type-B square.

### 03.3.3 Level change versus corestriction

*Type B has no corestriction.* Let `x ∈ A_{r+1}^†(K_0)`, so `x ∈ V_{r+1}(L̄)` with
`σx = c_{r+1}(σ)^{1/2}x`. Because `ϖ_{1,*}∘<d> = <pr_r d>∘ϖ_{1,*}` and `pr_r∘c_{r+1}^{1/2} = c_r^{1/2}`,

    σ(ϖ_{1,*}x) = c_r(σ)^{1/2} ϖ_{1,*}x   for all σ ∈ G_{K_0};

for `σ ∈ G_{L_r}` this says `σ` fixes `ϖ_{1,*}x`. So `ϖ_{1,*}x ∈ A_r^†(K_0)` with no trace, norm or
corestriction. In the varying-field picture this reads
`res_{L_{r+1}/L_r} Kum_{L_r}(ϖ_{1,*}x) = ϖ_{1,*} Kum_{L_{r+1}}(x)` — a **restriction** identity. The
degree-`p` cyclotomic layer is absorbed by the degree-`p` Galois layer `μ` of `ϖ_1` (S2 §1.3), whose
covering group is the diamond kernel meeting `c_{r+1}(Gal(L_{r+1}/L_r))`.

*Type A contains corestriction.* `c_r^{1/2}` is injective on `Γ_r`, so `Z[G_r](c^{1/2})` is a free
`Z[Γ_r]`-module; choosing representatives `R_r` of `G_r / c_r^{1/2}(Γ_r)` gives
`A_r^{†,A} ≅ (Res_{L_r/K_0} V_r)^{|R_r|}` (S3 Prop. 4.1). Under Shapiro,
`H^1(K_0, Z_p[Γ_r] ⊗ T) ≅ H^1(L_r, T)`, and the lattice projection `Z[Γ_{r+1}] → Z[Γ_r]` is
**corestriction** on `H^1` and the **trace** `V(L_{r+1}) → V(L_r)` on points. The projection
`pr_r: Z[G_{r+1}] → Z[G_r]` additionally merges `p^2` cosets per fibre (the diamond directions of
`ker pr_r` outside `c_{r+1}(Γ_{r+1})`); those sums are diamond sums, not field traces.

*Compatibility of the two.* `μ_r ∘ (pr_r ⊗ ϖ_{1,*}) = ϖ_{1,*} ∘ μ_{r+1}`, since
`<pr_r g> ϖ_{1,*} v = ϖ_{1,*}(<g>v)`. No `1/p` appears. BCPV's `1/p` in (4.9) belongs to the
`Hom_{Z_p[G]}(S, Z_p[G])` column, where the isomorphism `G^{-1}` changes with `|G_r|`; the outer columns
of (4.8) are plain `ϖ_{1,*}^{⊗3}`.

*The printed constant in (4.9) is inconsistent with (4.8).* Take `φ ∈ Hom_{Z_p}(_{r+1}S, Z_p)`. Going
through `G^{-1}` and then (4.9) gives the coefficient of `g'` as `c·Σ_{pr(g)=g'} φ(g^{-1}ϖ_1^{*⊗3}s)`, with
`c` the printed constant. Going through `(ϖ_1^{*⊗3})'` and then `G^{-1}` gives `φ(ϖ_1^{*⊗3}(g'^{-1}s))`.
Every `k ∈ ker(pr_r)` fixes `ϖ_1^*`-images, because `ϖ_1∘<k> = ϖ_1` for `k ≡ 1 (mod p^r)`, and
`ϖ_1^{*⊗3}∘g'^{-1} = g̃^{-1}∘ϖ_1^{*⊗3}` for any lift `g̃`. So the fibre sum is `|ker pr_r| = p^3` equal
terms, and commutativity forces **`c = p^{-3}`, not the printed `p^{-1}`**. This is DERIVED_HERE; Lane 4
independently recorded "(4.9) off by `p^2`". It does not touch the type-B square, which uses only the
outer columns.

**Verdict for this item.** *Modular level change and field corestriction are not conflated in type B:
corestriction does not occur, and the cyclotomic datum is the cocycle identity
`pr_r ∘ c_{r+1}^{1/2} = c_r^{1/2}`. In type A, corestriction occurs inside the lattice projection, and
the formulation must pass through `μ_r` before it can meet BCPV's classes.*

### 03.3.4 Fixed base versus varying field

`res: H^1(K_0, T_r^{tr,†}) → H^1(L_r^{(N)}, Hom(B_r, e'S_r))` is injective (Lemma F3; `T_pJ` has no
invariants over number fields). Hence the fixed-base square and the varying-field square (with
restriction maps written in) are equivalent statements. The fixed-base square is preferred only
because it keeps all transitions inside one Galois group.
