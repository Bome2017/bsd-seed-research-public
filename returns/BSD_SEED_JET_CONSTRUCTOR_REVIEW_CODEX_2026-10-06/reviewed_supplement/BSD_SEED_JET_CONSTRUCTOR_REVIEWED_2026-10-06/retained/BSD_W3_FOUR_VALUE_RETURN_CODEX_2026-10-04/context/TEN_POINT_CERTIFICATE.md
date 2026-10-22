# A nonzero genuine jet is sufficient after varying the critical point

Grade: WRITTEN_DERIVATION, conditional on ARITHMETIC_SOURCE.md, LOCAL_REVIEW.md and VARIABLE_WEIGHT_INDEX.md. No arithmetic nonvanishing is asserted.

## Statement

For the actual integral Euler-system coordinate F_p in this packet, on its cofinite ordinary domain,

    F_p not in (p,T,S)^4  ==>  Sha(E/Q)[p^infinity]=0.     (J1)

The original diagonal may be zero. We need not prove that it detects every nonzero jet. Ten explicitly specified critical specializations detect the whole jet and each has its own seed index bound.

## 1. Integral interpolation

Write F=Σ f_ab T^a S^b in Z_p[[T,S]], and put c_ab=p^(a+b)f_ab modulo p^4 for a+b≤3. There are ten such coordinates. Terms of degree at least four contribute zero at T,S in pZ_p.

For w≥0 put x_w=((1+p)^w-1)/p in Z_p. For i,j≥0 with i+j≤3, define

    e_ij=F((1+p)^(10+i)-1,(1+p)^(7+j)-1) mod p^4.

Then

    e_ij=Σ_(a+b≤3) c_ab x_(10+i)^a x_(7+j)^b mod p^4.    (J2)

The ten-by-ten evaluation matrix V in (J2) is invertible over Z_p for p≥5. To see this, use the Newton polynomials

    N_ab(X,Y)=Π_(u<a)(X-x_(10+u)) Π_(v<b)(Y-x_(7+v)),
    a+b≤3.

Their change of basis from the monomials is triangular with diagonal one. Order the nodes and polynomials by total degree. Evaluation vanishes unless a≤i and b≤j. The diagonal entries are products of differences x_(10+i)-x_(10+u) and x_(7+j)-x_(7+v). Every such difference reduces to a nonzero integer of absolute value at most three modulo p. Thus the diagonal entries are units. In particular det(V) mod p=Π_(a+b≤3)a!b!=576 mod p.

It follows that, as ideals of Z/p^4 Z,

    (e_ij : i+j≤3)=(c_ab : a+b≤3).                       (J3)

All c_ab vanish if and only if f_ab is divisible by p^(4-a-b) for every a+b≤3. This is exactly F in m^4. Therefore

    F not in m^4 <=> at least one e_ij is nonzero.         (J4)

The inverse matrix also recovers the ten weighted coefficients from the ten values, at their correct precisions. This is integral interpolation; no division by a p-power is allowed or needed.

## 2. Apply the arithmetic implication

Every node in (J2) is one of VARIABLE_WEIGHT_INDEX.md's genuine noncentral modular specializations. Its coefficient representation reduces to E[p], and its ordinary finite local condition reduces to the seed's Kummer condition. Consequently a nonzero e_ij implies (I3). Combining this with (J4) proves (J1).

In particular, a proof that the actual F_p is not in m_p^4 for all but finitely many ordinary p would prove primary vanishing for that ordinary tail. A nonzero formal polynomial in place of F_p proves nothing about the seed.

## 3. An arithmetic lower-divisibility consequence

The two known Mordell–Weil directions force b^Z_(w,s)≥2 at every node whenever its index is finite. A zero value has infinite valuation and also lies in p^2. Thus all e_ij are in p^2 Z_p. Applying the same unit interpolation matrix modulo p^2 gives c_ab in p^2 for every a+b≤3. In particular

    f_00 in p^2 Z_p, f_10,f_01 in p Z_p,
    F_p in m_p^2.                                       (J5)

This proves total maximal-ideal divisibility for this actual arithmetic source. It does not prove a T^2 factorization or that f_00, f_10, f_01 are zero.

The remaining object is therefore the actual class

    [F_p] in m_p^2/m_p^4.                               (J6)

Its nonzero status is sufficient. The module in (J6) has F_p-length 16; it is not a one-dimensional space in which choosing a nonzero vector produces a Kato class.

## 4. Exact scope relative to the submitted diagonal test

The submitted counterexample T-S remains valid for its diagonal. Even (T-S)^2 and p^2(T-S), both consistent with the new lower-divisibility condition, vanish there while some nodes in (J2) detect them. These are formal controls, not values of the seed's family.

Conversely a nonzero power series such as T^4 has a zero fourth-order jet. Rational nonvanishing, a unit somewhere among its coefficients, freeness of the family symbol module, and a Coleman isomorphism do not prove (J6) nonzero.

No equality of (J6) with C_p, a Kurihara witness, or the old normalized W3 scalar has been derived. Such an equality must be proved in matched integral coordinates before using it as a collision verdict. This packet neither asserts a new independent cofinite estimate nor refutes one.
