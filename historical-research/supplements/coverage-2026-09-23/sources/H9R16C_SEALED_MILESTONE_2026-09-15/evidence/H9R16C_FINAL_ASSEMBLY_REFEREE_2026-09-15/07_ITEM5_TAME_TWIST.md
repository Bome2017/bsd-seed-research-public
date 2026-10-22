# 07 — ITEM 5: is the tame ε_g^{-1} twist preserved by every map in the tower?

Continues 03–06. The twist in question is the one B2 proves survives descent: on the `g`-branch quotient of
the carrier, `Gal(F'_r/K_0)` acts through `ε_g^{(t)}(n_σ)^{±1}`; it is BCPV's `g^c = g⊗ε_g^{-1}` third
factor ((1.7) = `eqn_2023_09_29_1518`, BCPV.tex l.525–528) transported to the point side, where the carrier
has no Galois action of its own and the twist must be written into the module (Lane 4 `03` §2).

## §1. The twist, stated as part of the receptacle

From B5 and 03 §5, for `σ ∈ Gal(F'_r/K_0)`, `n_σ = χ_cyc(σ) mod N` (acting on the native carrier through
`n_σ mod N_g`), `m_σ = ⟨χ_cyc(σ)⟩ ∈ 1+pZ_p`:

    (σ⋆Φ)(b) = ⟨m_σ⟩^{-1/2}_{(1)} ⟨n_σ⟩^{-1}_{(1)} · σ( Φ( R(⟨n_σ⟩)^{-1} b ) ) .

The tame datum is the pair (`⟨n_σ⟩^{-1}` on factor 1, `R(⟨n_σ⟩)` on the carrier). Deleting either half
breaks the invariance: `Φ̄^mod_r` is `K_0`-rational **only** for this twisted action, and is otherwise only
`K_0(μ_{N_g})`-rational (B2; Lane 2 `03.2.3` H1). Item 5 asks whether the four maps of the tower relation
preserve it.

## §2. The four maps

Throughout: all diamonds `⟨d⟩` are `Q`-rational automorphisms, hence commute with the `σ`-action; `U'_p`,
`e'_ord`, `ϖ_1`, `pd^t`, `pd^{t_f}` are `Q`-rational; `N_{r+1,r}` and `U'_p` are central in `𝕋'^{ord}`.

**(a) `τ_r^MW = ϖ^{(1)}_{1,*}∘(−)`.** `ϖ^{(1)}_{1,*}: J^{(1)}_{r+1} → J^{(1)}_r` is `Q`-rational, so it
commutes with `σ`; and `ϖ_{1,*}⟨d⟩_{N_fp^{r+1}} = ⟨d mod N_fp^r⟩ϖ_{1,*}` (DR22 (1.13)–(1.14)). Its tame
part is the identity on `(Z/N_f)^×`, so `ϖ_{1,*}⟨n⟩_{(1)} = ⟨n⟩_{(1)}ϖ_{1,*}` **with the same `n`**. Also
`pr_r∘c_{r+1}^{1/2} = c_r^{1/2}` on the `p`-part (B1/T0). Hence
`σ⋆(τ_r^MW x) = τ_r^MW(σ⋆x)`: ⋆-equivariant. (This is Lane 4's L1 made explicit for this map.)

**(b) `1 ⊗ N_{r+1,r}`.** The kernel elements satisfy `d ≡ 1 (mod N_gp^r)`, in particular `d ≡ 1 (mod N_g)`:
`N_{r+1,r}` is a sum of **purely `p`-power-level** diamonds and has **trivial tame part**. Therefore it
commutes with `R(⟨n⟩)` for every tame `n`, and `(1⊗N)` is ⋆-equivariant. It also preserves the balance
relation (`N` central in `𝕋'`), so it is a well-defined endomorphism of `B^bal_{r+1} ≅ R_{r+1}` (04 Lemma C:
multiplication by `N_{r+1,r}`). **The tame twist is untouched by the norm element** — this is the precise
sense in which the `ε_g^{-1}` carrier twist and the `p`-direction norm live in complementary directions.

**(c) `π_r^*` (precomposition with `res^bal_{r+1,r}`).** `π_r` sends `⟨d⟩_{N_gp^{r+1}} ↦ ⟨d mod N_gp^r⟩`,
so `π_r(⟨n⟩) = ⟨n⟩` for tame `n` (the tame part of the level is the same at both levels). Hence
`res^bal∘R(⟨n⟩) = R(⟨n⟩)∘res^bal`, and `π_r^*` is ⋆-equivariant and injective (`res^bal` is surjective:
`R_{r+1} ↠ R_r`). So an equality of ⋆-invariant elements may be tested after `π_r^*`.

**(d) The normalizations `(U'_p)^{-s}_{(1)}` and `(U'_p)^{-2s}_{carrier}`.** `U'_p` is `Q`-rational and
commutes with all diamonds; it is invertible on `e'_ord`-parts (B6 H11). So `Q_s` has the same ⋆-law as
`Φ̄^mod_s`, and `Q_s ∈ 𝒫_s^♮`.

**(e) The tame push-downs.** `pd^t_*⟨d⟩_{Np^s} = ⟨d mod N_gp^s⟩pd^t_*` for both indices — verified
numerically, 05 §2, checks `(C-D)`, `(C-D')`. So the twist that appears on the native carrier is the image
of the common-level tame diamond, i.e. exactly `ε_g` evaluated on `n mod N_g`: the *same* character for
either choice of push-down. The choice of 05 §1 therefore does not move the twist.

## §3. Both sides of the tower relation carry the same twist

By §2(a)–(d), `τ_r^MW(Q_{r+1})∘(1⊗N_{r+1,r})` and `π_r^*Q_r` are both ⋆-invariant elements of
`Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})`, i.e. both lie in the common receptacle of B5's `(T♮_r)`
with the **same** tame twist on the carrier's third slot and the **same** factor-1 dagger. The identity of
05 §3.5 is therefore an identity inside a single ⋆-module — not a comparison across two different twists,
which is the failure mode Lane 3 recorded as the way E′(a) could be a TYPE_MISMATCH. It is not one here.

## §4. Hostile checks

| # | attack | finding |
|---|---|---|
| T5.1 | Does `N_{r+1,r}` carry a tame diamond that would rotate `ε_g`? | No: `d ≡ 1 mod N_g` (§2b). If one mistakenly used the **common**-level norm element `Σ_{d≡1 mod Np^r}⟨d⟩`, it would still have trivial tame part, but it would be the wrong operator for the native pairing; 05 §3.1 uses the native one, matching A1 at tame level `M = N_g`. PASS |
| T5.2 | Does the `p`-part half-twist leak into the carrier across the level step? | No: the `p`-part cancels on the carrier at **each** level separately (B2/B3), and `pr_r∘c^{1/2}_{r+1} = c^{1/2}_r` makes the surviving factor-1 half-twists compatible. PASS |
| T5.3 | Is `ε_g^{(t)} ≠ 1` (the Castella–Hsieh case) a problem for the relation? | No. The twist enters only through `R(⟨n⟩)`, which commutes with everything used in 05 §3. It **is** essential to the receptacle: with a dagger-only receptacle the finite point is not `K_0`-rational (Lane 4 `03` §2, L4-T3). PASS |
| T5.4 | Does the `g^c` (dual) direction reverse the transition? | No: `A_r`-transport makes `ι_r = id` (§C), the carrier moves by `res^bal` on both auxiliary slots, and the output factor stays covariant (Albanese). Lane 4 `03` §8's caution is respected, and 05 §3.1's transposition `U_p ↔ U'_p` is the only variance step, made explicit by `U_pA_r = A_rU'_p`. PASS |
| T5.5 | Could the tame twist be absorbed by enlarging the base field? | No: `Q(μ_N)∩Q(μ_{p^∞}) = Q`, so no `p`-cyclotomic base absorbs it (Lane 4 `03` §2). It must stay in the module, as it does. PASS |

## §5. Verdict for item 5

**ITEM 5 = PROVED.** The tame `ε_g^{-1}` twist is preserved by `ϖ^{(1)}_{1,*}`, by `π_r`/`res^bal`, by
`1⊗N_{r+1,r}` (whose elements are trivial at the tame level), by both tame push-downs, and by the `U'_p`
normalizations; both sides of the tower relation live in one and the same ⋆-module.

ITEM5_STATUS = PROVED (twist preserved by all four maps and by the push-down choice)
