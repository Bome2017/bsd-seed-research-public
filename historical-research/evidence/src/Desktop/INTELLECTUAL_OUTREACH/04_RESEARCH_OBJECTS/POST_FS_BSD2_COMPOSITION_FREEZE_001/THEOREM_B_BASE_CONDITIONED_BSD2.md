# Theorem B — base-conditioned BSD(2) transfer

```text
BSD2_COMPOSITION = BOUNDED_UNIFORM
UNCONDITIONAL_FROM_S_DYADIC = NO
LEAN_CERTIFIED = NO
ARISTOTLE_BSD2_TARGET = NOT_READY
```

**Deliberately kept separate from Theorem A.** It is conventional, literature-dependent, and gated
on a base-curve analytic hypothesis that is not known to hold across `H₄₁`.

## What is uniform

Both runs, independently:

| quantity | status on the `S_dyadic` family |
|---|---|
| `c = Σ_ℓ v₂(c_ℓ) = 2` | **uniform** — at 2 nonsplit `I_{4m−8}`, `c₂ = 2`; at odd `ℓ \| D`, `I_{v_ℓ(D)}` with odd factor; at `q`, `I₀*`, `c_q = 2` |
| `τ = v₂(\|E_q(ℚ)_tors\|) = 1` | **uniform** — `E_q(ℚ)_tors ≃ C₂`, `E'_q(ℚ)_tors ≃ C₂²` |
| period normalization `Ω_R = c_∞ Ω⁺` | **uniform**, and kept distinct from `ω_desc = ½ ω_min` |
| `rank = 0`, `Ш[2^∞] = 0` | **uniform on `H₄₁`**, from Theorem A |
| ordinarity / `v₂(N_q) = 2`, `a_q ≡ 2 (mod 8)` | **uniform on `H₄₁`** — there `m` is odd, so `(r/q) = −1`, and with `(D/q) = −1` certified **F** supplies it |

**Caution recorded by both:** the **complete** Tamagawa product is *not* uniform — `r = −128`,
`D = 513 = 3³·19`, `q = 5` gives `(2,3,1,2)`, product 12 — but `v₂(∏c_ℓ) = 2` still holds. The
invariant BSD(2) needs is uniform; the product is not.

## What is not uniform — the whole remaining gap

    L(E_base, 1) ≠ 0
    v₂( L(E_base,1) / Ω_R(E_base) ) = −2
    base optimality normalization

**The missing ingredient is no longer Selmer theory, torsion, Tamagawa valuation, ordinarity or
period normalization. It is the base analytic datum.**

## The transfer theorem

*If* a base satisfies the analytic gate above, the relevant Zhai theorem gives

    v₂( L(E_q,1) / Ω_R(E_q) ) = 0

and with `c = 2`, `τ = 1`, `Ш[2^∞] = 0` from Theorem A,

    a = c − 2τ = 2 − 2 = 0

so BSD(2) holds for the twist. **A genuine base-to-twist BSD(2) transfer theorem exists.**

What is **not** known is whether every `H₄₁` base passes the gate. Until that is settled:

    Do not promote S_dyadic to unconditional BSD(2).

## Why this is not an Aristotle target

Both runs: `ARISTOTLE_BSD2_TARGET = NOT_READY`. The analytic gate is external and base-specific, and
no `H¹`, rank, Ш or BSD object exists in the certified formal boundary. Formalizing this now would
mean formalizing the wrong abstraction.
