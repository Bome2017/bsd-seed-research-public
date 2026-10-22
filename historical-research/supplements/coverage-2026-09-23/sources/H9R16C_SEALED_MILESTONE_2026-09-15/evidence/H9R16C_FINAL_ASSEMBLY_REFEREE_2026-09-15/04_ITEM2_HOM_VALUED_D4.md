# 04 — ITEM 2: scalar D4 ⇒ Hom-valued D4,  Kum(Φ̄_r^mod) = Contr_r^{A_r}(Δ_r^ét)

Continues 03 (notation, the map Φ̄_r^mod, the ⋆-action). Inputs: A6 (scalar D4, frozen PROVED_FORMAL),
B1 (Kummer naturality package), B2/B5 (twisted descent, receptacle), §C (balance). No new input.

## §1. The carrier is free — so the Hom/H^1 interchange is legitimate

**Lemma C (carrier).** After the `A_r` transport of §C (`ι_r(u') = A_r^{-1}ρ_r(u')A_r = u'`), both auxiliary
factors are modules over the same commutative algebra `R_r := e'_ord𝕋'_{N_gp^r} ⊗ Z_p`, and the balancing
relation `(t_2u')⊗t_3 ∼ t_2⊗u't_3` is exactly `R_r`-bilinearity. Hence

    B_r^bal = R_r ⊗_{R_r} R_r ≅ R_r  (t_2 ⊗ t_3 ↦ t_2t_3),

a **finite free `Z_p`-module** (`R_r` is a finite `Z_p`-algebra acting faithfully on the free `Z_p`-module
`e'S^g_r`, hence `Z_p`-torsion-free and finitely generated, hence free). Consequences used below:
* `Hom_{Z_p}(B_r^bal, H^1(F, T)) = H^1(F, Hom_{Z_p}(B_r^bal, T))` for `T` a finite free `Z_p[G_F]`-module
  (B1 extension 2 then applies verbatim), so `T_r^♮ := Hom_{Z_p}(B_r^bal, T_pJ^{(1),ord}_r)` is the right
  étale target and `Kum^♮_r` of B5 is defined and injective;
* `rank_{Z_p}B_r^bal = rank_{Z_p}R_r`: **no `|G_r|` factor is present in the carrier itself** (used in 06);
* the tame action `R(⟨n⟩)` and the insertion `1 ⊗ N_{r+1,r}` are multiplication by `⟨n⟩` resp. `N_{r+1,r}`
  in `R_r` — both central, both `R_r`-linear (used in 05 and 07).

This lemma also disposes of Lane 4 `03` §6.3's caution (`B^bal` a quotient module, possible torsion): under
the frozen balance the quotient is free. Everything below is nevertheless proved **evaluationwise** first.

## §2. The typed étale target

For `b = [t_2⊗t_3] ∈ B_r^bal` define, on `S^{⊗3}_r(2)` with `S_r = H^1_ét(X̄_r, Z_p)`:

    Contr_r^{A_r}(b) : S_r^{⊗3}(2) ⟶ S^{(1)}_r(1) = T_pJ^{(1)}_r ,
    y_1⊗y_2⊗y_3 ↦ pd^{t_f}_*(y_1) · ⟨ pd^t_*y_2 , A_r pd^t_*y_3 ⟩_{N_gp^r}   with (t_2,t_3) inserted as in 03 §2,

i.e. `Contr_r^{A_r}(b) = Contr^{Γ(b)}` for the algebraic correspondence `Γ(b)` of 03 §4. Degrees:
`⟨,⟩: S_r(1)⊗S_r(1) → H^2(X̄,Z_p(2)) = Z_p(1)`, so `S^{⊗3}(2) → S(1)`; this is BCPV's normalization
(their (1.6) `eqn_2023_09_29_1444` l.514–518, `k = 0`) and DR22 (2.17) (`eqn:pairing-LambdaG`, l.2274–2282).
Push-forward on `H^1(F'_r, −)` gives `Contr_r^{A_r}(b)_*`. The étale contraction descends to `B_r^bal`
for the same reason as the point one (03 §3): `ρ_r(u')A_r = A_ru'` (§C), so
`⟨t_2u'y_2, A_rt_3y_3⟩ = ⟨t_2y_2, A_ru't_3y_3⟩`.

    T_r^♮ := Hom_{Z_p}(B_r^bal, T_pJ^{(1),ord}_r), with the ⋆-action of 03 §5 (B5).

## §3. Evaluationwise D4 ⇒ Hom-valued D4 (over F'_r)

**Theorem 2 (Hom-valued D4).** For the fixed index `e` of 03 §4 and every `b ∈ B_r^bal`,

    Kum_{F'_r}( Φ̄_r^mod(b) )  =  Contr_r^{A_r}(b)_* ( Δ_r^ét[e] )   in H^1(F'_r, T_pJ^{(1),ord}_r),

equivalently `Kum^♮_{F'_r}(Φ̄_r^mod) = Contr_r^{A_r}(Δ_r^ét[e])` in `Hom_{Z_p}(B_r^bal, H^1(F'_r, T_pJ^{(1),ord}_r))
= H^1(F'_r, T_r^♮)` (Lemma C).

*Proof.* Three steps, each with its type.

1. **One evaluation.** Fix `b = [t_2⊗t_3]`. `Γ(b)` is a `Z`-combination of algebraic correspondences on
   `X_r` over `F'_r` (03 §2.3, §4: `pd^t`, `pd^{t_f}` are morphisms over `Q`; `t_2,t_3` are over `Q`;
   `A_r` is over `F'_r`). A6 applied to `Γ = Γ(b)` and `d = e` gives exactly
   `Kum(Π_{Γ(b),*}Δ_r^{ord}[e]) = Contr^{Γ(b)}_*(K ∘ cl_1(Δ_r^{ord}[e])) = Contr_r^{A_r}(b)_*(Δ_r^ét[e])`.
   The f-side push-down on the output is already inside `Γ(b)`; if one prefers to apply it afterwards,
   B1 (F1) gives `Kum ∘ pd^{t_f}_* = H^1(F'_r, T_p pd^{t_f}_*) ∘ Kum`, since `pd^{t_f}_*` is a homomorphism
   of abelian varieties over `Q ⊂ F'_r`. Same conclusion.
2. **Linearity and the quotient.** Both sides are additive and `Z_p`-continuous in `b` (finitely generated
   `Z_p`-modules, p-adically complete targets), and both kill the balancing relations (§2 and 03 §3).
   Hence the identity holds for every `b ∈ B_r^bal`, i.e. as an identity of elements of
   `Hom_{Z_p}(B_r^bal, H^1(F'_r, T_pJ^{(1),ord}_r))`. ∎

**No extra hypothesis was used.** In particular the identity does **not** require the packaged class
`Δ_r^ét[[a,b,c]]`, nor BCPV's `G`/`G^{-1}` isomorphism, nor (4.9) (prohibited): the index-`e` class suffices
because the point object of 03 is the index-`e` point.

## §4. ⋆-equivariance over K_0 and descent

Write `θ_r := Contr_r^{A_r}(Δ_r^ét[e]) ∈ Hom_{Z_p}(B_r^bal, H^1(F'_r, T_pJ^{(1),ord}_r)) = H^1(F'_r, T_r^♮)`.

**(a) The point side is ⋆-invariant** — 03 §5 (B2), `Φ̄_r^mod ∈ 𝒫_r^♮`.

**(b) The étale side inherits ⋆-invariance by transport.** `Kum_{F'_r}` is `Gal(F'_r/K_0)`-equivariant
(functoriality of the Kummer sequence in the base field: `σ(Kum(x)) = Kum(σx)` for `σ ∈ Gal(F'_r/K_0)`,
acting on `H^1(F'_r,T)` by conjugation), and the diamond operators `⟨m⟩_{(1)}, ⟨n⟩_{(1)}` and `R(⟨n⟩)` are
`Q`-rational, so they commute with that conjugation action through `T_p`. Applying `σ⋆` to Theorem 2 and
using (a):
`θ_r = Kum^♮(Φ̄_r^mod) = Kum^♮(σ⋆Φ̄_r^mod) = σ⋆Kum^♮(Φ̄_r^mod) = σ⋆θ_r`.
So `θ_r` is ⋆-invariant, i.e. it is `Gal(F'_r/K_0)`-invariant for the twisted action on `H^1(F'_r, T_r^♮)`;
by inflation–restriction it is the restriction of a unique class in `H^1(K_0, T_r^♮)`, because
`(T_r^♮)^{G_{F'_r}} = Hom_{Z_p}(B_r^bal, (T_pJ^{(1)}_r)^{G_{F'_r}}) = 0` (`J^{(1)}_r(F'_r)` finitely generated,
so `T_p` of its torsion vanishes — B1 F3/L3). Likewise `Kum^♮_r(Φ̄_r^mod)` is that unique class:

    Kum^♮_r(Φ̄_r^mod) = Contr_r^{A_r}(Δ_r^ét[e])   in H^1(K_0, T_r^♮),   Kum^♮_r injective (B5 L3, Lemma C).

**(c) The same statement read off BCPV's triple-dagger module (E′(a) of Lane 3, now derived).** BCPV's
descended object is `Δ_r^ét[[a,b,c]] ∈ H^1(K_0, (S^{⊗3}(2))^†)` with `† = ⟨𝛘⟩_r^{-1/2}` applied through the
**diagonal** map `Z_p[Δ] → Z_p[G_r]` (`defn_Gal_twisted_general`, BCPV.tex l.1361–1366; the diagonal is
explicit at l.1364). Under `G` (l.1331–1332) this class corresponds to the index-`e` class `Δ_r^ét[e]` over
`F_r`, whose Galois law is the index shift `σ_mΔ^ét[e] = Δ^ét[m^{-1}e]` (l.1257 via `cl_1`). The content of
(b) is exactly that `Contr_r^{A_r}` converts:
* the **diagonal p-part dagger** `⟨m⟩^{1/2}` on three factors into `⟨m⟩^{1/2}` on factor 1 alone — the two
  auxiliary half-twists cancel against `σ(A_r) = A_r⟨m⟩^{-1}` (`⟨m⟩^{1/2}⟨m⟩^{1/2}⟨m⟩^{-1} = 1`, B2/B3);
* the **tame part** into `⟨n⟩_{(1)}` together with `R(⟨n⟩)` on the carrier — the surviving `ε_g^{-1}` twist
  (B2; item 5, file 07).
So the contracted class lands in the factor-1 dagger with the tame carrier twist, i.e. in `H^1(K_0,T_r^♮)`:
**E′(a) holds, with the ⋆-action of B5 as the correct target twist.** It is derived here from A6 + B2, not
assumed; no independent computation of the étale twist is needed, and none of BCPV (4.9), Ohta II,
KLZ17 7.2.3(v) is used.

## §5. Hostile checks on item 2

| # | attack | finding |
|---|---|---|
| D2.1 | Does the Hom-valued statement need `Hom(B,H^1) ≅ H^1(Hom(B,T))` (i.e. `B` free)? | Not for Theorem 2 (evaluationwise). It is used only to *name* the target `H^1(K_0,T_r^♮)`; Lemma C supplies freeness anyway. PASS |
| D2.2 | Is `Contr_r^{A_r}` `G_{K_0}`-equivariant? | **No, and it must not be** (P3): `A_r` is only `F'_r`-rational. Equivariance holds for the ⋆-twisted action, which is how `T_r^♮` is defined. Using plain `G_{K_0}`-equivariance would be a TYPE error; §4(b) avoids it by transporting invariance along an identity proved over `F'_r`. PASS |
| D2.3 | Does the identity secretly need the packaged class, where `G` vs `μ_r` could inject `\|G_r\|`? | No: both sides are index-`e` objects (§3). The packaging enters only if one *chooses* to name the classes BCPV's way; `G` is then an isomorphism, not a multiplication (06). PASS |
| D2.4 | Künneth: does `[Π_{Γ(b)}]_*` kill the other components of `H^3(X̄^3)`? | Part of A6 (frozen); BCPV do the same computation for `ε_0[Z]` in Prop 6.2 (l.1773–1776). NOT re-derived. INPUT |
| D2.5 | Is `cl_1` on `CH^1_0(X) = J` the Kummer map? | Part of A6 (frozen); BCPV use the identification in `eqn_2023_11_21_1605` (l.1706–1713) on the local side. INPUT |
| D2.6 | Torsion/`e'_ord` subtleties in `Ĵ(F')⊗Z_p` | `e'_ord` is an idempotent of a finite `Z_p`-algebra acting on `Ĵ(F')`; B1 extension 1 handles idempotent cuts; `(U'_p)^{-1}` exists on the `e'`-part. PASS |
| D2.7 | Citation for (AJ-corr) (R1) | The numbered statement is still unpinned in the packet (Jannsen LNM 1400 §9 / Nekovář 2000 §1 named but not page-pinned; the packet has no copy). The charter freezes `SCALAR_D4 = PROVED_FORMAL`, so this is **carried, not a defect**: `NOT_PRINTED_IN_PACKET`, recorded in 09. |

## §6. Verdict for item 2

**ITEM 2 = PROVED** in the exact form of Theorem 2 (over `F'_r`, evaluationwise then Hom-valued) together
with §4 (⋆-invariance, unique descent to `K_0`, injectivity of `Kum^♮_r`). The upgrade from A6 is genuinely
formal: linearity + the frozen balance + Galois-equivariance of `Kum` + `(T_pJ)^{G_{F'_r}} = 0`.

ITEM2_STATUS = PROVED (Hom-valued D4 over F'_r; ⋆-invariant; unique descent to K_0; E′(a) derived)
