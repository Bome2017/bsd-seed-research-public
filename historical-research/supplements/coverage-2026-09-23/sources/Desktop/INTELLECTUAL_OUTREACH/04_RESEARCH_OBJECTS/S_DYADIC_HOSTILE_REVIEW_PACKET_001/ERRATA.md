# Errata

## E1 — 62a1 twist reduction types were transcribed backwards in an earlier crosswalk

**Where.** `TWO_CURVE_ABSTRACTION_PACKET_001/CASE_CROSSWALK.md`, row 45 ("reduction types feeding
those"), 62a1 column.  That file is **manifested and frozen**; it has **not** been edited, and its
digest is unchanged.  The erroneous cell is recorded here instead.

**What it says (wrong):**

> split `I₄` at 2, nonsplit `I₁` at 31; `I₀*` at `q`

**What the frozen source says (right).**  `run013-62a1-bsd2-2026-08-22/BSD_CHAIN.md` §4, *Local
factors and torsion*, for every `q ∈ F₆₂`, the minimal local data of the **twist** `E_q`:

| place | reduction | local factor |
|---|---|---|
| `2` | **nonsplit** multiplicative `I₄` | `c₂ = 2` |
| `31` | **split** multiplicative `I₁` | `c₃₁ = 1` |
| `q` | additive `I₀*` | `c_q = 2` |

with the stated reasons: *"`q ≡ 5 mod 8` is the unramified nonsquare class in `Q₂`; it twists split
`I₄` to nonsplit `I₄`. `(q/31) = −1` twists nonsplit `I₁` at `31` to split `I₁`."*

**Cause.** The base curve 62a1 has split `I₄` at 2 and nonsplit `I₁` at 31.  The row was about the
**twist**, and the base-curve values were transcribed into it.  Twisting by `q ≡ 5 (mod 8)` with
`(q/31) = −1` flips both.

**Effect on the Tamagawa numbers: none.**  `(c₂, c₃₁, c_q) = (2, 1, 2)`, product 4, in both the
correct and the transcribed reading — which is why the error did not propagate into any conclusion.
Crosswalk row 44 (Tamagawa factors) is correct as written.

**Instruction to the referee.**  Where the crosswalk and a frozen source disagree, **use the frozen
source**.  For 62a1 local factors that is
`03_frozen_cases/62a1/exact_model_and_local_data/BSD_CHAIN_local_factors_source.md` §4.

*Found by the extraction Pro.  Recorded, not silently repaired.*

---

## E2 — the extraction report named in the packaging mandate does not exist

The mandate asked for "the full Pro extraction report ... beginning with
`FINITE_FIELD_GENERALIZATION = PROVED` / `FINITE_FIELD_PRIOR_ART = STANDARD/KNOWN` /
`SELMER_GENERALIZATION = NONTRIVIAL_UNIFORM_THEOREM`".

**No such file is present in `~/Downloads`.**  Every `.md` there was searched for the strings
`FINITE_FIELD_GENERALIZATION` and `SELMER_GENERALIZATION`; zero matches.  The same search failed
during the earlier Aristotle packaging pass.

`06_provenance/extraction_report.md` records the absence rather than reconstructing the report from
memory.  Nothing is lost for the review: `BOUNDED_DYADIC_SELMER_THEOREM.md` is self-contained,
carrying its own hypotheses, conclusions, full local proof, both specializations, the boundary
example and its own scope boundary.  In any case the mandate says the report's verdict is **not**
evidence.
