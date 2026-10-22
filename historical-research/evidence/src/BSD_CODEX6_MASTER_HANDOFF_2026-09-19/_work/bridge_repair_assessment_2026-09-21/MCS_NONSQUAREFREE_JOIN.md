# Nonsquarefree application by composing existing inputs

2026-09-21. **WRITTEN SOURCE COMPOSITION; NO NEW SHA BOUND.**

This closes a restricted applicability question raised by the returned source check. It does not prove a global BSD endpoint or a strict reduction in the difficulty of proving one. The literal squarefree hypothesis of Macias Castillo–Sano (MCS) Theorem 3.12 remains false for the seed; the statement below instead follows by assembling its proof with the more general cited main-conjecture input.

## Exact statement

Retain the project's qualifications on the fixed curve, residual-image theorem, local data, and source normalizations. Let
\[
E:y^2=x^3-22735x^2+106272484x,\qquad
N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843.
\]
Let \(p\) be a prime satisfying
\[
p\ge5,\quad p\nmid N,\quad p\notin\{19,59,487\},\quad
E\text{ ordinary at }p,\quad p\nmid\#\widetilde E(\mathbf F_p).
\tag{P}
\]
Choose an imaginary quadratic field \(K\) of odd fundamental discriminant \(D_K\ne-3\), coprime to \(Np\), in which every prime dividing \(Np\) splits. Put \(T=T_p(E)\), let \(K_\infty/K\) be the anticyclotomic \(\mathbf Z_p\)-extension, and use the Greenberg Selmer complex and the Heegner system in the cited sources.

Then the Heegner point main conjecture supplies an integral determinant basis over \(\Lambda=\mathbf Z_p[[\operatorname{Gal}(K_\infty/K)]]\). Specialization to \(K\) and the general MCS comparison give, for every \(n\ge1\), a basis \(\epsilon^{\rm Hg}_{n,0}\) of the rank-zero Stark-system module and
\[
\operatorname{Fitt}^{\,i}_{\mathbf Z/p^n}
 \bigl(\operatorname{Sel}_{p^n}(E/K)^*\bigr)
 =I_i(\epsilon^{\rm Hg}_{n,0})\qquad(i\ge0).
\tag{J}
\]
The star denotes the finite \(\mathbf Z/p^n\)-linear dual. This statement is only at the base layer \(m=0\); no all-layer extension beyond what is needed to construct and specialize the determinant basis is claimed.

## Proof and exact source interfaces

**1. Existing seed arithmetic supplies the ramification input.**
The [retained visibility calculation](../../audits/fixed_visibility_2026-09-19/FIXED_VISIBILITY_AUDIT.md), §3.1, gives residual ramification at \(3,2243,5843\) for every good \(p\ge5\): the multiplicative discriminant valuations are \(2,1,2\), all prime to \(p\). These are all the primes occurring exactly once in \(N\). Thus with \(N^-=1\), the ramification requirements in Burungale–Castella–Kim Hypothesis \(\spadesuit\) hold, including its nonsquarefree clause requiring at least two such split primes. The other BCK inputs are good ordinariness, the retained surjectivity over \(\mathbf Q\), and non-anomalousness, which follows from (P) since \(p\) splits in \(K\).

**2. The cited main-conjecture theorem already permits square factors.**
Apply BCK Theorem A. Its conductor need not be squarefree. The precise source read is the [author manuscript](https://web.math.ucsb.edu/~castella/PRconj.pdf), §1.2, Theorem A and Hypothesis \(\spadesuit\), with [local copy](mcs_sources/BCK_author_PRconj.pdf); the journal reference is Algebra & Number Theory 15 (2021), 1627–1653. The publisher PDF was not recovered in this operation, so textual claims are bound to the author copy. The proof of that theorem is imported, not independently re-audited.

**3. The determinant conversion introduces no squarefree requirement.**
Kataoka–Sano, [published §5.2 and Proposition 5.12](https://jamathr.org/index.php/jamr/article/download/Vol-2Issue-2Paper-1/Vol-2Issue-2Paper-1/38199), convert the Heegner main conjecture to the required determinant-basis statement. Their §5.2 assumes good ordinariness and unramifiedness at \(p\), with the Heegner splitting conditions inherited from §5; it does not impose squarefree conductor or analytic rank one. The rank-one assumptions in §5.1 are not assumptions of this proposition. Its proof uses the characteristic ideal and the Selmer complex's determinant, not non-torsion of the base Heegner point.

**4. Check the finite-level local conditions, without importing squarefreeness.**
First \(\bar\rho_{E,p}(G_K)=\mathrm{GL}_2(\mathbf F_p)\). Indeed a proper restriction to an index-two subgroup would make \(K\) the unique quadratic subfield of \(\mathbf Q(E[p])\): the index-two character of \(\mathrm{GL}_2(\mathbf F_p)\) factors through determinant. That quadratic field is ramified at \(p\), whereas \(K\) is not. In particular \(E(K)[p]=0\).

The [corrected Aristotle bad-place calculation](/Users/bsm/BSD_ARISTOTLE_INVENTION_PACKET_2026-09-20/review_2026-09-20/returned_archives/B_revision2/output-final_aristotle/ARISTOTLE_B_CORRECTIONS.md), §0, supplies \(E(\mathbf Q_\ell)[p]=0\) for each bad \(\ell\) under (P). Explicitly the orders of the finite reduction quotients, in the order \(2,3,2243,4547,5843\), are
\[
4,\quad8,\quad2242,\quad9094,\quad11688.
\]
Their relevant prime divisors are \(2,3,19,59,487,4547\); the formal groups are pro-\(\ell\), and \(p\ne\ell\). As these places split in \(K\), this proves the bad-place vanishing required in MCS Hypothesis 3.6(ii).

Every bad prime splits in \(K\), so the retained Tamagawa product gives
\[
\operatorname{Tam}(E/K)=16^2,
\]
and good reduction persists at the other places. Together with \(E(K)[p]=0\) and (P), this checks the sufficient criterion in MCS Remark 2.12 for Hypothesis 2.11 at \(T\).

**5. Complete the finite-level comparison.**
In the [MCS preprint](https://arxiv.org/html/2603.23978v1), apply the proof of Proposition 3.7 and the proof of Lemma 3.8 at \(m=0\). They use the just-checked local/global conditions, residual image, and non-anomalousness; they require no additional use of squarefreeness. In particular the core-vertex argument reduces to the cited general existence theorem with the local injectivity condition; at \(m=0\) the latter map is the identity. The core rank is zero by the self-dual finite Selmer sequence.

Now apply general Theorem 3.4 and Corollary 3.5 to the determinant basis from step 3. The specialization is the derived base-change map used in Definition 3.10, whose underlying cited base-change theorem does not require squarefree conductor. A generator of the determinant line remains a generator after tensoring to the base layer. This proves (J), for all \(n\), with the source's Heegner and modular-parametrization normalizations. It neither uses FIN nor assumes order nine.

Fields \(K\) with the imposed splitting conditions exist by choosing a negative odd fundamental discriminant in appropriate residue classes. They may depend on \(p\); no uniform choice of Heegner arithmetic across all \(p\) is obtained.

## What this closes and what it does not

**Closed input:** nonsquarefreeness alone does not prevent this determinant/Stark-system application in the regime (P). The existing ramification and local-vanishing work has supplied actual hypotheses of the more general source argument.

The regime is not empty: the retained count \(\#\widetilde E(\mathbf F_{11})=14\) gives \(a_{11}=-2\), so \(p=11\) satisfies (P). Its already-proved Sha vanishing is not used in this deduction.

**Endpoint:** a possible Sha-bound input. Equality (J) controls classical Selmer structure only when its arithmetic ideals are independently understood. No ideal \(I_i(\epsilon^{\rm Hg}_{n,0})\) is evaluated here, no numerical bound on the quotient by rational-point classes is obtained, and no new primary component is settled. The identification of these coordinates with WC witnesses is not asserted.

**Still missing:** an independently calculable arithmetic estimate with a proved implication for the excess Selmer classes. For a global conclusion the other prime regimes must also be addressed. The exceptional set in (P) is an applicability exclusion, not a support theorem for Sha. Anomalous and supersingular primes have not been shown to form a finite leftover set. The real regulator comparison is untouched.

**Research decision:** the squarefree-hypothesis investigation has an answer at this scope and should not become another cleanup campaign. A further coordinate project would need an explicit evaluation or bound that can be approached independently of the unknown Sha group; this note has not supplied that method. No successor computation or construction is launched.

**Grade:** written composition of source results with retained seed hypotheses, including a March 2026 preprint. Not Lean-verified, not a new theorem claimed in the literature, and not a strict difficulty reduction to full BSD. Local arithmetic and image qualifications are inherited rather than replayed. A subsequent external model check supports the conductor-use and residual-image arguments; it does not independently audit all source inputs.

**Subsequent review:** [the height and quotient deductions](MCS_DERIVED_HEIGHT_GATE.md) correct the proposed computation on the divided Heegner class and prove the conditional Fitting-ideal shift by three when a suitable rank-one twist is certified. They evaluate no Stark ideal and add no Sha bound.
