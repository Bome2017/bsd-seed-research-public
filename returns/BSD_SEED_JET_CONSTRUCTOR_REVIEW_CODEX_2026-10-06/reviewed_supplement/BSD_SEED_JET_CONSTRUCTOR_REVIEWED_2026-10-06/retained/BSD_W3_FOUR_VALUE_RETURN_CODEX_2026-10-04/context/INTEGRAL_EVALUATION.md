# Construct the integral critical-value functional before dividing it

Grade: WRITTEN_DERIVATION with the Hida/control inputs in
COFINITE_HIDA_CONTROL.md. The comparison to A_g is not asserted to be a unit.

## 1. The actual modular-symbol line

Work outside the fixed finite set of COFINITE_HIDA_CONTROL.md, and
outside the retained weight-three local exceptions. Set O=Z_p. At the
weight-three point g use the integral coefficient module Sym^1(O^2).
In this file its polynomials are P(X,Y)=aX+bY and its right matrix
action is

    P|[a b;c d] = P(dX-bY,-cX+aY).

This is the convention of Maksoud section 2.1. Use compact/parabolic
cohomology or, equivalently after localization at the non-Eisenstein
maximal ideal, the integral modular-symbol realization. The integral
identification of these realizations is part of the ordinary
control/multiplicity-one input. It is not an identification of a
rational eigenspace with an arbitrary integral lattice.

For a complex cusp form g define the symbol

    I_g({b}-{a}) = integral_a^b g(z)(X-zY) dz.

Let iota be the complex-conjugation involution in this polynomial
convention and e_plus=(1+iota)/2. At D={infinity}-{0}, its action on
coefficients is (X,Y)->(-X,Y). Therefore the coefficient of Y is
unchanged by e_plus. This sign convention is explicit; it is not the
label of the opposite convention using (zX+Y) without the same
coefficient action. In the anti-ordinary family convention the
weight-three sign is transported by the Atkin--Lehner map in Maksoud
(14), including its (-1)^k sign.

Choose the primitive integral generator phi_g of the resulting signed
g-line, obtained by integral specialization. Define Omega_g^sym by

    e_plus I_g = Omega_g^sym * phi_g.

Here e_plus includes the factor 1/2. Thus Omega_g^sym differs by the
explicit factor 1/2 from the convention using I_g+iota I_g. Since p>=5
this is harmless for valuations, but it is not omitted from the
definition. A new choice of primitive phi_g multiplies it by a unit
and divides Omega_g^sym by the same unit.

## 2. Evaluation

Define the O-linear functional on the actual symbol module by

    E_2(phi) = - coefficient_Y(phi(D)).                (E1)

It is integral: it evaluates an integral symbol at an integral divisor
and takes an integral polynomial coefficient. Mellin's identity gives

    integral_0^(i infinity) z*g(z) dz
        = L(g,2)/(2*pi*i)^2.

One obtains this identity first in the half-plane of absolute
convergence and then by analytic continuation; it is not an
unjustified term-by-term absolutely convergent series assertion at
the endpoint s=2. Consequently the constructed value is

    M_p := E_2(phi_g)
         = L(g,2)/Theta_g in Z_p,
    Theta_g := (2*pi*i)^2 Omega_g^sym.                 (E2)

The algebraic value in (E2) is transported through the fixed p-adic
embedding. We are not taking a p-adic valuation of an arbitrary
complex period. Noncentral critical-value nonvanishing makes M_p
nonzero, but says nothing about v_p(M_p).

This constructs the integral functional and a primitive specializing
symbol. It does not yet construct the divided residual object in the
submitted task.

## 3. Exact comparison with the retained local frame

Retain the previous return's definitions, without renaming its period:

    per_g^+(w_g) = Omega_g^K * gamma^+,
    w_g = c_g e_g,
    A_g = c_g L(g,2)/Omega_g^K,
    b_p = v_p(A_g).

Here e_g is the specified Gauss-sum local frame, including its tame
character and the local Euler cancellation already derived. Define

    eta_p = c_g * Theta_g/Omega_g^K.                   (E3)

The complex ratio Theta_g/Omega_g^K is interpreted through the two
algebraic critical quotients L(g,2)/Theta_g and L(g,2)/Omega_g^K and
the chosen p-adic embedding. The local comparison c_g is an element
of the p-adic coefficient field. No assertion that c_g, or eta_p, is
algebraic over Q is needed or made. Thus (E3) is a well-defined
scalar in the p-adic coefficient field, not the p-adic valuation of
an arbitrary complex number. We have the exact identity

    A_g = eta_p M_p,
    b_p = v_p(eta_p) + v_p(M_p).                      (E4)

Neither eta_p being integral nor eta_p being a unit has been proved
here. In particular it is not legitimate to use b_p>=2 to conclude
M_p is in p^2 Z_p. That conclusion would follow if eta_p were a unit;
it does not follow from (E4) alone.

For example, eta=p^2 and M=1 satisfy A in p^2 Z_p while M is not in
p Z_p. These are lattice controls, not asserted values for the seed.

The submitted equation E_2(lambda_3 Phi)=unit*A_g is precisely the
still-required statement eta_p in Z_p^times, after transporting the
stated conventions. Giving eta_p a name is not a proof of this
statement. The cofinite branch theorem does remove the ambiguity of
ramified coefficient extensions from this comparison.

## 4. What must be transported to prove the unit statement

One needs the integral, ramified weight-three comparison of the
q-expansion/modular-symbol period lattice with

    Z_p * e_g,

where the latter contains tau(omega)*a_alpha*t on the ordinary local
quotient. The previous local formula is exp*(Q_g)=p^(-2) Z_p e_g.
Thus the comparison must include both the Gauss factor and the
p-Euler factor, rather than using a good-crystalline formula at a
form of level Np.

Freeness of the Hida algebra or of its symbol module is not this
comparison. It prevents an eigenspace specialization defect on the
cofinite domain; it does not identify the two de Rham lattices by
itself. SOURCE_UNIT_REPAIR.md records what the closest source does
and the integral repair that can be justified, without treating that
repair as a completed application to e_g.

## 5. The weakest sufficient divided test

If eta_p is proved a unit, the requested first residual object is

    a_p^(2) = p^(-2) M_p mod p,

and a_p^(2)!=0 implies b_p=2. However the retained endpoint allows
b_p=3 as well. The less restrictive test is the single class

    J_p = p^(-2) M_p mod p^2 in Z/p^2 Z.              (E5)

Once the unit comparison holds, J_p!=0 is equivalent to b_p<=3
because b_p>=2 is retained. It implies Sha[p^infinity]=0 by the
retained index inequality and parity. The nonzero condition is
unchanged by replacing the primitive symbol generator by a unit
multiple. It must not be discarded merely because a_p^(2)=0.

No value of a_p^(2) or J_p is certified in this return. Both are
conditional on the unit comparison when they are used for BSD.
The cofinite ordinary statement still does not cover supersingular
primes or the exceptional coefficient primes.
