# Stage 1 audit — no compression theorem obtained

**Status: the independence gate failed.**

The inspected sources and retained constructions do not furnish a
cutoff, a support bound, or a finite list of regimes with proved
vanishing throughout each unresolved regime. The reduction-type
partition in PRIME_COVERAGE_MAP.md provides exhaustive labels only.

## Strongest applicable ordinary result

For every \(p\in O\), the retained hypotheses give residual surjectivity,
a \(p\)-unit Manin constant, and \(\operatorname{Tam}_E=16\).
Castella–Sano Theorem B therefore gives \(M_\infty(\delta^{(p)})=0\):
some Kurihara number is a unit modulo \(p\). It does not require the
auxiliary conductor to have two prime factors. Its supersingular clause
requires squarefree conductor, which this seed does not have.
[Castella–Sano, v1](https://arxiv.org/abs/2601.14504v1).

The available and needed quantifiers differ:
\[
\underbrace{\forall p\in O\ \exists n:\bar\delta^{(p)}_n\ne0}
_{\text{available, without a bound on }\nu(n)}
\quad\not\Rightarrow_{\text{any proved arrow here}}\quad
\underbrace{\forall p\in O\ \exists n:
 \nu(n)=2,\ \bar\delta^{(p)}_n\ne0}_{\text{rank-two requirement}}.
\]
This notation records the absence of a proved implication in this
session; it is not an arithmetic counterexample theorem.

Kim Theorem 1.8 identifies the first nonzero degree with Selmer corank.
Its identification with Mordell–Weil rank additionally assumes primary
Sha finiteness. Theorem 1.10 supplies the mod-\(p\) localization
description; its final rank assertion additionally assumes
\(\Sha[p]=0\). Neither additional assumption can be imported as a
consequence of the known rank-two basis.
[Kim, v6, Theorems 1.8 and 1.10](https://arxiv.org/abs/2203.12159v6).

The retained ordinary theorem O1 has already checked the auxiliary-prime
cyclicity and normalization issues and proves
\[
 h_p=0\ \Longleftrightarrow\ \Sha[p^\infty]=0\qquad(p\in O).
\]
It consequently gives the same equivalence uniformly outside any
specified finite subset of \(O\). Naming a uniform depth-zero condition
would recode the desired vanishing, without supplying the independent
information required by Stage 1.
[O1 and its exact scope](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md).

## Other inspected source boundaries

Kim's later structural results retain the same distinction: Corollary
1.11 bounds Selmer corank by the number of auxiliary primes of a
successful witness. It does not bound that number by two. The analytic
order comparison is Conjecture 1.6.
[Kim, with an appendix with Pollack, v1](https://arxiv.org/abs/2505.09121v1).

The September 2026 Heegner-point paper gives an equivalence between
primary finiteness and specified derived-point membership conditions
(Theorem 1.1). Its supersingular case assumes semistability. The finite
reduction tests of Theorem 4.7 depend on global data varying with \(p\)
and ring class fields; Questions 4.6 and 4.8 isolate unproved input and
an algorithmic issue. No fixed cross-prime support bound follows from
these statements. Finiteness alone also leaves the primary order open.
[Kim, v1](https://arxiv.org/abs/2609.15328v1).

## Difficulty-reduction gate applied

These are audits of already supplied mechanisms, not proposed successor
targets.

| Gate | Ordinary witnesses | Criterion SS | Existing WC/content assembly |
|---|---|---|---|
| Endpoint if all missing arithmetic input succeeded | Exact remaining ordinary vanishing; other regimes still needed | Exact remaining supersingular vanishing; other regimes still needed | At most finite support/FIN without further exact primary control |
| Complete conditional chain | Independent two-prime unit theorem → depth zero → ordinary primary vanishing → combine all other regimes and imports → order nine | Uniform successful coefficient theorem → Criterion SS at every member → supersingular primary vanishing → combine all other regimes and imports → order nine | Proved arithmetic antecedent → support restriction and required local finiteness → FIN; additional vanishing at every remaining support prime → order nine |
| First unproved arrow | Unrestricted witness existence → a two-prime unit for every \(p\) | Simultaneous success of the coefficient test | Independent arithmetic antecedent and its comparison |
| Non-equivalence test | O1 proves an exact converse for depth zero | No strict difficulty reduction established | Ordinary primitive tail already equivalent by O1 |
| New information supplied in this session | None proving the missing arrow | None proving uniform success | Conditional formal algebra only |
| Prior obstruction compatibility | N3/N4 forbid credit for pointwise existence or recoding | No theorem for all coefficients; repeated tests do not compress | N1–N4 forbid inference from source integrality/perfectness to evaluated content/support |
| Kill condition | Stop if degree-two uniformity is only required, not derived | Stop if a per-prime test is presented as a tail | Stop if the arithmetic comparison remains a hypothesis |

All three kill conditions are met at the level required to reject them
as *independent compressions in this session*. This does not disprove the
arithmetic assertions themselves.

A1 and A2 now provide checked conditional algebra at their successor
freezes. They do not construct an arithmetic antecedent, reduce its
difficulty, or prove uniform primary support. No time was spent
reproving that formal algebra.

The first missing arithmetic arrow has therefore not moved. Stage 1
ends here; no new object or replacement research target is introduced.
