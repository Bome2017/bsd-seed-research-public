# 07 — C6 (no rank factor)  [SECOND referee, independent]

**Verdict: CONFIRMED.** Exhaustive audit of every place a `p`-power could enter the assembly as I
derived it in files 02–06; and the counterfactual about `μ_r` is correct once its reading is pinned.

## §1. Exhaustive `p`-power audit of the assembly

| candidate | where it lives | used in the assembly? |
|---|---|---|
| `deg ϖ_1 = p^2`, i.e. `ϖ_{1,*}ϖ_1^* = p^2` | push-after-pull | **No.** C4 uses `ϖ_{1,*}` alone on factor 1; the only `ϖ_1^*` is inside A1 (MPC), which is pull-after-**push** |
| `ϖ_{2,*}ϖ_1^* = pU_p`, `ϖ_{1,*}ϖ_2^* = pU'_p`, `ϖ_{2,*}U'_p = pϖ_{1,*}` (A2) | the other composites | **No.** None occurs |
| `|ker(G_{r+1}→G_r)| = p^3` (triple) | type-A invariants, frozen `s_r⊗ϖ_*` (B3, Lane 4 `03` §1) | **No.** No triple-`G_r` packaging is used; the assembly contracts the **fixed-index** class `Δ^ét_r[e]` |
| BCPV (4.9)'s printed `1/p` (Lane 4: should be `p^{-3}`) | `τ^ét` written from (4.9) | **No** — prohibited by charter and not used; Lemma (L) of `05` is derived from MPC + Cor 4.11 |
| `Cor∘res = p` per level (Lane 4 `03` §4) | corestriction on the field side | **No.** C3 uses descent (`res` injective, `H^0 = 0`), C4c uses evaluationwise Kummer injectivity over `F'_{r+1}`. Corestriction never appears |
| `p^3/(p−1)^3` (BCPV Def, l.1397) | the **symmetrized** `Δ^ét_r` | **No.** The assembly uses `Δ^ét_r[e]` at a fixed Teichmüller index; 01 explicitly does not claim `Δ^ét_r[e] = Δ^ét_r` |
| constant in Cor 4.11(i) | level step of the class | none exists |
| `d_r` in MPC (A1) | level step of the modified pairing | `= 1` (input) |
| `N_{r+1,r}` | carrier | kept as a **group-ring element**; `N^2 = pN`, `π_r(N) = p·1` |

**The only `p` in the assembly is `π_r(N_{r+1,r}) = p·1`,** and it materializes only if one projects the
carrier to level `r` — which C4 deliberately does not do. Confirmed.

The `|G_r| = p^{3(r−1)}` of the type-A receptacle (B3) cannot enter for a structural reason,
already established in C1: after the contraction the carrier is `B^bal_r ≅ R_r`, a rank-one free
module over the **native-level primed ordinary Hecke algebra**, and the surviving dagger group is the
factor-1 quotient (Lane 4 `03` §1). There is no induced/permutation lattice anywhere in
`Hom_{Z_p}(B^bal_r, T_pJ^{(1),ord}_r)`.

## §2. The `μ_r` counterfactual

`μ_r` is **not used**: files 02–06 nowhere convert between a packaged and an unpackaged class. That
alone settles C6's operative clause.

The counterfactual value is convention-sensitive, and the conventions can be pinned from BCPV:

1. BCPV (4.7), l.1318: `Δ_r^ét[[a,b,c]] := Σ_{⟨d_1,d_2,d_3⟩∈G_r} Δ_r^ét[d_2d_3a, d_1d_3b, d_1d_2c]⟨d_1,d_2,d_3⟩`.
   By (4.1) (l.1218) the printed index is exactly `⟨d_1,d_2,d_3⟩Δ_r[a,b,c]`, **on `Δ`**.
2. Since `⟨a⟩W = W⟨a⟩^{-1}`, the same reindexing on `Δ^{ord} = (e'W)^{⊗3}Δ` is the **inverse** diamond:
   `Δ^{ord}_r[g·e] = ⟨g⟩^{-1}Δ^{ord}_r[e]` (the inversion already forced in C2 §2).
3. Hence, with the post-transport balance (a factor-2 diamond lands on the carrier as itself),
   `P_r[g·e] = ⟨d_1⟩^{-1}_{(1)}·Φ̄^mod_r( ⟨d_2d_3⟩^{-1}·b )`.

Now apply `μ_r : g⊗v ↦ ⟨g⟩v` in Lane 4 `03` §1's form (the type-A → type-B surjection onto
`V_r = J_r`, i.e. `⟨g⟩` acting by the factor-1 diamond `⟨d_1⟩`): the factor-1 twists cancel and

    μ_r( Σ_{g∈G_r} P_r[g·e] ⊗ g )  =  Φ̄^mod_r ∘ ( 1 ⊗ Σ_{g∈G_r} ⟨d_2d_3⟩^{-1} ) ,

**exactly C6's printed formula.** On a branch where the carrier diamonds act by a character `ψ`,
`Σ_{(d_1,d_2,d_3)∈G_r} ψ(d_2d_3)^{-1} = |G_r|` if `ψ` is trivial and `0` otherwise: `|G_r|`-or-`0`,
i.e. `|G_r|` times a projector, **not** a rescaling. Confirmed.

Recorded alternative (does not change the conclusion): under Lane 2 `01` T4's reading, where `⟨g⟩`
acts on `V_r = Hom_Z(M_r,J_r)` through all three components (`⟨d_1⟩` on `J_r`, `⟨d_2⟩,⟨d_3⟩` on
`M_r`), every twist cancels and one gets `|G_r|·Φ̄^mod_r` — a uniform rescaling by `|G_r| = p^{3(r−1)}`.
Either way a full `|G_r|` appears and `μ_r` is not a harmless identification; C6's headline holds
under both readings, and its printed formula holds under the Lane 4 `03` §1 reading.

## §3. BCPV's own conversion

Verified verbatim at BCPV.tex **l.1331–1332**:
`ψ(•) = Σ_{g∈G_r}ψ_g(•)g ↦ ψ_e(•)` and `Σ_{g∈G_r}φ(g^{-1}•)g ↦| φ(•)`. This is the
**identity-coefficient** map `G`, not a multiplication map. ✔ C6's citation is exact.

## §4. Status

| sub-claim | status |
|---|---|
| no `|G_r|`, `p^3`, `p^{±1}`, `p^{±2}` in the assembly | PROVED (§1, exhaustive) |
| the only `p` is `π_r(N_{r+1,r}) = p·1` | PROVED |
| `μ_r` is not used | PROVED by inspection of 02–06 |
| the `μ_r` counterfactual formula `Φ^mod∘(1⊗Σ_g⟨d_2d_3⟩^{-1})`, `|G_r|`-or-`0` | PROVED under the Lane 4 `03` §1 reading of `μ_r`; alternative reading gives `|G_r|·Φ^mod` (§2) |
| "BCPV's own conversion is the identity-coefficient map `G`" (l.1331–1332) | CONFIRMED verbatim |

**C6 = CONFIRMED.**
