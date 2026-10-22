# A3: minus signed control and a first-layer arithmetic bound

Working proof, 2026-09-22. This record does not supersede the frozen master. No primary component is asserted to vanish here. The new statements below are deductions from the cited BLV theorems and retained seed inputs, not claims of literature novelty or Lean verification.

**Subsequent derivation:** SIGNED_MINIMAL_LAMBDA_BRIDGE.md strengthens this calculation using exact specialization lengths and the equivariant residual presentation. Its written argument proves the quadratic forward implication and M_1=0 modulo p. Accordingly the linear-witness possibility in section 4 is excluded for this seed by that later argument, and the missing implications in section 5 describe this preliminary calculation alone. The combined proof remains subject to independent review; nonvanishing of the quadratic moment remains open.

## Inputs and exact scope

Let E be the fixed seed, K=Q(sqrt(-7)), and p>=5 with p not dividing 7N and a_p(E)=0. Retain the seed verification of BLV Hypothesis 1.1: N-minus=3*2243*5843 is squarefree; N-plus=2^3*4547^2; the residual representation is surjective and satisfies the specified bad-place conditions. The ordinary non-anomalous condition in Hypothesis 1.1(5) is not imposed at a supersingular prime. The class number of K is one.

Retain rank E(Q)=2, rank E^(-7)(Q)=0 and finiteness of Sha(E^(-7)/Q), at their existing project grades. In particular rank E(K)=2 and E(K)[p]=0. Neither FIN for E nor the desired leading-term formula is assumed.

Primary source: Bertolini--Longo--Venerucci, arXiv:2306.17784v2 (2026-02-05), sections 4.3, 5.1--5.6 and Theorem 7.1. Local source:

`/Users/bsm/run013-bsd-scout-2026-08-22/_evidence/txt/2306.17784.txt`

Online: <https://arxiv.org/html/2306.17784v2>.

## 1. Classical comparison at augmentation

Write S^- for BLV's discrete minus signed Selmer group over the anticyclotomic tower, and T=gamma-1. Then

\[
 S^-[T]\simeq\operatorname{Sel}_{p^\infty}(E/K),\qquad
 S^-[p^k,T]\simeq\operatorname{Sel}_{p^k}(E/K).
\tag{1}
\]

Here the finite-level isomorphism uses the usual identification with the p^k-torsion of the infinite Selmer group, valid since E(K)[p]=0.

Proof of the local point that ordinary arguments do not supply: BLV section 5.1 gives E(m_0)^-=E(m_0) for both split and inert p, and Proposition 5.3 gives exact restriction control at omega_0^-=T. The groups of points on the reductions have orders p+1 (split) and (p+1)^2 (inert), so the formal and full local groups have the same p-primary Kummer image. Corollary 5.5 gives the corresponding exact finite-level conditions. At N-plus the local cohomology vanishes by Lemma 5.8. At N-minus the retained ramification/Tate-curve calculation identifies BLV's ordinary local condition with the Kummer condition (the valuations of the minimal discriminant are 2,1,2, prime to p). Away from Np both are the finite local condition. Proposition 5.9, with the regular sequences (T) and (p^k,T), now gives (1). BLV's own proof of Theorem 7.1, Step 4, explicitly checks the residual signed/classical identification in every non-exceptional case.

The minus case is non-exceptional whether p splits or is inert. This argument never substitutes an ordinary unit root at a supersingular prime.

## 2. The minus first layer has the raw normalization

Let psi be BLV's primitive integral quaternionic eigenfunctional. Let P_1 be BLV's traced Gross point at conductor p^2, and set

\[
 \Theta_1=\sum_{j=0}^{p-1}\psi(\gamma^jP_1)\gamma^j,
 \qquad F^-(T)=\mathcal L_f^-(T)=\sum_{i\geq0}b_iT^i.
\]

The factorization in BLV section 4.3 at n=1 has sign +1 and tilde-omega_1^+=1. Consequently

\[
 F^-\pmod{(1+T)^p-1}=\Theta_1.
\tag{2}
\]

In particular, for every 0<=i<p,

\[
 \bar b_i=\sum_{j=0}^{p-1}\binom ji v_j,
 \qquad v_j=\overline{\psi(\gamma^jP_1)}.
\tag{3}
\]

This is a statement about reductions of coefficients: the finite layer does not determine their Z_p lifts. Its sign differs from the previously studied ordinary stabilized formula.

One can prove b_0=0 without importing an ordinary lower-order theorem. If b_0 were nonzero with valuation h, choose k>h. Theorem 7.1 for f modulo p^k, the minus sign, and the trivial character would bound the length of the classical p^k Selmer group by 2h. Its Mordell--Weil subgroup has length 2k, a contradiction. Thus

\[
 b_0=0,\qquad M_0=\sum_jv_j=0.
\tag{4}
\]

This does NOT yet prove b_1=0. Exact evenness of the raw Gross-point packet is not assumed.

## 3. A coefficient-to-classical-Selmer bound

**Proposition.** Suppose that, for an integer 1<=d<=p-2,

\[
 \bar b_0=\cdots=\bar b_{d-1}=0,\qquad \bar b_d\ne0.
\]

Then

\[
 \dim_{\mathbf F_p}\operatorname{Sel}_p(E/K)\leq2d,
\tag{5}
\]

and hence

\[
 \dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
 +\dim_{\mathbf F_p}\Sha(E^{-7}/\mathbf Q)[p]
 \leq2d-2.
\tag{6}
\]

**Proof.** Choose a character chi of exact order p, O=Z_p[zeta_p], and pi=zeta_p-1, normalized by v_pi(pi)=1. Then v_pi(p)=p-1. In F^-(zeta_p^{-1}-1), the degree d term has valuation d; every lower term has valuation at least p-1>d and every higher term has valuation greater than d. Therefore

\[
 v_\pi(F^-(\bar\chi))=d.
\]

Apply BLV Theorem 7.1 with L=1, g=f mod p^k and k large enough to retain this nonzero value. It gives

\[
 \operatorname{length}_{O}\operatorname{Sel}^-(K,A_g(\chi))\leq2d.
\]

The pi-torsion of this group is the residual minus Selmer group. More precisely, Proposition 5.9 applied to the character ideal P_chi and then to (P_chi,pi) identifies it with the specialization at (T,pi), since chi is trivial modulo pi. This is the classical Sel_p(E/K) by (1). Its dimension cannot exceed the length of the finite O-module, giving (5). The Kummer exact sequence subtracts the two independent Mordell--Weil directions. Restriction/corestriction for K/Q, with 2 invertible, splits the remaining p-torsion into the seed and quadratic-twist eigenspaces. This gives (6). No finiteness of the seed's Sha is used. QED.

Only the upper-bound direction of BLV Theorem 7.1 is needed for this proposition. Neither a characteristic-ideal-to-Fitting-ideal substitution nor the dismissal of finite Lambda-module errors is used.

## 4. Exact endpoint consequences and limits

Set M_i=sum_j j^i v_j. Equations (3)--(4) give

\[
 \bar b_1=M_1,\qquad \bar b_2=(M_2-M_1)/2.
\]

Therefore the following is a proved conditional implication, with an unevaluated arithmetic antecedent:

\[
 M_1\ne0\Longrightarrow
 \Sha(E/\mathbf Q)[p^\infty]=0
 \quad\hbox{and}\quad
 \Sha(E^{-7}/\mathbf Q)[p^\infty]=0.
\tag{7}
\]

Indeed (6) with d=1 makes both p-torsion groups zero, which makes their p-primary groups zero. We have NOT established M_1!=0 for any prime, or that the seed's functional equation permits it. It must not be advertised as an available computation before that compatibility is proved.

If instead M_1=0 and M_2!=0, then d=2 and the proved conclusion is only

\[
 \dim\Sha(E/\mathbf Q)[p]+\dim\Sha(E^{-7}/\mathbf Q)[p]\leq2.
\tag{8}
\]

In particular, the ordinary implication 'quadratic coefficient unit implies seed Sha_p=0' has NOT been proved for the signed construction by this argument. If the finite twist p-primary group is nonzero, its alternating Cassels--Tate pairing makes its p-torsion dimension at least two, and (8) would then imply seed vanishing. No twist support computation is authorized or proposed here.

Generator and basepoint checks: replacing gamma by gamma^a scales M_1 by a^(-1). If M_1=0, it scales M_2 by a^(-2). Translating P_1 changes M_1 by a multiple of M_0 and M_2 by a combination of M_0 and M_1. These observations preserve the relevant nonvanishing tests, but do not imply pure parity of the full packet.

## 5. Current proof boundary

Established: exact minus-to-classical augmentation control, the signed first-layer normalization, exact constant-term vanishing, and (5)--(8). These close source/normalization and conditional-bound arrows for the supersingular part of the project.

Not established: a value of either signed moment; a supersingular counterpart of the ordinary derived-regulator/exponent inequality; vanishing at any previously unsettled prime; a uniform tail; FIN; ORDER9; Q36.

The next calculation within A3 is to determine whether the ordinary exponent inequality can be obtained from the integral, complex-conjugation-equivariant finite presentations already supplied by BLV, without applying an ordinary derived-height theorem at a supersingular prime. A separate algebraic lemma must be proved before any such application is claimed.
