# SUPERSESSION — read before the other two files in this directory

`TASK.md`, `GATE.md` and `INPUTS.md` at the top level are **authoritative**. The two files below are historical
records copied for provenance. Where they give instructions or state open items, the following supersede them.

## `BRANCH_THETA.md`

| where | historical text | superseded by |
|---|---|---|
| l.78 | "Hold this Aristotle while the other finishes." | **Void.** This run is the current task. |
| §5 | H1 (the three-term relation) "carried as an explicit hypothesis", needing a source audit with exact conventions | The witness is now **bound directly to BLV's construction** (`INPUTS.md` §4): BLV's own `calL_{g,n}`, surjective `ψ_g`, traced Gross points. Do not route through another paper's relation. |
| §3 | the witness written as `Σ_σ c_2(σ) φ_E(x_{p^n}(σ))` "for some n" | **Superseded** by the precise definition in `INPUTS.md` §4: first layer `K_1`, traced Gross points of **conductor `p^2`**, primitive `ψ_g`. |
| §6 | the successor "attack the finite-layer Gross-point sum through its distribution relations" | Folded into route class A of `TASK.md`; not a separate instruction. |

## `ORDINARY_LANE_FREEZE.md`

| where | historical text | superseded by |
|---|---|---|
| §2, §5 | BLV↔BD module identification, BD 2.18(5)/2.23/Lemma 3.1, odd-`p` descent marked "not replayed by the project" / resting on two audits | **Independently source-audited** by an external read-only review, 2026-09-22: forward bridge intact. Conditional prime by prime. **Not Lean-verified.** |

## Anywhere

Any statement that `c_2(p)` lives on "conductor-`p`" Gross points is **wrong**: the first layer uses conductor `p^2`.
Any statement of a converse to the bridge without `rho_p = 4` is **withdrawn** (`INPUTS.md` §2).
