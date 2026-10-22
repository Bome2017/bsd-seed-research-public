# Lean replay: A3 bridge algebraic core (§§2–4)

Date 2026-09-22. File: `A3Core.lean` (765 lines, sha256 `f7a3c861c998f99630a46a9c988e41554ef630d46fdfbbe7f90383a4bf7f24ca`).
Object: `~/BSD_SUPERSINGULAR_SIGNED_BRIDGE_2026-09-22/SIGNED_MINIMAL_LAMBDA_BRIDGE.md` §§2–4 (sha `ed44d90d…`).

## Result: BUILD PASS, sorry-free, standard axioms only

    replay:   cd ~/proximity-prize && lake env lean ~/BSD_A3_LEAN_CORE_2026-09-22/A3Core.lean
    Lean 4.32.2 (commit f3b06c70…), Mathlib 905b95818eb32af7874a58b427f50c1711a5e96c (tag v4.32.2)
    exit 0; 0 errors; 0 warnings (build6.log, sha 07ec913c…)
    no `sorry` / `admit` / `native_decide` / `axiom` in the source
    every theorem: [propext, Classical.choice, Quot.sound]

The environment is the pre-built Mathlib in `~/proximity-prize`. That project was only read, never modified.
Earlier failed iterations are kept in `iterations/`.

**First failed algebraic implication: NONE.**

## What is machine-checked

| bridge step | Lean theorem | content |
|---|---|---|
| §2 | `torsion_eq_bot_of_exact_lengths`, `free_of_rank_of_exact_lengths` | Suppose `#(X/(T−a)X) = #(Y/(T−a)Y) = p^e`, `T−a` is injective on `Y = X/tors`, and `(T−a)` is topologically nilpotent. Then `tors X = 0`, and `X ≅ ℤ_p^{2d}`. The proof uses the exact sequence `0 → H/φH → X/φX → Y/φY → 0`, counting, `H ⊆ φ^n H ⊆ pX ∩ H = pH`, and Nakayama over ℤ_p. |
| §3 | `finrank_ker_ibar`, `finrank_coker_ibar`, `finrank_eq_of_graded_presentation` | Graded snake lemma: `ker(ī⁻) ≅ W[U]⁺` and `coker(ī⁻) ≅ W⁻/U(W⁺)`. So `dim ker ī⁻ = dim coker ī⁻` forces `dim W⁺ = dim W⁻`. |
| §3 sign twist | `range_inf_minus_eq_map_plus`, `range_uPlusK`, `minusOfQuotientEquiv'` | `(F ⧸ uF)⁻ ≅ F⁻ ⧸ u(F⁺)`, which makes the graded source and target of `ī⁻` the actual τ-eigenspaces. |
| §3 over ℤ_p | `isCompl_plus_minus`, `finrank_plus_add_minus`, `finrank_plus_eq_minus_of_presentation` | `X = X⁺ ⊕ X⁻` (2 is a unit); `X/pX = 𝕜⊗X⁺ ⊕ 𝕜⊗X⁻`; base change transfers the balance to `rank X⁺ = rank X⁻`. |
| §4 | `plusToSelQ_surjective`, `two_le_finrank_plus`, `sha_dual_eq_bot_of_finrank_plus_eq_two` | `X⁺ ↠ Sel(E/Q)^∨ ↠ ℤ_p²`, which gives `d ≥ 2`. If `d = 2`, Orzech makes the composite injective, so `Ш(E/Q)[p^∞]^∨ = 0`. |
| M₁ | `coeff_one_eq_zero_of_two_le_order`, `M1_eq_zero`, `order_eq_two` | `ord ≥ 2 ⇒ b̄₁ = 0`, hence `M₁ = 0` given the normalization `b̄₁ = Σ j v_j`. Also `b̄₀ = b̄₁ = 0, b̄₂ ≠ 0 ⇒ ord = 2`. |
| capstone | `A3_bridge_core` | The chain in one statement: `X ≅ ℤ_p^{2d}`; `rank X⁺ = rank X⁻ = d`; `d ≥ 2`; `d = 2 ⇒ Ш^∨ = 0`; `b̄₁ = 0`; `M₁ = 0`; `b̄₂ ≠ 0 ⇒ Ш^∨ = 0`. |

## Hypothesis ledger (every assumption the capstone takes)

**Arithmetic inputs, source-checked against BLV v2 in `~/BSD_SUPERSINGULAR_SIGNED_BRIDGE_REVIEW_2026-09-22/REVIEW.md`:**
* **(I1) control:** `c : X ↠ Sel(E/K)^∨` with `c∘τ = σ∘c`, and `ρ : (Sel(E/K)^∨)⁺ ≅ Sel(E/Q)^∨` (restriction/corestriction, p odd).
* **(I2) exact length at one character:** `hexact`.
* **(I3) graded free presentation of `X/pX` and the base-layer eigenspace equality:** the maps `iA iB πA πB u1 u0`, with `hexA hexB hπA hπB hiB hu0 h1 hcomm2 harith`.
* **(I4) `rank E(Q) = 2`:** `κ : Sel(E/Q)^∨ ↠ ℤ_p²`, where `ker κ = Ш(E/Q)[p^∞]^∨`.

**Structural Λ-module inputs (standard Iwasawa algebra, not arithmetic):**
* **(S1)** `X` is finitely generated over ℤ_p (μ = 0).
* **(S2)** `rank(X/tors) = 2d` and `ord_T F̄ = d`. Both encode `λ(char X) = 2λ(F⁻) = 2d` via BLV Thm 7.3.
* **(S3)** `(T−a)^n X ⊆ pX`.
* **(S4)** `T−a` is injective on `Y` and `#(Y/(T−a)Y) = p^e`: the characteristic ideal evaluated at `a` (Thm 7.3 plus det = index for ℤ_p-lattices).

**Modeling steps, stated here and not formalized:**
* **(M1)** The τ-equivariant presentation is entered through its ± components. The identification `(F/uF)⁻ = F⁻/u(F⁺)` **is** formalized. Not formalized: exactness of the eigenspace functor for the base-layer kernel and cokernel (`K⁻ = ker ī⁻`, `C⁻ = coker ī⁻`), and `(X/pX)^± = 𝕜 ⊗ X^±`. Both are standard for `char ≠ 2`.
* **(M2)** `Ш^∨ = 0 ⇒ Ш = 0` (Pontryagin duality).

## What the formalization sharpened

1. **§4 uses (I1) only through surjectivity and τ-compatibility of `X → Sel(E/K)^∨`.** The exact kernel `uX` is never used.
2. **§3 needs only the MINUS-part equality** `dim K⁻ = dim C⁻` of (I3). The plus-part equality is not used.
3. **The hypothesis `F̄ ≠ 0` (μ = 0) was redundant** once `ord_T F̄ = d` with `d` finite, and it was removed. Lean flagged it as unused.

## Not formalized (by design)

BLV, signed Selmer theory, Gross points, the witness `M₂`, and the group-algebra normalization `b̄₂ = M₂/2`
(handled elsewhere). No nonvanishing statement at any prime is claimed.
