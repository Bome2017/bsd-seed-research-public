# Local review of the supplied cohomological jet

Grade: CONFIRMED_UNDER_RETAINED_HIDA_INPUTS. This is a mathematical check of the local argument, not an independent reproof of COFINITE_HIDA_CONTROL.md.

Let R=Z_p[[T,S]], m=(p,T,S), and retain exactly the characters and lattices in the input PROOF.md. In particular

    U=V(T) nu_S^(-1),
    A=R(alpha(T)^(-1) chi nu_T nu_S^(-1)),
    M=R(alpha(T) nu_S^(-1)).

The residual character alpha-bar is nontrivial unramified. The residual characters of A and M have no H^0, and their Tate dual characters also have no H^0. Local duality and Euler characteristic give residual cohomology concentrated in degree one, of dimensions 1, 1, 2 for A, M, U.

KLZ Proposition 11.2.1, in its finite-free application here, supplies perfectness and derived base change. A minimal finite free complex over R has zero differentials after reduction modulo m. The preceding residual calculation therefore forces that complex to have just one nonzero term, in degree one. Thus

    RΓ(Q_p,A)=R[-1], RΓ(Q_p,M)=R[-1],
    RΓ(Q_p,U)=R^2[-1].

It follows that H^1 base change is exact for these modules, including all the finite quotients and arithmetic specializations used below. This conclusion concerns local cohomology. No analogous global base-change surjectivity is used.

The local quotient H^1(U)/H^1(A)=H^1(M) is free of rank one. Ochiai 2003 Proposition 5.1 gives a map with pseudo-null kernel and cokernel on the matched quotient. A homomorphism R→R with this property is multiplication by a unit: a nonzero nonunit would have a height-one divisor. Therefore the local Coleman map is an integral isomorphism before specialization.

The source matching is literal at the level of representations. Take the cohomological family V(T)^vee, then apply the cyclotomic character chi nu_S. Its Kummer dual is U. On the principal-unit coordinate X used for that source,

    X=p+(1+p)S,

and the tame component is omega. Normality, Gorensteinness, the ordinary free filtration and (MW) are retained hypotheses. They are not inferred from an arbitrary rational Hida branch. The coordinate change is an automorphism of the integral local ring and preserves m^n.

The submitted diagonal test and its integral-multiple variant are correct. The example T-S correctly refutes the assertion that every nonzero jet is detected on the diagonal. TEN_POINT_CERTIFICATE.md changes the arithmetic specializations and proves a different assertion; it does not overturn that example.

The preceding work's scalar eta_p is not shown to be a unit. Nothing here identifies its complex period with the integral Coleman frame.

The input archive verified 7/7 manifest entries. Its standalone checker reproduced the supplied output. Those checks concern finite-ring formulas, not seed Kato values.
