# Across-prime test of this particular primary-packing budget

This is a limit on the explicit upper-bound expression, not a lower bound on actual p-class groups and not a theorem that primary class control is impossible.

For the same full-image seed point-field construction at a good prime p>=5, put n=p^2-1, m=n/2, d=n/4. Retain the discriminant and positivity inputs of the October21 analytic-obstruction proof. In particular q=4547 gives

    D_K >= q^d, delta >= q^d,
    lambda = (log(delta)-n log2)/sqrt(p(p-1)) >0.

The relative unit dimension is d. The same norm-one ideal-group construction gives volume at most

    2^((p+3)/4) * C_an,

where C_an is the chosen Louboutin upper bound for h_relative times R_A/R_K. With the retained self-injectivity test R<=lambda/2, the primary-packing expression is

    B_pack = 2^((p+3)/4) C_an / (M vol(B_d) R^d)
           >= 2 B_old/M,

where B_old is exactly the whole-order expression from the earlier SCALING.md. This comparison concerns the computed bounds, not actual torsion orders.

Even granting every possible base prime, M<=mX for pairs of norm<=X. Grant the wider original-EV range X<=delta^(1/(2p)), rather than only the author-LOW range delta^(1/(4p)). The calculation in the supplied October21 ANALYTIC_OBSTRUCTION_PROOF.md, before its final substitution sqrt(Q)>=q^d, gives

    B_old > 2^(1+(p-1)/4) sqrt(D_K delta) / 4^d.

Therefore

    B_old/X > (q^(1-1/(2p))/4)^d > 400^d.

The final inequality holds for p>=5 because q^(1-1/(2p))>=4547^(9/10)>1600; the last comparison is an exact integer-power inequality. Consequently

    B_pack > 2*400^d/m > p^4.

For the last step use d>=p, m<p^2, p<=2^(p-1), and 400^p>64^(p-1)>=p^6.

Thus this explicit packing budget, using the earlier analytic product and lambda-based self-injectivity certificate, cannot produce a class allowance at most three anywhere on the stated domain, even if all admitted primes split. Merely extending the prime count within those norm ranges cannot repair it. The actual p=5 prefix experiment is consistent with this symbolic limitation and is substantially worse than its optimistic prime-supply estimate.

This does not exclude sharper actual regulator/minimum estimates, different nonuniform packing geometry, source-specific p-adic annihilators, or class maps with independently controlled kernels. It does say that the tested replacement of whole-order bounds by small-prime p-image packing has not supplied the smallness requested for FIN.
