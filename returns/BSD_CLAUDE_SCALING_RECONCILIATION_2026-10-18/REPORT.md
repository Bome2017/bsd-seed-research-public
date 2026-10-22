# Claude reconciliation focused on the scaling bound

2026-10-18. Baseline lab commit: `797eb5efc1793b7f5f3e5edadcc2e78b76c1560c`.

**Result: no overlooked larger-prime norm-rank bound was found in the inspected material. Claude's compatible-repair arithmetic is useful: it supports a joint upper-bound target that is less restrictive than demanding growing incidence-norm rank alone. The saved complete-source calculation has been independently rechecked. No new bound across coefficient primes is proved.**

## 1. What was checked

- All **64,883 source files in the nine previously archived Claude roots** still match their October 15 inventories. There are no changed, added or missing regular files in those roots. Hash verification is not reading.
- Both GitHub repository branch lists were checked. The four explicitly named Claude lab branches still end at September 24–27 commits. Their pinned result/task/status files were retrieved; they do not contain a later torsion-field unit-rank or class-kernel computation.
- Top-level Markdown in 60 older named Claude/Opus/norm-relation roots was keyword-screened; selected relevant reports were read. The current unit-rank review binds 23 inspected files and their reading scope.

This is a targeted reconciliation, not a claim to have read every file on the computer. `inventory/` records the checked locations and byte identities. The complete earlier Claude source archive remains preserved by the October 15 return.

## 2. The useful input, and a correction to the previous scaling summary

The previous global-norm-only sufficient bound was

\[
\dim K_\chi\le (p+1)/2-r_{\rm norm}+t_D+k_C.
\]

Using this inequality alone, a small bound requires growing norm rank unless other terms are controlled correspondingly. But **norm rank alone need not do all the work in a joint global/local bound**. My previous wording overstated that necessity.

Claude's class-lift computations retain whether one and the same unit correction makes a class lift satisfy both kinds of condition. The subsequent mirror calculation supplies an actual nonzero obstruction. A nontrivial class group need not contribute a surviving class direction after this compatibility test.

For a complete faithful-character source, use its unit/class/valuation filtration. Stack authenticated global necessary conditions and local Kummer conditions into a linear map R. Write

- d=(p+1)/2 for the ordinary faithful-character unit dimension in the retained full-image setting;
- r_U for the rank of R restricted to those units;
- c for the relevant ordinary class-source dimension;
- r_C for the rank of the class-lift defect **after quotienting the target by all legitimate unit corrections**;
- q for the dimension of the valuation layer still surviving the same joint conditions.

Then the dimension of this screened containing space is

\[
\boxed{D_p=(d-r_U)+(c-r_C)+q.}
\]

This is elementary filtered linear algebra applied to an independently controlled whole source. It is not a new Selmer comparison theorem. Every true Selmer class must satisfy the chosen conditions, so D_p is an upper bound when source containment and the rows are authenticated. Uncomputed classes cannot be ignored. The point plane is compared only after this upper bound is obtained.

Thus the sufficient scaling target is combined unit rejection and class-lift obstruction: D_p<=2 directly, or D_p<=3 on the separately retained parity domain. The rank in r_U can come from both global and local conditions. The class term need not be made small by proving that the whole class group is small.

## 3. Actual complete-source data, recomputed

The two independent implementations agree on all ten saved sources. These are new elimination/reconciliation checks of existing arithmetic, not new number-field or Selmer computations.

| Source | Global necessary screen: units, classes, valuation | Joint screen: units, classes, valuation | Whole-source joint upper bound |
|---|---:|---:|---:|
| Mirror of 389a1, coefficient 3 | (0,1,2) | (0,0,0) | 0 |
| Eight retained rank-two controls, coefficient 3 | See individual rows | (1,1,0) in each case | 2 |
| Seed, coefficient 3 | See individual row | (2,2,0) | 4, conditionally |

The mirror's ordinary class group is nontrivial. Its class is separately repairable globally and locally, but the corrections disagree; the joint class obstruction removes it. The local rows also remove the two valuation directions. This is an upper bound on the entire certified source, not merely detection of a supplied class.

In the eight rank-two controls, the surviving class direction is occupied by a rational point; it does not have to be eliminated. In the seed's positive-excess control, the point quotient leaves one unit-supported and one class-supported direction. That case prevents an invalid general claim that joint conditions must remove all excess.

The eight controls and mirror retain their existing complete-source certifications. The seed retains its **GRH-dependent class completeness**. The scripts do not recertify those number-field inputs, or derive completeness from a list of known classes. See `class_contribution/` and `INDEPENDENT_JOINT_CHECK.json`.

## 4. What the other Claude work can contribute here

The inspected CM, Kolyvagin and Kato reports do not supply a missing nonzero unit-norm image. Once a source is genuinely mapped into global E[p]-cohomology, its matched Schaefer–Stoll image already satisfies the incidence-norm equation. Such classes can control the kernel through an additional arithmetic index theorem; they cannot simply be counted as nonzero norm-image witnesses. No such uniform index estimate was recovered.

The tame, wild-leg and mock-plectic computations remain evidence for their stated scalar/determinant shapes. The records do not construct a map turning those outputs into independent unit-norm images or a complete class-kernel bound. The older lower-degree norm-relations result is kept only in its stated modular-factorization scope, not as a universal obstruction.

## 5. Effect on the work now

**Retain:** the prior p=5 unit bound, the conditional seed companion calculation, and the actual compatible-repair arithmetic.

**Change:** the scaling target should measure the joint rank on units and the induced obstruction on class lifts. Requiring incidence-norm rank alone to grow is unnecessarily restrictive.

**Still open:** sufficiently small D_p at larger coefficient primes, independent whole-source/class control there, and a theorem covering all but finitely many primes. This return has not computed a new p=7 joint bound or demonstrated uniform growth of either rank.

This makes previously accumulated work relevant to the current upper-bound architecture. It does not establish FIN, ORDER9, Q36, or new seed-prime coverage. A subsequent experiment must report a certified whole-space upper bound with all three contributions; a larger detector on an incomplete list is insufficient.
