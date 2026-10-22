# RESUME — ARISTOTLE_A1_WITNESS_CONTENT

## Status
COMPLETE at level **A1_FULL**: all 11 CORE targets, all 6 FULL targets and all 3 STRETCH targets
compile with no `sorry`, no `admit` and no new axiom. `#print axioms` shows only `propext`,
`Classical.choice`, `Quot.sound` (and `propext` alone for `zero_infinitely_divisible`).

## How it is organised
`WitnessContent/Targets.lean` proves each frozen `Spec.<Name>` statement, delegating to helper
files that were added for this run (the frozen files `Defs.lean`, `Spec.lean`, `Acceptance.lean`,
`lakefile.toml`, `lean-toolchain`, `scripts/level.py` are byte-identical to the package):

| file | content |
|---|---|
| `WitnessContent/GroupRing.lean` | augmentation-ideal representation `f = ∑ f g • (g − 1)`, truncated binomial expansion, Lemma A, graded pieces killed by `e` and by `p ^ v_p(e)`, the `cls2` bridge |
| `WitnessContent/Depth.lean` | downward closure of `p`-divisibility, depth attained/maximal/bounded, `h_p` characterisations, `J_E` bounds |
| `WitnessContent/Primary.lean` | `Sha[p] = 0 ⇒ Sha[p^∞] = 0`, primary decomposition of a torsion element, finiteness from a finite cover by finite primary parts |
| `WitnessContent/WC.lean` | T7 `WC_abstract`, T8 `WC_groupRing` |
| `WitnessContent/Countermodels.lean` | T9a, T9b, T12 |
| `WitnessContent/Instances.lean` | T10, T11 |
| `WitnessContent/Stretch.lean` | S1, S2, S3 |

## Verification
```bash
bash scripts/acceptance.sh
# frozen check 6/6 OK; clean build OK; no sorry/admit/axiom tokens;
# LEVEL: A1_FULL ; FIRST_NOT_CLEAN_TARGET: None ; STRETCH_CLEAN: all three
```

## Boundary (unchanged)
- The arithmetic antecedent `A ≠ 0 ∧ A ∈ J_E` is a hypothesis of T7 and T8 and is never proved.
- Ota's theorems, the Selmer corank facts and torsion of Sha are hypotheses and are never proved.
- Nothing here claims FIN, finiteness of Sha, or `J_E ≠ 0`.

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not
> establish that the antecedent is easier than FIN or that FIN has been reduced.
