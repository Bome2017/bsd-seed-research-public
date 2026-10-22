# 08 — The inverse-limit point module created, and the exact next gate

Items 1–5 are established (03–07), so H9R16-C closes. This file states (§1) the exact object the closure
creates, (§2) how the group-ring element `N_{r+1,r}` is absorbed (P8), and (§3) the exact statement of
`G_BIG_KUMMER_TRACE`, with (§4) the normalization dictionary and (§5) the items carried into it.

## §1. The inverse-limit point module

For `r ≥ 1` (native tame level `N_g` on the carrier, `N_f` on the output; `F'_r = Q(μ_{Np^r})`, `K_0 = Q(μ_p)`):

    B^bal_r ≅ R_r := e'_ord𝕋'_{N_gp^r} ⊗ Z_p        (04 Lemma C; finite free over Z_p)
    𝒫^♮_r  = Hom_{Z_p}( B^bal_r , Ĵ^{(1)}_r(F'_r)^{ord} )^{Gal(F'_r/K_0), ⋆}     (B5; 03 §5)
    Q_r    = (U'_p)^{-r}_{(1)} ∘ Φ̄^mod_r ∘ (U'_p)^{-2r}_{carrier} ∈ 𝒫^♮_r        (B6 T3; 03, 05 §3.5)
    τ_r^MW(x) = ϖ^{(1)}_{1,*} ∘ x ,   π_r^*(y) = y ∘ res^bal_{r+1,r} ,   N_{r+1,r} = Σ_{d ≡ 1 (N_gp^r)} ⟨d⟩ .

**Definition (the object created by H9R16-C).**

    𝒫^♮_∞ := { (Q_r)_{r≥1} ∈ ∏_{r≥1} 𝒫^♮_r  :  τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r}) = π_r^*(Q_r)  for all r ≥ 1 },

the limit being taken inside the common receptacles
`Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})^⋆`, into which `𝒫^♮_r` embeds by the injective `π_r^*`
(03 §5, 07 §2c). Structure: `𝒫^♮_∞` is a `Z_p`-module, and the diamond/Hecke actions on the carriers are
compatible under `π_r`, so it is a module over `𝕋'_∞(N_g) := lim_r R_r` — Hida's big ordinary Hecke algebra
of tame level `N_g` — with the tame part acting through the `ε_g^{-1}`-twisted `⋆`-structure (07).

**Theorem (H9R16-C, as closed here).** The system `𝒬_∞ := (Q_r)_{r≥1}` built in 03–05 from BCPV's own cycles
lies in `𝒫^♮_∞`: each `Q_r ∈ 𝒫^♮_r` (03, 07) and the compatibility holds integrally with constant `1`
(05 §3.5), for either tame push-down used uniformly (05 §4).

## §2. How `N_{r+1,r}` is absorbed (P8), and why the naive limit is the wrong one

`N_{r+1,r}` is an element of the finite group ring, not a scalar (A2). Three readings, only the first correct:

1. **Integral, as written.** The transition is the *pair* `(τ_r^MW, 1⊗N_{r+1,r})` landing in
   `Hom(B^bal_{r+1}, Ĵ^{(1)}_r)^⋆`; `N_{r+1,r}` acts on the carrier (multiplication by `N_{r+1,r}` in
   `R_{r+1}`, 04 Lemma C), never on the point. No division occurs; `𝒫^♮_∞` is a `Z_p`-lattice-type object.
2. **After the group-ring projection.** `π_r(N_{r+1,r}) = p·1` (A2), so on carrier-coinvariants the relation
   reads `ϖ^{(1)}_{1,*}Q_{r+1} = p·Q_r`. **The naive inverse limit along `ϖ_{1,*}` alone is therefore not the
   object**: it would require `Q_r ∈ p^{r}Ĵ`, and inverting `p` would change the normalization of every term.
   This is the same trap L4-T2 recorded in type A (with `p^3`); here it is `p^1` and it is avoided, not paid.
3. **Λ-adically.** `(N_{r+1,r})_r` is the standard norm-compatible system of `Λ(G_∞)`-theory (DR22
   `lemma:compatibility-bis`, DR22.tex l.2472–2499, where the same element appears as `(μ^3)^*(μ^3)_*` and
   the transition is `p_{r+1,r}`), which is why `𝒫^♮_∞` is `𝕋'_∞(N_g)`-linear and not merely `Z_p`-linear.

## §3. `G_BIG_KUMMER_TRACE` — exact statement of the next gate

Write `Kum^♮_r : 𝒫^♮_r ↪ H^1(K_0, T^♮_r)` (04 §4), `Θ_r := Contr_r^{A_r}(Δ_r^ét[e]) = Kum^♮_r(Q_r)`
up to the normalization of `Q_r` (04 Theorem 2 with the `(U'_p)^{-r}, (U'_p)^{-2r}` of §1), and let
`Θ_∞ := (Θ_r)_r` be the corresponding system in `lim_r H^1(K_0, T^♮_r)` (limit along
`τ_r^et ∘ (1⊗N_{r+1,r})` vs `π_r^*`, i.e. the étale image of §1's limit).

> **G_BIG_KUMMER_TRACE.** Let `f`, `g` be as in BCPV §1.1.5 (`ε_f = 1`, `ε_g = ε_g^{(t)}`, `N_f` square-free,
> (Dist), (NA), the root-number hypotheses), `h = g^c`. Prove that the inverse-limit Kummer class of the
> point system `𝒬_∞ ∈ 𝒫^♮_∞`,
>
>     Kum_∞(𝒬_∞) := ( Kum^♮_r(Q_r) )_r  ∈  lim_r H^1(K_0, T^♮_r) ,
>
> is, under the branch identification of the carrier (`𝕋'_∞(N_g) → R_g`) and the Künneth/trace maps of BCPV,
> the restriction to `K_0` of BCPV's **big trace class**
>
>     Δ^{tr}(f ⊗ ad(g)) := (id ⊗ tr)( Δ^ét(f ⊗ ad(g)) )  ∈ H^1(Q, T_f^†) ,
>     T_f^† = T_f ⊗ 𝛘_f^{-1/2}  (BCPV.tex l.469–473),  Δ^ét(f⊗ad(g)) as in `defn_2023_11_15_1209` (l.1462–1466),
>
> **with the following normalization dictionary made explicit and verified** (§4), and **before any
> weight-one coefficient specialization** — i.e. as an identity of `R_f ⊗̂ R_g`-adic objects, not of
> specializations.

Equivalently, in one line: *the big Kummer class of the inverse-limit contracted Chow–Heegner point equals
BCPV's big diagonal class after contraction by the modified pairing and the `ad(g)`-trace.*

## §4. The normalization dictionary that the gate must verify (P7, made exact)

| side | normalization | anchor |
|---|---|---|
| point tower (here) | `(U'_p)^{-r}` on factor 1, `(U'_p)^{-2r}` on the carrier; `N_{r+1,r}` (not `p`) in the transition | 05 §3.5, §6 |
| cycle tower (BCPV) | `Δ^ét_∞ = {(U'^{⊗3}_p)^{-r}Δ^ét_r}_r` | `definition_big_Heegner_main`, l.1437–1441 |
| branch push-down | `ϖ_{1,*}⊗ϖ_{1,*}⊗ϖ_{1,*}` to `(N_f,N_g,N_g)`, then `T_{fgh}` | `definition_big_diagonal_Hida_families`, l.1447–1459 (tame index convention: 05 §1) |
| specialization | `res Δ^ét(f⊗ad g)\|_{(κ,λ)} = a_p(f)^{-r}a_p(g)^{-2r}Δ^ét_r(κ,λ)` | `lemma_2023_11_14_1442`, l.1489–1495 |
| modified vs Poincaré trace | `Δ^{tr}_r(κ,λ) = a_p(g)^r λ_{N_gp^r}(g)^{-1} Δ^{(P)}_r(κ,λ)` | `eqn_2024_02_09_0654`, l.1726–1728; pairing `eqn_2024_02_08_1848`, l.1560–1562 |
| Λ-adic pairing target | `⟨x, W_{N_hp^r}^{-1}(U'_p)^r y⟩ ∈ Z_p[Δ_{N_hp^r}]⊗χ_cyc^{k+1}`, `k = 0` | (1.6) `eqn_2023_09_29_1444`, l.513–518 |

The matching of `(U'_p)^{-r}/(U'_p)^{-2r}` (point side) with `a_p(f)^{-r}a_p(g)^{-2r}` (BCPV side) is exactly
the finite-level content of 05 §6 and is the first thing the gate should check; the
`a_p(g)^rλ_{N_gp^r}(g)^{-1}` factor is the difference between the modified (`Δ^{tr}`) and plain (`Δ^{(P)}`)
trace classes and belongs to the gate, not to H9R16-C.

## §5. What is carried into the gate (open, recorded here, none of it used above)

1. **Tame push-down scalar** (05 §5): with `pr^t_1` vs `pr^t_2` the constructed point differs by the tame
   degeneracy interchange, a Hecke scalar at `ℓ | t` on `h`-isotypic quotients. Immaterial for H9R16-C
   (05 §4); must be fixed before any statement naming `λ_{N_gp^r}(g)` or `a_p(g)^{±r}`.
2. **(AJ-corr) citation (R1)** (04 §5 D2.7): the numbered statement for étale Abel–Jacobi functoriality
   under correspondences is still unpinned in the packet. Frozen as `PROVED_FORMAL` by the operator.
3. **`H_π`** (B6): the ring maps `π_r` with `ϖ_{1,*}t = π_r(t)ϖ_{1,*}`, used as part of the statement of the
   relation (the carrier transition); standard Hida theory, not proved in any lane.
4. **Downstream, deliberately untouched** (charter §2.2): inverse-limit identification with BCPV's module,
   density, H9R15 localization, `f`-branch extraction, weight-one specialization. The gate above is stated
   *before* all of these, as required.

## §6. Status

H9R16C_CLOSED. Object created: `𝒫^♮_∞` and the system `𝒬_∞ ∈ 𝒫^♮_∞` of §1. Next gate: §3.
