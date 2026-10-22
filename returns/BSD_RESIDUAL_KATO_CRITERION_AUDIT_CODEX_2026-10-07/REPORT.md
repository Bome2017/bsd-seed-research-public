# Residual derivative criterion: integral matching on a cofinite domain

**CRITERION_ALGEBRA_CONFIRMED; INTEGRAL_SOURCE_MATCHING_DERIVED_ON_D.**
Written proof under retained seed/cohomological inputs; further independent
review pending. No novelty or formal-certification claim.

The submitted algebra is correct under its explicit hypotheses. This
return additionally supplies written integral source matching on

    D={p≥5 : p∤N, p∉{19,59,487}}.

For the actual smoothed, simultaneously transported Kato derivative,

    δ_p=A_p κ(P₁)+B_p κ(P₂),

the resulting criterion is

    (A_p,B_p)Z_p=Z_p  ⇒  Sha(E/Q)[p∞]=0.

This covers ordinary and supersingular primes in D. It upgrades the
consequence of the specified residual nonvanishing from primary finiteness
to primary vanishing. It does not establish residual nonvanishing.

The matching does actual additional work:

- Corrects the rational printed display in Kato 12.5(4) to the integral
  theorem 13.4(3), used in 13.14.
- Derives the integral cyclotomic-kernel image condition from the retained
  full residual image.
- Removes the coefficient-prime local H² term using non-anomalous reduction
  and the fact that p-power extensions cannot first create p-torsion.
- Checks j_* versus full S-cohomology integrally. The bad-local Euler
  numerators are 4,2242,5844; their extra coefficient primes are precisely
  19,59,487. No p-nonunit is silently removed.
- Obtains the two-term free representative from derived residual control
  and perfectness, retaining the H² contribution.

[Integral proof](INTEGRAL_MATCHING.md) · [Algebra review](ALGEBRA_REVIEW.md) ·
[Handoff](HANDOFF.md) · [Source record](SOURCES.md)

Exact controls reproduce the seed's invariants, multiplicative signs,
exceptional-factor factorizations and #E(F₅)=8. Small matrix checks test
the image-lifting formula and its p=3 scope failure. They do not evaluate
any seed derivative or recertify the retained global image theorem.

**Endpoint:** no prime is newly settled. No uniform unit theorem, fixed
annihilator or tame comparison is obtained. FIN, ORDER9 and Q36 remain
unchanged. The next missing arithmetic is a proof that the actual coordinate
pair is primitive cofinitely, or a different independently controlled
arithmetic input. Another reformulation of that premise does not supply it.
