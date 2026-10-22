# Functional-equation reduction of the genuine Kato jet

Date: 2026-10-04
Status: WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS_AND_IMPORTED_THEOREMS.
Independent review is pending. No uniform nonvanishing or new primary result is claimed.

## 0. Inputs and scope

Fix an ordinary good prime p >= 17 outside the fixed exceptional set of the submitted cofinite Hida-control argument and outside {19,59,487}. Retain, without re-certifying, that argument's full localized algebra I=Z_p[[T]], its primitive integral signed symbol modules and ordinary representation V(T), and the source/quotient/Euler-system hypotheses in the return at a87b1af093f56efb5bce384b36d2463db2aa2dde. In particular retain its integral source matching, not merely an abstract existence claim.

Write R=Z_p[[T,S]], m=(p,T,S), J=(T,S), and let nu_T,nu_S be principal-unit characters with values 1+T,1+S at 1+p. The representation is U=V(T)nu_S^{-1}. Fix the source-compatible Coleman coordinate of the optimized integral Kato family Z(r), and let

    F(T,S)=Col(pr_- loc_p Z(1)).

Ochiai's Theorem 4.12, equation (4.12), identifies this coordinate with its family L-function. Its cyclotomic argument in the source is chi_cyc nu_S: source coordinate X=p+(1+p)S. In the conventional Mellin variable j-1 the character is nu_S. This shift is essential.

Retain the submitted global low-jet result F in J^2. Its integral Selmer-complex and deformation Euler-system proof has not been re-certified here. If that input fails, the four-value reduction below does not follow; the submitted ten-point criterion remains the separate fallback.

The tame conductor is the exact seed N=6503188012738584. The constant critical character has trivial tame part and specializes to the trivial character at the weight-two seed. The seed's root number is +1 and its ordinary stabilization is not exceptional (a_p is not 1 mod p). The assumptions p not dividing 6N phi(N) needed for Howard's family statement can be absorbed in the existing fixed finite exception set. The full non-squarefree N is retained.

## 1. An arithmetic involution, not a formal symmetry imposed on F

Define an integral involution of R by

    iota(T)=T,
    1+iota(S)=(1+T)/(1+S).

It preserves J and m. It is also the expected duality on the coefficient representation: det V(T)=chi_cyc nu_T, so U^*(1) is V(T)nu_T^{-1}nu_S, obtained by this substitution.

Representation duality by itself does not prove a functional equation for an arbitrary Euler-system coordinate. The arithmetic input used here is Howard, Central derivatives of L-functions in Hida families, section 4 (author PDF pp.10-11), the displayed functional equation immediately before (9) and Lemma 6. In Howard's Mellin convention it relates chi to [.] chi^{-1}, with multiplier -w_H chi^{-1}(-N) theta(-N). On this component [.] is nu_T and theta is its principal square root. Lemma 6 identifies -w_H with the root number at the nonexceptional weight-two seed, hence with +1. No finiteness of Sha or nonzero central L-value is used to identify that sign.

Set

    ell_N = log_p(<N>)/log_p(1+p) in Z_p,
    U_N(T,S)=(1+T)^(ell_N/2)(1+S)^(-ell_N),

where <N>=N/omega(N). Then, in the source-compatible analytic coordinate,

    F(T,S)=U_N(T,S) F(T,iota(S)).                    (FE)

Both multiplier and inverse are integral units. In particular iota(U_N)=U_N^{-1} and U_N(0,0)=1.

### Check of the source shift and normalization by a dense interpolation set

Here is a way to check (FE) without identifying ramified Gauss factors by a name. Choose w a nonnegative multiple of 2(p-1), s a nonnegative multiple of p-1, and 1 <= j=s+1 <= k-1, where k=w+2. These are a p-adically dense set of pairs after allowing w to grow. At these points g_w has trivial p-nebentypus and is the ordinary p-stabilization of a newform h_w of tame level N. The dual index is j'=k-j=w+1-s. Both j and j' are odd and j'-j is divisible by four.

Ochiai's interpolation (4.3), with phi=1 and the factor in Theorem B, is a weight-dependent period constant times

    (-1)^j Gamma(j)/(2 pi i)^j
      * (1-p^(j-1)/alpha_w) L(g_w,j).

Use the actual p-stabilization identity

    L(g_w,j)=(1-p^(k-1-j)/alpha_w)L(h_w,j).

The product of the two displayed Euler factors is invariant under j -> k-j. The period sign is the same at both indices; the weight-dependent period scalar cancels. The completed complex functional equation of h_w, with family sign +1 as above, gives the remaining ratio N^(w/2-s). The powers of i cancel because j'-j is divisible by four. Since w/2 and s are multiples of p-1, this ratio equals <N>^(w/2-s), exactly U_N(t_w,t_s), where t_n=(1+p)^n-1.

This argument is an equality, including when an L-value vanishes; it does not divide by that value. For each p-adic residue rectangle in w,s, arbitrarily large critical integer pairs with these divisibility conditions exist. Thus the equality holds on a topologically dense subset of pZ_p x pZ_p. The convergent integral power series agree everywhere on that polydisc and hence as formal power series (apply the one-variable identity principle twice). This transports the functional equation to the source's chi_cyc nu_S convention. It is not an assumed symmetry of the unknown seven coefficients.

This is the specific source-alignment step to examine in an independent review. If a different local generator has changed F by v in R^times, its functional equation multiplier becomes (v/iota(v))U_N. Work in the fixed source-compatible coordinate for the explicit formulas below, or transport that known unit. Ideal membership in m^4 is unchanged by such a change.

## 2. A unit normalization preserving the actual arithmetic class

Put

    zeta=(1+S)/(1+T)^(1/2),
    rho=zeta^(ell_N/2),
    H=rho F.

All binomial powers are in R; p is odd. We have iota(zeta)=zeta^{-1}, U_N=zeta^{-ell_N}, and therefore

    iota(H)=H.                                       (2.1)

Multiplication of the entire genuine family Z(r) by rho is an integral unit change of an Euler system, since the norm relations are R-linear. Thus H is still the Coleman image of actual arithmetic classes. It is not a fabricated invariant polynomial. Its specialized indices and its membership in m^4 are the same as those of F.

Introduce the integral coordinate

    Y=(zeta-zeta^{-1})/2.

It satisfies iota(Y)=-Y and Y=S-T/2+terms of degree >=2. The inverse is zeta=Y+sqrt(1+Y^2), followed by 1+S=zeta sqrt(1+T). Consequently R=Z_p[[T,Y]], J=(T,Y), and the maximal-ideal filtration is unchanged.

Since 2 is a unit, (2.1) gives

    H in Z_p[[T,Y^2]].

Combining this with the retained H in J^2 proves

    H = A T^2 + B Y^2 + C T^3 + D T Y^2  (mod m^4).   (2.2)

A and B are needed modulo p^2; C and D modulo p. There are four arithmetic coefficients, carrying six F_p-digits, rather than seven coefficients carrying ten digits. These coefficients have NOT been computed here.

### Explicit check against the original seven coefficients

For F=aT^2+bTS+cS^2+dT^3+eT^2S+fTS^2+gS^3+O(J^4), the arithmetic functional equation forces

    b=-c,
    g=-(1+ell_N/2)c,
    e+f=(1+ell_N/2)c-(ell_N/2)a.                       (2.3)

These are equalities of the actual Taylor coefficients in Z_p, in the fixed source coordinate. Direct expansion also gives

    A=a-c/4,
    B=c,
    C=d+e/4+c/8-(ell_N/8)a+(ell_N/16)c,
    D=-e+c/2-(ell_N/2)a-(ell_N/4)c.                   (2.4)

The exact symbolic identities are included in the checks. Equation (2.3) is an additional constraint from the global functional equation. It does not force any coefficient to be nonzero.

## 3. Four lower-weight critical points detect the remaining class

Use the four ordered nodes

    (w,s)=(3,2), (3,3), (4,3), (4,4).                 (3.1)

Their data are:

| (w,s) | weight k=w+2 | r=w+1-s | h=g_w tensor omega^(w-s) |
|---|---:|---:|---|
| (3,2) | 5 | 2 | g_3 tensor omega |
| (3,3) | 5 | 1 | g_3 |
| (4,3) | 6 | 2 | g_4 tensor omega |
| (4,4) | 6 | 1 | g_4 |

Each satisfies 1 <= r < k/2. Only two genuine Hida forms, of weights 5 and 6, are involved. This is a change from the four weights 12 through 15 in the input; it is not a claim about comparative running time at the seed's large level.

At a node define

    x_w=t_w/p,
    y_ws=Y(t_w,t_s)/p.

Both are integral, x_w=w mod p and y_ws=s-w/2 mod p. Let V_p have these four rows, with columns

    x_w^2, y_ws^2, x_w^3, x_w y_ws^2.

Then modulo p its matrix is

    [ 9, 1/4, 27,  3/4 ]
    [ 9, 9/4, 27, 27/4 ]
    [16,   1, 64,    4 ]
    [16,   4, 64,   16 ],

whose determinant is 864=2^5*3^3. Thus V_p is invertible over Z_p on our domain. This determinant follows also by subtracting the two rows within each weight: the squared-Y differences are 2 and 3, and the remaining two-by-two weight determinant contributes the remaining nonzero factors. The displayed exact matrix and its rational inverse are checked independently by fraction-free elimination.

For E_ws=H(t_w,t_s) mod p^4, (2.2) now gives

    (E_ws)=V_p (p^2 A, p^2 B, p^3 C, p^3 D)^t mod p^4. (3.2)

Inverting V_p involves no p-division. Hence

    F not in m^4
      <=> H not in m^4
      <=> at least one of the four E_ws is nonzero mod p^4
      <=> at least one F(t_w,t_s) is nonzero mod p^4.    (3.3)

For explicit reconstruction, compute the TRUE x_w and y_ws to the required precision. Replacing them by w and s-w/2 is sufficient only for the determinant test, not for p^4 coefficient extraction.

The normalizing units at the four nodes are especially concrete. Let r_N be the unique fourth root of <N> in 1+pZ_p. In the order (3.1),

    (rho(t_w,t_s))=(r_N, r_N^3, r_N^2, r_N^4).         (3.4)

No unknown modular period appears in these four units.

## 4. Each new node still bounds the original seed

This is not inferred from interpolation alone. The arithmetic proof must be extended to the new nodes.

At a node in (3.1) specialize the genuine integral family and use

    U_ws=V(g_w)chi^(-s)omega^s=D(h)(r).

Its ordinary graded characters are

    A_ws=Z_p(alpha_w^(-1) chi^r omega^(s-w)),
    M_ws=Z_p(alpha_w chi^(-s)omega^s).

Their residual characters are exactly the seed's alpha-bar^(-1)chi-bar and alpha-bar. The former has positive r, the latter nonpositive -s; alpha-bar !=1. The same H^0/H^2 vanishing and saturated ordinary finite-line argument used in the input therefore applies at all four nodes. Discrete p-torsion gives the seed's Kummer local condition. The retained bad-prime residual zeros and unramified conditions away from p give the global comparison

    B_ws[p] = Sel_p(E/Q),
    0 -> W_p -> B_ws[p] -> Sha(E/Q)[p] -> 0,
    dim W_p=2.

Kato's noncentral critical results apply because all four r lie strictly below k/2. The unit transvection at 2243 persists: the finite p-power-conductor twists are unramified there and residual ramification excludes conductor zero. Apply the integral Euler-system inequality to this actual specialized family class. Its component is nonzero whenever its tested local value is nonzero. Other components can be filled without changing it, as in the retained argument.

For clarity, the specialization bookkeeping remains a=a0+t and h-t<=a0, so h<=a; the Tor term is not dropped. Poitou--Tate and equality of the orders of the two noncentral dual Selmer groups then give

    length B_ws = b_ws-a+h <= b_ws,
    dim_Fp Sha(E/Q)[p] <= b_ws-2,
    b_ws=v_p F(t_w,t_s)                              (4.1)

when finite. The Coleman equality is in the proved integral local quotient. It is not a comparison to the old eta_p M_p. Multiplying the family by rho gives the same b_ws.

Equations (3.3), (4.1), and retained even parity prove the four-value criterion:

    some F(t_w,t_s) not in p^4 Z_p
         ==> Sha(E/Q)[p^infinity]=0.                 (4.2)

Thus the new four-value test detects exactly the same fourth-order family-jet nonvanishing as the submitted ten-point test, under the additional source-matched functional equation proved above. It does not replace that nonvanishing with an assumption.

## 5. Two weight fibres and independent local unit choices

The four nodes use only T=t_3 and T=t_4. Exact compatible restrictions to these two weight fibres determine the class modulo m^4 for F in J^2. To prove this, if two such series differ by K, vanishing on both fibres implies

    K=(T-t_3)(T-t_4)L.

The distinct linear factors are prime elements, so their ideal intersection is their product; comaximality is neither true nor needed. The product has nonzero constant t_3t_4. Comparing K's constant and two linear coefficients shows L in J^2. Since the product belongs to m^2, K belongs to m^4. This uses exact compatible fibre data from the genuine source, not arbitrary interpolation modulo a p-power.

For NONVANISHING alone, even the relative units between the four local cohomology generators need not be computed. Replacing any tested value by a unit multiple preserves whether it vanishes modulo p^4. For reconstruction of A,B,C,D by (3.2), use a common source coordinate, or transport those units. An unknown p-power multiplier is never allowed.

The four-weight gluing theorem is therefore not a mandatory implementation of this finite target. The two lower weight fibres suffice. No reduction in the required cyclotomic coefficient quotient is asserted here; retain the input's level-p^4 precision if using that model.

## 6. Minimality is only a statement about this finite test

The subspace of invariant jets killed by p in this test contains the four independent classes pT^2, pY^2, T^3, TY^2 in m^3/m^4. Each scalar evaluation into p^3 Z_p/p^4 Z_p supplies at most one F_p coordinate. Fewer than four scalar evaluations cannot detect every such formal class. Our four-node system is therefore minimal among universal scalar-evaluation tests for this invariant finite-jet space. This is NOT a lower bound for every arithmetic proof, and it does not assert that every formal class is realized by the seed.

## 7. Precisely what remains

No coefficient A,B,C,D and none of the four actual Kato values has been evaluated in this turn. The symmetry allows all four to vanish; it is not an upper bound on their p-divisibility. The statement needed for the ordinary tail is still an independent arithmetic proof that at least one of these four genuine residues is nonzero for all but finitely many ordinary p.

The change achieved here is an arithmetic functional-equation constraint and a proved reduction of the finite source/evaluation problem: seven coefficients to four, ten critical values to four, and four forms of weights 12--15 to two forms of weights 5 and 6. This is not a claim of a new vanishing prime, cofinite FIN, ORDER9, Q36, or a guaranteed route to full BSD. Supersingular primes and the excluded primes remain separate.
