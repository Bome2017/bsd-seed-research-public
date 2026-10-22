# Repair the unit argument at the integral level

The source Futterer, arXiv:2005.00896, Theorem 3.17 concludes that a
period factor U^- is a unit. The final paragraph of its printed proof
deduces this from nonvanishing at a Zariski-dense set of arithmetic
points. That particular inference is invalid. In Z_p[[T]], the element
p is nonzero at every characteristic-zero arithmetic specialization
and is not a unit. A nonempty closed zero locus can avoid a dense
set. This is a criticism of the printed argument, not a counterexample
to the theorem itself.

There is an integral repair in the following precisely stated setting.

**Lemma.** Let R be a local ring. Suppose an integral, surjective map

    ES: M -> S

has kernel M^+, where M=M^+ direct_sum M^- and each of M^+, M^-, S
is free of rank one over R. For bases xi^- and f write ES(xi^-)=U f.
Then U is a unit.

**Proof.** ES restricts to an isomorphism M^- -> S. Surjectivity gives
an element v with Uv=1. In the commutative local coefficient ring this
makes U a unit. No density or characteristic-zero specialization is
used.

The same proof works after a faithfully flat unramified extension:
being a unit descends, since a nonunit belongs to a maximal ideal and
remains a nonunit at a prime above it.

For an eigenspace cut from a larger Hecke module, surjectivity on the
whole module is not automatically surjectivity on the eigensubmodule.
COFINITE_HIDA_CONTROL.md removes this particular issue on its domain:
the full localized algebra is Lambda itself and the cuspidal module
has rank one. Section 6 of COFINITE_HIDA_CONTROL.md verifies the
additional family image hypotheses of Boston's theorem and hence the
allowed alignment of Futterer Condition 3.12. With this choice and
the exact integral map of his Theorem 2.39, the lemma repairs the
final step of Theorem 3.17 on this cofinite domain. The proof does
not infer big full image from residual surjectivity alone: ordinary
inertia in both regular parameters is also used.

Even this repaired abstract lemma does not identify the resulting
source period factor with eta_p of INTEGRAL_EVALUATION.md. Futterer's
period formulas use his chosen critical motive, beta map, embeddings,
and de Rham bases. The present problem uses the previous return's
specific Gauss frame for D(g)(1). The map between these conventions
is the remaining normalization calculation. Calling both bases
canonical would not establish it.

Kim, arXiv:2203.12157v4, Theorem 7.23 and Proposition 7.24 support the
primitive/optimal modular-symbol normalization at ordinary,
p-distinguished level Np. His comparison with the crystalline
de Rham generator in section 7.9 is made within the paper's good-prime
setting. It cannot simply be substituted for the ramified comparison
in this task. Kato section 17.5 likewise starts with good ordinary
reduction. These references do not license dropping eta_p.

Maksoud's canonical adjoint period/congruence results concern an
adjoint congruence module. This return uses its integral Hida and
period conventions, not an unconstructed map from seed Sha to an
adjoint Selmer group. A unit congruence ideal of the rank-one Hida
algebra does not assert that the standard L-value M_p is a unit.
