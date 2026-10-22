# P04C_TWO_DESCENT_QUOTIENT_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`
`PROGRAMME_STATUS = H¹-FREE BRIDGE COMPLETE — THE CHAIN STOPS HERE BY DECISION, NOT BY FAILURE`

```text
P04C_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8056 jobs, TwoDescent.lean 346 lines, 15 helper lemmas added)
RUN_B = CLEAN   (8056 jobs, TwoDescent.lean 370 lines, 17 helper lemmas added)

INPUT_IDENTITY              = BYTE_IDENTICAL   (both given d2f77d12…ac2f3708)
TARGET_STATEMENT_IDENTITY   = BYTE_IDENTICAL   (4f28de06… in all three copies)
SHIPPED_PLUMBING_IDENTITY   = BYTE_IDENTICAL   (dblHom/twoE/mem_twoE/KExp_le_GphiExp, 5060c0ac…)
INHERITED_SOURCES_UNTOUCHED = 30/30 byte-identical in both runs
SHARED_HELPER_NAMES         = 2   (second lowest of any stage — and it means nothing here)
ROLE-MATCHED HELPERS        = 11  of 15 / 17
CITATION PROFILE            = NEARLY IDENTICAL (one count differs)
DEPENDENCY FOOTPRINT        = IDENTICAL on every headline constant

PROHIBITED_CONSTRUCTS   = 0  (both)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both)
SORRYAX                 = ABSENT
FINITENESS ASSUMED      = NONE — Fintype and Finite are 0 in code in both returns

REPLICATION_STRENGTH = CONFIRMATION-GRADE, with independent scaffolding
WRAPPER_DEFECTS      = both stale metadata (51/53); fourteenth and fifteenth occurrences
```

## What is certified

For the certified family — `r = ε·2^m`, `m ≥ 3`, `ε = ±1`, `q` prime with `q ≡ 5 (mod 8)`,
`q ∤ 2D`, `(D/q) = −1`, odd valuations, on the stratum `H₄₁` — and for
`E_q : y² = x(x² + Aqx + r²q²)` as mathlib's **actual** `WeierstrassCurve.Affine.Point` group:

    E_q(ℚ) / 2E_q(ℚ)  ≃+  Additive (G_{φ,exp} ⧸ K_exp)

    Nat.card (E_q(ℚ) / 2E_q(ℚ)) = 2

    E_q(ℚ) / 2E_q(ℚ)  ≃+  ZMod 2

together with the point-cokernel exact sequence that produces them: `φ̂` induces a **surjection**
`E'_q(ℚ) ⧸ φ(E_q(ℚ)) →+ E_q(ℚ) ⧸ 2E_q(ℚ)`, pinned to be `⟦P'⟧ ↦ ⟦φ̂(P')⟧`, with kernel exactly
the image of `ker φ̂`.

**This is the endpoint of the H¹-free bridge the two hostile Pro audits prescribed.** It is not
a renamed intermediate goal; the programme stops here by decision.

## What it does NOT say — read before quoting it

* **It does not say `rank E_q(ℚ) = 0`.** An abstract abelian group can satisfy `G/2G ≅ C₂`
  without being finitely generated. Getting to the rank needs Mordell–Weil, which is **not** in
  this development. The construct scan confirms no `Finite` or `Fintype` hypothesis exists in
  code anywhere in either return.
* **It does not say `E_q(ℚ)` is finite.** `Nat.card` of the quotient being 2 says nothing about
  the group.
* **It is not `Sel₂`.** `S_dyadic`, `Run013.SelmerSet`, `GphiExp` and `KExp` are explicit
  descent-realization objects defined by solubility of quartic coverings. None is
  `H¹(ℚ, E[φ])`.
* **It is not Ш, not `Ш[2^∞]`, and it does not touch `L(E,s)`.** `touches_L_function = NO`
  stands unchanged.
* **It is not a mathlib `Isogeny`.** The pinned mathlib has no isogeny API; the maps were built
  by hand.

## The replication, measured three ways — and the name count is worthless here

Two shared helper names, the second lowest of any stage. It means nothing: P04c is
**confirmation-grade**.

1. **Both runs found the same route, and it is not the route that was verified before sending.**
   The pre-ship reachability proof transported the result along `P04a.isogeny_cokernels` with
   `QuotientAddGroup.congr`. Neither run did that. Both instead built two surjections out of
   `E'_q(ℚ)` — one to `E_q(ℚ)/2E_q(ℚ)`, one to `GphiExp/KExp` — proved they have the **same
   kernel**, and concluded both quotients are isomorphic to `E'_q(ℚ)` modulo that kernel.
   `E'_q(ℚ) ⧸ φ(E_q(ℚ))` never appears as an intermediate object in either proof. Eleven helper
   roles match one-to-one under that correspondence.
2. **Citation profiles are nearly identical** — every certified input consumed the same number
   of times on both sides except `mem_twoE` (4 vs 7). The opposite of P04b.
3. **Transitive dependency footprints are identical** on every headline constant
   (`receipts/DEPENDENCY_FOOTPRINT.txt`), computed by a Lean elaborator that walks the whole
   proof term rather than by grep.

Two independent searches landing on the same route the sender had not anticipated, with the same
dependency footprint, is meaningful — it says the route is the natural one for this statement.
It is not architectural divergence, and must not be reported as such.

## Three findings from the dependency footprint

* **`P04a.isogeny_cokernels` is not a dependency of the final theorem.** Thirteen P04a
  constants are — `deltaHomE`, `deltaHomE'` and their simp lemmas. P04a built the cokernel
  objects and certified what they are; the final theorem reaches `E/2E` without quoting it.
  P04a is load-bearing for the programme, not for this proof term.
* **`P01.p01_family_two_torsion` is not a dependency**; its component `P01.Ecurve_two_torsion`
  is.
* **`P04c.KExp_le_GphiExp`, supplied proved in the handoff by Claude, was used by neither run.**
  It earned its place in making the statement's `subgroupOf` unambiguous and nowhere else.

## What the cross-run probe adds

One probe, byte-identical, naming no run-specific helper. In **both** developments:
`Nat.card = 2` and an explicit `≃+ ZMod 2` at both `H₄₁` branches; `∃!` nonzero class for the
whole family; every class killed by doubling (so the group is `C₂`, not merely of order two by
some other structure); every class is the class of a `φ̂`-image; and the square-class side has
card 2 from the certified index.

## The formal ladder — complete

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b → P03c → P03d → P03e → P04a → P04b → P04c

| result | tier |
|---|---|
| Theorem F, `S_dyadic`, `H₄₁` saturation, δ, P01, P03a, P03b | `LEAN_CERTIFIED`, two runs |
| P03c bundled homs + kernels | `LEAN_CERTIFIED`, two runs — confirmation-grade |
| P03d dual composites | `LEAN_CERTIFIED`, two runs — architectural cross-check |
| P03e descent kernel = isogeny image | `LEAN_CERTIFIED`, two runs — constructive cross-check |
| P04a isogeny cokernels | `LEAN_CERTIFIED`, two runs — confirmation-grade |
| P04b saturation reconnect | `LEAN_CERTIFIED`, two runs — architectural cross-check |
| **P04c `E_q(ℚ)/2E_q(ℚ) ≅ C₂`** | **`LEAN_CERTIFIED`, two runs — confirmation-grade** |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

## Continuation base

**Run B**, if anything continues. It names `connectingHom`, `connectingHom_surjective` and
`ker_connectingHom` separately, so conjunct 1's exact sequence is available as standalone facts
rather than only inside the target, and `card_twoE_quotient` / `twoE_quotient_equiv_zmod` are
likewise standalone.

**But nothing is authorised to continue.** `PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`.
No novelty is claimed for `E_q(ℚ)/2E_q(ℚ) ≅ C₂` or for any other statement here.

## Next

Nothing. There is no P04d. The consolidated boundary statement for the completed programme is
`THEOREM_STATUS_H1_FREE_BRIDGE_COMPLETE_001`; the remaining gates named there — Mordell–Weil and
the rank, genuine cohomological `Sel₂`, `Ш[2^∞]`, BSD — are a separate phase requiring its own
go/no-go decision.
