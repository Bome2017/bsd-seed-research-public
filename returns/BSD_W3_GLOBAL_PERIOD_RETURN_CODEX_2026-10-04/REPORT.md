# W3 global-period attack: cofinite integral control, period gate open

**Status: W3_NEW_REDUCTION — cofinite integral-control and evaluation step only.**

The supplied attack was executed through the integral construction and source
comparison. A written cofinite Hida-control argument and an integral
critical-value functional were obtained. The required unit comparison with
the previously normalized Kato value was **not** completed. Therefore the
requested divided residual object, its collision identity, and a nonzero
fixed ancestor have not been established.

This status refers to the new construction steps below, at
written-derivation/imported-theorem grade. It does not mean that only one
step remains before BSD. Independent mathematical review is pending;
literature novelty is not claimed.

## What was constructed

For this seed, rational two-torsion and the Hasse bound give

    a_p(E) != +1,-1 mod p

at every good p>=5; the one small case p=5 has #E(F_5)=8. Define a fixed
nonzero integer D from the finite tame weight-two Hecke spectrum by taking
norms of eigenvalue differences separating every other newform from the
seed. No Sha or Kato index enters D.

Outside D, the ordinary weight-two fiber has only the seed's ordinary
stabilization: other tame eigensystems are separated by D, while p-new
forms would have U_p=+/-1 and are excluded by the displayed congruence.
Integral Hida control and finite freeness then give

    T_p = Z_p[[T]],       weight-three point T=p,

and a primitive integral modular-symbol specialization. This is the full
localized Hecke algebra, not an unidentified normalized branch. The proof
uses [EPW's integral Hida and multiplicity-one theorems](https://arxiv.org/abs/math/0404484).
See [COFINITE_HIDA_CONTROL.md](COFINITE_HIDA_CONTROL.md).

The same construction verifies Boston's big-image hypotheses, so the
embedding alignment used in the family period comparison can be made on
this domain. Integral surjectivity then gives a unit Eichler--Shimura factor
in the source's own realization. This repairs a gap in the printed
dense-point argument rather than relying on it. The precise proof and its
scope are in [SOURCE_UNIT_REPAIR.md](SOURCE_UNIT_REPAIR.md).

In an explicit Sym^1 polynomial convention, define

    E_2(phi) = -coeff_Y phi({infinity}-{0}).

For the primitive specialized symbol phi_g this gives the actual integral
value

    M_p=E_2(phi_g)=L(g,2)/Theta_g in Z_p,
    Theta_g=(2*pi*i)^2 Omega_g^sym.

Both the sign projector and the period convention are specified in
[INTEGRAL_EVALUATION.md](INTEGRAL_EVALUATION.md).

## The exact unfinished comparison

The retained local result is exp*(Q_g)=p^(-2)O e_g and

    A_g=c_g L(g,2)/Omega_g^K,       b_p=v_p(A_g).

The newly constructed modular-symbol value therefore satisfies

    A_g=eta_p M_p,
    eta_p=c_g Theta_g/Omega_g^K.

The calculation has not proved eta_p is a unit, or computed its valuation.
Consequently b_p>=2 does not yet imply M_p is divisible by p^2. The
source's unit Eichler--Shimura factor cannot be substituted for eta_p
without transporting the Tate twist, dual representation, Gauss sum,
Atkin--Lehner factor and fixed Kato period vector. The exact relevant
[KLZ comparison maps](https://arxiv.org/abs/1503.02888) and this remaining
transport are recorded in [DE_RHAM_TRANSPORT.md](DE_RHAM_TRANSPORT.md).

This is the first unfinished gate of this pass. It is not a claimed
arithmetic upper bound in another notation.

## Collision and ancestor decisions

The four named degree-two objects were checked against their retained
definitions. In particular the branch-theta coefficient is a stabilization
of the definite-theta coefficient, with a correction invisible modulo
(p,I^3) under the recorded norm-relation hypothesis. A tame singleton
coefficient is not a singleton Kato class. The corrected two-step Betti
multiplier is (a_p-1)^2.

No equality with the W3 residual was proved in a matched integral lattice.
Thus there is no justified collapse verdict, and no justified claim that
W3 escaped the collision test. See [COLLISION_CHECK.md](COLLISION_CHECK.md).

No fixed ancestor was constructed. The brief's broader finitely generated
module version also needs a non-killing realization map: a nonzero fixed
element can map to zero at every p. Character variation alone is not a
proof that ancestors cannot exist. These exact limits are in
[FIXED_ANCESTOR.md](FIXED_ANCESTOR.md).

One correction preserves the weakest useful target. If eta_p is proved a
unit, the class p^(-2)M_p modulo p^2 being nonzero already proves b_p<=3.
Testing only modulo p would require b_p=2 and unnecessarily discard the
b_p=3 case. Neither divided class is certified here.

## What this can contribute to BSD

The construction removes varying coefficient ramification and the
primitive-symbol specialization ambiguity outside a fixed finite set.
It supplies the integral functional required by the proposed route.
These are prerequisites for converting the retained index inequality
into a modular-symbol bound. They do not supply that bound.

The still-unproved chain is:

    transport to the Kato frame with controlled valuation
      -> construct the correctly divided symbol
      -> settle its integral collision/ancestor comparison
      -> independently prove b_p<=3 cofinitely.

Only the last inequality would yield the admitted ordinary primary
vanishing through the retained theorem. Supersingular primes and the
remaining finite FIN obligations are separate. No new primary vanishing,
FIN, ORDER9 or Q36 result was obtained.

## Evidence and custody

The supplied ZIP matches the stated SHA-256 and contains one attack brief,
with no inner manifest. Twelve relevant retained files are copied byte-for-
byte and bound in INPUT_BINDINGS.json. Eight primary-source records are
hashed in SOURCE_BINDINGS.json; their read scopes distinguish theorem
reads from a downloaded background paper.

The exact controls pass in nine groups: the seed equation change and p=5
count; the Hasse inequality; the Boston parameter change; the evaluation
sign; the cyclic norm; and the divisibility/ancestor countercontrols.
They check formulas. They are not an independent proof of Hida control,
a computation of a seed index, or certification of the retained arithmetic
inputs. No fixed-prime witness campaign or paid/external job was launched.

The proof, executable controls and handoff are preserved for the user's
authorized lab upload. Publication and hash verification do not change
the mathematical grade.
