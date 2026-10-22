# `c₂(p)` WITNESS — referee report

Witness definition used throughout: the correction supplied with this run (BLV with `g = f_E`,
`L = 1`, `R = Z_p`; `Λ = Z_p[[T]]`, `T = γ_∞ − 1`, `c₂(p) = [T²] 𝓛_{f_E} ∈ Z_p`; at the first
finite layer the image of `𝓛_{f_E,1}` in `F_p[G₁]/I³ ≅ F_p[t]/(t³)` determines `c₂(p) mod p`, with

    c₂(p) mod p  =  − Σ_{j=0}^{p−1} C(j,2) · ψ̄_{f_E}(γ^j P₁),   P₁ = traced conductor-`p²` Gross point).

This supersedes `INPUTS.md` §4 and `TASK.md`'s witness definition. The forward bridge and the
computational formula are unchanged and are **not** re-audited (no dependency error was found in
the course of this work, and none is claimed).

---

## VERDICT

    FIRST_MISSING_THEOREM:
      Let E/Q be non-CM, K imaginary quadratic with a factorization N = N⁺·N⁻ satisfying the
      definite Heegner hypothesis (N⁻ squarefree, odd number of prime factors), r = rank E(K),
      and let p ≥ 5 be a good ordinary prime with p ∤ N·disc(K)·h_K and ρ̄_{E,p} surjective.
      Let 𝓛_{f_E} ∈ Λ = Z_p[[T]] be BLV's square-root anticyclotomic p-adic L-function for
      (g, L, R) = (f_E, 1, Z_p) with ψ_{f_E} surjective and traced Gross points.  Then

            ord_T ( 𝓛_{f_E}  mod p )  =  r ,

      i.e.  μ(𝓛_{f_E}) = 0  and  λ(𝓛_{f_E}) = r ;  equivalently λ(L_p) = 2r for L_p = 𝓛·𝓛^ι.

For the seed, `r = 2`, and the case `r = 2` of this statement **is** the target `c₂(p) ∈ Z_p^×`
(proved equivalent below, in Lean, at the level of `Λ`-algebra).

What is missing is specifically the **upper bound** `λ ≤ r`: the lower bound `ord_T 𝓛 ≥ r` is the
unconditional input (BD Annals 2005, Cor. 3, with the certified `(r⁺,r⁻) = (2,0)`), and
`μ = 0` is the subject of the existing anticyclotomic nonvanishing literature. No statement in the
literature, and no argument found here, produces exactness of the order — at any single admissible
ordinary `p` for this curve, let alone uniformly.

### Quantifier level reached (per `TASK.md`)

**None of 1–4.** Not level 1: the witness is not established at a single prime. What is delivered
is (i) a `sorry`-free formalization of the algebra surrounding the witness, including two exact
reformulations of the target, and (ii) the statement of the first missing theorem together with a
labelled account of where each admissible route class stops.

---

## 1. What is proved here (machine-checked)

`RequestProject/C2Witness.lean` builds against Mathlib and contains **no `sorry` and no added
axioms** (all results depend only on `propext`, `Classical.choice`, `Quot.sound`). The arithmetic
inputs are *abstracted*, not assumed: the Gross-point data enters only as the packet of mod-`p`
values `v j = ψ̄_{f_E}(γ^j P₁) ∈ F_p`, and the theorems below are theorems about that data. In
particular nothing in the file assumes the target (`GATE.md` K1).

Label for every item in this section: **identification proved here, with proof (Lean)**.

| # | statement | Lean name |
|---|---|---|
| 1 | `t^k`-coefficient extraction: `[t^k] Σ_j a_j (1+t)^j = Σ_j C(j,k) a_j` | `coeff_sum_one_add_X_pow` |
| 2 | hockey stick `Σ_{j<n} C(j,k) = C(n,k+1)`; coefficients of the cyclic norm element `N = Σ_{j<p} γ^j` | `sum_range_choose_eq_choose`, `coeff_sum_one_add_X_pow_const` |
| 3 | for `p ≥ 5`, `N ≡ 0` in degrees `≤ 2` mod `p`: the ordinary stabilization term `α^{-1}ψ(P₀)·N` is invisible in `F_p[t]/(t³)` | `norm_element_coeff_eq_zero` |
| 4 | `(1+t)^p − 1 = t^p` in characteristic `p`, and `(t^p) ⊆ (t³)` for `p ≥ 3`: `F_p[G₁]/I³ ≅ F_p[t]/(t³)` | `one_add_X_pow_char`, `X_pow_mem_span_X_pow_three` |
| 5 | the witness depends only on the image in `F_p[t]/(t³)` — i.e. the first layer determines `c₂(p) mod p`, not the integral coefficient | `c2bar_eq_of_sub_mem_span` |
| 6 | **the reduction formula itself**, derived from BLV's layer-one element `α^{-1}Σ_σ ψ(σP₀)σ − Σ_σ ψ(σP₁)σ`: for `k ≤ 2` its `t^k`-coefficient is `−Σ_j C(j,k) v j`; for `k = 2` this is exactly the displayed formula for `c₂(p) mod p` | `layerOne`, `coeff_layerOne`, `coeff_two_layerOne` |
| 7 | `2·c₂ = M₁ − M₂` where `M_k = Σ_{j<p} j^k v j`; and the unconditional lower order (`layerOne ∈ I²`) forces `M₁ = 0` | `two_mul_c2bar`, `moment_one_eq_zero_of_layerOne_mem` |
| 8 | **Capstone.** For `p ≥ 5`, granting only the unconditional lower order, `c₂(p) ∈ Z_p^×` ⟺ `Σ_{j=0}^{p−1} j² · ψ̄_{f_E}(γ^j P₁) ≠ 0` in `F_p`; explicitly `c₂(p) ≡ −2^{-1} Σ_j j² v j` | `layerOne_coeff_two_ne_zero_iff`, `c2bar_eq_neg_inv_two_mul_moment_two`, `c2bar_ne_zero_iff_moment_two_ne_zero` |
| 9 | changing the topological generator `γ_∞ ↦ γ_∞^a` multiplies the `k`-th moment by `a^{-k}`; for `k = 2` the witness is therefore generator-independent | `momentZ_generator_change`, `momentZ_two_ne_zero_generator_independent` |
| 10 | **Obstruction.** The second moment annihilates every packet whose mod-`p` values are a polynomial function of the Galois index of degree `≤ p − 4`; in particular constant and affine packets give `c₂(p) ≡ 0` | `momentZ_eq_zero_of_low_degree`, `momentZ_two_eq_zero_of_affine` |
| 10′ | **Sharp form of the obstruction.** Writing the packet as the polynomial function `v x = Σ_{i<p} c_i x^i` (Lagrange; every function on `F_p` is such, uniquely), one has `Σ_x x² v x = −c_{p−3}`. So `c₂(p) ∈ Z_p^×` ⟺ `c_{p−3} ≠ 0`: the witness *is* one designated high-degree coefficient of the interpolating polynomial of the Gross-point packet | `momentZ_two_eq_neg_coeff`, `momentZ_two_ne_zero_iff_coeff_ne_zero`, `exists_poly_repr`, `sum_pow_eq_ite` |
| 11 | **Iwasawa form.** For `𝓛 ∈ I² ⊆ Λ`, `c₂(p) ∈ Z_p^×` ⟺ the mod-`p` reduction of `𝓛` has order exactly `2`, i.e. `μ(𝓛) = 0` and `λ(𝓛) = 2` | `isUnit_c2_iff_order_eq_two` |

Two consequences worth isolating.

* **(Sharper computational formula.)** Item 7 is new relative to the packet's formula: the
  unconditional lower order is not merely a lower bound on the order of vanishing, it is the
  *vanishing of the first moment of the packet*, and using it the binomial weight `C(j,2)`
  collapses to the pure second moment. So the target is

        Σ_{j=0}^{p−1} j² · ψ̄_{f_E}(γ^j P₁)  ≠  0   in F_p .

  (Consistency remark, *not formalized*: by item 9 the witness must transform with weight `−2`
  under `γ_∞ ↦ γ_∞^a`, and the raw expression `−(M₂ − M₁)/2` transforms that way for every `a`
  if and only if `M₁ = 0` — which is what the unconditional lower order supplies.)

* **(The witness is one high-degree coefficient.)** By items 10 and 10′ the witness is blind to
  every degree except `p − 3`: it is nonzero precisely when the interpolating polynomial of
  `j ↦ ψ̄_{f_E}(γ^j P₁)` on `F_p` has nonzero coefficient in degree `p − 3`. In particular no
  "smooth"/low-degree behaviour of the packet can produce a unit, and conversely nonvanishing
  results about the *values* `ψ̄(γ^j P₁)` individually — or about their distribution — say nothing
  about that one coefficient. This is the precise sense in which the ordinary lane's remaining
  obstruction is distributional, and it is sharper than "the values are not constant".

---

## 2. Equivalent forms of the missing theorem

Each is labelled per `GATE.md` K4.

* **(M1) Analytic / finite-layer form.** `Σ_{j=0}^{p−1} j² · ψ̄_{f_E}(γ^j P₁) ≠ 0` in `F_p`;
  equivalently (item 10′) the interpolating polynomial of `j ↦ ψ̄_{f_E}(γ^j P₁)` on `F_p` has
  nonzero coefficient in degree `p − 3`.
  *Status: **proved here to be equivalent** to `c₂(p) ∈ Z_p^×`, given only the unconditional lower
  order (Lean, item 8). The nonvanishing itself: **OPEN**.*

* **(M2) Iwasawa form.** `ord_T(𝓛_{f_E} mod p) = 2`, i.e. `μ(𝓛_{f_E}) = 0` and `λ(𝓛_{f_E}) = 2`;
  equivalently `λ(L_p) = 4 = 2·rank E(K)`.
  *Status: **proved here to be equivalent** to `c₂(p) ∈ Z_p^×` as `Λ`-algebra (Lean, item 11). The
  equality itself: **OPEN**. Note `μ = 0` alone is insufficient: it gives `λ < ∞`, not `λ = 2`.*

* **(M3) Algebraic form.** `Sha(E/K)[p^∞] = 0` **and** the Bertolini–Darmon derived `p`-adic height
  of the relevant order is nondegenerate on `E(K) ⊗ Z_p` (`ρ_p = 4`).
  *Status: **conditional** — the passage (M2) ⇔ (M3) uses BLV's ordinary equality
  `(L_p) = (Char_p)` and BD's derived-height theory (`INPUTS.md` §2), neither of which is replayed
  here. Recorded because it identifies what an algebraic route must supply. Note `INPUTS.md` §2:
  finiteness of `Sha` plus `R_der ≠ 0` does **not** suffice; the extra input is exactly
  `ρ_p = 4`.*

The first missing theorem is the **exactness of the order** — the upper bound `λ ≤ r`. Everything
else in the chain is either unconditional input (`λ ≥ r`) or a literature theorem about `μ`.

---

## 3. Why each admissible route class stops

### A. Analytic / horizontal nonvanishing — stops at a *fixed-layer, fixed-moment* statement

*Labels: literature statements below are **cited, not re-verified**; the mismatch analysis is an
**identification proved here** (items 8–10) plus an **unsupported inference** about the absence of
a route.*

The available machinery (Vatsal's uniform-distribution/μ-invariant results for definite
anticyclotomic theta elements; Cornut–Vatsal nonvanishing; Chida–Hsieh; and the Burungale-school
papers tabulated in `INPUTS.md` §5) produces nonvanishing **either** for all but finitely many
characters of conductor `p^n` with `n → ∞` at a **fixed** `p`, **or** for families of Hecke
characters in the CM/self-dual setting. Both are statements at high layers or at varying
characters.

The witness is orthogonal to that: by item 8 it is a **single `F_p`-linear functional of a
`p`-term packet at the first layer `n = 1`**, namely the second moment. Equidistribution input
controls such a sum only up to error terms that are `o(p)` in archimedean or `ℓ`-adic measure and
are *invisible mod `p`*; a mod-`p` statement about a `p`-term sum is not implied by any density or
equidistribution estimate of that shape. Items 10 and 10′ sharpen this decisively: the functional
is exactly the degree-`(p−3)` coefficient of the interpolating polynomial of the packet, so any
would-be proof must control one designated *high-degree* mod-`p` coefficient — not merely show
that the values are non-constant, or non-zero for most `j`, which is all that equidistribution and
the known nonvanishing theorems deliver.

This is a statement about *known methods*, not an impossibility result (`GATE.md` K5).

### B. Algebraic — stops at an input that is itself open, and at rank 2

*Labels: **cited** literature; **unsupported inference** that no current route exists.*

By (M3), an algebraic route must supply both `Sha(E/K)[p^∞] = 0` and derived-height
nondegeneracy. For this seed `rank E(Q) = 2 = analytic rank`, so Gross–Zagier–Kolyvagin supplies
nothing (it requires analytic rank `≤ 1`), and `E^{-7}` — the rank-0 twist — is already used up in
the certified `(r⁺,r⁻) = (2,0)` input; its finite `Sha` contributes only the exponent bound `2c`
already in the bridge. There is no Euler-system or Iwasawa-divisibility input known to bound
`Sha(E/Q)[p^∞]` for a curve of algebraic and analytic rank 2 at a general ordinary `p`. Derived
`p`-adic height nondegeneracy is a conjecture of the Schneider/Perrin-Riou type, open even for
rank-1 curves in the anticyclotomic derived setting.

Consequence worth stating plainly, as a calibration of the target's difficulty: a **uniform**
`c₂(p) ∈ Z_p^×` would, through the forward bridge, give `Sha(E/Q)[p^∞] = 0` at every good ordinary
`p ≥ 5`, `p ∤ 7N` — i.e. essentially finiteness of `Sha` for a rank-2 curve (up to the three bad
primes `2243, 4547, 5843` and the supersingular lane A3, both explicitly out of scope). No
unconditional technique for that is known. This does not make the target false or unprovable; it
does mean that route B cannot be closed by assembling existing theorems.

### C. Compressed computation — the precise missing primitive

*Labels: the resource statement is **cited input** (`INPUTS.md` §3); the reduction of the data
requirement is **proved here**; the twist remark at the end is an explicitly **unsupported
inference**.*

Item 8 is a genuine compression of the *data* requirement, and should be recorded as such: the
witness at a given `p` needs only

    the p values  ψ̄_{f_E}(γ^j P₁) ∈ F_p,  j = 0,…,p−1,

i.e. `p` scalars mod `p` — not the Brandt module, not the eigenvector, not the class set. What is
missing is the *evaluation primitive*:

> **Missing computational theorem.** An algorithm which, given the definite quaternion algebra `B`
> ramified at `{3, 2243, 5843, ∞}`, an Eichler order of level `N⁺ = 2³·4547²`, a good ordinary
> prime `p`, and a traced Gross point `x` of conductor `p²`, returns `ψ̄_{f_E}(x) ∈ F_p` for the
> **surjective (primitive)** eigenfunctional attached to `f_E`, in time polynomial in
> `log(mass) + log p`, i.e. **without** materializing the class set of mass `5.42·10^14`.

Two sub-problems are each unsolved, and `GATE.md` K2 is satisfied only if both are: (i) isolating
the `f_E`-eigencomponent of the Brandt module without computing the module (a trace-formula or
theta-series identity computing `⟨x, e_{f_E}⟩` directly), and (ii) certifying the **primitive**
normalization of `ψ_{f_E}` — `INPUTS.md` §4 warns that unit status is destroyed by rescaling by a
non-unit, so a computation that produces `ψ` only up to an unknown `p`-adic scalar proves nothing.
Note finally that even a complete success here reaches only `FIXED_P` (level 1 of the quantifier
discipline) and therefore does not reach FIN.

*Unsupported inference, flagged for verification, not used anywhere above:* the Eichler mass is
dominated by the factor `4547·4548 ≈ 2.07·10^7` coming from `4547² ‖ N⁺`. `INPUTS.md` §1 records
`v_q(j) < 0` only at `q = 3, 2243, 5843`, so `E` has potentially **good** reduction at `4547`. If
the reduction type there is the quadratic-twist type (`I₀*`), then `E` is a quadratic twist of a
curve unramified at `4547`, and the corresponding definite Shimura set would have mass smaller by
that factor (`≈ 2.6·10^7`) — within reach of direct linear algebra. This is *not* a route as it
stands: the Kodaira type at `4547` is not in the packet, and the twist changes the curve, the
`N⁺/N⁻` factorization relative to `K`, and the Gross-point dictionary; all of that would have to be
re-derived before any such computation meant anything about `c₂(p)`.

### D. Impossibility

Not claimed, and none is proved. Per `GATE.md` K5, the content of §3 is that the *methods*
currently available stop where indicated, which is a statement about the state of the literature
and not about what is provable.

---

## 4. Compliance notes

* **K1 (do not assume the target).** No result above, formal or informal, uses `c₂(p) ∈ Z_p^×` or a
  statement equivalent to it as a hypothesis. The two equivalences (M1), (M2) are proved from the
  definitions as pure algebra over `Λ` and over `F_p[G₁]/I³`; they are reformulations offered as
  targets, not as evidence.
* **K3 (do not reopen).** Nothing on the frozen list was reopened; no dependency error in the
  forward bridge was found, and it was not re-audited.
* **K4 (labels).** Every claim above carries one of: *proved here (Lean)*, *cited input*,
  *conditional (on what)*, *unsupported inference*.
* **K6 (scope).** Supersingular primes, the bad primes `2243, 4547, 5843`, `I_3(13)`, and any BSD /
  FIN / FORMULA claim are untouched.

## 5. Successor, stated narrowly

The single statement to attack next, in the form in which it is now exactly equivalent to the
witness:

    for admissible ordinary p,     Σ_{j=0}^{p−1} j² · ψ̄_{f_E}(γ^j P₁)  ≠  0   in F_p,

with `P₁` the traced conductor-`p²` Gross point and `ψ_{f_E}` primitive — a mod-`p` second-moment
nonvanishing at the first layer, equivalently `λ(𝓛_{f_E}) = 2`, equivalently the nonvanishing of
the degree-`(p−3)` coefficient of the interpolating polynomial of the Gross-point packet. The last
form is the one that says most clearly what an analytic route must deliver: control of a single
high-degree mod-`p` coefficient, uniformly in `p`.
