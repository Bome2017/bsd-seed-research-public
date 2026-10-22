# Lean sources for the tame route (from Aristotle projects 69562e6c and eb3e82a5, 2026-10-06)

These are the templates the frontier cites. Every arithmetic input appears in them as an explicit hypothesis, and none proves anything about Ш of the seed. All of them were recompiled read-only with Lean v4.28.0 and Mathlib 8f9d9cff. Axioms are listed in `LEAN_RECOMPILE.txt`. All use standard axioms, except `TameCircularity.slTwoCount_eq` (`native_decide`, not load-bearing).

- **`Coinvariant/` (project 69562e6c; plain `import`).**
  - `Frontier` → `DetectorRule` → `TameLink`.
  - `TameCarrier` → `TameCircularity`.
  - Key results:
    - `DetectorRule.exists_fixed_carrier_iff_finite_alarms` (namespace `Frontier`): a fixed carrier with free p-units exists exactly when the alarm set is finite.
    - `TameLink.link_iff_fin_and_kato`: the existence-form law is equivalent to FIN-tail ∧ (K).
- **`RequestProject/Continuation/` (project eb3e82a5; `module` / `public import`).**
  - `MiddleGround` → `Frontier`, and then `Frontier` → `AuxiliaryPrime`.
  - `TamePointCounts` → `TameScalar`.
  - Key results:
    - `TameScalar.k288_rows_check`: the nine audited rows.
    - `TameScalar.eq_288_of_mem_lattice`: the denominator-21 lemma.
    - `AuxiliaryPrime.degenerate_of_shaNonzero`: this assumes the Law, so read it together with G2.

The two projects both use the namespace `Frontier`, in different files. Importing both together raises no name clash.
