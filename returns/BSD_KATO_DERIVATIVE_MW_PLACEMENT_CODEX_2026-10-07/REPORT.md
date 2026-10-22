# The derivative lies in the integral point lattice

**MW_PLACEMENT_DERIVED_FROM_RETAINED_WEAK_ORDER_INPUTS.**
Written deduction; independent review pending.

There is a further consequence of the retained weak-order argument:

    ∂_γ z=a_p κ(P₁)+b_p κ(P₂),    a_p,b_p∈Z_p,

for its actual smoothed, simultaneously transported derivative at every
good p≥5 on the retained residual-image domain. This includes supersingular
primes and does not assume primary Sha finiteness.

The rational step is short. A zero derivative is in the point plane.
A nonzero derivative already forces rational H¹ to have dimension two,
so the known rank-two point plane is the entire space in that case.
The integral step uses compatible finite Kummer maps to prove that the
full Mordell–Weil image is saturated in integral H¹. It does not divide
an unknown normalization factor.

This corrects the previous status of **placement of this derivative**.
The previous source-interface checks stay closed at their stated grade;
this is not another repetition of those checks.

The result does not calculate a_p or b_p or prove either nonzero. The
coefficients may both vanish or both be divisible by p. They are p-adic
coordinates, not one prime-independent rational scalar. The analytic
Bockstein identity and the integral tame comparison are still unproved.

**Effect toward the seed:** the derivative route now has an integral
Mordell–Weil-valued object before FIN. A comparison may therefore target
that lattice without first assuming finiteness to identify all of H¹
with Mordell–Weil. No nonvanishing theorem or Sha bound follows from
placement alone. FIN, ORDER9 and Q36 are unchanged.

[Full proof](PROOF.md) · [Review handoff](HANDOFF.md) ·
[Sources and reading boundary](SOURCES.md) · [Scope controls](CONTROLS.md)

The source inputs and their grades are bound in INPUT_BINDINGS.json.
Custody verification is not independent mathematical verification.
