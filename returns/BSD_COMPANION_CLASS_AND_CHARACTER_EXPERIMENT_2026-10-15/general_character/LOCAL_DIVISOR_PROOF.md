# Primitive divisor incidence and the389 control atp5

This proves the ramification factor used in the finite local model. It does not replace the actual point-field class certification.

Let K be the splitting field of E[p]. Fix a rational prime q and a place of K aboveq, with decomposition group D and inertia I. Primes of A and B aboveq correspond to D-orbits on nonzero vectors and covectors. For a source orbit P write e_P for the size of the I-orbit of a representative; this is the ramification index of A_P/Q_q. Similarly define e_Q for a covector orbit.

For alpha in A, normalized valuations satisfy

    v_K(alpha(x)) = (|I|/e_P) v_P(alpha),   x in P.

For a chosen representative lambda of a target orbitQ, the incidence norm is the product over x with lambda(x)=1. Dividing its K-valuation by |I|/e_Q therefore gives the actual primitive divisor matrix

    u_D(Q,P) = (e_Q/e_P) * #{x in P : lambda(x)=1}.   (1)

The value is independent of the representative lambda by D-equivariance. Its integrality follows also from its construction as a map of divisor lattices. Omitting e_Q/e_P would compute the wrong map at a ramified prime. The source and target are primitive prime-divisor lattices; no class-group or S-unit saturation index is hidden in(1).

For389a1, the retained local arithmetic gives split multiplicative reduction at389 and minimal discriminant valuation1. At coefficient5, Tate inertia is primitive unipotent, and a compatible local model is

    I=< [[1,1],[0,1]] >,
    D=< I, diag(389 mod5,1) > = < I, diag(4,1) >.

The actual rank-two full residual image is a separate retained input. The finite model check is not a fresh proof of that image.

The source orbits with y=0 have nontrivial scalar stabilizer -1, so they contribute nothing to odd chi. The four source orbits y in F5^* have ramification5 and carry one copy of the faithful scalar character. In B, the four singleton covector orbits(0,b) have ramification1 and carry the inverse character; the remaining orbits again vanish in odd characters.

For lambda=(0,b), the relevant source orbit has y=b^-1 and has five incidence points. Equation(1) multiplies that count by1/5. Thus the character norm is the unit permutation y=b^-1:

    t_D,chi(389)=0.

check_local_divisors.py calculates all six source and six target D-orbits, all ramification indices, the entire primitive integer matrix and both scalar eigenspaces. It verifies the one-dimensional chi-to-chi^-1 map is1 modulo5. This checks the geometric consequence of the local inputs. The separate p5_arithmetic worker computes the actual point-field prime decomposition and scalar action, which can authenticate the local orbit description without identifying it from a desired bound.

At the coefficient place5, the separate actual prime decomposition/scalar action reports no faithful-character divisor component. The relevant ordinary unit root is2 modulo5. Do not silently infer this prime's absence only from a generic good-reduction slogan; the actual scalar action on its prime-divisor lattice is the available exact check.

If the ordinary source5-class group is certified to have no faithful-character component, formula(4) of PROOF.md now gives upper bound3 for the whole admitted global source. A BNF estimate with certification stopped at a time cap supplies only a conditional class input. The geometric calculation does not upgrade its grade.
