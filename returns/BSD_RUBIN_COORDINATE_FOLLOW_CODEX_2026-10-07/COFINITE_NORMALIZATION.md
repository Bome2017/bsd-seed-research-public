# A fixed-source normalization, and its precise limit

**FIXED_SOURCE_COMPARISON_DERIVED_COFINITELY.** Written deduction, independent review required. This removes a possible unbounded family of normalization exceptions after the source choices are fixed. It supplies no arithmetic nonvanishing.

## 1. The image lattice can be fixed before p varies

Fix one modular parametrization X1(N) -> E and its rational Manin–Drinfeld projection, as in BKS (2.1.1) and (2.1.2). Let H_B be the image of integral relative Betti homology in H1(E(C),Q), and let T_B=H1(E(C),Z). These are two full lattices in one fixed rational vector space. The map is rational and its domain is finitely generated, so its image really is a lattice.

Choose bases. The comparison matrix and its inverse have rational entries. There is therefore a fixed nonzero integer J for which

    H_B tensor Z[1/J] = T_B tensor Z[1/J].

Compatible Betti/etale comparison for this *same* rational map gives equality of the corresponding p-adic image lattice and T_pE for p not dividing J. This is stronger than independently invoking residual homothety at every p: outside this fixed support, no nonunit homothety is required. A different integral lattice isomorphism can still differ by a unit, which has zero valuation.

This argument does not compute J, assert J=1, or show that 5 or 17 avoids it. It also does not apply to an arbitrary sequence of p-dependent projectors or independently renormalized Kato classes. It is an existence-of-finite-support lemma for the fixed rational geometric map just specified.

## 2. Fix the Betti input and smoothing as well

Choose one Manin symbol xi with nonzero plus image. Such a choice exists because Manin symbols generate H_B and its plus part has rank one. Its nonzero coordinate in a fixed plus basis is rational. After adjoining its numerator and denominator to J, it satisfies BKS's primitive plus-source condition (2.1.3) at every remaining p. Its period ratio Omega_xi/Omega_E is a fixed nonzero rational number, so its support can also be included in J.

There is a concrete retained source for a nonzero plus direction: xi=[[1,0],[5,1]] gives {0,1/5}. The old symbol receipt has [1/5]^+=144 in the omega_1 convention, and the retained central value is zero. Thus this relative symbol has nonzero plus period. Using the fixed modular parametrization transports it to a nonzero rational plus direction. This receipt does not compute the full image-lattice index J.

Choose once and for all

    c=1+6N, d=1+12N.

They are positive, congruent to 1 modulo N, and coprime to 6N and to each other. Exclude the finite prime support of cd(c-1)(d-1). Then these are legitimate unit smoothings for every remaining p. This does not divide the class: it selects an actual smoothed source to which the integral criterion applies.

The resulting finite set also includes the criterion's original exceptions. No Sha, regulator, unknown derivative content or ETNC scalar is used to define these normalization exceptions. This is **not** a prime-independent ancestor for delta_p: the derivative remains a cyclotomic, p-dependent construction.

## 3. Comparison with the ordinary modular-symbol measure

Let L_std,p be the usual ordinary MTT measure with the fixed Neron real period, same gamma, and interpolation

    L_std,p(1)=(1-rho^(-1))^2 L(E,1)/Omega_E,
    chi(L_std,p)=tau(chi) rho^(-n) L(E,chi^(-1),1)/Omega_E

for nontrivial principal cyclotomic characters of conductor p^n. These equations specify the measure being compared, rather than declaring every output named L_p identical to it.

For the minimal S={infinity,p,bad primes}, define the bad-prime Euler series

    E_N(U)=product over multiplicative q|N of
           (1-a_q/q [Frob_q]^(-1)).

Additive primes contribute 1. The Frobenius uses the same arithmetic character convention as the interpolation formula. Its augmentation is

    E_N(0)=c_N=(1+1/3)(1-1/2243)(1+1/5843)
                =17469664/13105849
                =2^5*19*59*487/(2243*5843).

Compare BKS's printed page 895 with these interpolation equations. For a nontrivial cyclotomic character the missing bad Euler factors give E_N directly. At the trivial character the p-Euler factor in L_S(E,1) is

    (1-rho^(-1))(1-sigma^(-1)),

so its product with BKS's (1-rho^(-1))/(1-sigma^(-1)) is exactly (1-rho^(-1))^2. Thus interpolation uniqueness gives

    L_S,p = (Omega_E/Omega_xi) E_N(U) L_std,p.           (N1)

This identity does not omit the coefficient-prime Euler factor: it cancels with the explicitly different trivial-character prefactor. This cancellation is distinct from the Rubin prefactor epsilon, whose ordinary valuation is -1.

The weak-order and local-finiteness arguments already give Col(z) in U^2. Since the smoothing and E_N have nonzero augmentation, L_std,p has order at least two in U. The quadratic coefficient consequently satisfies

    [U^2]Col(z_raw)=t_cd(0)(Omega_E/Omega_xi)c_N [U^2]L_std,p.

Transport to T_pE multiplies by the specified lattice scalar. On the cofinite fixed-source domain of Sections 1–2 all these factors are proved units. Therefore

    v_p([U^2]Col(z)) = v_p([U^2]L_std,p).               (N2)

This is a valuation comparison. It does not determine the unit for an exact coordinate-vector computation. Changing gamma to its inverse preserves the valuation of a quadratic leading coefficient, but exact signs/coordinates still require the common convention.

The same interpolation comparison can be formulated with BKS's allowable supersingular distributions. No claim of coefficient integrality or of availability of the existing ordinary evaluator at supersingular primes follows.

## 4. The resulting arithmetic target

On this cofinite ordinary domain, where the matched height matrix is nonsingular, write L_2=[U^2]L_std,p and c=min v_p(adj(H) l), r=v_p(det H). The already-proved implication becomes

    v_p(L_2)+c-r-1=0  ==>  Sha[p^infinity]=0.           (N3)

The valuation equality in (N2) repairs a cofinite normalization issue. It does **not** prove the equality in (N3). In particular the fixed integer J bounds only normalization exceptions, not primes of intrinsic Kato divisibility. Calling J a Sha annihilator would be false.

For the previously submitted, possibly differently chosen sources at individual primes, the uncomputed homothety restriction remains until their actual choices are bound. This note does not retroactively declare those sources numerically matched at 5 or 17. The saved data below are a calibration of the correlated expression, with that qualification explicit.
