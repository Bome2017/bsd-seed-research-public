# Independent review of the complete relative class bound

Status: **WRITTEN DEDUCTION SUPPORTED UNDER THE RETAINED EXACT FIELD INPUTS**.
This review checks the proof rather than treating its arithmetic output as a
class-group computation. It supplies an independent exact numerical certificate
for the same integer threshold, with a slightly weaker real bound.

The object is the actual coefficient-five point field A of degree24, with
scalar-minus-one fixed field K of degree12. Their maximal-order discriminants,
signatures (4,10)/(4,4), scalar action and field inclusion retain their previous
exact-computation grades. No new maximal-order or discriminant certification is
claimed here.

## Checked mathematical interfaces

1. A relative norm-one unit different from +/-1 generates A/K. Consequently
   the relative field discriminant divides its quadratic order discriminant.
   Its logarithm has at most20 nonzero all-embedding coordinates, because the
   two real places becoming complex force zero logarithms for norm-one units.
   The triangle and Cauchy inequalities therefore give the stated lower length
   (log(delta)-24log(2))/(2sqrt(5)). This is a statement about every relative
   unit, including units not found computationally.

2. Minkowski's theorem in rank6 gives V>=pi^3 lambda^6/384. I independently
   rederived the all-embedding covolume conversion
   V_L=sqrt([L:Q])*R_L/2^(r2/2) by Cauchy--Binet. Embedding the rank7 base unit
   lattice multiplies its volume by2^(7/2). The norm index I is at most2^7:
   N(U_A)/U_K^2 injects into U_K/(+/- U_K^2), because a negative square cannot
   be a norm at a real place becoming complex. Omitting that sign argument
   would only give2^8. With it, R_A/R_K=64V/I>=V/2 is correct.

3. The norm on the entire ordinary class group is surjective. A/K is quadratic
   and ramified at finite places, so it is disjoint from the ordinary Hilbert
   class field of K. Chebotarev provides, in each K ideal class, a prime split
   in A; its prime above has that ideal norm. Thus the whole relative kernel
   has order h_A/h_K. This step does not assume any selected primes generate
   either class group. On the five-primary groups jN=1+tau and Nj=2 identify
   the norm kernel with the anti part. Its five-length bounds the sum of the
   two faithful F5-character dimensions, without assuming those dimensions
   are equal.

4. The analytic class-number formula gives
   h_A/h_K=sqrt(D_K*delta)*L_K(1,psi)/((2pi)^6*(R_A/R_K)).
   The factor is D_K*delta, not delta alone. The real signatures and roots of
   unity cancel; the complex-signature difference is six.

5. The primary source used for the L-value upper estimate is Louboutin,
   *Explicit Upper Bounds for Residues of Dedekind Zeta Functions and Values of L-Functions at s=1, and Explicit Lower Bounds for Relative Class Numbers of CM-Fields*, Canadian Journal of
   Mathematics53(6) (2001),1194--1222, Theorem4(1), display(10), printed1197.
   It applies to primitive ray characters over an arbitrary degree-m number
   field. The finite conductor norm is used. It does not require an everywhere
   totally imaginary or CM extension, and it does not impose the different
   infinity-unramified restriction appearing in Theorem5. The quadratic
   conductor--discriminant equality supplies conductor norm delta here.
   Source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008414X00028418
   DOI:10.4153/CJM-2001-045-5.

## Independent numerical certificate

`check_analytic_coarse.py` does not import the author's interval routine or
printed floating-point constants. It uses separate, coarser rational inequalities
for e, pi, logarithms and square roots, checked with Python integer/Fraction
arithmetic. It establishes

    h_A/h_K < 280*10^66 < 5^98.

This independently confirms

    length_Z5 ker(N)[5^infinity] <=97,
    dim_F5 Cl(A)[5]^chi2 + dim_F5 Cl(A)[5]^chi3 <=97.

The theory script establishes the slightly tighter bound262*10^66. I read its
outward-series implementation and found its directions and remainders correct;
my separately implemented certificate confirms the integer threshold97, not
its tighter decimal ceiling. Both require the written mathematics above.

## Scope

This is an unconditional complete class upper bound relative to the retained
exact field facts. It uses neither GRH nor elliptic BSD/Sha information and
includes classes absent from the collected relations. It does not prove the
class group is small. The optional complete-source ceiling3+97=100 also retains
the prior source/valuation/interface hypotheses; this review does not reprove
those elliptic interfaces. It is not a source bound at other coefficient primes
and does not settle FIN, ORDER9 or Q36.
