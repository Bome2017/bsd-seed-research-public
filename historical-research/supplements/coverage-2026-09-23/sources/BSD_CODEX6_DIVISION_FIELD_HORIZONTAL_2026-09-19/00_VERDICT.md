# CLASSGROUP_COMPONENT_IS_THE_HARD_WALL

For the fixed seed, put

\[
 C_p=\operatorname{Hom}_{\mathrm{GL}_2(\mathbf F_p)}
 \left(\mathrm{Cl}(\mathbf Q(E[p]))/p\mathrm{Cl}(\mathbf Q(E[p])),E[p]\right).
\]

The operation establishes, for every prime \(p\ge7\) outside
\(\{19,59,487,2243,4547,5843\}\),

\[
 \boxed{\Sha(E/\mathbf Q)[p]=0\iff\dim_{\mathbf F_p}C_p\le2.}
\]

It also proves \(\dim C_p\ge1\). Bare class-group-component vanishing is therefore the wrong target: the rank-two Mordell–Weil group forces an everywhere unramified contribution.

The sharper object removes those rational-point extensions. Define \(A_p=\mathrm{Cl}(K_p)/p\), take its maximal \(E[p]\)-isotypic semisimple quotient \(A_p^{(V)}\), let \(W_{0,p}\) be the rational-point Kummer classes locally divisible by \(p\) at \(p\), and set

\[
 X_p=\ker\bigl(A_p^{(V)}\to E[p]\otimes W_{0,p}^*\bigr).
\]

Then \(\operatorname{Hom}_{G_p}(X_p,E[p])=0\) is equivalent to \(\Sha[p]=0\), by an exact sequence with a cokernel of dimension at most one and unconditional parity. This is **Stage D classification B**, not a demonstrated reduction in difficulty.

The easier local contributions have been exhausted for the tail:

* Every away-from-\(p\) ray factor, including all five bad primes, is removed by the actual local Kummer conditions.
* At good \(p\), the exact local-condition conductor over \(K_p\) is two. Its natural-module ray source has dimension one, in both ordinary and supersingular cases.
* That direction is retained honestly; parity removes it from the Sha-vanishing test. No FIN hypothesis is used.
* The global restriction map is an isomorphism because both \(H^1(G_p,E[p])\) and \(H^2(G_p,E[p])\) vanish.

The first unresolved statement is the upper bound \(\dim C_p\le2\) for every sufficiently large prime. Neither the seed-specific representation argument nor the primary-source audit supplies an independent mechanism proving it. The strongest pointwise reduction is equivalent to the desired tail vanishing; no horizontal vanishing theorem is claimed.

The finite set above consists of exceptions to the simplified reduction, **not** the only remaining possible Sha primes. The proof covers every \(p>5843\), but proves no Sha-vanishing cutoff. Conductors at the three coefficient primes of bad reduction are left in the exact norm-subgroup formulation; the good-prime conductor-two assertion is not extended to them.

Read [the theorem and converse proof](DIVISION_FIELD_REDUCTION_THEOREM.md), [the local conductor and representation proof](LOCAL_CONDUCTOR_AND_MODULES.md), and [the primary-source audit](PRIMARY_SOURCE_AUDIT.md). This is a written mathematical derivation relative to the retained seed inputs, not a machine-checked or independently refereed theorem. The operation stops at the class-group upper bound.
