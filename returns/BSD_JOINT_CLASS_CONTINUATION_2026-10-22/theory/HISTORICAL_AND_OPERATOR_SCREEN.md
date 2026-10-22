# Joint class continuation: historical and operator admission screen

Date: 2026-10-22. Scope: written elementary deduction and exact finite algebra;
no number-field class group was computed and no novelty is asserted.

## What the archive has already done

Read the following current lab records rather than treating the earlier
97/106 bounds as the entire existing machinery:

- `BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15/character_review/CLASS_MAP_BOUND.md`: actual ordinary class map
  `u_C:Cl(A)[p]^chi -> Cl(B)[p]^(chi^-1)` and its unit connecting map.
- `BSD_JOINT_REPAIR_TARGET_EXPERIMENT_2026-10-15/theory/POINT_RELATIVE_REPAIR.md`:
  actual common global/local unit repair obstruction, its dual mixed rows,
  and the exact unit/class/valuation filtration modulo the point plane.
- The same return's `REPORT.md`: held-out arithmetic showing that identical
  marginal ranks and overlap dimensions do not determine the mixed class
  obstruction. Some unit classes can also survive as genuine excess.
- `BSD_CLASS_MAP_AND_PARTIAL_RELATIONS_2026-10-20/class_map/PROOF.md`:
  complete 1664n1 control; source and companion class groups C6, class map
  zero on the C3 component, connecting map zero, one unit and one class
  direction survive and are occupied by points.
- `BSD_GENUINE_RELATIVE_CLASS_METHOD_2026-10-20/theory/PRESENTATION_BOUND.md`:
  a complete class bound needs generator completeness modulo p, but not a
  full relation lattice or a whole class-number computation.
- `BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15/character_review/REVIEW.md`:
  geometric norm kernel and integral composition were already checked at
  5,7,11; an explicit counterlattice excludes replacing the actual unit
  index by the geometric index.

The common-repair map is therefore not a new construction to propose.
Likewise, calculating another geometric incidence rank cannot certify the
arithmetic class kernel.

## A complete screen for new orbit-weighted point-to-covector norms

Let V=F_p^2, X=V minus {0}, Y=V^* minus {0}, and let G=GL_2(F_p) act
contragrediently on Y. The G-orbits on Y times X are exactly

    O_t={(lambda,v):lambda(v)=t}, t in F_p.

For t nonzero each orbit has p(p^2-1) elements; O_0 has
(p-1)(p^2-1). Thus every G-equivariant integral correspondence from the
point permutation module to the covector permutation module is an integral
linear combination of the p incidence matrices N_t.

On the faithful homogeneous source, use f(a v)=chi(a) f(v), with chi a
nontrivial Teichmueller character. Write

    (N_t f)(lambda)=sum_{lambda(v)=t} f(v).

Changing v=t w shows N_t=chi(t) N_1 for t nonzero. For t=0 the nonzero
vectors on ker(lambda) form one scalar orbit, and sum_a chi(a)=0, so N_0=0.
Therefore every such correspondence restricts to a scalar multiple of the
existing affine incidence norm. This is an identity over Z_p, not only
modulo p. Stacking these orbit-weighted maps adds no new class-map kernel
constraint beyond that of N_1. If the scalar multiplier is nonunit it can
only weaken the condition.

Scope is essential: this concerns linear G-equivariant point-to-covector
correspondences built from this same finite torsion orbit geometry. It does
not cover arithmetic maps depending on new units, actual ideal classes,
ramified local conditions, a larger source, or a new reciprocity theorem.
The identity on genuine ideal maps must use the same retained primitive
push-pull normalization; raw unweighted ramification counts are not a
substitute. Here the identity is first proved on correspondences, hence
holds for their actual compatible arithmetic realizations.

`check_incidence_gate.py` independently enumerates the G-orbits using
unipotent and diagonal generators, constructs all N_t after scalar
projection, and checks their Teichmueller identities modulo p^2 for
p=3,5,7,11,13. It finds operator-span dimension one in every case.
For the degree-one Teichmueller character used in the finite check, the
source has dimension p+1, N_1 has rank p-1, and its kernel is
the two coordinate-linear functions. These latter geometric ranks were
already in the record; they are controls here, not new class bounds.
No claim that these ranks agree for every nontrivial scalar character is
made; the operator-span identity above does hold for every such character.

## Higher integral precision does not control multiplicity by itself

The hoped-for extra information must not be reduced to the identities
vu=uv=p or to an exponent bound. For every e>=1 and a>=1 take

    C_A=C_B=(Z/p^a)^e,   u=p,   v=identity.

Both compositions are multiplication by p, and u kills the entire
p-torsion subgroup F_p^e. The multiplicity e is arbitrary. With a=1 there
is no further p-adic layer to inspect, but the entire arbitrary-dimensional
class contribution remains. This is an abstract control, not a seed
realization. The script checks 36 finite cases at p=3,5,7.

Thus an integral incidence/Bockstein proposal is admissible only if it
uses additional arithmetic to bound the dimension of this first layer,
not merely the exponent or existence of the next lift. The class-carrying
1664 control additionally prevents requiring every admitted class to die:
one such class is needed for its point plane.

## Concrete next admission gate

The next genuinely new calculation cannot be an additional N_t or another
matrix from the same orbit algebra. It must authenticate either

1. a complete p-primary source presentation whose generation-mod-p defect
   is controlled independently, followed by the already-defined actual
   class map and common-unit repair; or
2. an arithmetic theorem bounding the kernel of those maps on the entire
   ordinary class group, including undiscovered classes.

Neither is supplied by this screen. For a computational first test, the
existing degree-eight seed source at p=3 is smaller and has saved class
and unit data, but its completeness cannot be assumed. A p-part-specific
certification using those data could be meaningful if it produces a new
unconditional bound. The existing class presentation [12,6,2] and known
point/excess classes must remain separate from a proof of completeness.
At coefficient five the desired upper source bound is at most three;
complete generator coverage plus enough norm/local rank is still needed.

FIN, ORDER9 and Q36 are unchanged. This screen closes neither the general
class method nor a whole research lane. It prevents sending already-known
maps back as if they were new arithmetic.
