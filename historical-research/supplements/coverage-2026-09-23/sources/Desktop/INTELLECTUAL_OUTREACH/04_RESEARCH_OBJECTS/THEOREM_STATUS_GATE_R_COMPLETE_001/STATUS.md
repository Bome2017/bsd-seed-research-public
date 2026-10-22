# THEOREM STATUS — GATE R COMPLETE

**Object type:** status and consolidation only. No new mathematics, no new Lean theorem, no new
inference, no reinterpretation of any prior boundary.

**Supersedes in role, not in place:** `THEOREM_STATUS_H1_FREE_BRIDGE_COMPLETE_001`
(`e823ed125663279cc9a0d6ee96fd54401d0c65d7411c21426fc9de2cb10f3462`), which remains frozen and
unmodified as the historical status at the P04c boundary. Nothing in that object is rewritten
here; where it is now wrong, the correction is recorded in
`CORRECTIONS_TO_ROADMAP_PROSE.md` as a successor correction.

---

## 1. The principal new certified endpoint

For the existing certified `H41` family, under the existing prime instance and the existing
hypotheses `SDyadic.Params ε m q` and `SDyadic.H41 ε m`:

```lean
theorem GateR.h41_rank_zero
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    Module.rank ℤ (P01.Ecurve ε m q).toAffine.Point = (0 : Cardinal)
```

**The codomain is `Cardinal`.** This is mathlib's cardinal-valued module rank, over `ℤ`, on
`WeierstrassCurve.Affine.Point` of `P01.Ecurve ε m q` over `ℚ`, under the canonical
`AddCommGroup.toIntModule` structure — read off the fully elaborated term, not the source text.
It is not `Module.finrank`, not `Group.rank`, not `AddGroup.rank`, and not a statement about a
quotient, subgroup or any other group.

    rank_Z E_q(Q) = 0        LEAN_CERTIFIED for the H41 family

Certification: two independent Aristotle proof searches on byte-identical input, both externally
rebuilt and re-audited by Claude. Axiom footprint of each output, regenerated externally:
`[propext, Classical.choice, Quot.sound]`.

## 2. The stronger intermediate certified statement

```lean
theorem GateR.every_point_torsion … :
    ∀ P : (P01.Ecurve ε m q).toAffine.Point, ∃ n : ℕ, 0 < n ∧ n • P = 0
```

Every rational point of `E_q` is formally proved to be a torsion point.

**Three distinctions that must be preserved.**

1. Every rational point is proved torsion. That is a genuine certified statement about the
   actual point group, not an abstract group-theoretic remark.
2. This does **not** identify `E_q(ℚ)` with `{O, T}`, and nothing in the development does.
   Pointwise finite order is not finiteness of the group.
3. **No theorem asserting `Finite E_q(ℚ)`, `Fintype`, `AddGroup.FG`, `Module.Finite ℤ` or
   `Module.Free ℤ` on the point group exists anywhere in the certified development.** This was
   checked, not assumed: see `receipts/FINITENESS_SEARCH.txt`. The only finiteness proved in the
   entire tree is finiteness of height **sublevel sets**.

Consequently any statement that the programme has determined `E_q(ℚ)` as a group, or exhibited
it as `{O, T}`, or proved it finite, would be false.

## 3. The H¹-free point-group endpoint, unchanged

```lean
Nat.card ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) = 2
Nonempty (((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+ ZMod 2)
```

    E_q(Q) / 2 E_q(Q)  ~=  Z/2Z

from `P04c.two_descent_quotient`, frozen in
`P04C_TWO_DESCENT_QUOTIENT_FORMALIZATION_FREEZE_001`
(`6b93c2278b5afa174808b42ee9427a20a102f0420a991701ca2cfeefe13061bb`, recomputed here).

**Neither endpoint is Sel₂, Ш, or BSD**, and neither may be described as such. Both are
statements about the actual rational point group and its subgroup of doubles. The full verbatim
statements are in `receipts/CERTIFIED_STATEMENTS_VERBATIM.txt`.

## 4. Certification tiers — never merged

    GateR.h41_rank_zero, GateR.every_point_torsion,
    GateR.height_sublevels, halving_representatives, bounded_halving      LEAN_CERTIFIED
    P04c, P04a, P04b, P03a-e, P01, R1, R0                                LEAN_CERTIFIED
    the F / S_dyadic / saturation base                                    LEAN_CERTIFIED
    anything about Sel_2, Sha, L-values, BSD                              NOT CERTIFIED AT ALL

"`LEAN_CERTIFIED`" in this programme means: proved in Lean, returned by two independent
Aristotle proof searches, externally rebuilt by Claude from frozen bytes against an independent
copy of the pinned dependencies, with axioms and constructs re-audited externally and the
statement's identity to the commissioned statement established by typechecking.

## 5. Boundary declarations

    FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
    ACTUAL_H1_SELMER_OBJECT  = NO
    touches_L_function       = NO          (for the formal Gate-R development)
    PRIOR_ART_BLOCKER        = UNRESOLVED

Environment pin, unchanged throughout: Lean `leanprover/lean4:v4.28.0`, mathlib
`8f9d9cff6bd728b17a24e163c9402775d9e6a365`.

## 6. Where to look

    CERTIFIED_ENDPOINTS.md      the certified statements and what each does and does not say
    FORMAL_CHAIN.md             the actual dependency structure, with one correction
    CORRECTIONS_TO_ROADMAP_PROSE.md   the Mordell-Weil necessity claim, withdrawn
    H41_DEPENDENCY.md           the unused hH binder, stated exactly
    REPLICATION_STATUS.md       what the two-run evidence is and is not
    NON_CLAIMS.md               what this completion does NOT certify
    REMAINING_GATES.md          Gate C and Gate A
    CUSTODY_AND_ERRATA_CARRIED_FORWARD.md   methodological corrections, none repaired
    ULTRA_AUDIT_ENTRYPOINT.md   why this object is the entry point for the whole-program audit
    receipts/                   generated evidence for every claim above
