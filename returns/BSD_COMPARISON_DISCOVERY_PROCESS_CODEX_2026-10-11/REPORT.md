# Discovering the arithmetic comparison for the BSD seed

Date: 2026-10-11. Lab baseline: `0d107bb0fa3356a7d20b007528251b7898b60f18`.

**Status: DISCOVERY_PROCESS_SPECIFIED; NO_NEW_COMPARISON_OR_BOUND.**

The user's question is how to discover a construction, rather than repeatedly request the missing theorem. This brief specifies a feedback process and its first experiment. It is a research design, not a theorem, a numerical result, or authorization for a production campaign. Two model agents examined the design and the existing pilot's feasibility; this is not independent mathematical certification.

## 1. What we are trying to make

For the actual smoothed, transported Kato derivative, retain

\[
\delta_p=A_p\kappa(P_1)+B_p\kappa(P_2),\qquad
m_p=\min\{v_p(A_p),v_p(B_p)\},\qquad
w_p=\min_i v_p(\log_\omega(P_i)/p).
\]

The retained written theorem says that nonzero delta gives primary finiteness and

\[
\operatorname{length}\Sha[p^\infty]\le m_p-w_p.
\]

Parity makes `delta != 0 and m_p-w_p <= 1` a sufficient primary-vanishing criterion on its stated domain. A proof outside one fixed finite set would settle the corresponding uniform tail. The exceptional primes, ORDER9, and Q36 remain separate.

A comparison is useful here if it lets independently controlled arithmetic bound this actual content. An equality with a second uncontrolled quantity would not finish that job. Full equality of global classes is not mandatory: a controlled integral image or an inequality with a proved error bound can suffice. Nor is a fixed rational scalar mandatory; a genuinely uniform estimate of the p-dependent corrected content is admissible.

## 2. Start by learning the required shape of a map

The latest constructions have different types:

| Existing object | Actual type | What is not supplied |
| --- | --- | --- |
| Shii/DI signed theta | Scalar group-ring element from unraised definite Gross points; currently an inert supersingular domain | Identification with the seed Kato derivative, or control of the surviving finite specialization error |
| Repaired Lubin–Tate period source | Local cohomology for a specified rank-one CM coefficient representation | A global E-valued class or a projection to the non-CM seed |
| Corrected CM map on the raised curve | Cohomology-valued finite-field Kummer map, retaining its coefficient line | Mixed-place arithmetic comparison and its absolute integral content |
| Kato derivative | Global E-valued cohomology in the full integral point plane | An independent bound on its two-coordinate content |

Shii already has a Selmer connection through a product/Fitting inclusion. The deficiency is its strength after specialization, not absence of any Selmer connection. The existing finite-error control shows why a quadratic theta unit alone is insufficient.

For each candidate record its response to changing a point basis, Galois conjugation, a Hecke correspondence, a conductor norm, a differential, and a smoothing parameter. Derive these rules from its construction before fitting a formula.

An elementary useful check is basis covariance. If the row of basis points changes by `P'=PM`, then

\[
a'=M^{-1}a,\qquad \ell'=M^t\ell,\qquad H'=M^tHM,
\]

where `a=(A,B)^t`, `ell=(log P1,log P2)^t` and H is a matched height matrix. A scalar theta value does not transform as the two coordinates a. The retained equation `Ha=epsilon K ell` has compatible covariance. This does not prove a new comparison, but prevents experiments on an incorrectly typed equality. For `M in GL_2(Z_p)`, both m and w are invariant. No height matrix is inverted if it is singular.

## 3. Construct a common source, rather than declare two outputs equal

The positive discovery question is: **what information discarded on passing to scalar theta values must be retained so that their defining arithmetic relations become relations between genuine Kummer classes in one specified representation?** This directs attention to the lost coefficient line, divisor degree, orientation, component data and integral congruence index. It does not assume those data are enough; their defects must be computed.

The concrete starting point is the existing raised CM-divisor construction. On its actual Shimura curve it already supplies

\[
q_m(D)=c_q^{-1}\operatorname{Kum}_I([(T_q-q-1)D]),
\qquad c_q=-\#E(\mathbf F_q),
\]

under the recorded unit and Hecke-quotient hypotheses. This specifies a geometric scale before taking a CM sum. The resulting CM-sum/localization identity is already in the record and must not be counted again as the discovery.

The first construction question is whether an actual correspondence, cohomology boundary, or trace from a specified arithmetic object provides the other realization with the required transformation rules. Write the candidate realization before passing to the quotient, and apply it to each defining arithmetic relation. A nonzero relation image is a concrete failure to descend. Try to identify and construct the genuine geometric term accounting for it, then retest the same relation. The rules in Section 2 narrow which operations can work: a missing dual, involution, exterior power, or Euler factor should be justified by a measured mismatch. They are not permission to add arbitrary factors or a formal quotient that merely kills the error by definition.

Do not assume the unraised definite Gross-point set and the raised indefinite curve share a divisor module. A correspondence between them is part of the problem. Do not invent a characteristic-zero map from the raised Jacobian to E: the retained reduction argument excludes that particular map. Work with the established finite-coefficient quotient where appropriate, and keep its global representation identification common to both local places.

## 4. Make discrepancies into the experimental data

Choose one small model retaining the structures being compared. Construct the maps themselves before collecting many endpoint values. The proposed first experiment is detailed in [FIRST_EXPERIMENT.md](FIRST_EXPERIMENT.md).

On several genuine arithmetic inputs, compare the two realizations after applying only independently justified identifications. Vary one input at a time: the divisor, a conductor step, a permissible Hecke operator, an auxiliary place, or a basis. Preserve both outputs and all factors, including valuations and zeros.

If two maps A and B with a common source and compatible coefficient modules have actually been constructed, a division-free proportionality diagnostic is

\[
W(x,y)=A(x)\otimes B(y)-A(y)\otimes B(x).
\]

This is only a diagnostic. If rank-one multiplicity already forces W=0, its vanishing is not new arithmetic. If W is nonzero, examine its behavior under the same operations; it may indicate that the correct comparison is bilinear, contains a boundary term, or uses a different quotient. Do not force a scalar fit. If only one realization is constructible, the output must identify its actual missing map, rather than fill the second column with BSD-predicted values.

The useful data are exact defects and their transformation laws, not just repeated numerical ratios. A discrepancy supported in a known local term suggests a correction to calculate. A discrepancy carrying an uncontrolled global class requires a new arithmetic argument. Discovering which occurs is the purpose of the experiment.

## 5. Let a failed identity produce a smaller lemma

Write a candidate formula only after identifying a mechanism for its terms. Then ask where the discrepancy lives and what operation detects it. Possible next lemmas include:

- the discrepancy factors through an explicit component group whose order is known;
- the two conductor recurrences agree after one explicitly computed Euler correction;
- a boundary term is the regulator realization of the two known point directions;
- a comparison cokernel has an independently bounded index.

These are alternative outcomes to investigate, not assertions that any holds here. Select the outcome from actual calculations and geometry. Test it on a held-out auxiliary choice and a second suitable curve. Include a case with nontrivial residual Selmer behavior when independently certified data are available; otherwise a formula that only works after Sha has been assumed zero can pass unnoticed.

The proof then has to explain the identity on actual arithmetic generators, show that it respects their relations and local conditions, and control the kernel or cokernel. Formal symbols, agreement at finitely many characters, or a local multiplicity-one statement alone do not provide that control.

## 6. Make the result address content, and then vary p

A useful one-sided comparison can be weaker than a full class identity. For example, for an explicitly defined integral functional

\[
L_p(a)=r_{1,p}A_p+r_{2,p}B_p,\qquad
c_p=\min_i v_p(r_{i,p}),
\]

one has `v_p(L_p(a)) >= m_p+c_p`. Hence a proved nonzero value and the bound

\[
v_p(L_p(a))-c_p-w_p\le1
\]

would suffice. This elementary observation is not a new seed result. It identifies a smaller possible deliverable: one source-matched, independently controlled scalar measurement may be enough. An arbitrary fitted functional or a hidden p-dependent denominator is not enough.

After a local or fixed-p comparison is discovered, vary p and retain the same geometric recipe. Determine whether every correction is supported on a fixed integer, or whether its valuation can be bounded uniformly together with the other terms. Constancy as an auxiliary prime varies at fixed p does not establish this. A mod-p identification does not extend automatically to mod-p².

Finally prove nonvanishing and the content estimate for the specified source, with all finite specialization errors retained. If the result covers only inert supersingular primes, record that domain and identify what construction covers its complement. A subset of primes is not a cofinite tail.

## 7. What changes in the work assignment

The next assignment is: **construct one pair of compatible arithmetic realizations on a justified common source, calculate their exact discrepancy, and use its transformation law to formulate and test the smallest new comparison lemma.** If a map cannot be built, work on its concrete geometric definition; if a defect is found, try the correction its structure suggests. Do not return merely “comparison open,” and do not continue generating examples that are forced by a previously proved rank-one statement.

The latest `0d107bb0` cross-check is incorporated as a design constraint, not imported wholesale as a theorem: the OpenAI detector, G2 primes, and positive-sign BD primes have different odd-p Frobenius regimes. Their detector formulas are not interchangeable. The newer Shii and local-period results are separate constructions; the negative OpenAI source screen does not universally rule them out.

This process gives experiments capable of changing the proposed construction. It does not promise that the needed arithmetic map exists, or that finding it alone supplies nonvanishing. **No new comparison, seed value, or upper estimate has been obtained in this design turn. FIN, ORDER9 and Q36 are unchanged.**

## Inputs and reading scope

The bound, matched height equation, CM map, signed-source and local-period claims above retain the grades of their cited project proofs. They have not been independently re-certified here. `INPUT_BINDINGS.json` records hashes and reading scope. Relevant primary source interfaces include [Shii's finite-level work](https://arxiv.org/html/2503.09034v1) and [Sano–Venjakob's local regulator work](https://arxiv.org/html/2412.12429v1); they do not assert the proposed global comparison. The added covariance and functional inequalities are elementary design calculations, not claims of literature novelty.
