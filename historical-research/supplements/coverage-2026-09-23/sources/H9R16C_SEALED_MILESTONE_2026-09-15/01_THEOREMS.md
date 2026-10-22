# 01 — The sealed statements

Conventions (BCPV / DR22 / KLZ17): `ϖ_1(A,P) = (A,pP)` (`τ ↦ τ`); `ϖ_2(A,P) = (A/⟨Mp^sP⟩, P mod)`
(`τ ↦ pτ`); `U'_p = π_{1*}π_2^* =` DR22's `U_p^*`, the Poincaré adjoint of the classical `U_p`;
`W` = KLZ17's moduli Atkin–Lehner with a compatible system `ζ_{Mp^{s+1}}^p = ζ_{Mp^s}`; weight 2 throughout,
so `W^2 = id`, `W^{-1} = W`, `W^* = W_*`. `S_s = H^1_ét(X̄^g_s, Z_p(1))`.

## §1. MPC (L5-T3) — the modified-pairing level compatibility

> For any tame level `M` prime to `p` and every `r ≥ 1`, on **all** of `H^1(X_1(Mp^{r+1}))` (Betti, étale
> with any Tate twist, de Rham), integrally, with `A_s := W_{Mp^s}^{-1}(U'_p)^s`:
>
>     ϖ_1^* ∘ A_r ∘ ϖ_{1,*}  =  A_{r+1} ∘ N_{r+1,r} ,
>     equivalently ⟨ϖ_{1,*}y, A_r ϖ_{1,*}z⟩_r = ⟨y, A_{r+1} N_{r+1,r} z⟩_{r+1} .
>
> **`d_r = 1` exactly**: no power of `p`, no diamond unit, no sign, no pseudo-eigenvalue, no Gauss sum.
> No ordinarity is used.

Mechanism: the `p`-powers of Hida (6.6) and KLZ17 Prop 2.4.5 live in the **push-then-pull** composites
`ϖ_{i,*}ϖ_j^*`; MPC contains the **pull-after-push** composite `ϖ_2^*ϖ_{1,*}`, which is a sum over a coset
space and yields a group-ring *element*, not a scalar. Evidence: `evidence/…LANE5…/03`; numerics in
`evidence/…LANE5…/_verify/` (7 cases × 2 primes).

## §2. The norm element (L5-T2)

>     ϖ_2^* ∘ ϖ_{1,*} = U'_p ∘ N_{r+1,r} = N_{r+1,r} ∘ U'_p ,   N_{r+1,r} = Σ_{d ∈ K_r}⟨d⟩ ,
>     K_r = {d ≡ 1 mod Mp^r}, cyclic of order p.

`N_{r+1,r}` is central, inversion-invariant, satisfies `N² = pN` (hence is a **zero-divisor**, not a unit),
and its image under `Z_p[(Z/Mp^{r+1})^×] → Z_p[(Z/Mp^r)^×]` is `p·1`. Two independent proofs (double cosets;
moduli), plus two consistency checks and numerics.

## §3. Lemma W (L5-T1) and the tame transport (L5-T5)

>     ϖ_1 ∘ W_{s+1} = W_s ∘ ϖ_2 ,   ϖ_2 ∘ W_{s+1} = W_s ∘ ϖ_1      exactly; no diamond.
>
> Tame analogue, `t := N/N_g`, `pr^t_1(A,P) = (A,tP)`, `pr^t_2(A,P) = (A/⟨N_gp^sP⟩, P mod)`, with
> `ζ_{Np^s}^t = ζ_{N_gp^s}`:
>
>     pr^t_1 ∘ W_{Np^s} = W_{N_gp^s} ∘ pr^t_2 ,   pr^t_2 ∘ W_{Np^s} = W_{N_gp^s} ∘ pr^t_1 .

Equivalently `pr^t_{2,*} = W_{N_gp^s} ∘ pr^t_{1,*} ∘ W_{Np^s}` (the exact form; **not** "a tame Hecke
scalar", which holds only after projecting to lines where each `W` acts by a scalar).

## §4. The group-ring form (L5-T4)

> With `⟨⟨x,y⟩⟩_s := Σ_{σ∈Δ_s} ⟨x, A_s⟨σ⟩y⟩_s [σ^{-1}]` and `π: Z_p[Δ_{r+1}] → Z_p[Δ_r]`:
>
>     π( ⟨⟨x,y⟩⟩_{r+1} ) = ⟨⟨ϖ_{1,*}x, ϖ_{1,*}y⟩⟩_r ,    constant 1.

This is the finite-level content of the Λ-adic pairing that KLZ17 `thm:ordinaryfiltration` states
(attributed to Ohta 2000); it is **derived here, not extracted** — Ohta 2000 was never obtained.

## §5. `A_r` is self-adjoint (second audit)

> In weight 2, `W^t = W` and `WU'_p = U_pW`, hence
>
>     A_r^t = ((U'_p)^r)^t W^t = (U_p)^r W = W (U'_p)^r = A_r .

Consequence: **both orientations of `Γ_A` induce the same bilinear form**. Every orientation caveat in the
earlier record is vacuous in weight 2. Numerically verified.

## §6. The carrier (C1, with its three mandatory narrowings)

> After the `A_r`-transport and passage to the transported commutative primed ordinary Hecke model
> (`ι_r(u') = A_r^{-1}ρ_r(u')A_r = u'`), the balancing relation `(t_2u')⊗t_3 ∼ t_2⊗u't_3` **is**
> `R_r`-bilinearity, so
>
>     B^bal_r = R_r ⊗_{R_r} R_r ≅ R_r ,   [t_2⊗t_3] ↦ t_2t_3 ,
>
> finite **free** over `Z_p`.

**Narrowings, all mandatory:**
1. `R_r` is the **native**-level `e'_ord𝕋'_{N_gp^r}⊗Z_p` — never a common-level algebra;
2. both auxiliary coefficient modules must be the **regular** `R_r`-module;
3. the interchange `Hom_{Z_p}(B,H^1(F,T)) = H^1(F,Hom_{Z_p}(B,T))` holds for `F ⊇ Q(μ_N)` (where the
   carrier is Galois-trivial) and **must not** be applied to the `⋆`-twisted module over `K_0`.

**Commutativity of `𝕋'` is load-bearing** (`ρ_r` is an anti-involution; the collapse fails without it).

## §7. `H_π` — the Hecke transition maps (PROVED)

> Let `p` be odd, `p ∤ N_g`, `r ≥ 1`. There is a **unique** homomorphism of `Z_p`-algebras
> `π_r : 𝕋'_{N_gp^{r+1}} → 𝕋'_{N_gp^r}` with `ϖ_{1,*} ∘ t = π_r(t) ∘ ϖ_{1,*}` in `Hom_{Z_p}(S_{r+1},S_r)`
> for every `t`; on generators `T'_ℓ ↦ T'_ℓ`, `U'_p ↦ U'_p`, `U'_ℓ ↦ U'_ℓ`, `⟨d̃⟩ ↦ ⟨d̃ mod N_gp^r⟩`.
> It is **surjective** (never injective for `r ≥ 1`), satisfies `π_r(e'_ord) = e'_ord`, and induces a
> surjective `π_r : R_{r+1} ↠ R_r`. Integral over `Z_p`; **all odd `p`**; **no ordinarity hypothesis**.

**The structural fact, reusable:** `ϖ_2^*` carries the **primed** ring; `ϖ_1^*` carries the **unprimed** one
(`ϖ_2^* = W_{r+1}ϖ_1^*W_r`, then conjugate `ϖ_1^*U_p = U_pϖ_1^*` by `W`). This is why `H_π` is not a citation
of Hida's printed tower, whose transition is restriction along `ϖ_1^*` for the unprimed algebra.
**Well-definedness** is the real content: `ϖ_{1,*}` is not injective, so the kernel inclusion runs the other
way and is supplied by the injection `ϖ_2^*` — `ev_{r+1}(P) = 0 ⟹ ϖ_2^*ev_r(φ_rP) = 0 ⟹ ev_r(φ_rP) = 0`.
**Uniqueness** from `ϖ_{1,*}ϖ_1^* = p²` on a torsion-free module (`p` cancelled, never inverted).
Caveat: uniqueness does **not** transport to the Mordell–Weil carrier (`Ĵ` can have `p`-torsion); consumers
must take the `S`-level `π_r(t)`.

## §8. Hom-valued D4 and the ⋆-receptacle

> `Φ̄^mod_r : B^bal_r → Ĵ^{(1)}_r(F'_r)^{ord}`, `b ↦ pd^{t_f}_*(Π_{Γ(b),*}Δ^ord_r[e])` at one fixed cycle
> index `e`, lies in `𝒫^♮_r`; and for every `b`,
>
>     Kum_{F'_r}(Φ̄^mod_r(b)) = Contr_r^{A_r}(b)_*(Δ^ét_r[e])   in H^1(F'_r, T_pJ^{(1),ord}_r),
>
> both sides ⋆-invariant and the restrictions of unique classes over `K_0`, where the identity holds;
> `Kum^♮_r` injective. `(T^♮_r)^{G_{F'_r}} = 0` makes the `K_0`-descent an isomorphism.

The ⋆-action, with `n_σ = χ_cyc(σ) mod N`, `m_σ = ⟨χ_cyc(σ)⟩`:
`(σ⋆Φ)(b) = ⟨m_σ⟩^{-1/2}_{(1)}⟨n_σ⟩^{-1}_{(1)}·σ(Φ(R(⟨n_σ⟩)^{-1}b))`. The `p`-part of the twist cancels on
the carrier and survives only on factor 1 (so the post-contraction dagger group is the **factor-1 cyclic
quotient**, not the triple `G_r`); the tame part does **not** cancel and is the `ε_g^{-1}` (`g^c`) carrier
twist.

## §9. The tower and the inverse-limit module

The theorem of `00`, with: constant exactly 1; the only `p` anywhere is `π_r(N_{r+1,r}) = p`; no `|G_r|`,
no `p^3`, no `p^{±1}`, `p^{±2}`; both normalization exponents `(s, 2s)` **forced**, not chosen. A system
satisfying both this relation and the naive `ϖ_{1,*}`-relation has `(1−p)π_r^*Q_r = 0`, hence `Q_r = 0` —
the naive limit meets this one only in `0`.
