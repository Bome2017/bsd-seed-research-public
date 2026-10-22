# 01 — The eight claims (statements only; no argument is supplied for any of them)

Notation: `p` odd; `N_f, N_g` tame levels, `N = lcm(N_f,N_g)`, `t = N/N_g`, `t_f = N/N_f`, `p ∤ N`;
`X_s = X_1(Np^s)`, `X^g_s = X_1(N_gp^s)`, `X^f_s = X_1(N_fp^s)`; `F'_r = Q(μ_{Np^r})`, `K_0 = Q(μ_p)`;
`A_r = W_{N_gp^r}^{-1}(U'_p)^r`; `ϖ_1(A,P) = (A,pP)`; tame degeneracies `pr^t_1(A,P) = (A,tP)` (forgetful) and
`pr^t_2(A,P) = (A/⟨N_gp^sP⟩, P mod)` (quotient), written `pd^t` when the choice is left open; `ρ_r` the raw
Rosati/transpose of the frozen H9R16-A/B text; `Π_Z = X_{14}×Z`, `Z = X_{23}` the plain diagonal
(BCPV.tex l.1647); `e = (a,b,c)` a cycle index via Teichmüller lifts, the same at every level.

**C1 (carrier).** After the `A_r`-transport and passage to the transported commutative primed ordinary Hecke
model (`ι_r(u') = A_r^{-1}ρ_r(u')A_r = u'`), the balancing relation `(t_2u')⊗t_3 ∼ t_2⊗u't_3` is exactly
`R_r`-bilinearity for `R_r := e'_ord𝕋'_{N_gp^r}⊗Z_p`, so

    B_r^bal = R_r ⊗_{R_r} R_r ≅ R_r   (t_2⊗t_3 ↦ t_2t_3),

a finite **free** `Z_p`-module. Consequently `rank_{Z_p}T_r^♮ = rank_{Z_p}(R_r)·2g^{(1)}_r` with no `|G_r|`
factor, and `Hom_{Z_p}(B_r^bal, H^1(F,T)) = H^1(F, Hom_{Z_p}(B_r^bal,T))` for finite free `T`.

**C2 (point object).** With `e` fixed and one choice of `pd^t`, `pd^{t_f}` used uniformly in `r`,

    Φ̄_r^mod : B_r^bal → Ĵ^{(1)}_r(F'_r)^{ord},
    b = [t_2⊗t_3] ↦ pd^{t_f}_*( Π_{Γ(b),*} Δ_r^{ord}[e] ),   Γ(b) = (pd^t)^t ∘ ρ_r(t_2) A_r t_3 ∘ pd^t,

is well defined on the quotient, coincides with the frozen H9R16-A/B functional
`Φ_r^mod(t_2,t_3) = Π_{Z,*}((1⊗t_2⊗A_rt_3)Δ_r^{ord})`, and lies in `𝒫_r^♮` — the ⋆-invariants of Lane 4 `04` §1,

    (σ⋆Φ)(b) = ⟨m_σ⟩^{-1/2}_{(1)} ⟨n_σ⟩^{-1}_{(1)} · σ( Φ( R(⟨n_σ⟩)^{-1} b ) ),  σ ∈ Gal(F'_r/K_0).

The orientation of `Γ_A` is the one whose induced bilinear form is `(y_2,y_3) ↦ ⟨y_2, A_r y_3⟩`; the opposite
orientation (`A_r^t = (U_p)^rW`) is not the frozen functional.

**C3 (Hom-valued D4).** For every `b ∈ B_r^bal`,

    Kum_{F'_r}( Φ̄_r^mod(b) ) = Contr_r^{A_r}(b)_*( Δ_r^ét[e] )   in H^1(F'_r, T_pJ^{(1),ord}_r),

where `Contr_r^{A_r}(b): y_1⊗y_2⊗y_3 ↦ pd^{t_f}_*(y_1)·⟨pd^t_*y_2, ρ_r(t_2)A_rt_3 pd^t_*y_3⟩_{N_gp^r}`;
equivalently `Kum^♮_r(Φ̄_r^mod) = Contr_r^{A_r}(Δ_r^ét[e])` in `H^1(F'_r, T_r^♮)`,
`T_r^♮ = Hom_{Z_p}(B_r^bal, T_pJ^{(1),ord}_r)` with the ⋆-action. Both sides are ⋆-invariant and are the
restrictions of unique classes in `H^1(K_0, T_r^♮)`, where the identity holds; `Kum^♮_r` is injective.
(Lane 3's `E′(a)` — that the contracted class lands in the factor-1 dagger with the tame carrier twist — is
asserted to follow, not to need separate computation.)

**C4 (tower relation, constant 1).** With `Q_s := (U'_p)^{-s}_{(1)} ∘ Φ̄_s^mod ∘ (U'_p)^{-2s}_{carrier}`,
`τ_r^MW(x) := ϖ^{(1)}_{1,*}∘x`, `π_r^*(y) := y∘res^bal_{r+1,r}`, and `N_{r+1,r} := Σ_{d ≡ 1 (N_gp^r)}⟨d⟩` the
**native-level** norm element:

    τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r}) = π_r^* Q_r   in Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord}),

integrally, with constant exactly 1. Sub-claim C4b: with the **factor-1 normalization alone** (Lane 4 `04`
`(T♮_r)`, Lane 5 `05` §4 as literally written) the constant is **not** 1 — the leftover is `(1⊗(U'_p)^2)` on the
carrier, matching BCPV's `a_p(g)^{-2r}`. Sub-claim C4c: Kummer injectivity is applied over `F'_{r+1}`,
evaluationwise, and no class over `K_0` is needed for this step.

**C5 (push-down independence).** C4 and its constant are unchanged if `pd^t`, `pd^{t_f}` are taken to be the
quotient maps rather than the forgetful maps, provided the choice is uniform in `r`. Only the *identity of the
constructed point* changes: by the tame-degeneracy interchange, a tame Hecke scalar at the primes dividing `t`
on `h`-isotypic quotients. (Which map BCPV intend is `NOT_PRINTED`: they write `ϖ_{1,*}` for the tame direction
at BCPV.tex l.1457 and l.1486–1487, and define `ϖ_1` only in the p-direction at l.1198–1199.)

**C6 (no rank factor).** No `|G_r| = p^{3(r−1)}`, no `p^3`, no `p^{±1}`, `p^{±2}` enters the assembly. The only
`p` is `π_r(N_{r+1,r}) = p·1`. The multiplication-type identification `μ_r : g⊗v ↦ ⟨g⟩v` is **not** used; applied
to the Lane 5 packaging `Σ_{g∈G_r}P_r[g·(a,b,c)]⊗g` it would give `Φ_r^mod∘(1⊗Σ_g⟨d_2d_3⟩^{-1})`, i.e.
`|G_r|`-or-`0` on a branch, not a rescaling. BCPV's own conversion is the identity-coefficient map `G`
(BCPV.tex l.1331–1332).

**C7 (tame twist preserved).** The tame `ε_g^{-1}` (`g^c`) carrier twist is preserved by `ϖ^{(1)}_{1,*}`, by
`π_r`/`res^bal`, by `1⊗N_{r+1,r}` (whose elements satisfy `d ≡ 1 mod N_g`, so the tame part is trivial), by both
tame push-downs, and by the `U'_p` normalizations; both sides of C4 lie in one and the same ⋆-module.

**C8 (inverse limit).** With the above,

    𝒫^♮_∞ := { (Q_r)_{r≥1} ∈ ∏_r 𝒫^♮_r : τ_r^MW(Q_{r+1})∘(1⊗N_{r+1,r}) = π_r^*(Q_r) ∀r },

the limit taken inside `Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})^⋆`, into which `π_r^*` embeds `𝒫^♮_r`
injectively, is a module over `𝕋'_∞(N_g) = lim_r R_r`, and the system `𝒬_∞ = (Q_r)_r` built from BCPV's cycles
lies in it integrally. The naive inverse limit along `ϖ_{1,*}` alone is **not** this object (it would need
`Q_r ∈ p^rĴ`).

## What is *not* claimed (do not adjudicate these)

* No claim about `G_BIG_KUMMER_TRACE`, density, localization, `f`-branch extraction or weight one.
* No claim that `(AJ-corr)` has a pinned numbered citation (it does not; frozen `PROVED_FORMAL`).
* No claim that `H_π` (the ring maps `π_r` with `ϖ_{1,*}t = π_r(t)ϖ_{1,*}`) is proved anywhere; it is part of
  the statement of C4.
* No claim that the fixed-index class `Δ_r^ét[e]` equals BCPV's symmetrized `Δ_r^ét`.
