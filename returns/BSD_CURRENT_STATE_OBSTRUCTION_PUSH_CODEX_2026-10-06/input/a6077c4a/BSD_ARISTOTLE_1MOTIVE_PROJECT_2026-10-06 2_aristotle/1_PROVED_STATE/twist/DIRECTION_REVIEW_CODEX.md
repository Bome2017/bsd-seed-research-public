# Pro's direction assessment: checked against the two returns

Status: **ASSESSMENT_CONFIRMED_WITH_CORRECTIONS_AND_ORDINARY_CRITERION_MATCHED**.
Date: 2026-10-06. Scope: the two supplied Aristotle archives, Pro's pasted assessment, and the supplied jet-progress transcript. This is not a live inspection of running Aristotle jobs, a full audit of every new norm sequence, or a fresh Lean replay.

Pro's main recommendation is sound: stop re-proving receiver exactness; retain the smaller-field reduction; require actual seed source arithmetic from the constructor experiments. The returns do not yet give an independent upper bound. An independently obtained bound on the smaller class group would still be useful: identifying a receiver with a Selmer group does not make every possible estimate circular.

I checked the specific theorem reference Pro identified, matched its ordinary hypotheses to the seed, verified the finite-batch congruence repair, and found an additional prime-power error in the Heegner index. No new primary vanishing or uniform bound follows from these checks.

## 1. Accepted comparison versus the new tasks

The preceding completed review gives B_p ≅ Sha[p] for every p ≥ 5 under the retained global inputs, including 4547. Its pinned report is [the global-exactness review](https://github.com/Bome2017/bsd-seed-lab/blob/cf8d444a968de4841378fa3c1f8aa5d3b424ae5a/work/returns/BSD_RECEIVER_GLOBAL_EXACTNESS_REVIEW_CODEX_2026-10-06/REPORT.md). This review imports that result; it does not repeat it.

For the smaller field in COINVARIANT_DESCENT.md, the stated local domain remains p ≥ 5, p ≠ 4547. Write s = dim Sha[p] and e = dim loc_p Sel_p. The return's strict-Selmer identification gives

    h_p = 2 + s - e,       e ∈ {0,1}.

With the separately retained evenness of s, h_p ≤ 2 is equivalent to s = 0: if s = 0 then h_p is 1 or 2; if s ≥ 2 then h_p ≥ 3. This deduction does not assume a rational basis point is locally primitive.

Thus Pro's proposed smaller-field target is correct under the return's identification. It is not a bound proved by the norm sequence. I have checked this implication and read the sequence derivation; I have not independently re-proved its entire S-unit/knot-group analysis or rebuilt Coinvariant/Descent.lean. Keep that distinction if the return is cited.

## 2. Heegner: the ordinary theorem application can be made explicit

Wei Zhang's *Selmer groups and the indivisibility of Heegner points*, §8.2 Lemma 8.4, gives the residual eigenspace dimensions used in the return. Its standing notation requires ordinary p, and §8.2 imports Hypothesis ♥. The derived-point construction and sign are in §3.7, equations (3.21)–(3.24). Hypothesis ♥ is on printed p.13; Lemma 5.1(2) handles additive places. [Author PDF](https://math.mit.edu/~wz2113/math/online/Kconj.pdf).

For this seed, those hypotheses match on

    p ≥ 5, p ∤ 23N, p good ordinary,

using the retained residual surjectivity and minimal local data. Indeed K = Q(sqrt(-23)) splits every prime of N, so N− = 1 and N+ = N. The multiplicative primes are 3, 2243, 5843, with minimal discriminant valuations 2, 1, 2. None is divisible by such a p, so the Tate-curve inertia action is nontrivial at all three. There are at least two such split multiplicative primes. The additive places 2 and 4547 satisfy the finite-coefficient condition in the cited lemma. There is no squarefree-N requirement that would eliminate this ordinary seed application.

Use the genuine Heegner system and the optimal quotient, or a primitively normalized parametrization differing by a prime-to-p isogeny; an arbitrary p-multiple of a parametrization is not silently substituted. With the source's normalization, the return's P_ell is the derived point in §3.7, up to the harmless derivative convention: summing i sigma^i from i=1 to m instead of i=0 to m−1 adds m times the identity, since sigma^m=1. Its effect vanishes modulo every eligible p|m.

The resulting implication is:

    ell inert in K, ell ∤ 23Np,
    p | gcd(a_ell, ell+1), P_ell ∉ pE(H_ell)
        ==> Sha(E/Q)[p] = 0.

Here is the derivation, retaining the seed's analytic-rank and Gross–Zagier inputs. The initial traced Heegner point y_K is torsion because L′(E/K,1)=0. Its residual Kummer class is zero (the retained full image excludes p-torsion over K). Nondivisibility of P_ell gives a nonzero class of length one, so the first nonzero residual length is exactly one. The seed has root number +1; the source sign is therefore +1 at length one. The cited lemma gives dimension two in that eigenspace. Restriction identifies it with Sel_p(E/Q), and the known rank-two point space exhausts it.

This checks the ordinary criterion at retained-input/imported-theorem grade. It does not compute P_ell. The independent point count a_53 = −6, for example, verifies that p=53 is ordinary; it does not prove the desired nondivisibility of P_3391.

The supersingular extension remains unauthenticated by the references checked. Kim's Theorem 1.1 assumes semistability in the supersingular case; this curve has additive places. That is a scope limitation of this citation, not a refutation of a more general criterion. [Kim, arXiv:2609.15328, Theorem 1.1](https://arxiv.org/pdf/2609.15328).

## 3. Pro's finite-batch repair is valid

Let m=ell+1 and M_ell=gcd(a_ell,m). From the retained norm relation and the integral derivative identity,

    (sigma−1) D_ell y_ell = m y_ell − a_ell y_1.

Both terms vanish modulo M_ell. Consequently exact a_ell=0 is unnecessary for defining the common residual derived-point classes at the prime factors of M_ell. Summing over the class-group representatives gives the usual invariant class. This repairs the trace objection in the original return.

For any prescribed finite batch of eligible coefficient primes with squarefree product M, use the actual complex-conjugation element in Gal(K(E[M])/Q). Its image on E[p] has trace zero and determinant −1 at each p|M, and its image on K is nontrivial. Chebotarev then gives infinitely many good inert ell with

    a_ell ≡ 0 (mod M),     ell ≡ −1 (mod M).

No assertion of independence between the different residual fields is needed. Their joint complex-conjugation element already exists.

This supplies simultaneous auxiliary eligibility, not simultaneous point indivisibility. Each finite batch can use a new point P_ell; that does not produce one fixed index with finite prime support, nor a uniform estimate on the changing points. Do not turn finite-batch eligibility into a cofinite theorem.

## 4. An additional correction: remove prime powers correctly

The return defines iota(ell) as the squarefree product of primes at which P_ell is divisible, then claims every eligible prime dividing (ell+1)/iota(ell) is settled. This is false when a failing prime occurs to higher power in ell+1. For example, m=50 and failure index 5 leave quotient 10, which still contains the failed prime 5. This is an arithmetic countercontrol, not a claim about an actual derived point.

Correct the statement by using sets of primes, or put

    U_ell = product of the eligible distinct prime divisors of M_ell,
    I_ell = product of those p|U_ell for which P_ell ∈ pE(H_ell).

Then only primes dividing U_ell/I_ell are certified by the criterion. Equivalently, remove the full p-adic power of every excluded or failed prime from the original modulus. This same repair applies to the bad-prime filtering error Pro identified.

The original height result also needs its written hypotheses preserved: trace zero, non-torsion input, and for the summed P_ell its stated group-splitting and non-torsion traced-point conditions. It rejects the tested comparison h(P_ell)/p² < minimum positive height. It does not exclude heights combined with an independently authenticated lattice or bounded search. No practical implementation of those alternatives is supplied here.

## 5. Jet source: Pro identifies a real certificate gap

The pasted elimination code stores pivot rows but not their expressions in the original rows. It can report proportional reduced vectors without delivering the requested independently recombinable multipliers. The transcript contains useful calibration, but no authenticated seed source value is supplied in these two archives. Its later seed attempt is a progress report, not a completed return I can replay.

The next certificate must retain the source rows and their multipliers. In homogeneous notation the appropriate identity is

    lambda J = v − c nu,
    J Phi = 0, nu(Phi) = 1  ==>  v(Phi) = c.

By contrast lambda J=v alone proves v(Phi)=0 for a homogeneous system. If an inhomogeneous jet system J Phi=b is used, give that right-hand side and evaluate lambda b. Specify the coefficient ring and all precision levels; field elimination modulo p does not automatically prove an identity modulo p^4.

The independent checker must regenerate seed row identifiers, action/Hecke matrices, eigenvalue-derivative terms and the normalization, then check equality on every column, including the boundary. A nonzero c establishes the intended arithmetic value only after the source, integral normalization and target functional are matched. A failed finite support is not a theorem that no sparse certificate exists. Neither full-space size nor success at small levels settles that question.

## 6. What I would carry forward

1. Treat full receiver exactness as fixed. Preserve the smaller-field target for any future independent arithmetic estimate; do not assign another repetition of the norm sequences.
2. Let the source-constructor attempt be judged by an actual seed relation/value certificate with the above provenance. This tests a missing arithmetic operation. Even success at one prime would not by itself prove uniform FIN.
3. For the Heegner lane, use the corrected ordinary criterion and common-modulus construction. The next arithmetic deliverable would be a certified reduction/evaluation of the genuine P_ell, or a proved identity controlling its divisibility. Auxiliary enumeration alone is not that deliverable. Require a costed, concrete evaluation method before commissioning a large seed computation.

These are the next admissible outputs, not an authorization to launch jobs and not a claim that either constructor is already feasible at this conductor. Neither archive currently provides the cross-prime indivisibility estimate or seed source certificate needed to close the uniform step. FIN, ORDER9 and Q36 remain unchanged.

## 7. Evidence and custody

The independent checker uses the minimal seed equation, whereas the supplied auxiliary counter uses the original equation. All 30 listed primes pass primality, inertness, point count a_ell=0, and factorization checks. The list's completeness below 100000 was not re-tested. Group-ring coefficient identities were checked for m=2,…,100; the dimension and prime-power controls are algebraic controls, not seed Sha computations.

The Heegner current manifests verify 26/26 and 22/22. The coinvariant root manifest is inherited: 62/63 entries match; STATE.json has changed, and COINVARIANT_DESCENT.md and Coinvariant/Descent.lean are not covered by it. The received bytes are freshly bound here rather than pretending the inherited manifest certifies the continuation. Historical task manifests are preserved as historical receipts, not claimed to validate the new return. This assessment does not re-extract or read the nested 5180-file corpus, and does not re-run Lean.

Archive hashes, all member hashes, selected evidence, the reproducible checker and its results accompany this report. Publication preserves custody; it does not upgrade the mathematics. No remote job was launched, interrupted, or messaged.
