# Independent review of the weight-three Kato index return

**CONFIRMED_WITH_CLARIFICATIONS** -- at retained-input and imported-theorem grade. No blocking defect found in the claimed cohomological index bound. This review supplies the explicit componentwise Euler-system application and specialization bookkeeping behind the submitted proof. No new seed prime is settled.

## Accepted statement

For the retained weight-three datum at a good ordinary seed prime p >= 5 outside {19,59,487}, using the actual coefficient DVR O and the normalized integral Kato class specified in the return,

    length_O B_g = b-a+h <= b,
    length_O(B_g/W_g) = b-a+h-2 <= b-2,
    b <= 3  ==>  Sha(E/Q)[p^infinity]=0.

Here a is the global Kato index, b is its singular local index at p, and h is the length of Kato's j_*-cohomology H2. The inequality uses h<=a; the exact equality does not. B_g is finite by the noncentral weight-three case of Kato's theorem, but is a different discrete Selmer group from the seed's primary Selmer group.

## Checks and clarifications

1. **Twist and finiteness: confirmed.** Kato's cohomological D(g)(1) equals V_g chi^{-1} omega. Thus r=1 is the direct twist for g; the Tate dual is r=2 for g*. Neither is central in weight three. Kato's fixed-form almost-all-primes assertion is not a uniform assertion about the diagonal family (g_p,p).

2. **Integral Euler-system bound: confirmed with an expanded proof.** The conductor-one, residually ramified place 2243 supplies a unit transvection in the cyclotomic kernel. Carayol's hypotheses fit. The weaker hypothesis of Kato 13.4(3), together with residual irreducibility, suffices for the adaptation; a new full-image theorem for g is not needed. Stable-lattice homothety, integral Iwasawa H1 freeness and the finite normalized-zeta quotient are all accounted for. Kato 13.7 concerns the collection of Euler systems, so the componentwise application is spelled out in VERIFIED_DERIVATION.md section 3.3.

3. **Specialization: confirmed with the Tor term displayed.** If t=length H2_Iw(T)[gamma-1] and a0 is the specialized Iwasawa index, then a=a0+t and Kato's cycle calculation gives h-t<=a0. Hence h<=a. There is no assumption t=0.

4. **Poitou--Tate: confirmed.** The bad-place discrepancies between Kato's S(T) and the propagated Bloch--Kato group vanish on the retained domain. The global and relevant p-local invariant factors are one. The exact sequence gives the Tate-dual length b-a+h; Kato 14.16(1) gives the same length for B_g. No self-duality of the weight-three representation was smuggled in.

5. **Quotient correction: confirmed.** Quotienting by W removes exactly two from finite length. The excess Sha[p] injects into the quotient's pi-torsion; it need not equal it. A quotient length at most one suffices by retained parity. All lengths and thresholds use pi, not an unqualified p-adic valuation.

6. **Numerical boundary: correctly retained.** The bound is on b=v_pi(x_g/d_g), with d_g the actual dual-exponential image lattice. Kato 14.21 explicitly assumes p does not divide the modular level and cannot be used as stated here. An integral calculation at ramified p and an independent bound on b remain open.

7. **Finite-pool shortcut: correctly rejected at its stated scope.** The determinant congruence for a fixed weight-three form restricts p to the prime divisors of one nonzero fixed norm. This does not exclude p-dependent constructions or uniform results about them.

## Primary-source verification and integrity

The input manifest verifies **15/15**; all three loose files match. The source PDF for [Kato (2004)](https://www.numdam.org/article/AST_2004__295__117_0.pdf) was freshly downloaded and is byte-identical to the archived PDF. The decisive formula pages were rendered and read, including 13.4, 13.14, 14.2, 14.9.3, 14.14-14.16 and 14.21. This closes the return's fresh-image access limitation. Carayol's printed pp.409-411 were also read in the primary PDF.

The cross-reference in Kato 14.5(3) really prints 12.5.1, while 12.5(4)'s image condition is numbered 12.5.2. Treat the present argument as the explicit 13.4(3) adaptation written here; do not describe the discrepancy as merely OCR corruption or claim an official erratum.

The supplied finite-algebra checks replay byte-for-byte: 14 module cases, 105 index-accounting cases, 18 unit-transvection cases and 6 nonunit controls. These check finite algebra, not the imported arithmetic theorems. An independent exact specialization check includes a codimension-two Tor control. The source and retained-input bindings are recorded separately.

## What this adds and what it does not

The return supplies a valid arithmetic upper bound for the changed Selmer group in terms of a precisely defined cohomological index. Together with retained residual control, a small index would settle a seed primary group. This is more than an unsupported replacement of Sha by a new symbol: the direction of the Euler-system inequality has been verified.

No b has been evaluated at an unsettled prime, and there is no proof that b<=3 outside a finite set. The next missing inputs for this numerical route are the ramified local lattice comparison and independent control of these indices. Neither is supplied by the finite-pool argument. Supersingular primes and the excluded primes remain outside this statement. There is no human-referee or formal-proof claim and no fresh replay of retained seed certificates.

Inputs, release files and repositories were not changed. No production computation, cloud job, message, commit or push was launched.

FIN, ORDER9 and Q36 are unchanged.
