# Direct BSD family 002: seed applicability and extractable inputs

Date: 2026-10-11. Source pin: `openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

## Verdict

**RELEVANT_METHODS_FOUND; NO_RANK_TWO_BSD_THEOREM_IMPORTED.**

The three principal papers concern full Selmer corank zero or one. Their main theorems cannot be applied directly to the retained rank-two seed, at any coefficient prime. This is a hypothesis mismatch established by the Kummer injection, not a criticism of the correctness of those papers and not a rejection of rank-two extensions of their methods.

There are concrete, separately addressable intermediate inputs: an integral high-character division lemma, derived finite models retaining torsion and operations, full-level Kato normalization, an exact rank-one tame logarithmic comparison, and a horizontal-divisor exclusion architecture. The division and finite-model statements do not have a rank-one hypothesis in their own formulations. The manuscript's arithmetic residual/central acyclicity argument does, at identifiable steps. None was promoted here to an accepted external theorem.

## Files and custody

All three READMEs, main/preamble/reference files, and all sections were retrieved from pinned raw GitHub URLs, using the GitHub contents API for directory discovery. Files are in `sources/direct/`. `SOURCE_BINDINGS.json` records each file, exact URL, SHA-256 and byte count. No PDF rendering or Lean verification was undertaken. The relevant source portions below were read; retrieval of every section is not a claim that every proof line was audited.

The repository README explicitly says these are internal-model outputs at differing verification stages and some unformalized results may have issues. Family 002 is not marked with a Lean link in the displayed catalogue. This is not proof that no supporting Lean artifact exists elsewhere; it is a reason not to call the family machine-certified without an exact theorem-to-artifact match.

The exact-BSD README says its October 7 version removes an obsolete supporting citation and updates companion citations. The converse and two-primary READMEs also record updated companion references. Historical versions must not replace the pinned current sources silently.

## Historical collision check: these are not newly discovered routes

After the initial source screen, the parent identified two existing project records, which I then read in full:

- `lab/work/returns/BSD_OPENAI_RELEASE_SCREEN_CLAUDE_2026-10-06/GATE4_CHECK.md`;
- `lab/work/returns/BSD_ARISTOTLE_RANK2_ANCHOR_SUBMISSION_2026-10-06/DELTA_TASK_RANK2_ANCHOR.md`.

They already screen the arbitrary-dimensional obstruction span, Bockstein alternation, square switches, missing-vertex architecture and rank-one spectral/tame identity. The rank-two-anchor assignment explicitly identifies the same three-stage comparison (tame factorization, nondegenerate auxiliary, missing global anchor). Therefore those mechanisms must NOT be presented as newly discovered on October11.

The added work in this note is narrower: a current pinned-source read of the October7 revision, exact tracing of the rank-one/finiteness input at `vertical:parity`, substitution of the existing rank-two derivative into `models:series-division`, and the explicit L=u+p^a, B=L² countercontrol. The rank-two quotient/acyclicity admission test below refines an already-recorded open comparison. It is not a new arithmetic input or a reason to rerun the unchanged anchor job.

The historical Gate4 note correctly withdrew a blanket claim that fixed-p methods cannot imply a global theorem. This note does not reinstate it. Its issue is the actual missing arithmetic anchor and the input types of the cited proof. The old delta-task contains strong retained assertions about BKS/tame factorization; those are historical source claims, not recertified by this screen and must be checked against later corrections before use.

## 1. Actual main theorem hypotheses

1. `exact_01-introduction.tex:49-73`, theorem `thm:main`: for some prime q, the FULL q-power Selmer corank must be in {0,1}. The theorem asserts rank equality, entire-Sha finiteness and all-prime exact BSD, with no additional local/residual conditions. Lines68-74 emphasize that low Selmer corank is essential and not replaceable by Mordell-Weil rank alone.
2. `converse_01-introduction.tex:24-44`, theorem `thm:main`: same corank range for any specified p, with analytic rank equality and entire-Sha finiteness, but not an exact leading-term evaluation.
3. `two_01-introduction.tex:56-97`, theorem `thm:main` and any-prime corollary: corank<=1, giving rationality and the exact 2-part. The corollary imports the converse, then uses finiteness to identify the 2-corank with rank.

For the seed, the two independent saturated rational points imply

    corank_Zq Sel_(q∞)(E/Q) >= rank E(Q) = 2

for every q. A quotient by the two point directions is not the full Selmer group of the same elliptic curve and does not satisfy the input type of these theorems.

The exact-BSD proof is not a standalone rank-two result obscured by its title. Its discrepancy X_p(E) is defined only after analytic low rank, finiteness and rationality have been obtained (`exact_01-introduction.tex:145-166`). Importing its final discrepancy inequality for the seed would assume quantities not yet available here.

## 2. Useful rank-independent algebra: division from high characters

Source: `exact_03-models.tex:538-590`, lemma `models:series-division` (statement557-566, proof568-590).

Let O be a complete integer DVR, and L,B in O[[t,u_1,...,u_m]]. Assume

    L mod(varpi,t) != 0.

If B(theta,u) is divisible by L(theta,u), after inverting p, for every sufficiently high finite p-power character theta of 1+t, then L divides B integrally. The proof uses a tame-coordinate change, integral Weierstrass division and the boundedness of the remainder coefficients. It explicitly permits bounded series (one common denominator), not arbitrary Q_p[[t]] series. This formulation does not assume rank one or Sha finiteness.

This is potentially useful when a genuine analytic-to-determinant comparison is known at sufficiently ramified characters but the integral specialization is unresolved. It is NOT itself a unit/nonvanishing theorem.

### Exact substitution of our existing derivative

The current seed object has z=U y, with actual determinant factor d(U), and an integral Kato inequality d | U g in the kernel coordinate y=g eta. The rank-two center forces the maximal minors to vanish there. Thus attempting to put L=d, t=U into the division lemma fails its stated prerequisite: d mod(p,U)=0.

In the nonzero-derivative branch the project derives d=U d_1. With no added tame variables, applying the same lemma to L=d_1 requires d_1(0) to be a p-unit. That is not known, and the desired target m_p-w_p<=1 deliberately permits some common p-content. The division lemma cannot manufacture this prerequisite.

Adding genuine tame variables can make the residual regularity condition possible even when the central determinant vanishes. That remains a valid research possibility. It only supplies integral divisibility until a separate unit or content argument is added.

### Own exact countercontrol (not a source theorem or seed realization)

For any a>=1, take R=Z_p[[t,u]],

    L=u+p^a,   B=L^2,   Q=B/L=L.

Then L mod(p,t)=u !=0, B mod(p,t)=u^2 !=0, and every character specialization has integral divisibility L(theta,u)|B(theta,u). Both L and B are vertically primitive (neither is divisible by p). Nevertheless Q(0,0)=p^a. Thus high-character division plus absence of a vertical p-factor places NO bound on central p-content.

Choosing a arbitrarily large even number is compatible with a parity requirement on a hypothetical finite length. This is only an algebra test, not an assertion about the seed.

The finite-error model already relevant to the seed makes the complementary point:

    D(U) = [[p^a,U,0],[0,0,U]],
    eta=(U,-p^a,0),   d=U,   z=U eta.

The specialized kernel vector has content a, while the actual cokernel contains R/(p^a,U), invisible to height-one characteristic data. The new paper's division lemma does not remove this term. Derived models must retain it.

## 3. First explicit rank-one use in the arithmetic bridge

Source: `exact_04-vertical.tex:13-16` sets E/K and its companion to rank one with finite Sha. The critical later step is lemma `vertical:parity`, lines243-306, especially252-266.

To prove generic acyclicity of a one-sided strict/full complex at t=0, it specializes centrally in characteristic zero. The proof invokes the auxiliary-field simple-zero choices to obtain **one compact Selmer line from points**; its localization at either p-place is nonzero because an individual nontorsion point has nonzero local logarithm. Strict/finite comparison then gives acyclicity. Generic acyclicity plus alternating self-duality is used to deduce even residual nullity. This is then an input to the residual concentration and horizontal jump arguments.

For the rank-two seed, localization of the two-dimensional known rational-point plane into a one-dimensional local Kummer line necessarily has a kernel of dimension at least one. For E over a quadratic K, the original rational points still inject. If using the retained -23 rank-one twist, the K-side point rank is at least three. Therefore this proof of central acyclicity cannot simply be copied.

The central use is explicit again in `exact_10-center.tex:12-22,58-74`: E(K) is rank one, Sha(E/K) is finite, and the strict/full complex is rationally acyclic because its unique global point direction localizes nontrivially.

This locates the first genuine hypothesis requiring replacement. It is not merely that the final theorem displays r<=1.

### Would quotienting by the saturated W repair it without assuming FIN?

The cone or residual quotient by the known point lattice can be defined without assuming finiteness. One must keep the complete derived complex and its dual map. However, declaring the resulting rational compact Selmer quotient acyclic requires controlling the Tate-module contribution of Sha; that is primary finiteness, not a consequence of saturation. Integral acyclicity would be stronger still because finite Sha and specialization torsion remain.

For a fixed p in the already-established branch delta_p !=0, primary finiteness is a consequence of that nonvanishing and can legitimately be used afterwards. That does not prove delta_p !=0 cofinitely, nor bound its excess content.

A further independent difficulty is deformation: the center's saturated point lattice is not automatically a flat rank-two subcomplex throughout the genuine tame-character family. The project's finite-order lifting results do not supply an all-order compatible family. Thus writing “remove W” in the universal determinant is not an available operation until its arithmetic map, flatness/derived errors and specialization are proved.

An exterior square alone does not fix the type: P1 wedge P2 belongs to an exterior power of cohomology, whereas the source's Kato class and Selmer line are degree-one objects. The exterior square of localization of two rational points to a single one-dimensional p-Kummer line is zero. A new comparison for a determinant/derived leading term is required; this is not a proof that such a comparison is impossible.

## 4. The source's missing ingredient beyond division is explicit

`exact_09-unit.tex:136-220` proves abstract codimension-two tests using augmented alternating matrices [A|B] and tangent minors. The algebra allows arbitrary finite dimensions; it is a useful template, not a seed bound by itself.

`exact_09-unit.tex:252-388`, proposition `unit:simultaneous-jumps`, constructs arithmetic tame directions and uses the previous parity/acyclicity inputs, joint evaluation, cup primitives, and Chebotarev to make simultaneous one-sided jump loci codimension at least two. `exact_08-extraction.tex:28-42` is the preceding theta-to-Selmer implication identifying analytic horizontal zeros with such jumps. `exact_09-unit.tex:396ff` combines these with integral specialization to prove quotient units.

This is a concrete candidate mechanism different from “produce one more relation.” But it requires both:

1. an actual rank-two analytic/divided source and determinant quotient whose horizontal zero implies the specified excess jump;
2. enough arithmetic tangent directions for the *same quotient*, while all source/specialization comparisons remain integral and no assumed Sha bound is used.

The first of these is not furnished by the existing exact receiver, order-three W-lift or Kato-content criterion. The second cannot be inferred from an abstract alternating-matrix lemma. The early rank-one acyclicity step must be replaced, not cited through it.

### Narrow next admission test

Before a large construction run, write the actual reduced complex for the seed's specified Kato derivative and the normalized analytic element intended to be its determinant coordinate. Test whether the source lemma `extraction:theta-implication` can be stated for that exact reduced object **without** assuming the reduced compact Selmer space vanishes and without replacing it by the rank-one object's primitive complex. If yes, check the tangent slice for the quotient with every H2/specialization term retained. If no such matching object/map can be written, this manuscript has not yet supplied a new arithmetic bound and the next task must construct that comparison, not replay the finite-order point lifts.

This is a source-specific unfinished test. No claim of likely success, or of a universal obstruction, is made.

## 5. Additional useful normalization source (not a bound)

`exact_05-single.tex:213-297`, `single:kato-calibration`, proves a full-level dual-exponential formula in square order, using Kato9.5 with k=2, r=r'=1, and explicit cusp residues fixing the scalar +/-M^-2. It visibly distinguishes rational cancellation of smoothing factors from integral divisibility (lines289-297).

`exact_05-single.tex:299-340`, `single:period-law`, gives the actual smoothing factor

    Delta_nu=(c^2-c nu(c)^-1)(d^2-d nu(d)^-1)

and imprimitive finite Euler factors, a common orientation sign, a primitive positive Betti period Omega_0, and unnormalized trace conventions. This could independently cross-check the seed's fixed-source normalization. That is supporting work only: normalization was already separated from uncontrolled intrinsic content in our record, and another normalization check is not new control on m_p-w_p.

The rank-one exact tame comparison is more arithmetically substantial:

`exact_05-single.tex:740-778`, `single:logarithm`, claims

    log_omega(z_b)/(log_omega P)^2
       = +/- d_0 L'(E,1)/(Omega_0 H(P)),

with d0 the specified smoothing/Euler product and analytic rank exactly one. It identifies the rational Selmer line with points using finite Sha at lines752-760. Its height is the paper's explicitly specified H attached to 2[O], not silently an alternative canonical-height convention. The proof uses an independently nonzero rank-zero quadratic twist and a rank-one height direction, not a rank-two second derivative.

This is relevant as a model for constructing a precise arithmetic comparison and as a calibration source for rank-one twists. It is not our desired seed depth-two 288 law, and differentiation/exterior squaring is not justified by the statement.

## 6. Application to an already-known auxiliary twist

Under the retained historical certificate, E^(-23) has analytic rank one. The standard analytic low-rank theorem supplies entire-Sha finiteness and full Selmer corank one; therefore the new exact-BSD theorem's hypotheses would hold for **that twist**, conditional on the correctness of the preprints. It would upgrade its all-prime leading-term formula in the stated normalizations, and the rank-one logarithmic comparison could be tested there.

This does not imply BSD for E. Over Q(sqrt(-23)), the L-function product has orders2+1=3 and the point rank is at least3. The exact paper's auxiliary-field construction demands a sum of ranks1. The record's -7 twist can likewise only be used after its retained rank-zero input is matched; it does not remove the original rank-two summand.

The exact paper's analytic twist-density input (from a companion) could help choose auxiliary twists with prescribed finite splitting conditions. It does not produce uniform residual nonvanishing of a class for the fixed seed. Density-one results about varying curves do not bound the fixed curve's Sha across coefficient primes.

## Scope and endpoint effect

This is a source-level relevance screen with explicit substitution tests. It is not an independent certification of the hundreds of pages in this dependency chain, a novelty assessment, or a formal verification. No source class, class group, large modular-symbol calculation, external job or paid submission was executed. No GitHub mutation was made by this subtask.

**FIN, ORDER9, Q36: unchanged.** Useful candidate tools and a concrete first rank-two replacement point have been identified. No new seed coefficient or arithmetic content estimate is supplied.
