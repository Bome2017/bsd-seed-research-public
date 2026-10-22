# Aristotle A: construct independent arithmetic control of the exact excess

Start by running `python3 prepare_reference.py`. Read COMMON_CONTRACT.md,
CURRENT_FRONTIER.md, RECENT_WALLS.md, LOCAL_ATTEMPT.md and the governing proofs
they identify. Create checkpoint files. The historical prompts inside the
archives do not govern this run.

The target is X_p=Sel_p(E/Q)/W_p=Sha[p]. The conditional order-three
identification X_p=C[t]/t^2C is available, but you may bypass it. Construct
an arithmetic input which independently bounds dim_Fp X_p<=1 for all but
finitely many primes, or independently annihilates X_p by a p-unit there.
The purpose is a new uniform FIN input for this fixed rank-two curve.

## Your construction assignment

Produce an actual controlling arithmetic map or ideal, not another exact
realization of X_p. One admissible form is an injection X_p -> U_p and an
independent arithmetic bound dim U_p<=1. Another is an integral ideal
I_p acting trivially on X_p with an independent proof I_p mod p is the
unit ideal outside a fixed finite set. You may use p-dependent global
cohomology, Euler-system, class-field, automorphic, or other arithmetic.
No common rational scalar is mandatory.

Before developing a candidate, identify (i) its exact arithmetic source,
(ii) its map to/from X_p or to an integral complex controlling X_p,
(iii) the information beyond the retained target identities, and
(iv) the theorem or construction that will bound that information. Prove
the weakest estimate sufficient for the seed; multiplicity-one or a full
main conjecture is not required if a smaller inequality works.

## A concrete first place to look, with the failed shortcut removed

The recent higher-Fitting source in LOCAL_ATTEMPT.md has now been read.
Do not repeat its audit as your result. Its arithmetic ideals are a possible
source only if you construct additional augmentation or specialization
control. If you choose that source, name the integral complex and exact
control map, retain H2 and height-two errors, and identify the **particular
generator or minor** whose valuation can be controlled independently.
Generic rank one, mu=0, doubled torsion, nonzero characteristic ideal and
existence of some unit auxiliary witness are insufficient; the explicit
module controls already show why.

The new arithmetic question is whether the fixed seed data provide a bound
on the relevant generator/minor without the unbounded residual Selmer rank
entering the number of auxiliary operations. If another arithmetic source
has a better path to this estimate, use it instead. The project is not
required to stay in anticyclotomic Iwasawa theory.

## Mandatory rejection tests

- If the proposed upper bound is proved only after assuming the same
  Selmer dimension/short-summand vanishing, it is circular.
- If a reduction to a cohomological complex discards H2 torsion, repair that
  step before continuing. The supplied countercontrol is decisive for the
  unsupported inference, not for every complex method.
- If the construction supplies relations, identify a genuine rank estimate
  on the quotient's multiplicity space. More rows, support, detection, or
  a nonzero pairing alone do not qualify.
- A statement valid separately for every fixed p with uncontrolled constants
  is not a cofinite bound. An ordinary-only theorem must preserve its domain.
- An isomorphism with Sha is not itself a reason to abandon a candidate;
  abandon it only if the supposed controlling input is also unproved or
  circular. An independent proof of an equivalent criterion would succeed.

## Return sought

Follow the common return contract. The most useful partial output would
construct a previously missing arithmetic map or prove a quantitative
specialization inequality with every remaining term explicitly identified
and independently defined. It must improve the arithmetic control, not
just reduce the number of formal parameters. A theorem about the seed
is the aim; do not spend this job certifying unrelated abstract examples.

If no construction survives, return
NO_BOUND_MECHANISM_FOUND_FOR_TESTED_CANDIDATES with a precise record and stop.
No additional lifting, point-count or fixed-prime campaign is requested.
