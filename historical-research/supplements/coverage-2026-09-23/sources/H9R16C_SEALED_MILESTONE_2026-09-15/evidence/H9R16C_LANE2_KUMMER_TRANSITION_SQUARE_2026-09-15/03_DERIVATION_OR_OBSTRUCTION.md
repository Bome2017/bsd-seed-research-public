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

## 03.2 Galois descent of the finite balanced point (point normalization over `K_0`)

### 03.2.1 BCPV (4.5) pins the Galois law of `W`

Inputs, all printed: (4.1) `<a_1,a_2,a_3> Δ_r[e] = Δ_r[a_2a_3e_1, a_1a_3e_2, a_1a_2e_3]`;
(4.2) `σ_m Δ_r[e] = Δ_r[me]`; (4.4) `Δ_r^ord = (e'W_{Np^r})^{⊗3}Δ_r`; (4.5)
`σ_m Δ_r^ord[e] = Δ_r^ord[m^{-1}e]`; KLZ2 diamond rule `<d>W = W<d^{-1}>`.

Suppose `W^{σ_m} = <m>^k ∘ W` on the p-part for some exponent `k`. Then

    σ_m Δ_r^ord[e] = (e' W^{σ_m})^{⊗3} Δ_r[me] = (e'W)^{⊗3} <m^{-k},m^{-k},m^{-k}> Δ_r[me]
                   = (e'W)^{⊗3} Δ_r[m^{1-2k} e] = Δ_r^ord[m^{1-2k} e].

(4.5) holds for all `m ≡ 1 (mod p)` iff `k = 1`. So **BCPV's printed (4.5) forces
`W^{σ_m} = <m> ∘ W`**, which is also what the KLZ2 moduli definition gives (the class `P''` with
`<P_Q, P''> = ζ_Q^z` is `z·P'_Q`), and has the same shape as Hida's `w_r^σ = <z>∘w_r` (S4 §5).
This is a free consistency test for Lane 1: a dictionary producing the opposite law contradicts (4.5).

The same inputs give, for `m = μ^2`, `μ ≡ 1 (mod p)`:

    <μ,μ,μ> Δ_r^ord[e] = (e'W)^{⊗3} <μ^{-1},μ^{-1},μ^{-1}> Δ_r[e] = Δ_r^ord[μ^{-2}e] = σ_m Δ_r^ord[e].    (G1)

The tame part of `W_{Np^r}^{⊗3}` moves by the diagonal tame diamond, which fixes the diagonal cycle;
so `Δ_r^ord` is `L_r`-rational, as BCPV (4.4) states.

### 03.2.2 The contracted point

`Φ_r^mod(t_2 ⊗ t_3) = Π_{Z,*}((1 ⊗ t_2 ⊗ A_r t_3) Δ_r^ord)`, `A_r = W_{N_g p^r}^{-1}(U'_p)^r` on factor 3.
Take `σ ∈ G_{K_0}` with `σ(ζ_{N_g p^r}) = ζ^{z}`, `z = (z_p, z_N)`, `z_p = m = μ^2`. All of `Π_Z`,
`t_2`, `t_3`, `U'_p`, `e'` are Q-rational; `A_r^σ = W^{-1}<z>^{-1}(U'_p)^r = A_r <z_p>^{-1}<z_N>^{-1}`. Using (G1),
`Π_{Z,*}(<μ>⊗1⊗1)(−) = <μ> Π_{Z,*}(−)`, and commutativity of the primed Hecke algebra:

    σ Φ_r^mod(t_2 ⊗ t_3) = <μ>_{(1)} Φ_r^mod( t_2<μ> ⊗ <z_N>^{-1} <m>^{-1} <μ> t_3 ).

Balance (H9R16-A/B, `u' = <μ>`; check: `ρ(<d>) A_r = <d>^{-1}W^{-1}U'^r = W^{-1}<d>U'^r = A_r<d>`)
moves `<μ>` from factor 2 to factor 3, and `<μ><μ><m>^{-1} = 1`:

    σ Φ_r^mod(t_2 ⊗ t_3) = <c_r(σ)^{1/2}>_{(1)} Φ_r^mod( t_2 ⊗ <z_N(σ)>^{-1} t_3 ).      (G2)

### 03.2.3 Reading (G2)

* **p-part.** The whole dagger twist lands on the `J_r`-factor as `<c_r^{1/2}>`; the carrier is
  untwisted at `p`. This is exactly what BCPV's target requires: in Def. 4.14 the trace passes through
  `ad(T_g)` with no dagger on it. If `W^σ = <z>^{-1}W` instead, the carrier would carry `<c_r>` and the
  contracted point would no longer map to BCPV's `T^† = T_f^† ⊗ ad(T_g)`.
* **tame part.** The carrier is twisted by `<ε_N>^{-1}` on factor 3 — on `g`-isotypic parts this is
  `ε_g^{-1}`, i.e. **the `g^c` twist of S1 (1.7)**. The balanced point is `K_0`-rational only after this
  twist; without it it is defined over `K_0(μ_{N_g})`. "Schematically over `Q(μ_p)`" is correct only
  with the tame nebentype twist written into the carrier.
* **Type.** (G2) says `Φ_r^mod ∈ Hom_{G_{K_0}}( B_r^{(ε)}, e'Ĵ_r(Q̄)^{(c^{-1/2})} )`, i.e. (by S3
  Thm. 1.4 with the inverse convention of Lemma 1.3) `Φ_r^mod ∈ P_r^{tr,†}`: a `K_0`-rational point of
  the type-B twist with lattice character `c_r^{+1/2}` on `J_r` and tame lattice character on factor 3.
  The normalized `Q_r` lies there too (`U'_p`, `e'` are Q-rational and `G_r`-central).

**Level caveat (inherited, not introduced here).** The frozen H9R16-A/B formula applies
`W_{N_g p^r}` on factor 3 of a cycle living at common tame level `N = lcm(N_f, N_g)`. As an
Atkin–Lehner operator `W_Q` on `X_1(Np^r)` this needs `Q = N_g p^r ∥ Np^r`, i.e. `gcd(N_g, N/N_g) = 1`;
otherwise factor 3 must first be pushed to the native level `N_g`. Only the tame factor `<z_N>` in
(G2) depends on this choice, and it lands on factor 3 either way. Fixing the level is Lane-1 bookkeeping.

**Status.** `C_POINT_NORMALIZATION` — descent of the finite point to the fixed-base type-B object —
is **PROVED here from printed inputs** ((4.1), (4.2), (4.4), (4.5), KLZ2 diamond rule, H9R16-A/B
balance) plus one step used by BCPV without statement: the pushforward `Π_{Z,*}` commutes with
factor-1 diamonds (the graph `X_{14}` is `<μ>×<μ>`-stable). No `W/w` dictionary is used.

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

## 03.4 The transition square and the one non-formal identity

### 03.4.1 The point transition is `K_0`-rational (co-ordinary, plain Albanese)

Define, on type-B objects,

    τ_r^MW : P_{r+1}^{tr,†} → Hom_{Z_p}(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0),     x ↦ ϖ_{1,*} ∘ x.

* `ϖ_{1,*}` is Q-rational and `O`-semilinear over `pr_r` (T1), so 03.1 extension 4 gives a
  `K_0`-homomorphism of twists; the tame carrier twist is untouched (it acts on factor 3).
* `ϖ_{1,*} ∘ e'_{r+1} = e'_r ∘ ϖ_{1,*}` because `U'_p` commutes with `ϖ_{1,*}` (S2 §1.3) and Lemma T.
* Hida's (u*1) (S4 §3) is the point-level statement that plain Albanese pushforward is a
  `U^*(p)`-isomorphism, i.e. that this is the natural transition on the co-ordinary tower.
  *Using this requires the identification `BCPV U'_p = U^*(p)` on the same model (Lane 1). The square
  itself only uses `ϖ_{1,*}U'_p = U'_pϖ_{1,*}`, which is printed (S2) — it does not need that name.*

Its Tate realization is post-composition with `ϖ_{1,*}` on `Hom(B_{r+1}, e'S)^†`. By Consequence C-F:

    Kum ∘ τ_r^MW = τ_r^et ∘ Kum,      τ_r^et := H^1(K_0, T_p τ_r^MW).                (SQ)

**(SQ) is PROVED — formal naturality.** No `W`, no `w`, no `δ_r` enters it.

### 03.4.2 Typing correction forced by coefficient retention

`Hom(B, −)` is contravariant in the carrier, and `B_{r+1} → B_r` (induced by `π_r`) is surjective.
There is therefore **no** arrow `P_{r+1}^{tr,†} → P_r^{tr,†}` of carrier-valued point modules. The
well-typed receptacle is the injective pull-back

    π_r^* : P_r^{tr,†} ↪ Hom_{Z_p}(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0),

and "compatibility" means an equality inside that module. Kummer injectivity holds there (03.1,
extension 2). This is a type correction to the prompt's square, not an obstruction.

### 03.4.3 What must still be shown: compatibility of the contracted classes

Let `c_r := Kum(Q_r)` — by the finite modified point/Kummer realization (H9R10, frozen input `(K_r)`)
this is the BCPV class `Δ_r^et` contracted by `(1 ⊗ t_2 ⊗ A_r t_3)`, normalized by
`(U'_p)^{-r}` on factor 1 and `(U'_p)^{-2r}` on the carrier. For the tower one needs

    (E_ν)   τ_r^et(c_{r+1}) ∘ (1 ⊗ ν_{r+1}) = π_r^* c_r      in H^1(K_0, Hom(B_{r+1}, e'S_r)^†)

for some fixed `ν_{r+1} ∈ e'𝕋'_{r+1} ⊗ Z_p` acting on factor 3 of the carrier. **(E_ν) is not in BCPV.**
It follows from BCPV Corollary 4.11(i) together with the following identity of correspondences on the
auxiliary tower `X_1(N_g p^{r+1})`:

    MPC_r(ν):   <ϖ_{1,*}y, A_r ϖ_{1,*}z>_r = <y, A_{r+1} ν_{r+1} z>_{r+1}
                for all y, z ∈ e'S^g_{r+1}     (equivalently ϖ_1^* A_r ϖ_{1,*} = A_{r+1} ν_{r+1}).

*Derivation of (E_ν) from MPC_r(ν).* Realize `Φ_{r+1}^mod(t_2 ⊗ ν t_3)` on `x_1⊗x_2⊗x_3` as
`x_1 <t_2x_2, A_{r+1}νt_3x_3>_{r+1}`. Push forward on factor 1; MPC_r(ν) with `y = t_2x_2`,
`z = t_3x_3` and `ϖ_{1,*}t = π_r(t)ϖ_{1,*}` turn this into the level-`r` contraction
`[π_r(t_2), π_r(t_3)]` of `ϖ_{1,*}^{⊗3}Δ_{r+1}^et`, which is `U'^{⊗3}_pΔ_r^et` by Corollary 4.11. Moving
the three `U'_p` out (factor 1, and onto the carrier by balance) and inserting the normalizations gives
`ϖ_{1,*} ∘ c_{r+1} ∘ (1⊗ν) = c_r ∘ π_r`. ∎

*From (E_ν) to points.* By (SQ), (K_{r+1}), (E_ν), (K_r):

    Kum( τ_r^MW(Q_{r+1}) ∘ (1⊗ν) − π_r^*Q_r ) = τ_r^et(c_{r+1})∘(1⊗ν) − π_r^*c_r = 0,

so Kummer injectivity gives **`τ_r^MW(Q_{r+1}) ∘ (1⊗ν_{r+1}) = π_r^* Q_r`** — the H9R16-C point
relation in its correctly typed form.

### 03.4.4 Status of MPC_r and the value of `ν`

* By Lemma T, MPC_r(ν) holds on `e'Ĵ` if and only if it holds on `e'S`. It is a statement about
  Hecke correspondences — **no Selmer, Sha, control or L-function input**.
* BCPV assert its Λ-adic form ("(1.7) are interpolated by (1.4)"), citing Ohta and KLZ2; KLZ2
  Theorem [Ohta] `thm:ordinaryfiltration`(v) supplies the canonical `Λ_D`-pairing and remarks that it
  involves `W_{Np^r}^{-1}(U'_p)^r`. The underlying Ohta 2000 statements (Cor. 1.3.8, 2.3.6) were **not
  obtained**.
* If the finite-level group-ring pairings are `Σ_{a} <x, <a> A_r y> [a]` and project compatibly under
  `Z_p[Δ_{p^{r+1}}] → Z_p[Δ_{p^r}]`, reading the identity coefficient gives MPC_r(ν) with
  `ν_{r+1} = N_{r+1,r} := Σ_{k ∈ ker} <k>`, the norm element of `ker((Z/p^{r+1})^× → (Z/p^r)^×)`.
  This is **DERIVED_HERE under that hypothesis, not proved**. Sanity check on old vectors
  `z = ϖ_1^*z_0`: both sides reduce to `p·ϖ_1^*A_r = A_{r+1}ϖ_1^*`, which is the `W`-conjugate of the
  q-expansion relation `U_p ∘ pr_2^* = p·pr_1^*` in weight 2 (KLZ2, proof after
  `thm:ordinaryfiltration`). Heuristic only.
* With `ν = N`, `π_r(N) = p`: the integral relation is `τ^MW(Q_{r+1})∘(1⊗N) = π_r^*Q_r`, and no
  division by `p` occurs. The kernel here is the single-factor kernel, of order `p`. It should not be
  matched with BCPV's printed `1/p` in (4.9): that is a triple-product constant, and commutativity of
  (4.8) forces `p^{-3}` there (03.3.3).

## 03.5 Where a W/w discrepancy `δ_r` can enter, and which identities make it harmless

Provisional Lane-1 output (value not guessed): after the model identifications,
`W_r = δ_r ∘ w̃_r` on `e'S^g_r` and `e'Ĵ^g_r`, where `w̃_r` is Hida's `w_r` transported to the BCPV model.
Put `Ã_r := w̃_r^{-1}(U'_p)^r`, so `A_r = Ã_r δ_r^{-1}` whenever `δ_r` commutes with `U'_p`.

### 03.5.1 Places where `δ_r` does **not** enter

| Step | Uses | `δ_r` needed? |
|---|---|---|
| descent of `Φ_r^mod` to `P_r^{tr,†}` (03.2) | BCPV (4.1)(4.2)(4.4)(4.5), KLZ2 diamond rule, balance | **No** — the Galois law of `W` is forced by (4.5) |
| the square (SQ) (03.4.1) | plain Albanese `ϖ_{1,*}` on co-ordinary parts, MRS functoriality, Lemma F | **No** |
| W on the f-factor inside `Δ^ord` | BCPV Lemma 4.10 (Chow level, printed) | **No** |

### 03.5.2 Places where it may enter

(α) **Proving MPC_r from Hida's `w`-relations** (S4 (6.6)–(6.8): `π_s^r∘π^*_{r,s} = p^{s-r}U(p)^{s-r}` and
`w`-twisted Cartier adjointness) instead of from Ohta's pairing.

(β) **Building the tower with the `w`-normalized functional** `Φ_r^w(t_2⊗t_3) := Π_{Z,*}((1⊗t_2⊗Ã_r t_3)Δ_r^ord)`,
i.e. with Hida's involution on the auxiliary factor. Then `Φ_r^w = Φ_r^mod ∘ (1 ⊗ δ_r)`.

(γ) **Using Hida's ordinary `w`-twisted tower on the f-factor** (`x ↦ w̃_r ∘ x`, transition `π_{r+1}^r`).
This involves the f-side `w` only. On the type-B twist it is `K_0`-rational at `p`
(`<z>c^{-1/2} = c^{+1/2}`) and at tame level wherever `ε_f = 1` (BCPV assume `ε_f` trivial). It is
isomorphic to the co-ordinary formulation and not needed.

### 03.5.3 Sufficient identities

    (D1) centrality      δ_r ∈ e'𝕋'_r ⊗ Z_p   (commutes with all T'_ℓ, U'_ℓ, <d>, e'_r)
    (D2) invertibility   δ_r ∈ (e'𝕋'_r ⊗ Z_p)^×        [integral tower]
                         δ_r ∈ (e'𝕋'_r ⊗ Q_p)^×        [Q_p-linear tower only]
    (D3) rationality     δ_r^σ = δ_r for all σ ∈ G_{K_0}
                         ⇔ W_r and w̃_r have the same Galois cocycle on G_{K_0}
                         ⇔ (by 03.2.1) w̃_r^σ = <z(σ)> ∘ w̃_r in the BCPV model
    (D4) diamond rule    <d> ∘ w̃_r = w̃_r ∘ <d^{-1}>            [implied by D1 and the rule for W]
    (D5) level           π_r(δ_{r+1}) = u_r · δ_r with u_r ∈ (e'𝕋'_r ⊗ Z_p)^× Q-rational
                         (simplest case u_r = 1)

**Proposition D.** Assume (D1), (D2), (D5).

1. *(α)* If `MPC_r^w(ν^w)`: `<ϖ_{1,*}y, Ã_r ϖ_{1,*}z>_r = <y, Ã_{r+1} ν^w z>_{r+1}` holds, then MPC_r(ν)
   holds with `ν_{r+1} = ν^w_{r+1} · ũ_{r+1}` for any lift `ũ_{r+1}` of `u_r` along `π_r`.
2. *(β)* Balance holds for `Φ_r^w` (ι_r = id), and the `w`- and `W`-normalized towers determine each
   other: `τ^MW(Q^w_{r+1})∘(1⊗ν^w) = π_r^*Q^w_r` ⇔ `τ^MW(Q_{r+1})∘(1⊗ν^wũ) = π_r^*Q_r`.
3. *(β, descent)* If moreover (D3), `Φ_r^w ∈ P_r^{tr,†}` with the same twist as `Φ_r^mod`.
   Without (D3), writing `δ_r^σ = κ_r(σ)δ_r`, `Φ_r^w` descends to the twist of the carrier by `κ_r`.

*Proof.* (1) By (D1), `A_r = Ã_rδ_r^{-1}`. By the defining property of `π_r` and (D5),
`δ_r^{-1}ϖ_{1,*} = u_r ϖ_{1,*}δ_{r+1}^{-1} = ϖ_{1,*}ũ_{r+1}δ_{r+1}^{-1}`. Hence
`<ϖ_*y, A_rϖ_*z> = <ϖ_*y, Ã_rϖ_*(ũδ_{r+1}^{-1}z)> = <y, Ã_{r+1}ν^wũδ_{r+1}^{-1}z> = <y, A_{r+1}(ν^wũ)z>`,
using `MPC_r^w` and commutativity of `e'𝕋'_{r+1}`.
(2) `ρ_r(u')Ã_r = ρ_r(u')A_rδ_r = A_ru'δ_r = Ã_ru'` by H9R16-A/B and (D1), so `ι_r = id` for `Φ^w`.
`Φ_r^w = Φ_r^mod∘(1⊗δ_r)`; the normalizations commute with `δ_r` (D1); `δ_r` is invertible (D2); and
(D5) converts `π_r^*(Q_r∘(1⊗δ_r))` into `(π_r^*Q_r)∘(1⊗δ_{r+1}ũ^{-1})`.
(3) Repeat 03.2.2 with `Ã_r^σ = A_r^σ δ_r^σ`. ∎

**Reading.** (D1)+(D2)+(D5) are what the tower consumes. (D3) is consumed only by (β)'s descent.
A central diamond `δ_r = <a_r>` (Q-rational) satisfies (D1)–(D3). It satisfies (D5) iff
`a_{r+1} ≡ a_r·(unit diamond)` compatibly, e.g. `δ_r = <p>_N^{±r}` has `u_r = <p>_N^{±1}`, a unit that is
absorbed. A scalar `δ_r = p^{e_r}` is central and Q-rational but fails (D2) integrally when `e_r > 0`;
over `Q_p` it is harmless if `u_r = p^{e_{r+1}-e_r}`. A discrepancy involving a Galois element or a
non-Hecke correspondence would violate (D1) or (D3); nothing in the sources read here suggests one.

**How to insert `δ_r`.** Never inside the square. Insert it (i) on factor 3 of the carrier, as
precomposition with `1⊗δ_r`, when converting between `W`- and `w`-normalized functionals; and (ii) in
the correction element `ν_{r+1} = ν^w_{r+1}ũ_{r+1}` of the compatibility relation.

## 03.6 Hostile checks on the Lane-2 construction

Labels: `NOT_PRINTED` / `FALSE` / `TYPE_MISMATCH` / `NEW_THEOREM_REQUIRED` / `PASS`.

| # | Attack | Finding | Label |
|---|---|---|---|
| H1 | Does the balanced finite point belong to the fixed-base MRS module over `Q(μ_p)`? | Only with the tame nebentype twist on the carrier's third factor (03.2.3). Without it the point is `K_0(μ_{N_g})`-rational and transforms by `<z_N>^{-1}` on factor 3. With it, (G2) proves membership. | literal "`Q(μ_p)`" is `TYPE_MISMATCH` unless `ε_g`-twist written; PASS with it |
| H2 | Is the Kummer target BCPV's Tate module? | Type B: yes. H9R8's type A has rank `\|G_r\|` times larger and is not BCPV's module; BCPV classes cannot be used there. | type A `TYPE_MISMATCH`; type B PASS |
| H3 | Level change conflated with corestriction? | Type B: no corestriction exists (03.3.3). Type A: the lattice projection is corestriction on its Weil-restriction blocks plus diamond sums. | PASS in type B |
| H4 | Group-ring projection vs MRS lattice | `id⊗pr_r` is `G_{K_0}`-equivariant because `pr_r∘c_{r+1}^{1/2} = c_r^{1/2}`; `μ_r` intertwines A and B with no `1/p`. | PASS |
| H5 | Hida `w`-transition on the twisted object | Not needed. If used on the f-factor it is `K_0`-rational at `p`, and at tame level on `ε_f = 1` parts (03.5.2 γ). | PASS (optional) |
| H6 | Central diamond discrepancy vs dagger descent | Descent uses `W` only, and its law is forced by BCPV (4.5). `δ_r` matters only through (D3) in route (β) and (D5) in the level relation. | PASS given (D1)(D2)(D5); (D3) only for (β) |
| H7 | p-completion / inverting `p` vs Kummer injectivity | Injective on `Â(K_0)`, on `e'`-summands, on `Hom(B, −)`, and after `⊗Q_p`. The integral relation with `ν = N` never divides by `p`. | PASS |
| H8 | Coefficient retention through the transition | No arrow `P_{r+1} → P_r` exists: `Hom(B,−)` is contravariant and `B_{r+1} → B_r` is onto. The correct target is `π_r^*P_r ⊂ Hom(B_{r+1}, e'Ĵ_r)^†`. | `TYPE_MISMATCH` in the prompt's arrow; PASS after correction |
| H9 | Does `g^c` duality change the direction? | No. `A_r` acts on factor 3; carrier transitions are `π_r` on both auxiliary factors; `g^c` changes the Galois module (tame `ε^{-1}`), not the variance. Balance `ι_r = id` keeps both factors covariant on `e'`-parts. | PASS |
| H10 | Finite point inferred from an étale realization? | No. `Φ_r^mod` is a Chow-level construction (H9R16-A/B), and its descent (03.2) is proved at Chow level. The Kummer realization `(K_r)` is a separate frozen input (étale Abel–Jacobi functoriality for algebraic correspondences). | PASS; `(K_r)` is an input |
| H11 | `(U'_p)^{-r}` on points | `e'_r ∈ 𝕋'_r ⊗ Z_p` is idempotent and `U'_p` is a unit of the finite `Z_p`-algebra `e'𝕋'_r ⊗ Z_p`, so the inverse exists on `e'Ĵ_r(F)` (cf. S4 §3). The BCPV Definition 4.12 inversion is not used at point level. | PASS |
| H12 | The class-compatibility identity (E_ν) | Reduces exactly to MPC_r(ν), an identity of Hecke correspondences on `X_1(N_g p^{r+1})`. Not printed in any source obtained. The Λ-adic form is asserted by BCPV after (1.7) and in KLZ2 `thm:ordinaryfiltration`(v); Ohta 2000 was not obtained. | `NOT_PRINTED` (not `NEW_THEOREM_REQUIRED`: no arithmetic input, Tate-faithful) |
| H13 | Citation hygiene | BCPV footnote 8 → Remark 4.9(ii) should be 4.5(ii); BCPV Lemma 4.10 → "[DR22] Lemma 2.5" is Lemma 2.4 in arXiv v1. | `NOT_PRINTED`-type drift, no mathematical effect |

**Obstruction search result.** No `FALSE` item and no `NEW_THEOREM_REQUIRED` item was found. Two
typing corrections are mandatory (H1 tame twist; H8 pull-back target) and one convention is mandatory
(03.3.1 MRS lattice sign). Type A is excluded for BCPV's classes (H2).

## 03.7 Conclusion of the derivation

1. **The square is formal.** With `P_r^{tr,†}` the type-B twist (lattice `c_r^{+1/2}` on the Jacobian
   factor, tame `ε`-twist on the carrier), `τ_r^MW = ϖ_{1,*}∘(−)`, target `π_r^*P_r^{tr,†}`, and
   `τ_r^et = H^1(K_0, T_pτ_r^MW)`, the square commutes by Lemma F. Nothing from Lane 1 is used.
2. **Point normalization over `K_0` is proved** from BCPV (4.1), (4.2), (4.4), (4.5), the KLZ2 diamond
   rule and H9R16-A/B balance (03.2).
3. **The tower relation** `τ_r^MW(Q_{r+1})∘(1⊗ν_{r+1}) = π_r^*Q_r` follows from the square, `(K_r)`,
   `(K_{r+1})`, BCPV Corollary 4.11, and **one** identity of correspondences, MPC_r(ν) (03.4.3).
4. **`δ_r`** is never inserted into the square. It is harmless under (D1)(D2)(D5) for the tower, plus
   (D3) if the `w`-normalized functional is used (Proposition D).

    C2_REDUCES_TO_FORMAL_NATURALITY
    (square PROVED; class compatibility reduced to MPC_r(ν), NOT_PRINTED)
