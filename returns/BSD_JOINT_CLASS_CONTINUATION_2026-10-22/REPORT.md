# Continuation toward a complete FIN source bound

2026-10-22. **NO_NEW_SMALL_CLASS_BOUND.** The actual seed experiments below
were executed; the analytic reconstruction is a valid sufficient certificate
whose arithmetic inputs have not been produced. FIN, ORDER9, Q36 and seed
prime coverage are unchanged. No claim of literature novelty is made.

The retained complete relative five-primary length bound is still **97**.
The previous direct primary-packing test gave the weaker ceiling 106. This
return did not rerun that packing calculation, optimize the failed BNF
certification, or count another selected relation matrix as complete.

## 1. Two changed constructions were tested and stopped

**A small-support arithmetic source on the actual seed.** Seven torsion-coordinate
elements in the degree-24 five-torsion point field really are S-units, with
support above {2,3,5,2243,4547,5843}. Exact principal-ideal reconstruction
verifies this; norms alone would not suffice. But their faithful scalar
projections all vanish. The program constructs fourteen literal fifth-power
identities, one for each element and faithful character. The parity proof
also excludes multiplicative scalar combinations and roots that remain
inside this field. Thus this source does not contribute a missing faithful
unit or class direction. This does not exclude larger-field or line-bundle
sources. [Arithmetic](arithmetic/REPORT.md) · [Proof](arithmetic/PROOF.md).

**More incidence norms from the same torsion geometry.** All equivariant
point-to-covector correspondences are combinations of the orbits
lambda(v)=t. On the faithful character, N_0=0 and N_t=chi(t)N_1 for t nonzero.
Consequently stacking these maps cannot reduce the existing class kernel.
The proof is uniform in p; exact checks at 3,5,7,11,13 support its implementation.
Separate finite-module controls show why the relations uv=vu=p and an exponent
bound alone do not bound class multiplicity. These are scoped exclusions,
not impossibility theorems for arithmetic class maps.
[Derivation](theory/HISTORICAL_AND_OPERATOR_SCREEN.md).

## 2. A partial presentation has an explicit, indispensable error

For complete finite p-group presentations P_A -> C_A and P_B -> C_B,
with kernels K_A,K_B and a compatible lift U of the actual class map u,
the snake lemma gives

    d_p ker(u) <= d_p ker(U) + d_p(K_B/U(K_A)).

Thus a complete source surjection and an exact target p-presentation suffice;
the whole source class number is unnecessary. However, an invertible selected
matrix can still conceal arbitrarily many genuine class-kernel directions
in its target relation error. More digits do not remove that error.
[Accounting](sources/PRESENTATION_DEFECT.md) ·
[Separate proof review](review/PRESENTATION_AND_PARITY_REVIEW.md).

The old source quotient-certificate attempt already used PARI's weaker
bnfcertify flag1 and timed out. It was found in the record and was not
reintroduced as a new workaround. A p-saturated unit subgroup alone also
does not certify a partial class presentation: missing generators and
missing relations can cancel in an analytic product check.

## 3. The remaining concrete alternative: reconstruct the relative class part

A different certificate avoids that presentation cancellation. Let E_0
be a rank-six subgroup of the actual norm-one units, V_0 its covolume,
j its index in the full relative-unit lattice, and I the retained
power-of-two unit index, I<=128. If E_0 is independently five-saturated,
then 5 does not divide j. The relative analytic class-number formula gives

    T/(64 V_0) = (h_A/h_K)/(I j),
    T = sqrt(D_A/D_K) L_K(1,psi)/(2 pi)^6.

The retained lower bound on the entire relative-unit covolume bounds j.
A certified narrow interval then isolates this rational number, whose
five-adic valuation is exactly the complete relative five-class length.
This concerns all classes, including those absent from a factor base.
It uses an independent number-field L-value, not an elliptic BSD or Sha
value. The construction and its finite precision gate are in
[RELATIVE_RECONSTRUCTION.md](sources/RELATIVE_RECONSTRUCTION.md).
For an upper bound, an independent bound v_5(j)<=a can replace saturation:
the resulting bound is v_5(h_A/h_K)<=v_5(t)+a. Exact determination of j
and strict five-saturation are not compulsory if that allowance is small.

**This is not yet an admitted seed computation.** The inspected completed
packets supply neither six such authenticated five-saturated relative units
nor a certified two-sided enclosure for that relative L-value. The old
one-sided bound does not isolate its valuation. The current sufficient
reconstruction scheme requires an absolute L-interval narrower than
9.1e-53 even under its most favorable use of the retained general index
bound. This is a precision condition for this scheme, not a theorem about
the minimum cost of every possible method. No large L-value job was launched.

The seven new S-units in Section1 cannot supply those six relative units:
their images have the wrong parity. Reusing them, or renaming the known
point/class specimens a complete unit lattice, would not fix this gate.

## 4. What is actually left open

There remain two distinct ways to address the complete class contribution:
an independently certified class presentation/kernel with its error bounded,
or the relative analytic reconstruction with genuine unit and analytic inputs.
Neither is supplied by this return, and neither has a demonstrated uniform
scaling theorem. Even a successful fixed-p reconstruction would still need
the existing unit/norm/local accounting and a new across-prime argument to
give FIN. These possibilities must not be advertised as a known route to
completion.

This run therefore records failed bounded constructions and a precise
alternative certificate, **not an improvement in the seed bound**. The
general FIN class route remains open; the specific source and orbit-map
variations in Section1 should not be repeated unchanged.

## Verification and custody

The root independently reran the actual seed S-unit calculation and the
finite orbit checks. A separate agent reviewed the presentation/parity
proof and the relative reconstruction. That is a same-session machine-agent
review, not human review or formal verification. The source/lattice interfaces
listed in the proofs retain their prior grades. See [REPLAY.md](REPLAY.md),
[SOURCES.md](SOURCES.md), and the manifests. Publication does not strengthen
any mathematical grade.
