# Explaining the measured valuations with integral main-conjecture theorems

2026-10-13. Baseline: `f97843a1b4768606787a9760ea4bad727a3dc4a1`.

**VALUATION_EXPLANATION_SOURCE_MATCHED; POSITIVE_CONTROL_SHA5_EXACT_DERIVED; SEED17_NUMERATOR_VALUATION_INFERRED_FROM_OLD_SHA17.**

The contrasting experiments have a theorem-backed explanation at the level of valuations. Combining an applicable integral ordinary main-conjecture theorem with the algebraic leading-term theorem gives

\[
 v_p\left(\frac{L_{2,p}\,|C(\mathbf Q)_{\rm tors}|^2}
 {(1-\alpha_p^{-1})^2\det H_U\prod_v c_v(C)}\right)
 =\operatorname{length}_{\mathbf Z_p}\Sha(C/\mathbf Q)[p^\infty].
\]

The precise hypotheses, finiteness implication and normalization are in [PROOF.md](PROOF.md). This is a composition of established theorems, not a newly invented empirical identity. The arithmetic inputs remain at their retained grades, and the new application requires independent review.

## 1. Both kinds of controls are covered

For the irreducible controls, Burungale--Castella--Skinner Theorem 1.1.2 applies. Exact small point-count witnesses and a multiplicative prime of discriminant valuation one verify its two relevant hypotheses. Both residual height configurations are admitted; no unit-regulator or line-coincidence condition is imposed.

For the positive control F (the d=43737 twist in the prior experiment), Castella--Grossi--Skinner Theorem A applies instead. Its residual characters are chi_d and omega*chi_d. At 5, chi_d is unramified with Frobenius -1 because 43737=2 mod5. Thus neither character is locally 1 or omega, exactly as required. The theorem applies at rank two; its separate classical-BSD corollary for ranks zero and one is not used.

The old positive-control coefficient has exact valuation two, its U-regulator is a unit, and all relevant local/torsion factors are units. The derived conclusion is therefore

\[
\boxed{\Sha(F/\mathbf Q)[5^\infty]\simeq(\mathbf Z/5\mathbf Z)^2.}
\]

Primary finiteness comes from the algebraic leading-term theorem after the nonzero quadratic coefficient gives order exactly two. The previously independent isogeny-Selmer lower bound then determines the group structure from its order 25. This does not establish finiteness or order of the full Sha(F).

## 2. A seed application without pretending to compute a new digit

The seed's retained all-prime residual theorem and multiplicative prime 2243 give the integral ordinary main conjecture at every good ordinary p>=5. After the p-unit finite local factors are removed, the displayed equality becomes

\[
 v_p(L_{2,p})-v_p(\det H_U)=\operatorname{length}\Sha(E/\mathbf Q)[p^\infty]
\]

on the nonzero quadratic-coefficient branch. The converse branch is available once primary finiteness and height nondegeneracy are known.

At 17, both converse inputs already exist independently of the cyclotomic numerator: the certified Ota witness at 103 gives Sha[17^infinity]=0, and the retained matched regulator has valuation one. Hence

\[
\boxed{L_{2,17}\ne0,\qquad v_{17}(L_{2,17})=1.}
\]

This is a new written inference from old inputs. No leading residue of L_2,17/17 was evaluated. Since the proof uses the existing Sha17 certificate, it is not a new independent proof of that certificate and does not settle another prime.

On the smaller domain of the earlier defect identity, comparison also sets its e_p to zero for the newly matched ordinary source in the nonzero branch. Arbitrarily rescaled or unmatched Kato classes are not covered by that conclusion.

## 3. What this explains, and what it does not

The shared regulator contribution and the surviving arithmetic contribution are not separated by the incidence of two residual height lines. They are separated by the algebraic leading-term theorem, with the integral main conjecture matching the independently defined analytic and Selmer series. The same mechanism accommodates the cancelling controls, the positive control, and the seed's representation.

It determines valuations only. The observed congruences Q_p=1+O(p^k) or Q_5=25+O(125) do not become exact unit identities. No p-adic rational recognition or complex BSD equality is used.

**This is not yet the independently computable new seed predictor requested by the discovery program.** The remaining scalar is identified with actual Sha length; its value is not determined for the unresolved seed primes. A relation whose right side is the unknown Sha group is an explanation, not an independent upper bound.

Thus this return supplies a specific exact primary result for the positive control and a seed17 valuation inference, but no cofinite estimate. FIN, ORDER9, Q36, supersingular coverage and new seed-prime coverage remain unchanged.

## 4. Verification and publication scope

The [checker](checks/verify.py) executes six small irreducibility/ordinary/Tate-inertia input screens, reconstructs the exact rational order-five base point, checks the local quadratic character, rechecks four leading valuation/unit comparisons from retained digits, and verifies precision boundaries. Its [output](checks/RESULTS.json) is deterministic. It does not verify the main-conjecture proofs, ranks, saturation, historical modular-symbol producers, or the old Ota certificate end to end.

Primary theorem statements were read in full-source text; the relevant BCS, CGS and Stein--Wuthrich theorem pages were visually inspected. No external mathematical reviewer, formal proof assistant, new coefficient producer, broad prime scan or production job was used.

This is an additive standalone review-branch return. No active endpoint ledger, frozen return, main branch or expert-review repository is promoted by its publication. Source details and retained hypotheses are in [SOURCES.md](SOURCES.md) and [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json). Hashes authenticate files, not theorem correctness.
