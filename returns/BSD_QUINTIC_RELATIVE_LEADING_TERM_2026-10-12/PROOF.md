# An exact relative leading term over the first cyclotomic quintic layer

2026-10-12. Baseline: `Bome2017/bsd-seed-lab@84a7333af028ff5bc694bc82bcb3c768a019f5c6`.

**DERIVED_UNDER_RETAINED_INPUTS; EXACT_ARITHMETIC_EXECUTED; INDEPENDENT_REVIEW_REQUIRED.**

No BSD conjecture, finiteness of the full Sha, or conjectural rationality of the base rank-two leading term is assumed in Sections 1-6. The result is a relative analytic identity, not the order of a Tate-Shafarevich group. The only BSD-conditional interpretation is labelled in Section 7. No novelty claim is made.

## 1. Objects and retained inputs

Let E be the seed with minimal coefficients

    [0,-1,0,-66020924,-65074271436].

Retain its rank-two saturated rational point basis, analytic rank two, rational torsion Z/2, and the recently reviewed equality E(Q_n)=E(Q) in the cyclotomic Z_5 tower. The stronger point-group equality, not just rank equality, will remove a possible regulator index.

Let F=Q_1 be the unique degree-five subfield of Q(mu_25). Thus

    Gal(F/Q) = (Z/25Z)^*/Delta,
    Delta = {1,7,18,24},

and 6 generates this quotient. F is totally real. For each a prime to 25, define j(a) in {0,1,2,3,4} by a=d*6^j(a) mod 25 with d in Delta. Let zeta be a primitive fifth root and choose the even primitive character chi(a)=zeta^j(a). All four nontrivial characters of Gal(F/Q) have conductor 25.

Use the *full real* Neron period

    Omega = integral over E(R) of |omega_E| = 2*omega_1.

The retained table is x_a=Re(lambda_f(a/25))/omega_1, for the normalized newform f. Its differential/period convention is bound by the predecessor's PERIOD_AUDIT.md. Define lambda_f using the positive additive Fourier series sum a_m*exp(2*pi*i*m*r)/m, interpreted by Abel limit. Reversing every modular-symbol path changes a global sign below but not the four-character product or any ideal/norm conclusion.

Use the field-relative Neron-Tate pairing: its restriction to E(Q) over a degree-d field is d times the Q pairing. This is not the absolute, field-independent height. Write R_K for its regulator on a full free point basis, C_K for the product of finite local Tamagawa numbers and differential corrections, and t_K=|E(K)_tors|.

For K=Q or F define an actual positive real number

    A_K = [ L^{(2)}(E/K,1)/2 ] * sqrt(|D_K|) * t_K^2
          / [ Omega^[K:Q] * R_K * C_K ].                 (1)

Analytic rank two over F will be proved below. Expression (1) is the BSD-normalized analytic leading term. It is defined without assuming it is rational, integral, or equal to #Sha. The number-field BSD conjecture would identify it with #Sha(E/K).

**Claim derived here:**

    A_F = 19^4 * A_Q = 130321 * A_Q.                    (2)

Since C_Q=16 and t_Q=2 in the retained seed data, A_Q=q_E/4, with q_E the project's L''/(2 Omega R_Q). Thus

    A_F = (130321/4)*q_E.                              (3)

## 2. Evaluate the four algebraic twisted numerators exactly

The 20 saved denominator-25 symbols, in inputs/SYMBOLS_m25.txt, give

    S_j = sum_{a: j(a)=j} x_a = (-76,0,-76,76,76).

This is recomputed from the individual rows, not assumed from a summary. The character map is checked both by coset enumeration and by

    j(a) = 4*((a^4 mod 25 - 1)/5) mod 5.

For an even character, the odd imaginary parts of lambda cancel between a and -a. Dividing the real table by two converts its normalization to Omega. Hence set

    B(zeta) = (1/2) * sum_j S_j*zeta^j
            = 38*(-1-zeta^2+zeta^3+zeta^4).             (4)

An exact identity in Z[zeta] is

    B(zeta) = -38*zeta^2*(1+zeta)*(zeta-1)^2.           (5)

For example, (5) follows by reduction modulo Phi_5(X)=1+X+X^2+X^3+X^4. It is checked for all four conjugates. Since zeta and 1+zeta are units of norm one and Norm(zeta-1)=5,

    Norm_{Q(zeta)/Q}(B(zeta)) = 38^4*25 = 52128400.    (6)

Two exact methods reproduce (6): multiplying all four conjugates in the cyclotomic ring, and taking the determinant of multiplication by B on its integral power basis.

In particular every B(zeta^k) is nonzero. Equation (5) also determines its principal ideal:

    (B(zeta)) = (38)*(zeta-1)^2.                       (7)

This is an ideal statement about an evaluated algebraic twisted numerator, not a statement about Sha support. The rational primes in (7) are 2, 5, and 19.

## 3. Pass from the numerators to the complex L-values

For the Dirichlet convention L(E,chi,s)=sum a_m*chi(m)/m^s, the finite Fourier identity for a primitive character gives

    sum_{a mod 25} chi(a)*lambda_f(a/25)
       = tau(chi)*L(E,chi^{-1},1).

It follows first at Abel-regularized integrals and then by the usual modular-symbol limit. Consequently, with the fixed path convention,

    B(zeta^k) = tau(chi^k)*L(E,chi^{-k},1)/Omega.       (8)

The opposite common path orientation puts a minus on the right of all four equations and changes none of the conclusions below. No Manin multiplier is inserted: the historical table is already for the normalized newform divided by the seed's minimal period, not a parametrization pullback.

All the characters are primitive and even, so

    tau(chi)*tau(chi^{-1})=25,
    tau(chi^2)*tau(chi^{-2})=25.

These two identities are also checked by forming the actual finite Gauss sums in Z[mu_25], not by a floating-point approximation. Combining them with (6) yields

    product_{k=1}^4 [ L(E,chi^k,1)/Omega ]
       = (38^4*25)/625 = 38^4/25 = 2085136/25.         (9)

Every twisted central value in (9) is nonzero. Artin factorization gives

    L(E/F,s)=L(E/Q,s)*product_{k=1}^4 L(E,chi^k,s).

The base analytic rank is retained as two and the other factors are holomorphic and nonzero at one. Thus the analytic rank over F is exactly two, and

    [L''(E/F,1)/2] / [L''(E/Q,1)/2]
       = Omega^4 * 38^4/25.                           (10)

The four twists in this section have character conductor 25. They are not quadratic twists E^D, not the cyclotomic derivative at another coefficient prime, and not auxiliary Ota theta elements.

## 4. Field, differential, and Tamagawa factors

### 4.1 Field discriminant

Conductor-discriminant for the abelian degree-five field gives

    D_F = product_{k=1}^4 conductor(chi^k) = 25^4,
    sqrt(D_F)=625.                                    (11)

There is a useful independent model check. For w=zeta_25 let

    eta=w+w^7+w^18+w^24.

Its five conjugates are distinct, and direct cyclotomic-ring arithmetic proves

    eta^5-10*eta^3+5*eta^2+10*eta+1=0.

The discriminant of this polynomial is 7^2*5^8, NOT 5^8. Thus Z[eta] has index 7 in O_F, using (11). The extra 7 is a power-basis artifact and must not be included in (1). The checker verifies the polynomial relation, the five distinct conjugates, and its discriminant by an exact multiplication-matrix determinant. The field discriminant itself uses the stated conductor-discriminant theorem; it is not inferred by mistaking the polynomial discriminant for it.

### 4.2 Minimal differential

F/Q is unramified away from 5; E has good reduction at 5. The existing minimal discriminant valuations at the bad primes 2,3,2243,4547,5843 are respectively 8,2,1,3,2, all less than 12. At an unramified extension they are unchanged. An integral equation with discriminant valuation below 12 cannot be further minimized, since a minimizing change lowers that valuation by a positive multiple of 12. At 5, good reduction remains good after base change and the differential remains minimal. Thus no finite differential factor is missing from C_F.

### 4.3 Splitting and component groups

Frobenius at q != 5 has order one or five according as j(q) is zero or nonzero. Exact residues give:

| q | Retained type and c_q | j(q) | Places in F | Residue degree | Product above q |
|---|---|---:|---:|---:|---:|
| 2 | I1*, 2 | 2 | 1 | 5 | 2 |
| 3 | nonsplit I2, 2 | 4 | 1 | 5 | 2 |
| 2243 | split I1, 1 | 0 | 5 | 1 | 1 |
| 4547 | III, 2 | 4 | 1 | 5 | 2 |
| 5843 | nonsplit I2, 2 | 0 | 5 | 1 | 32 |

For the multiplicative places this follows from the retained type and odd unramified residue degree. For III the geometric component group has order two. For I1* the geometric component group has order four; the Frobenius automorphism has order prime to five. Taking fifth powers therefore preserves its fixed subgroup. In particular the additive place at 2 has not been handled by an unsupported semistability assumption. Unramified base change preserves the geometric Kodaira configuration.

All other places have c=1. Therefore

    C_Q=16,  C_F=256,  C_F/C_Q=16.                    (12)

The local types and original c-values are retained inputs; the splitting and resulting product are newly assembled and checked here. No number-field Tate algorithm was executed.

## 5. Regulator and torsion: the new point equality matters

The reviewed predecessor proves E(F)=E(Q) using the stronger residual-image input. Hence t_F=t_Q=2, the full free point basis is unchanged, and there is no unidentified finite-index point lattice in F.

With the relative height convention fixed in Section 1,

    <P_i,P_j>_F=5*<P_i,P_j>_Q,
    R_F=25*R_Q.                                       (13)

Using the absolute field-independent height in (13) without changing (1) would introduce a spurious factor 25. Rank equality alone would allow an index-square correction; the retained *point-group* equality is what makes the index exactly one.

## 6. The exact relative identity

Combine (10), (11), (12), and (13) in definition (1). The period powers cancel, giving

    A_F/A_Q = (38^4/25) * 625 * (1/25) * (1/16)
            = 19^4 = 130321.                          (14)

No value of q_E was used. Both sides of (14) may a priori be irrational; (14) proves their ratio, not their separate rationality. The Gauss product 625 equals sqrt(D_F), so an equivalent all-rational calculation is Norm(B)/(25*16).

The checks deliberately retain four normalization mistakes as negative controls: using the primitive real period in a formula requiring the full one; mixing absolute and relative heights; using the polynomial discriminant; and dropping the Tamagawa ratio. Each changes (14).

## 7. Exact endpoint consequence and the unproved Sha interpretation

**DERIVED:** q_E=36 if and only if A_F=9*19^4=1172889. This is an exact reformulation under the retained inputs, not an independent way of establishing either value.

**CONJECTURE / CONDITIONAL ON BSD OVER BOTH FIELDS:**

    #Sha(E/F) = 19^4 * #Sha(E/Q).

In particular the seed target #Sha(E/Q)=9 would then predict #Sha(E/F)=1172889. Neither equality for actual groups is proved here. In particular (7) does not prove that the new 19-primary part exists, has exponent 19, or exhausts the relative Sha. No rank-zero main-conjecture equality for the nonreal character twists was checked or imported.

A possible further arithmetic task is to control the nontrivial character Selmer components independently, retaining their integral periods and local terms. The available ideal factorization identifies a concrete 19-primary target, but does not supply its classes or a two-sided size theorem. Maistret-Shukla's relevant ideal/Sha relation is explicitly conjectural; its computational descent examples have CM hypotheses which this seed does not satisfy.

For every coefficient prime ell != 5, restriction Sha(E/Q)[ell^infinity] -> Sha(E/F)[ell^infinity] is injective because corestriction composed with restriction is multiplication by 5. Thus the base-field unknown components survive extension. Merely changing the field or computing the relative factor cannot erase them. This is a scope statement for this argument, not an impossibility claim about other arithmetic uses of the tower.

**FIN, ORDER9, Q36, and base-field prime coverage remain unchanged.** What is added is an exact, seed-specific, regulator-and-local-factor-complete relative analytic leading term, obtained from actual saved symbols and the new point-group equality. No new modular-symbol value or p-adic coefficient digit was computed.
