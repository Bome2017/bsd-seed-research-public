# Unit-producer admission: principal-ideal infrastructure

Date: 2026-10-22. Scope: targeted source/code check, not exhaustive history or a new unit calculation.

## Proposed producer and exact acceptance condition

PARI's `idealred(nf,[I,t],v)` carries a principal multiplier while reducing an ideal in an archimedean direction. Starting with principal ideals, retaining exact generators, and detecting repeated reduced ideal HNFs can produce units: if `(a)=J=(b)`, then `a/b` is an ordinary unit. The identity is verified by maximal-order ideal equality, independently of numerical embeddings used to choose the reduction. A subsequent quotient `u/tau(u)` is a norm-one unit. No class-group completeness hypothesis is needed to admit an individual unit.

This is an implementable producer, but it is not an untested workaround in this project.

## Historical collision

The following source files were opened and read:

1. `BSD_SMALL_BOUND_CONTINUATION_2026-10-18/p7_reduced_ideals/discover.gp`: unit-ideal reductions in 4 families of archimedean directions, exact extended-ideal identity, reduced-ideal HNF collisions, exact ordinary-unit admission.
2. The sibling `walk.gp`: reductions of eight known principal ideals, exact retained generators, collision quotients, and ordinary-unit admission.
3. `BSD_GENUINE_RELATIVE_CLASS_METHOD_2026-10-20/arithmetic/relative_setup.gp`: the actual seed A24/K12 reduction, retaining residual ideals and removing only authenticated base-field ideal content.
4. That return's `REPORT.md`: 196 exact relative identities, 17 residual collisions, and 80 kernel products all equal to signs; zero new unit directions.

The first two experiments used a rank-two degree-48 coefficient-seven control, not the seed. The third and fourth concern the actual seed. This distinction is retained: the record does not prove that every principal-component infrastructure search on the seed fails. It does prove that the broad method and its exact cycle admission have already been attempted.

A giant-step or new-direction variant changes the search trajectory, but without a new arithmetic constraint or source it is another search with the same unresolved collision problem. No such variant was launched in this return or advertised as a new seed-bound mechanism. The finite family of prior rows is excluded; all possible infrastructure paths are not.

## Efficient acceptance target once an actual unit is produced

There is a useful structural implementation detail, not a source of units. On the torsion-free norm-one unit group `E/{+/-1}`, scalar two `sigma` satisfies `sigma^2=tau=-1` in additive notation. Thus it is a torsion-free Z[i]-module of rank three, and is free because Z[i] is a PID. Consequently three suitably chosen actual relative units and their sigma-translates can in principle supply the required six Z-independent units.

This does not mean any three relative units suffice. Both faithful residual components must be checked: since `Z[i]/5 = F5 x F5`, full five-saturation is equivalent to rank three in each of the scalar eigenvalue-2 and eigenvalue-3 components, or directly rank six in authenticated residue maps on all six units. A three-dimensional check in only one faithful component leaves the other component and the rank-six index uncontrolled. No such units or residue matrices were obtained by this method screen.

## Primary software source

PARI's current general-number-fields documentation describes `idealred` as an LLL ideal reduction, with optional archimedean direction, and describes the exact update of the principal part for extended ideals:

https://pari.math.u-bordeaux.fr/dochtml/ref/General_number_fields.html

The documented principal-ideal reduction is not a complete principality or unit-generation algorithm merely because it returns a reduced ideal. The old implementation's exact HNF checks are the necessary acceptance step.

## Disposition

No new infrastructure computation was admitted. The separate maximal-order basis-combination pilot, if executed, is a different finite input family and must report only the units it authenticates. No complete class bound, source rank, or BSD endpoint changes in this note.
