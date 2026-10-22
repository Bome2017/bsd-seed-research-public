# 03 — ITEM 1: does the Lane-5 contraction induce exactly Φ̄_r^mod ∈ 𝒫_r^♮ ?

Referee: final assembly, 2026-09-15. Inputs used: A1–A6 (02 §A), B1–B8 (02 §B), §C frozen definitions,
02a erratum. Nothing downstream of H9R16-C is used. Status vocabulary per 01 §2.3.

## §1. Notation fixed for files 03–08 (nothing here is new mathematics)

* `p` odd, `N_f`, `N_g` tame levels, `N := lcm(N_f,N_g)`, `t := N/N_g`, `t_f := N/N_f`, `p ∤ N`.
* `X_s := X_1(Np^s)` (common level), `X_s^g := X_1(N_gp^s)`, `X_s^f := X_1(N_fp^s)`; point-of-order model.
* p-direction degeneracies at any tame level `M`: `ϖ_1(A,P) = (A,pP)`, `ϖ_2(A,P) = (A/⟨Mp^sP⟩, P mod)`.
* tame-direction degeneracies `X_1(Np^s) → X_1(N_gp^s)`:
  `pr^t_1(A,P) = (A,tP)` (forgetful), `pr^t_2(A,P) = (A/⟨N_gp^sP⟩, P mod)` (quotient); likewise `pr^{t_f}_i`
  onto `X^f_s`. **Which of `pr^t_1`, `pr^t_2` is "BCPV's tame push-down" is NOT decided here** (02a §1); it is
  decided, or shown immaterial, in 05 (item 3). In this file the symbol `pd^t` denotes whichever is chosen,
  uniformly in `s`.
* roots of unity: one compatible system `ζ_m = e^{2πi/m}`, so that simultaneously
  `ζ_{Np^{s+1}}^p = ζ_{Np^s}` (needed by A1/A3) and `ζ_{Np^s}^t = ζ_{N_gp^s}` (needed by A5). Both hold for
  this system; no other normalization enters (checked: `(e^{2πi/Np^{s+1}})^p = e^{2πi/Np^s}`,
  `(e^{2πi/Np^s})^t = e^{2πi/N_gp^s}`).
* `F'_r := Q(μ_{Np^r})`, `K_0 := Q(μ_p)`; `S_s := H^1_ét(X̄_s, Z_p(1)) ≅ T_pJ_s`.
* `A_r := W_{N_gp^r}^{-1}(U'_p)^r = W_{N_gp^r}(U'_p)^r` on `X^g_r` (weight 2, §C, A1 conventions).

## §2. The Lane-5 contraction as one algebraic correspondence, and its identity with the frozen Φ_r^mod

**2.1 (frozen form, §C).** `Φ_r^mod(t_2,t_3) := Π_{Z,*}((1 ⊗ t_2 ⊗ A_r t_3) Δ_r^ord)`, `Π_Z := X_{14} × Z`,
`Z = X_{23}` the *plain* diagonal (BCPV fn. 11, BCPV.tex l.1647: `Π_Z := X_{14}×Z ⊂ X^4`, `𝒵_r` its class).

**2.2 (Lane-5 form, 05 §2).** `Π_Γ := X_{14} × Γ`, `Γ = Γ_{t_2}^t ∘ Γ_A ∘ Γ_{t_3} ⊂ X_2 × X_3`, and
`Φ_r^mod(t_2⊗t_3) := Π_{Γ,*}Δ_r^ord`.

**2.3 (they agree — written out).** Correspondence composition is associative and
`Π_{Z,*}∘(1⊗c_2⊗c_3)_* = Π_{Z∘(c_2×c_3),*}`, with `Z∘(c_2×c_3) = c_2^t ∘ c_3` as a correspondence
`X_2 → X_3` under the orientation of 2.4. Taking `c_2 = t_2`, `c_3 = A_r t_3` gives
`Γ = ρ_r(t_2)∘A_r∘t_3`, where `ρ_r` is the raw Rosati/transpose of §C (`T'_ℓ ↦ T_ℓ`, `U'_p ↦ U_p`,
`⟨d⟩ ↦ ⟨d⟩^{-1}`). Cohomologically: `Contr((1⊗t_2⊗A_rt_3)(y_1⊗y_2⊗y_3)) = ⟨t_2y_2, A_rt_3y_3⟩·y_1
= ⟨y_2, ρ_r(t_2)A_rt_3 y_3⟩·y_1`. So **Lane 5's `Γ_{t_2}^t` is exactly `ρ_r(t_2)`** and the two forms are
the same map. TYPE_CHECK = PASS. (No claim is made that `Γ` is effective; it is a Z-combination of
correspondences, which is all that A6 and §2.5 need.)

**2.4 Orientation of Γ_A (P5, and the A6 caveat), decided.** The frozen formula puts `A_r` on **factor 3
of the cycle**, and contracts factors 2,3 by the *plain* diagonal. Hence the induced bilinear form is
`(y_2,y_3) ↦ ⟨y_2, A_r y_3⟩` and the required orientation of `Γ_A` is `[Γ_A]_* = A_r` **acting on the
factor-3 slot**, which is precisely the orientation Lane 5 `05` §2 fixes. The opposite orientation would
give `⟨y_2, A_r^t y_3⟩` with `A_r^t = (U_p)^rW_{N_gp^r}`; that is *not* the frozen functional, and it is
excluded here, not chosen by convention: it contradicts §C's balance chain
`Φ^P(t_2u',A_rt_3) = Φ^P(t_2, ρ_r(u')A_rt_3) = Φ^P(t_2, A_ru't_3)`, which uses `ρ_r(u')A_r = A_ru'`, an
identity for `A_r` and **false for `A_r^t`** in general (`ρ_r(u')A_r^t = A_r^t u'` would need
`W^{-1}ρ(u')W = u'` on the other side; with `ρ_r(U'_p) = U_p` one gets `ρ(U'_p)A_r^t = U_p(U_p)^rW`
whereas `A_r^tU'_p = (U_p)^rWU'_p = (U_p)^{r+1}W`, equal only because `WU'_p = U_pW`; for `⟨d⟩` one gets
`ρ(⟨d⟩)A_r^t = ⟨d⟩^{-1}(U_p)^rW = (U_p)^rW⟨d⟩ = A_r^t⟨d⟩`, so the diamond test does *not* separate them).
**Recorded honestly:** the diamond and `U'_p` tests do not separate the two orientations, because
`A_r^t = WA_rW^{-1}·(unit)`-type conjugates satisfy the same balance. What separates them is the *printed*
frozen formula `(1 ⊗ t_2 ⊗ A_r t_3)Δ^ord` together with the plain diagonal `Z`: `A_r` is applied to the
cycle's third factor, and no transpose is applied to it. So the orientation is FIXED BY §C, and Lane 5's
choice matches it. The A6 caveat is therefore discharged, and nothing below depends on the alternative.

**2.5 Output factor.** `X_{14}` is the diagonal in `X_1 × X_4`, so a correspondence `c` applied to factor 1
of the cycle appears as `c` on the output: `Π_{Γ,*}∘(c⊗1⊗1)_* = c_*∘Π_{Γ,*}`. In particular
`e'_ord` (present in `Δ^ord`) and `U'_p` on factor 1 pass to the output Jacobian — this is what Lane 5 `05`
§4 uses ("`U'_p` on factor 1 = `U'_p` on `J_r`"), and it is proved, not assumed, by that identity.
Also `Π_{Γ,*}: CH^2_0 → CH^1_0 = J`, because `cl_0(Π_{Γ,*}z) = [Π_Γ]_*cl_0(z) = 0`; with
`Δ_r^ord ∈ CH^2_0` (BCPV Lemma `DR_Lemma_2_5`(i), l.1252–1260) the "degree-zero correction" of Lane 4 `01`
§6 is automatic and costs nothing.

## §3. The carrier and the balancing quotient, written explicitly

`B_r^bal := ( 𝕋'^{(2),ord}_r ⊗_{Z_p} 𝕋'^{(3),ord}_r ) / ⟨ (t_2u')⊗t_3 − t_2⊗u't_3 : u' ∈ 𝕋'^{ord}_r ⟩`
(Lane 4 `01` §6; §C "carrier": the `Z_p`-module quotient by `(t_2u')⊗t_3 − t_2⊗u't_3` **after `A_r`
transport**). Both auxiliary Hecke algebras are at the **native** level `N_gp^r` (this is forced: `A_r` is a
native-level operator, and `NATIVE_LEVEL_RESTRICTION = ESSENTIAL` in both local copies of the checkpoint,
paste-cache l.149 and recovered copy l.1259).

**Well-definedness on the quotient.** `Φ_r^mod(t_2u',t_3) = Φ_r^mod(t_2,u't_3)` is frozen (§C,
`G_BALANCED_HECKE_DUALITY = PROVED_FOR_A_r_TWISTED_MODIFIED_FUNCTIONAL`), via `ρ_r(u')A_r = A_ru'`.
So the map descends:  `Φ̄_r^mod : B_r^bal → Ĵ_r^{(1)}(F'_r)^{ord}`.
The same relation makes the *étale* contraction `Contr_r^{A_r}` descend to `B_r^bal` (used in 04).

`B_r^bal` is a finitely generated `Z_p`-module, not necessarily free (a quotient of a free module). Every
statement below is therefore made **evaluationwise on `b ∈ B_r^bal`** and only then read as an identity in
`Hom_{Z_p}(B_r^bal, −)`; no step uses `Hom(B,H^1(F,T)) ≅ H^1(F,Hom(B,T))` (which would need freeness).
This is the discipline Lane 4 `03` §6.3 asks for, and it costs nothing.

## §4. The explicit map: from the Lane-5 data to Φ̄_r^mod — and what happens to the packaging

Lane 5 `05` §2 produces three distinct objects. They must not be conflated:

| Lane-5 object | type | role |
|---|---|---|
| `P_r[d] := Π_{A,*}Δ_r^ord[d]` | element of `Ĵ(F'_r)` (common level) | the primitive datum |
| `P_r[[a,b,c]] := Σ_{g∈G_r} P_r[g·(a,b,c)] ⊗ g` | element of `Ĵ(F'_r) ⊗ Z_p[G_r]` | intermediate packaging only |
| `Φ_r^mod(t_2⊗t_3) := Π_{Γ,*}Δ_r^ord` | `Z_p`-linear map on the carrier | the object 𝒫_r^♮ needs |

**The map required by item 1 is the composite**

    Φ̄_r^mod : B_r^bal → Ĵ_r^{(1)}(F'_r)^{ord},
    b = [t_2 ⊗ t_3]  ↦  pd^{t_f}_*( Π_{Γ(b),*} Δ_r^{ord}[e] ),   Γ(b) = ρ_r(t_2) ∘ A_r ∘ t_3  (as in §2, with
    the tame push-down of factors 2,3 written into Γ(b): Γ(b) = (pd^t)^t ∘ ρ_r(t_2)A_r t_3 ∘ pd^t ),

with **one fixed cycle index** `e = (a,b,c) ∈ (F_p^×)^3` regarded in `G̃_r` by Teichmüller lift (the same
`(a,b,c)` at every level `r`, so that `e_{r+1} ↦ e_r` under `G̃_{r+1} → G̃_r`, which is what BCPV
`DR_lemma_2_5_dual` (l.1411–1415) and `cor_DR_lemma_2_5_dual` (l.1421) require).

**The packaging is not applied, and that is the correct reading, not a weakening.**
* BCPV's packaging `Δ^ét[[a,b,c]] = Σ_{g∈G_r}Δ^ét[g·(a,b,c)]⟨g⟩` (l.1317) is a *cohomological* device: it
  converts the index-shift Galois law `σ_mΔ^ét[e] = Δ^ét[m^{-1}e]` into `Z_p[G_r]`-valued equivariance so
  that the class descends to `K_0` after the dagger twist (l.1361–1379). Its inverse is `G`
  (l.1331–1332): `ψ = Σψ_g g ↦ ψ_e`, i.e. **reading off the identity coefficient**.
* On the point side the same law is already available *without* packaging: for `σ ∈ Gal(F'_r/K_0)` the
  index shift is realised by a **diagonal diamond** — `σ_mΔ_r^{ord}[e] = Δ_r^{ord}[m^{-1}e] =
  ⟨μ,μ,μ⟩Δ_r^{ord}[e]` for `m = μ²` (BCPV `eqn_2023_11_11_1700` l.1257 with (4.1) l.1218 and
  `⟨a⟩W = W⟨a⟩^{-1}`) — and a diagonal diamond is transported through `Π_{Γ,*}` by §2.5 and the carrier
  action. That is exactly how B2 (Lane 2 (G2), Lane 4 L4-T3) computes the twisted law. **So the point-side
  analogue of BCPV's dagger is the ⋆-action of B5, and the point-side analogue of `G` is "use the fixed
  index `e`".** Concretely `G(P_r[[a,b,c]]) = P_r[(a,b,c)]`: the identity coefficient of the packaged point
  is the index-`e` point, so the composite *packaging → G* is the identity and the intermediate step is
  information-free.
* **The one identification that must be refused** is the multiplication-type map `μ_r : g⊗v ↦ ⟨g⟩v`
  (Lane 2 T4, P1). It does not return `P_r[e]` and is not a rescaling of it: by (4.1) and §2.5,
  `μ_r(P_r[[a,b,c]]) = Σ_{g∈G_r} Φ_r^mod(t_2 ⊗ ⟨g_2g_3⟩^{-1}t_3)`, a **diamond average over the carrier**,
  a different functional. Quantified in 06 (item 4); no `|G_r|` or `p^3` enters the map of this section
  because that map never uses `μ_r`.

## §5. The ⋆-action, and membership Φ̄_r^mod ∈ 𝒫_r^♮

Precise ⋆ (B5, Lane 4 `04` §1), with `n_σ := χ_cyc(σ) mod N`, `m_σ := ⟨χ_cyc(σ)⟩ ∈ 1+pZ_p`:

    (σ⋆Φ)(b) := ⟨m_σ⟩^{-1/2}_{(1)} ⟨n_σ⟩^{-1}_{(1)} · σ( Φ( R(⟨n_σ⟩)^{-1} b ) ),   σ ∈ Gal(F'_r/K_0),
    𝒫_r^♮ = P_r^♮ = { Φ ∈ Hom_{Z_p}(B_r^bal, Ĵ_r^{(1)}(F'_r)^{ord}) : σ⋆Φ = Φ ∀σ }.

`R(⟨n⟩)` is the (central) tame diamond action on `B_r^bal`; it is well defined on the quotient because
diamonds are central in `𝕋'^{ord}` and `ρ_r(⟨n⟩) = ⟨n⟩^{-1}` still satisfies the balance relation.

B2 gives the transformation law of the contracted point (frozen; two independent derivations):
`σ ∘ Φ̄_r^mod = ⟨m_σ⟩^{1/2}_{(1)} ⟨n_σ⟩_{(1)} ∘ Φ̄_r^mod ∘ R(⟨n_σ⟩)` (Lane 4 L4-T3). Substituting,

    (σ⋆Φ̄_r^mod)(b) = ⟨m_σ⟩^{-1/2}⟨n_σ⟩^{-1}·[⟨m_σ⟩^{1/2}⟨n_σ⟩ Φ̄_r^mod(R(⟨n_σ⟩)R(⟨n_σ⟩)^{-1}b)] = Φ̄_r^mod(b),

so **Φ̄_r^mod ∈ 𝒫_r^♮**. The two frozen forms of B2 agree, as B2's own reconciliation states, and I have
re-checked the step: the tame diagonal diamond fixes `Δ_r^{ord}`, so `Φ = ⟨n⟩_{(1)}∘Φ∘(1⊗⟨n⟩²)` by balance,
whence Lane 2's `σΦ = ⟨c_r^{1/2}⟩_{(1)}Φ∘(1⊗⟨n⟩^{-1})` and Lane 4's
`σΦ = ⟨m⟩^{1/2}_{(1)}⟨n⟩_{(1)}Φ∘(1⊗⟨n⟩)` are the same statement.

Two structural facts used here and worth recording, since they are what makes the receptacle right:
* the p-part of the twist **cancels on the carrier** (`⟨m⟩^{1/2}·⟨m⟩^{1/2}·⟨m⟩^{-1} = 1`) and survives only
  on factor 1 — so the post-contraction dagger group is the factor-1 cyclic quotient (B3), not `G_r`;
* the tame part **does not cancel**; it is the `ε_g^{-1}` (`g^c`) carrier twist (B2, item 5 in 07).

## §6. The output level: the f-side tame push-down is part of the map

Lane 5 `05` §2 builds `P_r[d] ∈ J(F'_r)` with `J = Jac X_1(Np^r)` — **common** level — whereas 𝒫_r^♮'s target
is `Ĵ_r^{(1)}(F'_r)^{ord}` with `J^{(1)}_r = Jac X_1(N_fp^r)` (B5). The missing arrow is the f-side tame
push-down `pd^{t_f}_*: J_{Np^r} → J_{N_fp^r}` (BCPV's `pr_f`, l.1486–1487, the first leg of `pr_h`). It is:
Q-rational; compatible with `e'_ord` and `U'_p` (`pd^{t_f}_*U'_p = U'_ppd^{t_f}_*`, independent prime
directions); diamond-semilinear (`⟨d⟩_{Np^r} ↦ ⟨d mod N_fp^r⟩`). Hence it is ⋆-equivariant and maps the
common-level point into 𝒫_r^♮; and it commutes with `Π_{Γ,*}` because it acts on the output factor only,
while `Γ` acts on factors 2,3. **Item 1 is therefore stated for the composite of §4, not for Lane 5's
common-level `P_r[d]`.** (Which of `pd^{t_f}_1`, `pd^{t_f}_2` — same open point as on the g-side; 05.)

## §7. Verdict for item 1

**ITEM 1 = PROVED**, in the following exact form.

> Let `e = (a,b,c)` be a fixed index (Teichmüller lifts), `pd^t`, `pd^{t_f}` a fixed choice of tame
> degeneracy maps, used uniformly in `r`. Then
> `b ↦ pd^{t_f}_*(Π_{Γ(b),*}Δ_r^{ord}[e])`, `Γ(b) = (pd^t)^t∘ρ_r(t_2)A_rt_3∘pd^t`,
> is a well-defined `Z_p`-linear map `Φ̄_r^mod : B_r^bal → Ĵ^{(1)}_r(F'_r)^{ord}` which coincides with the
> frozen H9R16-A/B functional (§2.3, orientation §2.4), and it lies in `𝒫_r^♮` (§5).
> The Lane-5 group-ring packaging is intermediate and is removed by the identity-coefficient map `G`;
> the multiplication map `μ_r` is refused (§4).

Conditions carried forward (not defects of item 1):
1. the choice of `pd^t`, `pd^{t_f}` is not yet pinned to BCPV's text (02a §1) — item 3, file 05;
2. that no `|G_r|`/`p^3` re-enters through any identification — item 4, file 06;
3. the tame `ε_g^{-1}` twist is part of 𝒫_r^♮'s ⋆ and must survive the transitions — item 5, file 07.

ITEM1_STATUS = PROVED (explicit map, explicit ⋆, explicit carrier, orientation decided from §C)
