# Exact source-support experiment on torsion functions

The question was whether a cheap explicit source can supply the norm rank that has to grow with the coefficient prime. This experiment tests actual functions on the seed and controls, before any claim of norm rank. It does not compute a Selmer group or improve a seed upper bound.

## Norm identity

For the integral Weierstrass model put w=2y+a1*x+a3 and D(x)=4*x^3+b2*x^2+2*b4*x+b6. Let psi_p(x) be the odd division polynomial with leading coefficient p. For h(T)=w(T)-m*x(T)-b, its norm from the full nonzero-torsion etale algebra is

    N(h) = Res_x(psi_p, (m*x+b)^2-D(x))/p^3.

Indeed each x-coordinate has the two values w and -w; their factors multiply to (m*x+b)^2-D(x). The resultant contributes the leading coefficient p to the third power. This identity requires no class-number or Sha input and still holds if the torsion algebra splits.

Torsion x and w coordinates are integral away p: divide psi_p by its p-unit leading coefficient, and then use w^2=D(x). Therefore h is integral at every prime outside p. If the resultant has no rational prime factor outside S (with p in S), h is an S-unit. If it has such a factor, h itself fails S-unitness. This does NOT exclude a quotient of conjugates, a character projection, or a product of different h: their outside divisors can cancel.

## Completed finite search

The candidate lists are fixed in search.gp and CONTRACT.md. They include small slopes/intercepts and seed point-adapted intercepts. Coefficient primes are5,7,11. The seed has629 candidates per prime;389a1 and37a1 have625 per prime. All5637 tests were completed in search_direct.gp.

For every seed/prime pair and every389/prime pair, the only raw S-unit survivor is m=b=0, namely w itself. For37 at7 and11 the same holds. At37,p5 there are two additional raw survivors: (m,b)=(-2,1),(2,-1). Their resultants are supported at2. The first is h=2(y+x).

The baseline w survivor has zero odd-character class: scalar -1 changes w to -w, and -1 is a pth power for oddp. Thus it cannot produce the needed chi norm rank. The two nontrivial37 survivors require a further divisor test; their norm support alone does not admit them to the original S={5,37} source. See ../shifted_control37/ for the actual prime-over2 test, which finds nonzero projected valuations modulo5.

## Independent replay and computational repair

The original high-degree resultant search hit its100s wall cap after completing four tables. Those four completed files are retained; no unfinished table is accepted. We changed the calculation, not the mathematical candidate list:

    Res(psi_p,Q) = leading(Q)^degree(psi_p) * Norm_{Q[x]/Q}(psi_p mod Q),

where Q=(m*x+b)^2-D has degree3. The resultant swap has positive sign since degree(psi_p)=(p^2-1)/2 is even. This constant-degree norm computes all nine tables in about1s. A separate replay checks all2512 completed original rows against this identity, with every exact integer matching. The final table summaries recompute smooth support from the saved integers, not printed pass fields.

This repair is an arithmetic algorithm improvement for this experiment. It does not make a rejected source into a unit or provide an upper bound across primes. The untested possibility of cancellations among these projected candidates remains open; no absence theorem for such combinations is claimed.

## Scope

No admissible new norm-rank witness for the seed was obtained. The negative result is limited to the specified raw line-function family and the tested primes. It says nothing about all explicit unit constructions. This return preserves both the successful calculations and the exact admission failure so a later construction can change it rather than repeat it.
