# Extract the four Kato images from classical modular symbols

Grade: WRITTEN_DERIVATION_UNDER_RETAINED_SOURCE_AND_INTEGRAL_CONTROL. Independent review pending. This is an extraction formula, not a uniform upper bound and not a novelty claim.

## 1. Arithmetic input, rather than assigned jet coefficients

Keep the submitted ordinary domain: good p>=17 outside the fixed, not numerically enumerated Hida exceptional integer D and the retained local exceptions. Let g_w, w=3,4, be the actual specializations of the seed's Hida branch; their modular weights are 5 and 6 and their U_p eigenvalues are alpha_w in Z_p^times. They are not the seed weight-two newform.

Use precisely the signed modular-symbol specialization of the primitive family input Xi used to construct Ochiai's optimized Euler system. Write its polynomial convention as

    phi_w(D;X,Y) = sum_(h=0)^w c_h(D) X^(w-h)Y^h,
    I_g({b}-{a};X,Y) = integral_a^b g(z)(X-zY)^w dz.

The sign projection and period are those of this source line. Equivalently, use the cohomology basis b and periods in Ochiai Definition 4.1: the specialized family symbol is C_(g,p) b, and the corresponding complex symbol is Omega_(g,infinity) b. Consequently phi_w is the algebraic symbol obtained with the ratio C/Omega, not an arbitrary rescaling of a numerical eigenvector. The transported polynomial pairing is fixed by the displayed integral convention. Its binomial coefficients are units on this domain.

For a=1,...,p-1 put

    D_a={infinity}-{a/p},
    phi_w(D_a;X,Y)=sum c_(w,a,h) X^(w-h)Y^h.

Only c_(w,a,h) modulo p^(4-h), h=0,1,2,3, will be needed. At w=4 the fourth coefficient does not enter modulo p^4. This is 2(p-1) polynomial symbol values on two actual forms, not 2(p-1) scalar values of the seed's weight-two symbol.

## 2. An exact finite moment formula

Let omega(a) be the Teichmuller lift and s be 2 or 3 when w=3, and 3 or 4 when w=4. Define

    J_(w,s) = alpha_w^(-1) sum_(a=1)^(p-1) omega(a)^(-s)
                sum_(h=0)^s [binom(s,h)/binom(w,h)]
                    a^(s-h) p^h c_(w,a,h).                    (E1)

All divisions in this expression are by p-units. In the source's interpolation convention the four Coleman images are

    F_p(t_w,t_s) = (-1)^s J_(w,s).                           (E2)

For primary nonvanishing the displayed sign is irrelevant; it must be retained for reconstruction in the common frame. Reversing all paths changes the corresponding global sign consistently. Independently chosen primitive generators can multiply an entire weight fiber by a unit; that also preserves the test, but does not license coefficient reconstruction without transporting the units.

### Derivation of the polynomial factors

For the normalized analytic symbol before sign projection,

    integral_(a/p)^(i infinity) (a-pz)^s g(z) dz
      = sum_(h=0)^s [binom(s,h)/binom(w,h)]
                    a^(s-h) p^h I_g(D_a)_h.                 (E3)

Indeed I_g(D_a)_h=(-1)^h binom(w,h) integral z^h g(z) dz. The two signs cancel in (E3). The same equality holds after the specified linear sign projection. It is not the naive moment integral of z^s alone.

To check the measure convention directly, for n>=1 define

    J_n(a,s)=alpha_w^(-n) integral_(a/p^n)^(i infinity)
                                      (a-p^n z)^s g(z) dz.

Changing variables z=(u+j)/p in the sum over a+jp^n gives

    sum_(j=0)^(p-1) J_(n+1)(a+jp^n,s)=J_n(a,s),

using U_p g=alpha_w g in the q-expansion normalization U_p g=(1/p)sum g((z+j)/p). This verifies the sign, p-powers and alpha factor in one convention. Integrality of the polynomial symbols implies that J_n(a,s) differs from a^s J_n(a,0) by an element of p^n times a fixed integral lattice. Passing to the limit identifies these compatible moments with integration of x^s against the ordinary measure. Summing with omega(a)^(-s) computes the principal-unit moment.

### Match to the actual Kato source at the four points

Set j=s+1 and phi=omega^(-s). Here phi is nontrivial of conductor p: 0<s<p-1. In Ochiai (2.7), e_p(g,j,phi)=p^s/alpha_w. At the source point, chi_cyc^j phi=chi_cyc nu_s, exactly the previously retained shift X=p+(1+p)S and tame component omega.

The finite Gauss sum and Mellin integral applied to (E3) give

    J_(w,s) = - s! (p^s/alpha_w) tau(phi)
                    L(g_w,phi^(-1),s+1)/(2*pi*i)^(s+1)
                    * C_(g_w,p)/Omega_(g_w,infinity).       (E4)

One may obtain this first with a convergence parameter and then continue; the identity is a finite sum of convergent cusp integrals, not an interchange at a non-absolutely convergent Dirichlet-series endpoint. The signed component is the one selected by this critical functional. Ochiai (4.3) has factor (-1)^(s+1) s! with the same Euler, Gauss and period terms. Comparing yields (E2). Finally (4.12) identifies that very analytic source with the optimized Kato family's Coleman image. No claim about the old eta_p is needed.

The period ratio in (E4) is already represented in phi_w by its definition. There is no separate operation of converting a complex period to a p-adic unit. If only an arbitrarily normalized classical symbol is supplied, this derivation does not authorize using it.

## 3. Precision and executable formula

Modulo p^4 retain h<=min(s,3) in (E1). The h-th coefficient is needed modulo p^(4-h), while alpha_w and omega(a) are needed modulo p^4. All binomial denominators have prime factors at most 3 for w=3,4. Thus the calculation contains no integral division by p and no loss of precision.

`symbol_values.py` implements (E1)-(E2) and an input-shape checker. Its output explicitly does NOT authenticate the symbols' arithmetic provenance, their Hida-branch membership, their Hecke equations, or the exceptional-prime hypotheses. Those require separately bound arithmetic evidence. It never emits a certified Sha result from unauthenticated arrays.

The submitted `four_value.py` can reconstruct A,B,C,D from these four results only if the arrays use the same family frame. For a nonzero witness alone, separately primitive frames suffice.

For the BSD nonvanishing test, alpha_w need not even be evaluated: remove the unit alpha_w^(-1) and test the remaining sum. `symbol_values.py` therefore permits omission of alpha_w and still returns the unit-scaled certificate residues. In that mode it does not pretend to recover F itself or its common coefficients. Ordinarity of the actual form remains a required arithmetic hypothesis.

This eliminates the need to calculate an etale localization or build the level-p^4 cyclotomic source as a mandatory implementation. It does not prove that constructing the two seed eigensymbols at the enormous tame level is affordable. No seed-scale run or cost estimate is claimed.

## 4. Exact calibration on a genuine modular form

`checks/delta_moment_calibration.py` independently constructs the even modular symbol of Delta (level 1, weight 12) from the Manin relations and T_2=-24. The primitive polynomial is

    36(X^10-Y^10)-691 X^8Y^2+2073 X^6Y^4
        -2073 X^4Y^6+691 X^2Y^8.

At p=11 its ordinary stabilization has alpha=7536 modulo 11^4. For s=2,3,4 the one-layer formula gives 2673,13761,7546 modulo 14641. An independent Riemann sum over all 13,310 units modulo 11^4 gives exactly those residues. The stabilization correction is retained in the derivation: its h-th symbol coefficient has p^(10-h), so it disappears at this precision for h<=4. The integral primitive symbol is not inferred from numerical periods.

This calibrates the moment algorithm on actual modular symbols. It does not calibrate the seed's weight-five/six forms, its global inputs, or its Kato normalization. The use of p=11 here is outside the seed theorem domain and is only an algorithm check.

## 5. Endpoint and the remaining arithmetic estimate

On the retained domain, a proved nonzero value of one of the four sums modulo p^4 gives the existing index bound b<=3 and hence seed Sha[p^infinity]=0. A proof that this happens outside one fixed finite set of ordinary p would close the ordinary uniform component. Supersingular primes, exceptional primary finiteness, ORDER9 and Q36 are separate.

No sum for the seed has been evaluated here. No independent uniform upper bound on its valuation has been proved. Source primitivity, U_p invertibility and the functional equation were tested as possible ways of obtaining that bound; none supplies control of these particular weighted sums by itself. The result of this pass is a source-matched arithmetic extraction formula with an exact non-seed calibration, not a nonvanishing theorem.
