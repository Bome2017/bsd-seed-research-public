# Repairability of the existing BSD bridges

2026-09-21. Focused response to the request to inspect the bridges more deeply. This is supporting evidence for the existing master, not a replacement status map. No new arithmetic run, subagent, or literature survey was used. Historical written proofs retain their existing grades; reading their final corrections is not an independent replay of all their dependencies.

**Finding:** real bridges were built. Some reached their stated endpoint; others reached an analytic or geometric intermediate object. The inspected records do not contain a nearly completed proof of global FIN or the real leading-term formula that can be finished by normalization or formal bookkeeping. They do contain a direct corollary that supplies Kummer membership at the already settled primes, and later corrections that withdraw several overbroad negative claims.

## 1. A consequence that can be proved now

Let E be the fixed curve, let P1,P2 be its retained saturated Mordell–Weil basis, and put

\[
S_p=\left(\varprojlim_n\operatorname{Sel}_{p^n}(E/\mathbf Q)\right)
       \otimes_{\mathbf Z_p}\mathbf Q_p,
\qquad W_p=\delta_p(E(\mathbf Q)\otimes\mathbf Q_p).
\]

Here the Selmer groups have the usual local Kummer conditions. This qualification matters: the statement does not automatically apply to a class in a different modified Selmer group.

**Corollary, at the grade of the retained primary inputs.**

1. For p in {2,3,5,7,11}, S_p=W_p and this vector space has basis delta_p(P1), delta_p(P2).
2. For p in {5,7,11} and every n>=1, the Kummer map gives
   \[
   \operatorname{Sel}_{p^n}(E/\mathbf Q)
   =\delta_{p^n}(E(\mathbf Q)/p^nE(\mathbf Q))
   \simeq(\mathbf Z/p^n)^2.
   \]
3. At these three good primes, define S_p^str as the kernel of localization to the usual local Kummer space at p. Then
   \[
   S_p^{\rm str}=\mathbf Q_p\bigl(
   \log_p(P_2)\delta_p(P_1)-\log_p(P_1)\delta_p(P_2)\bigr).
   \]
   The logarithm uses the fixed invariant differential; rescaling it does not change the line.

**Proof.** The global Kummer exact sequence with local Kummer conditions is
\[
0\longrightarrow E(\mathbf Q)/p^nE(\mathbf Q)
\longrightarrow\operatorname{Sel}_{p^n}(E/\mathbf Q)
\longrightarrow\Sha(E/\mathbf Q)[p^n]\longrightarrow0.
\]
Taking inverse limits is exact here because the left-hand transition maps are surjective. Tensoring with Q_p gives
\[
0\longrightarrow E(\mathbf Q)\otimes\mathbf Q_p
\longrightarrow S_p\longrightarrow T_p\Sha\otimes\mathbf Q_p\longrightarrow0.
\]
If the p-primary group is finite, its Tate module is zero: a coherent sequence x_n satisfies x_n=p^k x_{n+k}=0 once p^k kills that group. All five retained primary groups are finite. This proves (1). At p=5,7,11 the groups themselves vanish, so the finite-level sequence proves (2); the rational torsion has order two and contributes nothing at these odd primes.

At a good prime, the elliptic logarithm identifies E(Q_p) tensor Q_p with the one-dimensional space Q_p. Its kernel on E(Q_p) is torsion: multiply into a sufficiently small formal subgroup on which logarithm is injective. A nontorsion rational point remains nontorsion over Q_p. Thus localization on the two-dimensional rational Kummer space is the nonzero linear functional (a,b) -> a log_p(P1)+b log_p(P2). Its kernel is precisely the displayed line. This proves (3).

**Exact effect.** Every independently constructed class already known to belong to S_p is a rational-point Kummer class at these primes. If it is strict, it lies on the displayed line. This does not prove that a proposed class is defined, satisfies these local conditions, is nonzero, or comes from the sealed geometric tower. The p=5 calibration already used this reasoning; including 7 and 11 integrates the later arithmetic inputs. This is a standard consequence, not new FIN progress. The p=3 case, where the finite Sha group has order nine but its Tate module is zero, also shows why rational Kummer membership cannot recover finite primary orders.

Dependencies: [current primary inputs](../../MASTER_BSD_DAG.md), [11-primary theorem](../../audits/P11_PRIMARY_THEOREM.md), and the elementary exact-sequence argument just given.

## 2. H9: what was actually completed, and what a repair would have to change

The [sealed H9R16-C milestone](/Users/bsm/H9R16C_SEALED_MILESTONE_2026-09-15/00_MILESTONE.md) retains an integral, correctly typed point-tower compatibility, with constant exactly one:
\[
\tau_r^{MW}(Q_{r+1})\circ(1\otimes N_{r+1,r})=\pi_r^*(Q_r).
\]
The compatible Hom-valued Jacobian points and finite Kummer compatibility are genuine completed objects at their recorded model-audit tier. The [sealed nonclaims](/Users/bsm/H9R16C_SEALED_MILESTONE_2026-09-15/05_NON_CLAIMS.md) explicitly exclude descent to E(Q), non-torsion, and the target big-trace application. Later weighted-reciprocity work must be read beyond that older file; the original parity objection is not the entire subsequent history.

The [seed calibration, section 3c](/Users/bsm/SEED_2243_12_MECHANISM_LANES_2026-09-18/00_LANE1_SYNTHESIS.md) identifies a sharper failure: the retained same-root/CH branch misses the desired nonzero strict line, and its Galois-compatible E(Q)-component is zero. Multiplying a zero specialization by a scalar cannot produce the required nonzero class.

The [derived-point gate](/Users/bsm/H9R19_WEIGHTED_RECIPROCITY_2026-09-15/20_DERIVED_POINT_GATE.md) checks the proposed repair. The sealed family has only the retained Hida direction and a collapsed g/h carrier; the proposed derivative needs a transverse f-weight direction and a different geometric family. An extra formal variable is not that family. The exceptional-zero hypothesis used in the proposed argument also differs from the seed's good-ordinary situation.

Consequently, source verification and auxiliary twist computations could finish parts of the conditional Castella/CH *calibration*. They would not make the sealed branch nonzero, nor supply the absent transverse geometric construction. The corollary above closes rational Kummer membership wherever the ordinary Selmer hypotheses already hold; it does not repair these geometric failures.

The [later coefficient check](/Users/bsm/H9R19_WEIGHTED_RECIPROCITY_2026-09-15/31_COEFFICIENT_GATE_SOURCE_CHECK.md) and [ABC correction](/Users/bsm/H9R19_WEIGHTED_RECIPROCITY_2026-09-15/32_ABC_NEW_MECHANISM_KILL_GATES.md) also matter. They withdraw blanket claims about all possible comparisons, primitive systems, and odd-prime families. The surviving status is a stopped construction and an open arithmetic target, not a theorem that every H9-type approach is impossible.

## 3. A later analytic bridge must also be preserved

The RS2 records went beyond the original weighted Mellin identity. Their normalized cross-cusp construction records
\[
\langle\widetilde A_2,f\rangle
=\widetilde\kappa_N L(f,2)L''(f,1),\qquad
\widetilde\kappa_N=
-\frac{\prod_{p\parallel N}(1-a_p/p)}
{2(2\pi)^3\prod_{p\mid N}(1-p^{-2})}\ne0.
\]

The governing [archive correction](/Users/bsm/BSD_FABLE_RS2_L3_2026-09-20/ARCHIVE_NOTE.md) grades this **written derivation with one source-custody seam**, concerning the cross-cusp Fourier normalization. This assessment does not upgrade it to source-closed or independently verified. The [normalized calculation](/Users/bsm/BSD_FABLE_RS2_NORMALIZED_A2_2026-09-20/RS2_NORMALIZED_A2_VERDICT.md) gives the formula; the [later L3 report](/Users/bsm/BSD_FABLE_RS2_L3_2026-09-20/RS2_L3_VERDICT.md) corrects the sparsity modulus to 18188 and leaves the required shifted-divisor continuation open.

Two different missing steps must not be combined:

* The analytic step is to justify the specified weight-two, level-N Poincare unfolding and continuation, with the required shifted-divisor kernel, at the target parameter. This is a definite mathematical problem, not refuted by the record. Its difficulty and novelty were asserted by the earlier report, not established by a completed proof here.
* The arithmetic step is a comparison with the real Neron–Tate regulator. The analytic continuation does not itself furnish one.

For precision, even grant the pairing formula and write the orthogonal f-component of the cuspidal projection as c_f f. Pure algebra then gives
\[
q=\frac{c_f\langle f,f\rangle}
{2\widetilde\kappa_N L(f,2)\Omega_E R}.
\]
Thus merely proving algebraicity of c_f would not establish controlled algebraicity of q without further control of the displayed period/regulator ratio. This is an explanation of the remaining obligation, not a new proposed invariant.

The archive explicitly withdraws the claim that the route was run to mathematical impossibility: Task 3 was never proved. Its actual conclusion is that no independent arithmetic successor was identified. Completing the analytic lemma could be worthwhile as analysis; the inspected files do not justify describing that assignment to Aristotle as a demonstrated route to full BSD. The stopped arithmetic follow-up remains stopped.

## 4. The other repair candidates

| Existing item | What can be repaired or extended | Exact endpoint limit |
|---|---|---|
| Finite-prime Iwasawa computation | The C11 missing input was supplied locally and the arithmetic argument completed. The same established procedure can be tested at another eligible fixed prime with a new certificate. | A successful next-prime result removes one primary component; it supplies no uniform tail or real comparison. No next-prime run is started here. |
| BKS/unit normalization | A further source audit might settle the precise comparison between height conventions. | Lemma U is a unit statement; one congruence or a convention match does not prove the real leading-term formula or force a unit to equal one. |
| Rank-two bridge design | It explicitly identifies the absent real comparison. | Its use of order nine is an assumption, not an output. FIN alone does not provide order nine. “Design complete” never meant its central comparison theorem was proved. |
| LINE/WC and support bounds | An independent uniform arithmetic estimate could change the situation. | Their written implications/equivalences do not provide that estimate. Re-formalizing them does not supply the missing hypothesis. |

Evidence for the middle two rows: [rank-two design](/Users/bsm/BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/R2_LEADING_TERM_BRIDGE_DESIGN.md), [unit/normalization audit](/Users/bsm/BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/LEMMA_U_AND_P5_UNIT_AUDIT.md). The separate R1/R2 cleanup remains stopped at the published-theorem dependency recorded in master section 2; this assessment does not reopen it.

## 5. What to ask Aristotle to do

The corollary in section 1 is ready for formalization with the retained primary results as explicit imported hypotheses. That would check its deduction; it would not independently verify the large numerical certificates or prove a new primary result. The proof is short enough that a substantial new Aristotle run solely for it is not warranted for the full-BSD objective.

The H9 wrong-branch problem requires an actual new geometric construction and nonvanishing argument. RS2's analytic gap has a definite statement but no established downstream regulator comparison. Neither should be advertised as a nearly finished BSD bridge merely because the gap now has a name.

No presently evidenced near-finished global repair was found in these inspected chains. This is a scoped assessment of the retained arguments, not a nonexistence theorem or an assertion that new mathematics cannot be developed. The useful repair made here is to carry completed arithmetic into its exact Selmer consequences and to preserve both the completed bridges and the later withdrawals of overbroad rejection claims.

FIN, total order nine, and q=36 remain open. No successor operation is launched.
