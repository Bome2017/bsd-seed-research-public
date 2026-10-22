# Review of the submitted algebra

**Verdict: CONFIRMED_UNDER_P1_TO_P4.**
This is a written mathematical check of context/SUBMITTED_CRITERION.md,
not kernel verification.

The consequential steps are correct:

1. If y=g m₀ in the free rank-one M and g∈(p,U), augmentation of y is
   divisible by p in H. Thus residual nonvanishing makes y a generator
   and M/Rz≅R/(U).
2. The coefficient triangle supplies H/pH→H¹(C⊗^L k) injectively. Hence
   the cycle y is nonzero modulo the maximal ideal in a free two-term
   representative. A unit coordinate permits it to be split off.
3. The remaining square map is injective because ker d=Ry. Its cokernel
   is the actual X, not a pseudo-isomorphic replacement.
4. Height-one bounds at all primes make its determinant divide U in the
   regular local UFD. A unit determinant contradicts the rank-two point
   lattice after augmentation.
5. If the residual matrix had corank at least two, unit-pivot elimination
   would leave a block of size at least two with all entries in (p,U);
   its determinant would belong to (p,U)². This contradicts det D∼U.
6. Reducing the split complex gives residual H¹ of dimension two. The
   Selmer/Kummer exact sequence then gives the claimed primary vanishing.

The proof does not use parity or an initial Sha-finiteness assumption.
The assumption of a perfect complex with Tor-amplitude [1,2] is essential;
cohomological concentration in [1,2] alone would not suffice.
INTEGRAL_MATCHING.md §7 supplies that distinction for the seed complex.

The submitted countercontrol is valid:

    C_e=R[-1]⊕[R^(e+1) --diag(U,p,…,p)--> R^(e+1)]

has primitive divided augmentation and U-local length one, but residual
H¹ dimension e+2. Its p-local H² length is e, whereas that of R/(U)
is zero. It therefore fails exactly the integral inequality at (p).

One source citation needs correction. The printed display in Kato 12.5(4)
is rational. The integral theorem used in this return is 13.4(3), with
the modular-source passage of 12.6 and 13.14 and explicit local checks.
The correction changes the citation and verification route, not the
validity of the abstract algebraic implication.

No full Smith normal form over Z_p[[U]] is assumed. Unit-pivot elimination
works here because the residual corank has already been proved to be one.
