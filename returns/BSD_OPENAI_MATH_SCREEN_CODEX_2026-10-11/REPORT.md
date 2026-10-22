# OpenAI math: what can actually be reused for the BSD seed

Date: October 11, 2026.

**RELEVANT_SOURCE_MECHANISMS_IDENTIFIED; NO_NEW_SEED_BOUND_OR_COMPARISON_ESTABLISHED.**

There is relevant material in the repository. The strongest matches are an explicit CM-divisor/localization/theta comparison, integral character-specialization methods, and the arithmetic argument that turns certain analytic zeros into Selmer jumps. They are useful source material for named interfaces in our work. None of the inspected statements supplies the seed's missing rank-two bound, and much of the broad architecture was already screened or tried on October 6–7. This return distinguishes the concrete reusable pieces from those earlier attempts.

Repository: [openai/math at fd4aeeb2](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), commit dated October 8. The current catalogue lists 719 manuscripts in 372 families. This was a catalogue and targeted source screen, **not a reading or verification of all 719 manuscripts**. The full source sections for the selected arithmetic papers were downloaded; each note states the passages actually inspected. Hashes establish custody, not mathematical validity.

## 1. Most concrete match to the current CM-divisor work

The [pointwise two-converse manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/sections/coefficients.tex) does not merely assert a comparison exists. In `co:kummer` and `co:theta-bridge` it writes an actual finite-field Kummer detector and a weighted theta coefficient formula:

\[
\lambda_M=b\kappa_M,\qquad
a_M(D)=c_0 2^{\omega(N)}\zeta_M(D)
\lambda_M(\operatorname{red}_{\ell}(LP_D))\pmod{2^M}.
\]

It explicitly retains modular parametrization, orientations, stabilizer denominators, torsion adjustment, local weights and character phases. That is a usable comparison template for the BD lane's divisor-to-local-point map. The most useful work would be to identify any genuinely shared integral reduction/pushforward square and its exact multiplier, instead of importing a scalar from a choice of bases.

The direct transplant fails a precise check: its detector uses Frobenius equal to complex conjugation and a plus-eigenline. Our G2 primes have Frobenius \(-I\) at odd p. An unchanged plus-invariant scalar row would satisfy \(b(-I)=b\), hence \(b=0\). Also, its global point is a rank-one Heegner sum, not our two-point determinant. The formula is therefore relevant **construction machinery**, not the missing 288 identity. Merely changing 2 to p does not fix those differences.

[Detailed map alignment and source labels](notes/ADJACENT_ARITHMETIC.md).

## 2. Relevant to the Kato derivative: integral specialization and horizontal zeros

The [exact-BSD manuscript, section 3](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/03-models.tex) states a rank-independent division lemma. Roughly: rational divisibility at every sufficiently high finite cyclotomic character becomes integral divisibility when the denominator has a specified nonzero residual tame component.

I tested that statement against the existing seed determinant rather than only listing it. Our central determinant has a forced U factor. Substituting it directly fails the lemma's residual hypothesis. Removing U in the established nonzero-derivative branch still does not give the needed content estimate. There is an exact algebra control:

\[
L=u+p^a,\qquad B=L^2.
\]

Both are primitive as power series, and every character specialization has integral divisibility. Nevertheless \((B/L)(0,0)=p^a\), with a arbitrary. Thus integrality and absence of a vertical p-factor do not bound central excess content. This does not refute the lemma; it checks what the lemma can deliver.

The manuscript has an additional proposed mechanism: sections 8–9 identify analytic horizontal zeros with simultaneous Selmer jumps and then exclude their divisors using arithmetic tangent directions. This is much closer to upper control than another principal relation. But its arithmetic proof uses central acyclicity from a single point-generated Selmer line. The exact use is section 4, `vertical:parity`, lines 252–266. The seed already has two rational point directions and a nonzero localization kernel on that plane.

Quotienting out the known plane can be defined; claiming the quotient is rationally acyclic would additionally kill the Tate-module contribution of Sha. The source does not prove that for us. An all-order family quotient is also not supplied by the previous order-three point lifts.

The source-specific question worth retaining is whether its **theta-zero to excess-jump implication** can be proved for the actual divided rank-two source, with all H² terms retained. This is an unfinished adaptation, not a theorem obtained here or a recommendation to repeat the earlier switch run.

[Exact substitution, source chain and countercontrol](notes/DIRECT_BSD_AUDIT.md).

## 3. A rational-scalar technique, with the needed geometry exposed

The [Milne-rationality manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/build/sections/02_transport.tex) normalizes local similitude factors by a ratio of rational intersection numbers of the **same** algebraic divisors. This is a concrete way to force local scalars to agree once actual geometric maps and a nonzero testing pairing exist.

It does not create those maps for the seed. Its theorem compares cohomological realizations at one fixed reduction place; it does not identify the scalars from all varying coefficient/auxiliary primes. Nor do rational Hodge/Tate classes recover point heights or Kummer extensions automatically: the ordinary cycle class of the degree-zero divisor [P]-[O] is zero even for an infinite-order point.

Keep the intersection normalization as a technique. Do not cite it as rationality of Q36, a fixed 288 scalar, or integral primitivity.

[Geometric input requirements and coefficient-versus-reduction-prime distinction](notes/GLOBAL_CYCLE_SCOPE.md).

## 4. Useful auxiliary and formalization material

- **Auxiliary twists:** the pointwise-converse source has local-squareclass-prescribed nonvanishing witnesses. This could help if a new geometric construction needs a different rank-zero/rank-one companion with exact local signs. It does not improve the already retained -7/-23 inputs just by providing more twists, and its new arithmetic proof needs review.
- **Rank-one normalization control:** exact-BSD section 5 gives detailed smoothing, period and tame-log formulas. An auxiliary rank-one twist is a legitimate place to test those conventions. Its resulting scalar does not automatically transfer to the seed's rank-two eigenspace.
- **Lean support:** pinned dependencies contain actual formal-log multiplication compatibility and an isomorphism between the reduction kernel and the formal group over a complete DVR. They could save Aristotle work on a specifically needed local formalization. The selected files were read, not built or independently kernel-audited here. They give no cofinite bound.

[Declaration names, hypotheses, pins and formalization limits](notes/FORMALIZATION_SCOPE.md).

## 5. Main-theorem and historical checks

The headline full-BSD theorem assumes the **full q-power Selmer group has corank zero or one** for some q. The saturated rank-two point lattice injects into this group for every q, so the seed is outside that hypothesis for every q. A quotient by the points is not another input satisfying the theorem. Goldfeld density statements concern a density-one family of twists; they do not settle this chosen rank-two curve. Imaginary-quadratic modularity supplies no missing modularity premise for an elliptic curve already over Q.

The October 6 lab screen, rank-two-anchor return, and subsequent Aristotle review were read and bound in `context/`. They already cover obstruction spanning, alternating pairings, determinant switches, missing-vertex interpolation and the rank-one anchor. Today's report does **not** announce them as new directions. The later deformation accounting in the conversation already identifies the preserved excess quotient, so another finite-order lifting task is not licensed by these sources.

At the current pin, no main-result Lean formalization is registered for the screened BSD/converse/Goldfeld/modularity families. The repository-wide 42% formalization statistic must not be attached to them. Complete scoped trees were fetched because GitHub's initial all-repository and all-Lean trees were truncated. No absence claim rests on a truncated tree.

The exact-BSD October 7 revision removes an obsolete introductory citation and updates companion references. It supplies no documented rank-two extension. Separate Hodge-related withdrawals were checked; neither association with those withdrawals nor absence from the withdrawal list certifies the BSD arguments.

## 6. Result for the seed and sensible reuse

The strongest current reuse is **source-level comparison of the CM-divisor map and its integral normalization**, followed, if a shared square exists, by importing only that proved square. The Kato paper's analytic-zero/excess-jump mechanism is a more ambitious adaptation target, with the precise rank-one step now located. Neither should become an unbounded generic task or a repeat of the already-tested anchor/point-lifting program.

No manuscript theorem is promoted to an accepted seed input by this screen. No derivative coefficient, CM value, new primary certificate, uniform content estimate, fixed-scalar tame identity or leading-term equality was obtained. No new Aristotle job, paid computation, prime campaign or external message was launched.

**FIN, ORDER9 and Q36 remain unchanged.** This return provides a pinned source map and usable methodological leads, not a claimed step through the missing upper-bound theorem.

## Evidence navigation

- [Direct BSD audit](notes/DIRECT_BSD_AUDIT.md)
- [Adjacent arithmetic and CM comparison](notes/ADJACENT_ARITHMETIC.md)
- [Global-cycle scope](notes/GLOBAL_CYCLE_SCOPE.md)
- [Formalization and correction audit](notes/FORMALIZATION_SCOPE.md)
- [Historical input bindings](INPUT_BINDINGS.json)
- Source bindings under `sources/direct/`, `sources/adjacent/`, `sources/formal/`, `sources/global_cycles/`
- `MANIFEST.sha256` and `checks/CUSTODY.json`: identity checks only
