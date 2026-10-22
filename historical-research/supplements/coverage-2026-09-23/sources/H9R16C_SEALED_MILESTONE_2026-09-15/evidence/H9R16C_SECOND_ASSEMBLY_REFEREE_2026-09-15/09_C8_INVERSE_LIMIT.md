# 09 — C8 (the inverse-limit point module)  [SECOND referee, independent]

**Verdict: CONFIRMED.** All four positive clauses hold; the negative clause is true and admits a
sharper proof than the one C8 offers, which is recorded because the sharper form is the useful one.

## §1. The object is well typed

There is no map `𝒫^♮_{r+1} → 𝒫^♮_r` (C3 §4), so `𝒫^♮_∞` cannot be a naive inverse limit of the
`𝒫^♮_r`. C8 defines it instead as the submodule of `∏_r 𝒫^♮_r` cut out by the level conditions, each
condition read inside the **mixed** module
`M_{r+1,r} = Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})^⋆`:

    𝒫^♮_∞ := { (Q_r)_r ∈ ∏_r 𝒫^♮_r :  τ_r^{MW}(Q_{r+1})∘(1⊗N_{r+1,r}) = π_r^*(Q_r)  ∀ r ≥ 1 }.

Both sides of each condition lie in `M_{r+1,r}` and are `⋆`-invariant there — C7 §7. So `𝒫^♮_∞` is the
equalizer of two `Z_p`-linear maps `∏_r 𝒫^♮_r ⇉ ∏_r M_{r+1,r}`, hence a `Z_p`-submodule. ✓

## §2. `π_r^*` embeds `𝒫^♮_r` injectively

`π_r : R_{r+1} → R_r` is **surjective** (`H_π`: generators to generators, and the listed generators
generate `R_r`), so `res^bal_{r+1,r} : B^bal_{r+1} → B^bal_r` is surjective under `B^bal_s ≅ R_s`
(C1), and precomposition with a surjection is injective. Together with C7 §7 (`π_r^*` lands in the
`⋆`-invariants) this is the claim. ✓ **This is the third consumption of `H_π`** (see `05` §6).

## §3. `𝕋'_∞(N_g)`-module structure

`𝕋'_∞(N_g) := lim_r R_r` along the surjective `π_r`. For `t = (t_r)_r ∈ 𝕋'_∞` put
`(t·Q)_r := Q_r ∘ R(t_r)` (action on the **carrier**, which is where `R_s` acts; the target `Ĵ^{(1)}_r`
carries the *f*-side algebra and is untouched). Then `t·Q` is again `⋆`-invariant (diamond and Hecke
operators are over `Q` and commute with `R(⟨n_σ⟩)`), and the level conditions are preserved:

    τ_r^{MW}((t·Q)_{r+1})∘(1⊗N) = ϖ_{1,*}∘Q_{r+1}∘R(t_{r+1})∘R(N)
                                = [τ_r^{MW}(Q_{r+1})∘(1⊗N)]∘R(t_{r+1})      [N central]
                                = π_r^*(Q_r)∘R(t_{r+1}) = Q_r∘res^bal∘R(t_{r+1})
                                = Q_r∘R(π_r(t_{r+1}))∘res^bal = Q_r∘R(t_r)∘res^bal = π_r^*((t·Q)_r),

the last line using `res^bal∘R(u) = R(π_r(u))∘res^bal` and the compatibility `π_r(t_{r+1}) = t_r` of
the inverse system. So `𝒫^♮_∞` is a `𝕋'_∞(N_g)`-module. ✓

## §4. `𝒬_∞ = (Q_r)_r` lies in it, integrally

* `Q_r = (U'_p)^{-r}_{(1)}∘Φ̄^mod_r∘(U'_p)^{-2r}_{carrier} ∈ 𝒫^♮_r`: C2 (`Φ̄^mod_r ∈ 𝒫^♮_r`) and
  C7 §6 (the normalizations are `⋆`-transparent).
* Level conditions: C4, with constant exactly 1.
* **Integrality**: no denominators are introduced. `U'_p` is a unit on `e'_ord`-parts, both in `R_s`
  and on `Ĵ^{(1),ord}_s`, so `(U'_p)^{-s}` and `(U'_p)^{-2s}` are honest endomorphisms of the integral
  (`Z_p`-lattice) objects — exactly BCPV's own justification for Def 4.12 (l.1438–1447). No `p` is
  divided out anywhere (C6). ✓

## §5. The naive limit: true, and provably sharper than stated

C8: "The naive inverse limit along `ϖ_{1,*}` alone is **not** this object (it would need
`Q_r ∈ p^rĴ`)." True. The sharp statement:

> Suppose `(Q_r)_r` satisfies **both** C4's condition and the naive condition
> `τ_r^{MW}(Q_{r+1}) = π_r^*(Q_r)`. Since `res^bal(N_{r+1,r}·b) = π_r(N_{r+1,r})·res^bal(b) = p·res^bal(b)`,
> composing the naive condition with `(1⊗N_{r+1,r})` gives
> `τ_r^{MW}(Q_{r+1})∘(1⊗N) = π_r^*(Q_r)∘(1⊗N) = p·π_r^*(Q_r)`.
> Comparing with C4: `π_r^*(Q_r) = p·π_r^*(Q_r)`, i.e. `(1−p)π_r^*(Q_r) = 0`. `1−p ∈ Z_p^×` and the
> ambient module is a `Z_p`-module, so `π_r^*(Q_r) = 0`, hence `Q_r = 0` by §2.

So the naive `ϖ_{1,*}`-limit meets the C4-system **only in 0** — not merely "would need `Q_r ∈ p^rĴ`"
(which the sharp form implies vacuously). This is the precise reason `(1⊗N_{r+1,r})` cannot be
dropped or replaced by its image `p`, and it is the same phenomenon as P8: `N_{r+1,r}` must be
absorbed as a **group-ring element**, never as a scalar.

Corollary worth carrying: on carrier-**coinvariants** (i.e. after applying `π_r` to the carrier) the
relation degenerates to `ϖ_{1,*}Q_{r+1} = p·Q_r`-type statements; any inverse limit formed there
loses a `p` per level. The integral object is the one defined at the level of carriers, as C8 does.

## §6. Boundary (kept, not crossed)

Per 01, C8 makes no claim about: identification of `𝒫^♮_∞` with BCPV's module, density, H9R15
localization, `f`-branch extraction, weight-one specialization, or the big Kummer trace. Nothing in
this file uses any of them, and `𝒫^♮_∞` as defined is purely a finite-level-compatible-system object.

## §7. Status

| sub-claim | status |
|---|---|
| `𝒫^♮_∞` well typed (equalizer inside the mixed `⋆`-modules) | PROVED |
| `π_r^*` embeds `𝒫^♮_r` injectively | PROVED (given `H_π`'s surjectivity clause) |
| `𝕋'_∞(N_g) = lim_r R_r`-module | PROVED |
| `𝒬_∞` lies in `𝒫^♮_∞` integrally | PROVED (C2 + C4 + C7) |
| naive `ϖ_{1,*}`-limit is not this object | PROVED, in the sharper form of §5 |

**C8 = CONFIRMED.**
