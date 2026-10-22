# FORMALIZATION_BOUNDARY — Aristotle A1 + A2, final immutable statement (2026-09-19)

Seed E: y² = x³ − 22735x² + 106272484x. The top level is unchanged: FULL BSD = RANK ∧ FIN ∧ FORMULA. RANK is closed;
**FIN and FORMULA are open.**

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced.

## PROVED / MACHINE-CHECKED
Lean 4.28.0 with mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`. The custodian replayed both returns from fresh unpacks.
Axioms ⊆ {propext, Classical.choice, Quot.sound}. Every declared type is syntactically the frozen `Spec` constant.

- **A1 — the finite algebra behind the CONDITIONAL WC implication** (level A1_FULL; 20/20 targets, including 3 stretch). It covers:
  - Lemma A (e·I^r ⊆ I^{r+1}), the graded pieces, depth, h_p and J_E;
  - Theorem WC in abstract and group-ring form. Its antecedent A ≠ 0 ∧ A ∈ J_E and the Ota 5.17 / Ota 1.5 / Selmer / Sha-torsion
    inputs are **explicit hypotheses**;
  - the bridge from Ota 5.17's printed form;
  - the instantiation checks.
- **A2 — the abstract primary-support / content / assembly machinery** (level A2_FULL; 28/28 targets, including 3 stretch). It covers:
  - torsion assembly;
  - the exact separation "every primary part finite ∧ finitely many nonzero";
  - J(P,h): its ideal structure, its nonzero ⟺ finite-support characterisation, and its generator;
  - lattice content (integral, p-adic, mod p^k), unimodular invariance, and the descent-to-ℤ implication;
  - Lemma B (valuation model);
  - the square-order theorem for nondegenerate alternating pairings into a cyclic ZMod N.
- **A2 order consequence.** For a *finite* abelian group G with |G[2^∞]| = 1, |G[3^∞]| = 9, |G[5^∞]| = 1 and every odd-primary
  order a square: **|G| = 9t², gcd(t, 30) = 1**. This is the abstract theorem `order_nine_t_sq` under exactly those hypotheses.
- **The packaged countermodels.** Each refutes a tempting false shortcut:
  - `CM_uniform_denominator` and `CM_nonzero_everywhere` (A1 and A2): nonzero witnesses at every prime do not give J ≠ 0 or
    finite support;
  - `CM_each_local_finite`: local finiteness does not give finiteness;
  - `CM_finite_support`: finite support does not give finiteness;
  - `CM_profinite_perfectness`: finite local defects do not give finite support;
  - `CM_order_441`: the H2 hypotheses do not give |G| = 9;
  - `CM_noncyclic_target`: square order fails for non-cyclic pairing targets;
  - `WC_abstract_nonvacuous`: the WC hypotheses are consistent.

## NOT PROVED
- J_E ≠ 0.
- Any uniform arithmetic witness-content antecedent: no nonzero A in J_E, no bounded-content comparison, no uniform prime support.
- FIN.
- #Sha finite.
- #Sha = 9. "FIN ⇒ #Sha = 9" is false as an inference; H2 gives only 9t² under its hypotheses.
- FORMULA.
- BSD.
- WC being easier than FIN.

## Why this is not a reduction in difficulty
Codex has shown that, on the good ordinary tail, depth-zero Ota-witness existence is equivalent to primary Sha vanishing:

  h_p = 0 ⟺ Sha(E/Q)[p^∞] = 0 at every good ordinary p ∉ S0 = {2, 3, 5, 2243, 4547, 5843}.

- **Source:** `~/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md`, Theorem O1, sha256
  `7a5ac582f42c8f7c…`; that folder's manifest verifies 24/24.
- **Status:** a written deduction from Kim Thm 1.10 and Castella–Sano Thm B with the seed hypotheses checked. It is not Lean-checked.
  The positive-depth transfer for the exact Ota-admissible set and the supersingular primes are not covered by O1.
- **Consequence:** WC's antecedent restates FIN's ordinary vanishing tail in Ota coordinates.
- **These formalizations close proof-engineering uncertainty only; they do not reduce the arithmetic difficulty.** The open
  mathematics is unchanged: an independent uniform arithmetic theorem, plus the exceptional primes.

## Methodological gate for any future FIN "compression" (not a theorem route)
Any proposal must pass the Albertson coverage gate (`~/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/ALBERTSON_COVERAGE_GATE.md`,
sha256 `6427eafb16b59bd6…`). It must independently supply:
1. a finite cutoff or regime reduction;
2. a uniform theorem for the entire tail;
3. terminating full-primary certificates for the exceptional cases;
4. exhaustive coverage plus assembly.

The A2 assembly theorems formalize only component 4's elementary *assembly* step. They supply none of components 1–3. No transfer
of Albertson-conjecture mathematics to BSD is claimed.

No novelty claim. Nothing is merged.
