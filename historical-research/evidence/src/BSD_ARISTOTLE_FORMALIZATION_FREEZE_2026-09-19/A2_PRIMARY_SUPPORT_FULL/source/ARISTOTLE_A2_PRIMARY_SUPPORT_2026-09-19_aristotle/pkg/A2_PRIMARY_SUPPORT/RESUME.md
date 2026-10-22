# RESUME — ARISTOTLE_A2_PRIMARY_SUPPORT

## Status
COMPLETE at level **A2_FULL**, with all three STRETCH targets also clean.
Every theorem in `PrimarySupport/Targets.lean` is proved: no `sorry`, no `admit`, no new `axiom`.
`bash scripts/acceptance.sh` reports: frozen files OK (6/6), clean build, and for all 28 targets
axioms ⊆ {`propext`, `Classical.choice`, `Quot.sound`}.

## Layout
| file | contents |
|---|---|
| `PrimarySupport/Defs.lean`, `Spec.lean`, `Acceptance.lean` | FROZEN, untouched |
| `PrimarySupport/Targets.lean` | the 28 target theorems, each proved from a helper lemma |
| `PrimarySupport/Content.lean` | content of `ℤⁿ`-vectors: L1–L6 |
| `PrimarySupport/Depth.lean` | `vInf`, `JOf`: J1–J4 and the `JOf = {0}` half of CM2 |
| `PrimarySupport/Descent.lean` | L7, descent to `ℤ` with a primitive comparison |
| `PrimarySupport/LemmaB.lean` | B1, B2 and the CM3 valuation datum |
| `PrimarySupport/Primary.lean` | primary parts, torsion decomposition, assembly: P1–P5 |
| `PrimarySupport/Countermodels.lean` | CM1 (`⨁_p ZMod p`) and CM1′ (`ℕ →₀ ZMod 2`) |
| `PrimarySupport/Order.lean` | H0, H2 and the order-441 countermodel CM4 |
| `PrimarySupport/Pairing.lean` | S2: cross product on `(ZMod 2)³` |
| `PrimarySupport/CodexExample.lean` | S3: `⨁_{p ≠ 2,5} (ZMod p)²` |
| `PrimarySupport/Symplectic.lean` | S1: nondegenerate alternating pairing into `ZMod N` ⇒ square order |

## Rules respected
- Frozen files untouched; no hypothesis of any target was added, removed or weakened.
- Every countermodel is proved, not weakened.
- All arithmetic inputs (finiteness, the square-order Cassels–Tate input, the 2-, 3-, 5-primary
  data, the comparison lattice vector of L7) occur only as hypotheses.
- No claim is made that FIN, finiteness of Sha, `J_E ≠ 0` or `#Sha = 9` is proved.

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not
> establish that the antecedent is easier than FIN or that FIN has been reduced.
