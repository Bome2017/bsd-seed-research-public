# The remaining de Rham transport: retain the actual source maps

The integral family calculation now has a stronger input than an abstract
rational period comparison. Nevertheless it is necessary to identify its
source and target before using it for the old local Kato frame.

## The integral comparison already available

KLZ, arXiv:1503.02888, Theorems 9.5.1--9.5.2 give Ohta's integral
isomorphism and its compatibility with the de Rham comparison, modulo the
Eisenstein part. On our non-Eisenstein localization that part is absent.
Proposition 10.1.1 gives the canonical differential functional on the
specified twisted ordinary graded representation and the complementary
functional with values in the branch congruence ideal.

On the cofinite domain constructed here the full localized Hecke algebra
is the branch Lambda itself. Thus the branch congruence module inside that
algebra is zero and its congruence ideal is the unit ideal. This removes a
possible congruence denominator on this domain. It does not say that an
L-value is a unit.

For a new specialization of level Np, KLZ Proposition 10.1.1(2)(a) explicitly
contains the factor

    alpha / lambda_(Np)(g),

with the Atkin--Lehner pseudo-eigenvalue in that source's convention.
Section 11.6 then keeps Gauss factors when comparing a dual integral
generator with de Rham vectors. These displayed factors cannot be
replaced by one merely because the congruence ideal is the unit ideal.

The source explicitly distinguishes q-expansion forms from its primed
de Rham forms in section 7.4. It also uses a dual representation, a
specified Tate/weight/nebentypus twist, and the arithmetic model of the
modular curve. Those distinctions are relevant at ramified level Np.

## The frame which must be reached

The retained local-index proof has quotient character

    O(alpha chi^(-1) omega)

inside U=D(g)(1), and fixes

    e_minus=tau(omega)*a_alpha*t tensor v_minus.

Its preimage e_g in Fil^0 D_dR(U) has the proved local lattice
exp*(Q)=p^(-2) O e_g. The Gauss factor tau(omega) has valuation
(p-2)/(p-1); it is not a unit. Twisting or dualizing changes the
character and potentially the corresponding Gauss factor. Pairing
against a de Rham vector is not automatically the same map as
expressing a vector in this frame.

The source maps just described therefore give a concrete transport
calculation, but this return has not completed that calculation with
the fixed Kato period vector. In particular it has not proved

    c_g*(2*pi*i)^2*Omega_g^sym / Omega_g^K in O^times.

One must transport the polynomial/Betti convention, the duality and
twist, the Atkin--Lehner factor, and the Gauss frame in the same diagram.
The embedding alignment in COFINITE_HIDA_CONTROL.md is available; it
is not authority to replace the earlier fixed Betti period vector
without doing this transport.

## Exact stopping point

The two improvements proved here remove coefficient ramification on a
cofinite domain and supply an integral Eichler--Shimura unit comparison
in its own realization. The comparison with the retained Kato frame is
still open. Its content has not been renamed a solved unit, and no
divided residual object is declared integral on that basis.

This is the first unfinished step in the present construction, not a
claim that it is the only unfinished step before uniform BSD.
