# ARISTOTLE_A2_PRIMARY_SUPPORT (2026-09-19) — READ ME FIRST

> **WARNING.** Formalizing WC proves only the implication from the stated witness-content antecedent.
> It does not establish that the antecedent is easier than FIN or that FIN has been reduced.
> This package formalizes the abstract primary-support and assembly infrastructure used by WC, and the same caveat applies:
> nothing here proves finiteness of Sha for any curve.

## What this package is
It is a self-contained Lean 4 / mathlib project covering the **abstract support assembly** around Codex's Theorem WC:
- primary parts of torsion abelian groups, and the assembly of global finiteness from local data under explicit hypotheses;
- the exact separation of "each primary part finite" from "only finitely many primary parts nonzero";
- the depth ideal J(P, h) and the exact **finite-prime-support** deduction;
- the content of vectors in the finite free lattice ℤⁿ, including its p-adic and mod-p^k divisibility forms, unimodular
  invariance, and the "descent to ℤ with a primitive comparison" sufficient condition;
- Codex's Lemma B (global lattice descent vs local finiteness), in a valuation model;
- the abstract order consequence #G = 9t² with gcd(t, 30) = 1. The square-order input (Cassels–Tate) is an explicit
  hypothesis, and a countermodel shows that #G = 9 does NOT follow;
- regression countermodels against every false stronger statement named in the Codex report.

## What this package is NOT
- **It is not about elliptic curves.** No Sha, Selmer group or modular symbol is formalized, and no arithmetic input is proved.
- **It does not prove FIN**, J_E ≠ 0, or #Sha = 9.
- It does not duplicate package A1 (the WC implication and the group-ring algebra). The only overlap is the three-line
  `primaryPart` definition and the assembly step, which WC (3) needs and which is proved in both places.
- There is no novelty claim.

## Files
Read in this order: `TASK.md`, `THEOREM_TARGETS.md`, `MATHEMATICAL_SPEC.md`, `DEFINITIONS.md`, `ASSUMPTIONS.md`,
`DEPENDENCY_DAG.md`, `KNOWN_TRAPS.md`, `SOURCE_EXCERPTS.md`, `ACCEPTANCE_TESTS.md`, then `STATE.json` / `RESUME.md`.

| Lean file | role |
|---|---|
| `PrimarySupport/Defs.lean` | FROZEN definitions (primaryPart, vInf, JOf, posSupport, content, reduceMod) |
| `PrimarySupport/Spec.lean` | FROZEN target statements (`def … : Prop`) |
| `PrimarySupport/Targets.lean` | `theorem <name> : Spec.<Name> := by sorry` — **fill these** |
| `PrimarySupport/Acceptance.lean` | FROZEN `#print axioms` probe |
| `lakefile.toml`, `lean-toolchain`, `lake-manifest.json` | Lean `v4.28.0`, mathlib `v4.28.0` (`8f9d9cff6bd728b17a24e163c9402775d9e6a365`) |

## Build
```bash
lake exe cache get   # if needed
lake build           # baseline: compiles, with one "declaration uses 'sorry'" warning per target
bash scripts/acceptance.sh
```

## Sibling package
`ARISTOTLE_A1_WITNESS_CONTENT` covers the WC implication itself and the group-ring algebra. The two packages are independent
and can run simultaneously.
