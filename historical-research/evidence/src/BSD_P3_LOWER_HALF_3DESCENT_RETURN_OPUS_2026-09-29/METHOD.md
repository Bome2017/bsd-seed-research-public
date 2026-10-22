# Method (search side and certificate side), Lane B2

## Search (may use GRH; nothing here is trusted by the verifier)
1. L = Q(T): Res_x(psi_3(x), u^2 - (4x^3+b2x^2+2b4x+b6)), polredbest -> same octic as the 09-18 record.
2. Sel_3 inside L^x/L^x3 (Schaefer-Stoll): L(S,3) from bnfunits (compact S-units) + Cl_S[3] lifts (GRH bnf);
   local images of E(Q_l)/3E(Q_l) at l | 3N from Hensel-lifted local points (valuation + ideallog mod p^n,
   n = floor(3e/2)+1 at p | 3); global conditions N_{L/L4}(alpha) in L^x3 and "additivity" (at primes split in
   L, S -> chi_p(alpha_S) is a homomorphism E[3] -> F3). Without the last two, fake classes appear (681b1).
3. Class -> cubic: A_xi = (Q x L, *_alpha), (b*b')_U = sum_{S+S'=U} gamma(S,S') r_{S+S'}/(r_S r_{S'}) b_S b'_{S'},
   M_S M_S' = gamma M_{S+S'} (Heisenberg matrices of translation by S on the Weierstrass cubic), r_S^3 = alpha_S.
   alpha' = alpha/tau(alpha) (tau: T -> -T) makes alpha' tau(alpha') = 1, which pins the cube roots at primes
   with Frobenius of order 8 (r_T r_{-T} = 1). Constants mod such p, CRT + rational reconstruction (adaptive).
   PARI alginit(Q, mt) -> maximal order; LLL-reduced order -> rank-1 element e -> 3-dim module O e ->
   psi_2 : A_xi -> M_3(Q); intertwiner g with psi_2 = g psi_1 g^-1 mod p gives U_C = U_E o g^-1 mod p; CRT.
   Famat exponents are reduced mod 3 first (exact cube quotient), so compact units are never expanded.
4. Size reduction by transvection descent.

## Certificate (verify_certificate.gp; exact, unconditional; recomputes everything from the cubic)
1. c4, c6 from Hessian covariants: q4 = (d/de H(U+eH(U)))/U, H(H(U)) = A U + B H(U); constants calibrated in
   the verifier on the generic Weierstrass cubic (c4 = q4/12, c6 = B/16, A = 48 c4^2). Jac(C) = E iff
   (c4,c6)(C) = (s^4 c4, s^6 c6)(E), s in Q (Artin-Rodriguez-Villegas-Tate).
2. Local solubility: R (odd degree); l in {2,3} u primes(N) u primes(Delta(C)): explicit point P with
   v_l(U(P)) > 2 min_i v_l(dU/dx_i(P)) (multivariate Hensel). Other l: l does not divide 6 Delta(C), so C mod l
   is smooth (the primitive discriminant vanishes on singular cubics over F_l-bar), Hasse-Weil gives a smooth
   F_l-point, Hensel lifts it (this is where "Lang" is used).
3. Class images: phi_T(xi) = e_3(.,T)_* res_L(xi) in L^x/L^x3 (a homomorphism). phi_T(kappa(P)) = f_T(P),
   f_T = tangent line at the flex T. phi_T([C]) = Cardano class of the line algebra of the unique L-rational
   triangle U + t0 H(U) (t0 an L-root of the Hesse quartic; Delta(U + tH) = kappa Q(t)^3): the 3 lines are the
   cosets of <T> in the flex torsor, a mu_3-torsor via e_3(.,T); its etale algebra fixes the class up to
   inversion. Uniqueness of the L-rational subgroup <T>: psi_3/(X - x_T) has no root mod a degree-1 prime.
4. Independence: cubic residue symbols at degree-1 primes (p, w - r), p = 1 mod 3, p not dividing disc(fL);
   F3-rank = number of classes. Inversion ambiguity does not affect rank.
