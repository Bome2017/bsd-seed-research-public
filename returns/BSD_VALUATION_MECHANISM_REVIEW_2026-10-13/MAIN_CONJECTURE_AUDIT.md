# Independent audit of the integral main-conjecture interface

Date: 2026-10-13. Scope: the theorem hypotheses and integral normalizations in `input/BSD_VALUATION_MECHANISM_2026-10-13/PROOF.md`, with an additional check for the later d=329233 control. Read-only with respect to the producer packets; no numerical coefficient, height or descent was rerun.

**Verdict: MAIN_CONJECTURE_INTERFACE_SUPPORTED_UNDER_RETAINED_ARITHMETIC.** No missing rank restriction, hidden primary-Sha-finiteness premise, or rational-versus-integral mismatch was found in this interface. This does not independently certify the retained arithmetic or the separate algebraic leading-term theorem application.

## Primary statements actually checked

1. **Burungale–Castella–Skinner**, arXiv:2405.00270v2, Theorem 1.1.2, printed p.2. Part (a) requires good ordinary p>3 and irreducibility of E[p] over F_p, and gives equality after inverting p. Part (b) gives equality in Z_p[[Gamma]] when an element of the cyclotomic kernel has Tate-module coinvariants isomorphic to Z_p. There is no rank bound or squarefree-conductor hypothesis. The rank-zero/one restriction belongs to the separate complex-BSD corollary, not this theorem. Both pinned PDF text and HTML were checked. The PDF is preferred for version custody; the HTML date metadata differs.

   https://arxiv.org/pdf/2405.00270v2

2. **Castella–Grossi–Skinner**, arXiv:2303.04373v2, Theorem A (p.2), Theorem 7.1.1 (p.29), §2.1 (p.6), and §3.2.1. The integral Iwasawa algebra is explicitly Z_p[[Gamma_Q]]. At a good prime p>2, reducible semisimplification with a constituent locally different from both 1 and omega gives integral equality for the ordinary Selmer characteristic ideal. There is no rank or Sha-finiteness hypothesis. The analytic generator is normalized by the given curve's minimal differential and primitive plus period. Isogeny invariance includes the period scaling; the theorem is not restricted to an optimal curve. The full-real/primitive-plus discrepancy is a 2-unit here. The result does not validate arbitrary p-rescalings of a computed measure.

   https://arxiv.org/pdf/2303.04373v2
   https://arxiv.org/html/2303.04373v2

I read the statement, normalization and isogeny passages in the primary texts, not only abstracts. I did not reconstruct either paper's full proof. Browser screenshot calls did not provide a usable displayed image for independent visual inspection; this audit therefore claims text inspection, not fresh visual confirmation.

## Hypothesis match for the two reducible controls

Retain the actual quadratic-twist/isogeny identification with the conductor-11 class. Its residual semisimplification at 5 is 1 plus omega, so the d-twist has constituents chi_d and omega*chi_d. This deduction concerns semisimplification and does not assume the representation splits.

An independent elementary calculation in this audit gives:

| d | factorization | d mod 4 | d mod 5 | quadratic character at 5 |
|---|---|---:|---:|---|
| 43737 | 3*61*239 | 1 | 2 | unramified, Frobenius -1 |
| 329233 | prime | 1 | 3 | unramified, Frobenius -1 |

Thus chi_d is nontrivial but trivial on inertia, whereas omega has nontrivial inertia. It follows directly that chi_d is neither 1 nor omega. The other constituent omega*chi_d is also neither: it is nontrivial on inertia and its quotient by omega is chi_d. The choice of isogeny-kernel character causes no ambiguity.

The recorded good ordinary reduction at 5, with a_5=-1 and seven residue points, is consistent with both twists. Therefore CGS applies separately to each named curve, including the nonoptimal F curve. A rational 5-isogeny is no obstruction to this particular theorem.

## Hypothesis match for the seed and irreducible controls

The producer's primitive-transvection argument is valid. At a multiplicative prime q != p with minimal discriminant valuation one, Tate inertia has a primitive upper-right entry in an integral Tate basis. The nonsplit case differs by an unramified quadratic twist, trivial on inertia. This inertia fixes all p-power roots of unity. Choosing a topological tame element therefore gives the required cyclotomic-kernel element with a free rank-one coinvariant quotient.

Applied to the retained q=2243 seed data, this verifies BCS (im). The retained residual-image theorem supplies (irrQ). The same argument applies to q=433 for 433a1 and q=131 for 655a1 at the stated coefficient primes. The listed nonsquare Frobenius discriminants exclude an F_p-invariant line; no stronger residual theorem is needed for the statement used here. This argument must remain restricted to good ordinary coefficient primes.

## Consequences and remaining custody

For d=43737, this audit finds no main-conjecture obstacle to upgrading the residual lower bound using the retained exact valuations (2,0). The separate leading-term interface, coefficient normalization, point saturation, rank bound and precision remain necessary inputs.

For d=329233, the same source theorem is available. Combining the retained valuations (4,2), unit Euler and Tamagawa/torsion corrections, and the separately audited algebraic leading-term theorem would give primary length two. Together with the retained independent residual lower bound of two, it would give (Z/5)^2 for this newer control as well. This is a proposed theorem application using saved arithmetic, not a newly evaluated coefficient or a conclusion about full Sha.

For the seed at 17, the main-conjecture interface supports the reverse deduction from the independently retained primary vanishing and nonzero matched height. It does not turn that inferred coefficient valuation into an independent Sha proof.

No theorem in this audit supplies a cofinite bound on the seed's quotient, a residue of its unknown leading coefficient, or the full p-adic unit in any control quotient. FIN, ORDER9 and Q36 are unchanged by this audit.
