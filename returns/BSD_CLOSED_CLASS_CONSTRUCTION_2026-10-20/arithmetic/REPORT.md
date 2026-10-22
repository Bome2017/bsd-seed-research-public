# Closed geometric class-relation test on the actual seed

Date:2026-10-20. Status:`NO_CLOSED_BOUND_FROM_TESTED_GEOMETRIC_FAMILY`.

The producer was changed from relative LLL reduction to genuine elliptic-function values. It uses the actual seed's nonzero5-torsion point field and no old196-row combinations, BNF computation, known Sha order, or control curve. The tested family supplies no new closed relation rank on the retained complete bounded-prime inventory. FIN, ORDER9 and Q36 are unchanged.

## Construction and admission

On E:y^2=x^3-22735x^2+106272484x, an exact scan of1<=x<=100000 found the six positive integral points

    (576,232080), (4547,327384), (5184,281520),
    (5843,210348), (18188,654768), (23372,1682784).

The second and third are the retained basis points. Their basis status is not needed for these principal-ideal identities; every point is checked directly on the curve.

The predeclared family comprises six tangents, six lines through the rational2-torsion point(0,0), fifteen chords between positive points and fifteen chords with the second point negated. Exact duplicate removal leaves31 functions f=y-mx-b. At the actual nonzero5-torsion point T, each alpha=f(T) is nonzero.

If F(x)=x^3-22735x^2+106272484x and psi5 is the degree12 division polynomial, then the quadratic relative norm of y-mx-b is (mx+b)^2-F(x). As [Aplus:Q]=12 is even, its absolute norm is

    Res_x(psi5(x), F(x)-(mx+b)^2) / lead(psi5)^3.

The code checks this against the exact number-field norm for every function. All31 pass the identity. Their rational norm numerators have144–267 decimal digits. Removing every rational prime below419776 leaves outside cofactors of42–237 digits. Thus none is individually admitted as a closed bounded-support relation. This was determined in0.13seconds; no attempt was made to factor those large remainders completely or blindly enumerate further lines.

## Exact common-factor repair

The next stage allows common outside factors to cancel among this same finite family. It includes all four scalar conjugates, giving124 actual elements. For each alpha, the least denominator in the retained integral basis is recorded as d. Both integral ideals (d*alpha) and(d) are retained, and their quotient is checked to equal(alpha). Rational denominators are therefore neither forgotten nor silently declared units.

Exact ideal gcd refinement gives134 pairwise-coprime ideal atoms. Their scalar action is a verified permutation. Every numerator and denominator ideal reconstructs exactly over this support. The atoms are actual ideals, possibly composite, rather than assumed prime classes.

Under each faithful character of the scalar C4 over F5, the support has28 columns. Six have support entirely at prime ideals of norm<=419775;22 have actual support outside this bound. The latter assertion is checked by partial integer factorization of each atom norm and actual prime-ideal valuations at every small rational factor. An atom's total norm alone is not used as a support certificate.

The code separately tests outside-divisor primitivity modulo5. None of the22 outside columns has unresolved fifth-power ambiguity. Pairwise-disjoint support and scalar closure then let the outside columns detect exactly the tested family's outside divisor classes modulo5.

The projected matrices have

    rank(R_chi)=20,
    rank(R_chi,outside)=20

for chi(sigma)=2 and chi(sigma)=3. Thus

    rank of relations supported on bounded primes =20-20=0.

This tests combinations after common-factor cancellation, not merely individual line functions. It accounts for the possibility that outside divisors cancel modulo5 rather than integrally. There is no new row to transport into the complete8918-column conditional generator list. The retained complete bound remains8918 in each faithful character; it does not become the selected presentation dimension28-20=8. The complete inventory's GRH qualification also remains unchanged.

## Exact unit closure

The anti-divisor matrix of the124 elements has rational rank40 and kernel dimension84. For each rational-kernel basis vector, after clearing denominators, the corresponding product of alpha/tau(alpha) is evaluated exactly in A and its ideal is checked to be the unit ideal. All84 products are exactly1.

Clearing rational-kernel denominators need not produce the saturated integer kernel. Nevertheless no non-torsion unit is hidden here: for any saturated-kernel product u, some u^n is an integer product of the tested units and equals1. Hence u is a root of unity. A has a real embedding, so u is +/-1, both trivial modulo fifth powers.

This conclusion concerns the complete multiplicative relation kernel of this fixed family. It is not a theorem excluding other relative units or other geometric sources.

## Relation to the earlier geometric control

The earlier655a1 coefficient7 tangent/chord family also had sign-valued unit products. That finite-family result was read before this run and was not promoted to an impossibility theorem for the seed. Here the objective was different: class relations closing on a fixed complete-prime list. The actual seed family was tested directly, including outside-support elimination. It also fails that objective, for the precise rank reason above.

## Evidence and disposition

- `norm_rows.gp`: all31 actual elements, exact norms/resultants, bounded partial factorizations and residual norm cofactors.
- `geometric_support.gp`:124 elements, numerator/denominator ideals,134 coprime atoms and actual scalar permutation.
- `geometric_rank_data.gp`: complete divisor reconstruction, both faithful matrices, support classifications and empty outside-fifth ambiguity list.
- `geometric_rank_result.gp`: [124,134,28,6,22,20,20,20,20,0,0,[]].
- `geometric_unit_kernel.gp`: exact anti-divisor matrix and84-column rational kernel.
- `geometric_units_result.gp`: all84 exact product outcomes.

The raw runner receipts bind entry scripts and retain direct stdout/stderr. Accepted elapsed times are0.13seconds for norm admission,56.72seconds for gcd refinement,57.02seconds for support/rank checking and0.72seconds for exact unit products. Each stage had a120-second process-group wall limit and a512MB PARI stack cap; measured peak RSS stayed below78MB.

The source record is bound by INPUT_BINDINGS.json. The final manifest binds all executed files. Scripts append evidence, so production replay must use a clean output directory. The independent review lane authenticates the final scope separately; its report is authoritative about which computations it actually replayed.

The finite family is stopped. Repeating it with more powers or treating outside cofactors as absent would not address the bound. No complete class-group result, new seed-prime certificate, or endpoint result is claimed. No remote computation or publication was performed by this worker.
