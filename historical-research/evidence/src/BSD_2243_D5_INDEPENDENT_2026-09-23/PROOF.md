# Independent D5 certificate at p = 2243

## Statement

On the retained minimal model

    E: y^2 = x^3 - x^2 - 66020924 x - 65074271436
    P1 = (-3031,327384), P2 = (-2394,281520),

let h be the corrected split-multiplicative height of Stein--Wuthrich section 4.2, and let H be its symmetric bilinear matrix, with polarization

    <P,Q> = (h(P+Q)-h(P)-h(Q))/2.

The independent finite calculation proves

    H = 2243 * [[2127,1294],[1294,764]] + O(2243^2) entrywise,
    det H = 2181 * 2243^2 + O(2243^3).

In particular det H is nonzero and its valuation is exactly 2. For kappa(gamma)=1+2243, H_gamma=H/log_p(1+p) has the displayed matrix modulo p and Reg_gamma=2181 modulo p, a unit.

The coordinate change from the original seed is x_old=x+7578, y_old=y, with scaling u=1. It preserves the invariant differential. The retained rank and basis statements identify the computed matrix with the regulator on the full free Mordell--Weil group. Nonvanishing on these two directions already proves nondegeneracy when the rank is two.

## 1. Precise imported height formula

The local pinned Stein--Wuthrich text defines the Bernardi sigma at section 4, the corrected split height at section 4.2 (Werner's correction to the earlier MTT formula), and gamma normalization at section 4.4. For a multiple Q=mP in the formal group at p and with nonsingular reduction at every other finite place, it gives

    h(P) = m^-2 [2 log_p(e(Q)/sigma_p(t(Q)))
                 - log_p(u(Q))^2/log_p(q_E)].                 (1)

Here t=-x/y; e(Q)>0 is the square root of the denominator of x(Q) in lowest terms; u(Q) is the preimage in 1+p Z_p under Tate uniformization; log_p(p)=0. The canonical sigma equals the Bernardi sigma times exp(e2 log_E^2/24), with e2 integral at this multiplicative p. We use precisely (1), not a conjectural BSD formula.

The logarithm of e(Q) is global denominator information. It includes its prime-to-p part. Replacing e(Q) by p^v_p(e(Q)) would NOT compute (1).

This run imports this published definition and the identification with the arithmetic height retained in D6. It does not independently reprove the entire Schneider/Werner/Jones comparison. It uses no finiteness of Sha in the numerical height calculation.

## 2. Rigorous truncation to the first normalized digit

Because a1=a3=0, x(t)=t^-2 V(t) with V in 1+t^2 Z_p[[t]], even. Substitution in the Weierstrass equation constructs V with integral coefficients. The invariant differential has the form

    omega = w(t) dt,
    w = 1 - t V'(t)/(2 V(t)) in 1+t^2 Z_p[[t]],

also even. The Bernardi definition is

    (d/dt)((log sigma)'/w) = -x w.

Integrate the Laurent series twice, using oddness of sigma to fix the intervening constant. After removing log t, write

    log(sigma(t)/t) = sum_{j>=2} b_j t^j.

Both integrations divide only by positive indices at most j; all other coefficients are integral. Consequently

    v_p(b_j) >= -2 floor(log_p j).

There is no degree-one term because a1=0 (equivalently by parity). If v_p(t)>=1, every omitted summand satisfies

    v_p(b_j t^j) >= j - 2 floor(log_p j) >= 2   (p=2243,j>=2),

and the lower bound tends to infinity. Thus the entire infinite logarithmic sigma tail lies in p^2 Z_p, not just a tested finite prefix. Similarly the formal logarithm, obtained by integrating w, satisfies log_E(Q)=t(Q) modulo p^2. The exponential modification contributes e2 log_E(Q)^2/24 in p^2 Z_p because p>3 and e2 is integral. Hence

    log_p(sigma_p(t)/t) = 0 modulo p^2.                       (2)

Let Tate uniformization pull back omega_E to C du/u. Since the model has multiplicative reduction, the isomorphism to its Tate curve has unit scaling. The Tate invariants satisfy c4(Tate)=1 and c6(Tate)=-1 modulo p. Their scaling rules give

    C^-2 = -c6(E)/c4(E) modulo p =: k.

The formal logarithm satisfies log_E(Q)=C log_p(u(Q)). Write ell=log_p(q_E)/p modulo p. When ell is a unit, (1)--(2) therefore reduce to the exact congruence

    h(P)/p = m^-2 [2 (log_p(e(Q)/t(Q))/p)
                   - k (t(Q)/p)^2 / ell] modulo p.           (3)

Precision accounting: an error in log_E of p^2 changes its square by p^3; division by log_p(q_E), of valuation one, leaves an error in p^2. Knowing k and ell modulo p is sufficient for the same reason. Knowing the unit e(Q)/t(Q) modulo p^2 determines its logarithm modulo p^2. No real approximation is involved.

## 3. Tate parameter and all logarithms

The invariant calculations, performed with integers, are

    c4 = 3169004368,
    c6 = 56243184546880,
    Delta = 16586638656786071143743744,
    v_p(Delta)=1, p does not divide c4*c6.

Let z=Delta/c4^3 modulo p^3. The Tate j-expansion is j=q^-1+744+O(q), so its inverse is q=z+744 z^2 modulo p^3. The ignored terms are in p^3 since v_p(z)=1. This gives

    q_E = 4521378839 modulo p^3,
    q_E/p = 2015773 modulo p^2.

For any p-adic unit a, the logarithm branch used in (1) satisfies

    log_p(a)/p = ((a^(p-1)-1)/p)/(p-1) modulo p.              (4)

Indeed log_p(a)=(p-1)^-1 log_p(a^(p-1)); after the first term the logarithm series of 1+p b is in p^2 Z_p, including all indices divisible by p. Here the Fermat quotient of q_E/p is 444, and (4) gives

    ell = 1799 modulo p,       k = 610 modulo p.

Thus v_p(log_p(q_E))=1 is certified independently of the retained PARI value. The q truncation loses one digit when dividing by p and still supplies the two unit digits needed by (4).

## 4. Global denominators without enormous rational points

Set R=2P, n=p-1=2242, and Q=nR=mP with m=4484. Exact rational addition produces R. The finite reduction checks in VERIFICATION.json show that R is nonsingular at every bad prime; when its denominator is divisible by a prime, its reduction is the smooth point at infinity. Smoothness is automatic at every good prime. Multiplication preserves the identity subgroup, so Q satisfies the global reduction hypothesis of (1).

Write x(R)=a/d^2 and y(R)=b/d^3 in lowest terms. Using the standard division polynomials psi_n and

    phi_n = x psi_n^2 - psi_(n-1) psi_(n+1),

we have x(nR)=phi_n(R)/psi_n(R)^2 and y(nR)=psi_(2n)(R)/(2 psi_n(R)^4), since a1=a3=0.

For this calculation there is no hidden cancellation in the global denominator:

    e(nR) = +/- d^(n^2) psi_n(R).                           (5)

Here is the local check establishing (5), including the bad primes. The integer

    A_n = d^(2n^2) phi_n(R)

is integral; phi_n is monic of degree n^2 in x. The prospective denominator d^(n^2) psi_n(R) is integral by the weighted homogeneity of psi_n. At primes dividing d, A_n is a unit by its monic leading term. At good primes not dividing d, multiplication on the smooth elliptic fiber has no common zero of phi_n and psi_n: the division-polynomial multiplication formula has no base point there. At every bad prime not dividing d, the separate division-free recurrence in verify_d5.py explicitly checks that phi_n(R) and psi_n(R) are not both zero modulo that prime, for the actual n=2242 and each of the three R. The outputs are in VERIFICATION.json. These checks exclude every possible common prime divisor, and prove (5) for the actual global rational denominator. They do not require factoring a huge denominator.

The resulting small modular formulas are

    t(Q) = -2 phi_n(R) psi_n(R)^2 / psi_(2n)(R),
    U := e(Q)/t(Q)
       = +/- d^(n^2) psi_(2n)(R)/(2 psi_n(R) phi_n(R)).       (6)

The sign in (5)--(6) is irrelevant because log_p(-1)=0. Thus (6) retains the entire denominator, rather than dropping away-from-p contributions.

For completeness the primary recurrence is

    psi_(2j+1) = psi_(j+2) psi_j^3 - psi_(j-1) psi_(j+1)^3,
    psi_(2j)   = psi_j/(2y) * (psi_(j+2) psi_(j-1)^2
                                      - psi_(j-2) psi_(j+1)^2).

All inversions by 2y in the main p-adic implementation are of units, checked during execution. The verifier uses a different, division-free recurrence for psi_odd and psi_even/(2y), which also works at the bad residue characteristics. Standard initial psi_1 through psi_4 are explicit in both files.

For all three points, the certified valuations are

    v_p(psi_n)=v_p(psi_(2n))=1,  v_p(phi_n)=0.

With calculations modulo p^5, removing p from these two quantities leaves p^4 precision. Every remaining denominator in (6) is a unit. Both U modulo p^2 and t modulo p^2 are therefore certified. The resulting nonzero t/p values also verify directly that Q belongs to the formal group with parameter valuation one.

## 5. Exact arithmetic results

All entries in the following table are residues modulo p, except U and t, which are modulo p^2. L denotes log_p(U)/p and B denotes k(t/p)^2/ell.

| P | U mod p^2 | t mod p^2 | t/p mod p | L | B | h(P)/p=(2L-B)/m^2 mod p |
|---|---:|---:|---:|---:|---:|---:|
| P1 | 206355 | 2063560 | 920 | 2151 | 280 | 2127 |
| P2 | 2402252 | 2599637 | 1159 | 1172 | 1531 | 764 |
| P1+P2 | 2675898 | 4663197 | 2079 | 1050 | 371 | 993 |

Since m^2=4 modulo p, polarization gives the off-diagonal residue

    (993 - 2127 - 764)/2 = 1294 modulo p.

Finally

    2127*764 - 1294^2 = -49408 = 2181 modulo 2243,

which proves the stated nonvanishing. Because log_p(1+p)/p=1 modulo p, the normalized regulator has the same residue 2181.

## 6. Verification and independence

- The calculation uses Python standard-library integers and fractions only. It calls neither PARI nor Sage and consumes no numerical coefficient corpus.
- A division-free polynomial recurrence independently agrees on the required indices at p^7 precision.
- Independent Jacobian-coordinate multiplication checks t(nR) modulo p^4, checking the curve equation and primitive coordinates at every step. No division-polynomial recurrence is used by that coordinate calculation.
- Exact rational coordinates for 18 small multiples independently confirm the full global denominator identity.
- All 15 actual bad-prime cases are checked for denominator cancellation or handled by the monic formal-group argument.
- Four- and seven-digit computations give the same matrix residue.
- Independently evaluated heights of P1-P2, 2P1 and P1+2P2 satisfy the parallelogram identity, quadratic scaling, and unimodular change-of-basis determinant equality modulo p.

Only after the independent derivation and first run was the resulting determinant compared with the retained PARI report: it agrees, with no fitted factor. The verifier shares the arithmetic input model and the imported height formula; this is not a second independent proof of those published formulas or a Lean verification.

## 7. Exact endpoint effect and boundaries

D5 is supplied: the corrected split height on the retained rank-two Mordell--Weil space is nondegenerate, and its gamma-normalized regulator is a unit.

Under the retained D1--D7 theorem, period, rank/image and symbol-lattice inputs, a future independently certified unit C_(2243,3) would give order three of the split analytic series. D2 removes its exceptional T factor, and D4 gives finite primary Sha before Jones's conditional leading-term theorem is used. The present nondegeneracy certificate supplies that theorem's D5 hypothesis; its leading-term valuation then yields Sha(E/Q)[2243^infinity]=0.

No cubic coefficient was evaluated here. No 2243-primary vanishing, global finiteness, order nine, or real leading-term identity is asserted by this height computation alone. No converse to Jones is needed for this D5 certificate. The published main-conjecture/period inputs retain their existing grades.
