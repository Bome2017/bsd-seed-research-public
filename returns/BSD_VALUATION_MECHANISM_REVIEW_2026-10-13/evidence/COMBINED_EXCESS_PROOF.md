# Independent exact audit of the d=329233 positive-excess control

Grade: written deduction with exact rational/integer checks. The PARI rank upper bound is retained, not independently rerun. No analytic value, p-adic height, class number, or predicted Sha order enters this lower-bound proof.

## Verified data

Let

- A=[0,-1,1,-1120075138986,-826418095533154920];
- F=[0,-1,1,-847680091476076,-9499397825675855099600].

The points are exactly those in the final GEOMETRY row of `geometry_screen_second.out`, hard-coded in `checks/combined_exact.py`. The checker uses completed-square coordinates Y=y+1/2, retaining the x^2 coefficient -1. A small 128 MB PARI call only supplies the explicit candidate rational map; the Python checker independently verifies its entire polynomial curve identity, absence of cancellation at its poles, differential identity, and point images.

The resulting degree-five map phi:A -> F satisfies

    phi(P1)=-2 Q1-Q2,
    phi(P2)=Q1-2 Q2.

Its matrix M=[[-2,1],[-1,-2]] has determinant 5. The two finite-field saturation tests use q=7 and q=109, with group cardinalities 10 and 120. After multiplication by the prime-to-5 part and discrete logarithm in a chosen order-five subgroup, the rows are:

    A: (4,1),(1,2), determinant 2 mod5;
    F: (3,4),(1,0), determinant 1 mod5.

They kill rational five-multiples. Both matrices are invertible, so the point pairs are independent modulo 5. Together with the retained upper bound rank(A)<=2 and isogeny invariance of rank, both pairs span their full Mordell-Weil lattices over Z_5. No saturation away from 5 is asserted.

Both curves have point counts 7,10,18,20 at 5,7,13,19. Good-prime reduction injectivity for prime-to-characteristic torsion excludes all rational torsion. At 5, a_5=-1, so reduction is good ordinary and non-anomalous.

## Periods and local terms

The minimal-model discriminants are

    Delta_A=-11^5*329233^6,
    Delta_F=-11*329233^6.

The exponent at every prime is less than 12; hence the displayed integral models are minimal. Exact c4 and -c6 tests show split I_5 and split I_1 at 11. At the prime d=329233, the checker translates x by (1-d)/3 and computes the I_0* cubic. It is separable and has three residue roots for each curve. Thus c_d=4 on each, while c_11(A)=5 and c_11(F)=1. The respective Tamagawa products are 20 and 4. The cubic data and roots are preserved in `combined_exact.json`.

The map satisfies phi*omega_F=omega_A. Its kernel x-coordinates are 1536421 and 5157984. At these coordinates, the completed-square right sides divided by d are respectively (3621563/2)^2 and (39837193/2)^2, both positive. Thus all five kernel points are real. Negative discriminants make both real loci connected. Integration on the resulting degree-five covering of real tori gives

    Omega_F/Omega_A=1/5.

## Sha lower bound

Cassels' isogeny-Selmer formula, in the same convention as Miller--Stoll section 6, now gives

    #Sel_phi(A) / #Sel_dual_phi(F)
       = (Omega_F/Omega_A)*(C_F/C_A) = 1/25.

Rational torsion kernels are trivial. Since both displayed point pairs are Z_5 bases and det M=5, F(Q)/phi A(Q) has dimension one over F_5. The dual quotient has the same dimension because dual_phi*phi=[5] on a rank-two group. The rational quotients are killed by 5, so no prime-to-5 saturation claim is needed.

The two finite-isogeny Kummer sequences therefore yield

    dim_F5 Sha(F)[dual_phi] - dim_F5 Sha(A)[phi] = 2.

Since phi*dual_phi=[5], Sha(F)[dual_phi] is contained in Sha(F)[5]. Hence

    dim_F5 Sha(F)[5] >= 2.

This is conditional only on the stated retained rank upper bound and the standard named theorem imports. No primary finiteness is assumed or proved. No upper bound, exact Sha order, full residual-image claim, or seed theorem follows.

## Reproduction and sources

Run `python3 checks/combined_exact.py` from the packet root. Its JSON output is deterministic. The source map was obtained using `checks/combined_exact_source.gp`; that tiny source-only call does not compute an L-value or a height and is not the verifier for the identities.

The imported arithmetic formula is Cassels' isogeny-Selmer ratio as stated in Miller--Stoll, *Explicit isogeny descent on elliptic curves*, section 6: https://www.mathe2.uni-bayreuth.de/stoll/papers/isogeny-descent.pdf . The local reduction rule is the I_0* branch of Tate's algorithm, e.g. Cremona, chapter 3: https://johncremona.github.io/book/fulltext/chapter3.pdf . These theorem sources are retained from the preceding positive-control audit; they were not reproved here.
