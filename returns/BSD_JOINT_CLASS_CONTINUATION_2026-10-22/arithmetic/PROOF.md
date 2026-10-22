# Exact parity screen for the tested source

## 1. General algebra

Let A be a characteristic-zero field with an involution tau, p an odd prime, and a in A*. Suppose tau(a)/a lies in {1,-1}. The class [a] in A*/A*^p is fixed by tau because both signs are pth powers. If a commuting scalar action has a character chi with chi(tau)=-1, its chi-projection therefore vanishes: it is simultaneously fixed and negated by tau, and 2 is invertible modulo p.

This conclusion holds for every product of scalar translates of such elements. If A has a real embedding, it also holds after adjoining any roots that already lie in A. Indeed, if b^n is such a product then (tau(b)/b)^n is a sign. The ratio is a root of unity of A; a field with a real embedding has only roots of unity +/-1. Consequently [b] is still tau-even. This does not allow roots in a larger field to be silently treated as elements of A.

If a product is a virtual unit, with div(a)=pI, its ideal-class contribution is tau-even as well: applying tau to the equality and using div(tau(a)/a)=0 gives tau(I)=I in the torsion-free divisor group. Thus faithful projection does not reappear in a hidden class-supported component of these products.

## 2. Exact five-torsion witnesses

At p=5 take sigma of order4 and tau=sigma^2. Put t=tau(a)/a in {+1,-1}, and s=sigma(a). Then the four scalar conjugates are

    (a,s,ta,ts).

For chi(sigma)=2 the integral exponents representing chi^(-j) modulo5 are (1,3,4,2). Their product is

    a*s^3*(ta)^4*(ts)^2 = (a*s)^5.

For chi(sigma)=3 the exponents are (1,2,4,3). Their product is

    a*s^2*(ta)^4*(ts)^3 = (t*a*s)^5.

The actual character idempotent differs by the factor1/4, a unit modulo5. Hence these literal identities prove the vanishing of both faithful projections. The script checks them without relying solely on finite-field formal algebra.

## 3. Seed elements and support

The retained seed model has a1=a3=0, so negation is (x,y) -> (x,-y). The seven elements in REPORT.md therefore satisfy the stated parity. The script separately verifies that P lies on the seed curve, [5]P=O, the retained sigma sends it to [2]P, and sigma^2 is negation.

The norms have the following exponent vectors at rational primes (2,3,5,2243,4547,5843):

| Element | Norm exponent vector | tau ratio |
|---|---|---|
| x(P), x(2P) | (24,0,-2,0,12,12) | +1 |
| y(P), y(2P) | (24,12,-3,6,18,12) | -1 |
| x(P)-x(2P) | (32,8,-2,4,12,8) | +1 |
| y(2P)/y(P), x(2P)/x(P) | (0,0,0,0,0,0) | +1 |

The last pair need not be ordinary units merely because its norm is one. The code computes every actual valuation above the six rational primes and multiplies those prime powers, including negative powers, to recover the principal fractional ideal exactly. Equality to idealhnf(NF,a) authenticates the complete support of each element. The saved exact field elements, valuation vectors and fifth roots are in replay/TORSION_SUNIT_RESULT.gp; SUMMARY.json records the smaller summary.

## 4. Moduli functions versus extra structures

A scalar-valued construction depending only on the isomorphism class of (E,P) cannot distinguish P from -P: [-1] is an isomorphism (E,P) -> (E,-P). If its specialization is an honest element of A, it is tau-invariant and falls under Section1. Thus an ordinary modular-function value of this kind does not repair the faithful-parity failure.

This statement must not be extended without proof to a root of a Siegel unit, a value with a nontrivial automorphy multiplier, a trivialized Hodge-line section, or a point equipped with additional level structure. Such objects may lie in another field or module and need their own descent, integral normalization and source comparison. No such comparison was constructed in this test. Adding a differential while retaining an untracked sign would be precisely an additional structure, not an unnoticed exception to the calculation above.

## 5. Completeness boundary

All multiplicative scalar combinations and roots inside A of this explicit seven-element family have zero faithful source contribution. This is a complete statement about that family, not about all S-units or all ideal classes. The actual faithful class dimension has not been calculated or bounded anew. A new family must change the parity/source issue as well as control its support; satisfying only one of those conditions is insufficient.
