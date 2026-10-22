# Cumulative admissible-route constraints

These entries are mandatory checks for future candidate cards.
Each records the failed implication and its boundary. A route is
excluded only when it satisfies the stated hypotheses. No bounded
search failure is a nonexistence theorem.

## FORMULA-side constraints

**F1 — Literal Mellin weight has infinite translation span.**
For nonconstant P, the translated functions
\(P(\log(-ic(z+nw)))\) are linearly independent. Therefore
\(\alpha_f P(\ell)\) is not a fixed coordinate of a finite
constant-matrix coefficient system on a modular curve or finite
cover. Adding finitely many literal coordinates, constant lower
Mellin weights, or changing the logarithm scale does not repair it.
Source: [M2](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md).
Boundary: this is not a statement that its integrated value is not
a period of another object.

**F2 — Finite algebraic exact corrections do not repair F1.**
Finite-rank meromorphic connections on the curve, finite iterated
integrals, finite covers, and algebraic meromorphic frames produce
coefficients with finite-dimensional cusp-translation span. That
class is closed under differentiation. Hence
\(\alpha_f\ell^2=\beta+dG+a\alpha_f+b\alpha_f\ell\) is impossible
when both beta and G belong to that class.
Source: [L3](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/EXACT_CORRECTION_OBSTRUCTION.md).
Boundary: a single-path scalar identity need not imply such a local
identity. Arbitrary analytic primitives exist but carry the same
unproved period difference in their endpoints. A successor must
exhibit a different proved mechanism, not merely a different finite
connection or gauge on the curve.

**F3 — Algebraic Tate-character jets are rigid in this setting.**
An algebraic character over \(\mathbb Q[\epsilon]/(\epsilon^3)\)
reducing to \(t^m\) is exactly \(t^m\). Differentiation of that
algebraic character family cannot produce the desired logarithmic jet.
Source: [M3](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md).
Boundary: \(d-Jdt/t\) is an algebraic logarithm connection on G_m.
The rejected assertion concerns algebraic group characters, not
all Kummer or logarithmic extensions.

**F4 — Ordinary elliptic homology loses this particular path.**
The image of the actual half-ray is a null-homotopic loop in
unpunctured E(C), whereas M1's weighted period is nonzero. No
functional of its ordinary homology class, or reduced flat holonomy
on that loop, recovers the period.
Source: [M4](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md).
Boundary: other paths, punctured curves, and arithmetic realizations
are not excluded by M4 alone; they must still pass F1/F2 if applicable.

**F5 — Full-ray vanishing does not cancel the half-ray first moment.**
\(J_j=(1+(-1)^j)H_j\), so J1=0 imposes no value on H1. Exact
terms on the open half-ray also carry endpoint evaluations.
Source: [L1](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/LOWER_MOMENT_AND_ENDPOINT_GATE.md).
Boundary: H1 for this curve is not asserted nonzero. The false
inference is cancellation from full-ray vanishing alone.

**F6 — Finite local precision does not supply conjugate control.**
Totally positive quadratic algebraic integers can approach 36
arbitrarily closely, match any specified finite p-adic precisions
at selected embeddings, and hide a large second conjugate.
Source: [A2](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/QUANTITATIVE_ALGEBRAICITY_THEOREM.md).
Boundary: these are abstract counterexamples, not BSD quotients.
A degree bound and integrality alone do not replace the quantitative
norm/trace bound for the actual q.

## FIN-side constraints

**N1 — Fixed finite source does not bound distinguished image content.**
The integral maps \(\mathbb Z\to\mathbb Z/p^3,\ n\mapsto p^2n\)
send the primitive source element 1 to a nonzero depth-two element
at every p. No nonzero integer controls those depths at all primes.
Even surjectivity of a whole map says nothing about its value on
a specified source element.
Sources: [C1–C2](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/COUNTEREXAMPLES.md),
[actual homology source](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/HOMOLOGY_SOURCE_THEOREM.md).
Boundary: a proved uniform bound for the evaluated arithmetic image
would supply additional information. Source integrality or a bound
for the whole-map cokernel does not supply it.

**N2 — Profinite perfectness does not imply finite global support.**
For \(R=\prod_p\mathbb Z_p\), the finite free complex
\([R^2\xrightarrow{(pI_2)_p}R^2]\) has finite local cokernels
\((\mathbb Z/p)^2\), with local alternating perfect pairings, and
is rationally acyclic at every p. Its global cokernel is the infinite
product of those groups.
Sources: [C5](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/COUNTEREXAMPLES.md),
[Lemma B](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md).
Boundary: this does not refute a perfect Z-complex with rationally
acyclic cohomology, which does have finite cohomology. Constructing
and arithmetically identifying such a Z-model is the missing input.

**N3 — Pointwise nonvanishing or finiteness does not give finite support.**
The maps in N1 are nonzero at every p but never primitive.
\(\bigoplus_p(\mathbb Z/p)^2\) has finite primary parts and infinitely
many nonzero parts. Thus finite-depth witnesses at each prime do not
imply primitive witnesses outside a finite set.
Sources: [WC section 4](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md),
[ordinary gate](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md).
Boundary: a single nonzero integer with the required valuation bounds
would give finite support; its existence is not proved by these
pointwise statements.

**N4 — Ordinary WC depth zero is a recoding of primary Sha vanishing.**
Under the retained hypotheses, for good ordinary
\(p\notin\{2,3,5,2243,4547,5843\}\),
\(h_p=0\Longleftrightarrow\Sha[p^\infty]=0\).
Consequently eventual depth zero on this ordinary set is exactly
eventual Sha vanishing there.
Source: [O1](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md).
Boundary: do not upgrade this to a converse at positive depth for
the exact Ota-admissible prime set, to the supersingular tail, or
to \(J_E\ne0\Longleftrightarrow\mathrm{FIN}\) globally. Those broader
claims were not established. A new method for the equivalent
primitive condition would be needed to justify substantial work.

**N5 — Finite tame levels cover only finitely many primes.**
For finite G, its exponent kills every positive augmentation graded
quotient. A finite list of levels therefore has zero such quotients
at all but finitely many primes.
Sources: [Lemma A](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md),
[C7](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/COUNTEREXAMPLES.md).
Boundary: completion can change the answer. This is not a ban on
inverse limits, whose global arithmetic comparisons remain to prove.

## Constraints joining the two endpoints

**B1 — FIN does not determine order nine.**
With the retained primary imports and alternating-pairing argument,
FIN permits \(\#\Sha=9t^2\), with \(\gcd(t,30)=1\).
The extra factor cannot be deleted without a theorem.
Source: [Lemma H](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md).
In particular q=36 alone closes neither FIN nor full FORMULA.
Preserve the p=3 provenance qualifications attached to this import.

**B2 — A common certificate requires independent interfaces.**
Setting \(B=q/4\) proves neither rationality nor any Sha bound;
setting \(B=\#\Sha\) presupposes FIN. A determinant line without
its distinguished element and comparisons gives neither interface.
Source: [exact common-B contract](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/COMMON_B_THEOREM_SPECIFICATION.md).
Boundary: the architecture is not impossible. Its bare numerical
existence is equivalent to the remaining endpoint under the retained
data; an independently constructed object and new comparison theorems
could still constitute a useful method. See G1 in the difficulty gate.

**B3 — A known zero central value cannot simply be differentiated
into leading-term arithmeticity.**
The analytic family \(c(s-1)^2\) has the same double zero and even
symmetry for arbitrary c. Algebraicity of a zero value and the
functional equation do not control its second derivative.
Source: [Lemma G](/Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md).
Boundary: this is an abstract counterexample to an inference, not
a modular L-function counterexample or exclusion of a genuine
arithmetic family theorem.

## Custody and use

Earlier proof statements were read at the paths above. The old
arithmetic input theorems and numerical certificates were not
independently replayed. Source hashes and precise read scopes are
recorded in SOURCE_INDEX.md and SOURCE_SNAPSHOT.json.

For every rejected future proposal, cite a register entry or add
a proved, scoped entry before suggesting a successor. Keep a
mathematical disproof distinct from “no applicable theorem supplied.”
The present task adds F2 and F5 and consolidates the retained
constraints. It does not prove common-B impossible.

The [coverage addendum](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/ALBERTSON_COVERAGE_GATE.md)
also prevents relabelling the support problem as a purported
finite/uniform reduction: the reduction and uniform input must
actually be proved. Replacing p by 1/p alone supplies neither.
