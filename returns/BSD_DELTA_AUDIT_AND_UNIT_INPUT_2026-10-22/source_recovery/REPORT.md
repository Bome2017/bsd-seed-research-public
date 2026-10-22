# Targeted recovery of an existing seed relative-unit input

Status: `NO_SAVED_FULL_RANK_SEED_RELATIVE_UNIT_SOURCE_IN_CHECKED_RECORD`.

This recovery searched the source names and read the listed October 18–22
reports and actual producer/result files. It is not an exhaustive host audit.
The exact files and SHA-256 bindings are in `RECEIPT.json`.

## What was recovered

1. `seed_five` is the actual seed at coefficient five. Its default BNF runs
   failed with stack overflow at 512 MB and 2 GB. No class table or unit table
   was produced.
2. The later smaller-factor-base BNF experiments passed the earlier memory
   barrier, but all three bounded relation searches stopped before any BNF
   or ordinary-unit system was returned. There is no cached output to extract.
3. `same_curve_scaling/units_compact.gp` is an authenticated 13-unit system,
   but its curve is **1664n1**, not the seed. Those units cannot be reused as
   elements of the seed field just because both fields have degree 24.
4. The actual seed relative-principal-ideal walk has an 80-dimensional
   rational divisor kernel. Its saved exact evaluations are all roots of
   unity, not a nonzero relative unit lattice.
5. The actual seed line-function family has an 84-dimensional divisor
   kernel. All saved products evaluate to +1. Its saturation does not hide
   nontorsion units.
6. The seven torsion-coordinate S-units from October 22 are genuine elements
   with authenticated support, but their classes are even under scalar -1.
   Both faithful projections vanish, as the frozen packet proves.
7. The older 14,326-element weighted relative-unit search was the rank-two
   -47 twist of 11a1 at coefficient seven. It produced no ordinary unit.
   It was not an actual-seed A24 computation.
8. The Claude reconciliation already checked the named earlier producers:
   scalar modular-symbol norms, coefficient-three class eigenspaces, Kolyvagin
   prime eligibility and mock plectic sums. It found no ordinary unit in the
   seed A24 field or authenticated incidence image. This return does not
   inflate that targeted reconciliation into an exhaustive new audit.

There are therefore zero recovered seed relative-unit generators from these
checked sources. No bound on their existence or on the complete group follows.

## Source size required by the proposed reconstruction

Let sigma be the order-four scalar automorphism and tau=sigma^2. If epsilon
is a norm-one unit for A/K, then tau(epsilon)=epsilon^{-1}. Therefore

    {epsilon, sigma(epsilon), sigma^2(epsilon), sigma^3(epsilon)}
    = {epsilon, sigma(epsilon), epsilon^{-1}, sigma(epsilon)^{-1}}.

One scalar orbit has multiplicative rank at most two. The full rank-six
relative-unit subgroup requires at least three independent scalar orbits.
One authenticated norm-one element and all its scalar translates cannot
by themselves meet that input requirement. This is an elementary source-size
check, not a new class bound or a restriction on other Galois correspondences.

## Disposition

The reconstruction route cannot yet be instantiated from the checked saved
unit data. A new source-producing arithmetic computation is required. The
negative-source families above should not be rerun under a new name.
No BNF, L-value, class-number, or Selmer computation was launched. The
following bounded ordinary-unit pilot was then authorized and executed.
FIN, ORDER9 and Q36 are unchanged.

## Distinct finite source pilot on the actual seed

The maximal-order basis itself and its two-term combinations provide integral
candidates whose admission does not require a class group or a collected
relation base. We tested the 24 individual basis elements and every

    c*b_i + d*b_j, i<j, c in {1,2}, d in {-2,-1,1,2}.

This gives exactly 2,232 candidates. For each the absolute norm was computed
exactly. A candidate is an ordinary unit if and only if its norm is +1 or -1,
since integrality is built in. Any admitted unit would then be checked for
integrality of its inverse and projected to epsilon=a/tau(a), with exact
relative norm one and integrality checks.

**Outcome:** the only admitted candidate was the constant 1. No nontrivial
relative unit was produced. The run completed in about five seconds with
empty stderr and its explicit completion marker. This is an exact result
for this finite basis-pair family, not a bound or failure theorem for all
short elements, all units, or all relative-unit methods. The search was not
expanded after its empty outcome.

The replay uses the retained maximal order and scalar action as inputs. It
does not recertify those earlier field constructions. Code, input hashes,
output and result are preserved alongside this report.
