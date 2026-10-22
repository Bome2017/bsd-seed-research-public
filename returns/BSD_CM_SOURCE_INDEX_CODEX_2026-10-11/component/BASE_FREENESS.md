# The actual base Hecke factor at 5

Grade: exact Brandt computation plus a written module deduction, using the retained quaternionic/Hecke realization. This is not a claim that an arbitrary rational eigenprojection is an integral Hecke operator.

The base is E0=[1,1,1,3,12], conductor2541, and the definite Brandt module is M=Z[S(3,847)]. Sage constructs176 ideal classes, all with monodromy weight1. The saved exact matrices T2,T13,T17 are symmetric with row sums3,14,18. For eigenvalues−1,−7,−3, their simultaneous right eigenspaces have dimensions

|Operators imposed|Q|F5|
|---|---:|---:|
|T2|11|11|
|T2,T13|1|4|
|T2,T13,T17|1|1|

The primitive rational eigenvector f has integral coordinates, sum0, gcd1, and norm144. `checks/verify_base_brandt.py` independently checks the saved integer matrices, their eigenvector, and all three residual dimensions using standard-library modular elimination. It does not independently construct the matrices.

Use the retained Jacquet–Langlands identification of the rational E0 eigensystem. Since the three displayed rational operators already isolate a single line, it is the E0 line for the full commuting Hecke algebra. In particular T167 f=a167(E0)f=−12f. All these operators are self-adjoint for the indicated unweighted pairing.

Over Z5 the unit norm144 supplies the Hecke-stable direct sum

M⊗Z5=Z5 f ⊕ f^perp.

Let m be the residual E0 Hecke maximal ideal. The common eigenspace in M/5M for the three operators is exactly F5 f. Hence its intersection with f^perp/5 is zero. If the m-localized perpendicular summand were nonzero, its reduction would be a nonzero finite module over the corresponding Artinian local Hecke algebra. Such a module has nonzero socle annihilated by m; the residue field is F5, so that socle would supply a common eigenvector for the three operators in f^perp/5. Contradiction. Thus the localized perpendicular summand vanishes.

Consequently the actual localized module is Z5 f, with its actual localized Hecke algebra Z5. It is free of rank one. This proves the base-freeness hypothesis at5 used in the retained C3 assembly, without inferring Hecke membership merely from the denominator144 of an endomorphism projector.

This does not reprove the geometric C3 exact sequences or their Picard/Albanese convention transport; those remain the explicitly retained written inputs in the predecessor. It supplies their specific base-lattice hypothesis for this control model.
