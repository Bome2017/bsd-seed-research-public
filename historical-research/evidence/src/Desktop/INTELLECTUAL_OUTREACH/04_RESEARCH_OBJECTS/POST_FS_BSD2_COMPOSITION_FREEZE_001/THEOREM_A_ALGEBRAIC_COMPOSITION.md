# Theorem A — the bounded algebraic composition

```text
STATUS = DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF
LEAN_CERTIFIED = NO
```

Conventional mathematics, independently reconstructed by two Pro runs before either saw the other's
work. **Not formalized.** The authoritative texts are the two Stage-I reconstructions and the two
final reports in `01_pro_C/` and `02_pro_D/`; this page is a distillation and they govern.

## Hypothesis `H₄₁`

Inside `S_dyadic`'s hypotheses (`Params`), restrict to the certified `(4,1)` stratum:

    H₄₁ :   (D < 0  and  s = 1)   or   (D > 0  and  s = 2  and  ℓ₁ ≡ ℓ₂ ≡ 3 (mod 4))

On `H₄₁`, certified `S_dyadic` supplies

    Sel^φ  = {1, [D], [q], [Dq]}        Sel^φ̂ = {1}

## Theorem A

On `H₄₁`:

    K = E'_q(ℚ)[φ̂] / φ(E_q(ℚ)[2]) = {1, [D]},   of order 2
    Sel₂(E_q) ≃ ⟨[D],[q]⟩ / ⟨[D]⟩ ≃ C₂
    rank E_q(ℚ) = 0
    Ш(E_q)[2] = 0
    Ш(E_q)[2^∞] = 0

From `0 → E_q(ℚ)/2E_q(ℚ) → Sel₂(E_q) → Ш(E_q)[2] → 0` and `|E_q(ℚ)[2]| = 2`:

    2 = 2^{rank E_q + 1} · |Ш(E_q)[2]|

so rank 0 and `Ш[2] = 0` follow **jointly**. Then `Ш[2^∞] = 0` by the elementary order argument.

## Four statements that must never be conflated

    Ш[2] = 0          proved on H₄₁
    Ш[2^∞] = 0        proved on H₄₁, without finiteness
    Ш finite          NOT proved here; requires external input
    Ш = 0             NOT proved, and not claimed

`FULL_SHA_FINITENESS = PROVED_WITH_EXTERNAL_INPUT` in both reports — the external input is cited
there, not supplied here.

**And: `rank = 0 ⟹ Ш[2] = 0` is false on its own.** Both runs flagged this. The two conclusions come
out of the order equation together; neither implies the other.

## The refinement neither was asked for

For an arbitrary rational degree-2 isogeny with **actual** Selmer shape `(4,1)`, if
`t = |E(ℚ)[2]| ∈ {2,4}` then

    |Sel₂(E)| = t

So the unique-rational-2-torsion hypothesis is needed specifically for `|Sel₂| = 2`; **rank 0 and
`Ш[2] = 0` hold in either case.** Both runs found this independently.

## Two boundaries that make the hypotheses load-bearing

**`(4,1)` alone does not give `|Sel₂| = 2`.** `E : y² = x(x−1)(x−9)` has full rational 2-torsion,
actual shape `(4,1)`, and `|K| = 1`, `|Sel₂| = 4`.

**`H₄₁` cannot be dropped from `S_dyadic`.** At `r = 128`, `D = −511 = −7·73`, `q = 29` — inside
`S_dyadic`, outside `H₄₁` — the certified shape is `(8,1)` and an explicit non-torsion point exists.
Rank is not zero. **"S implies rank zero" is false.**

## Position in the literature

Both runs were asked whether this is standard exact-sequence infrastructure, a useful
specialization, or stronger. See their reports; **no novelty is claimed here**, and the prior-art
blocker from the 66b1 work (`PRIOR_ART_BLOCKER = UNRESOLVED`, BSTW Theorem 1.7 explicitly listing
66b1) is unchanged.
