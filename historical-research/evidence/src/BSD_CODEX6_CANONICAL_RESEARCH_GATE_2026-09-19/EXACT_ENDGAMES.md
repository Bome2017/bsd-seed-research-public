# Exact endgames and their logical limits

**Status:** written elementary proofs and exact arithmetic checks. No new theorem controlling this seed's Sha or the arithmeticity of its leading term; no new Lean proof. The arithmetic hypotheses below are retained imports, including the p=3 R1/R2 qualifications.

## E1. The order gap at 441

Let G be a torsion abelian group. Assume its 2-, 3- and 5-primary parts have orders 1, 9 and 1. Assume also that if G is finite, its order is a square. For the seed, the latter is the retained Cassels–Tate consequence under finiteness.

If G is finite then

\[
\#G=9t^2,\quad t\in\mathbb Z_{>0},\quad (t,30)=1.
\]

Indeed the prime factorization of its square order has exponent two at 3, exponent zero at 2 and 5, and even exponents elsewhere. If t is not 1, some prime at least 7 divides t. Consequently

\[
\boxed{G\text{ finite and }\#G<441\ \Longrightarrow\ \#G=9.}
\]

The strict inequality is sharp under these abstract assumptions: `(Z/3)^2 direct_sum (Z/7)^2` has order 441, the required primary parts and a perfect alternating pairing. On each `(Z/p)^2`, use `(a,b),(c,d) -> (ad-bc)/p mod Z`, then take the orthogonal sum. Thus replacing `<441` by `<=441` does not force order nine. This is an abstract countermodel, not a claimed Sha of an elliptic curve.

**Endpoint:** FIN plus the order-nine input to FORMULA, conditional on the displayed bound. **First missing arrow:** an independent arithmetic proof of finiteness and the bound. **Still missing:** q=36 and the carried provenance repairs. **Converse:** order nine supplies both finiteness and the bound. Therefore this endgame does not by itself reduce mathematical difficulty.

## E2. A bound on all torsion levels already implies finiteness

Let G be any torsion abelian group. Suppose, for every integer n>=1, that G[n] is finite of order less than 441. The subgroups

\[
G[1!]\subseteq G[2!]\subseteq G[3!]\subseteq\cdots
\]

exhaust G: an element of order d belongs to G[m!] for m>=d. Their cardinalities are nondecreasing integers at most 440. There can be only finitely many strict increases, so the chain is eventually constant. Its union is that final finite subgroup and has order below 441. E1 now gives order nine under the retained primary and square-order hypotheses.

The same proof works for any divisibility-increasing sequence cofinal among positive integers. A factorial sequence is one convenient choice; the bound need not be separately proved at every integer if cofinality is proved.

Uniform boundedness without the threshold already proves FIN. A numeric constant below 441 supplies the additional order conclusion. Neither the constant nor its uniformity is available merely from pointwise finiteness.

It is not enough to replace “all n” by “all primes p”: the infinite group

\[
(\mathbb Z/3)^2\oplus(\mathbb Q_7/\mathbb Z_7)^2
\]

has the retained small-primary parts, and its p-torsion has order at most 49 at every prime. Its groups killed by `7^k` grow without bound. This example also shows why finite prime support alone does not prove FIN. It is an abstract quantifier counterexample; no claim is made that it is realized by the seed.

For the actual curve, the standard Kummer exact sequence identifies

\[
\operatorname{Sel}_n(E/\mathbb Q)\big/\delta_n(E(\mathbb Q)/nE(\mathbb Q))
\simeq\Sha(E/\mathbb Q)[n].
\]

A bound on this quotient is the relevant input. Information about the known points or a minor formed from their localizations controls only their image unless a further argument controls the quotient.

**Endpoint:** FIN, and order nine if the bound is below 441. **First missing arrow:** the uniform bound on the actual quotient. **Converse under E1's inputs:** order nine implies every displayed bound. These are useful sufficient certificates, not established reductions in difficulty.

## E3. The denominator threshold 174

Retain the rigorous interval

\[
|q-36|<\epsilon=573/100000.
\]

If q=a/b is reduced with `1<=b<=174` and q differs from 36, then `|a-36b|>=1`, so `|q-36|>=1/b>=1/174`. This contradicts the interval since

\[
174\epsilon=\frac{49851}{50000}<1.
\]

Hence bounded rationality forces q=36. The uniform denominator cutoff is sharp for this interval: `q=36+1/175=6301/175` lies inside it, is reduced, and differs from 36, because

\[
175\epsilon=\frac{4011}{4000}>1.
\]

An integer D with `Dq` integral and `D<=174` is also sufficient; a reduced-denominator bound does not mean that `174q` is integral. Rationality alone, with no useful bound, is insufficient. The much tighter floating-point estimate is not substituted for this rigorous interval.

**Endpoint:** q=36 only. **Still missing:** FIN and order nine for FORMULA. **Converse under the interval:** q=36 implies the bounded-rationality statement. Its antecedent still requires new arithmetic input.

## E4. Quantitative algebraicity is an alternative

Suppose q is algebraic with primitive irreducible polynomial `f(X)=a product_j(X-q_j)` in Z[X], where q_1=q. If

\[
|a|\prod_{j>1}|36-q_j|\le M,\qquad \epsilon M<1,
\]

then the integer `f(36)` has absolute value less than one. It is zero. Irreducibility and the rational root 36 imply q=36. A degree bound without conjugate control supplies no such conclusion.

The retained convenient degree-two specialization is also immediate. If q is a totally positive algebraic integer of degree two with trace T<=246, its other conjugate q' is positive and

\[
q'=T-q<246-(36-\epsilon)=210+\epsilon,
\quad |36-q'|<174+\epsilon.
\]

Thus `|(36-q)(36-q')| < epsilon (174+epsilon) < 1`, since the last product is exactly `9970528329/10000000000`. This is impossible for the nonzero integer `f(36)`. The degree-one case is already an integer in the interval, hence 36. Therefore the hypotheses “totally positive algebraic integer, degree at most two, trace at most 246 in degree two” force q=36.

These hypotheses, if true of the seed's q, would close the analytic scalar. They do not follow from the exact Mellin period or finite p-adic approximations. The reverse implication from q=36 is trivial, again preventing an automatic difficulty-reduction claim.

## E5. An exact sufficient contract for a common scalar B

Suppose B is a positive rational number, independently obtained, with:

1. `q=4B`;
2. for every prime p, `G[p^infinity]` is finite and `v_p(#G[p^infinity])<=v_p(B)`.

The left valuations are nonnegative, so every valuation of B is nonnegative. A positive rational with this property is a positive integer. The rigorous interval for q then forces B=9. For every p different from 3, the upper bound is zero, so the corresponding primary group is trivial. At 3 it has order at most 9; the retained 3-primary input gives equality. Since a torsion abelian group is the direct sum of its primary groups, G is finite of order nine. Finally q=36=4#G.

Finiteness of the primary groups in item 2 is explicit and indispensable: the cardinality valuation of an infinite group is not an integer. Alternatively, one can prove injections of the relevant primary groups into independently constructed finite groups with the same order bounds. No equality of local units is needed for this particular sufficient contract.

Bare existence of a numerical B with these properties is equivalent, under the retained inputs and interval, to FIN plus FORMULA: in the reverse direction `q=4#G` and the interval force `#G=9`, and B=9 works. The desired progress would be an independent construction and proof of the interfaces, not this existential equivalence.

## E6. Assembly and classification

\[
\begin{gathered}
\underbrace{\forall n\ge1:\ \#G[n]<441}_{\text{OPEN arithmetic input}}
\ \Longrightarrow\ G\text{ finite},\ \#G=9,\\
\underbrace{q\in\mathbb Q,\ \operatorname{den}(q)\le174}_{\text{OPEN arithmetic input}}
\ +\ \text{retained interval}\ \Longrightarrow\ q=36,\\
\#G=9\ \wedge\ q=36\ \Longrightarrow\ \mathrm{FIN}\wedge\mathrm{FORMULA}.
\end{gathered}
\]

E4 may replace the second antecedent; E5 may replace both branches. RANK is the retained input for full BSD. All implications inherit the exact hypotheses and provenance boundaries stated above.

**Progress classification:** an explicit sufficient endgame and corrected admission logic. No new arithmetic antecedent is proved, no prior arithmetic gap is closed, and no strict difficulty reduction is demonstrated. The kill condition for a candidate relying only on these displays is failure to supply an independent method for the marked open input.
