# The mathematical record for the fixed BSD seed

Reconciled in place on 2026-09-19; updated with the R1/R2 repair, its separate hostile model review, the bounded fixed-visibility test, the completed Euler-normalization cleanup, the certified 7- and 11-primary theorems, and the certified 13-primary theorem of 2026-09-21. **This is the single current mathematical account in this handoff.** The other reports are supporting proofs or historical records; their dates and titles do not independently determine the current status of a claim. The supersession table below states which assertions were replaced and why.

This is a source-bound consolidation, not a new proof audit of every imported theorem. “Retained” means that the stated result and its qualifications are imported from the linked record. Written proofs, computer-assisted certificates, conditional formalizations, and unproved assertions remain distinct. Historical recovery is incomplete; the precise coverage and omissions are stated at the end.

## 1. The curve, normalization, and exact endpoint

Throughout,

\[
E:\ y^2=x^3-22735x^2+106272484x,
\quad N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843.
\]

The retained Mordell–Weil theorem is

\[
E(\mathbf Q)=\langle T\rangle\oplus\mathbf ZP_1\oplus\mathbf ZP_2,
\quad T=(0,0),\quad
P_1=(4547,327384),\quad P_2=(5184,281520),\quad |T|=2.
\]

The points form a basis modulo torsion, not merely a subgroup of finite index. Write

\[
G=\Sha(E/\mathbf Q),\qquad
R=\det\bigl(\langle P_i,P_j\rangle_{\mathrm{NT}}\bigr),\qquad
q=\frac{L''(E,1)}{2\Omega_E R},
\]

where the period convention is \(\Omega_E=2\omega_1\), the retained full real period. The Tamagawa product is 16 and the torsion order is 2. Thus

\[
\begin{aligned}
\mathrm{RANK}&:\ \operatorname{rank}E(\mathbf Q)=\operatorname{ord}_{s=1}L(E,s)=2,\\
\mathrm{FIN}&:\ G\text{ is finite},\\
\mathrm{FORMULA}&:\ q=4\#G.
\end{aligned}
\]

**RANK is retained as proved with computer assistance. FIN and FORMULA are open.** FORMULA uses the actual finite order, not an analytic or predicted order.

Relative to the retained RANK theorem and the rigorous interval in §2,

\[
\boxed{\mathrm{full\ BSD}(E)\ \Longleftrightarrow\ (G\text{ finite of order }9)\ \land\ (q=36).}
\]

The reverse implication is substitution. In the forward direction, \(\#G=q/4\) is an integer in \((8.9985675,9.0014325)\), hence is 9. This equivalence is an exact description of the endpoint; it supplies no method for proving either open assertion.

## 2. Retained mathematical inputs and their qualifications

| Claim | Retained evidence and exact qualification |
|---|---|
| The displayed Mordell–Weil group and basis; \(G[2^\infty]=0\) | Zywina's preprint theorem and the recorded exact descent/saturation replay. The theorem's preprint status is retained. |
| \(L(E,1)=L'(E,1)=0\) | The positive algebraic rank rules out analytic rank zero by the retained rank-zero theorem; root number \(+1\) then gives the second vanishing. |
| \(L''(E,1)/2\in[35.929604,35.941023]\) | Rigorous Arb enclosure using independently checked coefficients. Its positivity proves analytic rank exactly two. |
| \(R\in(17.79651747249034020748,17.79651747249034039153)\) | Directed-rounding regulator certificate, with the normalizations of §1. |
| \(\Omega_E R\in(0.99820315980984172437,0.99820315980984173470)\) | The same certificate and its period calculation. |
| \(q\in(35.99427,36.00573)\) | Rigorous consequence of those enclosures. The much tighter floating-point estimate \(q\approx36\) is evidence only. |
| \(\bar\rho_{E,p}(G_{\mathbf Q})=\mathrm{GL}_2(\mathbf F_p)\) for every odd \(p\) | Retained residual-image theorem. For \(p\ge5\), the lifting argument with cyclotomic determinant gives full \(p\)-adic image. |
| The optimal Manin constant satisfies \(c_0=2^a\), \(a\le8\); the seed parametrization has \(c_E\mid2^9\) | Derived geometry/lattice argument with an audited formal algebra component; Edixhoven input is carried through published restatements. The stronger bound \(a\le4\) is not an established input. |
| \(G[3^\infty]\simeq(\mathbf Z/3)^2\), via published Skinner Theorem A | The 3-primary theorem is retained with the existing arithmetic, Jones deduction, and other source qualifications. R1 and the integral period-comparison subclaim passed model review. The failed internal μ transfer is not repaired; the bounded source cleanup stops with the SU Euler-removal interface unreconstructed. This does not reopen the 3-primary arithmetic. |
| \(G[5^\infty]=0\) | Sealed rigorous successor certificate. The formerly floating-point coefficient node is superseded by the Arb certificate. The Manin and preprint qualifications above still travel with the chain. |
| \(G[7^\infty]=0\) | [New computer-assisted theorem](audits/P7_PRIMARY_THEOREM.md). Certified depth-two leading coefficient is 1 modulo7 in the omega1 convention, or 4 in the full-period convention. Kato divisibility and canonical-height integrality prove finiteness and vanishing without main-conjecture equality. Retained rank/image/Manin qualifications remain; no independent human review or second end-to-end numerical run. |
| \(G[11^\infty]=0\) | [New computer-assisted theorem](audits/P11_PRIMARY_THEOREM.md). Certified depth-two leading coefficient is 8 modulo11 in the omega1 convention, or 4 in the full-period convention. Kato divisibility and canonical-height integrality give finiteness and vanishing without main-conjecture equality. The retained rank/image/Manin and computational trust qualifications remain; no independent human review or second end-to-end implementation. |
| \(G[13^\infty]=0\) | [Completed computer-assisted theorem](audits/P13_PRIMARY_THEOREM.md). Certified depth-two leading coefficient is **2 modulo13** in the omega1 convention, or **1** in the full-period convention. The returned 7/8 values omitted lattice normalization, with an additional missing unit-root factor in the alternative weights; both are corrected exactly. Kato divisibility and canonical-height integrality give finiteness and vanishing. All coefficient bindings, saved Arb units, exact downstream checks and final recombination pass. The pre-incident reused contents match their sealed hashes; the actual write-through incident remains recorded. Retained source/software qualifications remain; no fresh full integer-verifier replay, independent end-to-end implementation or Lean proof. |

**R1 passes as a source and conditional deduction; the full internal R2 repair remains incomplete, and its cleanup is stopped.** One separate, fresh-context model review checked the actual sources. It confirms the nonsplit Jones formula and the finite-before-leading-term ordering, conditional on the required integral characteristic-ideal equality. It also accepts the written seed-specific integral argument through

\[
X_{2243,\mathfrak m}\simeq\mathbb T_{\mathfrak m},
\qquad v_3\!\left(\eta_f(N)/\xi_f(N/2243,2243)\right)=0,
\]

and the claimed canonical/Gross-period unit comparison. Wiles's actual Jacobian theorem, the toric character module, Hecke variance, stabilizers, and the \(\Gamma_1/\Gamma_0\) index were checked. This does not yet establish the μ transfer needed at the end of the repair.

The failure is the assertion in **§3.6 of the original repair that the removed Euler factors have μ zero**. In its chosen quadratic field, \(q=2243\) is inert and \(a_q=1\). With the audited primitive CH interpolation and SU's removal of all places over primes in \(\Sigma\), the constant factor is

\[
1-q^{-2},\qquad
v_3(1-q^{-2})=v_3(2242\cdot2244)=1.
\]

The inert principal ideal has trivial anticyclotomic character, so this factor does not acquire a varying group-ring coefficient that could make its μ invariant zero. SU's stated setup includes \(q\) in \(\Sigma\), and Proposition 12.3.6's cited argument needs a unit specialized coefficient. The period-unit comparison does not erase this extra factor. A different normalization, cancellation, or replacement argument has not been justified here.

Accordingly the review grades the **complete R2 closure FATAL as written at that exact step**, while retaining the passed integral subclaims. This is a failure of the project's proposed transfer, not a refutation of Skinner's published main-conjecture theorem. The implication from the required integral equality through finiteness, Jones, and the arithmetic certificate to \(G[3^\infty]\simeq(\mathbf Z/3)^2\) remains valid. It is retained by importing Skinner Theorem A as published; it must not be presented as an independently completed audit of that theorem’s internal proof. Both Iwasawa divisibilities in the retained chain come from Skinner; the cited Kato theorem is not an independent bound at \(3\mid N\).

**Bounded source-normalization verdict:** “3-primary theorem retained via Skinner Theorem A as published; internal provenance open at the Euler-removal interface.” The published proof reaches the multiplicative case through higher-weight good-ordinary Hida specializations, Fitting-ideal congruences, and completeness (§3.1). Lemma 2.3.4(i) and (2-4-2) put the same nonzero Euler product on the Selmer and analytic ideals, so it cancels without being a unit. This is cancellation after integral equality, not a proof of the rejected μ-preservation statement. The good-ordinary input still imports SU; no cancellation inside its Proposition 12.3.6 was independently reconstructed. The local SU body is an author copy, not a verified journal-version PDF. Read the [bounded reconciliation](audits/euler_normalization_2026-09-19/EULER_RECONCILIATION.md) for the exact source limits. **Stop R2 cleanup; no new 3-primary arithmetic gap is asserted.**

The [original proof addendum](audits/p3_r1_r2_2026-09-19/R1_R2_THEOREM.md) is preserved unchanged as the reviewed artifact. Its overall closure claim and §3.6 are superseded by this qualification and the [hostile review](audits/p3_r1_r2_review_2026-09-19/REVIEW.md). This is model review, not independent human referee acceptance or formal verification. The original sealed arithmetic, the retained basis/preprint qualification, and other imported dependencies remain unchanged. No global FIN, order-nine, or scalar assertion is added.

The exact coefficient checks are

\[
a_{4,2}=15480\equiv9\pmod{27},\quad v_3(a_{4,2})=2;
\qquad a_{2,2}\equiv2\pmod5
\]

in the \(\omega_1\) convention. The certified 7-primary coefficient is \(a_{2,2}\equiv-1931\equiv1\pmod7\). In the Néron/full-period convention the 5-primary residue is 1 and the 7-primary residue is 4. This unit factor is a normalization change, not contradictory arithmetic. The new 11-primary coefficient is \(C_{11}\equiv-190\equiv8\pmod{11}\) in the omega1 convention, or 4 in the full-period convention. Raw-model \(p\)-adic regulator digits cannot be transferred unchanged across an isomorphism; the recorded valuation is the invariant input.

The bad-reduction data are:

| Prime | Type | Tamagawa number | Multiplicative sign when applicable |
|---|---|---|---|
| 2 | \(I_1^*\) | 2 | — |
| 3 | \(I_2\) | 2 | nonsplit |
| 2243 | \(I_1\) | 1 | split |
| 4547 | III | 2 | — |
| 5843 | \(I_2\) | 2 | nonsplit |

At 4547 the curve is potentially supersingular, with inertia of order four. At every good \(p\ge7\), rational 2-torsion and Hasse's bound give \(p\nmid\#E(\mathbf F_p)\): the only possible positive multiple of \(p\) in that range would be \(p\), which is odd. No conclusion about \(G[p]\) follows from this local fact alone.

Evidence: [retained seed theorem record](SEED_PROVED_STATE.md), [analytic-rank certificate](/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/ANALYTIC_RANK_CERTIFICATE.md), [regulator certificate](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/REGULATOR_CERTIFICATE.md), [original 3-primary theorem](/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/SHA3_THEOREM.md), [historical R2 source audit](/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/addenda/P3_R2_PERIOD_PROVENANCE_AUDIT.md), [R1/R2 repair](audits/p3_r1_r2_2026-09-19/R1_R2_THEOREM.md), [5-primary successor theorem](/Users/bsm/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/SHA5_RIGOROUS_THEOREM.md).

## 3. The exact remaining arithmetic, with quantifiers

For every \(n\ge1\), the Kummer sequence gives

\[
0\longrightarrow E(\mathbf Q)/nE(\mathbf Q)
\xrightarrow{\delta_n}\operatorname{Sel}_n(E)
\longrightarrow G[n]\longrightarrow0.
\tag{K}
\]

For odd \(p\), the first term has dimension two over \(\mathbf F_p\). The target is the **quotient by these two known directions**, not the construction or saturation of the directions themselves.

Because \(G\) is a torsion abelian group,

\[
\mathrm{FIN}\iff
\bigl(\forall p,\ G[p^\infty]\text{ finite}\bigr)
\land
\bigl(G[p]=0\text{ for all but finitely many }p\bigr).
\tag{F}
\]

Vanishing of \(G[p]\) implies vanishing of the full \(p\)-primary group: a nonzero element of order \(p^k\) yields a nonzero element of order \(p\). In contrast, finite prime support with nonzero \(p\)-torsion does not control higher depths or divisible parts.

Under FIN and the retained small-primary inputs, including the published-theorem dependency and internal provenance qualification in §2, the Cassels–Tate square-order consequence gives only

\[
\#G=9t^2,\qquad t\in\mathbf Z_{>0},\quad(t,30030)=1.
\tag{S}
\]

With the retained primary inputs through13, the next possible order is 2601. Thus \(G\) finite with \(\#G<2601\) forces order nine. Equivalently, the stronger-looking uniform assertion

\[
\forall n\ge1:\ \#G[n]<2601
\tag{U}
\]

already implies finiteness: the increasing sequence \(G[m!]\) exhausts \(G\), and its integer cardinalities are bounded by 2600, so it stabilizes. Combining with (S) gives order nine. The arithmetic bound (U) remains open. Order nine implies (U), so this is an endgame, not an established difficulty reduction.

The threshold is sharp under these abstract inputs: \((\mathbf Z/3)^2\oplus(\mathbf Z/17)^2\) has order 2601 and an alternating perfect pairing. The infinite group \((\mathbf Z/3)^2\oplus(\mathbf Q_{17}/\mathbf Z_{17})^2\) shows why a uniform bound on \(G[p]\) for primes alone is insufficient. The earlier thresholds 441, 1089 and 1521 remain valid under their earlier, weaker inputs; their witnesses involving settled primes are no longer compatible with the current record.

The prime-by-prime status remains:

| Regime | What is established | What is not established |
|---|---|---|
| 2, 3, 5, 7, 11, 13 | §2, with all qualifications; the 7-, 11- and 13-primary components vanish by certified computations | No implication to any other primary component |
| Good ordinary \(p\ge17\) | Applicable fixed-prime criteria and ordinary equivalence in §5.2 | No eventual vanishing theorem or proved uniform witness bound |
| Good supersingular \(p\) | The depth-two coefficient criterion below | No successful new seed coefficients here; no theorem covering this entire infinite regime |
| 2243, 5843 | Recorded semistable fixed-prime route | No completed certificates; split case also needs its stated nonzero \(\mathcal L\)-invariant input |
| 4547 | A recorded witness semi-decision | No witness or applicable replacement for the missing additive-prime control theorem |

The retained supersingular criterion says, under its non-CM, full-image and rank hypotheses, that

\[
\theta_1\bmod p=c_rX^r+O(X^{r+1}),\quad c_r\ne0
\quad\Longrightarrow\quad G[p^\infty]=0.
\]

For this seed \(r=2\). It is a sufficient test at each prime; a failed test proves no opposite conclusion. The coefficient is defined from depth-two symbols. The audited estimates of about 270/460 CPU-hours at 23/29 are retained cost estimates, not computations performed here. There are infinitely many supersingular primes, so an ordinary-only theorem leaves another infinite regime. Evidence: [Criterion SS audit](/Users/bsm/BSD_SEED_2243_12_CRITERION_SS_HOSTILE_GATE_2026-09-19/CRITERION_SS_HOSTILE_GATE.md) and [the coverage/source audit](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/SOURCE_AUDIT_AND_CORRECTIONS.md).

## 4. The exact analytic endgames

Put \(\varepsilon=573/100000\). The retained enclosure is \(|q-36|<\varepsilon\).

**Bounded rationality.** If \(q=a/b\) in lowest terms and \(1\le b\le174\), then either \(q=36\) or
\(|q-36|\ge1/b\ge1/174>\varepsilon\). Hence the former holds. Denominator 175 already fails as a uniform threshold: \(36+1/175\) is inside the interval. Rationality alone does not suffice.

**Bounded algebraicity.** If \(f(X)=a\prod_j(X-q_j)\in\mathbf Z[X]\) is the primitive irreducible polynomial with \(q_1=q\), then

\[
\varepsilon |a|\prod_{j>1}|36-q_j|<1
\quad\Longrightarrow\quad f(36)=0\quad\Longrightarrow\quad q=36.
\]

A convenient special case is: \(q\) is a totally positive algebraic integer of degree at most two, with trace at most 246 in the quadratic case. Then
\(\varepsilon(174+\varepsilon)<1\). Trace 247 admits a counterexample via the smaller root of \(X^2-247X+7595\).

Neither quantitative arithmeticity hypothesis has been proved for this \(q\). Each is equivalent to \(q=36\) within the retained interval; a new proof method would have to justify calling it easier.

**A common scalar.** Suppose an independently constructed \(B\in\mathbf Q_{>0}\) satisfies

\[
q=4B,\qquad
\forall p:\ G[p^\infty]\text{ finite and }
v_p(\#G[p^\infty])\le v_p(B).
\tag{B}
\]

All valuations of \(B\) are nonnegative, so \(B\) is an integer; the interval forces \(B=9\). The bounds kill every other primary component, and the qualified 3-primary input in §2 gives \(\#G=9\). This would establish both endpoints, with the other retained source qualifications. No such arithmetic construction and comparison has been proved. Defining \(B=q/4\) assumes the missing arithmeticity; defining \(B=\#G\) assumes the missing finiteness and comparison. Bare existence in (B) is an endpoint reformulation.

These implications and counterexamples are proved in the [exact endgames](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/EXACT_ENDGAMES.md) and [quantitative algebraicity report](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/QUANTITATIVE_ALGEBRAICITY_THEOREM.md). **Even a proof of \(q=36\) leaves order nine to prove. FIN alone does not supply it.**

**Current FORMULA frontier and admission result.** The authorized target is exactly \(q=36\). The first open arrow is an independently proved arithmetic expression for M1's weighted period together with its comparison to \(\Omega_E R\), without FIN or BSD. Initial consideration of an extension of M4 to more elliptic-path constructions supplied no independent height comparison or demonstrated difficulty reduction. That proposed extension was stopped before theorem development; no new obstruction theorem or arithmetic progress is claimed. No positive construction has yet passed admission. The later explicitly authorized automorphic-second-jet experiment produced the exact analytic decomposition recorded in §5.7, with a remaining Fourier period. It does not prove the weighted-period-to-height comparison. The midpoint and the Fricke-symmetrized endpoint residuals were subsequently certified nonzero in §5.7, excluding both single-vertex choices as exact integrated realizations. The target remains open, and no successor branch is active. Even success at \(q=36\) would leave the order-nine obligation.

## 5. Mechanisms, exact arrows, and accumulated obstructions

### 5.1 Integral sources and prime support

A finitely generated integral source does not bound the prime content of a family of images. The maps \(\mathbf Z\to\mathbf Z_p\), \(1\mapsto p^2\), are nonzero for every prime and have nonunit images at every prime. Likewise the two-term complex with diagonal differential \((p^2)_p\) over \(\prod_p\mathbf Z_p\) is perfect over that ring and has finite nonzero defects at infinitely many primes. It is not a rationally acyclic finite integral complex over \(\mathbf Z\).

Thus source integrality, profinite perfectness, pointwise nonvanishing, and pointwise finite primary groups do not imply finite support. A fixed nonzero integer satisfying \(G[p]\ne0\Rightarrow p\mid C\) would prove finite support, but full finiteness at its remaining primes would still be needed. Finitely many tame augmentation quotients see only primes dividing their finite group orders. An inverse limit requires an additional proved comparison.

Evidence: [witness-content theorem and countermodels](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md), [algebraic reduction lemmas](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md).

### 5.2 LINE, witness content, and ordinary equivalence

LINE postulates one rational scalar \(a/b\) relating the tame leading terms \(\delta_n\) and regulator terms \(\rho_n\) at all required auxiliary pairs and primes:
\(b\delta_n=a\rho_n\). The conditional theorem gives finite primary groups at the covered good primes, and vanishing away from the numerator support. The cross-prime scalar is unconstructed. The determinant-line version that required finiteness to define its comparison is not an unconditional equivalent formulation. Neither tame statement supplies an identity involving \(L''(E,1)\).

Witness content weakens this to a nonzero integer \(A\in J_E\). Its conditional implication is valid, and the finite algebra has been formalized. Its arithmetic antecedent is unproved. More sharply, for every retained good ordinary \(p\notin\{2,3,5,2243,4547,5843\}\),

\[
h_p=0\quad\Longleftrightarrow\quad G[p^\infty]=0.
\tag{O1}
\]

This is a written deduction with checked seed hypotheses, not the earlier conjectural “possibly equivalent” status. Uniform primitive witnesses on that ordinary tail are exactly uniform vanishing there. O1 does **not** prove a positive-depth converse, a supersingular converse, or \(J_E\ne0\iff\mathrm{FIN}\) globally.

Evidence: [LINE hostile audit](/Users/bsm/BSD_SEED_2243_12_LINE_HOSTILE_AUDIT_2026-09-19/LINE_HOSTILE_AUDIT.md), [O1 and its precise limits](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md), [A1/A2 formalization boundary](/Users/bsm/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/FORMALIZATION_BOUNDARY.md). A1/A2 establish conditional algebra; they establish neither arithmetic antecedent nor FIN.

### 5.3 Division fields and the global class-group component

For \(p\ge7\) outside \(\{19,59,487,2243,4547,5843\}\), let

\[
C_p=\operatorname{Hom}_{\mathrm{GL}_2(\mathbf F_p)}
\bigl(\mathrm{Cl}(\mathbf Q(E[p]))/p,E[p]\bigr).
\]

The completed written reduction is

\[
G[p]=0\quad\Longleftrightarrow\quad\dim_{\mathbf F_p}C_p\le2,
\qquad\dim C_p\ge1.
\]

The known Mordell–Weil classes already force a nonzero unramified contribution. The exact local conditions remove the away-from-\(p\) ray contributions; at good \(p\) the retained conductor-two ray source has natural-module multiplicity one. Restriction is an isomorphism by the finite-group cohomology vanishings; parity accounts for the remaining one-dimensional local ambiguity.

The global upper bound on \(C_p\) is still open and equivalent to the desired vanishing. The displayed finite set consists of exceptions to a simplified reduction, **not** a bound on the Sha primes. No class-group estimate is authorized as a continuation of this stopped route. Evidence: [division-field theorem](/Users/bsm/BSD_CODEX6_DIVISION_FIELD_HORIZONTAL_2026-09-19/DIVISION_FIELD_REDUCTION_THEOREM.md), [local module calculation](/Users/bsm/BSD_CODEX6_DIVISION_FIELD_HORIZONTAL_2026-09-19/LOCAL_CONDUCTOR_AND_MODULES.md).

### 5.4 Localization determinants of known rational points

By (K), an invertible localization matrix on \(\langle P_1,P_2\rangle/p\) does not show that the Selmer quotient vanishes. Abstractly, an isomorphism on \(M\) in \(0\to M\to M\oplus Q\to Q\to0\) says nothing about \(Q\).

The paused, unsealed seed experiment records invertible and singular auxiliary-pair matrices and an explicit \(p=3\) control. Its written determinant obstruction rules out one scalar, up to nonzero factors, matching all such raw determinants. The control is relative to the retained nonzero 3-primary input. This experiment is not promoted here to a newly sealed theorem. Determinants coupled to independently controlled arithmetic classes are outside that specific argument, but no such comparison has been proved.

Evidence: [raw determinant obstruction](/Users/bsm/BSD_CODEX6_SEED_INVENTION_2026-09-19/INTEGER_LIFT_OBSTRUCTION.md), [paused state](/Users/bsm/BSD_CODEX6_SEED_INVENTION_2026-09-19/STATE.json). The elementary quotient distinction does not depend on that experiment.

### 5.5 Destrempes–Malinin: trace and universal lifting

The audited failure is the implication

\[
\alpha\in\mathfrak P,\quad\mathfrak P\mid p
\quad\Longrightarrow\quad\operatorname{Tr}_{L/\mathbf Q}(\alpha)\in p\mathbf Z.
\]

It is false: in \(\mathbf Q(i)\), \(4+i\) lies above 17 but has trace 8. The audit also supplies contradictions in the division-field setting, rules out finite universal lift sets, and disproves the proposed fixed-field universal local coverage. These invalidate the paper's stated lifting mechanism, independently of publication status.

The seed checks do hold: for its integral short model,
\(4A^3+27B^2=-2^4 3^{14}\cdot2243\cdot4547^3\cdot5843^2\), and the required large-prime image is full. They do not repair the failed theorem. The proposed set \(\{7,13,2243,4547,5843\}\) is therefore not an established exhaustive Sha-exception set.

The earlier 20806a1 counterexample argument imported an exact \(L/\Omega\) value; the later audit explicitly did not replay that value. The internal trace/lifting obstruction is the controlling rejection and does not rely on an analytic Sha database entry. Evidence: [proof audit](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/PROOF_AUDIT.md), [obstruction proofs](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/TRACE_AND_FIXED_FIELD_OBSTRUCTION.md), [counterexample evidence boundary](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/COUNTEREXAMPLE_EVIDENCE.md).

### 5.6 Eisenstein congruences and the direction of control

For a cocycle \(c\in H^1(\mathbf Q,E[p])\),

\[
R_c(g)=\begin{pmatrix}\bar\rho(g)&c(g)\\0&1\end{pmatrix},\qquad
\det(1-XR_c(g))=(1-X)\det(1-X\bar\rho(g)).
\]

The characteristic polynomials forget \(c\). The exact characteristic-zero target \(1\oplus\rho_E\) has Hodge–Tate weights \(\{0,0,1\}\). In the declared GL(3) normalization its infinitesimal character is \(\{1,1,0\}\); a finite-dimensional algebraic coefficient requires the regular character \(\lambda+\rho_3\). Common twists and finite spectral-parameter jets do not repair this classical cohomology obstruction.

Nonclassical weight-two methods do reach the standard Selmer group at a chosen prime. The checked generalized matrix algebra comparison has direction

\[
\operatorname{Hom}(B_{\rm aut},\mathbf F_p)
\hookrightarrow\operatorname{Sel}_p(E)
\]

after its local checks. Its image consists of extensions factoring through the chosen automorphic quotient. It does not show that every exact Selmer extension factors through that quotient. The checked reducible \(R=T\) criterion requires a one-dimensional extension space and an independent upper bound; the two Mordell–Weil directions already prevent direct application. A fixed-prime family is also not automatically the localization of a fixed finite integral object across primes.

The required injection \(G[p]\hookrightarrow M[p]\), for one independently controlled finitely generated integral \(M\), was not obtained. **ROUTE_KILLED_AT_DIRECTION.** This repeats a previously encountered directional obstacle; it is not a new strict reduction. The classical weight calculation is an additional scoped constraint, not an impossibility theorem for every future nonclassical upper bound. Evidence: [exact type and direction audit](/Users/bsm/BSD_CODEX6_FIXED_EISENSTEIN_GATE_2026-09-19/EISENSTEIN_TYPE_AND_DIRECTION_AUDIT.md), [primary-source applicability audit](/Users/bsm/BSD_CODEX6_FIXED_EISENSTEIN_GATE_2026-09-19/PRIMARY_SOURCE_AUDIT.md).

### 5.7 Mellin periods, finite logarithmic systems, and endpoints

Let \(f\) be the normalized newform, \(\alpha_f=2\pi if(z)\,dz\), \(\ell(z)=\log(-i\sqrt Nz)\), and \(\gamma:i\infty\to i/\sqrt N\). The retained analytic identity is

\[
\int_\gamma\alpha_f\ell^2=\frac{L''(E,1)}2.
\tag{M1}
\]

It exists before FIN. The following particular arithmetic realizations are excluded by the written proofs:

* Nonconstant polynomials in \(\ell(z)\) have infinite cusp-translation span, so their literal coordinates do not fit a finite constant-monodromy system, even after the stated finite covers.
* An ordinary algebraic infinitesimal Tate-character deformation does not produce the asserted logarithmic jet. The algebraic connection \(d-J\,dt/t\) itself exists; the analytic coordinate used by M1 does not descend as proposed.
* The actual half-ray maps to a null-homotopic loop in the unpunctured elliptic curve. Its ordinary homology class cannot recover the nonzero weighted period.
* Finite algebraic connections, iterated integrals, and finite exact corrections in the class specified by L3 cannot supply the proposed local differential identity. Merely using a modular unit or a punctured curve in that same class does not remove the finite-translation-span obstruction.

If \(H_j\) denotes the half-ray moment and \(J_j\) the full-ray moment, then

\[
J_j=(1+(-1)^j)H_j.
\]

Thus \(H_0=0\) and \(J_1=0\), but no value for \(H_1\) follows. A correction
\(\alpha_f\ell^2-\beta=a\alpha_f+b\alpha_f\ell+dF\) leaves
\(bH_1+F(i/\sqrt N)-F(i\infty)\). Neither term may be silently discarded.

These obstructions do not disprove an independently established scalar equality from another construction. No such arithmetic comparison was obtained. Evidence: [M1–M4](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md), [L3](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/EXACT_CORRECTION_OBSTRUCTION.md), [lower moments and endpoints](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/LOWER_MOMENT_AND_ENDPOINT_GATE.md).

**Automorphic second-jet experiment (one bounded calculation).** A full Atkin–Lehner-invariant linear combination of the classical real-analytic cusp Eisenstein series can be normalized near \(s=0\) to have constant term exactly \((\sqrt N y)^s\). This particular section uses the two divisor orbits with 2-adic exponents \(\{0,3\}\) and \(\{1,2\}\) and 4547-adic exponents \(\{0,2\}\). Thus all scattered constant terms and all unwanted lower logarithmic terms cancel before integration. The [written calculation](audits/AUTOMORPHIC_SECOND_JET_EXPERIMENT.md) proves

\[
\int_\gamma\alpha_f\,\mathcal E''(z,0)
=\frac{L''(E,1)}2+\Delta,\qquad
\Delta=\int_\gamma\alpha_f R_N(z),
\]

with every Fourier coefficient of \(R_N\) explicit in (13) of that calculation. Its first Fourier frequency proves the integrand is not identically zero; **that initial calculation left the endpoint-section integral unevaluated; the endpoint certificate below now proves it positive**. The original verdict was **JET_IDENTITY_SURVIVES_WITH_ONE_TERM**, an exact analytic decomposition. This does not establish (*) without its residual, a regulator comparison, q=36, or a strict difficulty reduction. The nonholomorphic one-ray calculation is outside L3's holomorphic finite algebraic class and supplies no Eisenstein-ideal/Selmer mechanism. The calculation is complete; no arithmetic-intersection project or successor is active.

**Middle-orbit classification (authorized bounded extension).** The [written proof](audits/AUTOMORPHIC_MIDDLE_ORBIT_CLASSIFICATION.md) classifies all 96 divisor scalings: exactly four invariant orbits, of sizes 32, 32, 16, 16. The last two have 4547-adic exponent 1. Incoming constant term one and scattered term zero leave an affine family of dimension two over meromorphic germs; formulas (2.3)–(2.4) give every coefficient quadruple. A genuine second jet permits at most simple poles in its two free parameters, as proved in (3.2); formulas (3.3)–(3.9) give the full residual family. This extends the preceding report, which did not claim to classify other combinations.

The divisor-scaling Eisenstein representation is unramified at 4547 and entirely old at level \(4547^2\). Its new quotient is zero, and no nonzero fully Atkin–Lehner-invariant family is a \(U_{4547}\)-eigenvector. There is an independently defined **additional** local condition: invariance under the maximal compact stabilizing the unique midpoint of the level-\(4547^2\) lattice segment. With this condition, the normalized completion is uniquely the middle-orbit section (6.1), whose Fourier residual is (6.4). Corrected verdict: **CANONICAL_FAMILY_REMAINS; uniqueness holds only after imposing MC.** The previous UNIQUE_CANONICAL_COMPLETION headline overstated what the original symmetry and constant terms select. The old section instead symmetrizes the two endpoint spherical vectors. Both conventions are independent of the residual period; neither is implied by the elliptic newform's conductor.

For the midpoint section, \(\int_\gamma\alpha_f\mathcal E_{\rm mid}''=L''(E,1)/2+\Delta_{\rm mid}\). Its residual has only Fourier frequencies divisible by 4547 and is not identically zero. **That classification evaluated neither period. Both the midpoint residual and the endpoint-section residual are now proved positive by the two certified calculations below.** This closes the orbit/normalization classification, with written-proof and exact-algebra-check grade; it supplies no real-regulator comparison or BSD endpoint progress. The operation is complete and no successor is active.

**Midpoint \(U_{4547}\)-trace test.** The [bounded calculation](audits/MIDPOINT_UP_TRACE_TEST.md) verifies \(U_{4547}f=0\) from exact conductor exponent two, trivial nebentypus, and the newform theorem. The \(p=4547\) translated residual periods satisfy \(\sum_{a\bmod p}I_a=0\) and \(I_{-a}=\overline{I_a}\). Their additive Fourier components obey \(J_0=0\), while
\[
\Delta_{\rm mid}=I_0=\sum_{r\in\mathbf F_p^\times}J_r.
\]
Equations (3.1)–(3.6) of the report specify these surviving terms in the existing Fourier coefficients and explicit exponential-integral weights. The primitive conductor-two local type has dimension 4546. Its matrix coefficient \((4546,-1,\ldots,-1)\) proves that the trace and local newvector symmetries permit a nonzero zeroth coordinate; it is not asserted to be the actual period vector. Atkin–Lehner maps change the truncated paths, and the residual transforms with the explicit correction \(L(z)^2-L(wz)^2\), where \(L=\log(\sqrt N y)\). Thus cusp or Fricke equivalence supplies no missing individual-period equality. Verdict: **TRACE_ZERO_BUT_I0_NOT_FORCED**. The trace argument alone proves neither vanishing nor nonvanishing of the actual \(\Delta_{\rm mid}\); the numerical enclosure below settles its nonvanishing. The trace operation itself performed no numerical evaluation or regulator comparison.

**Global Mellin calculation.** The [derivation from the Fourier expansion](audits/MIDPOINT_GLOBAL_MELLIN_REDUCTION.md) proves
\[
P(u)=2\pi\int_0^\infty f(iy)R_{\rm mid}(iy)y^{u-1}\,dy
=(2\pi)^{1-u}\Gamma(u)\mathcal D(u),\qquad
P(1)=\mathcal D(1)=2\Delta_{\rm mid}.
\]
Both \(P\) and \(\mathcal D\) are entire, and \(P(u)=N^{1-u}P(2-u)\). The report's (3.1) is absolutely convergent for \(\Re u>3\); its value at one means the proved continuation, not an unqualified termwise sum. Its additive kernel specializes to \(1/(m+nd)\) and \(\log((m+nd)/(2nd))/(m-nd)\); the denominator \(m-nd\) is nonzero since \(4547\nmid m\) and \(4547\mid d\). Equations (4.3)–(4.6) give the residual's completed-zeta Mellin transform and the exact Barnes convolution with \(\Lambda(f,u-w)\).

The normalized family \(\mathcal D(u)\) has a nonzero continuous Mellin density \(-1/(x+4546)\) on \(4548<x<4549\). Uniqueness of Mellin transforms of weighted finite measures excludes an ordinary Dirichlet series, hence an Euler Dirichlet product or finite combinations of the Dirichlet series and derivatives specified in report §5. This is a functional obstruction for that normalization; it does **not** exclude every possible identity at the isolated value \(u=1\), or identities with freely inserted parameter-dependent archimedean kernels. Verdict: **EXPLICIT_SHIFTED_CONVOLUTION**, with the exact continued series and Barnes kernel. The Mellin operation left the scalar unevaluated; the numerical enclosure below subsequently proves it positive. That Mellin operation performed no numerical calculation, local-route continuation, or regulator comparison.

**Bounded Green-kernel comparison.** The [source and Fourier calculation](audits/MIDPOINT_GREEN_KERNEL_TEST.md) gives **PARTIAL_KERNEL_MATCH**. With \(J=R_{\rm mid}+L^2=\mathcal E_{\rm mid}''(z,0)\), \(L=\log(\sqrt N y)\), and \(\mathscr D_z=(2\pi i)^{-1}\partial_z\), it proves
\[
\mathscr D_zJ(z)=\frac12\sum_{d\in\mathcal O}d\,[b_d\mathsf E_2'(dz,1)+(\kappa b_d+e_d)\mathsf E_2(dz,1)],
\]
where \(\mathsf E_2=\mathscr D_z[\pi^{-s}\Gamma(s)\zeta(2s)E(z,s)]\) is exactly Berndt–Kühn's unmodified weight-two series; the explicit orbit coefficients are those of the residual. Positive, negative, and zero Fourier modes agree after this derivative, including the \(E_1=-\operatorname{Ei}=\Gamma(0,\cdot)\) normalization and elementary correction. Report (13) retains the additional normalization and cutoff term in the cited arithmetic theorem. The match is with its already-paired generating series in an auxiliary modular variable, not with a Green current in that variable.

The same calculation proves \(\Delta_0R_{\rm mid}=2H\ne0\), \(\Delta_0H=0\), and records that \(R_{\rm mid}\) has the explicit constant-term subtraction automorphy defect, whereas \(J\) is automorphic. Both are smooth in the interior. Equality to finite Green currents modulo interior-smooth boundary terms therefore requires the net interior divisor current to vanish. This does not exclude smooth zero-divisor kernels, parameter derivatives, or geometric integrals of Green functions; those exceptions are explicitly checked against the sources. No arithmetic Chow class for \(R_{\rm mid}\), arithmetic interpretation of its ray functional, residual evaluation, or regulator comparison is established. No numerical evaluation or successor operation was performed.

**Full-ray primitive and secondary descent.** The [bounded test](audits/MIDPOINT_SECONDARY_DESCENT_TEST.md) proves \(\Phi(z)=\int_{i\infty}^z\alpha_f\), \(\Phi(\infty)=\Phi(0)=L(f,1)=0\), and exponential endpoint decay. In particular \([\Phi J]_{i\infty}^{0}=0\), and
\[
\int_{i\infty}^{0}\alpha_fJ=-\int_{i\infty}^{0}\Phi\,dJ
=-4\pi\int_0^\infty\Phi(iy)\mathscr D_zJ(iy)\,dy.
\]
Substitution of the preceding differentiated Eisenstein identity gives report (6), with all signs and constants. It evaluates neither the weighted period nor its residual.

The period cocycle gives \(\gamma^*(\Phi dJ)-\Phi dJ=d(\lambda_\gamma J)\), and the exact gauge \(d(\Phi J)\) gives the global representative \(A=-J\alpha_f\). Its curvature is \(F=dA=\alpha_f\wedge dJ\ne0\). Thus descent modulo exact one-forms succeeds, but closedness for absolute/relative de Rham cohomology and flatness for the corresponding holomorphic Deligne connection fail. The genuine weaker object is the topologically trivial nonflat smooth connection \(d-J\alpha_f\) on \(Y_0(N)\); forgetting its connection gives the zero holomorphic Picard class. This object must not be relabeled as an arithmetic regulator.

At the cusp \(q=e^{2\pi iz}=0\), the curvature has leading coefficient \(-\log(\sqrt Ny)/(2\pi y\bar q)\), which is locally integrable but unbounded. It cannot extend smoothly across the cusp under any gauge. Since the elliptic logarithm satisfies \(w\circ\pi=c_Eq+O(q^2)\), it cannot be the pullback of a smooth connection on the unpunctured elliptic curve. Verdict: **SECONDARY_CLASS_OBSTRUCTED**, for the proposed relative/holomorphic Deligne-regulator interpretation on compact \(X_0(N)\). This does not deny the smooth open-curve connection or exclude arbitrary singular-current theories. The null-homotopic elliptic image does not force a nonflat holonomy to vanish; \(dJ\) is closed, while \(\Phi dJ\) is not. No arithmetic cycle, period evaluation, regulator comparison, or successor is obtained.

**Certified midpoint residual evaluation.** The [bounded interval calculation](audits/MIDPOINT_DELTA_INTERVAL.md) proves, with computer-assisted grade,
\[
\boxed{0.000535614030\le\Delta_{\rm mid}\le0.000801512867.}
\]
The decimal endpoints are outward-rounded exact rationals. A direct Fourier/half-ray enclosure is \([0.000264817525,0.001072309373]\); the integration-by-parts representation gives the narrower displayed interval. Both exclude zero and overlap. The coefficient stream through 150 million matches both retained independent certificate roots. The report supplies explicit infinite-coefficient, residual Fourier, compression, quadrature, and infinite-integral bounds, with Arb arithmetic. A final uncached replay reproduces all 28 saved ball dumps exactly. This is not a formal proof-assistant verification or independent human review.

**DELTA_MID_NONZERO_PROVED.** Consequently the MC midpoint section satisfies
\[
\int_\gamma\alpha_f\mathcal E_{\rm mid}''
=\int_\gamma\alpha_f\ell^2+\Delta_{\rm mid}
>\int_\gamma\alpha_f\ell^2.
\]
This particular completion does not reproduce the original weighted Mellin period after integration. Its residual must not be silently discarded or subjected to a further automatic-annihilation scout. That midpoint result did not evaluate the endpoint-section residual; the final endpoint test below now does. It does not exclude every other member of the classified completion family. It proves no real-regulator comparison, FIN, order-nine result, or scalar BSD identity. The single numerical operation is complete; no successor is authorized by it.

**Final vertex-spherical endpoint test.** The [scoped proof and interval certificate](audits/ENDPOINT_VERTEX_COMPLETION_TEST.md) first defines the class: choose the spherical line of one of the three vertices of the specified length-two segment at \(p=4547\), apply Fricke symmetrization, and retain the existing away-from-\(p\) data and incoming/scattered normalizations. The lines \(e_0,e_1,e_2\) map to exactly two lines, \(\mathcal M(e_0+e_2)\) and \(\mathcal M e_1\). The constant-term equations uniquely normalize them to \(\mathcal E_*\) and \(\mathcal E_{\rm mid}\). This is a classification of single-vertex symmetrizations; their full invariant linear span has further lines and is not reduced to two possibilities.

The endpoint residual obeys the exact identity
\[
R_*(z)=\tfrac12[R_{\rm mid}(z/p)+R_{\rm mid}(pz)],
\]
which agrees with the original endpoint Fourier expansion and preserves the existing numerical majorants. One 128-bit Arb run with the retained coefficient certificate proves
\[
\boxed{0.000757821864\le\Delta_*\le0.000841639764.}
\]
The direct-integral enclosure \([0.000691563630,0.000907897998]\) and the narrower integration-by-parts enclosure both exclude zero. Every infinite-sum and integration error is bounded explicitly in the certificate, which imports the existing midpoint error proofs. The run used 54.315 seconds and 33234944 bytes peak resident memory. Verdict: **ENDPOINT_DELTA_NONZERO_PROVED**, with computer-assisted proof grade and shared coefficient/software trust base.

**Scoped stop:** with that fixed normalization, no Fricke symmetrization of a single vertex-spherical line of this segment reproduces the weighted Mellin period. The midpoint and symmetrized-endpoint cases are both excluded by positive residuals. This stops the two-case vertex mechanism, including further attempts to annihilate either residual. It is not a theorem about arbitrary mixtures in the invariant span or all other local conditions. No arbitrary-family test, height comparison, FIN argument, or successor is started.

**Curvature-area test.** The [written derivation](audits/CURVATURE_AREA_TEST.md) proves **BROAD_CURVATURE_ORTHOGONALITY_THEOREM**. For a global \(C^1\) scalar function \(J\) on a modular curve, with polynomial/logarithmic growth of \(J\) and its first derivatives in every cusp coordinate, and every holomorphic weight-two cusp differential \(\alpha_f\),
\[
\boxed{\int_{Y_0(N)}\alpha_f\wedge dJ=0.}
\]
The integral is absolutely convergent. It equals the limit of the sum of the cusp fluxes \(\int_{x=0}^{h_{\mathfrak a}}J_{\mathfrak a}\alpha_{f,\mathfrak a}\); these vanish by cusp decay. This follows from \(\alpha_f\wedge dJ=d(-J\alpha_f)\), even when its curvature coefficient does not extend smoothly to the compactification. The actual midpoint jet and every regular finite divisor-scaling Eisenstein jet satisfy the bounds. The report independently unfolds the Eisenstein family before parameter differentiation: the inner integral is a cusp form's zero constant coefficient, so the same area pairing is zero. For real \(J\), the normalization is \(-8\pi^2i\langle f,\mathscr D_zJ\rangle_2\).

For the midpoint Fourier expansion, horizontal integration pairs positive frequency \(m\) of \(f\) with negative frequency \(-nd\) of \(J\). The diagonal \(m=nd\) vanishes by \(a_{4547n}=0\). This is a strip calculation, not a replacement of a modular domain by a strip; the full-domain theorem does not need the Fourier-support restriction or local newness. Also \(\partial\{0,\infty\}=[\infty]-[0]\ne0\) in cusp homology, so the relative path cannot bound a two-chain just because its \(f\)-period vanishes.

**Scope of the new stop:** unweighted full-domain curvature integrals from global moderate-growth scalar jets are zero, including scalar two-variable kernels satisfying the same hypotheses in each integrated variable. Changing only Fourier support cannot evade this. A nonexact \((0,1)\)-kernel can give a nonzero complex Hodge pairing, as the report proves by an explicit finite reproducing kernel, but this changes the exactness hypothesis and supplies no Mordell–Weil height determinant. No statement about every singular, multivalued, nonexact, or boundary-flux construction follows. The result is a written elementary analytic/topological proof with imported project inputs, not independent referee review, a formal certificate, or a claim of literature novelty. The positive ray-residual certificates remain unchanged. The bounded operation is complete, with no successor active.

### 5.8 Finite local data and derivative comparisons

Totally positive quadratic algebraic integers can approach 36 and match arbitrarily much prescribed finite local data while a second conjugate escapes. Neither bounded degree nor finite \(p\)-adic precision supplies the conjugate bound in §4. Equality of selected local units is likewise not a characteristic-zero rationality theorem.

The known first-derivative formulas do not calculate a primitive double zero: on this seed their first-derivative side vanishes. The factorization \(L(E/K,s)=L(E,s)L(E^K,s)\) is a valid identity, but multiplying a double zero by a nonzero auxiliary factor does not furnish its missing second-derivative arithmetic comparison. Algebraicity of a vanishing critical value and a functional equation alone do not imply arithmeticity of the second derivative.

The generalized Perrin–Riou/leading-term comparison remains unproved at the required interface. BKS Lemma U is an existing unit conclusion, not the missing real comparison; the recorded first digit \(u_5\equiv1\pmod5\) is consistency only. Evidence: [quantitative counterexamples](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/QUANTITATIVE_ALGEBRAICITY_THEOREM.md), [unit and normalization audit](/Users/bsm/BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/LEMMA_U_AND_P5_UNIT_AUDIT.md).

**Later analytic bridge, with its actual qualification.** The RS2 cross-cusp records give a written derivation of \(\langle\widetilde A_2,f\rangle=\widetilde\kappa_NL(f,2)L''(f,1)\), with explicit nonzero \(\widetilde\kappa_N\). Their governing [archive correction](/Users/bsm/BSD_FABLE_RS2_L3_2026-09-20/ARCHIVE_NOTE.md) retains a cross-cusp normalization source-custody seam and leaves the weight-two shifted-divisor continuation (L3) open. It explicitly withdraws the claim that the construction was proved incapable of an arithmetic continuation. No Néron–Tate comparison was identified. This is a source-qualified recorded analytic bridge, not an imported proof of FORMULA or a fresh proof audit here. Even granting the pairing identity, algebraicity of its cuspidal \(f\)-coefficient alone does not compare the Petersson/\(L(f,2)\) factor with \(\Omega_E R\). The [focused bridge assessment, §3](_work/bridge_repair_assessment_2026-09-21/ASSESSMENT.md) spells out that remaining factor. RS2 remains operationally archived; no successor is launched.

### 5.9 Generalized Kato classes, strict lines, and fixed-prime families

The older H5–H9 program distinguishes a class in a modified Selmer group from a rational-point Kummer class. A core-rank-one Euler system for the modified local conditions does not automatically control \(V_p\Sha\) in the Bloch–Kato sequence. The missing comparison with the rational-point subspace is substantive, not implied by support, norm compatibility, or primitivity terminology.

**Completed geometric bridge retained.** [H9R16-C](/Users/bsm/H9R16C_SEALED_MILESTONE_2026-09-15/00_MILESTONE.md) constructs the compatible Hom-valued Jacobian point tower and proves its integral finite-level compatibility with constant one, at its recorded model-audit tier. Its [explicit nonclaims](/Users/bsm/H9R16C_SEALED_MILESTONE_2026-09-15/05_NON_CLAIMS.md) exclude descent to \(E(\mathbf Q)\), non-torsion, and the target arithmetic application. The subsequent failure of that application does not erase the finite geometric theorem.

**Consequence of the settled primary inputs (2026-09-21).** Define \(S_p\) using the usual global Selmer group with local Kummer conditions and rational \(p\)-adic coefficients. At \(p\in\{2,3,5,7,11\}\), the retained finiteness of \(G[p^\infty]\) gives
\[
S_p=\delta_p(E(\mathbf Q)\otimes\mathbf Q_p)
=\mathbf Q_p\delta_p(P_1)\oplus\mathbf Q_p\delta_p(P_2).
\]
At \(p=5,7,11\), the retained primary vanishing also gives \(\operatorname{Sel}_{p^n}(E/\mathbf Q)\simeq(\mathbf Z/p^n)^2\) for every \(n\ge1\), and
\[
\ker(\operatorname{loc}_p:S_p\to H_f^1(\mathbf Q_p,V_pE))
=\mathbf Q_p\bigl(\log_p(P_2)\delta_p(P_1)-\log_p(P_1)\delta_p(P_2)\bigr).
\]
The [short proof](_work/bridge_repair_assessment_2026-09-21/ASSESSMENT.md) uses the Kummer exact sequence and the local logarithm. This supplies Kummer membership for a class already shown to lie in this Selmer group at these primes. It does not prove that a proposed class exists, satisfies the local conditions, is nonzero, or is the specialization of the geometric tower. This is a standard deduction from completed primary arithmetic, not new FIN or FORMULA progress; the 5-primary calibration below already used its rational form.

**Explicit finite-level connection at 11 (2026-09-21).** Combining the completed 11-primary theorem with Aristotle-B's corrected localization framework gives more than the older assertion that its finite-localization kernel is nonzero. For \(S=\{\infty,2,3,11,2243,4547,5843\}\), exact rational point arithmetic gives local coordinates \(\lambda_{11}(P_1)=1\), \(\lambda_{11}(P_2)=2\), where \(\lambda_{11}(Q)=14^{-1}t([14]Q)/11\bmod11\) and \(t=-x/y\). Consequently
\[
\ker(\operatorname{loc}_S|_{\operatorname{Sel}_{11}(E/\mathbf Q)})
=\mathbf F_{11}\delta_{11}(2P_1-P_2).
\]
The localization image and kernel each have dimension one; the corrected bad-place cohomology statement makes all other local factors in S zero. The [proof and exact computation](_work/bridge_repair_assessment_2026-09-21/C11_LOCALIZATION_JOIN.md) retain the imported C11/basis/local-theory grades. This is a standard deduction with an explicit mod-11 calculation, not an additional Sha theorem. It concerns mod-11 localization, not exact vanishing of the 11-adic logarithm. The older auxiliary-class target justified by Aristotle-B's reversed inequality is withdrawn in its correction and is not revived.

At the fixed seed and \(p=5\), the calibrated strict line is
\(\mathbf Q_5(P_1-tP_2)\), with \(t=\log_5(P_1)/\log_5(P_2)\). The retained sealed-branch calibration says the particular Castella–Hsieh branch output vanishes wherever defined and misses that line. The available 5-primary theorem is an input to that calibration, not its output. This excludes that branch, not every possible generalized Kato construction.

The seed-to-family regulator congruence is a retained fixed-prime result. Its remaining modular-symbol bit was not controlled uniformly, and no global FIN conclusion follows. Similarly, extending the known wedge of Kummer classes to the tested primitive residual Stark system was equivalent to \(G[p]=0\); its existence was not a new independent upper bound. The low-degree transfer and fixed-\(E[5]\) geometry gates failed their stated finite prerequisites; they do not prove universal impossibility of descent.

Evidence: [seed calibration](/Users/bsm/SEED_2243_12_MECHANISM_LANES_2026-09-18/00_LANE1_SYNTHESIS.md), [fixed-prime family report](/Users/bsm/BSD_LANE2_SEED_TO_FAMILY_2026-09-18/LANE2_REPORT.md), [older controlled-module audit, C8–C9](/Users/bsm/BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15/14_WHOLE_MAP_ASSEMBLY_AND_MISSING_INPUT_AUDIT_2026-09-16.md), and the retained scoped C1 records indexed in [the historical route report](ROUTES_AND_STOPS.md). The C1 proofs were not independently rerun in this consolidation.

### 5.10 Run013, the actual-point bridge, and H41: completed results and supersession

**The older family results are completed inputs, not merely failed approaches to this seed.** Run013 retains a conventional explicit 2-isogeny descent for the twists of 62a1 with prime \(q\equiv5\pmod8\) and \((q/31)=-1\), giving algebraic rank zero and trivial 2-primary Sha. The September 10 minimization proves that these congruences already imply the extra finite-field conditions in the original family; this prime set has relative natural density \(1/8\). The retained full-BSD assembly uses Zhai and Banwait–Huang with the public-preprint qualifications in its source. The 66b1 record gives the parallel qualified assembly for prime \(q\equiv5\pmod8\), \((q/3)=-1\), \((q/11)=1\). These are infinite twist-family results at their recorded grades, not new proofs or fresh source audits in this reconciliation. Evidence: [Run013 proof ledger](/Users/bsm/run013-62a1-bsd2-2026-08-22/PROOF.md), [family minimization](/Users/bsm/run013-family-minimisation-successor-2026-09-10/PROPOSITIONS_A_B.md), [66b1 theorem](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/66B1_CONVENTIONAL_FREEZE_001/THEOREM_STATEMENT.md), and [66b1 qualified assembly](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/66B1_CONVENTIONAL_FREEZE_001/LITERATURE_DEPENDENT_STRONG_BSD_COROLLARY.md).

**The formal point-group bridge also finished.** The common models are
\[
E_{r,q}:y^2=x^3+(1-2r)q x^2+r^2q^2x,\qquad r=\pm2^m,\quad m\ge3.
\]
The 62a1 and 66b1 descent models are respectively \(r=8\) and \(r=-8\). Under the exact `Params` and `H41` hypotheses in the frozen sources, the P01/P03/P04 chain reaches the actual rational-point quotient \(E_{r,q}(\mathbf Q)/2E_{r,q}(\mathbf Q)\simeq\mathbf Z/2\). Gate-R then proves rank zero, and its later finiteness freeze proves `Finite` for the actual rational-point group, without assuming Mordell–Weil finite generation. This supersedes the intermediate audit's “finiteness consequence not yet certified” status. It is finiteness of \(E_{r,q}(\mathbf Q)\), not finiteness of \(\Sha\). The formal claims are retained from their recorded Lean builds and source signatures; no fresh Lean rebuild was performed here. The separate conventional [algebraic composition](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/POST_FS_BSD2_COMPOSITION_FREEZE_001/THEOREM_A_ALGEBRAIC_COMPOSITION.md) derives rank zero and \(\Sha[2^\infty]=0\) from the established isogeny-Selmer shapes. Evidence: [actual-point bridge](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/THEOREM_STATUS_H1_FREE_BRIDGE_COMPLETE_001/THEOREM_STATUS.md), [rank assembly](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001/STATUS.md), and [finiteness freeze](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/GATE_R_FINITENESS_FORMALIZATION_FREEZE_001/STATUS.md).

The older characteristic-two multiplicity-one route needed
\(\dim_{\mathbf F_2}J_0(N)[\mathfrak m]=2\). The established statement about a one-dimensional differential eigenspace did not imply this Jacobian statement. The missing socle/Gorenstein assertion at the reducible Eisenstein prime was not supplied by the cited generic theorem. Component-group information could also vanish at precisely the vertices whose identity-component data were needed.

**The later H41 result must not be erased by that stop.** The September 16 supersession record closes the retained positive and negative H41 twist-family arguments through a specific mod-4 integral-character construction, with the stated external-literature qualifications. It supersedes the old global “H41 blocked” label; it does not retroactively prove the abandoned multiplicity-one shortcut. Those rank-zero chains consume \(L(E,1)\ne0\) and therefore do not transfer to this primitive rank-two seed.

The sealed Desktop [mod-4 addendum 018](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/H41_MOD4_SUCCESSOR_ADDENDUM_018/ADDENDUM.md) gives the precise changed input: integral character coordinates obtained before the component-group quotient, which determine the optimal curve, cusp order, and odd base value \(4L(E,1)/\Omega_{E,\mathbf R}\). Its retained positive/negative branches then reach twist BSD(2) and qualified full BSD. This is a conventional proof with recorded model reviews, not a Lean proof or independent human acceptance. The root proof and sealed Desktop proof were byte-identical when compared on September 21. [Addendum 019](/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/H41_W_AUDIT_IMPORT_ROWS_CUSTODY_ADDENDUM_019/ADDENDUM.md) binds the later source-import rows without adding a new theorem. No infinitude of H41 base curves, extension outside the retained twists, or general H9 application is claimed.

Evidence for the preceding stopped mechanism: [older multiplicity-one distinction, Track C](/Users/bsm/BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15/01_BSD_SUCCESSOR_MASTER_STATUS_AND_DEPENDENCY_MAP.md), [claim-specific H41 supersession](/Users/bsm/BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15/14_WHOLE_MAP_ASSEMBLY_AND_MISSING_INPUT_AUDIT_2026-09-16.md). The [September 21 coverage reconciliation](_work/historical_coverage_2026-09-21/COVERAGE_RECONCILIATION.md) records exactly which older sources were read and the remaining coverage limits. It does not promote any of these rank-zero family results to a rank-two regulator comparison.

### 5.11 Modular visibility: coverage does not fix the ambient

Tamiozzo's general Theorem 4.1.1, not merely its introductory corollary, assumes squarefree conductor. It nevertheless supplies a direction missing from older lower-bound constructions: **all** relevant Sha classes are visible in one modular ambient for each fixed residual prime. Its public manuscript also includes a supersingular case with an extra local hypothesis; it is not an ordinary-only theorem. The 2026 proceedings publication is verified at metadata level; this operation inspected the public 2024 manuscript's body.

The seed's nonsquarefree ordinary gate can be handled using Zhang's published Hypothesis \(\heartsuit\). For every good ordinary \(p\ge5\), the multiplicative primes \(3,2243,5843\) are residually ramified. At the additive primes \(2,4547\),
\(H^0(\mathbf Q_q,E[p])=H^1(\mathbf Q_q,E[p])=0\).
Choose an imaginary quadratic field in which all bad primes split. Zhang's level raising, local-condition comparison, and nonzero underived Heegner class in residual Selmer dimension one give the written varying-level visibility deduction in the [visibility audit, §3](audits/fixed_visibility_2026-09-19/FIXED_VISIBILITY_AUDIT.md). This imports the published theorems; it is not a fresh proof audit of their entire dependency chains. It does not use the 3-primary repair.

Two obstructions stop the proposed horizontal continuation. For a fixed good auxiliary prime \(\ell\),

\[
D_\ell=(\ell+1)^2-a_\ell(E)^2\ge(\ell-1)^2>0,
\qquad \ell\text{ admissible for }p\Longrightarrow p\mid D_\ell.
\]

Thus any finite predetermined stock of auxiliary primes works for only finitely many residual primes. More strongly, fix a modular target \(A_0\) at finitely many predetermined levels. Outside a finite set, every partner \(F_i\) in the level-raised gluing

\[
A_p=(E\times\prod_iF_i)/E[p]^r
\]

has a new ramified prime outside those levels, so \(\operatorname{Hom}_{\mathbf Q}(F_i,A_0)=0\). Every map \(h:A_p\to A_0\) must then kill the embedded \(E[p]\): pull it back to the product and evaluate it on the anti-diagonal kernel. Hence \(h\circ i_p=i_0\circ[u]\) forces \(p\mid u\). This excludes functorial descent preserving the class up to a \(p\)-unit, not every conceivable independent proof of fixed visibility.

For a fixed embedding \(i_0:E\hookrightarrow A_0\), Poincaré reducibility supplies \(r\circ i_0=[d]\) for some fixed nonzero integer \(d\). Its visible subgroup is finite and killed by \(d\). Consequently eventual fixed-ambient visibility on the ordinary tail is **equivalent** to eventual ordinary Sha vanishing; the reverse implication is vacuous visibility of zero. No strict difficulty reduction follows from proposing that statement alone.

**NO_HORIZONTAL_GAIN.** No Sha-support integer is extracted. The integer \(\prod D_\ell\) obstructs a chosen auxiliary stock and must not be relabeled a Sha bound. Sha local triviality kills the image in \(H^1(K_v,E)\), not necessarily its Selmer lift in \(H^1(K_v,E[p])\); residual representation level lowering does not transport the point or gluing extension. The ordinary nonsquarefree coverage deduction gives no supersingular transfer, primary-depth result, FIN, order-nine result, or scalar identity. The tested functorial descent is stopped; no successor is launched.

Evidence and complete scoped proofs: [fixed visibility audit](audits/fixed_visibility_2026-09-19/FIXED_VISIBILITY_AUDIT.md). The earlier blanket claim that every visibility argument has only a lower-bound direction is corrected; the lack of fixed ambient control remains.

### 5.12 Torus and vector extensions do not remove the Sha obstruction

The new admission check starts with the actual basis: rigidified degree-zero line bundles
\(\mathcal L_i=\mathcal O_E([P_i]-[O])\) define a commutative extension
\(0\to\mathbf G_m^2\to\mathcal G_P\to E\to0\).
This is a genuine characteristic-zero arithmetic object. Constructing it does not give a new finiteness argument.

**Exact lemma.** For any number field \(k\), abelian variety \(A/k\), and commutative extension
\(0\to\mathbf G_m^s\to\mathcal G\to A\to0\),
\[
\Sha^1(k,\mathcal G)\xrightarrow{\sim}\Sha(k,A),
\qquad
\Sha^1(k,H):=\ker\!\left(H^1(k,H)\to\prod_v H^1(k_v,H)\right).
\]
Hilbert90 makes the global and local maps \(H^1(\mathcal G)\to H^1(A)\) injective. For a locally trivial \(A\)-torsor, its connecting obstruction lies in
\(\ker(\operatorname{Br}(k)^s\to\prod_v\operatorname{Br}(k_v)^s)=0\)
by Brauer--Hasse--Noether. Its unique global lift is locally trivial by the local injections. No finiteness assumption is used. Vector-group extensions give the same conclusion, since their positive-degree field cohomology vanishes; quasi-trivial tori do as well by Shapiro's lemma.

More generally, suppose \(T\) splits over a finite Galois extension of degree \(d\). Then
\[
0\to T\to\mathcal G\to A\to0,
\quad \ell\nmid d
\quad\Longrightarrow\quad
\Sha^1(k,\mathcal G)[\ell^\infty]\simeq\Sha(k,A)[\ell^\infty].
\]
Restriction/corestriction kills \(H^1(k,T)\), every \(H^1(k_v,T)\), and \(\Sha^2(k,T)\) by \(d\); the last assertion follows by the Brauer injection over the splitting field. If \(\xi\in\Sha(A)[\ell^n]\), its obstruction is both \(d\)-torsion and \(\ell^n\)-torsion, hence zero. Choose a global lift \(\eta\). Then \(d\eta\) is locally trivial and killed by \(\ell^n\). Multiplying it by an inverse of \(d\bmod\ell^n\) lifts \(\xi\) in the required primary group. The kernel is killed by \(d\), so is zero on that group. This proves the assertion at all primary depths.

For the seed's split extension, there is an additional obstruction to an affine-group shortcut:
\[
\Gamma(\mathcal G_P,\mathcal O)
=\bigoplus_{(a,b)\in\mathbf Z^2}
 H^0(E,\mathcal L_{aP_1+bP_2})=\mathbf Q,
\qquad
\mathcal L_Q=\mathcal O_E([Q]-[O]).
\]
Independence of the two points makes every nonzero weight a nontrivial degree-zero line bundle, hence gives it no global section. Thus the group is anti-affine; in particular, every finite-dimensional algebraic linear representation is trivial. It is not an affine group to which an affine-group arithmetic theorem can simply be applied. The line-bundle grading and this criterion are checked against [Brion, §2.1 and Proposition2.1](https://arxiv.org/pdf/0710.5211). The cohomological inputs are [Milne, *Class Field Theory*, II1.22--1.24, IV2.14(e), and VII7](https://www.jmilne.org/math/CourseNotes/CFT.pdf).

**Admission verdict:** the split construction retains exactly the unknown Sha group, and a fixed nonsplit torus retains its entire prime tail outside a fixed finite set. This rules out treating toric/vector packaging itself as a difficulty reduction or replacing its arithmetic by that of an affine group. It does not disprove an additional substantive theorem about an arithmetic volume, nor exclude arbitrary mixed motives or connections. No such extra theorem or real leading-term comparison has been established here. No volume calculation or successor is launched from this gate. These are elementary deductions from standard inputs, not a claim of new literature results or a new FIN/FORMULA arrow.

The [working checkpoint](_work/active_full_bsd/WORKING.md) records the calculation and the bounded historical collision check; [source identities](_work/active_full_bsd/toric_sources/BINDINGS.json) identify the exact primary texts read. The later 13-primary theorem in §2 is the most recent positive primary closure; it does not change this toric obstruction.

## 6. Which assertions supersede which

Supersession is by claim and evidence. It does not delete the older result's valid scope or resolve an unrelated gap.

| Earlier assertion | Current replacement | Reason/source |
|---|---|---|
| Analytic rank two is only numerical | Rigorous enclosure proves exact analytic rank two | §2 analytic-rank certificate |
| The 5-primary chain still has a floating-point coefficient node | That node is rigorously certified | §2 sealed 5-primary successor; the older certificate remains historical |
| The 7-primary component is unresolved | It vanishes; its leading coefficient is a certified unit | §2 and the new 7-primary theorem |
| C11 is uncomputed and the 11-primary component is unresolved | C11 is 8 modulo11 (omega1); the 11-primary component vanishes | §2 and the new 11-primary theorem; the remote missing-artifact blocker is resolved by the local certified run |
| C13 is uncomputed and the 13-primary component is unresolved | C13 is 2 modulo13 (omega1), or 1 for the full real period; the 13-primary component vanishes | §2 and the completed [13-primary theorem](audits/P13_PRIMARY_THEOREM.md); numerical input, exact downstream and custody checks completed |
| The returned C13 values 7 and8 have an unresolved factor-of-three discrepancy | Both used lattice numerators; the alternative weights also omitted alpha^-2. Corrections 7*4=2 and 8*4*9=2 modulo13 preserve nonvanishing | [Exact normalization reconciliation](_work/active_full_bsd/p13/NORMALIZATION.md); original external result preserved |
| 441, 1089 or 1521 is the next possible total order under the current small-primary inputs | The successive 7-, 11- and 13-primary theorems raise it through1089 and1521 to2601, with gcd(t,30030)=1 | §3; the earlier thresholds remain valid under their weaker inputs |
| \(q\)'s narrow floating estimate is an exact proof | Only the wider rigorous interval is a proof input | §2 regulator/analytic certificates |
| Earlier unsupported claims that R2 was closed or cosmetic | The integral comparison has a written proof, but complete R2 closure is not retained after review | §2; original repair §3.6 fails at the removed Euler factor |
| R1's nonsplit source is inaccessible/unread | Jones's author copy is recovered and read; finiteness is derived before his leading-term formula | R1/R2 addendum §2 |
| No seed proof of R2's canonical/Gross-period comparison is supplied | The integral comparison survives the separate model review; its downstream μ-transfer claim does not | R1/R2 addendum §§3.1–3.5 and hostile review; Wiles and Ribet hypotheses checked |
| The written R1/R2 repair completely closes the internal p=3 audit | R1 and the integral period comparison survive; §3.6 fails. The bounded cleanup stops with internal SU provenance open, while the 3-primary theorem is retained via published Theorem A | §2, hostile review, and bounded Euler reconciliation |
| The failed internal μ transfer creates a new failure of 3-primary arithmetic | The published theorem remains the imported equality; its top-level Hida/Fitting proof and common Euler cancellation are identified | Bounded reconciliation §§2–4; no claim that the entire SU proof was independently reconstructed |
| Denominator 86 is the sharp retained interval threshold | 174; 175 fails | §4 exact integer-separation proof |
| FIN, or FIN plus \(q=36\), already proves the predicted formula | FIN permits \(9t^2\); order nine remains necessary | §3 square-order argument |
| WC is possibly equivalent on the ordinary tail | O1 proves the precise depth-zero equivalence | §5.2; no stronger global converse imported |
| LINE and determinant-line RZ are unconditionally equivalent | The finiteness-dependent RZ identification is withdrawn | §5.2 hostile audit |
| A finite source or perfect profinite complex bounds support | Explicit algebraic countermodels refute this inference | §5.1 |
| A finite set plus a tail is automatically a strict reduction | Its existence with all necessary conclusions is equivalent to FIN | §3; an independent method is still required |
| A bounded \(G[p]\) or finite support alone proves FIN | Full primary depths must be controlled | §3 counterexample |
| Supersingular primes require the old deeper test | The retained sufficient test is at depth two | §3 SS audit; still per prime and uncomputed |
| An ordinary-only theorem leaves finitely many cases | Supersingular primes form another infinite regime | §3 |
| 4547 is merely a compute-cost problem | The recorded approach has a theory gap as well | §3 |
| DM was a newly overlooked valid tail theorem | Earlier rejection exists; the later audit identifies false lifting steps | §5.5, with the older exact-data qualification preserved |
| The division-field exceptions bound possible Sha support | They bound the simplified reduction's applicability only | §5.3 |
| Eisenstein lower bounds control excess Sha | No converse or fixed integral upper bound was obtained | §5.6; repeated mechanism failure |
| Every visibility argument only produces a lower bound | Tamiozzo covers all Sha classes under his hypotheses; the ordinary seed transfer is written using Zhang's nonsquarefree inputs | §5.11 and visibility audit §3; varying ambient gives no horizontal bound |
| The general visibility theorem removes squarefreeness, or is ordinary-only | Its general theorem remains squarefree and includes an extra-hypothesis supersingular case | Visibility audit §1; public manuscript checked, published full text not obtained |
| Varying modular visibility can be made fixed-level just by local triviality / level lowering | Finite auxiliary stocks and p-unit functorial descent of the constructed ambients are obstructed | §5.11; no universal impossibility claim about unrelated fixed-level proofs |
| Fixed-ambient visibility itself demonstrates a strict reduction | For any fixed embedding its eventual ordinary-tail statement is equivalent to eventual ordinary vanishing | Visibility audit Lemma 1 and (FV) |
| Punctures, modular units, or finite exact terms automatically repair M1 | L3 excludes the specified finite local comparison; M1 survives | §5.7 |
| The midpoint residual might vanish after integration | Its certified interval is strictly positive; this MC completion fails the integrated Mellin identity | §5.7 and the residual interval certificate; other completions not classified by this verdict |
| The intrinsic endpoint-spherical alternative remains untested | Its residual is strictly positive too; both single-vertex Fricke-symmetrized choices fail the integrated Mellin identity | §5.7 endpoint certificate; arbitrary mixtures are outside the two-case class |
| Nonzero curvature of a global scalar jet might yield a nonzero unweighted full-domain pairing | The curvature is exact and has zero cusp flux; the complete area integral vanishes for every moderate-growth scalar jet | §5.7 curvature-area theorem; no Fourier-support hypothesis needed |
| Vanishing of the cusp-to-cusp f-period supplies a relative filling | The relative class maps to the nonzero cusp difference under the homology boundary map | Curvature-area report §2; elliptic image and modular-curve relative class are distinct |
| Both lower half-ray moments vanish | Only the stated even/full-ray identities follow | §5.7 L1 |
| An algebraicity certificate is automatically easier | Under the interval it is equivalent to \(q=36\) | §4; independent input missing |
| A1/A2 establish arithmetic finiteness | They formalize conditional algebra only | §5.2 |
| H41 remained blocked at the old component/multiplicity route | The later mod-4 route closes its retained rank-zero family at its qualified tier | §5.10; abandoned shortcut remains unproved |
| The old explicit descent and actual-point-group bridges never finished | Run013/66b1 retain qualified rank-zero BSD-family assemblies; P01/P03/P04 and Gate-R reach the actual point quotient and rank zero | §5.10; exact family and proof grades retained |
| The Gate-R finiteness consequence is only an uncertified private derivation | The later finiteness freeze certifies `Finite` for the actual rational-point group under Params/H41 | §5.10; does not assert finiteness of Sha |
| The H41 base analytic input remains the open premise of the older Theorem B | The sealed mod-4 successor supplies it on its retained positive/negative branches | §5.10; no extension to all bases or rank-two curves |
| A H9 checkpoint truncated at H9R2 is the complete history | The recorded later revisions and their corrections control their specific statements | §7; no reconstruction from the truncated export |
| The returned MCS check proves a fatal rank-two obstruction to every anticyclotomic Heegner construction | That inference and two claimed missing inputs are rejected; direct seed application still fails a stated conductor hypothesis | [Source review](_work/bridge_repair_assessment_2026-09-21/MCS_RETURN_REVIEW.md); no global arrow established |

Older detailed corrections, including normalization and formalization bookkeeping, remain in [DO_NOT_RESURRECT.md](DO_NOT_RESURRECT.md) as a frozen historical register. Its stale tentative wording does not override the explicit statements here.

## 7. Proof boundaries, contradictions, and coverage

FIN, order nine, and \(q=36\) remain open. The R1/R2 repair supplies a passed source recovery and integral period-comparison subclaim, but its separate hostile review rejects the final R2 μ transfer as written. The bounded normalization cleanup is stopped; the 3-primary theorem is retained via published Skinner Theorem A, with the internal SU interface unreconstructed. The visibility operation gives a written ordinary varying-level coverage deduction and the scoped fixed-level obstructions in §5.11, with no prime-support bound or scalar comparison. The changes are justified by the identified arguments, not by choosing the newest filename.

The following uncertainties remain explicit:

1. The current R1/R2 status is the split verdict in §2. Its separate fresh-context model review does not count as independent human acceptance or formal verification. The unreconstructed internal SU normalization is a recorded provenance limit, not an active cleanup target. The retained preprint/basis, arithmetic-certificate, and published-theorem dependencies remain explicit.
2. The initial reconciliation checked selected statements and dependency directions. The subsequent proof, hostile review, and visibility deduction have the exact scopes stated above. None reruns the large arithmetic certificates, Lean builds, or every proof in the main-conjecture chain. The visibility deduction imports Zhang’s published theorems and is not a new hostile audit of their dependencies. Historical and current model reviews are not independent human acceptance.
3. The raw localization experiment is paused and unsealed. The elementary quotient obstruction is independent; the stronger experimental claims retain their own grade.
4. The older research labels H1–H4 remain unreconstructed here; the recovered “H¹-free bridge” is a different label and does not fill that gap. The H9 source-custody report explicitly warns that local exports are truncated and points to a corrected Drive checkpoint; this operation has not retrieved that live checkpoint. It would be wrong to promote the truncated export to authority.
5. The September 21 coverage check found that the previous discovery rule omitted `Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS` and the unprefixed Gate-R/C1/fixed-E5 records. The existing checker now includes these locations and Run014 historical controls, with exact roots and exclusions in [RECONCILIATION_INVENTORY.json](RECONCILIATION_INVENTORY.json). Mixed archives also contain unrelated records. Discovery is not review: the [coverage reconciliation](_work/historical_coverage_2026-09-21/COVERAGE_RECONCILIATION.md) distinguishes source reading, theorem-signature inspection, filename-only coverage, and untouched material. The 11-primary integration's earlier scoped relevance check remains in [the launch reconciliation](_work/active_full_bsd/p11/LAUNCH_RECONCILIATION.json); its other discovered proofs were not silently admitted as C11 dependencies. Recent messages from the tasks **BSD status audit** and **BSD Project Strategy** were checked in the preceding consolidation; all older task histories and ChatGPT Library were not exhaustively recovered. Compressed archives, personal Documents, and cloud-only material have not all been opened. No claim is made to have read every BSD file on the computer.

The old master files were preserved before modification in the archive identified by the inventory. The original seed theorem record remains byte-for-byte unchanged. Selected evidence identities and the implemented drift checks are recorded in `STATE.json` and `SOURCE_BINDINGS.json`.

## 8. Maintenance and admission

No repair or successor to the stopped FIN mechanisms is launched. The authorized frontier is the exact scalar target in §4; the second-jet decompositions in §5.7 are retained, and both single-vertex Fricke-symmetrized completions have positive residuals. The two-case mechanism is stopped and supplies no arithmetic comparison. The separately authorized curvature-area test is also complete: every global moderate-growth scalar jet has zero full-domain pairing, by the theorem in §5.7. The contemplated elliptic-path extension is stopped because it had no demonstrated route through the first open comparison. The user subsequently authorized autonomous work toward both full-BSD endpoints with persistent checkpoints. That campaign closed the 7-primary component, and the separately authorized local C11 computation has now closed the 11-primary component by the theorem in §2. The C11 run is complete. No stopped construction is revived, no next-prime computation is launched, and these finite-prime results supply no uniform tail theorem. The existing RESUME.md and the [completed p11 checkpoint](_work/active_full_bsd/p11/RESUME.md) give the current operational state; the earlier whole-BSD impasse remains a historical checkpoint in _work/active_full_bsd/WORKING.md.

A later result changes this record only by giving the exact mathematical statement, hypotheses, direction, proof grade, source, and the particular assertion it replaces or qualifies. A contradiction without a resolution remains marked unresolved; it is not silently settled by recency. The before-state is archived and the affected statements here are updated in place. A new report alone is not an integration.

Before any new BSD proposal, check the mechanism against §5 and the historical coverage gaps. State the fixed endpoint, complete implication chain, first unproved arrow, converse, independent new input, previously failed arrow actually changed, and the stopping condition. A sufficient or equivalent reformulation earns no difficulty-reduction credit by itself. A direct whole-group bound is admissible; a prime-partition route must cover every infinite regime and full primary depths. Separate scalar and Sha arguments are admissible, but their exact order-nine assembly cannot be omitted.

The local verifier detects changed bound sources and newly discovered records in its stated scope. It cannot validate new mathematics or ensure that every other task reads this file. There is no automatic cross-task synchronization or claim of exhaustive historical recovery.

**September 21 research planning and returned source check, without a theorem upgrade.** The [source-assisted research plan](_work/bridge_repair_assessment_2026-09-21/RESEARCH_PLAN.md) separates reusable proved premises from the still-open global comparisons. Castella–Sano remains an already-used input to the WC equivalence. The user subsequently supplied the external Macias Castillo–Sano application report. Its broad impossibility reasoning is not retained: the [source review](_work/bridge_repair_assessment_2026-09-21/MCS_RETURN_REVIEW.md) records the exact corrections, actual applicability failure, and reading grade. This correction establishes no global arithmetic arrow and authorizes no successor. The plan's remaining construction requirements are unchanged; FIN, order nine and q=36 retain their existing status.

The report's author subsequently [retracted the incorrect reasons](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/RETRACTION_AND_CORRECTED_VERDICT.md), preserving the original verdict. That retraction now governs the external return. The literal conductor mismatch is not the only task between a possible extension and full BSD; the arithmetic bound, prime coverage, and real comparison remain unestablished, as specified in the source review.

**Scoped nonsquarefree source composition.** The [written application lemma](_work/bridge_repair_assessment_2026-09-21/MCS_NONSQUAREFREE_JOIN.md) combines BCK Theorem A, Kataoka–Sano Proposition 5.12, the general MCS determinant comparison, and the retained local calculations. For good ordinary primes \(p\ge5\), \(p\notin\{19,59,487\}\), with \(p\nmid\#\widetilde E(\mathbf F_p)\), it gives the base-layer Heegner Stark-system basis and classical Selmer Fitting-ideal identities at every primary depth over a suitable imaginary quadratic field. This is a written source composition at retained grades, not a direct application of the printed squarefree theorem, independent proof review, new primary vanishing, or global difficulty reduction. The arithmetic ideals are unevaluated. The exclusions do not bound Sha support; FIN, order nine, and q=36 remain open.

The [returned join audit](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/JOIN_AUDIT_AND_NEXT_QUESTION.md) supports the conductor-use and residual-image arguments at partial external-model-review grade. Its next proposal is qualified by the [derived-height and quotient deductions](_work/bridge_repair_assessment_2026-09-21/MCS_DERIVED_HEIGHT_GATE.md): the nonzero Heegner tower class has finite augmentation depth, but its divided specialization lifts to the full tower and is killed by every derived Bockstein. Pairing that class does not evaluate a leading coefficient; this does not exclude heights on other Selmer directions. If a suitable quadratic twist is rigorously certified to have analytic rank one, then the known rank-three point contribution gives
\[
\operatorname{Fitt}^{\,i}_{\mathbf Z/p^n}
 \bigl(\Sha(E/K)[p^n]^*\bigr)=I_{i+3}(\epsilon^{\rm Hg}_{n,0}).
\]
This is a proved conditional algebraic deduction from the join, not an evaluated ideal, a new Sha bound, or a strict difficulty reduction. That audit did not certify a twist. The completed D=-23 certificate below now supplies this premise for K=Q(sqrt(-23)), while leaving the ideal unevaluated. The compact Selmer group may still contain \(T_p\Sha\); its rank is not identified with the point rank. All original source dependencies remain load-bearing. The audit is preserved unchanged, no successor is launched, and the global endpoints are unchanged.

The audit's author has [accepted the derived-height correction](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/DERIVED_HEIGHT_CORRECTION_ACCEPTED.md) and withdrawn that proposed computation. The acceptance governs the old proposal together with the two wording clarifications in the existing height review, §5. No independent ideal evaluation or new mathematical result is supplied by this acceptance.

The subsequent [twist-and-ideal review](_work/bridge_repair_assessment_2026-09-21/MCS_TWIST_IDEAL_REVIEW.md) verifies the candidate discriminants but corrects the returned costing: 8,444,396 was the old prime-coefficient count, not its 150,000,000 summation cutoff. Scaling that cutoff to \(D=-23\) gives 3.45 billion, already covered by the retained C11 corpus; the relevant 206-segment prefix passed a fresh hash check. That review supplied no derivative enclosure or adequate-cutoff certificate; this numerical gap is superseded by the completed D=-23 computation below. The review derives the derivative series and a tail bound, proves the fixed finite twist-family exclusion with density \(2^{-r}\) for character rank \(r\), and supplies an abstract perfect-complex counterexample to determining specialized Fitting ideals from the Heegner index/characteristic ideal alone. These do not invalidate (J), exclude varying-\(K\) arguments, or establish an arithmetic ideal evaluation. No global endpoint changes or successor starts.

**Latest Aristotle archive comparison.** The [A6/B3 review](_work/aristotle_latest_pair_2026-09-21/REVIEW.md) records new content beyond the previously supplied A5/B2 archives. A6 formally checks the known ordinary reduction at 13, with point count 18 and trace \(-4\), but supplies no \(C_{13}\). B3 supplies a separate C11 numerical implementation and Lean finite assembly: all 45 required symbols and all 110 supplied denominator-121 values match the certified local table; replay of its captured buckets agrees after the documented sign conversion. This is additional corroboration, not a second primary closure or a new independently rigorous numerical certificate. The full large numerical run and Lean builds were not replayed here. Numerical-tail, floating-error, and custody limitations are in the review. No global endpoint or threshold changes.

**D=-23 feasibility return, corrected.** The [source-level review](_work/bridge_repair_assessment_2026-09-21/D23_FEASIBILITY_REVIEW.md) reproduces the reported tail values but rejects the inference that the 3.45-billion cutoff is inadequate: adequacy depends on the uncomputed truncated ball, and seven billion is likewise not yet certified adequate. The recorded C11 Stage A timings are real, but that stage already uses Arb balls, not modular-integer accumulation. Its source already constructs E1 Taylor coefficients; a twisted first-derivative mode remains to be adapted and benchmarked. The old dense derivative mode would require about 28 GB at seven billion, so the table-free C11 traversal is the relevant reusable component. A one-billion floating scout has an available rigorous tail bound around 5548 and can supply only heuristic scale information. The original return is preserved with these claim-specific corrections. No sum, benchmark, new engine or arithmetic result is supplied; no successor is launched.

**D=-23 certified execution, completed (September 21).** The isolated table-free [computation and certificate](_work/d23_twist_2026-09-21/RESULT.md) give
\[
\boxed{39.512236\le L'(E^{-23},1)\le40.182321.}
\]
The root number is -1, so the twist has analytic rank exactly one. The retained Gross–Zagier–Kolyvagin rank-one theorem and seed rank theorem therefore give rank E^{-23}(Q)=1 and rank E(Q(sqrt(-23)))=3. This supplies the suitable certified rank-one twist premise in the preceding Fitting-ideal shift. The [proof and precise dependencies](_work/d23_twist_2026-09-21/PROOF.md) verify that this K also satisfies the recorded splitting conditions at p=13. Under the retained source-composition hypotheses and grades, the displayed shift by three now applies to this actual K. No Stark ideal is evaluated, no additional seed primary component is settled, and FIN, ORDER9 and Q36 remain open. Finiteness of Sha of the rank-one twist does not imply finiteness for the seed or for E/K.

The initial cutoff T=3,456,106,495 sufficed: the finite sum is enclosed by 39.847278312318874 +/- 4.28e-16, including finite Arb and Taylor errors, and the infinite tail is at most 0.335041797049. The [completion review](_work/d23_twist_2026-09-21/COMPLETION_REVIEW.json) verifies all 1,030 unit identities, 206 freshly rehashed coefficient segments, the exact coverage count, independent first-segment counts and identical fresh recombination. The main run measured 708.40 seconds and 1,004,609,536 bytes peak resident memory. No seven-billion extension was run. This is a computer-assisted certificate with the explicitly inherited coefficient, software and theorem trust base, not a Lean proof, fresh replay of all prime witnesses, independent human review or second full numerical implementation. The sealed source engine and corpus remain unchanged. The [completed checkpoint](_work/d23_twist_2026-09-21/STATE.json) and [restart instructions](_work/d23_twist_2026-09-21/RESUME.md) preserve the run. The external Aristotle host has 32 GB per the user; this implementation is table-free. No successor is launched.

**D=-23 applicability through 160, checked.** The [bounded coverage review](_work/bridge_repair_assessment_2026-09-21/D23_COVERAGE_REVIEW.md) confirms that the certified field serves exactly p=13,31,41,47,71,73,101,127,139,151 among primes 5 through 160 under regime (P). Independent point counts at all 35 good primes in that range agree with the freshly hash-checked corpus. In particular p=13 has a13=-4, point count 18 and splitting character +1. This is verified applicability of the existing comparison, not an ideal evaluation or new primary closure. The unit-ideal test concerns Sha(E/K)[13], including the twist contribution; finiteness of the twist's Sha supplies no 13-primary vanishing. At this coverage checkpoint the conditional threshold was 1521; the subsequent C13 completion below raises it to2601. FIN, ORDER9 and Q36 remain open. The returned external checkpoint's stale launch fields are superseded by the completed local certificate; no restart or successor is launched.

**C13 evaluation gate, September 21.** In response to the request for the next operation, the [checked specialization and resource gate](_work/bridge_repair_assessment_2026-09-21/P13_EVALUATION_GATE.md) establish that the completed 7/11 cyclotomic method applies at 13: a unit quadratic coefficient would imply seed 13-primary vanishing using the retained source and regulator-integrality arguments. Two exact weight derivations agree on a predeclared 66-symbol functional. The unchanged engine's Arb cutoff routine gives T=55,046,045,695 at denominator169 and T=4,026,531,839 at denominator13. The current corpus supplies 2,333 of the 3,281 required segments; 948 additional segments require certified generation. No modular-symbol run, new coefficient generation, C13 value, primary theorem or threshold change is supplied by this gate. This is a justified finite arithmetic operation with an existing method; it gives no uniform-tail conclusion. A zero residue would leave the sufficient test inconclusive. The new external scope note correctly decomposes Sha over K; its Heegner-index suggestion is one possible method, not a necessity. The direct C13 operation avoids the twist-primary obligation without identifying C13 with I3.


**Completed C13 computation and normalization, September 21.** The [13-primary theorem](audits/P13_PRIMARY_THEOREM.md) supplies the gate's missing numerical premise: C13=2 modulo13 in omega1, or1 in the full real period. The exact group sums give -3950; the independent full depth-two measure agrees, and the same downstream implementation reproduces the retained 7/11 results. All179 exact checks pass. The returned 7/8 residues are explained by lattice-numerator scaling and omission of alpha^-2 in the alternative weights; the predeclared formula is unchanged. This review checked all3,281 coefficient/verifier files, the948 new witness receipts and bytes, and all17,605 saved Arb units, then reproduced both interval outputs and symbol tables byte for byte. The prior write-through incident is preserved: all2,333 reused contents match their pre-incident hashes, but they were not historically untouched. No fresh full integer-verifier replay or independent numerical implementation is claimed. Kato divisibility and canonical-height integrality now prove G[13^infinity]=0 with the retained source and computational qualifications. The conditional next-order threshold is2601; this does not supply FIN, ORDER9, Q36, twist-primary vanishing or I3 evaluation. The external run's historical RESULT/STATE/RESUME files and the earlier gate remain preserved; this completion supersedes only their missing-result, unresolved-normalization and pending-execution claims. The run is complete, and no successor is active.
