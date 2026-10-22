# Shii theta and local-period follow-through for the BSD seed

Date: 2026-10-11. Baseline lab commit: `9793ff7bddd1214afe5d3567beeb27f1d59a0fc8`.

**Status: SIGNED_SOURCE_AND_TWO_LAYER_EXTRACTION_DERIVED; LOCAL_PERIOD_COMPARISON_REPAIRED; NO_NEW_SEED_BOUND.**

This return follows the two arithmetic priorities in the previous source search. It completes specified source constructions and applies their actual conclusions to the seed. It does not merely list related papers. The deductions are written proofs under the named source and retained seed inputs; they are not independently certified, formally verified, or claimed novel.

The result is limited but concrete: the supersingular signed theta source is now specified integrally, its relevant residual data have explicit two-layer formulas, and a local trace/period comparison has been repaired. No seed coefficient, primary vanishing result, cofinite estimate, FIN, ORDER9 or Q36 was obtained.

## 1. Priority one: finish the actual supersingular theta source

On the retained good supersingular domain with p inert in K=Q(sqrt(-7)), excluding 7, we use one fixed primitive integral quaternionic eigenfunction for the seed. The construction matches the unraised Gross-point theta elements in Shii's finite-level Fitting theorem. It resolves the vertex/edge wording and the conductor/layer shift through the original Darmon–Iovita construction.

The actual source is now

\[
\Theta_n=\sum_{a=0}^{p^n-1} b_{n,a}\gamma^a=A_nQ_n,
\]

where the integers b_(n,a) are specified sums of that eigenfunction at Gross points of ring conductor p^(n+1). The signed division by A_n is an injective polynomial-factor map between the precise quotient modules. It retains any additional p-divisibility of Q_n.

This matters because the old raw quadratic extraction is automatically zero modulo p at every n>=2. The replacement is explicit: read a higher binomial moment of the raw source, or use its integral signed quotient. The first two layers already determine the two infinite signed quadratic jets.

The seed's rational points and the actual Fitting theorem force the signed constant terms to vanish. A separate finite Gross-point inversion argument, checked at the raw spherical vector without ordinarity, makes the residual linear terms vanish. Therefore

\[
Q_p^\pm(T)\equiv\beta_p^\pm T^2\pmod{(p,T^3)},
\]

with

\[
\boxed{
\begin{aligned}
\beta_p^-&=-\sum_{a<p}b_{1,a}\binom a2,\\
\beta_p^+&=-\sum_{a_0,a_1<p}a_0a_1\,b_{2,a_0+pa_1}\pmod p.
\end{aligned}}
\]

These are **two digits from two finite source layers**, of ring conductors p² and p³. No deeper layer is required for these jets. Their values have not been computed. A supplied exact extractor implements the formulas and preserves the distinction between input provenance, formula checks, and seed values.

[Full source construction](notes/SHII_SOURCE_COMPARISON.md) · [Executable extraction and checks](checks/README.md).

## 2. What the actual application to Sha says

Shii supplies

\[
\Theta_n\iota(\Theta_n)\in
\operatorname{Fitt}_{\mathbf Z_p[G_n]}
\operatorname{Sel}_{p^\infty}(E/K_n)^\vee.
\]

It supplies the product, not the square-root theta in that Fitting ideal. We wrote down and tested the direct upper-bound implication: a product outside the cube of the maximal ideal would bound the seed Selmer dimension by two. The actual seed symmetry prevents the raw theta from meeting that trigger at every layer, including the first. We therefore do not recommend a first-order search.

Nor does a unit quadratic theta coefficient close the gap. For an abstract integral module

\[
M_a=(R_n/(T))^2\oplus(R_n/(p^a,T))^2,
\]

the Fitting ideal contains T^4, yet its trivial specialization retains a finite pair of total length 2a. This exact control allows arbitrarily large a. It is not a seed realization; it isolates the insufficiency of the tested Fitting/order argument. The historical degree-four obstruction is preserved, not presented as a newly discovered universal impossibility theorem.

Consequently, the two-digit extraction is a completed arithmetic input format, **not an admitted stand-alone BSD certificate**. Removing the explicit supersingular factors in the theta construction does not authorize canceling them from the finite group-ring Fitting ideal.

[Direct seed application, symmetry and finite-error controls](notes/INDEPENDENT_SEED_CONTROL.md).

## 3. Priority two: repair and calculate the local-period comparison

The integral-theta thesis cites a formal-group trace relation in a step written with ordinary coordinate traces. We supply a coherent logarithmic replacement, using the formal logarithm to convert the cited trace to an actual additive trace identity. The later Burungale–Kobayashi–Ota result proves that the minimal-level coordinate and logarithmic character resolvents differ by a principal unit. The valuation correction is therefore controlled, not assumed.

With p>=5, the unramified quadratic local field, uniformizer -p, a character chi of order p^n, epsilon=(-1)^n, and h_n=ceil(n/2), the matched local formula is

\[
\boxed{
\widetilde\Omega_{\chi^{-1}}\mathcal L_\tau(y)(\chi^{-1})
=\frac{(-p)^{n+1}}{\tau_{\rm LT}(\chi^{-1})}
p^{-h_n}\omega_n^{-\epsilon}(\chi(\gamma)).}
\]

Here y is the source-matched, corestriction-normalized full Lubin–Tate lift described in the proof; tau denotes the rank-one coefficient character, and tau_LT the explicitly normalized Gauss sum. Their similar notation must not identify them. The Gauss quotient has valuation zero for these pure anticyclotomic characters. The logarithmic period has valuation zero for odd n and one half for even n. The conductor is n+1 in the full Lubin–Tate tower, not n.

This calculation uses the special Sano–Venjakob Corollary 2.6.6 appropriate to this coefficient line. The preceding general formula excludes its Frobenius value. All conductor, signed-polynomial, tame-trace and character-inversion conventions are retained in the proof.

The completed formula concerns a **local rank-one CM coefficient line**. It does not show that the thesis's global theta family can be replaced character by character while staying integral. It also does not identify this line or its classes with the full non-CM seed representation or the specified smoothed Kato derivative.

[Local derivation, source theorem interfaces and remaining global comparison](notes/LUBIN_TATE_COMPARISON.md).

## 4. Exactly where these completions attach to the seed

The current seed upper-control target remains

\[
\delta_p\ne0,\qquad m_p-w_p\le1,
\]

for the actual smoothed, transported derivative on its retained cofinite domain. The present Shii source has no established map to that derivative. It is also not the separately level-raised two-prime detector or the tame C₂(p,ell) source. The local comparison determines a denominator/conductor factor on its own source; it does not supply the missing global numerator.

A substantive continuation would need an integral arithmetic map from these actual source classes to the seed's quotient, retaining the rational-point directions and specialization errors, or an independent bound on those source classes with a justified seed consequence. That map/bound was not constructed here. We do not substitute another request to compute many theta values for it.

The previous finite-modulus C3 repair remains intact. Nothing in this return reinstates the old claim that prime-specific theorems cannot assemble over a finite modulus. Likewise, none of the scoped failures above excludes the entire signed-theta, Euler-system or Lubin–Tate theories.

## 5. Evidence and review grade

- Source proofs and precise reading scopes are retained, with hashes of local copies. Full third-party papers and rendered pages remain outside the published package.
- The two model agents separately checked the raw finite inversion transport and its signed cancellation. The parent reviewed the displayed algebra, source distinctions and finite-error example. This is not independent human review or formal certification.
- Exact controls pass: 360 finite-ring cases, 2,215 Lucas indices, 140 synthetic two-layer reconstructions, 24 rational valuation controls, and four abstract maximal-minor controls.
- None of those controls evaluates an actual seed theta element, Kato class, Selmer group or class group.
- The primitive integral source convention is defined mathematically. The enormous quaternionic eigenvector has not been enumerated computationally.

**FIN, ORDER9 and Q36 remain open.** What can now be retained is the finished source extraction and the repaired local comparison, with their precise interfaces and limitations, rather than an unexecuted “construct the signed analogue” task.
