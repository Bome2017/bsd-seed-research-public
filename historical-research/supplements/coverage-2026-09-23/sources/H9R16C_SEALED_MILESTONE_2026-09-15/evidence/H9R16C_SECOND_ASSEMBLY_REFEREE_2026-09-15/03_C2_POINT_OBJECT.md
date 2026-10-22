# 03 — C2 (the point object `Φ̄_r^mod ∈ 𝒫_r^♮`)  [SECOND referee, independent]

**Verdict: CONFIRMED_WITH_NARROWER_HYPOTHESIS.** Well-definedness and `⋆`-invariance are PROVED
(re-derived here from the printed laws, not taken from Lane 4). The "coincides with the frozen
functional" clause holds only under Lane 4 `01` §6's reading of an unstated push-down. The final
**orientation clause is FALSE**, harmlessly: `A_r` is self-adjoint, so the two orientations of `Γ_A`
give the *same* functional.

## §1. Well-definedness on the quotient

`Γ(b) = (pd^t)^t ∘ ρ_r(t_2)A_rt_3 ∘ pd^t`, a correspondence `X_2 ⇢ X_3` at common level whose action
on `H^1` is `(pd^t)^* ∘ ρ_r(t_2)A_rt_3 ∘ pd^t_*`; by the projection formula its bilinear form is
`(y_2,y_3) ↦ ⟨pd^t_*y_2, ρ_r(t_2)A_rt_3 pd^t_*y_3⟩_{N_gp^r}` — C3's `Contr_r^{A_r}(b)` exactly.
Replacing `(t_2u',t_3)` by `(t_2,u't_3)`:
`ρ_r(t_2u')A_rt_3 = ρ_r(t_2)ρ_r(u')A_rt_3 = ρ_r(t_2)A_ru't_3` (commutativity + transport, C1 §2).
So `Γ` and hence `Φ̄_r^mod` factor through `B^bal_r ≅ R_r`, and by C1 the map is
`R_r → Ĵ^{(1)}_r(F'_r)^{ord}`, `t ↦ pd^{t_f}_*Π_{Γ(t),*}Δ^ord_r[e]` with `Γ(t) = (pd^t)^tA_rt·pd^t`.
Ordinarity of the value: `Δ^ord_r` already carries `e'^{⊗3}_ord`, and `e'_ord` on factor 1 commutes
with `Π_*` and with `pd^{t_f}_*`.

## §2. `⋆`-invariance, re-derived

Inputs used, all printed: (a) `W^σ = ⟨z_σ⟩∘W = W∘⟨z_σ⟩^{-1}` (Ohta 1999 (4.2.4)/Hida p.15; B2's
standing input); (b) `T'_ℓ, U'_p, ⟨d⟩, e'_ord, Π, pd^t, pd^{t_f}` are defined over `Q`;
(c) BCPV (4.1) `⟨a_1,a_2,a_3⟩Δ_r[d] = Δ_r[a_2a_3d_1,a_1a_3d_2,a_1a_2d_3]` (l.1218) and
`σ_mΔ_r^{ord}[d] = Δ_r^{ord}[m^{-1}d]` (l.1257); (d) the post-transport balance (C1).

**A step that must not be skipped.** The diamond action on `Δ^{ord}` is the `W`-conjugate of the one
on `Δ`: since `⟨a⟩W = W⟨a⟩^{-1}`,

    ⟨a,a,a⟩ Δ_r^{ord}[d] = (e'W)^{⊗3}⟨a^{-1},a^{-1},a^{-1}⟩Δ_r[d] = Δ_r^{ord}[a^{-2}d] .

Reading (c) through this gives `σ_mΔ^{ord}_r[d] = ⟨m^{1/2},m^{1/2},m^{1/2}⟩Δ^{ord}_r[d]`
(exponent **+1/2**). Using the naive `(4.1)` on `Δ^{ord}` instead yields `−1/2` and the `p`-part
does **not** cancel below. Lane 4 `03` §2's `+1/2` is the correct one.

**p-part** (`σ = σ_m`, `m ∈ 1+pZ_p`, `n_σ = 1`). `A_r^σ = (W^σ)^{-1}(U'_p)^r = A_r∘⟨m⟩^{-1}`
(factor 3). Contributions to `σ∘Φ̄^mod_r`: factor 1 `⟨m⟩^{1/2}` → output; factor 2 `⟨m⟩^{1/2}` →
carrier **unchanged** (`ρ_r(⟨d⟩) = ⟨d⟩^{-1}` and `⟨d⟩^{-1}A_r = A_r⟨d⟩`, so a factor-2 diamond lands
on the carrier as itself — this is the post-transport balance); factor 3 `⟨m⟩^{1/2}` → carrier;
`A_r^σ` → carrier `⟨m⟩^{-1}`. Carrier total `⟨m⟩^{1/2+1/2-1} = 1`:

    σ ∘ Φ̄^mod_r = ⟨m_σ⟩^{1/2}_{(1)} ∘ Φ̄^mod_r        (pure factor-1 dagger twist).

**Tame part** (`χ_cyc(σ) ≡ n (N)`, trivial `p`-part). `σ` fixes `Δ_r[e]` (defined over `Q(μ_{p^r})`),
and `σ(W_{Np^r})^{⊗3} = ⟨n,n,n⟩W^{⊗3}`, so `σΔ^{ord}_r[e] = ⟨n,n,n⟩Δ^{ord}_r[e] = Δ^{ord}_r[e]`: the
**diagonal tame** diamond acts trivially on `Δ^{ord}` (it preserves `X_{123}` and the `p^r`-Weil
conditions). At native level `A_r^σ = A_r⟨n⟩^{-1}`, so the only twist is `⟨n⟩^{-1}` on the carrier;
rewriting it by the same diagonal relation `⟨n⟩^{-1}_{(3)}Δ^{ord} = ⟨n⟩_{(1)}⟨n⟩_{(2)}Δ^{ord}`:

    σ ∘ Φ̄^mod_r = ⟨n_σ⟩_{(1)} ∘ Φ̄^mod_r ∘ R(⟨n_σ⟩) .

(The two forms `Φ̄∘R(⟨n⟩^{-1})` and `⟨n⟩_{(1)}Φ̄∘R(⟨n⟩)` agree; equivalently
`Φ̄ = ⟨n⟩_{(1)}Φ̄∘R(⟨n⟩^2)` — B2's "Reconciliation". This is an internal symmetry of `Φ̄^mod`,
not an extra hypothesis.)

Combining: `σ∘Φ̄^mod_r = ⟨m_σ⟩^{1/2}_{(1)}⟨n_σ⟩_{(1)}∘Φ̄^mod_r∘R(⟨n_σ⟩)`, i.e. exactly
`σ⋆Φ̄^mod_r = Φ̄^mod_r` for the `⋆`-action printed in C2/B5. **`Φ̄^mod_r ∈ 𝒫^♮_r`: PROVED.**
`⋆` is a genuine action (diamonds are over `Q`, commute with `σ` and with `R`).

Sign caveat, carried: the exponents depend on (i) the sign in `W^σ = ⟨z⟩W` and (ii) the transpose
convention for a factor-1 diamond crossing `Π_Z`. Flipping either flips exponents but not the two
structural conclusions (p-part cancels on the carrier; a tame `⟨n_σ⟩` survives there). The tame twist
is non-trivial on the `g`-branch iff `ε_g^{(t)} ≠ 1` — the Castella–Hsieh case.

## §3. "Coincides with the frozen H9R16-A/B functional": NOT literally checkable

The frozen formula is `Φ_r^mod(t_2,t_3) := Π_{Z,*}((1⊗t_2⊗A_rt_3)Δ_r^{ord})` with `Z = X_{23}` the
**plain** diagonal. Two mismatches with C2's `Φ̄^mod_r`:
1. `Δ^{ord}_r` lives at common level `Np^r` while `A_r = W_{N_gp^r}^{-1}(U'_p)^r` is an operator at
   native level `N_gp^r`. The bare formula is therefore not type-correct until a tame push-down is
   inserted; the frozen text does not state one (Lane 4 `01` §6 supplies it as "factorwise as in BCPV
   Def 4.13"; the coordinator erratum records that BCPV's tame map is written `ϖ_{1,*}` with no
   printed definition). C2's `Γ(b)` is the **unique** reading that makes the frozen formula typed.
2. The frozen `Φ^mod_r` takes values in `J` at common level; C2's `Φ̄^mod_r` adds `pd^{t_f}_*` on
   factor 1 to land in `Ĵ^{(1)}_r`. Again this is Lane 4 `01` §6's factorwise reading.

So the coincidence is **PROVED under the reading "factorwise tame push-down as in BCPV Def 4.13,
the same `pd` at every level"**, and is `NOT_PRINTED` against the bare frozen formula. Given the
reading, the identification `Π_{Z,*}((1⊗t_2⊗A_rt_3)Δ) = Π_{Γ,*}Δ` with `Γ = Γ_{t_2}^t∘Γ_A∘Γ_{t_3}`
is the standard move of operators into the correspondence (Lane 5 `05` §2).

## §4. The orientation clause is FALSE (harmlessly)

C2: "the opposite orientation (`A_r^t = (U_p)^rW`) is **not** the frozen functional."

In weight 2 on `X_1(N_gp^r)`: `W^2 = id` (so `W^t = W_* = W^* = W`) and `W U'_p W = U_p`
(BCPV (1.8)–(1.9)/Ohta 1.5.4). Hence

    A_r^t = ((U'_p)^r)^t W^t = (U_p)^r W = (W U'_p W)^r W = W (U'_p)^r W·W = W(U'_p)^r = A_r .

**`A_r` is self-adjoint**, the modified pairing `(y_2,y_3) ↦ ⟨y_2, A_ry_3⟩` is symmetric, and the two
orientations of `Γ_A` induce the *same* bilinear form. Numerically confirmed
(`_verify/transport_check.py` (T5),(T5'); `(N_g,p,r) ∈ {(5,3,1),(5,3,2),(7,2,1),(3,5,1)}`,
ℓ ∈ {1000003, 999983}, all PASS).

Consequence: the orientation caveat of A6 (Lane 5 `07` item 5) and pressure point P5 are **vacuous in
weight 2**; the assembly is insensitive to the orientation choice — strictly safer than C2 asserts.
The clause as printed is FALSE and should be deleted, not repaired. It is used nowhere downstream.

## §5. Status

| sub-claim | status |
|---|---|
| `Φ̄^mod_r` well defined on `B^bal_r` | PROVED |
| `Φ̄^mod_r ∈ 𝒫^♮_r` (`⋆`-invariance, both parts) | PROVED (§2), independently re-derived |
| coincidence with the frozen functional | PROVED under Lane 4 `01` §6's reading; `NOT_PRINTED` against the bare frozen formula |
| orientation clause ("opposite orientation is not the frozen functional") | **FALSE** — `A_r^t = A_r` (§4); harmless |

**C2 = CONFIRMED_WITH_NARROWER_HYPOTHESIS** (§3's reading), with the §4 clause struck.
