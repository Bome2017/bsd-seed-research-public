# Reconciliation of the two independent Pro returns

This document compares the two returns. It does **not** merge them. Where they
differ, both readings are recorded with their source lines and neither is
rewritten to match the other.

Line references are to the files as frozen in `01_pro_1/` and `02_pro_2/`.

---

## 1. Independence

Each report names the SHA-256 of its own pre-comparison reconstruction, written
and hashed before Stage-II access. Both were recomputed here from the delivered
file rather than transcribed:

| run | claimed | computed | |
|---|---|---|---|
| PRO_1 | `711278fc2cfc3322423279c15340c17b7b28a38b2fe85c114f31d9a1f3283600` | same | MATCH |
| PRO_2 | `24527fb717de2daeaa9873f8b13f49b23503faa1dcf1f47fc816fdc9d98b6881` | same | MATCH |

The two documents are distinct. PRO_1 additionally shipped a composite
`FINAL_REFEREE_REPORT.md`; its embedded Stage-I span was extracted and diffed
against the standalone frozen file — the only difference is four trailing
separator lines, zero content lines. PRO_1's "not edited after freezing" claim
therefore holds mechanically. Receipt: `receipts/STAGE_I_INDEPENDENCE.txt`.

**Limit, stated plainly.** These checks show the two delivered reconstructions are
distinct files with correct self-reported digests. They do not prove the two runs
were causally isolated from one another. That rests on the operator's run
discipline, not on anything verifiable from the artifacts.

---

## 2. The headline blocks agree on every enumerated value

Both blocks carry the same 14 keys in the same order. **12 of 14 values are
byte-identical.** The two that differ — `WHERE_THE_COST_SITS` and
`NEXT_DISPOSITION` — are free-text fields, and both name the same three cost
centres and the same next target in different words.

Receipt: `receipts/HEADLINE_DIFF.txt`.

This is the substantive convergence finding. It is stronger than "the two
referees reached the same conclusion": every discrete verdict token they were
asked to emit came out the same, including the ones that could most easily have
diverged (`EXPLICIT_ROUTE_WITHOUT_H1 = PARTIAL`, `ABSTRACT_SEQUENCE_PLUS_MAP =
RIGHT_SHAPE`, and all three `LARGE_DEVELOPMENT` bridge rows).

### One row that must not be lost

Both reports say `MATHLIB_SELMER_OBJECT = PRESENT`. Read alone that row is
dangerous. Both immediately disambiguate it:

- PRO_1 (`FINAL_REFEREE_REPORT.md:42-46`) adds an extra row,
  `MATHLIB_ELLIPTIC_SELMER_OBJECT = ABSENT`, and states that PRESENT means the
  Dedekind-domain object `K(S,n)`, "**not** an elliptic-curve Selmer group".
- PRO_2 (`REFEREE_REPORT.md:42`) says the same: "The headline's **Selmer PRESENT**
  denotes `IsDedekindDomain.selmerGroup`, the multiplicative valuation group
  K(S,n), not elliptic Selmer. ... The actual elliptic Selmer object was not located."

Local verification confirms it: at the pin, "Selmer" occurs in exactly three
files, none of them under `Mathlib/AlgebraicGeometry/EllipticCurve/`, and two of
those three are about Selmer *trinomials*.

---

## 3. Where the two reports genuinely differ

Four real differences. None is a contradiction; three are refinements and one is
a scope choice.

### 3.1 The rank countermodel — PRO_2's is strictly stronger

| | model | what it refutes |
|---|---|---|
| PRO_1 (`:293-304`) | `G = C₂ ⊕ ℚ` | `G/2G ≅ C₂` **and** `G[2] ≅ C₂` ⇏ rank 0 |
| PRO_2 (`:99-103`) | `L = ℤ[1/2]`, `U = L⊕C₂`, `V = L⊕C₂⊕C₂`, `f(x,t)=(x,0,0)`, `g(x,u,v)=(2x,u)` | the **whole four-term interface** ⇏ rank 0 |

Both were verified here (`receipts/INDEPENDENT_MATH_CHECKS.txt`, checks 5–15).
PRO_2's model satisfies *every* index the proposed bridge would read off —
`g∘f = [2]`, `f∘g = [2]`, both kernels of order 2, `|V/f(U)| = 4`, `U/g(V) = 0`,
`U/2U ≅ C₂` — and even satisfies the four-term index identity (`4 = 4`), while
`U` still has rational rank 1. It is a countermodel *inside* the sequence, not one
that violates it.

**Consequence.** `RANK_REQUIRES_SEPARATE_FG_OR_HEIGHT_GATE = YES` is not caution.
A formal bridge stated at that interface without the finite-generation premise
would be false. Use PRO_2's model as the regression test.

### 3.2 Next-theorem scope: general field K vs ℚ

- PRO_1 (`:305-334`) states the target over a **characteristic-zero field K**, with
  `C_K = K×/(K×)²`, and adds field-embedding naturality as the next small target.
- PRO_2 (`ARISTOTLE_TASK.md`) specialises the first implementation to **ℚ**, using
  the existing `Run013.Qsq` directly, and defers naturality.

Both are the same theorem; they differ on where to start. The operator has chosen
PRO_2's rational version as primary. PRO_1's generic-K form is preserved verbatim
in `01_pro_1/` and recorded in `NEXT_ARISTOTLE_TARGET.md` as the immediate
follow-on, not as a discarded alternative.

### 3.3 Blocked-shortcut bookkeeping

PRO_1 carries 3 BLOCKED items as graph nodes (26, 27, 28). PRO_2 carries 4 in a
separate `blocked_shortcuts` list and uses no BLOCKED node class. Three pair up by
content. PRO_2's fourth — "Replace absolute H¹ by H¹ of the coefficient splitting
field" — has no PRO_1 *node*, but PRO_1 states the identical prohibition in prose
at `FINAL_REFEREE_REPORT.md` §4.3 (line 181). The prohibition is common; only its placement differs.

Receipt: `receipts/DEPENDENCY_GRAPH_AUDIT.txt`.

### 3.4 Graph granularity

28 nodes vs 34. Not a disagreement: PRO_2 subdivides the continuous-cohomology
obligation more finely and enumerates 7 `ALREADY_IN_MATHLIB` ingredients where
PRO_1 aggregates 2. Both graphs parse, are **acyclic**, are topologically ordered,
and have no unresolved dependency tokens (PRO_1's `C` is a declared external
input, not a dangling edge).

---

## 4. Refinements PRO_2 contributes that PRO_1 does not state as sharply

Recorded as PRO_2's, not promoted to joint findings.

**Sel₂ does not require Ш first.** (`REFEREE_REPORT.md:89-93`) Genuine `Sel₂` can be
built from continuous H¹ of the *finite* kernel module `E[2]` together with local
point-Kummer images, without first constructing `H¹(ℚ, E(ℚ̄))`. Genuine Ш cannot:
it is the kernel of `H¹_cont(G_ℚ, E(ℚ̄)) → ∏_v H¹_cont(G_{ℚ_v}, E(ℚ̄_v))`, and that
coefficient module is **infinite**. A finite-coefficient-only development may not
be called Ш. PRO_1 reaches the same separation through its graph (nodes 17–20 vs
node 22) but does not isolate the coefficient-module reason as crisply.

**The correction term is `E′[ψ]/φ(E[2])`, not `E′[2]`.** (`:73`) Its squareclass
image is `⟨[D]⟩`, a two-element group — *not* the four-element
`{1,[D],[q],[Dq]}`. PRO_1 agrees (`STAGE_II_COMPARISON.md:35-41`) and both note the
prior Pro C/D reports already had this right. This is a concrete regression test
for any future implementation.

**Ш may fall before rank.** Both agree, and it is worth stating as the headline
surprise. Once the actual Kummer sequences exist, certified saturation gives
`Ш(E)[φ] = 0` and `Ш(E′)[ψ] = 0`; since the induced maps compose to multiplication
by 2, `Ш(E)[2] = 0` follows **without** Mordell–Weil, and the elementary induction
`2x=0 ⇒ x=0` ⟹ `2ⁿx=0 ⇒ x=0` gives `Ш(E)[2^∞] = 0` **without** finiteness of Ш.
PRO_1: `:287-292` and node 19. PRO_2: `:111`.

So the expected formal order is: **actual point quotient → Ш[2^∞]=0 → possibly
Sel₂**, with **rank last**, waiting on heights or finite generation. Neither
referee predicted this before doing the dependency analysis, and it inverts the
ordering the project had assumed.

---

## 5. What neither report supplies

Neither supplies a missing arithmetic object, a mathlib theorem, or any Lean. Both
say so explicitly. Both also state that the prior Pro C/D reports' correctness is
**not** evidence that the new bridge is cheap (PRO_2 `:129`), and that recommending
the now-certified saturation target again would fail to advance the boundary
(PRO_1 `:382-387`, PRO_2 `:17`).

Neither re-reviewed F, `S_dyadic`, saturation, or Theorem A. Neither opened the
analytic branch. Both confirm the certified inputs were accepted at their stated
boundaries only.

---

## 6. Evidence tier of the negative findings

Both referees state clearly that they had no local mathlib checkout and that their
negative availability flags are **static exact-pin surveys, not machine-exhaustive
absence proofs** (PRO_1 `:64`, PRO_2 `:40`). That caveat is preserved and is
restated in `SURVEY_EVIDENCE_BOUNDARY.md`.

A local checkout at exactly `8f9d9cff6bd728b17a24e163c9402775d9e6a365` was
available on this machine, so the surveys were re-run mechanically. The result
**raises the tier of the negative findings without changing any verdict**:

- `isogeny` — **0 occurrences** anywhere in mathlib at the pin.
- Ш under every spelling tried (`shafarevich`, `Sha`, `Ш`, …) — **0 occurrences**.
- `mordell`, `canonicalHeight`, `néron` — **0 occurrences**.
- `Selmer` — 3 files, none elliptic.
- All 16 PRO_1 source paths and all 19 PRO_2 source paths — **present**.
- PRO_1's `ContinuousCohomology` TODO characterisation — **verbatim correct**.
- PRO_2's Hilbert-90 `[FiniteDimensional K L]` scope claim — **correct**.
- `Group.rank` is `Nat.find` over `fg_iff'` — **min generators, confirmed**, so
  PRO_1's `BLOCKED` classification of it is right.

Receipt: `receipts/PINNED_MATHLIB_LOCAL_VERIFICATION.txt`. One citation defect was
found and is carried as an erratum, not repaired (`ERRATA.md` E2).

---

## 7. Disposition

`NO_CHEAP_BRIDGE` stands, from two independent reviews, with a bounded successor.
The two-Pro experiment on this question is complete. The next object is a Lean
handoff for the actual coordinate descent homomorphism, specified in
`NEXT_ARISTOTLE_TARGET.md`.
