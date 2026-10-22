# 02 — Derivation of the norm element `N_{r+1,r}` from the group-ring / coset structure

Conventions and inputs: 01. Throughout `M := N p^r` (`r ≥ 1`), `Γ := Γ_r = Γ_1(M)`, `Γ' := Γ_{r+1} = Γ_1(pM)`,
`α := diag(p,1)` (so `ϖ_2` is `τ ↦ ατ` and `ϖ_1` is `τ ↦ τ`). All identities are identities of
correspondences (effective cycles on `X_{r+1} × X_{r+1}` or `X_s × X_{s'}`), hence of operators on any `H^1`.

## §0. Why a norm element and not a constant: two different composites

Two composites of the degeneracy maps occur in this problem and must not be confused:

| composite | multivalued map on points | value |
|---|---|---|
| `ϖ_{2,*} ϖ_1^*` (pull back along `ϖ_1`, push along `ϖ_2`) | `x ↦ ϖ_2(ϖ_1^{-1}(x))` | `p · U_p` (§2) |
| `ϖ_{1,*} ϖ_2^*` | `x ↦ ϖ_1(ϖ_2^{-1}(x))` | `p · U'_p` (§2) |
| **`ϖ_2^* ϖ_{1,*}`** (push along `ϖ_1`, then pull back along `ϖ_2`) | `y ↦ ϖ_2^{-1}(ϖ_1(y))` | **`U'_p ∘ N_{r+1,r}`** (§3) |
| `ϖ_1^* ϖ_{1,*}` | `y ↦ ϖ_1^{-1}(ϖ_1(y))` | not a group-ring element (`ϖ_1` is not Galois) |

The first two are Hida's "U-isomorphism" composites (Hida LMWM (6.6): `π_s^r ∘ π^*_{r,s} = p^{s−r} U(p^{s−r})`):
a power of `p` appears because a degree-`p^2` map is pushed through the *other* leg. The identity MPC
needs is the third one — the fibre of `ϖ_2` over `ϖ_1(y)` — and it produces the *group-ring norm*, with
no power of `p`. This is the whole content of the derivation; Lane 4's worry about a `p`-power
"as in Hida (6.4)" concerns the first row, which never enters MPC.

## §1. Sanity anchor: which operator is `U'_p` (derived, not assumed)

Let `𝒰` be the correspondence `x ↦ Σ_{b mod p} β_b x`, `β_b := [[1,b],[0,p]]`, i.e. `(A,P) ↦ Σ_C (A/C, P mod C)`
over the `p` subgroups `C` of order `p` with `C ∩ ⟨P⟩ = 0` (lattice check: `A_τ/⟨(τ+b)/p⟩ = A_{(τ+b)/p}` and the
point `1/M` maps to `1/M`). Its target-leg pushforward `b_* a^*` is KLZ17's `U'_p = pr_* ∘ (hpr∘φ_p)^*`
(pullback along "τ ↦ pτ", pushforward along "τ ↦ τ"; the fibre of "τ ↦ pτ" over `x` is `{(x+b)/p}`) and
DR22's `U_p^* = π_{1*} π_2^*`. On a weight-2 form `ω = f dτ`, the local branches of `b_* a^*` at `τ'` are
`x = α^{-1}γ_a τ' = [[p,0],[aM,1]]τ'` (`γ_a = [[1,0],[aM,1]]` representing `Γ/(Γ ∩ αΓα^{-1})`), so

    (U'_p ω) = Σ_a f|_2 [[p,0],[aM,1]] dτ = f|[Γ diag(p,1) Γ] dτ,

the *adjoint* of the classical `U_p = f|[Γ diag(1,p) Γ] = (1/p)Σ_b f((τ+b)/p)`. This matches KLZ17 §2.4
("`T'_ℓ` are the transposes of `T_ℓ`"; "`T_ℓ` correspond to the familiar formulae on q-expansions").
So `U'_p` = target-pushforward of `𝒰`, `U_p = (U'_p)^t` = target-pushforward of `𝒰^t : x ↦ Σ_a [[p,0],[aM,1]] x`.
(Double-coset bookkeeping: `Γ diag(1,p) Γ = ⊔_b Γ β_b` and `Γ diag(p,1) Γ = ⊔_a Γ [[p,0],[aM,1]]`, the latter
because `[[1,0],[c,1]] diag(p,1) = diag(p,1) [[1,0],[cp,1]]` and `[[1,0],[cp,1]] ∈ Γ_1(M)` iff `M | cp`.)

## §2. The two "U-isomorphism" composites (for orientation; also reproduces KLZ17 Prop 2.4.5)

(a) `ϖ_{2,*} ϖ_1^*`: `x ↦ Σ_{γ ∈ Γ'\Γ} αγx` (`p^2` terms). The cosets `Γ αγ` lie in `Γ diag(p,1) Γ`, which has
`p` right cosets; `Γ' ⊂ H' := Γ ∩ α^{-1}Γα` (index `p` in `Γ`), so each coset is hit `p` times:
`ϖ_{2,*}ϖ_1^* = p · U_p`. Transposing: `ϖ_{1,*} ϖ_2^* = p · U'_p`.

(b) `ϖ_{2,*} U'_p` (level `r+1` to `r`): `x ↦ Σ_b ϖ_2((x+b)/p) = Σ_b (x+b) = p·x` in `X_r`
(`[[1,b],[0,1]] ∈ Γ`), i.e. `ϖ_{2,*} ∘ U'_p = p · ϖ_{1,*}`. This is exactly KLZ17 Prop 2.4.5 (`(pr_2)_* U'_p =
p^{k+1} (pr_1)_*`, `k = 0`). The framework reproduces a printed identity.

(c) `ϖ_{1,*} U'_p = U'_p ϖ_{1,*}` as cycles (`(A,P') ↦ Σ_{C ≠ ⟨P'⟩[p]} (A/C, pP' mod C)` on both sides, since
`⟨pP'⟩[p] = ⟨P'⟩[p]` for `r ≥ 1`). This is DR22 §1.3 ("`U_p^*` is compatible with the transition maps") and is
used in BCPV Lemma 4.10 / Cor 4.11. Transposing: `ϖ_1^* U_p = U_p ϖ_1^*`. (Note: `ϖ_1^* U'_p ≠ U'_p ϖ_1^*`
as cycles — the defect is exactly a diamond in `K_r`; this is where the norm element comes from.)

## §3. THE NORM-ELEMENT IDENTITY: `ϖ_2^* ∘ ϖ_{1,*} = U'_p ∘ N_{r+1,r}` on `H^1(X_{r+1})`

**Statement.** As correspondences on `X_{r+1}` (each with `p^2` points counted with multiplicity one):

    ϖ_2^* ∘ ϖ_{1,*}  =  U'_p ∘ N_{r+1,r}  =  N_{r+1,r} ∘ U'_p,      N_{r+1,r} = Σ_{d ∈ K_r} ⟨d⟩.

**Proof A (double cosets).** By (F3) the left side is `y ↦ ϖ_2^{-1}(ϖ_1(y)) = {αγ y : γ ∈ Γ}` modulo `Γ'`, i.e.
the sum over the distinct right cosets `Γ' αγ`, `γ ∈ Γ`. Two elements give the same coset iff
`αγγ'^{-1}α^{-1} ∈ Γ'` iff `γγ'^{-1} ∈ H := α^{-1}Γ'α ∩ Γ`. Computing `α^{-1}[[a,b],[c,d]]α = [[a, pb],[c/p, d]]`:

    H = { δ = [[a,b],[c,d]] ∈ Γ_1(M) : b ≡ 0 (mod p),  d ≡ 1 (mod pM) }.

`[Γ : H] = p^2` (index `p` for `b ≡ 0 (p)` inside `Γ_1(M)` with `p | M`, then index `p` for `d mod pM`).
Choose diamond representatives `δ_d ∈ Γ_1(M) ∩ Γ^0(p) ∩ Γ_0(pM)` with lower-right entry `≡ d (mod pM)`,
`d ∈ K_r` (possible: take lower-left `pM`, lower-right `d' ≡ d (pM)` coprime to `pM`, upper-left
`a ≡ d'^{-1} (mod p^2 M)`, upper-right `(ad'−1)/(pM) ≡ 0 (mod p)`). Then the `p^2` elements
`[[1,b],[0,1]] δ_d` (`b mod p`, `d ∈ K_r`) are pairwise inequivalent mod `H` (the product
`[[1,b],[0,1]]δ_dδ_{d'}^{-1}[[1,−b'],[0,1]]` has upper-right `≡ b − b' (mod p)` and lower-right `≡ d/d' (mod pM)`
because `δ_dδ_{d'}^{-1} ∈ Γ^0(p) ∩ Γ_0(pM)`), hence form a full set of representatives of `H\Γ`. Therefore

    ϖ_2^* ϖ_{1,*} : y ↦ Σ_{d ∈ K_r} Σ_{b mod p} α [[1,b],[0,1]] δ_d y = Σ_{d ∈ K_r} Σ_b β_b (δ_d y),

which is "first the diamond `⟨d⟩`, then `𝒰`", i.e. the operator `U'_p ∘ Σ_d ⟨d⟩_*` by (F2). Since `K_r` is a
group, `Σ_d ⟨d⟩_* = Σ_d ⟨d⟩^* = N_{r+1,r}` whatever convention (`d` vs `d^{-1}`) is used for diamonds, and
diamonds commute with `U'_p`. ∎

**Proof B (moduli; independent of A).** For `(A,P') ∈ X_{r+1}` (`P'` of order `pM`), `ϖ_1(A,P') = (A, pP')` and

    ϖ_2^{-1}(A, pP') = { (A/D, (P'+t) mod D) : D ⊂ A[p] of order p, D ≠ ⟨P'⟩[p];  t ∈ A[p]/D }.

Indeed a point `(B,R)` with `B/⟨N p^r R⟩ ≅ A`, `R ↦ pP'`, corresponds to an isogeny `ψ: B → A` of degree `p`
with `ker ψ = ⟨N p^r R⟩`; writing `B = A/D` with `D = ker(ψ̂)` one gets `ψ(R) = pP' = ψ(ψ̂ P')`, so
`R = ψ̂(P' + t)` with `t ∈ A[p]`; `N p^r R = N p^r P' mod D` (as `p^r t = 0`) generates `A[p]/D = ker ψ` iff
`D ≠ ⟨N p^r P'⟩ = ⟨P'⟩[p]`, and then `R` has exact order `pM`. Count: `p · p = p^2 = deg ϖ_2`. ✓
On the other side, `N_{r+1,r}(A,P') = Σ_{d ∈ K_r} (A, dP') = Σ_{t ∈ ⟨P'⟩[p]} (A, P' + t)` (as `d = 1 + N p^r u`
runs over `K_r`, `(d−1)P' = u·N p^r P'` runs over `⟨P'⟩[p]`), and `U'_p(A, P'+t) = Σ_{C ≠ ⟨P'+t⟩[p] = ⟨P'⟩[p]} (A/C, (P'+t) mod C)`.
For fixed `C = D ≠ ⟨P'⟩[p]`, `t ↦ t mod D` is a bijection `⟨P'⟩[p] → A[p]/D`. Hence the two multisets of
points coincide. ∎

**Consistency checks (both pass).** Apply `ϖ_{2,*}` on the left: `ϖ_{2,*}ϖ_2^*ϖ_{1,*} = p^2 ϖ_{1,*}` (F1), while
`ϖ_{2,*} U'_p N = p ϖ_{1,*} N = p · p · ϖ_{1,*}` by §2(b) and `ϖ_{1,*}⟨d⟩ = ϖ_{1,*}` for `d ∈ K_r`. ✓
Apply `ϖ_{1,*}`: `ϖ_{1,*}ϖ_2^*ϖ_{1,*} = p U'_p ϖ_{1,*}` (§2(a)), while `ϖ_{1,*}U'_p N = U'_p ϖ_{1,*} N = p U'_p ϖ_{1,*}`. ✓
Degrees: both sides have `p^2` points over a generic `y`. ✓

**Relation to DR22 Lemma 2.4/2.8.** Through DR22's factorization `ϖ_i = π_i∘μ`: `μ^* μ_* = Σ_{d ∈ K_r} ⟨d⟩ = N_{r+1,r}`
(DR22 (eqn:galois-pushforward), `μ` Galois with group `K_r`), and `ϖ_2^* ϖ_{1,*} = μ^* (π_2^* π_{1*}) μ_*`. The identity
says `π_2^* π_{1*} = μ_* U'_p μ^*/p`-type bookkeeping is unnecessary: the norm element is *exactly* `μ^*μ_*`, the
"Galois pushforward" that DR22 use in the proof of Lemma 2.8 (there for the triple product), with no constant.
This is the "invariant group-ring transition" the prompt asks to use instead of BCPV (4.9); (4.9) is not used
anywhere in this lane.

## §4. What `N_{r+1,r}` is in the three group-ring languages

* Level-`N p^{r+1}` diamonds `(Z/Np^{r+1})^×`: `N_{r+1,r} = Σ_{d ≡ 1 (Np^r)} ⟨d⟩`, the trace of the kernel of
  `(Z/Np^{r+1})^× → (Z/Np^r)^×`. Its image under the projection of group rings is `p · 1`.
* BCPV's `G_r ⊂ ((Z/p^r)^×)^3` (p-Sylow, three factors): on ONE auxiliary factor the same element is the trace of
  `ker(G^{(i)}_{r+1} → G^{(i)}_r)`, of order `p`. The kernel of `G_{r+1} → G_r` for the *triple* group has order
  `p^3 = |K_r|^3`, which is the number Lane 4 found in BCPV (4.9); it is the product of the three per-factor
  kernels and never appears as a scalar in MPC.
* KLZ17 `Λ_D = Z_p[[Z_p^×]]` acting through inverse diamonds `⟨u^{-1}⟩_{p^r}` (Prop 7.2.1(1)): `N_{r+1,r}` is the
  image of the trace element `Σ_{u ∈ (1+p^rZ_p)/(1+p^{r+1}Z_p)} [u]` (inversion-invariant, so the `u ↔ u^{-1}` convention is immaterial).
