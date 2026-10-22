# The existing whole-order estimate cannot supply the required small class allowance

**Written deduction, not an independent human review.** All statements below concern the specific upper-bound expression in the October 20 SCALING.md, not the size of an actual class group. The seed's retained type-III inertia at 4547 and the earlier tame permutation calculation are inputs.

Put n=p²−1, d=n/4, m=n/2=2d, q=4547, Q=|D_A|/|D_K|=|D_K|δ. At a good coefficient prime p≥5 the earlier local calculation gives v_q(D_K)=d and v_q(δ)=d. Hence Q≥q^(2d). The relative-discriminant positivity gate has already been proved, so λ>0 in

    λ=(log δ−n log 2)/sqrt(p(p−1)).

The published-in-lab complete class-order expression is

    B_p=2^(1+(p−1)/4) Γ(d/2+1) sqrt(Q)
          * (e log(Q)/n)^(2d) / (π^(3d/2) λ^d).

## Lower bound on this expression

Because |D_K|≥1, δ≤Q, so λ≤log(Q)/sqrt(p(p−1)). For odd p, d/2=(p²−1)/8 is an integer k≥3. Integrating log(x) on [1,k] shows k!≥(k/e)^k. Insert these inequalities into B_p, then use sqrt(Q)≥q^d and log(Q)≥2d log(q). Exact algebra gives

    B_p ≥ 2^(1+(p−1)/4)
          [ q e^(3/2) log(q) / (8 π^(3/2))
            * sqrt(2p/(p+1)) ]^d.

Now e^(3/2)>2, π^(3/2)<8, sqrt(2p/(p+1))>1 and log(4547)>8. The last inequality follows, for example, from e<11/4 and (11/4)^8<4547. Therefore the bracket is strictly greater than q/4=1136.75>1000. Thus

    B_p > 1000^d > p^4                     for every good p≥5.

For the last comparison, d≥p for p≥5 and p≤2^(p−1), so p^4≤16^(p−1)<1000^p≤1000^d.

## Consequence and exact boundary

Substituting only floor(log_p B_p) for the class allowance can never force that allowance to be ≤3. This remains true even granting the maximal possible elimination of the unit term. Therefore this **particular** global class-order estimate, standing alone, cannot deliver the parity-relaxed source ceiling three at any good prime, nor eventually as p grows.

This does NOT say that the true class group has order at least p^4; the inequality is in the wrong direction for that. It does NOT disprove a small class kernel, a refined characterwise estimate, a substantially stronger regulator estimate, a different analytic estimate, or a joint global/local class-lift obstruction. It does not rule out FIN. It rules out trying to finish the current source bound solely by evaluating the previously uncomputed discriminants in expression (G).

The exact integer checker records the minimum floor values implied by 1000^d at selected primes. They describe a limitation of the bound expression, not arithmetic lower bounds on undiscovered classes.
