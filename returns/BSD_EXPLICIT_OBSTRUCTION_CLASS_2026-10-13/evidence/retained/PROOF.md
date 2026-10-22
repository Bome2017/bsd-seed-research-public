# Independent arithmetic lower bound for the positive control

Grade: written deduction plus exact computations. No BSD or Sha-finiteness assumption. Not independently reviewed or formally verified.

## 1. Curves and point lattices

Let d=43737=3*61*239 and set

    A=[0,0,1,-19766893413,-1937478573143510],
    F=[0,0,1,-14959712463303,-22270654620235278500].

These are respectively the d-twists of [0,-1,1,-10,-20] and [0,-1,1,-7820,-263580]. PARI's two-descent returns rank(A)=2 with points

    P1=(1778638/9,1169009812/27),
    P2=(6466626346478/36517849,2366996613841078836/220677361507).

The rational 5-isogeny phi:A->F gives equal ranks. On F take

    Q1=(6288329,-11502941299),
    Q2=(8502485,21568458354).

The reduction certificate in outputs/EXACT_CONTROL.json independently proves that both pairs are linearly independent modulo 5 in their full rational point groups. It uses the homomorphisms obtained by reduction at q=7 and 19 followed by multiplication by #E(F_q)/5, then discrete logarithms in the resulting order-five group. The group cardinalities are 10 and 20. In the bases of those cyclic groups chosen by the checker the rows are:

    A: (2,2), (3,1), determinant 1 mod5;
    F: (2,3), (2,0), determinant 4 mod5.

If a nontrivial mod-5 combination were a rational 5-multiple, both evaluations would vanish, contradicting these determinants. Since rank is two and rational 5-torsion is zero, each point pair spans the full Mordell–Weil lattice after tensoring with Z_5. This is all the saturation needed below. No full prime-to-5 saturation claim is made.

## 2. Exact isogeny and point index

In short coordinates y'=y+1/2, define

    h(x)=x^2-889319*x+139856084578,
    f(x)=x^5-1778638*x^4+4058589566895*x^3
         -2382059022317513158*x^2+555932503837435168004716*x
         -43668321039996772149044128719,
    g(x)=h(x)f'(x)-2f(x)h'(x).

The map is (x,y') -> (f/h^2,y'g/h^3). The standard-library checker verifies the polynomial identity placing the image on F, and verifies exactly

    phi(P1)=-Q1-Q2,
    phi(P2)= 3Q1-2Q2.

Thus its point matrix is [[-1,3],[-1,-2]], with determinant 5. The 5-primary index of phi A(Q) in F(Q) is exactly 5; it is the entire index because this quotient is killed by 5 and both curves have trivial rational torsion. Consequently

    dim_F5 F(Q)/phi A(Q)=1.

For the dual phi_hat:F->A, the identity phi_hat phi=[5], rank two and trivial rational 5-torsion give

    dim_F5 A(Q)/phi_hat F(Q)=1.

The map sends infinity to infinity and has degree five. Its kernel polynomial factors as (x-204106)(x-685213). The corresponding four nonzero points are real: the completed-square right-hand sides divided by d are positive rational squares. Together with infinity, these are all five kernel points. The identity defining g proves phi^*omega_F=omega_A in the minimal differentials. Both curves have negative discriminant and connected real locus. Hence

    Omega_F/Omega_A=1/5

exactly, by the degree-five covering of the real torus. The numerical period check is supplementary, not the proof of this rational factor.

## 3. Local factors and Cassels' formula

The minimal models have bad primes 3,11,61,239 and respective Tamagawa numbers

    A: 1,5,2,2  (product 20),
    F: 1,1,2,2  (product 4).

These are the saved PARI local-reduction results. In particular both are good at 5, have a_5=-1 and #E(F_5)=7, and have no rational 5-torsion.

Cassels' isogeny-Selmer ratio, in the convention stated in Miller–Stoll, section 6, is

    #Sel_phi(A)/#Sel_phi_hat(F)
      = (#A(Q)[phi]/#F(Q)[phi_hat])
        (Omega_F/Omega_A) product_q c_q(F)/c_q(A).

Here it is 1/25. This is a theorem about finite isogeny Selmer groups and does not assume Sha finite. Therefore

    dim Sel_phi_hat(F) - dim Sel_phi(A) = 2.

The two isogeny Kummer sequences have Mordell–Weil terms of dimension one by section 2. Subtraction gives the exact relation

    dim Sha(F)[phi_hat] - dim Sha(A)[phi] = 2.

In particular dim Sha(F)[phi_hat]>=2. Since phi phi_hat=[5], this subgroup is contained in Sha(F)[5], proving

    dim_F5 Sha(F)[5]>=2.

No class number, L-value, p-adic coefficient, real regulator, BSD quotient, primary finiteness or parity assertion is an input to this last argument.

## 4. Numerator convention and precision

The numerator is computed from the Neron-normalized plus modular symbol of the conductor-11 curve [0,-1,1,-7820,-263580], twisted by the primitive quadratic character of d. PARI's documented mspadicmoments implements this twist, allowing computation at the small base level.

Here the model change from the specified quadratic twist to the minimal F has u=1; the saved change is [1,14579,0,21869]. For positive d the complex differential scaling gives Omega_F=Omega_base/sqrt(d). The quadratic Gauss factor is sqrt(d), so the twisted modular-symbol normalization matches this minimal Neron period. At primes dividing d the primitive twisted curve has additive reduction and trivial Euler factor; no omitted twist Euler factor contributes. The base and F both have one real component. The isogeny factor 5 has already been retained by using the modular symbol of the second conductor-11 curve, not silently replacing it with its partner's symbol.

The valid computation yields

    Lp(0)=O(5^5), Lp'(0)=O(5^4), J=Lp''(0)/2=4*5^4+O(5^5).

Direct power-series extraction gives [U^2]Lp=4*5^2+O(5^3). Thus the coefficient is evaluated directly, not inferred by asserting an exact double zero from finite precision. The second-derivative conversion agrees to this precision; the possible first-coefficient error is O(5^3).

Independently, the height calculation on Q1,Q2 gives

    R_scalar=4*5^2+4*5^3+4*5^4+3*5^5+4*5^7+3*5^9+O(5^10).

Dividing by log(6)^2 gives a unit determinant in U coordinates. The ordinary unit root is alpha=-1 mod5, so (1-alpha^-1)^2=4 mod5. The Tamagawa product is 4 and the torsion order is 1. Therefore the explicitly normalized point-pair quotient has valuation two and

    Q/25 = 4/(4*4*4) = 1 mod5.

The numerator/regulator calculation is not used to prove the Sha lower bound. Conversely the lower bound was not fed into the numerator. This numerical match does not supply an upper bound on Sha(F), or identify its exact order. It is the new experimental observation.
