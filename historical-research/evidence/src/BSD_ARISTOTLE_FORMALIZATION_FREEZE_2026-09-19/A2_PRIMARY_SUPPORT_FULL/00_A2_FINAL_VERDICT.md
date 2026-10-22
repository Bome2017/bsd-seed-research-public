# 00_A2_FINAL_VERDICT — Aristotle A2 (primary support): successor freeze, 2026-09-19

## RETURN (A2 part): **PASS_WITH_CUSTODY_REPAIR**. Combined verdict: `../FREEZE_INDEX.md`

```
PRIMARY SUPPORT / CONTENT / ASSEMBLY = LEAN MACHINE-CHECKED
LEVEL = A2_FULL (+ 3/3 STRETCH)
FIN STATUS = UNCHANGED
FORMULA STATUS = UNCHANGED
#Sha = 9 t^2 is formally checked under its exact abstract hypotheses (order_nine_t_sq); NOT #Sha = 9
```

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced.

## Findings (independent replay; the returned logs were not trusted)
1. **Fresh build.** `rm -rf .lake/build && lake build` gives `Build completed successfully (8040 jobs)`, with 0 sorry, 0 warnings
   and 0 errors. Environment: Lean 4.28.0, mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
2. **Fresh acceptance.** Frozen 6/6, `LEVEL: A2_FULL`, `FIRST_NOT_CLEAN_TARGET: None`,
   `STRETCH_CLEAN: [alternating_square, CM_noncyclic_target, CM_codex_torsion_example]`.
3. **Frozen files.** Defs, Spec, Acceptance, lakefile.toml, lean-toolchain and level.py are byte-identical to the original package.
4. **Targets.** 28/28 CLEAN. Every declared type is syntactically `PrimarySupport.Spec.<Name>`, 12 kernel re-checks pass, and the
   `Spec` namespace holds exactly the 28 frozen constants.
5. **Axioms.** Every target stays within {propext, Classical.choice, Quot.sound}. There is no sorryAx, user axiom, native_decide,
   extern or implemented_by.
6. **Boundary** (`A2_FORMAL_BOUNDARY.md` §2): all seven points are confirmed.
   - Both conditions are required in `finite_iff_local_and_support`.
   - Exceptional-prime finiteness stays explicit in `assembly_WC_shape`.
   - No nonzero J is made from pointwise nonvanishing.
   - `content_bounds_J` keeps its comparison hypotheses.
   - `order_nine_t_sq` concludes only 9t², gcd(t,30) = 1.
   - `CM_order_441` meets every hypothesis and has order 441.
   - `alternating_square` targets a cyclic ZMod N, and the non-cyclic generalisation is refuted.
   - No elliptic-curve input is derived internally.
7. **Custody defect (repaired).**
   - The returned package keeps the stale pre-run `MANIFEST.sha256` (21/24; Targets, STATE and RESUME changed; 12 files unbound).
   - That file is kept byte-exactly in `source/` as a historical file.
   - This directory's NEW `MANIFEST.sha256` is authoritative.

**Not claimed:** FIN, #Sha finite, #Sha = 9, J_E ≠ 0, uniform prime support, FORMULA, BSD, or that WC is easier than FIN. There is
no novelty claim.
