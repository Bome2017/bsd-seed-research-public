# 01 — Exact objects and types (Lane 5, fresh MPC prover, 2026-09-15)

Everything below is stated in the printed conventions of BCPV (arXiv 2409.08645v1, TeX source), DR22
(arXiv 2207.01314, TeX source) and KLZ17 (arXiv 1503.02888, Nov-2023 TeX source). Sources and hashes: 06, 08.
Weight two throughout (k = 0 in BCPV's notation); trivial coefficient sheaf.

## 1. Curves, levels, roots of unity

* `N` := the tame level in force (native level `N_g` for the auxiliary factors; the common level
  `N = lcm(N_f,N_g,N_g)` for `Δ_r^ord`). `p ∤ N`. Everything below holds verbatim for any tame level `M`
  with `p ∤ M`; see 04 §3 for the common-to-native transport.
* `X_s := X_1(N p^s)` (compactified), point-of-order model: `(A,P)`, `P` of exact order `N p^s`
  (BCPV §4.2 `\subsection{Big diagonal cycles}`; DR22 §1.3; KLZ17 Def 2.4.1 with `Y_1(N) = Y(1,N)`).
* `Γ_s := Γ_1(N p^s) ⊂ SL_2(Z)`; `X_s(C) = Γ_s\H*`. For `N p^s ≥ 4` the moduli problem is representable
  and `−1 ∉ Γ_s`.
* Roots of unity: a compatible system `ζ_{N p^{s+1}}^p = ζ_{N p^s}` (KLZ17 §7.1: `ζ_m = e^{2πi/m}` is such
  a system). This is the only normalization choice that enters.

## 2. Degeneracy maps (BCPV §4.2, DR22 §1.3 (eqn:def-varpi-12), KLZ17 Def 2.4.1)

* `ϖ_1 : X_{s+1} → X_s`, `(A,P) ↦ (A, pP)`; on `H`: `τ ↦ τ`. `deg ϖ_1 = p^2` for `s ≥ 1`.
* `ϖ_2 : X_{s+1} → X_s`, `(A,P) ↦ (A/⟨N p^s P⟩, P mod ⟨N p^s P⟩)`; on `H`: `τ ↦ pτ`
  (KLZ17: `pr_2` "corresponds to `z ↦ Az`"; DR22: "sends τ to pτ"). `deg ϖ_2 = p^2` for `s ≥ 1`.
* DR22's factorization: `ϖ_i = π_i ∘ μ` with `μ : X_{s+1} → X_{s,s+1}` the cyclic Galois cover of
  degree `p` (Galois group = the diamond kernel `K_s` below) and `π_1, π_2 : X_{s,s+1} → X_s` non-Galois
  of degree `p`.
* Matrices: `ϖ_2` is induced by `α := diag(p,1)` (τ ↦ pτ); `α Γ_{s+1} α^{-1} ⊂ Γ_s`.

## 3. Diamond operators and the kernel `K_s`

* `⟨d⟩ : X_{s+1} → X_{s+1}`, `(A,P) ↦ (A, dP)` for `d ∈ (Z/N p^{s+1})^×`; induced by any
  `δ_d ∈ Γ_0(N p^{s+1})` with lower-right entry `≡ d` (or `d^{-1}`; irrelevant below, see 02 §3).
* `K_s := ker((Z/N p^{s+1})^× → (Z/N p^s)^×) = {d ≡ 1 mod N p^s}`, cyclic of order `p` for `s ≥ 1`.
  `ϖ_1 ∘ ⟨d⟩ = ϖ_1` for `d ∈ K_s` (since `p·dP = pP`). `K_s` is the Galois group of `μ`.
* **The norm element** `N_{s+1,s} := Σ_{d ∈ K_s} ⟨d⟩ ∈ Z[ diamonds of level N p^{s+1} ]`.
  It is central in the Hecke algebra (diamonds commute with `U'_p`, `U_p`, `T'_ℓ`) and is fixed by
  `⟨d⟩ ↦ ⟨d^{-1}⟩`. Under DR22's `p_{r+1,r}: Λ(G_{r+1}) → Λ(G_r)` it is the trace of the kernel.

## 4. Hecke operators (KLZ17 Def 2.4.4; DR22 §1.3; BCPV §1.1.8)

Let `Z_s := X(Γ_s ∩ Γ_0(N p^{s+1})) = X_{s,s+1}` with `a_s := π_1` ("τ ↦ τ") and `b_s := π_2` ("τ ↦ pτ").

* `U'_p := (π_1)_* ∘ (π_2)^*` on `H^1(X_s)` (DR22 §1.3: `U_p^* := π_{1*}π_2^*`; KLZ17 Def 2.4.4:
  `U'_p = pr_* ∘ Φ_p^* ∘ hpr^*`, whose two legs are "τ ↦ τ" (pushforward) and "τ ↦ pτ" (pullback);
  BCPV §1.1.8 `e'_ord := lim (U'_p)^{n!}` "Hida's ordinary projector associated to `U'_p`").
  As a correspondence (multivalued map on points, pushforward along the target leg):
  `U'_p : (A,P) ↦ Σ_{C ⊂ A[p], |C| = p, C ∩ ⟨P⟩ = 0} (A/C, P mod C)`, i.e. `τ ↦ Σ_{b mod p} (τ+b)/p`
  = the right cosets of `Γ_s diag(1,p) Γ_s = ⊔_b Γ_s [[1,b],[0,p]]`.
* `U_p := (π_2)_* ∘ (π_1)^*` = the Poincaré transpose of `U'_p` (KLZ17 §2.4: "`T_ℓ` ... are the transposes
  of the `T'_ℓ` with respect to Poincaré duality"; DR22 §2.3: "`U_p` and `U_p^*` are adjoint").
  As a correspondence: `τ ↦ Σ_{a mod p} [[p,0],[aNp^s,1]]·τ` (right cosets of `Γ_s diag(p,1) Γ_s`).
* On weight-2 forms (via `H^0(Ω^1) ⊂ H^1_dR`): `U_p` is the classical operator `Σ a_{pn} q^n`; `U'_p` is its
  adjoint (KLZ17 §2.4: "it is the `T_ℓ` rather than the `T'_ℓ` that correspond to the familiar formulae
  for the action on q-expansions"). Derived check in 02 §1.
* `e'_ord := lim_n (U'_p)^{n!}`, `e_ord := lim_n (U_p)^{n!}`.

## 5. Atkin–Lehner operator (KLZ17 Def 2.5.2 and Def 2.5.4, `Q = N p^s` full level)

* Matrix class: `W_{Np^s} = [[Np^s x, y],[Np^s z, Np^s w]]` with `Np^s xw − yz = 1`, `y ≡ −1 mod Np^s`;
  the representative `w_s := [[0,−1],[N p^s, 0]]` (x = 0, y = −1, z = 1, w = 0) is the classical
  Fricke matrix; it induces `τ ↦ −1/(N p^s τ)`.
* Moduli: `W_s(E,P) := (E/⟨P⟩, P')` with `P' ∈ E[Np^s]/⟨P⟩` the unique class with
  `e_{Np^s}(P, P') = ζ_{Np^s}` (Weil pairing). Defined over `Z[1/N, ζ_{Np^s}]`; over `C` it coincides with
  the matrix action (KLZ17, sentence after Def 2.5.4).
* Relations (KLZ17 after Def 2.5.2, full level `Q = N`): `W_N^2 = [[N,0],[0,N]]·⟨N⟩_1·⟨−1⟩_N`. In
  weight 2 the scalar matrix acts trivially, `⟨N⟩_1 = 1`, and `⟨−1⟩_N = id` on `Y_1(N)`; hence
  **`W_s^2 = id` as an automorphism of `X_s`, so `W_s^{-1} = W_s` and `W_s^* = W_{s,*}` on `H^1(X_s)`.**
* Galois: `W_s^σ = ⟨a⟩ W_s` for `σ(ζ_{Np^s}) = ζ_{Np^s}^a` (Ohta 1999 (4.2.4): `w_r^σ = w_r∘T(a;a) = T^*(a;a)∘w_r`;
  BCPV Lemma 4.2(ii) uses "the moduli description of the Atkin–Lehner operator and the action of
  Gal(Q(μ_{p^r})/Q)"). Not needed for MPC (both sides of MPC are conjugated identically); needed for the
  group-ring packaging in 05.
* `A_s := W_{Np^s}^{-1} (U'_p)^s = W_s (U'_p)^s` on `H^1(X_s)` (BCPV (1.6)/(1.8): `x ⊗ y ↦ ⟨x, W^{-1}(U'_p)^r y⟩`).

## 6. Cohomology, pairings, functoriality (the only formal inputs)

Let `H^1(X_s)` denote any of: Betti `H^1(X_s(C), Z)`, étale `H^1_ét(X̄_s, Z_p)` or `H^1_ét(X̄_s, Z_p(1))`,
`H^1_dR`. All statements below are identities of algebraic correspondences (cycles on `X_{s} × X_{s'}`
defined over `Q(μ_{Np^{s+1}})`), so they hold in every Weil cohomology theory compatibly with the
comparison isomorphisms and with the Galois action.

* (F1) For a finite morphism `f : Y → X` of smooth projective curves: `f^*`, `f_*` on `H^1`;
  `f_* f^* = deg f`; projection formula `⟨f_* u, x⟩_X = ⟨u, f^* x⟩_Y` for the Poincaré pairings.
* (F2) A correspondence `T = (Z; a, b)` (`a, b : Z → X` finite) acts as `T := b_* a^*`; its transpose
  `T^t := a_* b^*` satisfies `⟨T x, y⟩ = ⟨x, T^t y⟩`. Composition of correspondences (as multivalued
  maps on points, first `T_1` then `T_2`) is composition of operators `T_2 ∘ T_1`.
* (F3) For a finite cover `f: Y → X` and a finite `g : Y' → X`, the composite `g^* f_*` is the
  correspondence `Y ×_X Y'` (fibre product along `f, g`), i.e. on points `y ↦ g^{-1}(f(y))` with
  multiplicities; `f_* g^*` likewise `y' ↦ f(g^{-1}... )` — used as `x ↦ f(g^{-1}(x))`.
* (F4) An automorphism `w` of `X` (over a field) acts as `w^* = (w^{-1})_*`; if `w^2 = id` then
  `w^* = w_*`.

Nothing else is assumed. No density argument, no localization, no weight-one specialization, no Λ-adic
input, no Ohta II.

## 7. The target, typed

**MPC_r(N_{r+1,r}), operator form.** For `r ≥ 1`, as endomorphisms of `H^1(X_{r+1})`:

    ϖ_1^* ∘ A_r ∘ ϖ_{1,*}  =  d_r · A_{r+1} ∘ N_{r+1,r},    A_s = W_s (U'_p)^s.

**Pairing form.** For all `y, z ∈ H^1(X_{r+1})`:

    ⟨ϖ_{1,*} y, A_r ϖ_{1,*} z⟩_r  =  d_r · ⟨y, A_{r+1} N_{r+1,r} z⟩_{r+1}.

The two forms are equivalent by (F1) (projection formula for `ϖ_1`) and perfectness of `⟨,⟩_{r+1}`.
Restricting to `e'_ord H^1` gives Lane 2's `MPC_r(ν)` with `ν_{r+1} = d_r N_{r+1,r}` and Lane 4's `(★_r)`
with `u_r = d_r N_{r+1,r}`. **Proved in 02–04 with `d_r = 1`, on all of `H^1`, not only on `e'_ord H^1`.**
