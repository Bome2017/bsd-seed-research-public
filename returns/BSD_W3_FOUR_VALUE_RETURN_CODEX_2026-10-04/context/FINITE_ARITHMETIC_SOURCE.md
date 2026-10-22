# Four weight fibers suffice to define the genuine finite jet

Grade: DERIVED_FACTORISATION_OF_AN_IMPORTED_ARITHMETIC_CONSTRUCTION. This is not an executed evaluation of the seed's coefficients.

Fix the optimized integral Kato family Z_p of ARITHMETIC_SOURCE.md. For u=0,1,2,3 put

    t_u=(1+p)^(10+u)-1,
    I_u=(T-t_u),
    J=Π_(u=0)^3(T-t_u).

The four I_u are distinct height-one principal prime ideals of Z_p[[T]]. Their intersection is their product, even though they are not comaximal. Hence the same identity holds after adjoining S. Each factor belongs to m=(p,T,S), so J belongs to m^4.

The source theorem's integral gluing construction provides the compatible Euler-system class modulo J from its four weight fibers. These are actual modular Kato systems of weights 12,13,14,15 with the source's common primitive family symbol normalization. This is where arithmetic compatibility is used. Four arbitrary local values, or four classes which only agree after inverting p, cannot be substituted.

Reduction gives the finite arithmetic map

    Z_(J)(1) in H^1(global,U/JU)
      -> H^1(global,U/m^4 U)
      -> H^1(Q_p,M/m^4 M)
      -> R/m^4.

Its output is F_p mod m^4. The local arrows are exact by LOCAL_REVIEW.md. The global arrow is simply the image of the supplied integral class, not a claim that every class over U/m^4 lifts globally.

The gluing can also be viewed as taking the global class supplied by the published theorem and reducing it modulo J, then m^4. No reproof of the theorem's gluing step by informal interpolation is being substituted for the source.

The cyclotomic coefficient character has a finite quotient at this precision: for p≥5,

    (1+S)^(p^3)-1 in (p,S)^4.

Indeed the coefficients of S,S^2,S^3 have valuations at least 3, and all higher-degree terms have total degree at least four. The shift X=p+(1+p)S preserves this assertion. Thus the principal-unit coefficient action modulo m^4 factors through Gamma/Gamma^(p^3), corresponding to cyclotomic level p^4. This does not prove that constructing all geometric classes, projecting to the seed, or computing localization at that level is cheap.

## Formula for the ten coordinates

One may extract f_ab from the preceding finite arithmetic output at precision p^(4-a-b). Alternatively, compute the ten actual cohomological values e_ij of TEN_POINT_CERTIFICATE.md. With its explicit unit matrix V,

    (p^(a+b) f_ab)_(a+b≤3)=V^(-1)(e_ij)_(i+j≤3) mod p^4.

This is a formula for the coordinates from a finite arithmetic source with no nonunit division. It is not their evaluation: the values e_ij themselves have not been computed here.

## Remaining arithmetic calculation

The unresolved task is to determine enough of this genuine finite source to prove [F_p] in m^2/m^4 is nonzero cofinitely, or derive an independent estimate guaranteeing it. The construction has removed the need to make the old complex-period comparison a prerequisite, and the ten-point theorem removes mandatory detection at T=S=p. Neither step proves the required arithmetic nonvanishing.

No individual-p production run, field computation, or automatic follow-up is specified by this document.
