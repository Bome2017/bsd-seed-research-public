# 04 — C3 (Hom-valued D4)  [SECOND referee, independent]

**Verdict: CONFIRMED.** The upgrade from the scalar/evaluationwise A6 to the `Hom`-valued identity is
exact, with one input A6 does not itself supply (the factor-1 tame push-down) and one hypothesis it
inherits from C1 (freeness). No type error found at the contravariance seam.

## §1. Types, written out

* `S_r := H^1_ét(X̄_1(Np^r), Z_p)` (common level); `Δ^ét_r[e] := cl_1(Δ^{ord}_r[e]) ∈
  H^1(Q(μ_{p^r}), S_r^{⊗3}(2))` (BCPV l.1307, Künneth `K` already applied).
* `Contr_r^{A_r}(b) : S_r^{⊗3}(2) → T_pJ^{(1),ord}_r`,
  `y_1⊗y_2⊗y_3 ↦ pd^{t_f}_*(y_1)·⟨pd^t_*y_2, ρ_r(t_2)A_rt_3 pd^t_*y_3⟩_{N_gp^r}`.
  Twists: `S⊗S → H^2(X̄)(?) ≅ Z_p(−1)` on factors 2,3, so `S^{⊗3}(2) → S_r^{(1)}(1) = T_pJ^{(1)}_r`. ✓
* Linearity and well-definedness in `b`: as in C2 §1, `ρ_r(t_2u')A_rt_3 = ρ_r(t_2)A_ru't_3`, so
  `b ↦ Contr_r^{A_r}(b)` is a `Z_p`-linear map `B^bal_r → Hom(S_r^{⊗3}(2), T_pJ^{(1),ord}_r)`,
  equivalently a map `Contr_r^{A_r} : S_r^{⊗3}(2) → Hom_{Z_p}(B^bal_r, T_pJ^{(1),ord}_r) = T^♮_r`.
* Galois: `pd^t, pd^{t_f}, ρ_r, t_2, t_3, U'_p` are over `Q`; `W_{N_gp^r}` over `Q(μ_{N_gp^r}) ⊆ F'_r`.
  So `Contr_r^{A_r}` is a `G_{F'_r}`-map and induces
  `H^1(F'_r, S_r^{⊗3}(2)) → H^1(F'_r, T^♮_r)` after `res_{F'_r}` of `Δ^ét_r[e]`. ✓ (This is P3: it is
  **not** plainly `G_{K_0}`-equivariant; equivariance only holds for the `⋆`-twisted structure.)

## §2. Evaluationwise D4 ⇒ `Hom`-valued D4

**(i) Evaluationwise.** A6 (input, `PROVED_FORMAL`) gives, for each `b = [t_2⊗t_3]`,
`Kum(Π_{Γ(b),*}Δ^{ord}_r[e]) = Contr^{Γ(b)}_*(Δ^ét_r[e])` — A6 is stated for an arbitrary algebraic
correspondence `Γ` on the auxiliary factors, and `Γ(b) = (pd^t)^t∘ρ_r(t_2)A_rt_3∘pd^t` is one.
A6 does **not** contain the factor-1 tame push-down `pd^{t_f}_*`; it is supplied by B1 (Kummer
naturality for a homomorphism of abelian varieties over `F'_r`):
`Kum ∘ pd^{t_f}_* = H^1(F'_r, T_p pd^{t_f}_*) ∘ Kum`. Composing,

    Kum_{F'_r}(Φ̄^mod_r(b)) = Contr_r^{A_r}(b)_*(Δ^ét_r[e])   in H^1(F'_r, T_pJ^{(1),ord}_r),  ∀ b.

(Equivalently, absorb `pd^{t_f}` into the correspondence: `pd^{t_f}_*∘(X_{14}×Γ)_*` is again
`(X_{1,4'}×Γ)_*` with the fourth factor at native level, so it is inside A6's scope either way.)

**(ii) Upgrade.** By C1, `B^bal_r ≅ R_r` is finite **free** over `Z_p`; over `F'_r` the carrier
carries the trivial Galois action (C1 §4.3), so

    Hom_{Z_p}(B^bal_r, H^1(F'_r, T_pJ^{(1),ord}_r)) = H^1(F'_r, Hom_{Z_p}(B^bal_r, T_pJ^{(1),ord}_r))
                                                    = H^1(F'_r, T^♮_r),

the identification being "evaluate at `b`". Both `b ↦ Kum(Φ̄^mod_r(b))` and
`b ↦ Contr_r^{A_r}(b)_*(Δ^ét_r[e])` are `Z_p`-linear in `b` and agree for every `b` by (i); hence they
are the same element of `H^1(F'_r, T^♮_r)`:

    Kum^♮_r(Φ̄^mod_r) = Contr_r^{A_r}(Δ^ét_r[e])   in H^1(F'_r, T^♮_r).                (C3)

**This is exactly where C1's freeness is consumed**, and it is consumed after it is earned. Without
freeness (Lane 4 `03` §6.3's worry) the left-hand side would only be an element of
`Hom(B^bal_r, H^1(F'_r, ·))`, which is not a cohomology group of a Galois module and cannot meet the
class side.

## §3. Descent to `K_0`, injectivity

`(T^♮_r)^{G_{F'_r}} = Hom_{Z_p}(B^bal_r, (e'_{ord}T_pJ^{(1)}_r)^{G_{F'_r}}) = 0`, because
`(T_pJ)^{G_F} = T_p(J(F)[p^∞]) = 0` for a number field `F`. Inflation–restriction for
`1 → G_{F'_r} → G_{K_0} → Gal(F'_r/K_0) → 1` therefore has vanishing `H^1` **and** `H^2` of the finite
quotient with `H^0`-coefficients, so

    H^1(K_0, T^♮_r)  ≅  H^1(F'_r, T^♮_r)^{Gal(F'_r/K_0), ⋆} ,

an isomorphism, not merely an injection. The left side of (C3) is `⋆`-invariant because
`Φ̄^mod_r ∈ 𝒫^♮_r` (C2) and `Kum` is Galois-natural while the twist is by `Q`-rational diamonds;
the right side is `⋆`-invariant because it is equal to it. Both therefore descend to one and the same
unique class in `H^1(K_0, T^♮_r)`, and the identity holds there. `Kum^♮_r : 𝒫^♮_r → H^1(K_0,T^♮_r)`
is injective (evaluationwise Kummer injectivity on `Ĵ^{(1)}_r(F'_r)` plus injectivity of `res`).

## §4. The contravariance seam (the operator's second pressure point)

There is **no** type error here. `T^♮_r = Hom_{Z_p}(B^bal_r, −)` is contravariant in the carrier; the
carrier map of the tower `res^bal_{r+1,r} : B^bal_{r+1} → B^bal_r` runs **with** the tower (it is
`π_r` under `B^bal_s ≅ R_s`, C1), so `π_r^* = (−)∘res^bal` runs **against** it:

    π_r^* : Hom(B^bal_r, M) → Hom(B^bal_{r+1}, M)   (injective when res^bal is onto).

C3's objects are all at one level, so the seam is only exercised in C4; there the two sides
`τ_r^{MW}(Q_{r+1}) = ϖ^{(1)}_{1,*}∘Q_{r+1}` (post-composition, covariant in the target, level `r+1`
carrier) and `π_r^*Q_r` (pre-composition, level `r+1` carrier) land in the *same* module
`Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})`. Pre- and post-composition commute, and B1's
naturality clause covers exactly this: `Kum(x∘β) = Kum(x)∘β` for `Z_p`-linear `β : B' → B`. No
arrow `𝒫^♮_{r+1} → 𝒫^♮_r` is used or needed.

## §5. Lane 3's `E′(a)`

C3's parenthetical is correct **and its direction of inference must be recorded**: `E′(a)` (the
contracted class lands in the factor-1 dagger with the tame carrier twist) is *derived from* the
point side — the class equals `Kum^♮_r` of a point already shown to lie in `𝒫^♮_r` (C2), so its
receptacle is forced. It is therefore a corollary of C2 + A6 + B1, not an independent obligation,
and correspondingly it is **not** independent evidence for C2. Lane 3's `NOT_PRINTED` status for
`E′(a)` as a statement about the étale side alone is unchanged; what closes here is the *packaged*
statement needed by the assembly.

## §6. Status

| sub-claim | status |
|---|---|
| `Contr_r^{A_r}` well typed, `Z_p`-linear on `B^bal_r`, `G_{F'_r}`-equivariant | PROVED |
| evaluationwise D4 including the factor-1 push-down | PROVED (A6 + B1) |
| `Hom`-valued upgrade `Kum^♮_r(Φ̄^mod_r) = Contr_r^{A_r}(Δ^ét_r[e])` | PROVED (uses C1 freeness) |
| both sides `⋆`-invariant; unique descent to `H^1(K_0,T^♮_r)`; identity there | PROVED |
| `Kum^♮_r` injective | PROVED |
| `E′(a)` follows, no separate computation | PROVED, with §5's directionality recorded |

**C3 = CONFIRMED.**
