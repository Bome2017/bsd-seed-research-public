# Errata carried into this packet

## E1 — 62a1 twist reduction types, in the frozen crosswalk

`stage_II/06_crosswalk_and_errata/CASE_CROSSWALK_original_frozen.md`, **row 45**, 62a1 column, reads

> split `I₄` at 2, nonsplit `I₁` at 31; `I₀*` at `q`

**That is backwards.** It transcribes the *base curve*'s reduction types into a row about the
*twist*. The frozen source is authoritative — `stage_I/02_case_62a1/BSD_CHAIN.md` §4, *Local factors
and torsion*, for every `q ∈ F₆₂`:

| place | reduction | local factor |
|---|---|---|
| `2` | **nonsplit** multiplicative `I₄` | `c₂ = 2` |
| `31` | **split** multiplicative `I₁` | `c₃₁ = 1` |
| `q` | additive `I₀*` | `c_q = 2` |

with the stated reasons: `q ≡ 5 (mod 8)` is the unramified nonsquare class in `ℚ₂` and twists split
`I₄` to nonsplit `I₄`; `(q/31) = −1` twists nonsplit `I₁` to split `I₁`.

**Effect on Part B: none numerically.** `(c₂, c₃₁, c_q) = (2, 1, 2)`, product 4, either way — which
is why the error never propagated into a conclusion. Crosswalk row 44 (Tamagawa factors) is correct.

**Effect on Part B's reasoning: potentially real.** If you are looking for a *uniform* Tamagawa
argument across the family, the split/nonsplit behaviour is exactly the kind of thing that must be
tracked correctly, even when the valuation happens to coincide. Use the source, not the cell.

**The crosswalk is included unedited on purpose.** Correcting a frozen, manifested artifact in place
would destroy its custody value. Where crosswalk and frozen source disagree, **the frozen source
governs**.

## E2 — the F extraction report named in an earlier mandate does not exist

An earlier packaging mandate referred to a Pro extraction report headed
`FINITE_FIELD_GENERALIZATION = PROVED`. No such file was ever found on this machine; `~/Downloads`
was searched twice for that string and for `SELMER_GENERALIZATION`, with zero matches. It is not in
this packet and was never reconstructed from memory. Nothing depends on it.
