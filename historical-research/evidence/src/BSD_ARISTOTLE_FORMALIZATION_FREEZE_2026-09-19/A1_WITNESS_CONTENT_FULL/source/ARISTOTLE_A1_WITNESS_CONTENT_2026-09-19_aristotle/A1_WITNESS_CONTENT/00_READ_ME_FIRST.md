# ARISTOTLE_A1_WITNESS_CONTENT (2026-09-19) — READ ME FIRST

> **WARNING.** Formalizing WC proves only the implication from the stated witness-content antecedent.
> It does not establish that the antecedent is easier than FIN or that FIN has been reduced.

## What this package is
It is a self-contained Lean 4 / mathlib project. The task is to machine-check the **purely algebraic content** of Codex's
**Theorem WC** (witness-content criterion) and the finite group-ring algebra it rests on:
- **Lemma A:** e·I^r ⊆ I^(r+1) in a group ring;
- divisibility depth in finite p-primary modules;
- the witness ideal J_E;
- the bridge from Ota's Theorem 5.17 (group-ring form) to the witness form;
- regression countermodels that refute the tempting false shortcuts.

## What this package is NOT
- **It is not a proof of FIN**, of finiteness of Sha, or of anything about a specific elliptic curve.
- **The arithmetic antecedent is never proved and must not be attempted.** It says that a nonzero integer A lies in J_E, i.e.
  that there is uniform witness-content control.
  - In every target it is an explicit hypothesis at the formal boundary, tagged `NOT_PART_OF_THIS_TASK`.
- **Ota's theorems, the Selmer-group facts and torsion of Sha are not formalized.** They enter as explicit hypotheses tagged
  `IMPORTED_ARITHMETIC_THEOREM`.
- **Nothing here relies on the older LINE theorem**, which is stronger than WC and not needed.
- There is no novelty claim.

## Files (read in this order)
1. `TASK.md` — the exact assignment, acceptance levels and rules.
2. `THEOREM_TARGETS.md` — every target: its Lean name, statement, level, source and proof hints.
3. `MATHEMATICAL_SPEC.md` — the mathematics in prose, including Codex's proof of WC.
4. `DEFINITIONS.md` and `ASSUMPTIONS.md` — every definition, and every hypothesis tagged.
5. `DEPENDENCY_DAG.md`, `KNOWN_TRAPS.md`, `SOURCE_EXCERPTS.md` (verbatim Codex, restated Ota).
6. `ACCEPTANCE_TESTS.md` and `scripts/acceptance.sh` — how the result is judged.
7. `STATE.json` and `RESUME.md` — keep them updated as you work.

## Lean files
| file | role |
|---|---|
| `WitnessContent/Defs.lean` | FROZEN definitions (primary parts, depth, h_p, J_E, augmentation ideal, graded pieces, cls2) |
| `WitnessContent/Spec.lean` | FROZEN target statements, each a `def … : Prop` |
| `WitnessContent/Targets.lean` | `theorem <name> : Spec.<Name> := by sorry` — **fill these** |
| `WitnessContent/Acceptance.lean` | FROZEN `#print axioms` probe for every target |
| `lakefile.toml`, `lean-toolchain`, `lake-manifest.json` | environment pin: Lean `v4.28.0`, mathlib `v4.28.0` (`8f9d9cff6bd728b17a24e163c9402775d9e6a365`) |

## Build
```bash
lake exe cache get   # if your environment needs mathlib binaries
lake build           # baseline: compiles, with one "declaration uses 'sorry'" warning per target
bash scripts/acceptance.sh
```
At packaging time the baseline `lake build` succeeded from an unpacked copy of this tarball; see `ACCEPTANCE_TESTS.md`.

## Sibling package
`ARISTOTLE_A2_PRIMARY_SUPPORT` formalizes the abstract primary-support infrastructure (assembly, J characterisation,
lattice content, the square-order consequence). The two packages are independent and can run simultaneously. Their only
overlap is the three-line definition of `primaryPart` and a small assembly step that WC (3) needs.
