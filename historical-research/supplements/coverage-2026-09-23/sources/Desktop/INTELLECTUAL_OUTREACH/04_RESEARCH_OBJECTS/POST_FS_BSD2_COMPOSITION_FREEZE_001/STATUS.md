# Post-F/S composition — status

Two independent Pro runs received the identical packet and mandate. Both froze a Stage-I
reconstruction before opening Stage II. **Every headline flag agrees.**

```text
                                  PRO_C                     PRO_D
STAGE_I_INDEPENDENCE              PASS                      PASS
ALGEBRAIC_COMPOSITION             PROVED                    PROVED
KERNEL_TERM                       VERIFIED_ORDER_2          VERIFIED_ORDER_2
SEL2_ORDER_FROM_4_1               PROVED                    PROVED
RANK_ZERO_FROM_4_1                PROVED                    PROVED
SHA_2_ZERO                        PROVED                    PROVED
SHA_2PRIMARY_ZERO                 PROVED                    PROVED
FULL_SHA_FINITENESS               PROVED_WITH_EXTERNAL_INPUT PROVED_WITH_EXTERNAL_INPUT
BSD2_COMPOSITION                  BOUNDED_UNIFORM           BOUNDED_UNIFORM
UNIFORM_ANALYTIC_L_VALUE_CONTROL  PARTIAL                   PARTIAL
UNIFORM_TAMAGAWA_CONTROL          YES                       YES
UNIFORM_PERIOD_NORMALIZATION      YES                       YES
ARISTOTLE_ALGEBRAIC_TARGET        READY                     READY
ARISTOTLE_BSD2_TARGET             NOT_READY                 NOT_READY
COUNTEREXAMPLE_FOUND              YES                       YES
```

## Stage-I independence

```text
PRO_C  34072e6fed3f833953a447db6760f3ce907b8f6ea31eedeb4d7237702f0a6b34   12 962 bytes
PRO_D  5c7250caed61cca4d67ae47fc37ee2c3556a5bc8f64d3703a878a6f5badcc61b   17 429 bytes
```

Distinct documents, distinct digests, 4 467 bytes apart. Verified here; see
`receipts/STAGE_I_INDEPENDENCE.txt`.

## Certification level of what they produced

```text
ALGEBRAIC_COMPOSITION = DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF
BSD2_TRANSFER         = CONVENTIONAL_AND_BASE_CONDITIONED
LEAN_CERTIFIED        = NO   (for both — only F and S_dyadic are)
```

**Nothing in this freeze is Lean-certified.** F and `S_dyadic` remain the only formally certified
results; their status does not transfer to anything derived here.

## What is now known, and what is not

**Known — the algebraic composition, on the certified `(4,1)` stratum `H₄₁`:**

    K = E'_q(ℚ)[φ̂] / φ(E_q(ℚ)[2]) = {1, [D]},  order 2   (computed, not assumed)
    Sel₂(E_q) ≃ ⟨[D],[q]⟩ / ⟨[D]⟩ ≃ C₂
    rank E_q(ℚ) = 0,  Ш(E_q)[2] = 0,  Ш(E_q)[2^∞] = 0

**Not known — unconditional BSD(2) from `S_dyadic`.** Both runs: the missing ingredient is no longer
Selmer theory, torsion, Tamagawa valuation, ordinarity or period normalization. It is the **base
analytic datum** — `L(E_base,1) ≠ 0` and `v₂(L(E_base,1)/Ω_R(E_base)) = −2`, plus base optimality.
A base-to-twist transfer theorem exists; whether every `H₄₁` base passes its analytic gate is open.

## The frontier has moved

The unresolved mathematical frontier is now **analytic base control, not the descent.**
