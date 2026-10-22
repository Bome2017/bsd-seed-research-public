# 00_A1_FINAL_VERDICT — Aristotle A1 (witness content): successor freeze, 2026-09-19

## RETURN: **A1_FREEZE_PASS_WITH_CUSTODY_REPAIR**

```
A1 WC FINITE-ALGEBRA FORMALIZATION = MACHINE-CHECKED
STATUS = CONDITIONAL
LEVEL = A1_FULL
ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED
FIN STATUS = UNCHANGED
```

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced.

## Findings (independent replay; nothing taken from the returned logs)
1. **Fresh build.** `rm -rf .lake/build && lake build` gives `Build completed successfully (8037 jobs)`, with 0 `sorry`,
   0 warnings and 0 errors. Environment: Lean 4.28.0, mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
2. **Fresh acceptance** (`bash scripts/acceptance.sh`, unchanged script): frozen 6/6, `LEVEL: A1_FULL`,
   `FIRST_NOT_CLEAN_TARGET: None`, 3/3 stretch targets clean.
3. **Frozen files.** Defs, Spec, Acceptance, lakefile.toml, lean-toolchain and level.py are byte-identical to the original package.
4. **Targets.** 20/20 are CLEAN. Each declared type is syntactically `WitnessContent.Spec.<Name>`, the kernel re-check passes for
   the five sensitive targets, and the `Spec` namespace holds exactly the 20 frozen constants.
5. **Axioms.** For every target they are ⊆ {propext, Classical.choice, Quot.sound}. There is no `sorryAx`, no user axiom, and no
   `ofReduceBool`.
6. **Source scan.** No sorry, admit, axiom, unsafe, extern, implemented_by, native_decide, opaque, csimp, macro or elab.
   No new instances or definitions. Only heartbeat `set_option`s appear.
7. **Proof boundary.** It is exactly "antecedent + imported Ota/Selmer/Sha hypotheses ⇒ WC (1)–(3)" (`A1_FORMAL_BOUNDARY.md`).
   - Finite support comes from the prime factors of the fixed A.
   - The false inference "nonzero witness everywhere ⇒ finite support" is not used, and it is refuted in the same library.
   - Exceptional-prime finiteness is used only at S0, and only in (3).
   - There is no hidden FIN.
   - **No mathematical or formal mismatch with Codex's WC theorem.** The recorded formal differences (witness form plus bridge,
     bounded exponent, abstract index type) and the provenance note D1 on Ota's S-class (Thm 1.5 vs 6.4) were fixed before the run.
8. **Custody defect (repaired).**
   - The returned package carries the stale ORIGINAL pre-run `MANIFEST.sha256`: 21/24 OK, with Targets, STATE and RESUME
     changed and 9 new files unbound.
   - It is kept byte-exactly inside `source/` as a historical file.
   - The authoritative custody record is this directory's NEW `MANIFEST.sha256`.

## Contents
- `A1_FORMAL_BOUNDARY.md`
- `A1_TARGET_AND_AXIOM_AUDIT.md`
- `A1_REPLAY.md`
- `STATE.json`, `RESUME.md`
- `replay/`: fresh logs and comparisons
- `audit/TypeIntegrity.lean`: a custodian meta-check, not part of the library
- `source/`: a byte-exact copy of the full returned tree, excluding `.lake`

**Not claimed:**
- that FIN or BSD is proved;
- that J_E ≠ 0;
- that uniform prime support is proved;
- that WC is easier than FIN.

There is no novelty claim.
