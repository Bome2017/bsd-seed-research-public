# W3 global-period attack — 2026-10-04

## Endpoint

Retain the new local identity
\[
b_p=v_{\varpi_p}(A_{g_p}),\qquad A_{g_p}=c_{g_p}\frac{L(g_p,2)}{\Omega_{g_p}},
\]
and the reviewed implication
\[
b_p\le3\Longrightarrow \Sha(E/\mathbf Q)[p^\infty]=0.
\]
The task is to determine the first nonzero residual coefficient of the **integral Hida modular-symbol specialization** giving \(A_{g_p}\), not to re-prove the local lattice.

## Construction to execute

For each retained good ordinary p, work in the ordinary localized integral modular-symbol module for the Hida branch through f. Fix its primitive integral generator \(\Phi_p\) by the same Kato/Hida lattice used in the W3 return. Let \(\kappa\) be the weight character and let \(\lambda_{3,p}\) be the arithmetic specialization giving weight 3 and nebentype \(\omega^{-1}\).

Construct the integral evaluation functional \(\mathcal E_2\) whose classical specialization is the algebraic critical value at s=2. Prove, with all period and Euler factors,
\[
\mathcal E_2(\lambda_{3,p}(\Phi_p))=u_p A_{g_p},\qquad u_p\in\mathcal O_p^\times.
\tag{1}
\]

The retained W3 result implies the left side lies in \(\varpi_p^2\). Define the **divided residual specialization** only after proving divisibility in the integral module:
\[
\mathfrak a_p:=\varpi_p^{-2}\mathcal E_2(\lambda_{3,p}(\Phi_p))\bmod\varpi_p.
\tag{2}
\]
Then
\[
\mathfrak a_p\ne0\Longrightarrow b_p=2\Longrightarrow\Sha[p^\infty]=0.
\tag{3}
\]
If the normalization permits one extra unavoidable factor, record the exact exponent; the acceptable endpoint is still \(b_p\le3\).

## Mandatory collision test

Before attempting nonvanishing, compare (2) with every retained residual degree-two object: the two-prime Kurihara scalar \(C_p\), singleton c2, definite theta c2, and the branch-theta augmentation coefficient.

A comparison counts only if proved in the same integral lattice.

- If \(\mathfrak a_p=u_p C_p\), or is equivalent to any retained witness whose nonvanishing is already equivalent to \(\Sha[p]=0\), return `W3_COLLAPSES_TO_EXISTING_WITNESS` and stop this branch.
- If it is distinct, exhibit the exact map separating it and continue.

## If distinct: seek a fixed/global ancestor

Do not attempt prime-by-prime evaluation. Search for an integral characteristic-zero or tame-level object \(\mathfrak A\) with
\[
\mathfrak a_p=\operatorname{red}_p(\mathfrak A)
\]
for all but finitely many p, or for a fixed finitely generated Z-module element whose p-reduction maps to \(\mathfrak a_p\). If such an ancestor is nonzero, only finitely many primes can kill it; this would give the desired cofinite ordinary bound.

The required proof must include:
1. the fixed module/object independent of p;
2. the specialization/reduction map;
3. integrality and denominator support;
4. proof that the fixed object is nonzero without BSD/Sha finiteness.

If no fixed ancestor exists because the omega^{-1} specialization intrinsically changes with p, prove that obstruction for this construction and stop it.

## Do not substitute

- nonvanishing of the complex L-value for p-adic unitness;
- mu=0 for a bound on the first divided coefficient;
- rational/canonical bases for integral lattice equality;
- a p-adic regulator unit conjecture;
- “almost all p” heuristics for a theorem.

## Required statuses

`W3_COFINITE_BOUND` — proves b_p<=3 cofinitely.

`W3_FIXED_ANCESTOR` — constructs a nonzero p-independent integral ancestor and proves the reduction formula, with only a finite denominator set left.

`W3_COLLAPSES_TO_EXISTING_WITNESS` — proves the divided specialization is the old open witness in another normalization.

`W3_NO_FIXED_ANCESTOR_FOR_THIS_CONSTRUCTION` — proves the p-dependence prevents the proposed fixed-object reduction.

`W3_NEW_REDUCTION` — a genuinely new proved map strictly closer to one of the above, with its single remaining step.

`NO_NEW_RESULT`.
