# GATE — admission, kills, resources, returns

## Admission: what counts as controlling the quotient
The target is the **whole** unknown quotient `Sha(E/Q)[p^n] = Sel_{p^n}(E)/(E(Q)/p^n E(Q))`. A candidate is admissible
if it controls all of it, by **any** of:
* a bounded source **surjecting** onto it;
* a bounded target **receiving it injectively**;
* bounded kernel **and** cokernel of a comparison;
* an explicit annihilator;
* an exact sequence with the other terms controlled;
* an independently proved equivalent assertion.

**There is no arrow-orientation rule.** "Must map out of Selmer, not into it" is wrong and must not be applied — it
would reject a valid bounded-target injection. What killed the earlier automorphic routes was **absence of coverage**:
the image was a selected subspace with nothing bounding the complement. Diagnose coverage, not direction.

## Kill conditions — return STOP immediately on any of these
* **K1.** You **prove**, in a precisely delimited class of candidate objects that you state, that no fixed integral
  lift or comparison exists in that class. **Failure to construct one is not K1.** If you searched without success the
  verdict is `NO_SURVIVOR`, worded *"no fixed comparison was proved in the class C"* — never *"no fixed comparison
  exists"*. Delimit `C` explicitly.
* **K2.** The comparison cannot be made uniform over all split primes outside a finite, **proved** list.
* **K3.** No admissible rank-one cover can be constructed. (Note: the three-imaginary-field cover is already known
  impossible — `TASK.md` Q2. Do not report that as a new finding.)
* **K4.** The finite-support claim assumes FIN, BSD, an equivalent unproved global Sha statement, or a conjectural
  input (e.g. Stark-Heegner points).
* **K5.** The result is an equivalence to FIN in new language rather than new control.

## Resources
No large modular-symbol or twist computation. No prime ladder. No `C_17`. After the structural argument is settled you
may test a **bounded** list of small `D_2` candidates against the cheap gates only (splitting conditions, regime (P),
root number). Certified twist derivatives are expensive and are not authorized here.

## Returns — exactly one
| verdict | when |
|---|---|
| `TAIL_FINITE_SUPPORT_PROVED` | you prove `Sha(E/Q)[p] != 0 => p in S` for one explicit finite `S` |
| `STRICT_REDUCTION` | a new theorem makes FIN strictly easier, with the first open arrow downstream of new proved information; give the full chain |
| `NEW_LEMMA_ONLY` | a genuinely new reusable theorem that does not yet compress the tail; state exactly what it proves and what remains |
| `NO_SURVIVOR` | every construction collapses; list only the **new** obstructions |

**Wording mandate.** In every negative verdict distinguish (i) a proved impossibility inside a class you state,
(ii) a located theorem whose hypotheses fail here, and (iii) a construction you attempted and could not complete. Only
(i) may be phrased as an impossibility. Inability to prove a step must never be promoted into a no-go theorem — that
failure mode has already cost this project several retractions.

State the exact first unproved arrow in every case. Do not write a roadmap, do not survey literature, do not
re-audit an archived route. `record/FRONTIER.md` lists the route stops with their scope and the overclaims this project
has already had to withdraw — read §6 there before asserting any impossibility.
