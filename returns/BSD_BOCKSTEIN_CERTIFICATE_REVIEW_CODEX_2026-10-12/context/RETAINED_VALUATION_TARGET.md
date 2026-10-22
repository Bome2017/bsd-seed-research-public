# The less restrictive arithmetic target

**Conditional on CONTENT_BOUND_PROOF.md and the retained matched Rubin comparison.** No coefficient is evaluated here.

Use distinct symbols to avoid confusing the cofactor valuation with a smoothing parameter. Set

\[
K_p=[U^2]\operatorname{Col}_\rho(z),\quad
\ell_p=(\log_\omega(P_1),\log_\omega(P_2))^t,
\]

\[
H_p(A_p,B_p)^t=\epsilon_{p,\rho}K_p\ell_p,
\quad r_p=v_p(\det H_p),\quad
c_p=\min_i v_p((\operatorname{adj}H_p\ell_p)_i).
\]

Assume H_p nonsingular and K_p nonzero. Then the actual content is

\[
m_p=v_p(K_p)+v_p(\epsilon_{p,\rho})+c_p-r_p.
\]

The coefficient and heights may be in an extension; valuations are normalized by v_p(p)=1. The total expression is an integer because it equals the content of the actual Z_p-coordinate pair. Exact source matching is essential.

The quantitative conclusion is

\[
\operatorname{length}\Sha[p^\infty]
\le v_p(K_p)+v_p(\epsilon_{p,\rho})+c_p-r_p-w_p.
\tag{V1}
\]

Thus the expression on the right being at most one suffices for primary vanishing. It is nonnegative under the hypotheses.

## Ordinary primes

Non-anomalous ordinary primes have v_p(epsilon)=-1. The new lower bound and sufficient upper bound together read

\[
\boxed{r_p-c_p+w_p+1\le v_p(K_p)\le r_p-c_p+w_p+2.}
\tag{V2}
\]

Only the upper bound in V2 is still required once nonzero K and the retained comparison are given; the lower bound follows from the quantitative theorem. The earlier primitive test demanded the single value r_p-c_p+1. The present test allows one extra factor above the threshold corrected by w_p.

Equivalently the desired cofinite estimate is

\[
v_p(K_p)+c_p-r_p-w_p\le2,
\]

with K_p nonzero and its source controlled. The fixed-source normalization theorem can replace v_p(K_p) by the matching standard quadratic coefficient outside its fixed support. It supplies no bound on the resulting correlated expression.

## Seed calibration at 17

The retained quantities are w17=0, c17=1, r17=1. Hence

\[
\operatorname{length}\Sha[17^\infty]\le v_{17}(K_{17})-1.
\]

Either valuation 1 or valuation 2 would force vanishing. Since K17 is integral and divisibility by 17 is forced, a matched certificate that K17 is nonzero modulo 17^3 is enough. In particular, if K17/17 is zero mod17 but K17/17² is nonzero mod17, the derivative is nonprimitive and the stronger theorem still applies.

This is an interpretation of a possible arithmetic value, not a computed value or an instruction to launch a prime-specific campaign. Also 17 is not automatically outside the unspecified source-lattice exception set.

## Supersingular and singular-height scope

For a matched supersingular root the retained Rubin prefactor has valuation zero. Formula V1 applies with that value and the root-specific height convention. The preceding ordinary bounded-measure normalization is not substituted for it.

The cohomological content theorem itself needs no nonsingular height matrix. If H is singular, do not use V1 by dividing by its determinant. A direct arithmetic bound m_p<=w_p+1 is still sufficient, or a correctly matched row equation may bound m_p without inverting H.

## What must actually change the endpoint next

An arithmetic estimate proving m_p-w_p<=1 on a cofinite domain would give cofinite primary vanishing. A fixed-integer support argument or a genuine correlated coefficient estimate could supply it. The present proof supplies neither. Normalizing away actual p-content, requiring independent regulator unitness, or only repeating the matrix identity would not establish this estimate.

No claim of a converse is made: arbitrary extra smoothing can increase m_p while leaving Sha unchanged. The actual specified class must be kept throughout the estimate.
