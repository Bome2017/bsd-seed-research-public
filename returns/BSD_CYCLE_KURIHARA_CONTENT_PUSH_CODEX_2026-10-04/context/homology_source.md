# An actual fixed integral source and its specialization maps

Status: proved construction using modularity, the retained Manin/isogeny data, elementary topology and Ota membership. It exists before FIN. The uniform content estimate is not proved.

## Source

Let X=X_0(N)(C), H=H_1(X,Z), and M_Z=Hom_Z(H,Z). The compact modular curve is a finite-genus compact Riemann surface, so H and M_Z are finite free of rank 2g. No basis of this enormous lattice is computed here.

Choose the modular parametrization pi:X_0(N)->E with pi(infinity)=O, obtained by the optimal quotient to E_0 followed by an isogeny E_0->E. The retained seed data give degree at most two for that isogeny and

    pi^*(omega_E)=c_E * 2pi i f(z) dz,
    c_E divides 2^9.

The variable c_E is the Manin factor of this parametrization, not an unknown content bound for WC. Let Omega_O denote Ota's positive real period: the generator of the real projection of the period lattice of E. Define

    z_E(C)=Re integral_{pi_* C} omega_E / Omega_O,  C in H.

This is an integer by the definition of Omega_O. It is a nonzero homomorphism, hence an actual distinguished z_E in M_Z. No L'' value, Sha group, post-FIN determinant generator or conjecture defines it.

The source is primitive at all odd p. Indeed H_1(X,Z)->H_1(J_0(N),Z) is an isomorphism. The optimal quotient J_0(N)->E_0 has connected kernel, so it is surjective on the integral homology lattices. The isogeny E_0->E has homology image index its degree, at most two. Real projection divided by Omega_O is a surjection H_1(E,Z)->Z. Thus z_E(H) has index dividing two in Z. Only the weaker conclusion 'prime-to-p source content for p in P' is needed here. It does NOT imply primitive images below.

## Explicit cycles

For gcd(S,N)=1 and a in (Z/S)^*, the cusp a/S is equivalent to the cusp 0 under Gamma_0(N). Let gamma_{a,S} be the path from infinity to a/S and gamma_0 the path from infinity to 0, regarded on the compact quotient. Then

    C_{a,S}=gamma_{a,S}-gamma_0

is an integral absolute 1-cycle. Although the endpoints have different rational representatives upstairs, their cusp points on X agree. The orientation is chosen so that the integral of 2pi i f dz from infinity to a/S is 2pi integral_0^infinity f(a/S+it)dt.

The retained analytic rank gives L(E,1)=0, so the integral on gamma_0 is zero. Therefore, with Ota's plus symbol,

    z_E(C_{a,S})=c_E [a/S]^+_O.                      (H1)

This directly realizes the relevant symbols in a fixed integral lattice. The denominators here divide the fixed power of two c_E. No relative-cusp torsion bound or ad hoc rational splitting is required.

## Exact specialization

Fix p in P, an admissible S, and for each ell|S a generator sigma_ell of the maximal p-quotient of (Z/ell)^*. Put e_ell=v_p(ell-1). For a in (Z/S)^*, write x_ell(a) for the integer in [0,p^e_ell-1] giving its exponent in that quotient. Write X_ell=sigma_ell-1. Define integral cycles

    C_i(p,S)=sum_a binom(x_i(a),2) C_{a,S},
    C_ij(p,S)=sum_a x_i(a)x_j(a) C_{a,S}.

Using the decomposition in TWO_PRIME_SUPPORT_THEOREM.md, define the Z-linear map

    phi_{p,S}: M_Z -> M(p,S)
    phi_{p,S}(lambda)=c_E^(-1) [sum_i lambda(C_i) X_i^2
                               +sum_{i<j} lambda(C_ij) X_i X_j].       (H2)

The inverse of c_E is taken in Z_p; its use introduces no p-denominator. The codomain is the full degree-two quotient, using the canonical isomorphism from the maximal p-quotient. Choices of generators and logarithm lifts are stated explicitly; changing them does not change the intrinsic depth of phi_{p,S}(z_E).

**Theorem H3.** phi_{p,S}(z_E)=t(p,S).

Proof. Expand the image of a in the group ring as product_i (1+X_i)^x_i(a) modulo I^3. Its quadratic coefficients are precisely the binomial and mixed weights in (H2). The plus contribution agrees by (H1). The minus symbols are odd under a->-a, while each x_i(-a)=x_i(a) because the p-quotient kills -1. Their weighted sums vanish. Finally theta_S belongs to I^2 by Ota 5.17. In the truncated presentation for odd p, the linear and quadratic monomial modules have the direct relations given in T1, so extracting these quadratic coefficients gives its class in I^2/I^3. QED.

This constructs the schematic source M_Z, distinguished z_E and every required specialization. It does not construct the integer A in WC.

## Kernel, image and the arithmetic obstruction

The kernel of phi_{p,S} is exactly the set of lambda for which lambda(C_i)=0 modulo p^e_i and lambda(C_ij)=0 modulo p^min(e_i,e_j). The source has a large kernel because the target is finite. The image and cokernel are finite p-groups obtained from this explicit evaluation matrix. A determinant over Q_p is not a useful invariant: the entire target vanishes after tensoring with Q_p. Relevant invariants are Smith factors of the finite evaluation matrix and, more specifically, its value on z_E.

For the top-support cycles at one- or two-prime levels, the remaining problem is whether their periods under this ONE primitive functional generate a uniformly large ideal. It is not the primitivity of the full homology module, nor the source Manin denominator, nor the size of the whole image of phi. INTEGRAL_COMPARISON_ATTACK.md states that exact remaining arithmetic lemma.
