# Primary-source checks for this single Eisenstein operation

Checked 2026-09-19. The desired theorem must upper-bound **excess mod-\(p\) Selmer classes for the standard representation of this fixed curve**, with all primes controlled by one fixed finitely generated integral object. This audit tests precisely that applicability. It is not a claim to have classified every Eisenstein theorem in existence.

## Findings tied to theorem statements

| Primary source | Exact item read | Applicability finding |
|---|---|---|
| [Harder–Raghuram, *Eisenstein cohomology for GL(N) and ratios of critical values of Rankin–Selberg L-functions*](https://arxiv.org/pdf/1405.6513) | §§2.2.5–2.2.6, 3.1.4; definitions of algebraic coefficients and infinitesimal characters | The finite-dimensional algebraic-coefficient category requires the regular infinitesimal character determined by a dominant weight. The exact seed datum has character \(\{1,1,0\}\), so is not a point of this classical cohomology. Calling \(\mathrm{GL}_2\times\mathrm{GL}_1\) a Rankin–Selberg datum does not remove this weight test. |
| [Urban, *On the ranks of Selmer groups for elliptic curves over Q*](https://www.math.columbia.edu/~urban/eurp/tifr.pdf) | Introduction, Theorems 1.1 and 2.2, weight-two discussion, §4 | This genuinely concerns the standard central Selmer group, including weight two, through a non-arithmetic \(p\)-adic Eisenstein construction on U(2,2). It must not be dismissed as merely adjoint or as wholly unable to reach weight two. Its conclusions are nonvanishing and lower corank bounds, including a lower bound of two in the positive even-order case. They give no upper bound on excess mod-\(p\) classes and no fixed cross-prime integral module. |
| [Urban's 2013 erratum](https://www.math.columbia.edu/~urban/eurp/erratum-tifr.pdf) | Both corrections | The family theorem requires polarization; the local extension argument is corrected to establish the stated de Rham conclusion. The erratum does not reverse the Selmer inequality or construct an integral horizontal bound. |
| [Bellaïche–Chenevier, *Families of Galois representations and Selmer groups*](https://arxiv.org/pdf/math/0602340), Astérisque 324 | Theorems 1.5.5, 1.5.6; Remark 1.5.8 | The off-diagonal module dual injects into an extension group. Its image consists of extensions factoring through the chosen Cayley–Hamilton quotient. That image need not exhaust the Galois extension group; the dependence on the quotient is explicit. This is the exact direction obstruction for an automorphic quotient. |
| [Berger–Klosin, *On deformation rings of residually reducible Galois representations and R=T theorems*](https://arxiv.org/pdf/1103.5100) | Assumption 5.1; Theorems 8.5–8.6; Remark 8.7 | The relevant extension space is assumed one-dimensional, incompatible with the seed's two Kummer directions when the constituents are \(E[p]\) and 1. Theorem 8.5 also inputs a Selmer-order upper bound. It cannot be used to obtain that bound from congruences alone. |
| [Berger–Brown–Klosin, *Klingen Eisenstein congruences and modularity*, Canadian J. Math., 2025](https://doi.org/10.4153/S0008414X25101612) | Assumption 6.2; Proposition 6.14; Theorem 7.2 | The modularity application concerns four-dimensional representations and twisted adjoint Selmer groups of the two-dimensional form. Its hypotheses include a specified order of a twisted adjoint Selmer group and adjoint vanishing. No proved specialization to the seed's standard \(E[p]\) quotient is provided. |
| [Manji–Thøgersen–Wu, *Families of symplectic Galois representations over small parabolic eigenvarieties for Siegel cuspforms of genus 2*, v2, 22 July 2026](https://arxiv.org/pdf/2604.18433v2) | §5.3; Theorems 1.3.1–1.3.2 and the Saito–Kurokawa applications | The infinitesimal \(R=T\) discussion assumes an absolutely irreducible representation and the stated refinement hypotheses. The separate Saito–Kurokawa applications give nonvanishing/lower-bound information for standard Bloch–Kato Selmer groups at a chosen \(p\); they are not a residual integral upper bound across primes. The v2 theorem, rather than just the earlier abstract, was checked. |
| [Iyengar–Khare–Manning–Urban, *Congruence modules in higher codimension and zeta lines in Galois cohomology*](https://arxiv.org/pdf/2311.13070) | Introduction and §5 arithmetic application | The arithmetic application uses adjoint motives of Hilbert modular forms and begins with a fixed \(p\)-adic coefficient ring. Higher codimension does not by itself give a second-order standard-representation theorem for this rank-two seed, a Mordell–Weil quotient comparison, or a common integral annihilator. |

The first three rows distinguish an actual weight obstruction for classical GL(3) from an existing nonclassical route to **lower bounds** for the right standard Selmer group. The final verdict is therefore a direction failure for the broader mechanism allowed in the brief, not an assertion that weight-two Selmer groups are inaccessible to all Eisenstein methods.

## The recent tangent inequality still points the wrong way

In Manji–Thøgersen–Wu v2, Theorem 1.3.2 has the form

\[
 t\le\frac{(d+1)(3d+2)}2+1,
\]

where \(t\) is an eigenvariety tangent dimension and \(d\) is the dimension of the indicated standard Bloch–Kato Selmer group. Under its hypotheses this can force **a lower bound on \(d\)** from a large \(t\). A bound on \(t\) does not reverse this inequality. Moreover these are characteristic-zero \(p\)-adic Selmer dimensions, not the required integral excess mod-\(p\) torsion comparison.

The explicit map in Bellaïche–Chenevier is even more direct: automorphic off-diagonal functionals give extension classes. Its image characterization makes the missing converse a factorization/modularity assertion, not a formal property of generalized matrix algebras.

## What was searched and what is not asserted

The search covered GL(3) maximal-parabolic Eisenstein cohomology, Urban's standard-representation Selmer constructions, reducible three-dimensional deformation rings, generalized matrix algebras, completed/coherent cohomology and parabolic eigenvarieties, modern reducible \(R=T\) statements, and higher/derived congruence modules. Exact-weight and exact-representation checks were then applied to the closest primary texts.

No verified theorem was located that simultaneously supplies:

1. the exact standard-representation local Kummer conditions;
2. the Selmer-to-congruence **upper-bound direction**, after accounting for \(W\);
3. reduction/localization of one fixed finitely generated integral object as \(p\) varies.

This bounded negative finding is distinct from the proved singular-weight calculation and the elementary trace-invisibility identity in the main report. Those algebraic obstructions hold independently of the search.

No claim is made that a future converse or nonclassical integral comparison is impossible. Nor is the missing comparison declared equivalent to full rank-two BSD without a proved converse. The operation has failed its present gate and stops; it does not launch a search for such a new architecture.

## Source custody

The primary PDFs and the initially inspected v1 eigenvariety HTML are archived under `sources/`. The controlling modern eigenvariety check is the v2 PDF, which supersedes that v1 snapshot for this audit. `SOURCES.json` binds source URLs and SHA-256 digests. Only cited sections and statements were audited; this is not a full referee review of these papers.

The preceding division-field theorem and current seed record are read-only inputs. No class-group estimates, GL(3) computations, exceptional-prime arithmetic, or automated successor work were performed.
