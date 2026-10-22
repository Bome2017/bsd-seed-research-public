# Actual coefficient-seven local condition

This note matches a finite local power computation to a necessary Selmer condition. It does not assert a unit basis or any class-group completeness.

## The necessary condition

For 389a1, written as \(y^2+y=x^3+x^2-2x\), the retained exact count is \(\#E(\mathbf F_7)=13\). Thus reduction is ordinary and nonanomalous. Write

\[
0\longrightarrow V^+\longrightarrow E[7]\longrightarrow V^-\longrightarrow0
\]

for the ordinary filtration. The quotient is unramified with nontrivial Frobenius character \(a_7=2\pmod7\). The completed local point group is its formal subgroup, since 13 is prime to 7. Taking a division point inside the formal group shows that its Kummer image lies in the image of \(H^1(\mathbf Q_7,V^+)\). Local Euler characteristic and \(H^0(V^-)=H^2(V^+)=0\) show that the latter has dimension one and injects into \(H^1(\mathbf Q_7,E[7])\). This agrees with the one-dimensional local point quotient. This paragraph uses the standard ordinary filtration and local duality inputs retained by the root's `LOCAL_CONDITION_REVIEW.md`.

Let T be a nonzero formal 7-torsion point and K=Q7(T). Pairing with T kills V+ and identifies V-|K with mu7. In particular every local Kummer class evaluates to zero in H1(K,mu7). Under the Schaefer--Stoll descent source map this means that its value at T is a seventh power in K. Only this necessary direction is used below; no converse is required to exclude a source element.

The actual number-field data make this branch explicit. The retained point field has three primes above7 with (e,f)=(6,1),(7,3),(7,3). Direct evaluation of the saved universal point gives valuation pairs

\[
(v(x(T)),v(y(T)))=(-2,-3),(0,0),(0,0),
\]

respectively. Hence the first branch really is the formal-point branch. Its scalar automorphism fixes that prime. This tests the field/point identification rather than selecting a branch solely by its degree.

The source comparison is the natural Weil-evaluation map used in the retained descent. The normalization of a Miller function does not enter this zero test, because the input consists of source elements already expressed in A*/A*7. An unmatched alternate descent normalization would need its own comparison.

## Exact finite quotient and precision

Let P be this prime and pi a computed element with vP(pi)=1. Its local ramification index is6. Every element of 1+P^8 is a seventh power: the logarithm has valuation at least8, division by7 leaves valuation at least2, and exponential converges for valuation greater than e/(7-1)=1. Thus reduction to

\[
(\mathcal O_K/P^8)^*/((\mathcal O_K/P^8)^*)^7
\]

captures the full local unit seventh-power class. A local unit has zero class here exactly when it is a seventh power in K. This is not merely a necessary test at insufficient precision.

The calculation uses PARI `idealstar` modulo seventh powers and `ideallog`. Both P^8 and P^9 give an abstract quotient (Z/7)^6. Their coordinates need not agree, but zero and rank agree. At both precisions the explicit local unit 1+pi^2 has a nonzero class, while its seventh power has zero class. These are local calibration elements, not asserted global ordinary units.

## Compact sources and cancellation

The sibling arithmetic lane supplies26 actual field elements and their six scalar translates, together with a156-by99 integer matrix K whose columns kill their full principal-divisor matrix. Thus each column represents an actual ordinary unit. This admission depends on that exact principal-ideal certificate; the local calculation does not establish it by itself.

Some individual factors have positive valuation at P. For each factor a_j, write

\[
v_j=v_P(a_j),\qquad \widetilde a_j=a_j\pi^{-v_j}.
\]

The same pi is used throughout. Since \(\sum_jK_{jc}v_j=0\), the local residue class of the compact unit \(\prod_ja_j^{K_{jc}}\) is exactly the sum of the logs of \(\widetilde a_j\) with coefficients K_jc. No term from the uniformizer is discarded. The scalar chi projection uses the retained integral representative [6,2,3,1,5,4] for the six orbit powers.

On this first batch all99 compact units have zero local class even before chi projection. This gives no rejection rank. The156 factor columns themselves have451 nonzero coordinates modulo7 at precision P^8, so the zero output is not caused by a zero-valued extractor. It is also reproduced at P^9.

## Independent split-prime evaluation

At q=38711,66977,131671 the reduced field polynomial has48 distinct roots. The universal point coordinates give the48 distinct nonzero 7-torsion points, and the saved scalar map is checked against multiplication by3 using the elliptic group law. Evaluation of all compact products and their chi projections gives zero unit-residue vectors at each of these primes. The additive-function quotient therefore has rank zero as well.

The allowance used in that separate test consists of all linear functions on E[7], a two-dimensional space. Every one of its49 elements is checked to be killed by the quotient computation. The root's independent geometry comparison shows this is the same full split-prime affine-norm allowance; it is not counted as an extra condition beyond all affine-norm rows at the same place.

## Scope

The formal branch is a genuinely additional local Selmer condition on a global cohomology source. On genuine H1 classes it removes at most one dimension, so its existence alone cannot give a growing-rank theorem. On the current actual99-unit batch its rank is zero. Zero at these places does not prove the units globally trivial or seventh powers; an exact multiplicative dependency test is separate.

No complete-unit or ordinary-class presentation is inferred. There is no new whole-source upper bound or seed conclusion from this first batch.

Source freshly inspected: Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, long version, Section5 (actual local source evaluations and local Kummer image), https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf. The ordinary filtration argument is a written deduction under the retained local representation inputs; it is not claimed as a newly quoted theorem from that paper. PARI calls were checked against the installed function help. No new BNF computation was run.

## Changed 11a1 source

The same local argument applies to11a1, E=[0,-1,1,-10,-20], where a fresh count gives #E(F7)=10 and a7=-2. The code makes its curve coefficients explicit; no389 group law is used for this source. Its authenticated26 compact ordinary units have projected local rank1 at bothP^8 andP^9. Actual split-prime additive-function defects have rank3, and their stack with the formal local row has rank4. The nonzero4-by4 minor is in11a1_MINOR_CERTIFICATE.json. As the complete ordinary chi-unit space has dimension4 under the retained full-image framework, its joint kernel is zero. This conclusion leaves the ordinary class and divisor contributions untouched. SeeREPORT.md for the full scope and arithmetic bindings.
