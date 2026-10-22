# 08 — C7 (the tame `ε_g^{-1}` / `g^c` twist is preserved)  [SECOND referee, independent]

**Verdict: CONFIRMED.** Each of the five preservation statements is checked separately below, and the
"one and the same `⋆`-module" clause is verified for both sides of C4 including the Galois steps
`Gal(F'_{r+1}/F'_r)` that the level mismatch creates.

## §1. Where the twist actually sits

BCPV put the twist in the Galois module: factor 3 is `h^c = h ⊗ ε_h^{-1}` ((1.7), p.5). On the point
side there is **no** Galois action on the Hecke-coefficient carrier, so the same twist has to appear
as the tame diamond in the `⋆`-action (Lane 4 `03` §2). Concretely, for
`σ ∈ Gal(F'_s/K_0)`, `n_σ := χ_cyc(σ) mod N`, `m_σ := ⟨χ_cyc(σ)⟩ ∈ 1+pZ_p`:

    (σ⋆Φ)(b) = ⟨m_σ⟩^{-1/2}_{(1)} ⟨n_σ⟩^{-1}_{(1)} · σ( Φ( R(⟨n_σ⟩)^{-1} b ) ) ,

and on the `g`-branch quotient of `B^bal_s` the carrier diamond `R(⟨n⟩)` acts by `ε_g^{(t)}(n)`.
**That factor is the tame `ε_g^{-1}` twist.** "Preserved" therefore means: every arrow of the tower is
`⋆`-equivariant for these actions at the two levels. That is what §2–§6 check.

## §2. `ϖ^{(1)}_{1,*}` (factor 1)

`ϖ_{1,*}` is `Q`-rational, so it commutes with `σ`; `ϖ_{1,*}⟨d⟩_{N_fp^{r+1}} = ⟨d mod N_fp^r⟩ϖ_{1,*}`;
`ϖ_{1,*}e'_{r+1} = e'_rϖ_{1,*}` (A2: `ϖ_{1,*}U'_p = U'_pϖ_{1,*}`). It does not touch the carrier at all.
Hence for `σ ∈ Gal(F'_{r+1}/K_0)`:

    (σ⋆(ϖ_{1,*}∘Q_{r+1}))(b) = ϖ_{1,*}( ⟨m_σ⟩^{-1/2}_{(1),r+1}⟨n_σ⟩^{-1}_{(1),r+1} σ(Q_{r+1}(R(⟨n_σ⟩)^{-1}b)) )
                             = ϖ_{1,*}( Q_{r+1}(b) ) ,

using `pr_r∘c^{1/2}_{r+1} = c^{1/2}_r` (the square root is taken in `1+pZ_p`, so reduction commutes
with it). **The tame part `⟨n_σ⟩` is carried unchanged from level `r+1` to level `r`.** ✓

## §3. `π_r` / `res^bal`

`π_r(⟨d⟩) = ⟨d mod N_gp^r⟩`; in particular `π_r(⟨n⟩) = ⟨n⟩` for tame `n ∈ (Z/N_g)^×`, so
`res^bal_{r+1,r}∘R_{r+1}(⟨n⟩) = R_r(⟨n⟩)∘res^bal_{r+1,r}`. Therefore

    (σ⋆(π_r^*Q_r))(b) = ⟨m_σ⟩^{-1/2}_{(1)}⟨n_σ⟩^{-1}_{(1)}σ( Q_r( R_r(⟨n_σ⟩)^{-1} res^bal(b) ) )
                      = (σ⋆Q_r)(res^bal b) = Q_r(res^bal b) = (π_r^*Q_r)(b)

for `σ ∈ Gal(F'_r/K_0)`. **The tame carrier twist passes through the carrier map unchanged.** ✓

## §4. `1 ⊗ N_{r+1,r}`

`N_{r+1,r} = Σ_{d ≡ 1 (N_gp^r)}⟨d⟩`. Every such `d` satisfies `d ≡ 1 (mod N_g)`, so each `⟨d⟩` has
**trivial tame component**: `N_{r+1,r}` lies in the `p`-part of the diamond group ring, and on the
`g`-branch every term has `ε_g(d) = 1`. Moreover diamonds commute, so
`(1⊗N)∘R(⟨n⟩) = R(⟨n⟩)∘(1⊗N)`; hence `(1⊗N)` is `⋆`-equivariant and does not move the twist. ✓
(C7's parenthetical is exactly right, and it is the reason the norm element can be inserted on the
carrier without disturbing the nebentype bookkeeping.)

## §5. Both tame push-downs

`pr^t_1` and `pr^t_2` are both defined over `Q` (so they commute with `σ`), and both satisfy
`pd_*⟨n⟩ = ⟨n mod⟩ pd_*` — **verified numerically**, `_verify/transport_check.py` (T4e),(T4f), at
`(N_g,t,p,s) = (5,2,3,1)` and `(3,2,5,1)`, ℓ ∈ {1000003, 999983}, all PASS. So the passage from the
common-level tame diamond `⟨n⟩_{Np^s}` to the native-level `⟨n mod N_gp^s⟩` (factors 2,3) and to
`⟨n mod N_fp^s⟩` (factor 1) is compatible with either choice, which is what C2's descent computation
and C5 both require. ✓

## §6. The `U'_p` normalizations

`U'_p` is defined over `Q` and commutes with all diamonds, hence with `σ` and with `R(⟨n⟩)`:

    (σ⋆Q_s)(b) = (U'_p)^{-s}_{(1)}·(σ⋆Φ̄^mod_s)((U'_p)^{-2s}b) ,

so `Q_s ∈ 𝒫^♮_s` iff `Φ̄^mod_s ∈ 𝒫^♮_s` (C2). Both the `(U'_p)^{-r}` on factor 1 and the
`(U'_p)^{-2r}` on the carrier are `⋆`-transparent. ✓ (They are also carried *through* the tower
correctly — that is the exponent computation of `05` §4, and §2–§3 here say the `⋆`-structure does
not obstruct it.)

## §7. Both sides of C4 lie in one and the same `⋆`-module

The common receptacle is `M_{r+1,r} := Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})` with the
`⋆`-action of `Gal(F'_{r+1}/K_0)` given by the **level-`r`** factor-1 diamonds and the
**level-`(r+1)`** carrier action. Two checks are needed beyond §2–§3, both because of the level gap:

* `π_r^*Q_r` for `σ ∈ Gal(F'_{r+1}/F'_r)`: then `n_σ = 1` and `m_σ ∈ 1+p^rZ_p`, so
  `⟨m_σ⟩^{-1/2}` is trivial at level `N_fp^r`; and `σ` fixes `Q_r`'s values, which lie in
  `Ĵ^{(1)}_r(F'_r)`. Invariant. ✓
* `τ_r^{MW}(Q_{r+1})` for the same `σ`: `σ(Q_{r+1}(b)) = ⟨m_σ⟩^{1/2}_{(1),r+1}Q_{r+1}(b)` by C2, and
  `ϖ_{1,*}⟨m_σ⟩^{1/2}_{(1),r+1} = ⟨m_σ mod N_fp^r⟩^{1/2}ϖ_{1,*} = ϖ_{1,*}`. Invariant. ✓

So `τ_r^{MW}(Q_{r+1})∘(1⊗N_{r+1,r})` and `π_r^*Q_r` are both in `M_{r+1,r}^{Gal(F'_{r+1}/K_0),⋆}`,
and C4's identity is an identity there. ✓ (C4 itself was proved in `05` without any of this — by
evaluationwise Kummer injectivity over `F'_{r+1}` — so §7 is a statement about *where* the identity
lives, not an ingredient of it. That order of dependence is the correct one: it keeps C4c honest.)

## §8. One recorded caveat (not a defect)

Everything above uses `W^σ = ⟨z_σ⟩W` as a standing input (B2), and the `±` exponents throughout C2/C7
flip if that law or the factor-1 transpose convention through `Π_Z` is normalized the other way. The
two structural conclusions are convention-independent: the `p`-part cancels on the carrier, and a
tame `⟨n_σ⟩` survives there. The twist is non-trivial on the `g`-branch exactly when
`ε_g^{(t)} ≠ 1` — the Castella–Hsieh case with `ε_g = ω^{-1}η_{K/Q}`, i.e. exactly the target case.

## §9. Status

| sub-claim | status |
|---|---|
| preserved by `ϖ^{(1)}_{1,*}` | PROVED (§2) |
| preserved by `π_r` / `res^bal` | PROVED (§3) |
| preserved by `1⊗N_{r+1,r}` (`d ≡ 1 mod N_g`) | PROVED (§4) |
| preserved by **both** tame push-downs | PROVED (§5), numerically corroborated |
| preserved by the `U'_p` normalizations | PROVED (§6) |
| both sides of C4 in one and the same `⋆`-module | PROVED (§7), including the `Gal(F'_{r+1}/F'_r)` steps |

**C7 = CONFIRMED.**
