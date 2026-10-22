# A reusable first-order graph norm lemma

Status: elementary written algebraic deduction. This lemma is a method for computing a residual normalization, not a theorem bounding Sha.

Let O=Z_(p), p odd. Let d:C1 -> C0 be the boundary map of a connected finite graph. Give the free chain modules perfect O-valued symmetric pairings, and let d^dagger be the adjoint. Assume all edge and vertex weights are p-units. Put X=ker d. Suppose an integral potential xi satisfies

    d*d^dagger xi = p*b,

and an actual cycle v in X satisfies

    v = c*d^dagger xi mod p,  c in O^times.

Choose a degree-zero divisor D, an edge chain z with dz=D, and the source functional x_D(w)=<z,w> on X. Assume s=<D,xi> is a p-unit. Then

    <v,v>/p = -c^2<xi,b> mod p,
    x_D(v) = c*s mod p,

and consequently

    <v,v>/(p*x_D(v)^2) = -<xi,b>/s^2 mod p.

Proof: write v=c*d^dagger xi-p*w. The boundary equation gives dw=c*b. Expanding its norm and using adjointness yields

    <v,v> = p*c^2<xi,b>-2p*c^2<xi,b>+p^2<w,w>.

The source equation follows from <z,d^dagger xi>=<D,xi>. Both formulae are independent of the unknown correcting flow w. Replacing z by z+x for x in X changes the residual source evaluation by <x,v>=0 mod p, because vbar is a gradient. This proves the claim.

For an elliptic toric quotient with geometric component order p, functorial monodromy makes <v,v>/p its polarized quotient degree. The lemma then computes degree/component-index-squared modulo p from a much smaller vertex potential. For general component order p*u with u a unit, divide the displayed quotient by u as well.

Its admission checks are substantive: the weights must be p-units, the actual quotient vector must reduce to the displayed gradient line, and the component source must be the same D. Merely finding a Laplacian eigenvalue divisible by p does not certify any of those identifications. The 167 application verifies them under its retained C3 inputs and fixes D on the even summand to avoid a parity-coordinate ambiguity.
