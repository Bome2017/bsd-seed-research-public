# Theorem F — formalization status

```text
THEOREM_F                       = LEAN_CERTIFIED
INDEPENDENTLY_REPLICATED        = YES (two Aristotle proof-search runs)
PRIMARY_IMPLEMENTATION          = 01_primary_proof_B   (Run B, 9 modules, 897 lines)
ALTERNATE_IMPLEMENTATION        = 02_alternate_proof_A (Run A, 6 modules, 789 lines)
TARGET_STATEMENT_IDENTICAL      = YES (byte-identical in V1, A and B)
AFFINE_COUNT_BRIDGE_PROVED      = YES in both (not assumed)
SORRY / ADMIT / CUSTOM_AXIOMS   = 0 / 0 / 0 in both
AXIOMS                          = {propext, Classical.choice, Quot.sound} in both
INDEPENDENT_REBUILD_HERE        = PASS for both
```

Valid for **all finite fields of odd characteristic**, including characteristic 3 and non-prime
fields.

## The qualification that stays in the permanent record

"Independent" here means **two independent Aristotle proof-search runs**. Both use the same Lean
kernel and the same mathlib revision, and both were given the same theorem input. This is therefore
**not independent proof-assistant verification**.

It is nonetheless considerably stronger than two language models agreeing: two materially different
Lean developments were each checked by the kernel, and the kernel does not care which model wrote
them.

## Prior art — unchanged

The theorem is classical: Miret–Moreno–Rio–Valls, *Determining the 2-Sylow subgroup of an elliptic
curve over a finite field*, Math. Comp. **74** (2005), 411–427, Proposition 1 §3.1, p. 416. The
target is its order-four specialisation plus elementary finite-group structure. **No novelty is
claimed.** The value is the kernel-checked proof and the reusable infrastructure.

## Environment (both runs)

```text
Lean     leanprover/lean4:v4.28.0
mathlib  8f9d9cff6bd728b17a24e163c9402775d9e6a365
```
